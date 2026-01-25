# Quiz Citation Schema Specification

> **Version**: See package.json <!-- SSoT-OK -->
> **Status**: Draft
> **Purpose**: Machine-readable quiz format with embedded authoritative citations

## Overview

This schema extends the base quiz JSON format to include authoritative references for every question and answer. Each citation includes:

- Source URL
- Exact quoted text from the source
- Authority level (Tier 1-3)

## Schema Definition

### Quiz Document Structure

```json
{
  "$schema": "./quiz-citation-schema.json",
  "title": "string",
  "description": "string",
  "version": "semver",
  "isQuiz": true,
  "domain": "string",
  "weight": "0.0-1.0",
  "authorityPolicy": {
    "minimumTier": 1,
    "requireQuotedText": true,
    "lastValidated": "ISO-8601 date"
  },
  "questions": [Question]
}
```

### Question Structure (Extended)

```json
{
  "questionNumber": 0,
  "questionText": "string",
  "type": "multiple_choice | short_answer | multi_select",
  "required": true,
  "options": ["string"],
  "correctAnswerIndex": 0,
  "correctAnswer": "string",
  "explanation": "string",

  "citations": {
    "question": [Citation],
    "correctAnswer": [Citation],
    "incorrectOptions": {
      "0": [Citation],
      "1": [Citation],
      "2": [Citation]
    }
  }
}
```

### Citation Structure

```json
{
  "source": {
    "type": "documentation | api | adr | blog | official",
    "title": "Human-readable source name",
    "url": "https://... or file://~/.claude/...",
    "onlineUrl": "https://... (optional, for public review page)",
    "section": "Optional: specific section heading",
    "accessDate": "ISO-8601 date"
  },
  "authority": {
    "tier": 1,
    "organization": "Anthropic | cc-skills | Community",
    "confidence": "0.0-1.0"
  },
  "quotedText": "Exact text from source that validates this answer",
  "context": "Optional: surrounding context for the quote"
}
```

### Dual URL Support

| Field       | Required | Description                                             |
| ----------- | -------- | ------------------------------------------------------- |
| `url`       | Yes      | Primary URL (local `file://` or online `https://`)      |
| `onlineUrl` | No       | Public HTTPS URL for review page (clickable hyperlinks) |

**Rendering rules:**

- If `onlineUrl` present: Review page renders as clickable link
- If only `url`: Review page renders as code block (not clickable)

## Authority Tiers

| Tier  | Description                      | Examples                                      |
| ----- | -------------------------------- | --------------------------------------------- |
| **1** | Official Anthropic documentation | docs.anthropic.com, claude.ai/docs            |
| **2** | Verified internal documentation  | cc-skills ADRs, ~/.claude/docs/, hooks schema |
| **3** | Community/blog sources           | Blog posts, GitHub issues, tutorials          |

## Example: Fully Cited Question

```json
{
  "questionNumber": 0,
  "questionText": "Which tool should you use to read the contents of a file in Claude Code?",
  "type": "multiple_choice",
  "required": true,
  "options": ["Read tool", "cat command via Bash", "Open tool", "File tool"],
  "correctAnswerIndex": 0,
  "correctAnswer": "Read tool",
  "explanation": "The Read tool is the dedicated file reading tool in Claude Code. Using Bash with cat is discouraged.",

  "citations": {
    "correctAnswer": [
      {
        "source": {
          "type": "documentation",
          "title": "Claude Code Tool Reference - Read",
          "url": "file://~/.claude/docs/tools/read.md",
          "section": "Overview",
          "accessDate": "2026-01-22"
        },
        "authority": {
          "tier": 2,
          "organization": "cc-skills",
          "confidence": 0.95
        },
        "quotedText": "Reads a file from the local filesystem. You can access any file directly by using this tool.",
        "context": "Tool description from function schema"
      }
    ],
    "incorrectOptions": {
      "1": [
        {
          "source": {
            "type": "documentation",
            "title": "Bash Tool Usage Policy",
            "url": "file://~/.claude/docs/tools/bash.md",
            "section": "When NOT to use Bash",
            "accessDate": "2026-01-22"
          },
          "authority": {
            "tier": 2,
            "organization": "cc-skills",
            "confidence": 0.9
          },
          "quotedText": "Avoid using Bash with the find, grep, cat, head, tail, sed, awk, or echo commands... Instead, always prefer using the dedicated tools for these commands: Read files: Use Read (NOT cat/head/tail)",
          "context": "Explicit policy against using cat via Bash"
        }
      ]
    }
  }
}
```

## Validation Rules

1. **Every question MUST have at least one citation for the correct answer**
2. **Citations MUST include `quotedText`** - exact text from source
3. **URLs MUST be accessible** - file:// for local docs, https:// for web
4. **Authority tier MUST be specified** (1, 2, or 3)
5. **accessDate MUST be within 90 days** or marked stale

## File Organization

```
quiz-data/
├── schema/
│   └── quiz-citation-schema.json    # JSON Schema for validation
├── references/
│   ├── tool-references.md           # Consolidated tool documentation excerpts
│   ├── hooks-references.md          # Hooks documentation excerpts
│   └── best-practices-references.md # Best practices excerpts
├── claude-code-basics.json          # Quiz with embedded citations
├── agentic-workflows.json
├── best-practices.json
├── error-handling-safety.json
└── hooks-lifecycle.json             # NEW: Hooks domain quiz
```

## Mise Tasks

```toml
[tasks."quiz:validate-citations"]
description = "Validate all quiz citations are present and accessible"
run = "uv run scripts/validate-citations.py"
sources = ["quiz-data/*.json"]
outputs = ["logs/citation-validation.log"]

[tasks."quiz:refresh-citations"]
description = "Update citation accessDate and verify quotedText"
run = "uv run scripts/refresh-citations.py"
depends = ["quiz:validate-citations"]
```

## Migration Path

1. **Phase 1**: Add citations to existing 40 questions (prioritize Tier 1-2 sources)
2. **Phase 2**: Create hooks-lifecycle.json with full citations
3. **Phase 3**: Build automated citation validation tooling
4. **Phase 4**: Web scraping for Tier 1 sources (Anthropic docs)

## Related Documents

- [Quiz JSON Schema](./quiz-json-schema.json) - Base schema without citations
- [Authority Sources Index](./authority-sources-index.md) - Master list of valid sources
- [Citation Extraction Guide](./citation-extraction-guide.md) - How to extract quotes
