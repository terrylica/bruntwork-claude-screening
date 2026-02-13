# Documentation Hub

**Navigation**: [← Root](../CLAUDE.md) | [adr/](adr/) | [design/](design/) | [research/](research/)

---

## Overview

Documentation for the BruntWork Claude Code VA Screening system.

## Directory Structure

```
docs/
├── CLAUDE.md                           ← This file (spoke hub)
├── index.md                            ← GitHub Pages landing page (assessment links)
├── review.md                           ← Generated answer key (89 questions)
├── adr/
│   └── 2026-01-25-quiz-consolidation-v2.md  ← v2.0 consolidation decision
├── design/
│   └── quiz-citation-schema.md         ← Citation format specification
└── research/
    ├── task-system-notes.md            ← Task system research
    └── quiz-gap-analysis.md            ← Gap analysis for quiz coverage
```

## Key Documents

| Document                                                  | Purpose                                                       |
| --------------------------------------------------------- | ------------------------------------------------------------- |
| [index.md](index.md)                                      | GitHub Pages landing with current assessment links            |
| [review.md](review.md)                                    | Auto-generated answer key with all 89 questions and citations |
| [quiz-citation-schema.md](design/quiz-citation-schema.md) | Machine-readable quiz format with citations                   |

## GitHub Pages

The site is published at the repository's GitHub Pages URL. Two pages:

| Page    | Path      | Content                                         |
| ------- | --------- | ----------------------------------------------- |
| Landing | `/`       | Assessment table with Google Forms links        |
| Review  | `/review` | Full answer key with explanations and citations |

**To update the landing page**: Edit `docs/index.md` (form URLs, question counts).
**To regenerate the review page**: Run `uv run scripts/generate-review-page.py` (reads from `quiz-data/*.json`).

## Architecture Decision Records

ADRs follow [MADR 4.0](https://adr.github.io/madr/) format with naming convention: `YYYY-MM-DD-slug.md`

| ADR                                                                            | Status   | Decision                                                               |
| ------------------------------------------------------------------------------ | -------- | ---------------------------------------------------------------------- |
| [2026-01-25-quiz-consolidation-v2.md](adr/2026-01-25-quiz-consolidation-v2.md) | Accepted | Consolidated 6 tool-focused quizzes into 4 principle-based assessments |

## Research Notes

| Document                                              | Purpose                                              |
| ----------------------------------------------------- | ---------------------------------------------------- |
| [task-system-notes.md](research/task-system-notes.md) | Claude Code Task system research for quiz questions  |
| [quiz-gap-analysis.md](research/quiz-gap-analysis.md) | Gap analysis identifying missing quiz coverage areas |

## Citation Schema Quick Reference

Quiz questions include embedded authoritative citations:

| Authority Tier | Description             | Examples                                   |
| -------------- | ----------------------- | ------------------------------------------ |
| **Tier 1**     | Official Anthropic docs | docs.anthropic.com, code.claude.com        |
| **Tier 2**     | Verified internal docs  | cc-skills ADRs, ~/.claude/docs/, hooks ref |
| **Tier 3**     | Community sources       | Blog posts, GitHub issues, tutorials       |

→ Full specification: [design/quiz-citation-schema.md](design/quiz-citation-schema.md)

## Related

- [Quiz data](../quiz-data/CLAUDE.md) — JSON quiz definitions
- [Scripts](../scripts/CLAUDE.md) — Validation and generation scripts
- [Root hub](../CLAUDE.md) — Project overview and workflow
