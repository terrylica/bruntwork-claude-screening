---
title: Quiz Answer Key & Review
permalink: /review/
toc: true
toc_sticky: true
---

<style>
.citation {
  font-size: 0.8em;
  margin: 0.5em 0;
  padding: 0.75em;
  background: rgba(128,128,128,0.1);
  border-radius: 4px;
  border-left: 3px solid #666;
}
.citation summary {
  cursor: pointer;
  font-weight: 500;
  color: #888;
}
.citation blockquote {
  font-size: 0.95em;
  margin: 0.5em 0;
  font-style: italic;
}
</style>

> This page contains all correct answers with explanations and authoritative citations.
> Use this as a learning resource alongside the [assessment quizzes](./).

*Generated: 2026-02-03 07:06*

---

## Statistics

| Metric | Value |
| ------ | ----- |
| Total Questions | 89 |
| Domains | 5 |
| Citation Coverage | 100% |
| Tier 1 (Official) | 93% |
| Tier 2 (Internal) | 7% |
| Tier 3 (Community) | 0% |

---

## Table of Contents

| # | Domain | Questions | Weight | Jump |
| - | ------ | --------- | ------ | ---- |
| 1 | Prompting & Context | 15 | 25% | [Go](#effective-prompting) |
| 2 | Safety & Control | 16 | 20% | [Go](#safety-autonomy) |
| 3 | Advanced Architecture | 29 | 20% | [Go](#agents-deep-dive) |
| 4 | Hooks & Automation | 17 | 15% | [Go](#hooks-lifecycle) |
| 5 | Integration & Workflows | 12 | 15% | [Go](#integration-tools) |

---

## Effective Claude Code Prompting

*Domain: Prompting & Context | Weight: 25%*

### Q1. What is the most important factor for Claude Code's success rate according to Anthropic?

| Option | |
| ------ | --- |
| A. Specifying which tools to use | |
| **B. Clear, specific instructions about what you want** | ✓ |
| C. Using the latest model version | |
| D. Running in a specific environment | |

**Explanation**: WHY THIS MATTERS: Claude Code v2.1+ autonomously selects tools based on context - you don't need to micromanage. What matters is WHAT you want, not HOW to do it. According to Anthropic: 'Claude Code's success rate improves significantly with more specific instructions, especially on first attempts.' Focus your energy on describing outcomes clearly, not on directing implementation details.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Be specific in your instructions<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Claude Code's success rate improves significantly with more specific instructions, especially on first attempts. Giving clear directions upfront reduces the need for course corrections later."</blockquote>

</details>

---

### Q2. What is CLAUDE.md and why is it important?

| Option | |
| ------ | --- |
| A. A log file that records all Claude Code sessions | |
| **B. A special file automatically pulled into context at session start** | ✓ |
| C. A configuration file for Claude Code CLI settings | |
| D. A markdown template for documentation | |

**Explanation**: WHY THIS MATTERS: CLAUDE.md is your project's 'memory' - it persists across sessions and automatically loads into context. This is where you put project conventions, common commands, code style guidelines, and testing instructions. It's the difference between repeating yourself every session and having Claude understand your project from the start. This single file can dramatically improve Claude's effectiveness on your specific codebase.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Use CLAUDE.md for context<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"CLAUDE.md is a special file that Claude automatically pulls into context when starting a conversation. This makes it an ideal place for documenting repository etiquette, developer environment setup, and any unexpected behaviors particular to the project."</blockquote>

</details>

---

### Q3. When Claude 4.5 seems too brief or skips actions, what should you do?

| Option | |
| ------ | --- |
| A. Switch to a different model | |
| **B. Add more explicit instructions for the behavior you want** | ✓ |
| C. Use more technical jargon | |
| D. Report a bug to Anthropic | |

**Explanation**: WHY THIS MATTERS: Claude 4.5 models are trained for precise instruction following - they do what you ask, not what you might mean. If you want detailed explanations, ask for them. If you want Claude to implement changes rather than suggest them, say 'make these changes' not 'can you suggest changes?' This precise behavior is a feature - it gives you control - but requires being explicit about your expectations.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude 4.x Prompting Best Practices<br>
<strong>URL</strong>: <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices">Claude 4.x Prompting Best Practices</a><br>
<strong>Section</strong>: Be explicit with your instructions<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Claude 4.x models respond well to clear, explicit instructions. Being specific about your desired output can help enhance results. Customers who desire the 'above and beyond' behavior from previous Claude models might need to more explicitly request these behaviors."</blockquote>

</details>

---

### Q4. What's the recommended approach when you want Claude to make changes to code?

| Option | |
| ------ | --- |
| A. Say 'can you suggest some changes?' | |
| **B. Say 'make these changes' or 'change this function to...'** | ✓ |
| C. Paste the code and wait | |
| D. Always use specific tool names | |

**Explanation**: WHY THIS MATTERS: Claude 4.5 follows instructions precisely. 'Can you suggest changes?' results in suggestions. 'Make these changes' results in actual edits. This isn't a limitation - it's intentional design that lets users choose between analysis and action. In vibe coding, you typically want action: 'Fix this bug', 'Add logging here', 'Refactor this function'. Be direct about your intent.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude 4.x Prompting Best Practices<br>
<strong>URL</strong>: <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices">Claude 4.x Prompting Best Practices</a><br>
<strong>Section</strong>: Tool usage patterns<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"If you say 'can you suggest some changes,' it will sometimes provide suggestions rather than implementing them—even if making changes might be what you intended. For Claude to take action, be more explicit: 'Change this function to improve its performance.'"</blockquote>

</details>

---

### Q5. Why should you explain WHY you want something, not just WHAT?

| Option | |
| ------ | --- |
| A. It makes the prompt longer which is better | |
| **B. Claude can generalize from the explanation to similar situations** | ✓ |
| C. It's required for tool access | |
| D. It improves response speed | |

**Explanation**: WHY THIS MATTERS: Providing context about motivation helps Claude understand your goals beyond the literal request. If you say 'never use ellipses because this will be read by text-to-speech,' Claude understands the underlying constraint (audio output) and can apply similar judgment to other formatting decisions. Context is currency in vibe coding - it compounds into better decisions throughout your session.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude 4.x Prompting Best Practices<br>
<strong>URL</strong>: <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices">Claude 4.x Prompting Best Practices</a><br>
<strong>Section</strong>: Add context to improve performance<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude 4.x models better understand your goals. Claude is smart enough to generalize from the explanation."</blockquote>

</details>

---

### Q6. What should you NOT worry about when using Claude Code effectively?

| Option | |
| ------ | --- |
| A. Being specific about what you want | |
| B. Providing project context in CLAUDE.md | |
| **C. Specifying which internal tools Claude should use** | ✓ |
| D. Explaining your constraints and goals | |

**Explanation**: WHY THIS MATTERS: Claude Code v2.1+ has 'significantly improved native subagent orchestration capabilities' - it recognizes when tasks benefit from delegation and does so proactively. Telling Claude 'use the Grep tool' or 'spawn an Explore agent' is micromanagement that adds no value. Let Claude decide HOW while you focus on WHAT and WHY. This represents a fundamental shift from early AI coding tools.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude 4.x Prompting Best Practices<br>
<strong>URL</strong>: <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices">Claude 4.x Prompting Best Practices</a><br>
<strong>Section</strong>: Subagent orchestration<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Claude 4.5 models demonstrate significantly improved native subagent orchestration capabilities. These models can recognize when tasks would benefit from delegating work to specialized subagents and do so proactively without requiring explicit instruction."</blockquote>

</details>

---

### Q7. What does 'vibe coding' mean in the context of Claude Code?

| Option | |
| ------ | --- |
| A. Writing code while listening to music | |
| **B. Describing projects in natural language instead of writing code directly** | ✓ |
| C. A specific programming language | |
| D. A debugging technique | |

**Explanation**: WHY THIS MATTERS: Vibe coding, coined by Andrej Karpathy in February 2025, represents a paradigm shift. Instead of writing code line-by-line, you describe what you want and let AI handle implementation. Claude Code transformed this from concept to practice: 'You just tell it to do something, and it works.' Understanding this paradigm helps you work WITH the tool rather than fighting it.

<details open class="citation">
<summary>Citation [Tier 2 - Axios] (90% confidence)</summary>

<strong>Source</strong>: Anthropic's Claude Code transforms vibe coding<br>
<strong>URL</strong>: <a href="https://www.axios.com/2026/01/07/anthropics-claude-code-vibe-coding">Anthropic's Claude Code transforms vibe coding</a><br>
<strong>Section</strong>: Overview<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"The term vibe coding—describing projects in natural language instead of code—was coined by Andrej Karpathy on February 3, 2025. Claude Code changed this by letting users talk directly to an agent. 'You just tell it to do something, and it works.'"</blockquote>

</details>

---

### Q8. What should you ask Claude to do BEFORE it starts implementing a complex feature?

| Option | |
| ------ | --- |
| A. List all the tools it will use | |
| **B. Make a plan and wait for your confirmation before coding** | ✓ |
| C. Estimate how long it will take | |
| D. Show its system prompt | |

**Explanation**: WHY THIS MATTERS: For complex tasks, alignment before implementation saves massive rework. Explicitly tell Claude 'don't code until you've confirmed the plan looks good.' This creates a checkpoint where you can catch misunderstandings before they become 500 lines of wrong code. It's the difference between steering and chasing. Course corrections mid-implementation are always more expensive.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Ask Claude to make a plan<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Ask Claude to make a plan before coding. Explicitly tell it not to code until you've confirmed its plan looks good."</blockquote>

</details>

---

### Q9. For long-running autonomous tasks, what should you provide to Claude?

| Option | |
| ------ | --- |
| A. A strict time limit | |
| **B. A way to verify results without human feedback** | ✓ |
| C. Detailed step-by-step instructions | |
| D. Access to external APIs | |

**Explanation**: WHY THIS MATTERS: Autonomous operation requires a verification loop. If you want Claude to run for hours without supervision, it needs to know if it's on track. Tests, linters, type checkers - these provide objective feedback. Without verification, autonomous work drifts. The write-test cycle (write code, run it, check output, repeat) is what makes extended autonomous operation reliable.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Autonomous workflows<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"If you want Claude Code to run something autonomously, you need to give it a way to verify results. The key is completing the write-test cycle: write code, run it, check the output, and repeat."</blockquote>

</details>

---

### Q10. What belongs in CLAUDE.md for your project?

| Option | |
| ------ | --- |
| A. API keys and credentials | |
| **B. Project conventions, common commands, code style, testing instructions** | ✓ |
| C. Full conversation history | |
| D. Debug logs from previous sessions | |

**Explanation**: WHY THIS MATTERS: CLAUDE.md is your project's knowledge base - information that should persist across all sessions. Include branch naming conventions, how to run tests, which compilers work, unusual project behaviors. Don't include secrets (use environment variables) or transient data. A well-maintained CLAUDE.md turns every Claude Code session into one with a developer who already knows your project.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Using CLAUDE.md<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"CLAUDE.md is an ideal place for documenting repository etiquette (branch naming, merge vs. rebase), developer environment setup (pyenv use, which compilers work), common bash commands, core files and utility functions, code style guidelines, and testing instructions."</blockquote>

</details>

---

### Q11. What should you do when Claude's responses start 'forgetting' earlier instructions or making repeated mistakes?

| Option | |
| ------ | --- |
| A. Report a bug to Anthropic | |
| B. Keep correcting in the same session until it works | |
| **C. Use /clear to reset context and start fresh with a better prompt** | ✓ |
| D. Switch to a different AI model | |

**Explanation**: WHY THIS MATTERS: As context fills, Claude's performance degrades - this is the 'Lost in the Middle' effect where instructions in long contexts get less attention. A session cluttered with failed approaches is less effective than a fresh start. After two failed corrections, /clear and rewrite your prompt incorporating what you learned. Clean context + better prompt almost always outperforms accumulated corrections.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Context Management<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"LLM performance degrades as context fills. When the context window is getting full, Claude may start 'forgetting' earlier instructions. After two failed corrections, /clear and write a better initial prompt incorporating what you learned."</blockquote>

</details>

---

### Q12. What does the /init command do in Claude Code?

| Option | |
| ------ | --- |
| A. Initializes a new git repository | |
| **B. Scans the codebase and generates a starter CLAUDE.md file** | ✓ |
| C. Resets all Claude Code settings to defaults | |
| D. Creates a new project from a template | |

**Explanation**: WHY THIS MATTERS: /init is the fastest path to context-aware Claude sessions. It automatically detects your tech stack, project structure, build commands, and common patterns, creating a CLAUDE.md foundation you can customize. This is universally recommended as the first step in any new project - it gives Claude immediate understanding of your codebase without manual documentation.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code CLI Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/cli-reference">Claude Code CLI Reference</a><br>
<strong>Section</strong>: Commands<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"The /init command scans your codebase and generates a starter CLAUDE.md file with detected project conventions, build commands, and structure."</blockquote>

</details>

---

### Q13. According to Anthropic, what is the 'single highest-leverage thing' you can do to improve Claude Code's performance?

| Option | |
| ------ | --- |
| A. Use the latest model version | |
| **B. Provide tests, screenshots, or expected outputs so Claude can verify its own work** | ✓ |
| C. Write detailed step-by-step instructions | |
| D. Grant maximum permissions for faster execution | |

**Explanation**: WHY THIS MATTERS: Claude performs dramatically better when it can verify its own work. Without clear success criteria, it might produce something that looks right but doesn't work. Tests, linters, type checkers, and screenshots create objective feedback loops - the write-test cycle (write code, run it, check output, repeat) is what enables reliable autonomous operation. You become the reviewer, not the only feedback mechanism.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Verification<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"This is the single highest-leverage thing you can do. Claude performs dramatically better when it can verify its own work."</blockquote>

</details>

---

### Q14. How do you resume your most recent Claude Code conversation?

| Option | |
| ------ | --- |
| A. Run 'claude --last' | |
| **B. Run 'claude --continue' or 'claude -c'** | ✓ |
| C. Press Ctrl+R in the terminal | |
| D. Sessions cannot be resumed | |

**Explanation**: WHY THIS MATTERS: Session continuity prevents losing context between work sessions. The --continue flag (or -c shorthand) picks up exactly where you left off, including conversation history, file context, and any in-progress tasks. This is essential for long-running projects where you work across multiple terminal sessions or days.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code CLI Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/cli-reference">Claude Code CLI Reference</a><br>
<strong>Section</strong>: Session Management<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Use --continue or -c to resume the most recent conversation in the current directory."</blockquote>

</details>

---

### Q15. What happens when your CLAUDE.md file becomes too long with too many instructions?

| Option | |
| ------ | --- |
| A. Claude processes it faster due to more context | |
| **B. Claude ignores important rules because they get lost in the noise** | ✓ |
| C. Claude automatically summarizes the content | |
| D. Nothing - Claude handles any length equally well | |

**Explanation**: WHY THIS MATTERS: A bloated CLAUDE.md causes Claude to overlook important instructions due to the 'Lost in the Middle' attention pattern. Research suggests LLMs can follow ~150-200 instructions consistently. For each line, ask: 'Would removing this cause Claude to make mistakes?' If not, cut it. If Claude keeps doing something wrong despite having a rule against it, your file is probably too long.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: CLAUDE.md Best Practices<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Bloated CLAUDE.md files cause Claude to ignore your actual instructions! If Claude keeps doing something you don't want despite having a rule against it, the file is probably too long."</blockquote>

</details>

---


## Safety & Autonomy

*Domain: Safety & Control | Weight: 20%*

### Q1. What is Claude Code's default permission behavior?

| Option | |
| ------ | --- |
| A. All operations are allowed automatically | |
| **B. Asks permission for each action, with pre-approval available for known-safe operations** | ✓ |
| C. No operations are allowed without admin approval | |
| D. Permissions depend on your subscription tier | |

**Explanation**: WHY THIS MATTERS: Claude Code's permission system balances safety with usability. By default, you approve each action, maintaining full control. As you build trust, use /permissions to pre-approve safe operations without constant interruption. This isn't about distrust - it's about visibility. Even experienced users appreciate knowing what's happening before irreversible changes occur.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security Reference</a><br>
<strong>Section</strong>: Permission-based architecture<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Claude Code uses strict read-only permissions by default. When additional actions are needed, Claude Code requests explicit permission. You can customize the allowlist to permit additional tools that you know are safe."</blockquote>

</details>

---

### Q2. What directory restriction applies to Claude Code write operations?

| Option | |
| ------ | --- |
| A. Can write anywhere on the system | |
| **B. Can only write to the folder where it was started and subfolders** | ✓ |
| C. Can only write to /tmp | |
| D. Cannot write any files | |

**Explanation**: WHY THIS MATTERS: This sandbox prevents accidental damage outside your project. Claude can read system libraries and other projects (useful for understanding patterns), but writes are confined to the working directory. This means a bug in Claude's reasoning can't corrupt unrelated projects or system files. The asymmetry is intentional: broad read access for context, narrow write access for safety.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security Reference</a><br>
<strong>Section</strong>: Permission-based architecture<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Claude Code can only write to the folder where it was started and its subfolders—it cannot modify files in parent directories without explicit permission. While Claude Code can read files outside the working directory (useful for accessing system libraries), write operations are strictly confined to the project scope."</blockquote>

</details>

---

### Q3. Which git operations should NEVER be done without explicit user request?

| Option | |
| ------ | --- |
| A. git status, git diff | |
| B. git add, git log | |
| **C. git push --force, git reset --hard, git clean -f** | ✓ |
| D. git branch, git checkout | |

**Explanation**: WHY THIS MATTERS: These commands are destructive and often irreversible. 'git push --force' can overwrite teammates' work. 'git reset --hard' discards uncommitted changes permanently. 'git clean -f' deletes untracked files. AI should never make these decisions autonomously - the consequences are too severe. Even experienced developers pause before running these commands.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Git Safety Protocol<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"NEVER run destructive git commands (push --force, reset --hard, checkout ., restore ., clean -f, branch -D) unless the user explicitly requests these actions."</blockquote>

</details>

---

### Q4. When should Claude Code commit changes to git?

| Option | |
| ------ | --- |
| A. Automatically after every file change | |
| B. At the end of each session | |
| **C. Only when the user explicitly asks** | ✓ |
| D. After completing each feature | |

**Explanation**: WHY THIS MATTERS: Commits are checkpoints in your project's history. Users have different workflows - some squash commits, some use conventional commits, some want to review changes before committing. AI auto-committing creates messy history and removes user control. The rule is simple: if you're unsure whether to commit, ask. This feedback evolved from users who found proactive commits invasive.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Git Safety Protocol<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Only create commits when requested by the user. If unclear, ask first. NEVER commit changes unless the user explicitly asks you to."</blockquote>

</details>

---

### Q5. What should happen BEFORE running a command that modifies many files?

| Option | |
| ------ | --- |
| A. Just run it - Claude Code has undo capability | |
| **B. Explain the scope and get confirmation from the user** | ✓ |
| C. Create a backup of every file first | |
| D. Test on one file then automatically do the rest | |

**Explanation**: WHY THIS MATTERS: Bulk operations multiply risk. A typo in a regex could rename hundreds of files incorrectly. Before any mass operation, clearly state: 'This will affect N files matching pattern X.' Let the user confirm scope. This transparency prevents the 'wait, I didn't want THAT' moment. The user bears responsibility for approving scope; AI bears responsibility for clearly communicating it.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security Reference</a><br>
<strong>Section</strong>: User responsibility<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Claude Code only has the permissions you grant it. You're responsible for reviewing proposed code and commands for safety before approval."</blockquote>

</details>

---

### Q6. You notice code with a potential SQL injection vulnerability. What should you do?

| Option | |
| ------ | --- |
| A. Fix it silently to avoid alarming the user | |
| **B. Point it out and offer to fix it** | ✓ |
| C. Ignore it - security is not Claude's concern | |
| D. Stop all work until it's addressed | |

**Explanation**: WHY THIS MATTERS: Security vulnerabilities need visibility, not silent fixes. If you fix SQL injection without telling the user, they won't understand the risk, won't audit for similar issues, and won't learn to prevent them. Flag it clearly, explain the risk, offer to fix, but let the user acknowledge the issue. This creates teachable moments and maintains user awareness of their codebase's security.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security Reference</a><br>
<strong>Section</strong>: Security best practices<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Review all suggested changes before approval. Use project-specific permission settings for sensitive repositories. Always maintain good security practices when working with any AI tool."</blockquote>

</details>

---

### Q7. What are the 3 levels of Claude Code autonomy control?

| Option | |
| ------ | --- |
| A. Free, Standard, Premium | |
| **B. Approve each action, Pre-approve safe tools, Skip permissions entirely** | ✓ |
| C. Read, Write, Execute | |
| D. View, Edit, Admin | |

**Explanation**: WHY THIS MATTERS: You control how much autonomy Claude has. Default: approve each action (maximum safety). Intermediate: pre-approve known-safe tools via /permissions (balanced). Maximum: --dangerously-skip-permissions for isolated/trusted environments (use with caution). Choose based on your risk tolerance and environment. Higher autonomy = faster workflows but less oversight.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Controlling autonomy<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Users can toggle between: Asking permission for each tool use (default), Pre-approving safe tools via /permissions, Using --dangerously-skip-permissions for trusted workflows in isolated environments."</blockquote>

</details>

---

### Q8. What does 'supervised autonomy' mean for AI coding tools?

| Option | |
| ------ | --- |
| A. A human watches every action in real-time | |
| **B. You provide goals and guardrails, Claude executes, you approve/reject at decision points** | ✓ |
| C. Claude asks permission for every single operation | |
| D. Multiple humans review all AI-generated code | |

**Explanation**: WHY THIS MATTERS: Supervised autonomy is the sweet spot for productivity. You're not watching every file read, but you're approving destructive actions. You set the goal ('fix authentication'), Claude executes independently, and you review at checkpoints. This balance preserves safety while delivering substantial productivity gains - you're steering, not typing.

<details open class="citation">
<summary>Citation [Tier 2 - Community] (90% confidence)</summary>

<strong>Source</strong>: Claude Code 2.0 Best Practices<br>
<strong>URL</strong>: <a href="https://skywork.ai/blog/claude-code-2-0-best-practices-ai-coding-workflow-2025/">Claude Code 2.0 Best Practices</a><br>
<strong>Section</strong>: 2025 Updates<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"The most interesting practical tools in 2025 cluster around Level 3-4: supervised autonomy where you provide goals and guardrails, the agent executes independently, and you approve/reject at decision points. This balance preserves safety while delivering substantial productivity gains."</blockquote>

</details>

---

### Q9. What is the user's responsibility when using Claude Code?

| Option | |
| ------ | --- |
| A. None - Claude handles everything safely | |
| **B. Review proposed code and commands for safety before approval** | ✓ |
| C. Only verify syntax correctness | |
| D. Write all the code manually | |

**Explanation**: WHY THIS MATTERS: AI is a powerful tool, not a replacement for human judgment. You approve what gets executed. You verify the logic makes sense. You catch the edge cases AI might miss. This isn't about distrust - it's about accountability. When you approve a command, you're taking responsibility for its effects. This shared responsibility model is what makes human-AI collaboration safe and effective.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security Reference</a><br>
<strong>Section</strong>: User responsibility<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Claude Code only has the permissions you grant it. You're responsible for reviewing proposed code and commands for safety before approval."</blockquote>

</details>

---

### Q10. What does Claude Code 4.5's 'overeagerness' tendency mean, and how should you address it?

| Option | |
| ------ | --- |
| A. It runs too slowly - request faster execution | |
| **B. It tends to overengineer by adding extra files and unnecessary abstractions** | ✓ |
| C. It asks too many questions - tell it to proceed without asking | |
| D. It refuses to make changes - grant more permissions | |

**Explanation**: WHY THIS MATTERS: Claude Opus 4.5 sometimes creates extra files, adds unnecessary abstractions, or builds in flexibility that wasn't requested. This 'helpful' overengineering creates bloat and maintenance burden. Address it by being explicit: 'Keep solutions simple. Only make changes that are directly requested. Don't add features beyond what was asked.' The fix is prompt engineering, not configuration.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude 4.x Prompting Best Practices<br>
<strong>URL</strong>: <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices">Claude 4.x Prompting Best Practices</a><br>
<strong>Section</strong>: Overeagerness and file creation<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Claude Opus 4.5 has a tendency to overengineer by creating extra files, adding unnecessary abstractions, or building in flexibility that wasn't requested. If you're seeing this undesired behavior, add explicit prompting to keep solutions minimal: 'Avoid over-engineering. Only make changes that are directly requested.'"</blockquote>

</details>

---

### Q11. What is the checkpoint system in Claude Code and how do you use it?

| Option | |
| ------ | --- |
| A. A debugging tool for viewing API calls | |
| **B. Automatic code state saving before changes - press Esc twice or use /rewind to restore** | ✓ |
| C. A manual save feature requiring explicit /checkpoint command | |
| D. A git integration for automatic commits | |

**Explanation**: WHY THIS MATTERS: Checkpoints are your safety net for Claude's edits. Every time Claude modifies code, the previous state is automatically saved. If something goes wrong, press Escape twice or use /rewind to restore - no manual saving required. This enables confident experimentation because you can always undo. Note: checkpoints only apply to Claude's edits, not user modifications or bash commands.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Enabling Claude Code to Work More Autonomously<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously">Enabling Claude Code to Work More Autonomously</a><br>
<strong>Section</strong>: Checkpoints<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Checkpoints automatically save code state before each change. Press Esc twice or use /rewind to restore. You can restore code, conversation, or both."</blockquote>

</details>

---

### Q12. What are the two boundaries enforced by Claude Code's sandboxing feature?

| Option | |
| ------ | --- |
| A. Memory isolation and CPU limits | |
| **B. Filesystem isolation and network isolation** | ✓ |
| C. Read-only mode and audit logging | |
| D. User isolation and process isolation | |

**Explanation**: WHY THIS MATTERS: Sandboxing confines Claude to specific directories (filesystem isolation) and approved network destinations (network isolation). This achieved 84% reduction in permission prompts internally at Anthropic while maintaining security. On Linux it uses bubblewrap, on macOS it uses seatbelt. Run /sandbox to configure. This is the foundation for safe autonomous operation.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Sandboxing<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-sandboxing">Claude Code Sandboxing</a><br>
<strong>Section</strong>: Overview<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Sandboxing enforces filesystem isolation (Claude can only access/modify specific directories) and network isolation (only connect to approved servers), achieving 84% reduction in permission prompts."</blockquote>

</details>

---

### Q13. What is a common Claude Code behavior that power users warn about during test-driven development?

| Option | |
| ------ | --- |
| A. Claude refuses to write tests | |
| **B. Claude may modify tests to match buggy code instead of fixing the code** | ✓ |
| C. Claude only writes unit tests, never integration tests | |
| D. Claude requires manual test file creation | |

**Explanation**: WHY THIS MATTERS: Claude optimizes for passing tests, but sometimes takes the path of least resistance by weakening assertions rather than fixing bugs. This is why power users recommend reviewing ALL test modifications carefully. When tests fail, verify Claude is fixing the code, not the tests. Use TDD approach: write tests first, review them thoroughly before implementation.

<details open class="citation">
<summary>Citation [Tier 2 - Community] (90% confidence)</summary>

<strong>Source</strong>: Claude Code Gotchas<br>
<strong>URL</strong>: <a href="https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/">Claude Code Gotchas</a><br>
<strong>Section</strong>: Test Manipulation<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Be very wary of changes to your test files. Claude writes failing tests, then modifies tests to match buggy code instead of fixing the code."</blockquote>

</details>

---

### Q14. When using --dangerously-skip-permissions for autonomous operation, what environment does Anthropic recommend?

| Option | |
| ------ | --- |
| A. Your main development machine with full internet access | |
| **B. A container or VM without internet access** | ✓ |
| C. A staging server with production data | |
| D. Any environment with version control | |

**Explanation**: WHY THIS MATTERS: Autonomous operation without permission checks creates prompt injection and data exfiltration risks. Anthropic explicitly recommends using --dangerously-skip-permissions 'in a container without internet access.' Container isolation limits blast radius, and network isolation prevents data exfiltration. Version control alone isn't sufficient protection against malicious or unintended operations.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security</a><br>
<strong>Section</strong>: Autonomous Mode<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Use --dangerously-skip-permissions only in a container without internet access where damage is contained."</blockquote>

</details>

---

### Q15. What is the purpose of managed-settings.json in enterprise Claude Code deployments?

| Option | |
| ------ | --- |
| A. Store user preferences that can be customized | |
| **B. Enforce organization-wide policies that cannot be overridden by local settings** | ✓ |
| C. Cache API responses for faster performance | |
| D. Store authentication tokens securely | |

**Explanation**: WHY THIS MATTERS: Enterprise deployments need consistent security policies across all users. Managed-settings.json files are deployed to system directories and cannot be overridden by developers. This ensures organization-wide tool permissions, file access restrictions, and MCP server configurations are enforced uniformly. Settings hierarchy: Enterprise policies > CLI flags > Local > Shared > User.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Settings<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/settings">Claude Code Settings</a><br>
<strong>Section</strong>: Managed Settings<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Managed settings in /Library/Application Support/ClaudeCode/managed-settings.json (macOS) or /etc/claude-code/managed-settings.json (Linux) enforce organization-wide policies that cannot be overridden."</blockquote>

</details>

---

### Q16. Given permission config: allow: ['Bash'], ask: ['Bash(rm *)'], what happens when Claude tries to run 'rm -rf /tmp/test'?

| Option | |
| ------ | --- |
| A. Executes without prompting (Bash is allowed) | |
| **B. Permission prompt appears (content-level 'ask' takes precedence over tool-level 'allow')** | ✓ |
| C. Command is blocked entirely | |
| D. Error due to conflicting rules | |

**Explanation**: WHY THIS MATTERS: Understanding permission precedence is critical for safe configuration. As of v2.1.27, content-level rules take precedence over tool-level rules. This means allow: ['Bash'] grants general bash access, but ask: ['Bash(rm *)'] still prompts for rm commands. This layered approach lets you grant broad permissions while maintaining guardrails on dangerous operations.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Changelog v2.1.27<br>
<strong>URL</strong>: <a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code Changelog v2.1.27</a><br>
<strong>Section</strong>: v2.1.27<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Permissions now respect content-level 'ask' over tool-level 'allow'. Previously allow: ['Bash'], ask: ['Bash(rm *)'] allowed all bash commands, but will now permission prompt for rm."</blockquote>

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

**Explanation**: WHY THIS MATTERS: This distinction affects how you design your workflow. Pre-defined agents are like 'specialists on call' - when the right situation arises, they activate automatically. On-demand subagents are like 'contracted help' - you explicitly spawn them for specific tasks. Pre-defined agents reduce cognitive load (you don't have to remember to invoke them), while on-demand gives precise control. Choose based on how predictable your needs are.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Sub-agents<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/sub-agents">Claude Code Sub-agents</a><br>
<strong>Section</strong>: Pre-defined agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Pre-defined agents are stored in your project's .claude/agents/ directory. When Claude detects that a task matches an agent's capabilities, it automatically activates that agent."</blockquote>

</details>

---

### Q2. Where are Claude Code pre-defined agents stored?

| Option | |
| ------ | --- |
| A. ~/.claude/skills/ | |
| B. ~/.claude/plugins/ | |
| **C. .claude/agents/ in project root** | ✓ |
| D. ~/.config/claude/agents/ | |

**Explanation**: WHY THIS MATTERS: Project-root storage (.claude/agents/) means agents are version-controlled with your code. When teammates clone the repo, they get the same specialized agents. This is intentionally different from skills (which can be global). Project-specific agents encode project-specific knowledge that shouldn't leak to other codebases.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Sub-agents<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/sub-agents">Claude Code Sub-agents</a><br>
<strong>Section</strong>: Pre-defined agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Pre-defined agents are stored in your project's .claude/agents/ directory."</blockquote>

</details>

---

### Q3. What happens when a pre-defined agent's trigger pattern matches a user request?

| Option | |
| ------ | --- |
| A. User is prompted to approve activation | |
| **B. Agent auto-activates without explicit user request** | ✓ |
| C. Main agent pauses execution | |
| D. Session terminates for safety | |

**Explanation**: WHY THIS MATTERS: Auto-activation creates seamless experiences. Instead of 'please use the migration agent,' you just say 'migrate the database schema' and Claude recognizes the pattern. This reduces friction and cognitive load - you describe what you want, and the right specialist appears. The magic is in the trigger patterns, which let you define precisely when each agent should activate.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Sub-agents<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/sub-agents">Claude Code Sub-agents</a><br>
<strong>Section</strong>: Pre-defined agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"When Claude detects that a task matches an agent's capabilities, it automatically activates that agent."</blockquote>

</details>

---

### Q4. What is the 'context gatekeeping' anti-pattern in multi-agent systems?

| Option | |
| ------ | --- |
| A. Limiting token usage to save costs | |
| B. Restricting tool access for security | |
| **C. Subagents hiding context from the main orchestrator** | ✓ |
| D. Caching conversation history for performance | |

**Explanation**: WHY THIS MATTERS: This is the #1 anti-pattern in multi-agent systems. Imagine a research agent finding a security vulnerability but summarizing it as 'minor issues found.' The orchestrator never learns the severity, so the final response downplays a critical problem. Context gatekeeping happens accidentally when subagents over-summarize. The fix: subagents should report findings with enough detail for the parent to make informed decisions.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building a Multi-Agent Research System<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/research/building-a-multi-agent-research-system">Building a Multi-Agent Research System</a><br>
<strong>Section</strong>: Coordinator Design<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"The coordinator agent needs visibility into all research findings to synthesize a coherent response. Subagents that hide context prevent holistic decision-making."</blockquote>

</details>

---

### Q5. Why does context gatekeeping reduce agent effectiveness?

| Option | |
| ------ | --- |
| A. Increases latency significantly | |
| B. Uses more tokens than necessary | |
| **C. Prevents holistic reasoning across domain boundaries** | ✓ |
| D. Causes memory leaks in long sessions | |

**Explanation**: WHY THIS MATTERS: The value of a coordinator is drawing connections across domains - 'the auth system and the payment system both have this vulnerability.' If subagents only report isolated findings, the coordinator becomes a dumb aggregator. Holistic reasoning requires holistic visibility. This is why simpler architectures (single agent with full context) often outperform complex multi-agent systems with context loss.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building a Multi-Agent Research System<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/research/building-a-multi-agent-research-system">Building a Multi-Agent Research System</a><br>
<strong>Section</strong>: Coordinator Design<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"The coordinator agent needs visibility into all research findings to synthesize a coherent response that draws connections across domains."</blockquote>

</details>

---

### Q6. What is the recommended alternative to context gatekeeping?

| Option | |
| ------ | --- |
| A. Use more subagents for parallelism | |
| **B. Keep context in main agent, use subagents only for isolated subtasks** | ✓ |
| C. Increase context window size | |
| D. Implement caching layers between agents | |

**Explanation**: WHY THIS MATTERS: The key word is 'isolated.' If subtasks are truly independent (scan these 5 repos for vulnerabilities), parallelization helps without context loss. But if subtasks inform each other (understand the architecture THEN plan the migration), running them in parallel loses the dependency. Default to keeping context in the main agent; only split when tasks are genuinely independent.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Agent architectures<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"The simplest architecture is a single agent that handles all tasks. For more complex scenarios, use orchestrator patterns where subagents handle isolated subtasks and report back."</blockquote>

</details>

---

### Q7. In the Multi-Agent Research System design, what was the key insight about subagent coordination?

| Option | |
| ------ | --- |
| **A. Parent agent must see and synthesize all findings** | ✓ |
| B. Each subagent should operate independently without coordination | |
| C. Subagents should communicate directly with each other | |
| D. Results should be aggregated externally | |

**Explanation**: WHY THIS MATTERS: Anthropic's multi-agent research system was their proving ground for these principles. The key insight: the coordinator seeing raw findings (not just summaries) let it connect dots that specialized agents missed individually. This is the architectural principle that should guide your multi-agent designs - synthesis happens at the top, not distributed across components.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building a Multi-Agent Research System<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/research/building-a-multi-agent-research-system">Building a Multi-Agent Research System</a><br>
<strong>Section</strong>: System Architecture<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"The coordinator agent synthesizes findings from all research agents to produce a coherent final answer."</blockquote>

</details>

---

### Q8. What is the fundamental difference between skills and subagents in Claude Code?

| Option | |
| ------ | --- |
| A. Skills are faster to execute | |
| B. Skills use fewer tokens | |
| **C. Skills run in main context, subagents have isolated context windows** | ✓ |
| D. Skills require user approval | |

**Explanation**: WHY THIS MATTERS: This is the most important architectural distinction in Claude Code. Skills EXPAND your main context (the checklist stays visible, the template persists). Subagents ISOLATE work (the exploration noise goes away, only results return). Choose skills when visibility matters; choose subagents when clean context matters. Most users overuse subagents when skills would work better.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code Skills</a><br>
<strong>Section</strong>: Skills vs Subagents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Skills run within the main conversation context, while subagents operate in isolated context windows with their own tool access."</blockquote>

</details>

---

### Q9. When should you use a skill instead of a subagent?

| Option | |
| ------ | --- |
| A. For complex multi-step tasks requiring autonomy | |
| **B. For checklists, templates, or context injection** | ✓ |
| C. For parallel execution of independent tasks | |
| D. For background processing | |

**Explanation**: WHY THIS MATTERS: Think about what happens AFTER the skill/subagent runs. Checklists need to stay visible so Claude (and you) can check items off. Templates need to persist for reference. But exploration output? You don't want 50 file reads cluttering your context - just the insights. Match the mechanism to the persistence need: skills for reference material, subagents for working memory.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code Skills</a><br>
<strong>Section</strong>: When to use skills<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Use skills for context injection, checklists, and templates where you want the information to remain in the main conversation."</blockquote>

</details>

---

### Q10. What happens to skill context after execution?

| Option | |
| ------ | --- |
| **A. It remains in the main conversation context** | ✓ |
| B. It is discarded after use | |
| C. It is saved to disk | |
| D. It is compressed for efficiency | |

**Explanation**: WHY THIS MATTERS: Persistence has cost and benefit. Skill content consumes your context window for the entire session - good when you need ongoing reference, bad when it's one-time information. Subagent context disappears after the task - good for keeping main context clean, bad when you need to reference intermediate findings later. Design accordingly: inject what you'll reference repeatedly, isolate what you'll use once.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code Skills</a><br>
<strong>Section</strong>: Context persistence<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Skill content is injected into the main conversation context and remains available throughout the session."</blockquote>

</details>

---

### Q11. According to Anthropic, when is multi-agent architecture appropriate?

| Option | |
| ------ | --- |
| A. Always, for any complex task | |
| **B. Only when truly parallel, independent subtasks exist** | ✓ |
| C. When a single agent is too slow | |
| D. When the context window is limited | |

**Explanation**: WHY THIS MATTERS: Multi-agent adds complexity: coordination overhead, context synchronization challenges, harder debugging. The payoff is parallelism and specialization. For most Claude Code tasks, a single agent is faster and more reliable because it maintains full context and doesn't need coordination. Reserve multi-agent for genuinely parallel tasks (scan 10 repos) or extreme specialization needs.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: When (not) to use agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Multi-agent systems can be appropriate when you have truly parallel, independent subtasks. For most applications, start with a single agent."</blockquote>

</details>

---

### Q12. What makes single-agent architecture preferable for most tasks?

| Option | |
| ------ | --- |
| A. Lower cost per request | |
| **B. Simplicity, transparency, and holistic reasoning** | ✓ |
| C. Faster execution speed | |
| D. Easier debugging | |

**Explanation**: WHY THIS MATTERS: This is Anthropic's hard-won wisdom. They tried complex multi-agent systems and often found simpler single-agent approaches worked better. Why? Full context enables holistic reasoning (seeing connections), transparency makes debugging possible (one context to inspect), and simplicity reduces failure modes (no coordination bugs). Start simple, add complexity only when proven necessary.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Principles<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Maintain simplicity in your agentic system. Start with the simplest solution that could work, then add complexity only when needed."</blockquote>

</details>

---

### Q13. Multi-agent adds value when subtasks are what?

| Option | |
| ------ | --- |
| A. Sequential and dependent on each other | |
| **B. Parallelizable and truly independent** | ✓ |
| C. Simple and repetitive | |
| D. User-facing and interactive | |

**Explanation**: WHY THIS MATTERS: The test for multi-agent is simple: can these tasks run at the exact same time without talking to each other? If yes (scan 5 independent codebases), parallelize. If no (understand the code, THEN plan the refactor), don't. Forcing parallel execution on dependent tasks creates worse results than sequential single-agent work because you lose the dependency information.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Multi-agent patterns<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Multi-agent systems excel when you have independent, parallelizable subtasks that don't require shared state."</blockquote>

</details>

---

### Q14. What is Anthropic's first principle for building effective agents?

| Option | |
| ------ | --- |
| **A. Maintain simplicity in agent design** | ✓ |
| B. Maximize tool access | |
| C. Use the largest context window available | |
| D. Parallelize all operations | |

**Explanation**: WHY THIS MATTERS: This principle fights the tendency to over-architect. 'I need a multi-agent system with specialized coordinators' often loses to 'I need a single Claude with a good CLAUDE.md file.' Complexity has costs: harder debugging, more failure modes, longer development time. Start simple. If it doesn't work, you've learned WHY you need complexity. If it does work, you've saved yourself massive overhead.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Principles for building effective agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Maintain simplicity in your agentic system. Start with the simplest solution that could work."</blockquote>

</details>

---

### Q15. What does 'transparency' mean in agent architecture according to Anthropic?

| Option | |
| ------ | --- |
| A. Showing all source code to users | |
| **B. Agent actions and reasoning are visible and understandable** | ✓ |
| C. Logging all API calls to a database | |
| D. Open-source licensing requirements | |

**Explanation**: WHY THIS MATTERS: Transparency enables debugging and builds trust. When something goes wrong, can you see WHY the agent made that decision? When it works, can you understand HOW so you can replicate it? Black-box agents that 'just work' become unmaintainable when they stop working. Claude Code's task tracking, verbose mode, and transcript logs all serve transparency - use them.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Principles for building effective agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Design for transparency: make agent actions and reasoning visible and understandable."</blockquote>

</details>

---

### Q16. What is ACI (Agent-Computer Interface) design?

| Option | |
| ------ | --- |
| A. Graphical user interface for agents | |
| **B. Careful design of how agents interact with tools and environments** | ✓ |
| C. API specification format | |
| D. Memory management protocol | |

**Explanation**: WHY THIS MATTERS: Just as bad UX frustrates humans, bad ACI frustrates agents. If a tool returns cryptic errors, the agent can't recover. If tool descriptions are vague, the agent misuses them. Claude Code's tools are designed with ACI principles: clear error messages, consistent output formats, predictable behavior. When building custom tools or MCP servers, apply the same care you'd apply to human UX.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Agent-Computer Interface (ACI) design<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Just as good UI design is critical for human-computer interaction, ACI design is critical for agent-computer interaction."</blockquote>

</details>

---

### Q17. How do you toggle the task list view in Claude Code?

| Option | |
| ------ | --- |
| A. Type /tasks in the prompt | |
| **B. Press Ctrl+T (or Cmd+T on Mac)** | ✓ |
| C. Click the Tasks icon in the sidebar | |
| D. Run claude --tasks from the terminal | |

**Explanation**: WHY THIS MATTERS: The task list is Claude Code's project management interface, showing up to 10 tasks with their status. Ctrl+T gives instant visibility into what Claude is tracking. This is especially valuable during complex multi-step work - you can see the plan, what's done, and what's blocked. It transforms Claude from a chat interface into a project dashboard.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Interactive Mode<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/interactive-mode">Claude Code Interactive Mode</a><br>
<strong>Section</strong>: Task Management<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Press Ctrl+T to toggle the task list view, which displays up to 10 tasks with their current status."</blockquote>

</details>

---

### Q18. What is the correct format for TaskCreate's 'subject' vs 'activeForm' fields?

| Option | |
| ------ | --- |
| A. Both should use past tense (e.g., 'Fixed the bug') | |
| **B. Subject: imperative (e.g., 'Fix the bug'), activeForm: present continuous (e.g., 'Fixing the bug')** | ✓ |
| C. Subject: noun phrase (e.g., 'Bug fix'), activeForm: imperative (e.g., 'Fix the bug') | |
| D. Both should use present continuous (e.g., 'Fixing the bug') | |

**Explanation**: WHY THIS MATTERS: This distinction serves different UI purposes. The 'subject' is the permanent task label - imperative verbs ('Add', 'Fix', 'Refactor') clearly state what needs doing. The 'activeForm' appears in the spinner while the task runs - present continuous ('Adding', 'Fixing') shows ongoing work. Getting this right makes the task list readable and the spinner informative.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Task Management<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/interactive-mode">Claude Code Task Management</a><br>
<strong>Section</strong>: TaskCreate<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Subject field uses imperative form ('Implement X', 'Add Y'), while activeForm uses present continuous ('Implementing X') for the spinner display."</blockquote>

</details>

---

### Q19. How do you share a task list across multiple Claude Code sessions?

| Option | |
| ------ | --- |
| A. Export tasks to a JSON file and import in each session | |
| **B. Set CLAUDE_CODE_TASK_LIST_ID environment variable before launching** | ✓ |
| C. Use the /share command within Claude Code | |
| D. Tasks are automatically shared across all sessions | |

**Explanation**: WHY THIS MATTERS: Cross-session task sharing enables team workflows and persistent project tracking. By setting CLAUDE_CODE_TASK_LIST_ID=my-project before running claude, all sessions share the same task list. This is powerful for long-running projects where you work across multiple terminal windows or days. Tasks persist even when context is compacted.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Interactive Mode<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/interactive-mode">Claude Code Interactive Mode</a><br>
<strong>Section</strong>: Cross-Session Tasks<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Share task lists across sessions with CLAUDE_CODE_TASK_LIST_ID=my-project claude."</blockquote>

</details>

---

### Q20. When should you NOT use the Task system in Claude Code?

| Option | |
| ------ | --- |
| A. For multi-step implementation projects | |
| **B. For single trivial fixes like typos or one-line changes** | ✓ |
| C. When tracking dependencies between tasks | |
| D. During plan mode workflows | |

**Explanation**: WHY THIS MATTERS: Tasks add overhead - creation, status updates, visibility in the UI. For a typo fix, this overhead exceeds the benefit. Use tasks when work benefits from tracking: multi-step projects, dependency chains, cross-session continuity. Skip tasks for quick fixes that complete in under 3 steps. The tool exists to organize complexity, not to bureaucratize simplicity.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Task Management<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/interactive-mode">Claude Code Task Management</a><br>
<strong>Section</strong>: When to Use Tasks<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Do not use tasks for single trivial fixes, pure research/exploration, or tasks completable in fewer than 3 steps."</blockquote>

</details>

---

### Q21. What happens when a skill and a slash command share the same name?

| Option | |
| ------ | --- |
| A. An error is thrown and neither runs | |
| B. The slash command takes precedence | |
| **C. The skill takes precedence** | ✓ |
| D. The user is prompted to choose | |

**Explanation**: WHY THIS MATTERS: This precedence rule lets you override built-in behavior with custom skills. If you create a /commit skill, it runs instead of any built-in commit command. This design choice enables progressive customization - start with defaults, replace them as your workflow matures. It's the extensibility pattern that makes Claude Code adaptable to any team's conventions.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/skills">Claude Code Skills</a><br>
<strong>Section</strong>: Skills vs Commands<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"If a skill and a command share the same name, the skill takes precedence."</blockquote>

</details>

---

### Q22. Where are project-specific skills stored so teammates get them when cloning?

| Option | |
| ------ | --- |
| A. ~/.claude/skills/ (global home directory) | |
| **B. .claude/skills/ (project root, version-controlled)** | ✓ |
| C. ~/.config/claude/skills/ (XDG config) | |
| D. package.json skills section | |

**Explanation**: WHY THIS MATTERS: Project-root storage means skills travel with your code. When teammates clone, they get your custom /deploy, /test, and /review skills automatically. No manual setup, no drift between team members. This is 'team-shared commands via Git' - encode your workflow once, distribute it through your normal version control process.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/skills">Claude Code Skills</a><br>
<strong>Section</strong>: Skill Locations<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Project-specific skills in .claude/skills/ are version-controlled with your code, enabling team-shared commands via Git."</blockquote>

</details>

---

### Q23. What is the difference between global skills (~/.claude/skills/) and project skills (.claude/skills/)?

| Option | |
| ------ | --- |
| A. Global skills run faster | |
| **B. Global skills apply to all projects, project skills only to the current repository** | ✓ |
| C. Global skills have more permissions | |
| D. There is no functional difference | |

**Explanation**: WHY THIS MATTERS: This scoping matches how developers think about tooling. Personal preferences (your /fmt skill for formatting) go global. Project conventions (your team's /deploy skill) go in the project. Global skills let you carry your workflow everywhere; project skills ensure everyone on the team follows the same procedures. Use both layers intentionally.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/skills">Claude Code Skills</a><br>
<strong>Section</strong>: Skill Scopes<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Global skills in ~/.claude/skills/ apply to all projects. Project skills in .claude/skills/ are scoped to the repository."</blockquote>

</details>

---

### Q24. How are slash commands and skills related in recent Claude Code versions?

| Option | |
| ------ | --- |
| A. They are completely separate systems | |
| B. Slash commands call skills internally | |
| **C. Skills and commands were merged - both create slash commands** | ✓ |
| D. Skills replaced slash commands entirely | |

**Explanation**: WHY THIS MATTERS: This merge simplified the mental model. Previously, you had to know whether something was a 'command' or a 'skill.' Now, everything is a slash command - some are built-in, some come from skills. You invoke them the same way (/name), they appear in the same autocomplete list, and skills can override built-ins. One concept instead of two.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/skills">Claude Code Skills</a><br>
<strong>Section</strong>: Skills Overview<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Skills create slash commands that can be invoked with /skill-name. Built-in commands and skill-defined commands share the same invocation pattern."</blockquote>

</details>

---

### Q25. Why would you use a subagent for codebase research instead of having Claude read files directly?

| Option | |
| ------ | --- |
| A. Subagents are faster at reading files | |
| **B. Subagents run in separate context windows and report back summaries, keeping your main conversation clean** | ✓ |
| C. Subagents have special file permissions | |
| D. Direct file reading is not supported | |

**Explanation**: WHY THIS MATTERS: When Claude researches a codebase, it reads many files that consume your context window. Subagents explore in their own context and report back findings as summaries. This preserves your main conversation's context for implementation while still getting comprehensive research. It's like having a research assistant who summarizes instead of reading aloud - you get the insights without the noise.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Subagent patterns<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Use subagents to investigate in a separate context, keeping your main conversation clean for implementation. They explore and report back findings."</blockquote>

</details>

---

### Q26. What workflow pattern does the Claude Code team recommend for building large features?

| Option | |
| ------ | --- |
| A. Start coding immediately and iterate based on errors | |
| B. Write comprehensive documentation before any code | |
| **C. Start with a minimal spec, have Claude interview you for requirements, then execute in a new session** | ✓ |
| D. Use parallel Claude instances to write all components simultaneously | |

**Explanation**: WHY THIS MATTERS: This spec-based workflow uses AskUserQuestionTool to gather requirements iteratively. Claude interviews you about edge cases, constraints, and preferences you might not have considered. Then a fresh session executes the refined spec with clean context. This prevents the common pattern of accumulated context pollution during lengthy requirement discussions.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Thariq (Claude Code team) on Twitter<br>
<strong>URL</strong>: <a href="https://x.com/trq212/status/2005315275026260309">Thariq (Claude Code team) on Twitter</a><br>
<strong>Section</strong>: Thread<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Start with a minimal spec, ask Claude to interview you using AskUserQuestionTool, then make a new session to execute the spec."</blockquote>

</details>

---

### Q27. Why is the 'Writer/Reviewer' pattern with two Claude sessions effective for code quality?

| Option | |
| ------ | --- |
| A. Two sessions can process code twice as fast | |
| **B. A fresh context avoids bias toward code the reviewing Claude didn't write** | ✓ |
| C. Two Claude instances share the same memory and can collaborate | |
| D. The pattern is required for all code reviews in Claude Code | |

**Explanation**: WHY THIS MATTERS: When Claude reviews code it just wrote, it's biased toward defending its own decisions. A fresh session with no memory of writing the code evaluates it objectively - like having a colleague review instead of self-review. This catches issues the writer-Claude rationalized away. Use separate worktrees or sessions for writing and reviewing.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Code Review<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"A fresh context improves code review since Claude won't be biased toward code it just wrote."</blockquote>

</details>

---

### Q28. What is the relationship between the 'Task' tool and 'TaskCreate' in Claude Code?

| Option | |
| ------ | --- |
| A. They are the same tool with different names | |
| **B. Task spawns subagents; TaskCreate manages work item tracking - different systems** | ✓ |
| C. TaskCreate is a deprecated version of Task | |
| D. Task is for background jobs; TaskCreate is for foreground tasks | |

**Explanation**: WHY THIS MATTERS: This naming collision causes common confusion. The Task tool spawns subagents with isolated context for parallel work. The Task* system (TaskCreate, TaskUpdate, TaskList, TaskGet) manages a visible work item list for tracking progress. They serve completely different purposes - one is for delegation, the other is for organization. Don't confuse launching a subagent with creating a todo item.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: GitHub Issue #22695<br>
<strong>URL</strong>: <a href="https://github.com/anthropics/claude-code/issues/22695">GitHub Issue #22695</a><br>
<strong>Section</strong>: Issue description<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Naming collision: Task tool vs Task* system. Task spawns subagents, while TaskCreate/TaskUpdate manage work item tracking."</blockquote>

</details>

---

### Q29. When you spawn a subagent via the Task tool, what happens to your permission allowlist?

| Option | |
| ------ | --- |
| A. The subagent inherits all permissions from the parent session | |
| **B. The subagent has NO inherited permissions - it operates with fresh permission state** | ✓ |
| C. Only Bash permissions are inherited | |
| D. Permissions are inherited but with reduced scope | |

**Explanation**: WHY THIS MATTERS: This is a common source of unexpected permission prompts. When you've pre-approved certain tools in your main session, subagents don't inherit those approvals - they start fresh. This is intentional for security (subagents shouldn't automatically get elevated permissions), but surprising when your pre-approved commands suddenly prompt again inside a subagent.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: GitHub Issue #22665<br>
<strong>URL</strong>: <a href="https://github.com/anthropics/claude-code/issues/22665">GitHub Issue #22665</a><br>
<strong>Section</strong>: Issue description<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Subagent (Task tool) does not inherit permission allowlist from settings.json. Subagents operate with fresh permission state."</blockquote>

</details>

---


## Claude Code Hooks Lifecycle

*Domain: Hooks & Automation | Weight: 15%*

### Q1. What is the primary purpose of Claude Code hooks?

| Option | |
| ------ | --- |
| A. To replace Claude's built-in tools with custom implementations | |
| **B. To execute shell commands at specific lifecycle events for validation, automation, and control** | ✓ |
| C. To modify Claude's underlying language model behavior | |
| D. To disable Claude Code's security features | |

**Explanation**: WHY THIS MATTERS: Hooks are Claude Code's extension mechanism for power users. Unlike prompting (which guides Claude's decisions), hooks provide deterministic control - they execute YOUR code at specific lifecycle points. This enables validation that AI can't bypass, automated logging that survives context resets, and safety guardrails enforced by your infrastructure. Think of hooks as the 'hard rules' layer beneath Claude's 'soft reasoning' layer.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Hook lifecycle<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Hooks fire at specific points during a Claude Code session."</blockquote>

</details>

---

### Q2. When does the UserPromptSubmit hook fire?

| Option | |
| ------ | --- |
| A. After Claude processes the prompt | |
| **B. When you submit a prompt, BEFORE Claude processes it** | ✓ |
| C. When Claude finishes responding | |
| D. When the session ends | |

**Explanation**: WHY THIS MATTERS: This hook intercepts user input BEFORE Claude sees it. This timing is critical - you can validate prompts (block certain keywords), inject context (add today's date automatically), or log everything for compliance. The 'before processing' timing means you're modifying what Claude receives, not reacting to what it does. It's your first line of defense and customization.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: UserPromptSubmit<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Runs when the user submits a prompt, before Claude processes it. This allows you to add additional context based on the prompt/conversation, validate prompts, or block certain types of prompts."</blockquote>

</details>

---

### Q3. Which hooks CAN block execution (prevent an action from proceeding)?

| Option | |
| ------ | --- |
| A. Only PreToolUse and PostToolUse | |
| **B. UserPromptSubmit, PreToolUse, PermissionRequest, PostToolUse, PostToolUseFailure, SubagentStop, and Stop** | ✓ |
| C. All hook types can block | |
| D. Only Stop and SessionEnd | |

**Explanation**: WHY THIS MATTERS: Understanding which hooks CAN block is fundamental to hook architecture. 'Hard' blocks prevent actions entirely (PreToolUse can stop rm -rf before it runs). 'Soft' blocks (PostToolUse) can only alert Claude after the fact - the damage is done. Know the difference: put safety checks in PreToolUse, put logging in PostToolUse. The hooks that CAN'T block (SessionStart, SessionEnd) are for observation only.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Exit Code 2 Behavior<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Exit code 2: Blocking error. Only stderr is used as the error message and fed back to Claude. PreToolUse: Blocks the tool call, shows stderr to Claude. UserPromptSubmit: Blocks prompt processing, erases prompt. Stop: Blocks stoppage, shows stderr to Claude."</blockquote>

</details>

---

### Q4. How do hooks receive their input data?

| Option | |
| ------ | --- |
| A. Via environment variables like $TOOL_NAME and $COMMAND | |
| B. Via command-line arguments | |
| **C. Via stdin as a JSON object** | ✓ |
| D. Via a configuration file | |

**Explanation**: WHY THIS MATTERS: stdin JSON is the standard Unix pattern for passing structured data to processes. This design means hooks can be written in any language (Python, Node, Bash with jq), and they receive rich context (session ID for logging, transcript path for analysis, cwd for relative operations). The JSON structure is stable across Claude Code versions, making hooks future-proof.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Hook Input<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Hooks receive JSON data via stdin containing session information and event-specific data: { session_id: string, transcript_path: string, cwd: string, permission_mode: string, hook_event_name: string, ... }"</blockquote>

</details>

---

### Q5. What is the CORRECT way to reference a hook script in settings.json?

| Option | |
| ------ | --- |
| A. "command": "uv run $HOME/.claude/hooks/script.py" | |
| B. "command": "python3 $HOME/.claude/hooks/script.py" | |
| **C. "command": "$HOME/.claude/hooks/script.py"** | ✓ |
| D. "command": "./hooks/script.py" | |

**Explanation**: WHY THIS MATTERS: Direct paths with shebangs ensure hooks work regardless of environment (no PATH issues, no virtual environment confusion). CLAUDE_PROJECT_DIR lets you ship hooks with your project that work when teammates clone the repo. The chmod +x requirement catches permission errors at development time, not during critical operations. These patterns come from hard-won debugging sessions.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Project-Specific Hook Scripts<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"You can use the environment variable CLAUDE_PROJECT_DIR (only available when Claude Code spawns the hook command) to reference scripts stored in your project, ensuring they work regardless of Claude's current directory."</blockquote>

</details>

---

### Q6. When does PostToolUse hook fire?

| Option | |
| ------ | --- |
| A. Only when a tool throws an unhandled exception | |
| **B. After a tool completes successfully ONLY (NOT on errors)** | ✓ |
| C. Before a tool executes, to validate parameters | |
| D. Immediately after the user grants permission | |

**Explanation**: WHY THIS MATTERS: The split between PostToolUse (success) and PostToolUseFailure (failure) lets you handle outcomes differently. Log successful file edits to an audit trail in PostToolUse; alert on failed commands in PostToolUseFailure. If these were merged, you'd need conditional logic in every hook. The separation reflects that success and failure often require completely different handling.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: PostToolUse<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"PostToolUse: Runs immediately after a tool completes successfully. PostToolUseFailure: After tool fails."</blockquote>

</details>

---

### Q7. For PostToolUse hooks, what is required for Claude to see your message?

| Option | |
| ------ | --- |
| A. Output {"reason": "your message"} | |
| B. Output {"additionalContext": "your message"} | |
| **C. Output {"decision": "block", "reason": "your message"}** | ✓ |
| D. Write to stdout with plain text | |

**Explanation**: WHY THIS MATTERS: This is a common source of confusion. 'decision: block' in PostToolUse doesn't undo the tool call - the file is already edited. What it does is make Claude NOTICE your message (the 'reason' field). Without 'block', your output is silently ignored. Use 'additionalContext' for info Claude should consider but doesn't require acknowledgment. This visibility pattern evolved from hooks whose warnings were lost.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: PostToolUse Decision Control<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"'block' automatically prompts Claude with reason. undefined does nothing. reason is ignored. hookSpecificOutput.additionalContext adds context for Claude to consider."</blockquote>

</details>

---

### Q8. What are the default timeout values for different hook types?

| Option | |
| ------ | --- |
| A. 60 seconds for all hook types | |
| **B. Command hooks: 600 seconds (10 min), Prompt hooks: 30 seconds, Agent hooks: 60 seconds** | ✓ |
| C. 30 seconds for all hook types | |
| D. No timeout - hooks run until completion | |

**Explanation**: WHY THIS MATTERS: Different hook types have different timeout defaults based on their expected complexity. Command hooks get 10 minutes for potentially complex shell operations. Prompt hooks (single LLM call) get 30 seconds. Agent hooks (multi-turn subagent) get 60 seconds. These are configurable per-command. Understanding these defaults helps you design hooks that won't unexpectedly timeout.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Hook Execution Details<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Default timeouts: Command hooks 600 seconds (10 minutes), Prompt hooks 30 seconds, Agent hooks 60 seconds. Configurable per command."</blockquote>

</details>

---

### Q9. What does exit code 2 mean in a hook script?

| Option | |
| ------ | --- |
| A. Success - allow the action | |
| B. Non-blocking error | |
| **C. Hard block - cannot be bypassed** | ✓ |
| D. Soft block - user can override | |

**Explanation**: WHY THIS MATTERS: Exit codes are your hook's primary communication channel. Exit 0 = 'proceed, here's optional JSON data.' Exit 2 = 'STOP, something is wrong, here's why (in stderr).' Other codes = 'there was an issue but don't stop everything.' This convention lets hooks enforce hard constraints (exit 2 for dangerous operations) while gracefully handling recoverable errors (exit 1 for warnings).

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Simple: Exit Code<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Exit code 0: Success. Exit code 2: Blocking error. Only stderr is used as the error message and fed back to Claude. JSON in stdout is NOT processed for exit code 2. Other exit codes: Non-blocking error."</blockquote>

</details>

---

### Q10. In Stop hooks, what does {"continue": false} actually do?

| Option | |
| ------ | --- |
| A. Allows Claude to stop normally | |
| B. Prevents Claude from stopping (forces continuation) | |
| **C. Halts Claude entirely (emergency stop)** | ✓ |
| D. Has no effect | |

**Explanation**: WHY THIS MATTERS: The Stop hook controls session termination. 'continue: false' is an emergency brake - use it when you detect something critically wrong that needs human attention before ANY more AI actions. 'decision: block' with a reason keeps Claude working - useful for 'you're not done yet, the tests still fail.' Empty JSON {} allows normal completion. This granularity lets you implement sophisticated session management.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Stop/SubagentStop Decision Control<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"If continue is false, Claude stops processing after the hooks run. 'block' prevents Claude from stopping. You must populate reason for Claude to know how to proceed. undefined allows Claude to stop."</blockquote>

</details>

---

### Q11. What is headless mode in Claude Code and when would you use it?

| Option | |
| ------ | --- |
| A. Running Claude without a display for accessibility | |
| **B. Non-interactive mode for CI/CD pipelines and automation scripts** | ✓ |
| C. A low-resource mode for slow computers | |
| D. Running multiple Claude instances simultaneously | |

**Explanation**: WHY THIS MATTERS: Headless mode transforms Claude Code from an interactive assistant into an automation tool. In CI/CD, you can have Claude review PRs, generate documentation, or run code analysis - all without human interaction. This enables 'Claude as a service' patterns where automated workflows invoke Claude for specific tasks. It's the bridge between interactive coding and automated pipelines.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code CLI Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/cli-reference">Claude Code CLI Reference</a><br>
<strong>Section</strong>: Headless Mode<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Headless mode enables non-interactive execution for CI/CD pipelines, automation scripts, and programmatic access to Claude Code capabilities."</blockquote>

</details>

---

### Q12. How do you run Claude Code in headless mode with a prompt?

| Option | |
| ------ | --- |
| A. claude --headless "your prompt" | |
| **B. claude -p "your prompt"** | ✓ |
| C. echo "your prompt" | claude --no-interactive | |
| D. claude run "your prompt" | |

**Explanation**: WHY THIS MATTERS: The -p flag is the gateway to automation. Combined with --output-format json, you get structured results for parsing. Combined with --allowedTools, you control exactly what Claude can do. This simple flag unlocks use cases from automated code review to scheduled documentation updates to integration testing. Master -p and you unlock Claude as a programmable service.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code CLI Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/cli-reference">Claude Code CLI Reference</a><br>
<strong>Section</strong>: Command Line Options<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Use -p or --prompt to run Claude Code in headless mode with a specified prompt, without starting the interactive interface."</blockquote>

</details>

---

### Q13. What output format option is most useful for parsing Claude Code results in scripts?

| Option | |
| ------ | --- |
| A. --output-format text (human readable) | |
| **B. --output-format json (structured, machine parseable)** | ✓ |
| C. --output-format markdown (documentation ready) | |
| D. --output-format xml (legacy compatibility) | |

**Explanation**: WHY THIS MATTERS: JSON output turns Claude's responses into data you can programmatically process. Extract specific fields, check for errors, feed results into other tools. In a CI pipeline, you might parse JSON to determine if Claude found issues, what files were modified, or whether tests passed. This is the interface between Claude's intelligence and your automation infrastructure.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code CLI Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/cli-reference">Claude Code CLI Reference</a><br>
<strong>Section</strong>: Output Formats<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Use --output-format json for structured output that can be parsed by scripts and automation tools."</blockquote>

</details>

---

### Q14. What is the difference between command hooks and prompt hooks in Claude Code?

| Option | |
| ------ | --- |
| A. Command hooks are faster | |
| **B. Command hooks run shell scripts; prompt hooks use an LLM to evaluate decisions** | ✓ |
| C. Prompt hooks have higher priority | |
| D. Command hooks require admin permissions | |

**Explanation**: WHY THIS MATTERS: This is a fundamental architectural choice. Command hooks (type: 'command') execute deterministic shell scripts - fast, predictable, no API cost. Prompt hooks (type: 'prompt') send context to an LLM for intelligent evaluation - flexible but slower and costs tokens. Use command hooks for rule-based checks, prompt hooks for nuanced decisions that need reasoning.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Hook Types<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Command hooks run shell scripts. Prompt hooks use an LLM to evaluate decisions with single-turn reasoning."</blockquote>

</details>

---

### Q15. What happens when you set async: true on a command hook?

| Option | |
| ------ | --- |
| A. The hook runs faster | |
| **B. The hook runs in background - cannot block or return decisions** | ✓ |
| C. The hook gets more CPU resources | |
| D. The hook retries on failure | |

**Explanation**: WHY THIS MATTERS: Async hooks fire-and-forget - they can't block execution because the action has already proceeded by the time they run. Use async for logging, notifications, or background processing where you don't need to influence the outcome. The output is delivered on the next conversation turn. This is perfect for audit trails that shouldn't slow down the user.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Async Hooks<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"async: true runs hooks in background without blocking. Cannot return decisions. Output delivered on next conversation turn."</blockquote>

</details>

---

### Q16. How do you restrict Claude Code to read-only operations in a CI pipeline?

| Option | |
| ------ | --- |
| A. Set CLAUDE_READ_ONLY=true environment variable | |
| **B. Use --allowedTools Read,Grep,Glob to whitelist specific tools** | ✓ |
| C. Run with --safe-mode flag | |
| D. CI automatically restricts write access | |

**Explanation**: WHY THIS MATTERS: Controlling tool access is essential for safe automation. --allowedTools lets you whitelist exactly what Claude can do, following principle of least privilege. For code review pipelines, 'Read,Grep,Glob' enables analysis without modification risk. For documentation generation, add 'Write'. This granular control makes Claude safe for automated environments.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code CLI Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/cli-reference">Claude Code CLI Reference</a><br>
<strong>Section</strong>: Headless Mode Options<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Use --allowedTools to explicitly list only the tools needed for the task, enabling read-only analysis without modification risk."</blockquote>

</details>

---

### Q17. How do you stop Claude mid-action without exiting the application?

| Option | |
| ------ | --- |
| A. Press Ctrl+C | |
| **B. Press Escape** | ✓ |
| C. Press Ctrl+Z | |
| D. Type 'stop' and press Enter | |

**Explanation**: WHY THIS MATTERS: This is a common gotcha. Ctrl+C exits Claude Code entirely, losing your session. Escape stops the current action while keeping the session alive - you can then redirect, clarify, or start something else. This is essential for 'vibe coding' flow when Claude heads in the wrong direction. Stop early, redirect, continue - don't lose your whole session.

<details open class="citation">
<summary>Citation [Tier 2 - Community] (95% confidence)</summary>

<strong>Source</strong>: How I Use Claude Code<br>
<strong>URL</strong>: <a href="https://www.builder.io/blog/claude-code">How I Use Claude Code</a><br>
<strong>Section</strong>: Keyboard Shortcuts<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Stopping Claude isn't Control+C (that just exits entirely). Use Escape to actually stop Claude mid-action."</blockquote>

</details>

---


## Claude Code Integration Tools

*Domain: Integration & Workflows | Weight: 15%*

### Q1. What is MCP (Model Context Protocol) in Claude Code?

| Option | |
| ------ | --- |
| A. A compression algorithm for context windows | |
| **B. A protocol for connecting external tools and data sources to Claude** | ✓ |
| C. A security mechanism for permission management | |
| D. A caching layer for faster responses | |

**Explanation**: WHY THIS MATTERS: MCP extends Claude Code beyond its built-in tools. Database connectors, API integrations, custom search engines - MCP servers provide these capabilities through a standardized protocol. This is how you make Claude Code domain-specific: connect it to your internal tools, your company's APIs, your specialized data sources. It transforms Claude from a general assistant into a specialized team member.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code MCP Integration<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/mcp">Claude Code MCP Integration</a><br>
<strong>Section</strong>: Overview<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Model Context Protocol (MCP) is a protocol for connecting external tools and data sources to Claude, extending its capabilities beyond built-in tools."</blockquote>

</details>

---

### Q2. What is Tool Search in Claude Code and why is it valuable?

| Option | |
| ------ | --- |
| A. A way to find files by name | |
| **B. A feature that reduces token usage by lazy-loading tool descriptions only when needed** | ✓ |
| C. A search engine for finding community tools | |
| D. A debugging tool for inspecting tool calls | |

**Explanation**: WHY THIS MATTERS: Every tool description consumes context tokens. With many MCP servers, you could spend 40%+ of your context just describing available tools. Tool Search solves this by loading tool descriptions on-demand - Claude sees a tool index initially, then fetches full descriptions only for tools it might use. This optimization enables large tool libraries without context bloat.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code MCP Integration<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/mcp">Claude Code MCP Integration</a><br>
<strong>Section</strong>: Tool Search<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Tool Search provides significant token reduction by lazy-loading tool descriptions only when Claude determines they may be relevant to the current task."</blockquote>

</details>

---

### Q3. What security consideration is important when configuring MCP servers?

| Option | |
| ------ | --- |
| A. MCP servers run in a sandbox and cannot access the network | |
| **B. MCP servers have full system access - only use trusted servers** | ✓ |
| C. MCP servers are automatically audited by Anthropic | |
| D. MCP servers can only read data, not write | |

**Explanation**: WHY THIS MATTERS: MCP servers execute code on your machine with your permissions. A malicious or buggy server could read your files, make network requests, or modify data. Only install MCP servers from trusted sources, audit their code if possible, and understand what permissions they need. The power of MCP comes with responsibility for vetting what you connect.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security</a><br>
<strong>Section</strong>: MCP Security<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"MCP servers run with your user permissions. Only install MCP servers from trusted sources and review their capabilities before enabling."</blockquote>

</details>

---

### Q4. What are git worktrees and why are they useful with Claude Code?

| Option | |
| ------ | --- |
| A. A visualization of git history | |
| **B. Multiple working directories from one repo, enabling parallel Claude sessions on different branches** | ✓ |
| C. A backup mechanism for git repositories | |
| D. A way to merge branches faster | |

**Explanation**: WHY THIS MATTERS: Worktrees let you have multiple checked-out copies of your repo, each on a different branch. Run one Claude session exploring a refactor in worktree A while another implements a feature in worktree B. No context switching, no stashing, no branch conflicts. This is the power-user pattern for parallel exploration - multiple Claudes, multiple branches, all progressing simultaneously.

<details open class="citation">
<summary>Citation [Tier 2 - Community] (90% confidence)</summary>

<strong>Source</strong>: Claude Code Advanced Workflows<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code Advanced Workflows</a><br>
<strong>Section</strong>: Parallel Development<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Git worktrees enable parallel Claude Code sessions by providing separate working directories for different branches of the same repository."</blockquote>

</details>

---

### Q5. How does CLAUDE.md work across git worktrees?

| Option | |
| ------ | --- |
| A. Each worktree needs its own CLAUDE.md | |
| **B. CLAUDE.md is shared because it's in the repo - changes in one worktree appear in others after commit** | ✓ |
| C. CLAUDE.md is ignored in worktrees | |
| D. Worktrees use the global ~/.claude/CLAUDE.md only | |

**Explanation**: WHY THIS MATTERS: CLAUDE.md is version-controlled, so it travels with your code. When you improve CLAUDE.md in one worktree and commit, other worktrees get the update when they pull. This creates a shared 'team memory' that evolves with your project. Pro tip: designate one branch as the CLAUDE.md improvement branch and periodically merge those insights to all feature branches.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Using CLAUDE.md<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"CLAUDE.md is version-controlled with your code, so improvements made in one branch propagate to others through normal git workflows."</blockquote>

</details>

---

### Q6. What is the recommended workflow for parallel Claude sessions using worktrees?

| Option | |
| ------ | --- |
| A. Run all sessions in the same directory with different terminals | |
| **B. Create worktrees for independent tasks, run separate Claude sessions in each** | ✓ |
| C. Use a single Claude session and rapidly switch branches | |
| D. Parallel sessions are not recommended | |

**Explanation**: WHY THIS MATTERS: This workflow maximizes parallelism while maintaining isolation. Each worktree has its own file state, so Claude sessions don't interfere with each other. You can have Claude exploring architecture options in one worktree while implementing a known feature in another. The key is 'independent tasks' - parallel work that doesn't need to coordinate minute-by-minute.

<details open class="citation">
<summary>Citation [Tier 2 - Community] (90% confidence)</summary>

<strong>Source</strong>: Claude Code Advanced Workflows<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code Advanced Workflows</a><br>
<strong>Section</strong>: Parallel Development<br>
<strong>Access Date</strong>: 2026-01-30<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"For parallel development, create worktrees for independent tasks and run separate Claude Code sessions in each, allowing simultaneous progress without interference."</blockquote>

</details>

---

### Q7. What are the three MCP server configuration scopes in Claude Code, and what is their precedence order?

| Option | |
| ------ | --- |
| A. Global > User > Project (global settings override all) | |
| **B. Local > Project > User (local settings have highest priority)** | ✓ |
| C. User > Project > Local (user settings always win) | |
| D. Project > Local > User (team settings override personal) | |

**Explanation**: WHY THIS MATTERS: Understanding scope precedence prevents the #1 MCP configuration error - 'server not found'. Local scope (personal, current project) overrides Project scope (team-shared .mcp.json), which overrides User scope (cross-project personal). This lets you override team configurations when needed while maintaining shared defaults.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code MCP Integration<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/mcp">Claude Code MCP Integration</a><br>
<strong>Section</strong>: Configuration Scopes<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"MCP configuration scopes: Local > Project > User. Local settings have highest priority and override project and user settings."</blockquote>

</details>

---

### Q8. What specific security risk does Anthropic warn about when using MCP servers that fetch untrusted content?

| Option | |
| ------ | --- |
| A. Slower response times due to network latency | |
| B. Higher API costs from additional token usage | |
| **C. Exposure to prompt injection attacks** | ✓ |
| D. Memory leaks from poorly written servers | |

**Explanation**: WHY THIS MATTERS: MCP servers that fetch content from external sources (web scrapers, email readers, issue trackers) can inadvertently inject malicious prompts into Claude's context. An attacker could embed hidden instructions in a GitHub issue or email that manipulates Claude's behavior. This is why Anthropic specifically warns: 'Be especially careful when using MCP servers that could fetch untrusted content.'

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code MCP Integration<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/mcp">Claude Code MCP Integration</a><br>
<strong>Section</strong>: Security Considerations<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Be especially careful when using MCP servers that could fetch untrusted content, as these can expose you to prompt injection risk."</blockquote>

</details>

---

### Q9. When does Claude Code's MCP Tool Search automatically activate?

| Option | |
| ------ | --- |
| A. Always enabled when any MCP server is connected | |
| **B. When MCP tool descriptions would exceed 10% of the context window** | ✓ |
| C. Only when manually enabled with /tool-search command | |
| D. When using more than 5 MCP servers simultaneously | |

**Explanation**: WHY THIS MATTERS: Tool Search runs in 'auto' mode by default - it activates only when your MCP tool definitions would consume more than 10% of context. This prevents context bloat while maintaining access to all tools. With many servers, tool definitions can consume 40%+ of context before you even start. Tool Search reduced Anthropic's internal tool definitions from 134K tokens to on-demand lookups.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code MCP Integration<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/mcp">Claude Code MCP Integration</a><br>
<strong>Section</strong>: Tool Search<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Tool Search activates in auto mode when tool descriptions would exceed 10% of context window. Configurable threshold with auto:N syntax."</blockquote>

</details>

---

### Q10. How should teams share MCP server configurations across all team members?

| Option | |
| ------ | --- |
| A. Email the configuration to each team member | |
| **B. Create a .mcp.json file at the project root and check it into version control** | ✓ |
| C. Each team member must configure MCP servers individually | |
| D. MCP servers cannot be shared between team members | |

**Explanation**: WHY THIS MATTERS: Project-scoped MCP configurations in .mcp.json are automatically picked up by all team members when they clone the repository. This ensures everyone has access to the same tools - database connectors, API integrations, internal services. One central configuration, distributed through normal version control.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code MCP Integration<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/mcp">Claude Code MCP Integration</a><br>
<strong>Section</strong>: Project Configuration<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Project-scoped MCP configurations in .mcp.json are version-controlled and automatically apply to all team members."</blockquote>

</details>

---

### Q11. Why was the Claude Code SDK renamed to Claude Agent SDK?

| Option | |
| ------ | --- |
| A. To indicate it's only for automated agents, not human interaction | |
| **B. Because the agent harness powering Claude Code is useful for many non-coding applications** | ✓ |
| C. To separate coding tools from general AI capabilities | |
| D. Due to trademark concerns | |

**Explanation**: WHY THIS MATTERS: The rename reflects that Claude Code's underlying agent architecture is general-purpose. Teams at Anthropic use it as a general agent, not just for code. The SDK lets you build custom agents for any domain - customer support, research, data analysis - using the same battle-tested infrastructure that powers Claude Code.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Thariq (Claude Code team) on Twitter<br>
<strong>URL</strong>: <a href="https://x.com/trq212/status/1975243734083379662">Thariq (Claude Code team) on Twitter</a><br>
<strong>Section</strong>: Thread<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Claude Code SDK renamed to Claude Agent SDK. Claude Code is All You Need - the team uses it as a general agent, not just for code."</blockquote>

</details>

---

### Q12. What is a Claude Code plugin?

| Option | |
| ------ | --- |
| A. A browser extension for Claude.ai | |
| **B. A collection of related skills, agents, and hooks bundled together** | ✓ |
| C. A paid add-on from Anthropic | |
| D. A security scanning tool | |

**Explanation**: WHY THIS MATTERS: Plugins bundle related capabilities for distribution. A 'deployment' plugin might include a /deploy skill, pre-deployment validation hooks, and specialized agents for infrastructure analysis. The /plugin command lets you add marketplaces and discover community-built extensions, rapidly expanding Claude's capabilities without manual configuration.

<details open class="citation">
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Plugins<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/plugins">Claude Code Plugins</a><br>
<strong>Section</strong>: Overview<br>
<strong>Access Date</strong>: 2026-02-03<br>
<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"Plugins bundle related skills, agents, and hooks together for distribution via the marketplace."</blockquote>

</details>

---


---

*This answer key is auto-generated from the [quiz source files](https://github.com/terrylica/bruntwork-claude-screening/tree/main/quiz-data).*
