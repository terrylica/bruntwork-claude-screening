#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-auth",
#     "google-auth-oauthlib",
#     "google-auth-httplib2",
#     "google-api-python-client",
#     "python-dotenv",
#     "tabulate",
# ]
# ///
"""
Fetch and display responses from Google Forms quizzes.

Usage:
    uv run fetch_responses.py              # Show summary of all forms
    uv run fetch_responses.py --form NAME  # Show responses for specific quiz
    uv run fetch_responses.py --all        # Show all responses in detail
    uv run fetch_responses.py --export     # Export all to CSV files
"""

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tabulate import tabulate

SCRIPT_DIR = Path(__file__).parent
TOKEN_FILE = SCRIPT_DIR / "token.json"
FORMS_FILE = SCRIPT_DIR / "created_forms.json"
EXPORT_DIR = SCRIPT_DIR / "response_exports"

SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/drive",
]


def get_credentials():
    """Load credentials from token.json."""
    if not TOKEN_FILE.exists():
        print("No token.json found. Run create_forms.py first.")
        return None
    return Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)


def load_forms():
    """Load form metadata."""
    if not FORMS_FILE.exists():
        print("No created_forms.json found. Run create_forms.py first.")
        return []
    with open(FORMS_FILE) as f:
        return json.load(f)


def fetch_responses(forms_service, form_id: str) -> list:
    """Fetch all responses for a form."""
    try:
        result = forms_service.forms().responses().list(formId=form_id).execute()
        return result.get("responses", [])
    except HttpError as e:
        print(f"   Could not fetch responses (HTTP {e.resp.status}): {e.reason}")
        return []


def fetch_form_structure(forms_service, form_id: str) -> dict:
    """Fetch form structure to get question titles."""
    try:
        form = forms_service.forms().get(formId=form_id).execute()
        questions = {}
        for item in form.get("items", []):
            if "questionItem" in item:
                q_id = item["questionItem"]["question"].get("questionId")
                if q_id:
                    questions[q_id] = item.get("title", "Unknown")
        return questions
    except HttpError as e:
        print(f"   Could not fetch form structure (HTTP {e.resp.status}): {e.reason}")
        return {}


def summarize_responses(responses: list) -> dict:
    """Create a summary of responses."""
    if not responses:
        return {"count": 0, "latest": None}

    timestamps = []
    for r in responses:
        if "lastSubmittedTime" in r:
            timestamps.append(r["lastSubmittedTime"])

    latest = max(timestamps) if timestamps else None
    return {"count": len(responses), "latest": latest}


def display_summary(forms: list, forms_service):
    """Display summary table of all forms and response counts."""
    print("\n" + "=" * 70)
    print("QUIZ RESPONSE SUMMARY")
    print("=" * 70 + "\n")

    table_data = []
    total_responses = 0

    for form in forms:
        responses = fetch_responses(forms_service, form["formId"])
        summary = summarize_responses(responses)
        total_responses += summary["count"]

        latest_str = "-"
        if summary["latest"]:
            try:
                dt = datetime.fromisoformat(summary["latest"].replace("Z", "+00:00"))
                latest_str = dt.strftime("%Y-%m-%d %H:%M")
            except ValueError:
                latest_str = summary["latest"][:16]

        table_data.append(
            [
                form["title"][:40],
                summary["count"],
                latest_str,
            ]
        )

    print(tabulate(table_data, headers=["Quiz", "Responses", "Latest"], tablefmt="simple"))
    print(f"\nTotal responses across all forms: {total_responses}\n")

    return total_responses


def display_form_responses(form: dict, forms_service):
    """Display detailed responses for a single form."""
    print(f"\n{'=' * 70}")
    print(f"{form['title']}")
    print(f"{'=' * 70}\n")

    questions = fetch_form_structure(forms_service, form["formId"])
    responses = fetch_responses(forms_service, form["formId"])

    if not responses:
        print("   No responses yet.\n")
        return

    for i, response in enumerate(responses, 1):
        print(f"--- Response #{i} ---")
        print(f"Submitted: {response.get('lastSubmittedTime', 'Unknown')}")

        answers = response.get("answers", {})
        for q_id, answer_data in answers.items():
            q_title = questions.get(q_id, q_id)

            # Extract answer text
            text_answers = answer_data.get("textAnswers", {}).get("answers", [])
            answer_texts = [a.get("value", "") for a in text_answers]
            answer_str = ", ".join(answer_texts) if answer_texts else "-"

            # Truncate long answers
            if len(answer_str) > 100:
                answer_str = answer_str[:97] + "..."

            print(f"  {q_title[:40]}: {answer_str}")
        print()


def export_to_csv(forms: list, forms_service):
    """Export all responses to CSV files."""
    EXPORT_DIR.mkdir(exist_ok=True)

    print(f"\nExporting responses to {EXPORT_DIR}/\n")

    for form in forms:
        questions = fetch_form_structure(forms_service, form["formId"])
        responses = fetch_responses(forms_service, form["formId"])

        # Create safe filename from source file
        source = form.get("sourceFile", form["title"])
        filename = source.replace(".json", "-responses.csv")
        filepath = EXPORT_DIR / filename

        if not responses:
            print(f"   [SKIP] {form['title'][:40]}: No responses to export")
            continue

        # Build CSV
        headers = ["Timestamp", "Response ID"]
        q_ids = list(questions.keys())
        headers.extend([questions[q] for q in q_ids])

        rows = []
        for response in responses:
            row = [
                response.get("lastSubmittedTime", ""),
                response.get("responseId", ""),
            ]
            answers = response.get("answers", {})
            for q_id in q_ids:
                answer_data = answers.get(q_id, {})
                text_answers = answer_data.get("textAnswers", {}).get("answers", [])
                answer_texts = [a.get("value", "") for a in text_answers]
                row.append("; ".join(answer_texts))
            rows.append(row)

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)

        print(f"   [OK] {form['title'][:40]}: {len(responses)} responses -> {filename}")

    print(f"\nExport complete: {EXPORT_DIR}/\n")


def main():
    parser = argparse.ArgumentParser(description="Fetch Quiz Form Responses")
    parser.add_argument("--form", help="Show responses for specific quiz (by title substring)")
    parser.add_argument("--all", action="store_true", help="Show all responses in detail")
    parser.add_argument("--export", action="store_true", help="Export all to CSV files")
    args = parser.parse_args()

    creds = get_credentials()
    if not creds:
        return

    forms_service = build("forms", "v1", credentials=creds)
    forms = load_forms()

    if not forms:
        return

    if args.export:
        export_to_csv(forms, forms_service)
    elif args.form:
        # Find matching form
        matching = [f for f in forms if args.form.lower() in f["title"].lower()]
        if not matching:
            print(f"No form found matching '{args.form}'")
            print(f"   Available: {', '.join(f['title'][:30] for f in forms)}")
            return
        for form in matching:
            display_form_responses(form, forms_service)
    elif args.all:
        for form in forms:
            display_form_responses(form, forms_service)
    else:
        display_summary(forms, forms_service)


if __name__ == "__main__":
    main()
