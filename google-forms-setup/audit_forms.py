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
Audit created Google Forms against source quiz JSON files.

Validates:
- Form exists and is accessible
- Question count matches JSON
- Quiz settings are correct
- Generates MASTER-SUMMARY.md report

Usage:
    uv run audit_forms.py           # Audit all forms
    uv run audit_forms.py --verbose # Show detailed differences
"""

import argparse
import json
from datetime import datetime
from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from tabulate import tabulate

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
TOKEN_FILE = SCRIPT_DIR / "token.json"
FORMS_FILE = SCRIPT_DIR / "created_forms.json"
QUIZ_DIR = PROJECT_DIR / "quiz-data"
AUDIT_DIR = SCRIPT_DIR / "audit-reports"

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


def load_created_forms():
    """Load created forms metadata."""
    if not FORMS_FILE.exists():
        print("No created_forms.json found. Run create_forms.py first.")
        return []
    with open(FORMS_FILE) as f:
        return json.load(f)


def load_quiz_json(source_file: str) -> dict | None:
    """Load quiz JSON from source file."""
    quiz_path = QUIZ_DIR / source_file
    if not quiz_path.exists():
        return None
    with open(quiz_path) as f:
        return json.load(f)


def fetch_form_details(forms_service, form_id: str) -> dict | None:
    """Fetch form structure from Google Forms API."""
    from googleapiclient.errors import HttpError

    try:
        return forms_service.forms().get(formId=form_id).execute()
    except HttpError as e:
        print(f"   Could not fetch form (HTTP {e.resp.status}): {e.reason}")
        return None


def audit_form(form_meta: dict, forms_service, verbose: bool = False) -> dict:
    """Audit a single form against its source JSON."""
    result = {
        "title": form_meta["title"],
        "formId": form_meta["formId"],
        "sourceFile": form_meta.get("sourceFile", "unknown"),
        "status": "PASS",
        "issues": [],
    }

    # Load source JSON
    quiz_data = load_quiz_json(result["sourceFile"])
    if not quiz_data:
        result["status"] = "FAIL"
        result["issues"].append(f"Source file not found: {result['sourceFile']}")
        return result

    # Fetch form from API
    form = fetch_form_details(forms_service, form_meta["formId"])
    if not form:
        result["status"] = "FAIL"
        result["issues"].append("Could not access form via API")
        return result

    # Check question count
    form_items = form.get("items", [])
    form_questions = [i for i in form_items if "questionItem" in i]
    expected_count = len(quiz_data.get("questions", []))

    if len(form_questions) != expected_count:
        result["status"] = "WARN"
        result["issues"].append(
            f"Question count mismatch: form has {len(form_questions)}, JSON has {expected_count}"
        )

    # Check quiz mode
    form_info = form.get("info", {})
    settings = form.get("settings", {})
    is_quiz = settings.get("quizSettings", {}).get("isQuiz", False)

    if quiz_data.get("isQuiz", True) and not is_quiz:
        result["status"] = "WARN"
        result["issues"].append("Form is not in quiz mode but JSON specifies isQuiz: true")

    # Check title matches
    if form_info.get("title") != quiz_data.get("title"):
        result["status"] = "WARN"
        result["issues"].append(
            f"Title mismatch: form='{form_info.get('title')}', JSON='{quiz_data.get('title')}'"
        )

    result["questionCount"] = len(form_questions)
    result["expectedCount"] = expected_count
    result["isQuiz"] = is_quiz

    if verbose and result["issues"]:
        print(f"\n   Issues for {result['title']}:")
        for issue in result["issues"]:
            print(f"      - {issue}")

    return result


def generate_summary_report(results: list) -> str:
    """Generate markdown summary report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "# Forms Audit Summary",
        "",
        f"**Generated**: {now}",
        f"**Forms Audited**: {len(results)}",
        "",
        "## Status Overview",
        "",
    ]

    # Status counts
    pass_count = sum(1 for r in results if r["status"] == "PASS")
    warn_count = sum(1 for r in results if r["status"] == "WARN")
    fail_count = sum(1 for r in results if r["status"] == "FAIL")

    lines.append(f"| Status | Count |")
    lines.append(f"| ------ | ----- |")
    lines.append(f"| PASS | {pass_count} |")
    lines.append(f"| WARN | {warn_count} |")
    lines.append(f"| FAIL | {fail_count} |")
    lines.append("")

    # Detailed table
    lines.append("## Form Details")
    lines.append("")
    lines.append("| Form | Source | Questions | Quiz Mode | Status |")
    lines.append("| ---- | ------ | --------- | --------- | ------ |")

    for r in results:
        quiz_mode = "Yes" if r.get("isQuiz") else "No"
        q_count = f"{r.get('questionCount', '?')}/{r.get('expectedCount', '?')}"
        lines.append(
            f"| {r['title'][:40]} | {r['sourceFile']} | {q_count} | {quiz_mode} | {r['status']} |"
        )

    lines.append("")

    # Issues section
    issues_found = [r for r in results if r["issues"]]
    if issues_found:
        lines.append("## Issues Found")
        lines.append("")
        for r in issues_found:
            lines.append(f"### {r['title']}")
            lines.append("")
            for issue in r["issues"]:
                lines.append(f"- {issue}")
            lines.append("")

    # Form URLs
    lines.append("## Form URLs")
    lines.append("")
    lines.append("| Form | Edit URL |")
    lines.append("| ---- | -------- |")
    for r in results:
        edit_url = f"https://docs.google.com/forms/d/{r['formId']}/edit"
        lines.append(f"| {r['title'][:40]} | [Edit]({edit_url}) |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Audit Google Forms against quiz JSON")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output")
    args = parser.parse_args()

    # Load forms metadata
    forms = load_created_forms()
    if not forms:
        return

    # Authenticate
    print("Authenticating...")
    creds = get_credentials()
    if not creds:
        return

    forms_service = build("forms", "v1", credentials=creds)

    # Audit each form
    print(f"\nAuditing {len(forms)} forms...\n")
    results = []

    for form in forms:
        print(f"   Auditing: {form['title'][:50]}...")
        result = audit_form(form, forms_service, verbose=args.verbose)
        results.append(result)

        status_icon = {"PASS": "[OK]", "WARN": "[!]", "FAIL": "[X]"}[result["status"]]
        print(f"      {status_icon} {result['status']}")

    # Display summary table
    print("\n" + "=" * 70)
    print("AUDIT SUMMARY")
    print("=" * 70 + "\n")

    table_data = [
        [r["title"][:40], r["sourceFile"], r["status"], len(r["issues"])]
        for r in results
    ]
    print(tabulate(table_data, headers=["Form", "Source", "Status", "Issues"], tablefmt="simple"))

    # Generate and save report
    AUDIT_DIR.mkdir(exist_ok=True)
    report = generate_summary_report(results)
    report_file = AUDIT_DIR / "MASTER-SUMMARY.md"
    with open(report_file, "w") as f:
        f.write(report)

    print(f"\nReport saved to: {report_file}")

    # Exit code based on results
    if any(r["status"] == "FAIL" for r in results):
        exit(1)


if __name__ == "__main__":
    main()
