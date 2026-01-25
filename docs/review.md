---
title: Quiz Answer Key & Review
permalink: /review/
toc: true
toc_sticky: true
---

> This page contains all correct answers with explanations and authoritative citations.
> Use this as a learning resource alongside the [assessment quizzes](./).

*Generated: 2026-01-24 22:55*

---

## Statistics

| Metric | Value |
| ------ | ----- |
| Total Questions | 72 |
| Domains | 6 |
| Citation Coverage | 100% |
| Tier 1 (Official) | 38% |
| Tier 2 (Internal) | 62% |
| Tier 3 (Community) | 0% |

---

## Table of Contents

| # | Domain | Questions | Weight | Jump |
| - | ------ | --------- | ------ | ---- |
| 1 | Tool Mastery | 10 | 25% | [Go](#claude-code-basics) |
| 2 | Agentic Patterns | 10 | 25% | [Go](#agentic-workflows) |
| 3 | Best Practices | 10 | 15% | [Go](#best-practices) |
| 4 | Error Handling + Safety | 10 | 35% | [Go](#error-handling-safety) |
| 5 | Hooks & Automation | 10 | 20% | [Go](#hooks-lifecycle) |
| 6 | Advanced Architecture | 22 | 20% | [Go](#agents-deep-dive) |

---

## Claude Code Basics

*Domain: Tool Mastery | Weight: 25%*

### Q1. Which tool should you use to read the contents of a file in Claude Code?

| Option | |
| ------ | --- |
| **A. Read tool** | ✓ |
| B. cat command via Bash | |
| C. Open tool | |
| D. File tool | |

**Explanation**: The Read tool is the dedicated file reading tool in Claude Code. Using Bash with cat is discouraged.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code System Prompt - Tool Usage Policy<br>
<strong>URL</strong>: <code>file://~/.claude/docs/system-prompt-reference.md</code><br>
<strong>Section</strong>: Bash Tool Usage Policy<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Avoid using Bash with the find, grep, cat, head, tail, sed, awk, or echo commands... Read files: Use Read (NOT cat/head/tail)"</blockquote>

</details>

---

### Q2. When you need to make a small change to an existing file, which tool is most appropriate?

| Option | |
| ------ | --- |
| A. Write tool (rewrite entire file) | |
| **B. Edit tool (targeted replacement)** | ✓ |
| C. Bash with sed | |
| D. Create a new file and delete the old one | |

**Explanation**: Edit tool performs targeted string replacements, preserving the rest of the file. More efficient than rewriting.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Edit Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/edit.md</code><br>
<strong>Section</strong>: Description<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Performs exact string replacements in files... Edit files: Use Edit (NOT sed/awk)"</blockquote>

</details>

---

### Q3. Before using the Edit tool on a file, what must you do first?

| Option | |
| ------ | --- |
| A. Nothing, Edit works on any file | |
| B. Run a backup command | |
| **C. Read the file using the Read tool** | ✓ |
| D. Check file permissions | |

**Explanation**: Edit tool requires that you've read the file first in the conversation to ensure you know the current contents.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Edit Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/edit.md</code><br>
<strong>Section</strong>: Usage<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"You must use your Read tool at least once in the conversation before editing. This tool will error if you attempt an edit without reading the file."</blockquote>

</details>

---

### Q4. What is the correct way to search for files by name pattern in Claude Code?

| Option | |
| ------ | --- |
| A. find command via Bash | |
| B. ls command with grep | |
| **C. Glob tool** | ✓ |
| D. Search tool | |

**Explanation**: Glob tool is the dedicated file pattern matching tool. Avoid using find via Bash.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Glob Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/glob.md</code><br>
<strong>Section</strong>: Description<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Fast file pattern matching tool that works with any codebase size... File search: Use Glob (NOT find or ls)"</blockquote>

</details>

---

### Q5. When searching for text content within files, which tool should you use?

| Option | |
| ------ | --- |
| A. grep command via Bash | |
| **B. Grep tool** | ✓ |
| C. Find tool | |
| D. Search tool | |

**Explanation**: Grep tool is optimized for content searching with proper permissions. Don't use grep via Bash.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Grep Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/grep.md</code><br>
<strong>Section</strong>: Description<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"ALWAYS use Grep for search tasks. NEVER invoke grep or rg as a Bash command. The Grep tool has been optimized for correct permissions and access."</blockquote>

</details>

---

### Q6. The Bash tool should primarily be used for:

| Option | |
| ------ | --- |
| A. Reading file contents | |
| B. Searching for files | |
| **C. Terminal operations like git, npm, docker** | ✓ |
| D. Editing files | |

**Explanation**: Bash tool is for actual system commands. File operations have dedicated tools (Read, Write, Edit, Glob, Grep).

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Bash Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/bash.md</code><br>
<strong>Section</strong>: Description<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"IMPORTANT: This tool is for terminal operations like git, npm, docker, etc. DO NOT use it for file operations (reading, writing, editing, searching, finding files) - use the specialized tools for this instead."</blockquote>

</details>

---

### Q7. What happens if you try to Edit a file with an old_string that appears multiple times?

| Option | |
| ------ | --- |
| A. All occurrences are replaced | |
| B. Only the first occurrence is replaced | |
| **C. The edit fails - old_string must be unique** | ✓ |
| D. You're prompted to select which occurrence | |

**Explanation**: Edit requires unique old_string. Provide more context to make it unique, or use replace_all parameter.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Edit Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/edit.md</code><br>
<strong>Section</strong>: Usage<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"The edit will FAIL if old_string is not unique in the file. Either provide a larger string with more surrounding context to make it unique or use replace_all to change every instance of old_string."</blockquote>

</details>

---

### Q8. When creating a new file with the Write tool, what should you verify first?

| Option | |
| ------ | --- |
| A. That the parent directory exists | |
| B. That you have admin privileges | |
| C. That the file doesn't already exist | |
| **D. Both A and C** | ✓ |

**Explanation**: Write overwrites existing files. Always verify the parent directory exists and the file doesn't exist (unless intentional overwrite).

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Write Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/write.md</code><br>
<strong>Section</strong>: Usage<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"This tool will overwrite the existing file if there is one at the provided path. If this is an existing file, you MUST use the Read tool first to read the file's contents."</blockquote>

</details>

---

### Q9. What is the purpose of the Task tool in Claude Code?

| Option | |
| ------ | --- |
| A. Creating todo lists | |
| **B. Spawning specialized subagents for complex tasks** | ✓ |
| C. Scheduling commands to run later | |
| D. Managing background processes | |

**Explanation**: Task tool launches specialized agents (Explore, Plan, Bash, etc.) for complex, multi-step operations.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Task Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/task.md</code><br>
<strong>Section</strong>: Description<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Launch a new agent to handle complex, multi-step tasks autonomously. The Task tool launches specialized agents (subprocesses) that autonomously handle complex tasks."</blockquote>

</details>

---

### Q10. When you need to explore a codebase to answer a question (not a specific file lookup), which approach is recommended?

| Option | |
| ------ | --- |
| A. Run multiple Glob and Grep commands directly | |
| **B. Use Task tool with subagent_type=Explore** | ✓ |
| C. Ask the user where to look | |
| D. Read every file in the directory | |

**Explanation**: For open-ended exploration, the Explore agent is optimized to search across the codebase efficiently.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Task Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/task.md</code><br>
<strong>Section</strong>: Tool Usage Policy<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"When exploring the codebase to gather context or to answer a question that is not a needle query for a specific file/class/function, it is CRITICAL that you use the Task tool with subagent_type=Explore instead of running search commands directly."</blockquote>

</details>

---


## Agentic Workflows

*Domain: Agentic Patterns | Weight: 25%*

### Q1. When should you use the Task tool to spawn a subagent instead of doing work directly?

| Option | |
| ------ | --- |
| A. For any task that takes more than one tool call | |
| **B. For complex multi-step tasks or open-ended exploration** | ✓ |
| C. Always - subagents are more efficient | |
| D. Never - direct tool calls are always better | |

**Explanation**: Task tool is for complex tasks requiring multiple rounds of exploration. Simple tasks should use direct tool calls.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Task Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/task.md</code><br>
<strong>Section</strong>: When NOT to use the Task tool<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Launch a new agent to handle complex, multi-step tasks autonomously... When NOT to use the Task tool: If you want to read a specific file path, use the Read or Glob tool instead"</blockquote>

</details>

---

### Q2. What is the key benefit of running multiple Task tool calls in parallel?

| Option | |
| ------ | --- |
| A. Reduces token usage | |
| **B. Maximizes efficiency by concurrent execution** | ✓ |
| C. Makes the output cleaner | |
| D. Avoids context pollution | |

**Explanation**: When tasks are independent, running them in parallel completes work faster than sequential execution.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Task Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/task.md</code><br>
<strong>Section</strong>: Usage notes<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Launch multiple agents concurrently whenever possible, to maximize performance; to do that, use a single message with multiple tool uses"</blockquote>

</details>

---

### Q3. When spawning an Explore agent, what should your prompt include?

| Option | |
| ------ | --- |
| A. Just the file path to look at | |
| **B. The question to answer and thoroughness level (quick/medium/thorough)** | ✓ |
| C. A complete list of all files to read | |
| D. The expected answer format | |

**Explanation**: Explore agents need clear questions and thoroughness guidance to search effectively.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Task Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/task.md</code><br>
<strong>Section</strong>: Available agent types<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Explore: Fast agent specialized for exploring codebases... When calling this agent, specify the desired thoroughness level: 'quick' for basic searches, 'medium' for moderate exploration, or 'very thorough' for comprehensive analysis"</blockquote>

</details>

---

### Q4. What is the TodoWrite tool primarily used for?

| Option | |
| ------ | --- |
| A. Creating permanent project documentation | |
| **B. Tracking task progress and planning complex multi-step work** | ✓ |
| C. Sending notifications to the user | |
| D. Logging errors and warnings | |

**Explanation**: TodoWrite helps track progress on complex tasks and provides visibility to users on what's being done.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code TodoWrite Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/todowrite.md</code><br>
<strong>Section</strong>: Description<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user."</blockquote>

</details>

---

### Q5. When should you mark a todo as 'in_progress'?

| Option | |
| ------ | --- |
| A. When you add it to the list | |
| B. After completing the previous task | |
| **C. Before beginning work on that task** | ✓ |
| D. Only when the user asks about progress | |

**Explanation**: Mark tasks in_progress BEFORE starting. This gives users real-time visibility into current work.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code TodoWrite Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/todowrite.md</code><br>
<strong>Section</strong>: Task States and Management<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"When you start working on a task - Mark it as in_progress BEFORE beginning work. Ideally you should only have one todo as in_progress at a time"</blockquote>

</details>

---

### Q6. How many todos should be 'in_progress' at any given time?

| Option | |
| ------ | --- |
| A. As many as are being worked on in parallel | |
| **B. Exactly one** | ✓ |
| C. Zero until all are complete | |
| D. No limit | |

**Explanation**: Only ONE task should be in_progress at a time. Complete current tasks before starting new ones.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code TodoWrite Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/todowrite.md</code><br>
<strong>Section</strong>: Task Management<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Exactly ONE task must be in_progress at any time (not less, not more). Complete current tasks before starting new ones"</blockquote>

</details>

---

### Q7. When a user asks you to implement a non-trivial feature, what tool should you consider using first?

| Option | |
| ------ | --- |
| A. Write tool to start coding immediately | |
| **B. EnterPlanMode to design the approach first** | ✓ |
| C. Task tool to spawn multiple agents | |
| D. Read tool to look at existing code | |

**Explanation**: For non-trivial implementations, planning first prevents wasted effort and ensures alignment with user expectations.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code EnterPlanMode Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/enterplanmode.md</code><br>
<strong>Section</strong>: When to Use This Tool<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment."</blockquote>

</details>

---

### Q8. What happens when you use AskUserQuestion tool?

| Option | |
| ------ | --- |
| **A. The conversation pauses until the user responds** | ✓ |
| B. A background process waits for input | |
| C. The question is logged for later review | |
| D. Multiple questions are batched together | |

**Explanation**: AskUserQuestion is synchronous - use it when you need clarification before proceeding.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code AskUserQuestion Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/askuserquestion.md</code><br>
<strong>Section</strong>: Description<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Use this tool when you need to ask the user questions during execution. This allows you to: Gather user preferences or requirements, Clarify ambiguous instructions, Get decisions on implementation choices as you work"</blockquote>

</details>

---

### Q9. When should you NOT use the TodoWrite tool?

| Option | |
| ------ | --- |
| A. For complex multi-step tasks | |
| B. When the user provides multiple requirements | |
| **C. For a single, straightforward task that takes one step** | ✓ |
| D. When planning implementation strategy | |

**Explanation**: Skip TodoWrite for trivial single-step tasks. Just do the work directly.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code TodoWrite Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/todowrite.md</code><br>
<strong>Section</strong>: When NOT to Use This Tool<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"When NOT to Use This Tool: Skip using this tool when: There is only a single, straightforward task. The task is trivial and tracking it provides no organizational benefit. The task can be completed in less than 3 trivial steps."</blockquote>

</details>

---

### Q10. What is the correct approach when you encounter an error during task execution?

| Option | |
| ------ | --- |
| A. Mark the todo as completed and move on | |
| **B. Keep the task in_progress, investigate and fix the error** | ✓ |
| C. Delete the todo and start over | |
| D. Ask the user what to do | |

**Explanation**: Never mark tasks complete if errors occurred. Keep in_progress while investigating and fixing.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code TodoWrite Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/todowrite.md</code><br>
<strong>Section</strong>: Task Completion Requirements<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"ONLY mark a task as completed when you have FULLY accomplished it. If you encounter errors, blockers, or cannot finish, keep the task as in_progress. When blocked, create a new task describing what needs to be resolved."</blockquote>

</details>

---


## Claude Code Best Practices

*Domain: Best Practices | Weight: 15%*

### Q1. When the user asks about a file you haven't seen yet, what should you do FIRST?

| Option | |
| ------ | --- |
| A. Provide general guidance based on the filename | |
| **B. Use the Read tool to view the file contents** | ✓ |
| C. Ask the user to paste the relevant code | |
| D. Make assumptions based on common patterns | |

**Explanation**: Never propose changes to code you haven't read. Always read first, then understand, then suggest.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Understanding code before modifying<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"NEVER propose changes to code you haven't read. If a user asks about or wants you to modify a file, read it first. Understand existing code before suggesting modifications."</blockquote>

</details>

---

### Q2. The user asks for a 'quick fix' to add logging. What's the best approach?

| Option | |
| ------ | --- |
| A. Add comprehensive logging throughout the codebase | |
| **B. Add logging only to the specific area mentioned** | ✓ |
| C. Refactor the code to use a logging framework first | |
| D. Add logging plus docstrings and comments for clarity | |

**Explanation**: Avoid over-engineering. Only do what was asked. Don't add features, refactoring, or 'improvements' beyond the request.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Avoid over-engineering<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Avoid over-engineering. Only make changes that are directly requested or clearly necessary. Keep solutions simple and focused. Don't add features, refactor code, or make 'improvements' beyond what was asked."</blockquote>

</details>

---

### Q3. When writing code for the user, should you add docstrings and comments?

| Option | |
| ------ | --- |
| A. Yes, always add comprehensive documentation | |
| **B. Only add comments where logic isn't self-evident** | ✓ |
| C. Never - let the code speak for itself | |
| D. Only if the user specifically requests it | |

**Explanation**: Don't add unnecessary documentation. Only comment non-obvious logic. Don't add docstrings/comments to code you didn't change.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Avoid over-engineering<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Only add comments where the logic isn't self-evident. Don't add docstrings, comments, or type annotations to code you didn't change."</blockquote>

</details>

---

### Q4. The user's code has a minor style inconsistency near where you're making changes. Should you fix it?

| Option | |
| ------ | --- |
| A. Yes, clean up surrounding code while you're there | |
| **B. No, only change what was requested** | ✓ |
| C. Ask the user if they want you to fix it | |
| D. Fix it silently - they'll appreciate the polish | |

**Explanation**: A bug fix doesn't need surrounding code cleaned up. Stay focused on the requested change only.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Avoid over-engineering<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't need extra configurability."</blockquote>

</details>

---

### Q5. What's the recommended approach for providing time estimates?

| Option | |
| ------ | --- |
| A. Always provide estimates so users can plan | |
| B. Give rough estimates like 'a few minutes' | |
| **C. Never give time estimates - focus on what needs to be done** | ✓ |
| D. Only estimate when the user asks directly | |

**Explanation**: Don't predict timing. Focus on breaking work into actionable steps and let users judge timing themselves.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: No time estimates<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Never give time estimates or predictions for how long tasks will take, whether for your own work or for users planning their projects. Focus on what needs to be done, not how long it might take."</blockquote>

</details>

---

### Q6. How should you handle uncertainty about the user's requirements?

| Option | |
| ------ | --- |
| A. Make reasonable assumptions and proceed | |
| **B. Use AskUserQuestion to clarify before acting** | ✓ |
| C. Implement multiple options and let them choose | |
| D. Do the most common interpretation | |

**Explanation**: When requirements are unclear, ask! AskUserQuestion prevents wasted effort from wrong assumptions.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Tools - AskUserQuestion<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/core-features#asking-questions">Claude Code Tools - AskUserQuestion</a><br>
<strong>Section</strong>: Description<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Use this tool when you need to ask the user questions during execution. This allows you to: Clarify ambiguous instructions"</blockquote>

</details>

---

### Q7. A file already exists at the path where you want to create a new file. What should you check?

| Option | |
| ------ | --- |
| A. Just overwrite it - the user knows what they asked for | |
| **B. Read it first to understand if it should be modified vs replaced** | ✓ |
| C. Create a backup automatically before overwriting | |
| D. Use a different filename to avoid conflict | |

**Explanation**: Always prefer editing existing files over creating new ones. Read first to understand what's there.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: File operations<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required. If this is an existing file, you MUST use the Read tool first to read the file's contents."</blockquote>

</details>

---

### Q8. What's the correct communication style when responding to users?

| Option | |
| ------ | --- |
| A. Detailed explanations with plenty of enthusiasm and emoji | |
| **B. Short, concise responses focused on the task** | ✓ |
| C. Technical jargon to demonstrate expertise | |
| D. Formal language with lots of caveats | |

**Explanation**: Output is displayed in CLI - keep responses short and concise. Avoid emojis unless requested.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Tone and style<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Your output will be displayed on a command line interface. Your responses should be short and concise. Only use emojis if the user explicitly requests it."</blockquote>

</details>

---

### Q9. When referencing code locations in your response, what format should you use?

| Option | |
| ------ | --- |
| A. Just the filename | |
| **B. file_path:line_number** | ✓ |
| C. A code snippet with the relevant lines | |
| D. The function name only | |

**Explanation**: Use file_path:line_number format (e.g., src/utils.py:42) so users can navigate directly to the location.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Code References<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"When referencing specific functions or pieces of code include the pattern file_path:line_number to allow the user to easily navigate to the source code location."</blockquote>

</details>

---

### Q10. The user disagrees with your technical recommendation. How should you respond?

| Option | |
| ------ | --- |
| A. Insist on the correct approach - you know best | |
| B. Immediately agree with whatever they say | |
| **C. Explain your reasoning objectively, but respect their decision** | ✓ |
| D. Change the subject to avoid conflict | |

**Explanation**: Prioritize technical accuracy - explain your reasoning. But ultimately respect the user's autonomy to decide.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Professional objectivity<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Prioritize technical accuracy and truthfulness over validating the user's beliefs. It is best for the user if Claude honestly applies the same rigorous standards to all ideas and disagrees when necessary, even if it may not be what the user wants to hear."</blockquote>

</details>

---


## Error Handling & Safety

*Domain: Error Handling + Safety | Weight: 35%*

### Q1. When a Bash command exits with a non-zero exit code, what should you do?

| Option | |
| ------ | --- |
| A. Ignore it and continue with the next task | |
| **B. Stop and acknowledge the failure, diagnose, then fix** | ✓ |
| C. Retry the same command automatically | |
| D. Report to the user and wait for instructions | |

**Explanation**: Never ignore non-zero exits. Acknowledge, diagnose from stderr, fix the root cause, then verify success.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Python Silent Failure Principles<br>
<strong>URL</strong>: <code>file://~/.claude/docs/hooks/silent-failure-guard.md</code><br>
<strong>Section</strong>: Error Handling Principles<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"ALWAYS use subprocess.run(..., check=True) - without check=True, non-zero exits are silent. Fix each pattern to make failures VISIBLE and ACTIONABLE, not silent."</blockquote>

</details>

---

### Q2. What is the correct pattern for handling cd failures in shell scripts?

| Option | |
| ------ | --- |
| A. cd /path/to/dir | |
| **B. cd /path/to/dir || exit 1** | ✓ |
| C. cd /path/to/dir 2>/dev/null | |
| D. if cd /path/to/dir; then echo 'ok'; fi | |

**Explanation**: cd can fail silently. Always handle with || exit 1 or || { echo 'Failed'; exit 1; }

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Bash Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/bash.md</code><br>
<strong>Section</strong>: Directory Verification<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"If the command will create new directories or files, first use ls to verify the parent directory exists and is the correct location"</blockquote>

</details>

---

### Q3. When writing Python code, which exception handling pattern is WRONG?

| Option | |
| ------ | --- |
| A. except ValueError as e: logging.error(f'Invalid: {e}'); raise | |
| **B. except Exception: pass** | ✓ |
| C. except (TypeError, KeyError) as e: handle_error(e) | |
| D. except SpecificError: logger.warning('Known issue'); return default | |

**Explanation**: Bare 'except: pass' swallows all errors silently, hiding bugs. Always catch specific exceptions and handle/log them.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Python Silent Failure Principles<br>
<strong>URL</strong>: <code>file://~/.claude/docs/hooks/silent-failure-guard.md</code><br>
<strong>Section</strong>: Python Silent Failure Principles<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"NEVER use bare 'except:' - it catches KeyboardInterrupt, SystemExit, and hides real bugs. NEVER use 'except: pass' - errors must be logged, re-raised, or explicitly handled. CATCH SPECIFIC exceptions."</blockquote>

</details>

---

### Q4. What is the risk of using subprocess.run() without check=True in Python?

| Option | |
| ------ | --- |
| A. No risk - it's the recommended pattern | |
| B. The command output is not captured | |
| **C. Non-zero exit codes are silently ignored** | ✓ |
| D. The subprocess runs asynchronously | |

**Explanation**: Without check=True, subprocess.run() returns normally even on failure. Always use check=True.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Python Silent Failure Principles<br>
<strong>URL</strong>: <code>file://~/.claude/docs/hooks/silent-failure-guard.md</code><br>
<strong>Section</strong>: Subprocess Rules<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"ALWAYS use subprocess.run(..., check=True) - without check=True, non-zero exits are silent. PLW1510: subprocess.run() without check= silently ignores command failures"</blockquote>

</details>

---

### Q5. Claude Code runs in a sandbox. What does this mean for file operations?

| Option | |
| ------ | --- |
| A. You cannot access any files on the system | |
| B. Files outside the working directory are completely inaccessible | |
| **C. You can access the filesystem but with user-level permissions** | ✓ |
| D. All file operations require explicit user approval | |

**Explanation**: Claude Code has filesystem access with user permissions. You can read/write files the user can access.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Read Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/read.md</code><br>
<strong>Section</strong>: Description<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Reads a file from the local filesystem. You can access any file directly by using this tool. Assume this tool is able to read all files on the machine."</blockquote>

</details>

---

### Q6. Which git operations should you NEVER do without explicit user request?

| Option | |
| ------ | --- |
| A. git status, git diff | |
| B. git add, git log | |
| **C. git push --force, git reset --hard** | ✓ |
| D. git branch, git checkout | |

**Explanation**: Destructive git operations (force push, hard reset) can lose work. Only do these when explicitly requested.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code System Prompt - Git Safety Protocol<br>
<strong>URL</strong>: <code>file://~/.claude/docs/system-prompt-reference.md</code><br>
<strong>Section</strong>: Git Safety Protocol<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"NEVER run destructive git commands (push --force, reset --hard, checkout ., restore ., clean -f, branch -D) unless the user explicitly requests these actions. Taking unauthorized destructive actions is unhelpful and can result in lost work"</blockquote>

</details>

---

### Q7. When should you commit changes to git?

| Option | |
| ------ | --- |
| A. After every file change | |
| B. At the end of each session | |
| **C. Only when the user explicitly asks** | ✓ |
| D. After completing each feature | |

**Explanation**: Never commit proactively. Users may want to review changes or have their own commit workflow.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code System Prompt - Git Safety Protocol<br>
<strong>URL</strong>: <code>file://~/.claude/docs/system-prompt-reference.md</code><br>
<strong>Section</strong>: Git Safety Protocol<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Only create commits when requested by the user. If unclear, ask first... NEVER commit changes unless the user explicitly asks you to. It is VERY IMPORTANT to only commit when explicitly asked"</blockquote>

</details>

---

### Q8. You notice code that might contain a security vulnerability (e.g., SQL injection). What should you do?

| Option | |
| ------ | --- |
| A. Fix it silently to avoid alarming the user | |
| **B. Point it out and offer to fix it** | ✓ |
| C. Ignore it - security is not your concern | |
| D. Stop all work until it's addressed | |

**Explanation**: Always flag security issues. Be helpful by offering to fix, but don't modify without acknowledgment.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code System Prompt - Doing tasks<br>
<strong>URL</strong>: <code>file://~/.claude/docs/system-prompt-reference.md</code><br>
<strong>Section</strong>: Doing tasks<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"Be careful not to introduce security vulnerabilities such as command injection, XSS, SQL injection, and other OWASP top 10 vulnerabilities. If you notice that you wrote insecure code, immediately fix it."</blockquote>

</details>

---

### Q9. What should you do before running a command that modifies many files (like a mass rename)?

| Option | |
| ------ | --- |
| A. Just run it - Claude Code has undo capability | |
| **B. Explain the scope and get confirmation from the user** | ✓ |
| C. Create a backup of every file first | |
| D. Test on one file then automatically do the rest | |

**Explanation**: For bulk operations, explain what will be affected and confirm before proceeding. Users need to understand scope.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code System Prompt - Git Safety Protocol<br>
<strong>URL</strong>: <code>file://~/.claude/docs/system-prompt-reference.md</code><br>
<strong>Section</strong>: Committing changes with git<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"When staging files, prefer adding specific files by name rather than using 'git add -A' or 'git add .', which can accidentally include sensitive files (.env, credentials) or large binaries"</blockquote>

</details>

---

### Q10. What is the correct approach when the user provides a path that doesn't exist?

| Option | |
| ------ | --- |
| A. Create it automatically and continue | |
| B. Fail silently and skip that operation | |
| **C. Inform the user and ask how to proceed** | ✓ |
| D. Guess what they meant and use a similar path | |

**Explanation**: Don't assume. Let the user know the path doesn't exist and ask whether to create it or use a different path.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Bash Tool Reference<br>
<strong>URL</strong>: <code>file://~/.claude/docs/tools/bash.md</code><br>
<strong>Section</strong>: Directory Verification<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"If the command will create new directories or files, first use ls to verify the parent directory exists and is the correct location. For example, before running 'mkdir foo/bar', first use 'ls foo' to check that 'foo' exists"</blockquote>

</details>

---


## Claude Code Hooks Lifecycle

*Domain: Hooks & Automation | Weight: 20%*

### Q1. What is the primary purpose of Claude Code hooks?

| Option | |
| ------ | --- |
| A. To replace Claude's built-in tools with custom implementations | |
| **B. To execute shell commands at specific lifecycle events for validation, automation, and control** | ✓ |
| C. To modify Claude's underlying language model behavior | |
| D. To disable Claude Code's security features | |

**Explanation**: Hooks are user-defined shell commands that execute automatically at specific points in Claude Code's lifecycle. They provide deterministic control for validation, automation, blocking dangerous operations, and injecting context.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Hook lifecycle<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Hooks fire at specific points during a Claude Code session."</blockquote>

</details>

---

### Q2. When does the UserPromptSubmit hook fire?

| Option | |
| ------ | --- |
| A. After Claude processes the prompt | |
| **B. When you submit a prompt, BEFORE Claude processes it** | ✓ |
| C. When Claude finishes responding | |
| D. When the session ends | |

**Explanation**: UserPromptSubmit fires when the user presses Enter, before Claude begins processing. This allows validation, capture, or blocking of prompts.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Introduction to Claude Code Hooks<br>
<strong>URL</strong>: <code>file://~/.claude/docs/hooks/00-INTRODUCTION.md</code><br>
<strong>Section</strong>: UserPromptSubmit<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"**Fires**: When you submit a prompt to Claude (before processing)"</blockquote>

</details>

---

### Q3. Which hooks CAN block execution (prevent an action from proceeding)?

| Option | |
| ------ | --- |
| A. Only PreToolUse and PostToolUse | |
| **B. UserPromptSubmit, PreToolUse, PermissionRequest, PostToolUse, PostToolUseFailure, SubagentStop, and Stop** | ✓ |
| C. All hook types can block | |
| D. Only Stop and SessionEnd | |

**Explanation**: These hooks can block: UserPromptSubmit (hard), PreToolUse (hard), PermissionRequest (hard), PostToolUse (soft - tool already ran), PostToolUseFailure (soft - tool already failed), SubagentStop (hard), and Stop (hard). SessionStart, PreCompact, Notification, and SessionEnd cannot block.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Lifecycle Reference<br>
<strong>URL</strong>: <code>file://~/.claude/plugins/marketplaces/cc-skills/plugins/itp-hooks/skills/hooks-development/references/lifecycle-reference.md</code><br>
<strong>Section</strong>: Blocking vs Non-Blocking Hooks<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"**CAN BLOCK** — These hooks can prevent or modify execution: UserPromptSubmit (Hard), PreToolUse (Hard), PermissionRequest (Hard), PostToolUse (Soft), PostToolUseFailure (Soft), SubagentStop (Hard), Stop (Hard)"</blockquote>

</details>

---

### Q4. How do hooks receive their input data?

| Option | |
| ------ | --- |
| A. Via environment variables like $TOOL_NAME and $COMMAND | |
| B. Via command-line arguments | |
| **C. Via stdin as a JSON object** | ✓ |
| D. Via a configuration file | |

**Explanation**: All hooks receive their input via stdin as a JSON object. Environment variables are NOT used for input - only CLAUDE_PROJECT_DIR, CLAUDE_CODE_REMOTE, and CLAUDE_ENV_FILE are available.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Lifecycle Reference<br>
<strong>URL</strong>: <code>file://~/.claude/plugins/marketplaces/cc-skills/plugins/itp-hooks/skills/hooks-development/references/lifecycle-reference.md</code><br>
<strong>Section</strong>: Hook Input Delivery Mechanism<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"All hooks receive their input data via **stdin as a JSON object**. ... **Critical**: Hook inputs are NOT passed via environment variables."</blockquote>

</details>

---

### Q5. What is the CORRECT way to reference a hook script in settings.json?

| Option | |
| ------ | --- |
| A. "command": "uv run $HOME/.claude/hooks/script.py" | |
| B. "command": "python3 $HOME/.claude/hooks/script.py" | |
| **C. "command": "$HOME/.claude/hooks/script.py"** | ✓ |
| D. "command": "./hooks/script.py" | |

**Explanation**: Hooks must use direct executable paths without wrappers. Never use 'uv run', 'python3', or relative paths. The script must have a shebang and be executable (chmod +x).

<details>
<summary>Citation [Tier 2 - cc-skills] (90% confidence)</summary>

<strong>Source</strong>: Claude Code Hook Best Practices<br>
<strong>URL</strong>: <code>file://~/.claude/docs/hooks/HOOK_BEST_PRACTICES.md</code><br>
<strong>Section</strong>: Use Direct Executable Paths<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"**Rule**: Never wrap executables with command prefixes like `uv run`, `python3`, or similar. **Why**: Hook parser expects single-token commands (direct executable paths). Multi-token commands cause "Found 0 hook matchers" failures."</blockquote>

</details>

---

### Q6. When does PostToolUse hook fire?

| Option | |
| ------ | --- |
| A. After any tool completes (success or failure) | |
| **B. After a tool completes successfully ONLY (NOT on errors)** | ✓ |
| C. Before a tool executes | |
| D. When the user submits a prompt | |

**Explanation**: PostToolUse ONLY fires after successful tool completion. Failed Bash commands (exit ≠ 0) do NOT trigger PostToolUse. There is no PostToolUseError hook.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Lifecycle Reference<br>
<strong>URL</strong>: <code>file://~/.claude/plugins/marketplaces/cc-skills/plugins/itp-hooks/skills/hooks-development/references/lifecycle-reference.md</code><br>
<strong>Section</strong>: CRITICAL: Non-Existent Hook Types<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"PostToolUse fires for all tool completions | **Only fires on SUCCESS** | Failed Bash commands (exit ≠ 0) do NOT trigger PostToolUse"</blockquote>

</details>

---

### Q7. For PostToolUse hooks, what is required for Claude to see your message?

| Option | |
| ------ | --- |
| A. Output {"reason": "your message"} | |
| B. Output {"additionalContext": "your message"} | |
| **C. Output {"decision": "block", "reason": "your message"}** | ✓ |
| D. Write to stdout with plain text | |

**Explanation**: Counterintuitively, PostToolUse requires 'decision: block' for Claude to see the reason - but this does NOT actually block anything since the tool already ran. Without this field, Claude sees nothing.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Lifecycle Reference<br>
<strong>URL</strong>: <code>file://~/.claude/plugins/marketplaces/cc-skills/plugins/itp-hooks/skills/hooks-development/references/lifecycle-reference.md</code><br>
<strong>Section</strong>: PostToolUse: Visibility Requires decision: block<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"**Counterintuitive but documented**: Claude only sees `reason` when `decision: "block"` is present. ... **Key insight**: The `decision: "block"` is required for visibility, but it does NOT actually block anything - the tool already ran."</blockquote>

</details>

---

### Q8. What is the recommended execution time for hooks?

| Option | |
| ------ | --- |
| A. Under 1 second | |
| **B. Under 100 milliseconds** | ✓ |
| C. Under 5 seconds | |
| D. No time limit | |

**Explanation**: Hooks should execute quickly (< 100ms) using the fire-and-forget pattern. Long-running hooks degrade user experience and risk timeouts.

<details>
<summary>Citation [Tier 2 - cc-skills] (90% confidence)</summary>

<strong>Source</strong>: Claude Code Hook Best Practices<br>
<strong>URL</strong>: <code>file://~/.claude/docs/hooks/HOOK_BEST_PRACTICES.md</code><br>
<strong>Section</strong>: Keep Hook Execution < 100ms<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"**Rule**: Hooks should execute quickly (< 100ms) using fire-and-forget pattern. **Why**: Blocks Claude Code session start/stop if too slow. Poor user experience with noticeable delays."</blockquote>

</details>

---

### Q9. What does exit code 2 mean in a hook script?

| Option | |
| ------ | --- |
| A. Success - allow the action | |
| B. Non-blocking error | |
| **C. Hard block - cannot be bypassed** | ✓ |
| D. Soft block - user can override | |

**Explanation**: Exit code 2 is a hard block that cannot be bypassed. Exit 0 is success, and other exit codes are non-blocking errors.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Lifecycle Reference<br>
<strong>URL</strong>: <code>file://~/.claude/plugins/marketplaces/cc-skills/plugins/itp-hooks/skills/hooks-development/references/lifecycle-reference.md</code><br>
<strong>Section</strong>: Exit Codes<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"**0** — Success/allow (JSON output processed) | **2** — Hard block, cannot bypass (stderr only) | **Other** — Non-blocking error"</blockquote>

</details>

---

### Q10. In Stop hooks, what does {"continue": false} actually do?

| Option | |
| ------ | --- |
| A. Allows Claude to stop normally | |
| B. Prevents Claude from stopping (forces continuation) | |
| **C. Halts Claude entirely (emergency stop)** | ✓ |
| D. Has no effect | |

**Explanation**: continue: false is an ACTIVE intervention to halt Claude entirely - it does NOT mean 'allow stop'. To allow normal stop, output an empty object {}. To force continuation, use decision: block.

<details>
<summary>Citation [Tier 2 - cc-skills] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Lifecycle Reference<br>
<strong>URL</strong>: <code>file://~/.claude/plugins/marketplaces/cc-skills/plugins/itp-hooks/skills/hooks-development/references/lifecycle-reference.md</code><br>
<strong>Section</strong>: Stop Hook Schema<br>
<strong>Access Date</strong>: 2026-01-22<br>
<blockquote>"**Key insight**: `{"continue": false}` means "HARD STOP Claude entirely" - it does NOT mean "allow normal stop". ... **Allow stop**: `{}` (empty object) | **Continue session**: `{"decision": "block", "reason": "..."}` | **Hard stop**: `{"continue": false, "stopReason": "..."}`"</blockquote>

</details>

---


## Claude Code Agents Deep Dive

*Domain: Advanced Architecture | Weight: 20%*

### Q1. What distinguishes pre-defined agents from on-demand subagents in Claude Code?

| Option | |
| ------ | --- |
| A. Pre-defined agents are faster to execute | |
| **B. Pre-defined agents auto-trigger based on patterns, on-demand subagents are explicitly spawned** | ✓ |
| C. Pre-defined agents have access to more tools | |
| D. Pre-defined agents run in the background | |

**Explanation**: Pre-defined agents in .claude/agents/ directory auto-activate when their trigger patterns match user requests, without explicit invocation. On-demand subagents are spawned explicitly via the Task tool during execution.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Sub-agents<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/sub-agents">Claude Code Sub-agents</a><br>
<strong>Section</strong>: Pre-defined agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Pre-defined agents are stored in your project's .claude/agents/ directory. When Claude detects that a task matches an agent's capabilities, it automatically activates that agent."</blockquote>

</details>

---

### Q2. Where are Claude Code pre-defined agents stored?

| Option | |
| ------ | --- |
| A. ~/.claude/skills/ | |
| B. ~/.claude/plugins/ | |
| **C. .claude/agents/ in project root** | ✓ |
| D. ~/.config/claude/agents/ | |

**Explanation**: Pre-defined agents are stored in the .claude/agents/ directory within the project root, not in user-level directories. This allows project-specific agent configurations.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Sub-agents<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/sub-agents">Claude Code Sub-agents</a><br>
<strong>Section</strong>: Pre-defined agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Pre-defined agents are stored in your project's .claude/agents/ directory."</blockquote>

</details>

---

### Q3. What happens when a pre-defined agent's trigger pattern matches a user request?

| Option | |
| ------ | --- |
| A. User is prompted to approve activation | |
| **B. Agent auto-activates without explicit user request** | ✓ |
| C. Main agent pauses execution | |
| D. Session terminates for safety | |

**Explanation**: When Claude detects that a task matches an agent's capabilities based on trigger patterns, it automatically activates that agent without requiring explicit user invocation.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Sub-agents<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/sub-agents">Claude Code Sub-agents</a><br>
<strong>Section</strong>: Pre-defined agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"When Claude detects that a task matches an agent's capabilities, it automatically activates that agent."</blockquote>

</details>

---

### Q4. When should you convert a pre-defined agent to an on-demand subagent?

| Option | |
| ------ | --- |
| A. When it runs frequently | |
| **B. When it rarely triggers or has narrow scope** | ✓ |
| C. When it uses many tools | |
| D. When it accesses external APIs | |

**Explanation**: Pre-defined agents that rarely trigger or have very narrow scope should be converted to on-demand subagents to reduce cognitive overhead and avoid agent sprawl. Keep pre-defined agents for frequently-used, domain-specific capabilities.

<details>
<summary>Citation [Tier 2 - alpha-forge] (90% confidence)</summary>

<strong>Source</strong>: RFC: Reduce Pre-Defined Subagent Count<br>
<strong>URL</strong>: <a href="https://github.com/EonLabs-Spartan/alpha-forge/issues/123">RFC: Reduce Pre-Defined Subagent Count</a><br>
<strong>Section</strong>: Agent Analysis Criteria<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"DELETE (0-2): Generic agents that duplicate built-in capabilities or rarely trigger. KEEP (9-10): Domain-specific, irreplaceable agents with unique value."</blockquote>

</details>

---

### Q5. What is the 'context gatekeeping' anti-pattern in multi-agent systems?

| Option | |
| ------ | --- |
| A. Limiting token usage to save costs | |
| B. Restricting tool access for security | |
| **C. Subagents hiding context from the main orchestrator** | ✓ |
| D. Caching conversation history for performance | |

**Explanation**: Context gatekeeping occurs when subagents process information but don't share full context with the parent agent. This prevents the orchestrator from making holistic decisions across domain boundaries.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: When (not) to use agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path."</blockquote>

</details>

---

### Q6. Why does context gatekeeping reduce agent effectiveness?

| Option | |
| ------ | --- |
| A. Increases latency significantly | |
| B. Uses more tokens than necessary | |
| **C. Prevents holistic reasoning across domain boundaries** | ✓ |
| D. Causes memory leaks in long sessions | |

**Explanation**: When subagents hide context, the parent agent cannot synthesize information across different domains, leading to fragmented decision-making and missed connections between related findings.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building a Multi-Agent Research System<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/research/building-a-multi-agent-research-system">Building a Multi-Agent Research System</a><br>
<strong>Section</strong>: Coordinator Design<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"The coordinator agent needs visibility into all research findings to synthesize a coherent response that draws connections across domains."</blockquote>

</details>

---

### Q7. What is the recommended alternative to context gatekeeping?

| Option | |
| ------ | --- |
| A. Use more subagents for parallelism | |
| **B. Keep context in main agent, use subagents only for isolated subtasks** | ✓ |
| C. Increase context window size | |
| D. Implement caching layers between agents | |

**Explanation**: The main agent should retain full context and use subagents only for truly isolated, parallelizable subtasks where the parent doesn't need intermediate visibility. Results flow back to the main agent for synthesis.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Agent architectures<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"The simplest architecture is a single agent that handles all tasks. For more complex scenarios, use orchestrator patterns where subagents handle isolated subtasks and report back."</blockquote>

</details>

---

### Q8. In the Multi-Agent Research System design, what was the key insight about subagent coordination?

| Option | |
| ------ | --- |
| **A. Parent agent must see and synthesize all findings** | ✓ |
| B. Each subagent should operate independently without coordination | |
| C. Subagents should communicate directly with each other | |
| D. Results should be aggregated externally | |

**Explanation**: The research system demonstrated that the coordinator/parent agent needs visibility into all findings to synthesize coherent responses that draw connections across different research domains.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building a Multi-Agent Research System<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/research/building-a-multi-agent-research-system">Building a Multi-Agent Research System</a><br>
<strong>Section</strong>: System Architecture<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"The coordinator agent synthesizes findings from all research agents to produce a coherent final answer."</blockquote>

</details>

---

### Q9. What is the fundamental difference between skills and subagents in Claude Code?

| Option | |
| ------ | --- |
| A. Skills are faster to execute | |
| B. Skills use fewer tokens | |
| **C. Skills run in main context, subagents have isolated context windows** | ✓ |
| D. Skills require user approval | |

**Explanation**: Skills execute within the main conversation context, keeping all information visible to Claude. Subagents run in isolated context windows, receiving only what's passed to them and returning only their output.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code Skills</a><br>
<strong>Section</strong>: Skills vs Subagents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Skills run within the main conversation context, while subagents operate in isolated context windows with their own tool access."</blockquote>

</details>

---

### Q10. When should you use a skill instead of a subagent?

| Option | |
| ------ | --- |
| A. For complex multi-step tasks requiring autonomy | |
| **B. For checklists, templates, or context injection** | ✓ |
| C. For parallel execution of independent tasks | |
| D. For background processing | |

**Explanation**: Skills are ideal for checklists, templates, prompts, and context injection where you want the information to remain visible in the main conversation. Subagents are better for autonomous, isolated tasks.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code Skills</a><br>
<strong>Section</strong>: When to use skills<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Use skills for context injection, checklists, and templates where you want the information to remain in the main conversation."</blockquote>

</details>

---

### Q11. What happens to skill context after execution?

| Option | |
| ------ | --- |
| **A. It remains in the main conversation context** | ✓ |
| B. It is discarded after use | |
| C. It is saved to disk | |
| D. It is compressed for efficiency | |

**Explanation**: Skills inject their content directly into the main conversation context, where it persists for the remainder of the session. This is unlike subagents whose context is isolated and discarded after returning results.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code Skills</a><br>
<strong>Section</strong>: Context persistence<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Skill content is injected into the main conversation context and remains available throughout the session."</blockquote>

</details>

---

### Q12. A pre-defined agent rated 3-5 (valuable checklist with minimal reasoning required) should be converted to what?

| Option | |
| ------ | --- |
| A. On-demand subagent | |
| **B. Skill** | ✓ |
| C. Hook | |
| D. MCP server | |

**Explanation**: Agents that primarily provide checklists or templates with minimal autonomous reasoning should be converted to skills. Skills inject content into the main context where the main agent can use it directly.

<details>
<summary>Citation [Tier 2 - alpha-forge] (90% confidence)</summary>

<strong>Source</strong>: RFC: Reduce Pre-Defined Subagent Count<br>
<strong>URL</strong>: <a href="https://github.com/EonLabs-Spartan/alpha-forge/issues/123">RFC: Reduce Pre-Defined Subagent Count</a><br>
<strong>Section</strong>: Conversion Criteria<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"CONVERT TO SKILL (3-5): Valuable checklist or reference that requires minimal autonomous reasoning. Content should be injected into main context."</blockquote>

</details>

---

### Q13. What rating indicates an agent should be KEPT as a pre-defined agent?

| Option | |
| ------ | --- |
| A. 0-2 | |
| B. 3-5 | |
| C. 6-8 | |
| **D. 9-10** | ✓ |

**Explanation**: Agents rated 9-10 are domain-specific, irreplaceable, and provide unique value that cannot be achieved through built-in capabilities or simple prompts. These should remain as pre-defined agents.

<details>
<summary>Citation [Tier 2 - alpha-forge] (92% confidence)</summary>

<strong>Source</strong>: RFC: Reduce Pre-Defined Subagent Count<br>
<strong>URL</strong>: <a href="https://github.com/EonLabs-Spartan/alpha-forge/issues/123">RFC: Reduce Pre-Defined Subagent Count</a><br>
<strong>Section</strong>: Rating Scale<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"KEEP (9-10): Domain-specific, irreplaceable agents that provide unique value. These are core to the project's functionality."</blockquote>

</details>

---

### Q14. What characterizes agents rated 0-2 that should be DELETED?

| Option | |
| ------ | --- |
| **A. Generic agents that duplicate built-in capabilities** | ✓ |
| B. Domain-specific agents with irreplaceable value | |
| C. Agents with high token usage | |
| D. Agents with complex dependencies | |

**Explanation**: Agents rated 0-2 are generic, duplicate what Claude can already do with built-in tools, or rarely trigger. They add cognitive overhead without providing unique value and should be deleted.

<details>
<summary>Citation [Tier 2 - alpha-forge] (92% confidence)</summary>

<strong>Source</strong>: RFC: Reduce Pre-Defined Subagent Count<br>
<strong>URL</strong>: <a href="https://github.com/EonLabs-Spartan/alpha-forge/issues/123">RFC: Reduce Pre-Defined Subagent Count</a><br>
<strong>Section</strong>: Rating Scale<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"DELETE (0-2): Generic agents that duplicate built-in capabilities or rarely trigger. Adds cognitive overhead without unique value."</blockquote>

</details>

---

### Q15. Agents rated 6-8 should be handled how?

| Option | |
| ------ | --- |
| A. Kept as-is without changes | |
| B. Deleted immediately | |
| **C. Consolidated with related agents** | ✓ |
| D. Converted to hooks | |

**Explanation**: Agents rated 6-8 have overlapping functionality with other agents. They should be consolidated into fewer, more focused agents to reduce sprawl while preserving their valuable capabilities.

<details>
<summary>Citation [Tier 2 - alpha-forge] (92% confidence)</summary>

<strong>Source</strong>: RFC: Reduce Pre-Defined Subagent Count<br>
<strong>URL</strong>: <a href="https://github.com/EonLabs-Spartan/alpha-forge/issues/123">RFC: Reduce Pre-Defined Subagent Count</a><br>
<strong>Section</strong>: Rating Scale<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"CONSOLIDATE (6-8): Agents with overlapping scope that should be merged with related agents to reduce sprawl."</blockquote>

</details>

---

### Q16. What is 'agent sprawl' in enterprise AI systems?

| Option | |
| ------ | --- |
| A. Agents using too much memory | |
| **B. Enterprise anti-pattern of producing dozens of agents without centralized organization** | ✓ |
| C. Agents running too slowly | |
| D. Agents accessing too many files | |

**Explanation**: Agent sprawl is an enterprise anti-pattern where teams produce dozens of AI agents without coordination, leading to redundancy, maintenance burden, and difficulty understanding which agent to use for what purpose.

<details>
<summary>Citation [Tier 2 - alpha-forge] (90% confidence)</summary>

<strong>Source</strong>: RFC: Reduce Pre-Defined Subagent Count<br>
<strong>URL</strong>: <a href="https://github.com/EonLabs-Spartan/alpha-forge/issues/123">RFC: Reduce Pre-Defined Subagent Count</a><br>
<strong>Section</strong>: Problem Statement<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Agent sprawl is an enterprise anti-pattern where teams produce dozens of AI agents without centralized organization, leading to redundancy and maintenance burden."</blockquote>

</details>

---

### Q17. According to Anthropic, when is multi-agent architecture appropriate?

| Option | |
| ------ | --- |
| A. Always, for any complex task | |
| **B. Only when truly parallel, independent subtasks exist** | ✓ |
| C. When a single agent is too slow | |
| D. When the context window is limited | |

**Explanation**: Multi-agent architecture is appropriate when you have subtasks that can run in parallel and don't require shared context. For most tasks, a single agent with careful prompting is more effective.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: When (not) to use agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Multi-agent systems can be appropriate when you have truly parallel, independent subtasks. For most applications, start with a single agent."</blockquote>

</details>

---

### Q18. What makes single-agent architecture preferable for most tasks?

| Option | |
| ------ | --- |
| A. Lower cost per request | |
| **B. Simplicity, transparency, and holistic reasoning** | ✓ |
| C. Faster execution speed | |
| D. Easier debugging | |

**Explanation**: Single-agent architecture is preferred because it's simpler to reason about, the agent has full context for holistic decision-making, and its actions are more transparent. Multi-agent adds complexity that's often unnecessary.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Principles<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Maintain simplicity in your agentic system. Start with the simplest solution that could work, then add complexity only when needed."</blockquote>

</details>

---

### Q19. Multi-agent adds value when subtasks are what?

| Option | |
| ------ | --- |
| A. Sequential and dependent on each other | |
| **B. Parallelizable and truly independent** | ✓ |
| C. Simple and repetitive | |
| D. User-facing and interactive | |

**Explanation**: Multi-agent systems add value when subtasks can run in parallel without needing to share context. If tasks are sequential or dependent, a single agent is more effective.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Multi-agent patterns<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Multi-agent systems excel when you have independent, parallelizable subtasks that don't require shared state."</blockquote>

</details>

---

### Q20. What is Anthropic's first principle for building effective agents?

| Option | |
| ------ | --- |
| **A. Maintain simplicity in agent design** | ✓ |
| B. Maximize tool access | |
| C. Use the largest context window available | |
| D. Parallelize all operations | |

**Explanation**: Anthropic's first principle is simplicity: start with the simplest solution that could work, then add complexity only when needed. Many tasks that seem to require agents can be solved with simpler approaches.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Principles for building effective agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Maintain simplicity in your agentic system. Start with the simplest solution that could work."</blockquote>

</details>

---

### Q21. What does 'transparency' mean in agent architecture according to Anthropic?

| Option | |
| ------ | --- |
| A. Showing all source code to users | |
| **B. Agent actions and reasoning are visible and understandable** | ✓ |
| C. Logging all API calls to a database | |
| D. Open-source licensing requirements | |

**Explanation**: Transparency means that the agent's actions, decisions, and reasoning process should be visible and understandable to developers and users, making debugging and trust-building possible.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Principles for building effective agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Design for transparency: make agent actions and reasoning visible and understandable."</blockquote>

</details>

---

### Q22. What is ACI (Agent-Computer Interface) design?

| Option | |
| ------ | --- |
| A. Graphical user interface for agents | |
| **B. Careful design of how agents interact with tools and environments** | ✓ |
| C. API specification format | |
| D. Memory management protocol | |

**Explanation**: ACI design focuses on how agents interact with their tools and environment. Well-designed ACIs make it easy for agents to understand tool capabilities, receive clear feedback, and recover from errors.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Agent-Computer Interface (ACI) design<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Just as good UI design is critical for human-computer interaction, ACI design is critical for agent-computer interaction."</blockquote>

</details>

---


---

*This answer key is auto-generated from the [quiz source files](https://github.com/terrylica/bruntwork-claude-screening/tree/main/quiz-data).*
