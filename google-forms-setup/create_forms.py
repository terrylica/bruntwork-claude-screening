#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-auth",
#     "google-auth-oauthlib",
#     "google-auth-httplib2",
#     "google-api-python-client",
#     "python-dotenv",
# ]
# ///
"""
Create Google Forms from Claude Code quiz JSON files.

Usage:
    uv run create_forms.py [--quiz QUIZ_NAME] [--all]

Credentials are loaded from 1Password via .env references.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Configuration
SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/drive",
]
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
QUIZ_DIR = PROJECT_DIR / "quiz-data"
CREDENTIALS_FILE = SCRIPT_DIR / "credentials.json"
TOKEN_FILE = SCRIPT_DIR / "token.json"

# Load .env
load_dotenv(PROJECT_DIR / ".env")


def get_secret_from_1password(ref: str) -> str:
    """Fetch a secret from 1Password using op CLI."""
    try:
        result = subprocess.run(
            ["op", "read", ref], capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to read from 1Password: {ref}")
        print(f"   Error: {e.stderr}")
        sys.exit(1)


def ensure_credentials():
    """Ensure credentials.json exists, creating from 1Password if needed."""
    client_id_ref = os.getenv("GOOGLE_CLIENT_ID_REF")
    client_secret_ref = os.getenv("GOOGLE_CLIENT_SECRET_REF")
    project_id = os.getenv("GOOGLE_PROJECT_ID", "bruntwork-claude-screening")

    if not client_id_ref or not client_secret_ref:
        print("❌ Missing GOOGLE_CLIENT_ID_REF or GOOGLE_CLIENT_SECRET_REF in .env")
        sys.exit(1)

    print("🔐 Fetching credentials from 1Password...")
    client_id = get_secret_from_1password(client_id_ref)
    client_secret = get_secret_from_1password(client_secret_ref)

    credentials_data = {
        "installed": {
            "client_id": client_id,
            "project_id": project_id,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": client_secret,
            "redirect_uris": ["http://localhost"],
        }
    }

    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(credentials_data, f, indent=2)
    print(f"✓ Created {CREDENTIALS_FILE}")


def get_google_services():
    """Authenticate and return Forms and Drive API services."""
    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                ensure_credentials()
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_FILE), SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    forms_service = build("forms", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    return forms_service, drive_service


def create_form_from_quiz(quiz_data: dict, forms_service, drive_service) -> dict:
    """Create a Google Form from quiz JSON data."""
    title = quiz_data["title"]
    description = quiz_data.get("description", "")

    print(f"📝 Creating form: {title}")

    # Create empty form
    form = {"info": {"title": title, "documentTitle": title}}
    result = forms_service.forms().create(body=form).execute()
    form_id = result["formId"]

    # Build update requests
    requests = []

    # Set description
    if description:
        requests.append(
            {
                "updateFormInfo": {
                    "info": {"description": description},
                    "updateMask": "description",
                }
            }
        )

    # Enable quiz mode if specified
    if quiz_data.get("isQuiz", True):
        requests.append(
            {"updateSettings": {"settings": {"quizSettings": {"isQuiz": True}}}}
        )

    # Add questions
    for i, q in enumerate(quiz_data.get("questions", [])):
        question_request = build_question_request(q, i)
        if question_request:
            requests.append(question_request)

    # Execute batch update
    if requests:
        forms_service.forms().batchUpdate(
            formId=form_id, body={"requests": requests}
        ).execute()

    form_url = f"https://docs.google.com/forms/d/{form_id}/edit"
    responder_url = f"https://docs.google.com/forms/d/{form_id}/viewform"

    print(f"   ✓ Created: {responder_url}")

    return {
        "title": title,
        "formId": form_id,
        "editUrl": form_url,
        "responderUrl": responder_url,
        "questionCount": len(quiz_data.get("questions", [])),
    }


def build_question_request(q: dict, index: int) -> dict | None:
    """Build a createItem request for a question."""
    q_type = q.get("type", "multiple_choice")
    q_text = q.get("questionText", "")
    required = q.get("required", True)

    if q_type == "multiple_choice":
        options = q.get("options", [])
        correct_index = q.get("correctAnswerIndex", 0)

        choices = []
        for i, opt in enumerate(options):
            choice = {"value": opt}
            if i == correct_index:
                choice["isCorrect"] = True
            choices.append(choice)

        return {
            "createItem": {
                "item": {
                    "title": q_text,
                    "questionItem": {
                        "question": {
                            "required": required,
                            "grading": {
                                "pointValue": 1,
                                "correctAnswers": {"answers": [{"value": options[correct_index]}]},
                            },
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": choices,
                            },
                        }
                    },
                },
                "location": {"index": index},
            }
        }

    elif q_type == "short_answer":
        correct_answer = q.get("correctAnswer", "")
        return {
            "createItem": {
                "item": {
                    "title": q_text,
                    "questionItem": {
                        "question": {
                            "required": required,
                            "grading": {
                                "pointValue": 1,
                                "correctAnswers": {"answers": [{"value": correct_answer}]},
                            },
                            "textQuestion": {"paragraph": False},
                        }
                    },
                },
                "location": {"index": index},
            }
        }

    elif q_type == "paragraph":
        return {
            "createItem": {
                "item": {
                    "title": q_text,
                    "questionItem": {
                        "question": {
                            "required": required,
                            "textQuestion": {"paragraph": True},
                        }
                    },
                },
                "location": {"index": index},
            }
        }

    return None


def main():
    parser = argparse.ArgumentParser(description="Create Google Forms from quiz JSON")
    parser.add_argument("--quiz", help="Name of specific quiz to create")
    parser.add_argument("--all", action="store_true", help="Create all quizzes")
    args = parser.parse_args()

    if not args.quiz and not args.all:
        parser.print_help()
        sys.exit(1)

    forms_service, drive_service = get_google_services()

    results = []

    if args.all:
        quiz_files = list(QUIZ_DIR.glob("*.json"))
        print(f"📚 Found {len(quiz_files)} quiz files")
    else:
        quiz_file = QUIZ_DIR / f"{args.quiz}.json"
        if not quiz_file.exists():
            print(f"❌ Quiz not found: {quiz_file}")
            sys.exit(1)
        quiz_files = [quiz_file]

    for quiz_file in quiz_files:
        with open(quiz_file) as f:
            quiz_data = json.load(f)
        result = create_form_from_quiz(quiz_data, forms_service, drive_service)
        result["sourceFile"] = quiz_file.name
        results.append(result)

    # Save results
    output_file = SCRIPT_DIR / "created_forms.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n✓ Results saved to {output_file}")


if __name__ == "__main__":
    main()
