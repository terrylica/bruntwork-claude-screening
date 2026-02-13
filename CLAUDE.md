# BruntWork Claude Code VA Screening

**Navigation**: [docs/](docs/CLAUDE.md) | [google-forms-setup/](google-forms-setup/CLAUDE.md) | [scripts/](scripts/CLAUDE.md) | [quiz-data/](quiz-data/CLAUDE.md)

---

## Navigation

| I need to...                       | Go to                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------------- |
| Understand quiz design             | [docs/design/quiz-citation-schema.md](docs/design/quiz-citation-schema.md)   |
| Set up Google Forms API            | [google-forms-setup/CLAUDE.md](google-forms-setup/CLAUDE.md)                 |
| Review architecture decisions      | [docs/adr/](docs/adr/)                                                       |
| Understand automation scripts      | [scripts/CLAUDE.md](scripts/CLAUDE.md)                                       |
| Author or edit quiz questions      | [quiz-data/CLAUDE.md](quiz-data/CLAUDE.md)                                   |
| Find old form IDs / past responses | [google-forms-setup/form-history.json](google-forms-setup/form-history.json) |
| Review quiz answer key             | [docs/review.md](docs/review.md) (GitHub Pages: `./review`)                  |

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

**Known issue**: `mise run` shows a `[hooks.enter]` parse error. Workaround: call `uv run` directly (e.g., `uv run scripts/validate-quiz.py`).

## Directory Structure

```
bruntwork-claude-screening/
├── CLAUDE.md                    ← Hub (this file)
├── mise.toml                    ← Orchestrator: tools + env + tasks
├── package.json                 ← semantic-release config
├── .releaserc.yml               ← Release automation
├── docs/
│   ├── CLAUDE.md                ← Documentation spoke
│   ├── index.md                 ← GitHub Pages landing (assessment links)
│   ├── review.md                ← Generated answer key (89 questions)
│   ├── adr/                     ← Architecture decisions
│   ├── design/                  ← Quiz design specs
│   └── research/                ← Research notes
├── quiz-data/                   ← JSON quiz definitions (89 questions)
│   ├── CLAUDE.md                ← Quiz authoring guide
│   ├── effective-prompting.json ← Prompting & Context (15 Q)
│   ├── safety-autonomy.json     ← Safety & Control (16 Q)
│   ├── agents-deep-dive.json    ← Architecture + Tasks + Skills (29 Q)
│   ├── hooks-lifecycle.json     ← Hooks + Headless mode (17 Q)
│   └── integration-tools.json   ← MCP + Plugins + Agent SDK (12 Q)
├── google-forms-setup/          ← Forms API integration spoke
│   ├── CLAUDE.md                ← Setup guide + archival policy
│   ├── form-history.json        ← Version-controlled form ID archive (SSoT)
│   ├── created_forms.json       ← Current form IDs (gitignored, ephemeral)
│   ├── create_forms.py          ← Form creation
│   ├── audit_forms.py           ← Form auditing
│   ├── fetch_responses.py       ← Response fetching + CSV export
│   ├── add_candidate_fields.py  ← Add Full Name field to forms
│   └── response_exports/        ← CSV exports (gitignored)
├── scripts/                     ← Automation scripts spoke
│   ├── CLAUDE.md                ← Scripts guide
│   ├── validate-quiz.py         ← Pydantic quiz validator
│   ├── validate-citations.py    ← Citation validation
│   └── generate-review-page.py  ← Review page generator
└── logs/                        ← Local logs (gitignored)
```

## Form Archival Policy

**CRITICAL**: Google Forms are CREATED, never deleted. Old forms with candidate responses must remain accessible.

| File                                    | Purpose                                              | Tracked?        |
| --------------------------------------- | ---------------------------------------------------- | --------------- |
| `google-forms-setup/form-history.json`  | All form versions with IDs, dates, candidates (SSoT) | **Yes** (git)   |
| `google-forms-setup/created_forms.json` | Current version's form IDs only                      | No (gitignored) |
| `google-forms-setup/response_exports/`  | CSV exports from `fetch_responses.py`                | No (gitignored) |

**When recreating forms**: Always append a new version entry to `form-history.json` before or after running `create_forms.py`. Record the git commit hash, date, and question counts.

**To find past candidate responses**: Look up the form version in `form-history.json`, use the `editUrl` to access the form in Google, or use `fetch_responses.py` with the old form ID.

→ Deep dive: [google-forms-setup/CLAUDE.md](google-forms-setup/CLAUDE.md)

## Quiz Domains (v2.2)

**Philosophy**: Focus on principles, not tool micromanagement. Claude Code v2.1+ autonomously selects tools - users should describe WHAT they want, not HOW.

