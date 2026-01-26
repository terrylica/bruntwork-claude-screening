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
Add candidate info fields (Name) to all Google Forms.
Email is collected via form settings (must be enabled manually in Google Forms UI).

Position: Remote Vibe Coder - Claude Code CLI for Financial Time Series Forecasting

Usage:
    uv run add_candidate_fields.py           # Add fields to all forms
    uv run add_candidate_fields.py --form X  # Add to specific form
"""

import argparse
import json
from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCRIPT_DIR = Path(__file__).parent
TOKEN_FILE = SCRIPT_DIR / "token.json"
FORMS_FILE = SCRIPT_DIR / "created_forms.json"

SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/drive",
]

def authenticate():
    """Load saved credentials."""
    if not TOKEN_FILE.exists():
        print("No token.json found. Run create_forms.py first.")
        return None
    return Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)


def add_fields_to_form(forms_service, form_id: str, form_title: str) -> bool:
    """Add Name field to the beginning of a form."""
    print(f"\nUpdating: {form_title}")

    # Create request to add Full Name field at the beginning (index 0)
    requests = [
        {
            "createItem": {
                "item": {
                    "title": "Full Name",
                    "description": "Please enter your full name as it appears on your ID.",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "textQuestion": {"paragraph": False},
                        }
                    },
                },
                "location": {"index": 0},
            }
        },
    ]

    try:
        forms_service.forms().batchUpdate(
            formId=form_id, body={"requests": requests}
        ).execute()
        print("   [OK] Added 'Full Name' field")
        return True
    except HttpError as e:
        print(f"   [FAIL] HTTP {e.resp.status}: {e.reason}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Add candidate fields to forms")
    parser.add_argument("--form", help="Update specific form (by title substring)")
    args = parser.parse_args()

    # Load form data
    if not FORMS_FILE.exists():
        print("No created_forms.json found. Run create_forms.py first.")
        return

    with open(FORMS_FILE) as f:
        forms = json.load(f)

    # Authenticate
    print("Authenticating...")
    creds = authenticate()
    if not creds:
        return

    forms_service = build("forms", "v1", credentials=creds)

    # Filter forms if --form specified
    if args.form:
        forms = [f for f in forms if args.form.lower() in f["title"].lower()]
        if not forms:
            print(f"No form found matching '{args.form}'")
            return

    # Update each form
    print(f"\nAdding candidate fields to {len(forms)} forms...")

    success_count = 0
    for form in forms:
        if add_fields_to_form(forms_service, form["formId"], form["title"]):
            success_count += 1

    # Summary
    print("\n" + "=" * 60)
    print(f"Updated {success_count}/{len(forms)} forms")
    print("=" * 60)
    print(
        "\nREMINDER: You still need to manually enable 'Collect email addresses' "
        "in each form's Settings in the Google Forms UI."
    )


if __name__ == "__main__":
    main()
