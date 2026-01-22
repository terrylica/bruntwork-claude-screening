# Documentation Hub

**Navigation**: [← Root](../CLAUDE.md) | [adr/](adr/) | [design/](design/)

---

## Overview

Documentation for the BruntWork Claude Code VA Screening system.

## Directory Structure

```
docs/
├── CLAUDE.md          ← This file (spoke hub)
├── adr/               ← Architecture Decision Records
│   └── (ADRs go here)
└── design/
    └── quiz-citation-schema.md  ← Citation format specification
```

## Key Documents

| Document                                                  | Purpose                                     |
| --------------------------------------------------------- | ------------------------------------------- |
| [quiz-citation-schema.md](design/quiz-citation-schema.md) | Machine-readable quiz format with citations |

## Architecture Decision Records

ADRs follow [MADR 4.0](https://adr.github.io/madr/) format with naming convention: `YYYY-MM-DD-slug.md`

| ADR          | Status | Decision |
| ------------ | ------ | -------- |
| _(none yet)_ | -      | -        |

## Citation Schema Quick Reference

Quiz questions include embedded authoritative citations:

| Authority Tier | Description             | Examples                                   |
| -------------- | ----------------------- | ------------------------------------------ |
| **Tier 1**     | Official Anthropic docs | docs.anthropic.com, claude.ai/docs         |
| **Tier 2**     | Verified internal docs  | cc-skills ADRs, ~/.claude/docs/, hooks ref |
| **Tier 3**     | Community sources       | Blog posts, GitHub issues, tutorials       |

→ Full specification: [design/quiz-citation-schema.md](design/quiz-citation-schema.md)
