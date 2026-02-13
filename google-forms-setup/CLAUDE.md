# Google Forms Setup

**Navigation**: [← Root](../CLAUDE.md) | [form-history.json](form-history.json) | [create_forms.py](create_forms.py) | [fetch_responses.py](fetch_responses.py)

---

## Overview

Google Forms API integration for creating quiz forms from JSON definitions, fetching candidate responses, and managing form lifecycle.

## Form Archival Policy

**CRITICAL**: Forms are CREATED, never deleted. Old forms contain candidate responses that must remain accessible for cross-referencing.

| File                 | Purpose                                                                     | Tracked?        |
| -------------------- | --------------------------------------------------------------------------- | --------------- |
| `form-history.json`  | All form versions with IDs, dates, candidates (SSoT)                        | **Yes**         |
| `created_forms.json` | Current version's form IDs only (overwritten on each `create_forms.py` run) | No (gitignored) |
| `response_exports/`  | CSV exports from `fetch_responses.py`                                       | No (gitignored) |

**When recreating forms**:

1. Run `create_forms.py` (creates NEW Google Forms, old ones untouched)
2. Append a new version entry to `form-history.json` with: version, date, commit hash, form IDs, question counts
3. Update `docs/index.md` with new form URLs
4. Commit `form-history.json` and `docs/index.md`

**To find past candidate responses**:

1. Open `form-history.json` → find the version when the candidate took the quiz
2. Use the `editUrl` to open the form in Google Forms editor (Responses tab)
3. Or run: `uv run google-forms-setup/fetch_responses.py --export` (fetches from current `created_forms.json`)

## Directory Structure

```
google-forms-setup/
├── CLAUDE.md                 ← This file (spoke hub)
├── form-history.json         ← All form versions archive (SSoT, tracked)
├── created_forms.json        ← Current form IDs (gitignored, ephemeral)
├── create_forms.py           ← Form creation from quiz JSON
├── audit_forms.py            ← Audit forms vs source JSON
├── fetch_responses.py        ← Fetch/export responses to CSV
├── add_candidate_fields.py   ← Add Full Name field to forms
├── remove_role_field.py      ← Remove VA Role field (one-time migration)
├── credentials.json          ← OAuth credentials (gitignored)
├── token.json                ← Cached OAuth token (gitignored)
├── response_exports/         ← CSV exports (gitignored)
└── audit-reports/            ← Validation reports
```

## Quick Start

```bash
# Create all forms (creates NEW forms, never deletes old)
uv run google-forms-setup/create_forms.py --all

# Add candidate info fields
uv run google-forms-setup/add_candidate_fields.py

# Audit forms against source JSON
uv run google-forms-setup/audit_forms.py

# Fetch responses summary
uv run google-forms-setup/fetch_responses.py

# Export responses to CSV
uv run google-forms-setup/fetch_responses.py --export
```

**Note**: `mise run forms:*` commands also work but may show a `[hooks.enter]` parse error from `mise.toml`. The `uv run` commands above bypass this issue.

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
| `mise run` shows `[hooks.enter]` parse error     | Use `uv run` directly instead                          |

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
| `add_candidate_fields.py` | Add Full Name field to forms       | `forms:add-fields`      |

## Related

- [Quiz data files](../quiz-data/CLAUDE.md) — JSON quiz definitions
- [Validation scripts](../scripts/CLAUDE.md) — Quiz and citation validation
- [Root hub](../CLAUDE.md) — Project overview and workflow
