# Quiz Consolidation to Principle-Based Assessments (v2.0)

## Status

**Accepted** (2026-01-25)

## Context

The original quiz structure (6 files, 72 questions) focused heavily on tool-specific knowledge:

- "Which tool should you use to read files?"
- "What is the correct way to search for files by name pattern?"
- "When searching for text content, which tool should you use?"

**Problem**: Claude Code v2.1+ autonomously selects tools based on context. Per [Anthropic's official documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices):

> "Claude 4.5 models demonstrate significantly improved native subagent orchestration capabilities. These models can recognize when tasks would benefit from delegating work to specialized subagents and do so proactively without requiring explicit instruction."

Teaching users "which tool to use" is now obsolete - Claude decides autonomously. The questions were testing implementation details rather than principles that matter for effective Claude Code usage.

## Decision

Consolidate 6 quiz files (72 questions) into 4 principle-based assessments (46 questions):

### Removed Files (Legacy Tool-Focused)

- `claude-code-basics.json` - Tool selection micromanagement
- `agentic-workflows.json` - Internal tool orchestration details
- `best-practices.json` - Mixed useful/obsolete content
- `error-handling-safety.json` - Merged into safety-autonomy.json

### New Structure

| File                       | Domain                | Questions | Focus                                         |
| -------------------------- | --------------------- | --------- | --------------------------------------------- |
| `effective-prompting.json` | Prompting & Context   | 10        | CLAUDE.md, clear instructions, vibe coding    |
| `safety-autonomy.json`     | Safety & Control      | 10        | Permissions, destructive ops, autonomy levels |
| `agents-deep-dive.json`    | Advanced Architecture | 16        | Skills vs subagents, context gatekeeping      |
| `hooks-lifecycle.json`     | Hooks & Automation    | 10        | Exit codes, blocking, visibility patterns     |

### Guiding Principles

1. **Test principles, not tool selection** - Users describe WHAT, Claude decides HOW
2. **Focus on context clarity** - CLAUDE.md, clear prompts, verification methods
3. **Teach safety boundaries** - Permissions, destructive operations, autonomy levels
4. **Architecture for advanced users** - Skills vs subagents, simplicity principle
5. **Hooks for power users** - Deterministic control layer

## Consequences

### Positive

- Questions remain valid as Claude Code evolves (not tied to tool names/counts)
- Teaches users the RIGHT mental model (describe outcomes, not methods)
- Aligns with official Anthropic best practices documentation
- Reduced maintenance burden (46 vs 72 questions)

### Negative

- Existing Google Forms must be recreated
- Users familiar with old structure need reorientation
- Some detailed tool knowledge is no longer assessed

### Neutral

- Citation schema unchanged (still Tier 1/2/3 with quotedText)
- Review page regenerates automatically from new files

## References

- [Claude 4.x Prompting Best Practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices)
- [Claude Code Best Practices (Anthropic Engineering)](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Anthropic's Claude Code transforms vibe coding (Axios)](https://www.axios.com/2026/01/07/anthropics-claude-code-vibe-coding)
