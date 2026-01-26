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
Remove 'VA Role Applying For' field from all Google Forms.

Single position: Remote Vibe Coder - Claude Code CLI for Financial Time Series Forecasting

Usage:
    uv run remove_role_field.py
"""

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


def remove_role_field(forms_service, form_id: str, form_title: str) -> bool:
    """Find and remove 'VA Role Applying For' field from a form."""
    print(f"\nProcessing: {form_title}")

    try:
        # Get form structure
        form = forms_service.forms().get(formId=form_id).execute()
        items = form.get("items", [])

        # Find the VA Role field
        role_item_id = None
        for item in items:
            title = item.get("title", "")
            if "VA Role" in title or "Role Applying" in title:
                role_item_id = item.get("itemId")
                print(f"   Found field: '{title}' (itemId: {role_item_id})")
                break

        if not role_item_id:
            print("   [SKIP] No 'VA Role' field found")
            return True

        # Delete the item
        request = {"requests": [{"deleteItem": {"location": {"index": 1}}}]}

        forms_service.forms().batchUpdate(formId=form_id, body=request).execute()
        print("   [OK] Removed 'VA Role Applying For' field")
        return True

    except HttpError as e:
        print(f"   [FAIL] HTTP {e.resp.status}: {e.reason}")
        return False


def main():
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

    # Update each form
    print(f"\nRemoving 'VA Role' field from {len(forms)} forms...")

    success_count = 0
    for form in forms:
        if remove_role_field(forms_service, form["formId"], form["title"]):
            success_count += 1

    # Summary
    print("\n" + "=" * 60)
    print(f"Updated {success_count}/{len(forms)} forms")
    print("=" * 60)


if __name__ == "__main__":
    main()
