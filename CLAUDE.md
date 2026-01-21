# BruntWork Claude Code VA Screening

> **Navigation**: This file is the hub. Each section links to deeper documentation.

## Overview

Google Forms-based screening system for BruntWork virtual assistant candidates to assess Claude Code proficiency.

**Stack**: Python (uv) · Bun/TypeScript · Google Forms API · mise (runtimes)
**Pattern**: Polyglot monorepo with semantic versioning

## Quick Reference

| Action             | Command                      |
| ------------------ | ---------------------------- |
| Create forms       | `mise run forms:create`      |
| Validate quiz data | `mise run quiz:validate`     |
| Release (full)     | `mise run release:full`      |
| Release (dry)      | `mise run release:preflight` |

## Directory Structure

```
bruntwork-claude-screening/
├── CLAUDE.md                    ← Hub (this file)
├── mise.toml                    ← Orchestrator: tools + env vars
├── package.json                 ← semantic-release config
├── .releaserc.yml               ← Release automation
├── docs/
│   ├── adr/                     ← Architecture decisions
│   └── design/                  ← Quiz design specs
├── quiz-data/                   ← JSON quiz definitions
│   ├── claude-code-basics.json
│   ├── tool-usage-patterns.json
│   └── agentic-workflows.json
├── google-forms-setup/          ← Forms API integration
│   ├── create_forms.py          ← Form creation script
│   ├── credentials.json         ← OAuth credentials (gitignored)
│   └── audit-reports/           ← Form validation reports
├── scripts/                     ← Automation scripts
└── logs/                        ← Local logs (gitignored)
```

## Quiz Domains

Assessment covers 5 domains for Claude Code VA proficiency:

| Domain               | Weight | Focus Areas                               |
| -------------------- | ------ | ----------------------------------------- |
| **Tool Mastery**     | 25%    | Read, Edit, Write, Bash, Grep, Glob usage |
| **Agentic Patterns** | 25%    | Task delegation, multi-agent coordination |
| **Error Handling**   | 20%    | Recovery strategies, debugging workflows  |
| **Best Practices**   | 15%    | Context management, efficiency patterns   |
| **Safety**           | 15%    | Sandbox awareness, permission boundaries  |

## Workflow Protocol

1. **Design** — Create quiz JSON in `quiz-data/`
2. **Validate** — Run `mise run quiz:validate`
3. **Deploy** — Run `mise run forms:create`
4. **Audit** — Review generated forms via audit reports
5. **Iterate** — Update quiz JSON, redeploy

## Related Projects

- [dental-career-opportunities](~/459ecs/dental-career-opportunities) — Original Google Forms implementation
- [cc-skills](~/.claude/plugins/marketplaces/cc-skills) — Claude Code skills reference

## Credentials

Google Forms API credentials managed via 1Password:

```bash
# Set in .env (gitignored)
GOOGLE_CLIENT_ID_REF=op://Engineering/google-forms-api/client_id
GOOGLE_CLIENT_SECRET_REF=op://Engineering/google-forms-api/client_secret
```

→ Deep dive: [google-forms-setup/README.md](google-forms-setup/README.md)
