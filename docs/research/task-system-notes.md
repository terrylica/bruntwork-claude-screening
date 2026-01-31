# Claude Code Task System Research Notes

**Research Date**: 2026-01-30
**Status**: Active feature, replaces TodoWrite/TodoRead

<!-- SSoT-OK: External Claude Code version references, not this package -->

---

## Overview

The Task System is Claude Code's new project management interface, replacing the legacy TodoWrite/TodoRead tools. It provides dependency tracking, cross-session persistence, and visibility into agent work.

## How to Invoke

| Method   | Description                                                      |
| -------- | ---------------------------------------------------------------- |
| `Ctrl+T` | Toggle task list view (shows up to 10 tasks)                     |
| `/tasks` | List and manage background tasks                                 |
| `/todos` | Legacy interface (disable with `CLAUDE_CODE_ENABLE_TASKS=false`) |

## Available Tools

| Tool         | Purpose                                                |
| ------------ | ------------------------------------------------------ |
| `TaskCreate` | Create new tasks with subject, description, activeForm |
| `TaskUpdate` | Modify status, add dependencies, delete tasks          |
| `TaskList`   | List all tasks with summary view                       |
| `TaskGet`    | Get full task details by ID                            |

## TaskCreate Best Practices

| Field         | Format             | Example                                      |
| ------------- | ------------------ | -------------------------------------------- |
| `subject`     | Imperative verb    | "Add validation to login form"               |
| `activeForm`  | Present continuous | "Adding validation to login form"            |
| `description` | Detailed context   | Acceptance criteria, file paths, constraints |

**Why the distinction**: `subject` is the permanent label, `activeForm` appears in the spinner while the task is `in_progress`.

## Task Dependencies

Tasks can block other tasks using the `blockedBy` field:

```json
{
  "taskId": "2",
  "addBlockedBy": ["1"] // Task 2 cannot start until Task 1 completes
}
```

**Auto-unblocking**: When a blocking task is marked `completed`, dependent tasks automatically become available.

## Cross-Session Task Sharing

Share task lists across multiple Claude Code sessions:

```bash
CLAUDE_CODE_TASK_LIST_ID=my-project claude
```

**Storage Location**: `~/.claude/tasks/{sessionId}/*.json`

## Status Workflow

```
pending → in_progress → completed
              ↓
           deleted (permanent removal)
```

## When to Use Tasks

**Use Tasks For**:

- Multi-step implementation projects (3+ distinct steps)
- Complex refactoring with dependencies
- Plan mode workflow tracking
- Cross-session continuity needs

**Do NOT Use Tasks For**:

- Single trivial fixes (typos, one-line changes)
- Pure research/exploration (use Explore agent instead)
- Tasks completable in < 3 steps

## Configuration

| Variable                   | Default          | Description                 |
| -------------------------- | ---------------- | --------------------------- |
| `CLAUDE_CODE_ENABLE_TASKS` | `true`           | Enable/disable task system  |
| `CLAUDE_CODE_TASK_LIST_ID` | session-specific | Share tasks across sessions |

## Version History

| Version | Change                                                             |
| ------- | ------------------------------------------------------------------ |
| 2.1.16  | Introduced Task System (TaskCreate, TaskUpdate, TaskList, TaskGet) |
| 2.1.20  | Added ability to delete tasks via TaskUpdate `status: "deleted"`   |
| 2.1.21  | Fixed task IDs potentially being reused after deletion             |

## Sources

- [Claude Code Interactive Mode](https://code.claude.com/docs/en/interactive-mode) - Official docs
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference) - Command reference
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog) - Version history
