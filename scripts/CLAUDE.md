# Scripts

**Navigation**: [← Root](../CLAUDE.md) | [validate-quiz.py](validate-quiz.py) | [validate-citations.py](validate-citations.py) | [generate-review-page.py](generate-review-page.py)

---

## Overview

Automation scripts for quiz validation, citation verification, and review page generation.

## Directory Structure

```
scripts/
├── CLAUDE.md              ← This file (spoke hub)
├── validate-quiz.py       ← Pydantic-based quiz validator
├── validate-citations.py  ← Citation URL/date validator
└── generate-review-page.py ← Review page generator (docs/review.md)
```

## Available Scripts

### validate-quiz.py

Validates quiz JSON files against the Pydantic schema.

```bash
uv run scripts/validate-quiz.py
```

**Validation checks:**

- Required fields present (title, questions, correctAnswerIndex)
- Option indices within bounds
- Question types are valid (`multiple_choice`, `short_answer`, `paragraph`)
- Weight values between 0.0 and 1.0

**Exit codes:**

- `0` — All quizzes valid
- `1` — Validation errors found

### validate-citations.py

Validates citations in quiz JSON files.

```bash
# Standard mode
uv run scripts/validate-citations.py

# Strict mode (fail on warnings)
uv run scripts/validate-citations.py --strict

# Verbose output
uv run scripts/validate-citations.py -v
```

**Validation checks:**

- All questions have at least one citation for correctAnswer
- All citations have required fields (source, authority, quotedText)
- Authority tiers are valid (1, 2, or 3)
- Access dates are within 90 days (warning if stale)
- File URLs are accessible (file:// protocol)

**Exit codes:**

- `0` — Validation passed
- `1` — Errors found (or warnings in strict mode)

### generate-review-page.py

Generates the `docs/review.md` answer key page from quiz JSON files.

```bash
uv run scripts/generate-review-page.py
```

**What it does:**

- Reads all `quiz-data/*.json` files
- Generates a markdown page with all questions, correct answers, explanations, and citations
- Writes to `docs/review.md` (served as `/review` on GitHub Pages)

**Run this after**: Any change to quiz JSON files (new questions, edited explanations, updated citations).

## Adding New Scripts

1. Create script with `uv` inline dependencies:

   ```python
   #!/usr/bin/env python3
   # /// script
   # requires-python = ">=3.11"
   # dependencies = ["pydantic"]
   # ///
   ```

2. Add mise task in `mise.toml`:

   ```toml
   [tasks."script:name"]
   description = "Description"
   run = "uv run scripts/name.py"
   sources = ["scripts/name.py", "quiz-data/*.json"]
   ```

3. Document in this CLAUDE.md

## Scripts Reference

| Script                    | Purpose                             | mise task                 |
| ------------------------- | ----------------------------------- | ------------------------- |
| `validate-quiz.py`        | Pydantic schema validation          | `quiz:validate`           |
| `validate-citations.py`   | Citation URL and access date checks | `quiz:validate-citations` |
| `generate-review-page.py` | Generate docs/review.md answer key  | _(no mise task yet)_      |

## Related

- [Quiz data](../quiz-data/CLAUDE.md) — JSON quiz definitions
- [Google Forms setup](../google-forms-setup/CLAUDE.md) — Form creation scripts
- [Root hub](../CLAUDE.md) — Project overview and workflow
