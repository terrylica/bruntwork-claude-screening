---
title: Quiz Answer Key & Review
permalink: /review/
toc: true
toc_sticky: true
---

> This page contains all correct answers with explanations and authoritative citations.
> Use this as a learning resource alongside the [assessment quizzes](./).

*Generated: 2026-01-25 12:21*

---

## Statistics

| Metric | Value |
| ------ | ----- |
| Total Questions | 46 |
| Domains | 4 |
| Citation Coverage | 100% |
| Tier 1 (Official) | 96% |
| Tier 2 (Internal) | 4% |
| Tier 3 (Community) | 0% |

---

## Table of Contents

| # | Domain | Questions | Weight | Jump |
| - | ------ | --------- | ------ | ---- |
| 1 | Prompting & Context | 10 | 35% | [Go](#effective-prompting) |
| 2 | Safety & Control | 10 | 30% | [Go](#safety-autonomy) |
| 3 | Advanced Architecture | 16 | 20% | [Go](#agents-deep-dive) |
| 4 | Hooks & Automation | 10 | 20% | [Go](#hooks-lifecycle) |

---

## Effective Claude Code Prompting

*Domain: Prompting & Context | Weight: 35%*

### Q1. What is the most important factor for Claude Code's success rate according to Anthropic?

| Option | |
| ------ | --- |
| A. Specifying which tools to use | |
| **B. Clear, specific instructions about what you want** | ✓ |
| C. Using the latest model version | |
| D. Running in a specific environment | |

**Explanation**: WHY THIS MATTERS: Claude Code v2.1+ autonomously selects tools based on context - you don't need to micromanage. What matters is WHAT you want, not HOW to do it. According to Anthropic: 'Claude Code's success rate improves significantly with more specific instructions, especially on first attempts.' Focus your energy on describing outcomes clearly, not on directing implementation details.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Be specific in your instructions<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Claude Code's success rate improves significantly with more specific instructions, especially on first attempts. Giving clear directions upfront reduces the need for course corrections later."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Use CLAUDE.md for context<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"CLAUDE.md is a special file that Claude automatically pulls into context when starting a conversation. This makes it an ideal place for documenting repository etiquette, developer environment setup, and any unexpected behaviors particular to the project."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude 4.x Prompting Best Practices<br>
<strong>URL</strong>: <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices">Claude 4.x Prompting Best Practices</a><br>
<strong>Section</strong>: Be explicit with your instructions<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Claude 4.x models respond well to clear, explicit instructions. Being specific about your desired output can help enhance results. Customers who desire the 'above and beyond' behavior from previous Claude models might need to more explicitly request these behaviors."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude 4.x Prompting Best Practices<br>
<strong>URL</strong>: <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices">Claude 4.x Prompting Best Practices</a><br>
<strong>Section</strong>: Tool usage patterns<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"If you say 'can you suggest some changes,' it will sometimes provide suggestions rather than implementing them—even if making changes might be what you intended. For Claude to take action, be more explicit: 'Change this function to improve its performance.'"</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude 4.x Prompting Best Practices<br>
<strong>URL</strong>: <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices">Claude 4.x Prompting Best Practices</a><br>
<strong>Section</strong>: Add context to improve performance<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude 4.x models better understand your goals. Claude is smart enough to generalize from the explanation."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude 4.x Prompting Best Practices<br>
<strong>URL</strong>: <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices">Claude 4.x Prompting Best Practices</a><br>
<strong>Section</strong>: Subagent orchestration<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Claude 4.5 models demonstrate significantly improved native subagent orchestration capabilities. These models can recognize when tasks would benefit from delegating work to specialized subagents and do so proactively without requiring explicit instruction."</blockquote>

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

<details>
<summary>Citation [Tier 2 - Axios] (90% confidence)</summary>

<strong>Source</strong>: Anthropic's Claude Code transforms vibe coding<br>
<strong>URL</strong>: <a href="https://www.axios.com/2026/01/07/anthropics-claude-code-vibe-coding">Anthropic's Claude Code transforms vibe coding</a><br>
<strong>Section</strong>: Overview<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"The term vibe coding—describing projects in natural language instead of code—was coined by Andrej Karpathy on February 3, 2025. Claude Code changed this by letting users talk directly to an agent. 'You just tell it to do something, and it works.'"</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Ask Claude to make a plan<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Ask Claude to make a plan before coding. Explicitly tell it not to code until you've confirmed its plan looks good."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Autonomous workflows<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"If you want Claude Code to run something autonomously, you need to give it a way to verify results. The key is completing the write-test cycle: write code, run it, check the output, and repeat."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Using CLAUDE.md<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"CLAUDE.md is an ideal place for documenting repository etiquette (branch naming, merge vs. rebase), developer environment setup (pyenv use, which compilers work), common bash commands, core files and utility functions, code style guidelines, and testing instructions."</blockquote>

</details>

---


## Safety & Autonomy

*Domain: Safety & Control | Weight: 30%*

### Q1. What is Claude Code's default permission behavior?

| Option | |
| ------ | --- |
| A. All operations are allowed automatically | |
| **B. Asks permission for each action, with pre-approval available for known-safe operations** | ✓ |
| C. No operations are allowed without admin approval | |
| D. Permissions depend on your subscription tier | |

**Explanation**: WHY THIS MATTERS: Claude Code's permission system balances safety with usability. By default, you approve each action, maintaining full control. As you build trust, use /permissions to pre-approve safe operations without constant interruption. This isn't about distrust - it's about visibility. Even experienced users appreciate knowing what's happening before irreversible changes occur.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security Reference</a><br>
<strong>Section</strong>: Permission-based architecture<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Claude Code uses strict read-only permissions by default. When additional actions are needed, Claude Code requests explicit permission. You can customize the allowlist to permit additional tools that you know are safe."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security Reference</a><br>
<strong>Section</strong>: Permission-based architecture<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Claude Code can only write to the folder where it was started and its subfolders—it cannot modify files in parent directories without explicit permission. While Claude Code can read files outside the working directory (useful for accessing system libraries), write operations are strictly confined to the project scope."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Git Safety Protocol<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"NEVER run destructive git commands (push --force, reset --hard, checkout ., restore ., clean -f, branch -D) unless the user explicitly requests these actions."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Best Practices<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/best-practices">Claude Code Best Practices</a><br>
<strong>Section</strong>: Git Safety Protocol<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Only create commits when requested by the user. If unclear, ask first. NEVER commit changes unless the user explicitly asks you to."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security Reference</a><br>
<strong>Section</strong>: User responsibility<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Claude Code only has the permissions you grant it. You're responsible for reviewing proposed code and commands for safety before approval."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security Reference</a><br>
<strong>Section</strong>: Security best practices<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Review all suggested changes before approval. Use project-specific permission settings for sensitive repositories. Always maintain good security practices when working with any AI tool."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code: Best practices for agentic coding<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code: Best practices for agentic coding</a><br>
<strong>Section</strong>: Controlling autonomy<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Users can toggle between: Asking permission for each tool use (default), Pre-approving safe tools via /permissions, Using --dangerously-skip-permissions for trusted workflows in isolated environments."</blockquote>

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

<details>
<summary>Citation [Tier 2 - Community] (90% confidence)</summary>

<strong>Source</strong>: Claude Code 2.0 Best Practices<br>
<strong>URL</strong>: <a href="https://skywork.ai/blog/claude-code-2-0-best-practices-ai-coding-workflow-2025/">Claude Code 2.0 Best Practices</a><br>
<strong>Section</strong>: 2025 Updates<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"The most interesting practical tools in 2025 cluster around Level 3-4: supervised autonomy where you provide goals and guardrails, the agent executes independently, and you approve/reject at decision points. This balance preserves safety while delivering substantial productivity gains."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Security Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/security">Claude Code Security Reference</a><br>
<strong>Section</strong>: User responsibility<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Claude Code only has the permissions you grant it. You're responsible for reviewing proposed code and commands for safety before approval."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude 4.x Prompting Best Practices<br>
<strong>URL</strong>: <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices">Claude 4.x Prompting Best Practices</a><br>
<strong>Section</strong>: Overeagerness and file creation<br>
<strong>Access Date</strong>: 2026-01-25<br>
<blockquote>"Claude Opus 4.5 has a tendency to overengineer by creating extra files, adding unnecessary abstractions, or building in flexibility that wasn't requested. If you're seeing this undesired behavior, add explicit prompting to keep solutions minimal: 'Avoid over-engineering. Only make changes that are directly requested.'"</blockquote>

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

**Explanation**: WHY THIS MATTERS: Project-root storage (.claude/agents/) means agents are version-controlled with your code. When teammates clone the repo, they get the same specialized agents. This is intentionally different from skills (which can be global). Project-specific agents encode project-specific knowledge that shouldn't leak to other codebases.

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

**Explanation**: WHY THIS MATTERS: Auto-activation creates seamless experiences. Instead of 'please use the migration agent,' you just say 'migrate the database schema' and Claude recognizes the pattern. This reduces friction and cognitive load - you describe what you want, and the right specialist appears. The magic is in the trigger patterns, which let you define precisely when each agent should activate.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Sub-agents<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/sub-agents">Claude Code Sub-agents</a><br>
<strong>Section</strong>: Pre-defined agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"When Claude detects that a task matches an agent's capabilities, it automatically activates that agent."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building a Multi-Agent Research System<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/research/building-a-multi-agent-research-system">Building a Multi-Agent Research System</a><br>
<strong>Section</strong>: Coordinator Design<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"The coordinator agent needs visibility into all research findings to synthesize a coherent response. Subagents that hide context prevent holistic decision-making."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building a Multi-Agent Research System<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/research/building-a-multi-agent-research-system">Building a Multi-Agent Research System</a><br>
<strong>Section</strong>: Coordinator Design<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"The coordinator agent needs visibility into all research findings to synthesize a coherent response that draws connections across domains."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Agent architectures<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"The simplest architecture is a single agent that handles all tasks. For more complex scenarios, use orchestrator patterns where subagents handle isolated subtasks and report back."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building a Multi-Agent Research System<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/research/building-a-multi-agent-research-system">Building a Multi-Agent Research System</a><br>
<strong>Section</strong>: System Architecture<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"The coordinator agent synthesizes findings from all research agents to produce a coherent final answer."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code Skills</a><br>
<strong>Section</strong>: Skills vs Subagents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Skills run within the main conversation context, while subagents operate in isolated context windows with their own tool access."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code Skills</a><br>
<strong>Section</strong>: When to use skills<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Use skills for context injection, checklists, and templates where you want the information to remain in the main conversation."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Skills<br>
<strong>URL</strong>: <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code Skills</a><br>
<strong>Section</strong>: Context persistence<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Skill content is injected into the main conversation context and remains available throughout the session."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: When (not) to use agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Multi-agent systems can be appropriate when you have truly parallel, independent subtasks. For most applications, start with a single agent."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Principles<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Maintain simplicity in your agentic system. Start with the simplest solution that could work, then add complexity only when needed."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Multi-agent patterns<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Multi-agent systems excel when you have independent, parallelizable subtasks that don't require shared state."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Principles for building effective agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Maintain simplicity in your agentic system. Start with the simplest solution that could work."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Principles for building effective agents<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Design for transparency: make agent actions and reasoning visible and understandable."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Building Effective Agents<br>
<strong>URL</strong>: <a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective Agents</a><br>
<strong>Section</strong>: Agent-Computer Interface (ACI) design<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Just as good UI design is critical for human-computer interaction, ACI design is critical for agent-computer interaction."</blockquote>

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

**Explanation**: WHY THIS MATTERS: Hooks are Claude Code's extension mechanism for power users. Unlike prompting (which guides Claude's decisions), hooks provide deterministic control - they execute YOUR code at specific lifecycle points. This enables validation that AI can't bypass, automated logging that survives context resets, and safety guardrails enforced by your infrastructure. Think of hooks as the 'hard rules' layer beneath Claude's 'soft reasoning' layer.

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

**Explanation**: WHY THIS MATTERS: This hook intercepts user input BEFORE Claude sees it. This timing is critical - you can validate prompts (block certain keywords), inject context (add today's date automatically), or log everything for compliance. The 'before processing' timing means you're modifying what Claude receives, not reacting to what it does. It's your first line of defense and customization.

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: UserPromptSubmit<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Runs when the user submits a prompt, before Claude processes it. This allows you to add additional context based on the prompt/conversation, validate prompts, or block certain types of prompts."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Exit Code 2 Behavior<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Exit code 2: Blocking error. Only stderr is used as the error message and fed back to Claude. PreToolUse: Blocks the tool call, shows stderr to Claude. UserPromptSubmit: Blocks prompt processing, erases prompt. Stop: Blocks stoppage, shows stderr to Claude."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Hook Input<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Hooks receive JSON data via stdin containing session information and event-specific data: { session_id: string, transcript_path: string, cwd: string, permission_mode: string, hook_event_name: string, ... }"</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Project-Specific Hook Scripts<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"You can use the environment variable CLAUDE_PROJECT_DIR (only available when Claude Code spawns the hook command) to reference scripts stored in your project, ensuring they work regardless of Claude's current directory."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: PostToolUse<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"PostToolUse: Runs immediately after a tool completes successfully. PostToolUseFailure: After tool fails."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: PostToolUse Decision Control<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"'block' automatically prompts Claude with reason. undefined does nothing. reason is ignored. hookSpecificOutput.additionalContext adds context for Claude to consider."</blockquote>

</details>

---

### Q8. What is the RECOMMENDED execution time for hooks to ensure responsive UX? (Note: Official timeout is 60 seconds)

| Option | |
| ------ | --- |
| A. Under 1 second | |
| **B. Under 100 milliseconds (best practice)** | ✓ |
| C. Under 5 seconds | |
| D. 60 seconds (official timeout) | |

**Explanation**: WHY THIS MATTERS: The 60-second timeout is a safety net, not a target. Every millisecond your hook runs is a millisecond the user waits with a frozen UI. At 100ms, delays are imperceptible; at 500ms, users notice; at 2 seconds, they think something's broken. Fast hooks maintain the 'vibe coding' flow. If you need heavy processing, consider async patterns: write to a file and have a background process handle it.

<details>
<summary>Citation [Tier 1 - Anthropic] (95% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Hook Execution Details<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Timeout: 60-second execution limit by default, configurable per command. A timeout for an individual command does not affect the other commands."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Simple: Exit Code<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"Exit code 0: Success. Exit code 2: Blocking error. Only stderr is used as the error message and fed back to Claude. JSON in stdout is NOT processed for exit code 2. Other exit codes: Non-blocking error."</blockquote>

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

<details>
<summary>Citation [Tier 1 - Anthropic] (98% confidence)</summary>

<strong>Source</strong>: Claude Code Hooks Reference<br>
<strong>URL</strong>: <a href="https://code.claude.com/docs/en/hooks">Claude Code Hooks Reference</a><br>
<strong>Section</strong>: Stop/SubagentStop Decision Control<br>
<strong>Access Date</strong>: 2026-01-24<br>
<blockquote>"If continue is false, Claude stops processing after the hooks run. 'block' prevents Claude from stopping. You must populate reason for Claude to know how to proceed. undefined allows Claude to stop."</blockquote>

</details>

---


---

*This answer key is auto-generated from the [quiz source files](https://github.com/terrylica/bruntwork-claude-screening/tree/main/quiz-data).*
