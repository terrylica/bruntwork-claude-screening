# BruntWork Claude Code VA Screening

**Navigation**: [docs/](docs/CLAUDE.md) | [google-forms-setup/](google-forms-setup/README.md) | [scripts/](scripts/README.md) | [quiz-data/](quiz-data/)

---

## Navigation

| I need to...                  | Go to                                                                      |
| ----------------------------- | -------------------------------------------------------------------------- |
| Understand quiz design        | [docs/design/quiz-citation-schema.md](docs/design/quiz-citation-schema.md) |
| Set up Google Forms API       | [google-forms-setup/README.md](google-forms-setup/README.md)               |
| Review architecture decisions | [docs/adr/](docs/adr/)                                                     |
| Understand automation scripts | [scripts/README.md](scripts/README.md)                                     |
| View quiz JSON files          | [quiz-data/](quiz-data/)                                                   |

---

## Overview

Google Forms-based screening system for BruntWork virtual assistant candidates to assess Claude Code proficiency.

**Stack**: Python (uv) · Bun/TypeScript · Google Forms API · mise (runtimes)
**Pattern**: Polyglot monorepo with semantic versioning

## Quick Reference

| Action               | Command                            |
| -------------------- | ---------------------------------- |
| Create forms         | `mise run forms:create`            |
| Validate quiz data   | `mise run quiz:validate`           |
| Validate citations   | `mise run quiz:validate-citations` |
| Audit forms          | `mise run forms:audit`             |
| Fetch responses      | `mise run forms:fetch-responses`   |
| Add candidate fields | `mise run forms:add-fields`        |
| List quizzes         | `mise run quiz:list`               |
| Release (full)       | `mise run release:full`            |
| Release (dry)        | `mise run release:preflight`       |

## Directory Structure

```
bruntwork-claude-screening/
├── CLAUDE.md                    ← Hub (this file)
├── mise.toml                    ← Orchestrator: tools + env + tasks
├── package.json                 ← semantic-release config
├── .releaserc.yml               ← Release automation
├── docs/
│   ├── CLAUDE.md                ← Documentation spoke
│   ├── adr/                     ← Architecture decisions
│   └── design/                  ← Quiz design specs
├── quiz-data/                   ← JSON quiz definitions (5 files, 50 questions)
│   ├── claude-code-basics.json
│   ├── agentic-workflows.json
│   ├── best-practices.json
│   ├── error-handling-safety.json
│   └── hooks-lifecycle.json
├── google-forms-setup/          ← Forms API integration spoke
│   ├── README.md                ← Setup guide
│   ├── create_forms.py          ← Form creation
│   ├── audit_forms.py           ← Form auditing
│   ├── fetch_responses.py       ← Response fetching
│   ├── add_candidate_fields.py  ← Add Name/Role fields
│   └── audit-reports/           ← Validation reports
├── scripts/                     ← Automation scripts spoke
│   ├── README.md                ← Scripts guide
│   ├── validate-quiz.py         ← Pydantic quiz validator
│   └── validate-citations.py    ← Citation validation
└── logs/                        ← Local logs (gitignored)
```

## Quiz Domains

Assessment covers 6 domains for Claude Code VA proficiency (50 questions total):

| Domain                 | Weight | Questions | Focus Areas                                |
| ---------------------- | ------ | --------- | ------------------------------------------ |
| **Tool Mastery**       | 20%    | 10        | Read, Edit, Write, Bash, Grep, Glob usage  |
| **Agentic Patterns**   | 20%    | 10        | Task delegation, multi-agent coordination  |
| **Error Handling**     | 15%    | 10        | Recovery strategies, debugging workflows   |
| **Best Practices**     | 15%    | 10        | Context management, efficiency patterns    |
| **Safety**             | 10%    | 10        | Sandbox awareness, permission boundaries   |
| **Hooks & Automation** | 20%    | 10        | Lifecycle events, blocking, implementation |

### Citation Schema

All questions include embedded authoritative citations with:

- Source URL and section reference
- Authority tier (1=Official Anthropic, 2=cc-skills, 3=Community)
- Exact quoted text from source
- Access date for validation

→ Deep dive: [docs/design/quiz-citation-schema.md](docs/design/quiz-citation-schema.md)

## Workflow Protocol

1. **Design** — Create quiz JSON in `quiz-data/`
2. **Validate** — Run `mise run quiz:validate`
3. **Deploy** — Run `mise run forms:create`
4. **Audit** — Review generated forms via audit reports
5. **Iterate** — Update quiz JSON, redeploy

## Key Files

| File                                         | Purpose                                |
| -------------------------------------------- | -------------------------------------- |
| `mise.toml`                                  | Tools + env + task orchestrator (SSoT) |
| `package.json`                               | semantic-release metadata              |
| `.releaserc.yml`                             | Release plugin configuration           |
| `scripts/validate-quiz.py`                   | Pydantic-based quiz validation         |
| `scripts/validate-citations.py`              | Citation URL/access date validation    |
| `google-forms-setup/create_forms.py`         | Google Forms API integration           |
| `google-forms-setup/audit_forms.py`          | Audit forms against source JSON        |
| `google-forms-setup/fetch_responses.py`      | Fetch and export form responses        |
| `google-forms-setup/add_candidate_fields.py` | Add Name/Role fields to forms          |

## Link Conventions

| Context          | Format          | Example                               |
| ---------------- | --------------- | ------------------------------------- |
| Same repo        | Relative (`./`) | `[ADR](docs/adr/file.md)`             |
| External repos   | Full URL        | `[cc-skills](https://github.com/...)` |
| Local-only paths | Absolute        | `~/eon/bruntwork-claude-screening/`   |

## Credentials

Google Forms API credentials managed via 1Password:

```bash
# Set in .env (gitignored)
GOOGLE_CLIENT_ID_REF="op://Employee/ptby3smss3sjnod4iacgdnhtoi/username"
GOOGLE_CLIENT_SECRET_REF="op://Employee/ptby3smss3sjnod4iacgdnhtoi/password"
```

**Account**: `usalchemist@gmail.com`
**GCP Project**: `eonlabs-data`

→ Deep dive: [google-forms-setup/README.md](google-forms-setup/README.md)

## Local-Only Resources

| Resource        | Location                                | Purpose                      |
| --------------- | --------------------------------------- | ---------------------------- |
| OAuth token     | `google-forms-setup/token.json`         | Cached API auth (gitignored) |
| Created forms   | `google-forms-setup/created_forms.json` | Form IDs and URLs            |
| Validation logs | `logs/quiz-validation.log`              | Validation run history       |

**Note**: These files are workspace-local and gitignored.

## Related Projects

- [dental-career-opportunities](https://github.com/terrylica/dental-career-opportunities) — Original Google Forms implementation
- [cc-skills](https://github.com/terrylica/cc-skills) — Claude Code skills reference
