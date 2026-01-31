# Quiz Data

**Navigation**: [← Root](../CLAUDE.md) | [docs/design/quiz-citation-schema.md](../docs/design/quiz-citation-schema.md)

---

## Overview

JSON quiz definitions for Claude Code VA screening assessments.

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

### Example Refactoring

**Before** (ephemeral):

```json
{
  "questionText": "How many hook event types does Claude Code support?",
  "options": ["5", "7", "10", "12"],
  "correctAnswer": "10"
}
```

**After** (stable):

```json
{
  "questionText": "What is the primary purpose of Claude Code hooks?",
  "options": [
    "Replace built-in tools",
    "Execute shell commands at lifecycle events for validation and control",
    "Modify Claude's language model",
    "Disable security features"
  ],
  "correctAnswer": "Execute shell commands at lifecycle events for validation and control"
}
```

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
mise run quiz:validate

# Validate citations (URLs, dates)
mise run quiz:validate-citations
```

## Quiz Philosophy (v2.0)

**Focus on principles, not tool micromanagement.** Claude Code v2.1+ autonomously selects tools based on context. Users should describe WHAT they want, not HOW to do it.

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

## Current Quiz Files

| File                       | Domain                  | Questions | Focus                                              |
| -------------------------- | ----------------------- | --------- | -------------------------------------------------- |
| `effective-prompting.json` | Prompting & Context     | 10        | CLAUDE.md, clear instructions, vibe coding         |
| `safety-autonomy.json`     | Safety & Control        | 10        | Permissions, destructive ops, autonomy levels      |
| `agents-deep-dive.json`    | Advanced Architecture   | 24        | Skills vs subagents, Tasks, context gatekeeping    |
| `hooks-lifecycle.json`     | Hooks & Automation      | 13        | Exit codes, blocking, headless mode                |
| `integration-tools.json`   | Integration & Workflows | 6         | MCP, Tool Search, git worktrees, parallel sessions |

## Related

- [Google Forms setup](../google-forms-setup/CLAUDE.md) — Deploy quizzes to Google Forms
- [Validation scripts](../scripts/CLAUDE.md) — Quiz and citation validation
