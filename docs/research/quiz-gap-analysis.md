# Quiz Coverage Gap Analysis

**Analysis Date**: 2026-01-30
**Current Questions**: 46 across 4 quiz files

---

## Current Coverage Summary

| Quiz File                  | Domain                | Questions | Topics Covered                                          |
| -------------------------- | --------------------- | --------- | ------------------------------------------------------- |
| `effective-prompting.json` | Prompting & Context   | 10        | CLAUDE.md, clear instructions, vibe coding, plan mode   |
| `safety-autonomy.json`     | Safety & Control      | 10        | Permissions, destructive ops, autonomy levels, git safe |
| `agents-deep-dive.json`    | Advanced Architecture | 16        | Skills vs subagents, context gatekeeping, ACI design    |
| `hooks-lifecycle.json`     | Hooks & Automation    | 10        | Exit codes, blocking, lifecycle events, visibility      |

## Identified Gaps (from State-of-the-Art Research)

### Priority 1: High Value for Vibe Coders

| Topic               | Relevance                               | Recommended Location          |
| ------------------- | --------------------------------------- | ----------------------------- |
| **Task System**     | New project management (recent release) | `agents-deep-dive.json`       |
| **Skills/Commands** | Merged in recent release, team sharing  | `agents-deep-dive.json`       |
| **MCP Integration** | External tools, Tool Search             | New: `integration-tools.json` |

### Priority 2: DevOps/Automation Focus

| Topic                  | Relevance                             | Recommended Location          |
| ---------------------- | ------------------------------------- | ----------------------------- |
| **Headless Mode**      | CI/CD automation (`-p` flag)          | `hooks-lifecycle.json`        |
| **Git Worktrees**      | Parallel sessions (Boris workflow)    | New: `integration-tools.json` |
| **Context Management** | `/compact`, `/clear`, window strategy | `effective-prompting.json`    |

### Priority 3: Nice to Have

| Topic                   | Relevance                    | Recommended Location       |
| ----------------------- | ---------------------------- | -------------------------- |
| **Session Persistence** | Cross-session continuity     | `effective-prompting.json` |
| **Plugin Marketplace**  | Installing community plugins | `agents-deep-dive.json`    |

---

## Recommended Approach: Hybrid (Option C)

Based on thematic coherence and minimal file creation:

### Extend Existing Files

1. **agents-deep-dive.json** (+8 questions -> 24 total)
   - Task System: 4 questions (invocation, dependencies, cross-session, when NOT to use)
   - Skills/Commands: 4 questions (merge, precedence, team sharing, project vs global)

2. **hooks-lifecycle.json** (+3 questions -> 13 total)
   - Headless Mode: 3 questions (purpose, `-p` flag, output formats)

3. **effective-prompting.json** (+2 questions -> 12 total)
   - Context Management: 2 questions (`/compact`, context strategies)

### Create New File

1. **integration-tools.json** (NEW, 6 questions)
   - MCP: 3 questions (purpose, Tool Search, security)
   - Git Worktrees: 3 questions (purpose, parallel sessions, CLAUDE.md sharing)

---

## Question Count After Implementation

| Quiz File                  | Current | Added   | Final  |
| -------------------------- | ------- | ------- | ------ |
| `effective-prompting.json` | 10      | +2      | 12     |
| `safety-autonomy.json`     | 10      | 0       | 10     |
| `agents-deep-dive.json`    | 16      | +8      | 24     |
| `hooks-lifecycle.json`     | 10      | +3      | 13     |
| `integration-tools.json`   | 0       | +6      | 6      |
| **TOTAL**                  | **46**  | **+19** | **65** |

---

## Decision Required

**Proceed with Hybrid approach?**

- Extend 3 existing files (agents, hooks, prompting)
- Create 1 new file (integration-tools)
- Total: 65 questions across 5 quizzes

**Alternative**: Add all 19 questions to `agents-deep-dive.json` (35 questions, single file)

---

## Sources for New Questions

| Topic           | Authoritative Source                       |
| --------------- | ------------------------------------------ |
| Task System     | code.claude.com/docs/en/interactive-mode   |
| Skills/Commands | code.claude.com/docs/en/skills             |
| MCP             | docs.anthropic.com/en/docs/claude-code/mcp |
| Headless Mode   | code.claude.com/docs/en/cli-reference      |
| Git Worktrees   | Community (Boris workflow) - Tier 2        |
| Context Mgmt    | code.claude.com/docs/en/interactive-mode   |
