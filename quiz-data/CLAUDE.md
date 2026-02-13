# Quiz Data

**Navigation**: [← Root](../CLAUDE.md) | [Citation Schema](../docs/design/quiz-citation-schema.md) | [Form History](../google-forms-setup/form-history.json)

---

## Overview

JSON quiz definitions for Claude Code VA screening assessments. Currently 89 questions across 5 domains.

## Quiz Files

| File                       | Domain                  | Questions | Focus                                                      |
| -------------------------- | ----------------------- | --------- | ---------------------------------------------------------- |
| `effective-prompting.json` | Prompting & Context     | 15        | CLAUDE.md, /init, /clear, verification, session continuity |
| `safety-autonomy.json`     | Safety & Control        | 16        | Permissions, sandboxing, checkpoints, test manipulation    |
| `agents-deep-dive.json`    | Advanced Architecture   | 29        | Skills vs subagents, Tasks, spec workflow, Writer/Reviewer |
| `hooks-lifecycle.json`     | Hooks & Automation      | 17        | Hook types, async hooks, timeouts, --allowedTools          |
| `integration-tools.json`   | Integration & Workflows | 12        | MCP scopes, prompt injection, plugins, Agent SDK           |

## Quiz Design Principles

**Avoid ephemeral content.** Questions must remain valid as Claude Code evolves.

### What to Avoid

| Pattern                   | Problem                            | Fix                                   |
| ------------------------- | ---------------------------------- | ------------------------------------- |
| "How many X exist?"       | Counts change with releases        | Ask about purpose or behavior instead |
| Hardcoded version numbers | Versions become outdated           | Reference `claude --version` or omit  |
| "Which N items can do X?" | N changes; list becomes incomplete | List items in answer, not count       |
| Specific feature counts   | Features added/removed over time   | Focus on conceptual understanding     |

### What to Prefer

| Pattern                         | Why It Works                                |
| ------------------------------- | ------------------------------------------- |
| "What is the purpose of X?"     | Purpose rarely changes                      |
| "Which hooks CAN block?" (list) | Answer includes full list, not a count      |
| "How does X work?"              | Behavior is more stable than feature counts |
| "What happens when X fails?"    | Error handling concepts remain stable       |

### Lessons from Deep-Dive Analysis (2026-02-13)

After verifying every wrong answer from two candidates against authoritative sources, these quiz design issues were found and corrected:

| Issue                                                                    | Lesson                                                                              | Fix Applied                                      |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------ |
| Hook script path: both `python3 script.py` and direct path are valid     | Don't mark one approach as "THE correct way" when docs show alternatives            | Replaced with CLAUDE_PROJECT_DIR question        |
| `additionalContext` vs `decision: block` both make Claude "see" messages | Ask about specific behavior ("guarantees acknowledgment"), not vague "sees message" | Rephrased to ask about guaranteed acknowledgment |
| Citation referenced fabricated changelog quote                           | Always verify `quotedText` against actual source URL before committing              | Replaced with settings docs citation             |
| Citation said `--prompt` but flag is `--print`                           | Run `claude --help` to verify CLI flag names                                        | Fixed quotedText                                 |

### Citation Verification Protocol

Before adding or modifying a citation:

1. **Open the source URL** in a browser
2. **Find the exact section** referenced
3. **Verify the `quotedText`** matches (or closely paraphrases) the actual content
4. **Check the access date** is current
5. **Run** `uv run scripts/validate-citations.py` after changes

## File Schema

Each JSON file follows this structure:

```json
{
  "title": "Quiz Title",
  "description": "Quiz description",
  "isQuiz": true,
  "domain": "Domain Name",
  "weight": 0.20,
  "questions": [
    {
      "questionNumber": 0,
      "questionText": "Question text?",
      "type": "multiple_choice",
      "required": true,
      "options": ["A", "B", "C", "D"],
      "correctAnswerIndex": 1,
      "correctAnswer": "B",
      "explanation": "Why B is correct",
      "citations": { ... }
    }
  ]
}
```

## Citation Requirements

Every question must have at least one citation for the correct answer.

| Field        | Required | Description                              |
| ------------ | -------- | ---------------------------------------- |
| `source`     | Yes      | URL, title, section, accessDate          |
| `authority`  | Yes      | tier (1-3), organization, confidence     |
| `quotedText` | Yes      | Exact text from source supporting answer |

→ Full schema: [docs/design/quiz-citation-schema.md](../docs/design/quiz-citation-schema.md)

## Validation

```bash
# Validate all quiz files
uv run scripts/validate-quiz.py

# Validate citations (URLs, dates)
uv run scripts/validate-citations.py

# Regenerate review page after changes
uv run scripts/generate-review-page.py
```

## Quiz Philosophy (v2.0+)

**Focus on principles, not tool micromanagement.** Claude Code autonomously selects tools based on context. Users should describe WHAT they want, not HOW to do it.

### What to Test

| Topic                   | Why It Matters                                       |
| ----------------------- | ---------------------------------------------------- |
| Clear prompting         | Context determines Claude's effectiveness            |
| Safety boundaries       | Permissions, destructive operations, autonomy levels |
| Architecture principles | Skills vs subagents, context gatekeeping, simplicity |
| Hooks (advanced)        | Deterministic control for power users                |

### What NOT to Test

| Topic                     | Why It's Obsolete              |
| ------------------------- | ------------------------------ |
| "Which tool to use for X" | Claude decides autonomously    |
| Tool-specific syntax      | Internal implementation detail |
| Specific command patterns | Changes between versions       |

## Related

- [Google Forms setup](../google-forms-setup/CLAUDE.md) — Deploy quizzes to Google Forms
- [Validation scripts](../scripts/CLAUDE.md) — Quiz and citation validation
- [Form history](../google-forms-setup/form-history.json) — All form versions with candidate data
