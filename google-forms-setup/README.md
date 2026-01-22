# Google Forms Setup

**Navigation**: [← Root](../CLAUDE.md) | [create_forms.py](create_forms.py) | [audit_forms.py](audit_forms.py) | [fetch_responses.py](fetch_responses.py) | [audit-reports/](audit-reports/)

---

## Overview

Google Forms API integration for creating quiz forms from JSON definitions.

## Directory Structure

```
google-forms-setup/
├── README.md                 ← This file (spoke hub)
├── create_forms.py           ← Form creation
├── audit_forms.py            ← Audit forms vs source JSON
├── fetch_responses.py        ← Fetch/export responses
├── add_candidate_fields.py   ← Add Name/Role fields
├── credentials.json          ← OAuth credentials (gitignored)
├── token.json                ← Cached OAuth token (gitignored)
├── created_forms.json        ← Form IDs and URLs
├── response_exports/         ← CSV exports (gitignored)
└── audit-reports/            ← Validation reports
```

## Quick Start

```bash
# Create all forms
mise run forms:create --all

# Audit forms against source JSON
mise run forms:audit

# Fetch responses summary
mise run forms:fetch-responses

# Export responses to CSV
uv run google-forms-setup/fetch_responses.py --export

# Add candidate info fields (Name, Role)
mise run forms:add-fields

# List available quizzes
mise run quiz:list
```

## Authentication Setup

### Prerequisites

1. Google Cloud Project with Forms API + Drive API enabled
2. OAuth 2.0 Desktop Client credentials
3. 1Password CLI (`op`) configured

### Credentials

Credentials are stored in 1Password and referenced via `.env`:

```bash
GOOGLE_CLIENT_ID_REF="op://Employee/ptby3smss3sjnod4iacgdnhtoi/username"
GOOGLE_CLIENT_SECRET_REF="op://Employee/ptby3smss3sjnod4iacgdnhtoi/password"
GOOGLE_PROJECT_ID="eonlabs-data"
NOTIFICATION_EMAIL="usalchemist@gmail.com"
```

### First-Time Setup

1. **Create GCP Project** at <https://console.cloud.google.com/>
2. **Enable APIs**: Google Forms API, Google Drive API
3. **Configure OAuth Consent**: Add test user (your email)
4. **Create OAuth Client**: Desktop application type
5. **Store in 1Password**: Client ID as username, Client Secret as password
6. **Update `.env`**: Set 1Password reference paths

### OAuth Flow

On first run:

1. Browser opens for Google OAuth approval
2. Click "Continue" (ignore unverified app warning)
3. Grant Forms and Drive permissions
4. Token cached in `token.json` for future runs

## Troubleshooting

| Error                                            | Solution                                               |
| ------------------------------------------------ | ------------------------------------------------------ |
| "Access blocked: has not completed verification" | Add test user in GCP → Google Auth Platform → Audience |
| "Failed to read from 1Password"                  | Run `op signin` first                                  |
| "Token expired"                                  | Delete `token.json` and re-run                         |
| "credentials.json not found"                     | Check `.env` 1Password references                      |

## API Limitations

- Quiz mode requires `isQuiz: true` in form settings
- Correct answers set via `grading.correctAnswers`, not on options
- `updateMask` required for all `updateSettings` requests

## Scripts Reference

| Script                    | Purpose                            | mise task               |
| ------------------------- | ---------------------------------- | ----------------------- |
| `create_forms.py`         | Create Google Forms from quiz JSON | `forms:create`          |
| `audit_forms.py`          | Validate forms match source JSON   | `forms:audit`           |
| `fetch_responses.py`      | Download/export form responses     | `forms:fetch-responses` |
| `add_candidate_fields.py` | Add Name/Role fields to forms      | `forms:add-fields`      |

## Related

- [Quiz data files](../quiz-data/) — JSON quiz definitions
- [Validation scripts](../scripts/README.md) — Quiz and citation validation
