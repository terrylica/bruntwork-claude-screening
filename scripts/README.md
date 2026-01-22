# Scripts

**Navigation**: [← Root](../CLAUDE.md) | [validate-quiz.py](validate-quiz.py) | [validate-citations.py](validate-citations.py)

---

## Overview

Automation scripts for quiz validation and maintenance.

## Directory Structure

```
scripts/
├── README.md              ← This file (spoke hub)
├── validate-quiz.py       ← Pydantic-based quiz validator
└── validate-citations.py  ← Citation URL/date validator
```

## Available Scripts

### validate-quiz.py

Validates quiz JSON files against the Pydantic schema.

```bash
# Via mise task
mise run quiz:validate

# Direct invocation
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
# Via mise task
mise run quiz:validate-citations

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

3. Document in this README

## Scripts Reference

| Script                  | Purpose                             | mise task                 |
| ----------------------- | ----------------------------------- | ------------------------- |
| `validate-quiz.py`      | Pydantic schema validation          | `quiz:validate`           |
| `validate-citations.py` | Citation URL and access date checks | `quiz:validate-citations` |

## Related

- [Quiz data files](../quiz-data/) — JSON quiz definitions
- [Google Forms setup](../google-forms-setup/) — Form creation scripts