| Domain                      | Weight | Questions | Focus Areas                                                      |
| --------------------------- | ------ | --------- | ---------------------------------------------------------------- |
| **Prompting & Context**     | 25%    | 15        | CLAUDE.md, /init, /clear, verification loops, session continuity |
| **Safety & Control**        | 20%    | 16        | Permissions, sandboxing, checkpoints, test manipulation warning  |
| **Advanced Architecture**   | 20%    | 29        | Skills vs subagents, Tasks, spec-based workflow, Writer/Reviewer |
| **Hooks & Automation**      | 15%    | 17        | Hook types, async hooks, timeouts, --allowedTools for CI         |
| **Integration & Workflows** | 20%    | 12        | MCP scopes, prompt injection, Tool Search, plugins, Agent SDK    |

**Total**: 89 questions across 5 assessments

### Citation Schema

All questions include embedded authoritative citations with:

- Source URL and section reference
- Authority tier (1=Official Anthropic, 2=cc-skills, 3=Community)
- Exact quoted text from source
- Access date for validation

→ Deep dive: [docs/design/quiz-citation-schema.md](docs/design/quiz-citation-schema.md)

## Quiz Design Principles

**Avoid ephemeral content in questions.** Questions must remain valid as Claude Code evolves.

| Ephemeral (Avoid)                         | Stable (Preferred)                                 |
| ----------------------------------------- | -------------------------------------------------- |
| "How many hook types does Claude support" | "What is the purpose of hooks"                     |
| "Which 10 hooks can block execution"      | "Which hooks CAN block execution" (list in answer) |
| Specific version numbers                  | "Check `claude --version` for current"             |
| Feature counts that change                | Conceptual understanding of feature purpose        |

**Lessons from deep-dive analysis** (2026-02-13):

| Issue Found                                        | Lesson                                                                              |
| -------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Anthropic docs show multiple valid approaches      | Don't mark one approach as "THE correct way" when docs show alternatives            |
| `additionalContext` vs `decision: block` confusion | Ask about specific behavior ("guarantees acknowledgment"), not vague "sees message" |
| Fabricated changelog citation                      | Always verify quotedText against actual source before committing                    |
| `--prompt` vs `--print` flag name                  | Run `claude --help` to verify CLI flag names, don't rely on memory                  |

→ Deep dive: [quiz-data/CLAUDE.md](quiz-data/CLAUDE.md)

## Workflow Protocol

1. **Design** — Create/edit quiz JSON in `quiz-data/`
2. **Validate** — Run `mise run quiz:validate`
3. **Deploy** — Run `mise run forms:create`
4. **Archive** — Update `google-forms-setup/form-history.json` with new form IDs
5. **Audit** — Review generated forms via audit reports
6. **Iterate** — Update quiz JSON, redeploy (append to form-history.json)

## Key Files

| File                                         | Purpose                                           |
| -------------------------------------------- | ------------------------------------------------- |
| `mise.toml`                                  | Tools + env + task orchestrator (SSoT)            |
| `package.json`                               | semantic-release metadata                         |
| `.releaserc.yml`                             | Release plugin configuration                      |
| `scripts/validate-quiz.py`                   | Pydantic-based quiz validation                    |
| `scripts/validate-citations.py`              | Citation URL/access date validation               |
| `scripts/generate-review-page.py`            | Generates docs/review.md from quiz JSON           |
| `google-forms-setup/create_forms.py`         | Google Forms API integration                      |
| `google-forms-setup/audit_forms.py`          | Audit forms against source JSON                   |
| `google-forms-setup/fetch_responses.py`      | Fetch and export form responses to CSV            |
| `google-forms-setup/add_candidate_fields.py` | Add Full Name field to forms                      |
| `google-forms-setup/form-history.json`       | Version-controlled archive of all form IDs (SSoT) |

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

→ Deep dive: [google-forms-setup/CLAUDE.md](google-forms-setup/CLAUDE.md)

## Local-Only Resources

| Resource        | Location                                | Purpose                       |
| --------------- | --------------------------------------- | ----------------------------- |
| OAuth token     | `google-forms-setup/token.json`         | Cached API auth (gitignored)  |
| Created forms   | `google-forms-setup/created_forms.json` | Current form IDs (gitignored) |
| Form archive    | `google-forms-setup/form-history.json`  | All form versions (tracked)   |
| Response CSVs   | `google-forms-setup/response_exports/`  | Exported candidate data       |
| Validation logs | `logs/quiz-validation.log`              | Validation run history        |

## Related Projects

- [dental-career-opportunities](https://github.com/terrylica/dental-career-opportunities) — Original Google Forms implementation
- [cc-skills](https://github.com/terrylica/cc-skills) — Claude Code skills reference
