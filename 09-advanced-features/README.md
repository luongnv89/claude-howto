<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Advanced Features

Comprehensive guide to Claude Code's advanced capabilities including planning mode, extended thinking, auto mode, background tasks, permission modes, print mode (non-interactive), session management, interactive features, channels, voice dictation, remote control, web sessions, desktop app, task list, prompt suggestions, git worktrees, sandboxing, managed settings, and configuration.

## Table of Contents

1. [Overview](#overview)
2. [Planning Mode](#planning-mode)
3. [Ultraplan (Cloud Plan Drafting)](#ultraplan-cloud-plan-drafting)
4. [Extended Thinking](#extended-thinking)
5. [Auto Mode](#auto-mode)
6. [Background Tasks](#background-tasks)
7. [Monitor Tool (Event-Driven Streams)](#monitor-tool-event-driven-streams)
8. [Scheduled Tasks](#scheduled-tasks)
9. [Permission Modes](#permission-modes)
10. [Headless Mode](#headless-mode)
11. [Session Management](#session-management)
12. [Interactive Features](#interactive-features)
13. [TUI Mode (Fullscreen)](#tui-mode-fullscreen)
14. [Voice Dictation](#voice-dictation)
15. [Channels](#channels)
16. [Chrome Integration](#chrome-integration)
17. [Remote Control](#remote-control)
18. [Web Sessions](#web-sessions)
19. [Desktop App](#desktop-app)
20. [Task List](#task-list)
21. [Prompt Suggestions](#prompt-suggestions)
22. [Git Worktrees](#git-worktrees)
23. [Sandboxing](#sandboxing)
24. [Managed Settings (Enterprise)](#managed-settings-enterprise)
25. [Configuration and Settings](#configuration-and-settings)
26. [Agent Teams](#agent-teams)
27. [Best Practices](#best-practices)
28. [Additional Resources](#additional-resources)

---

## Overview

Advanced features in Claude Code extend the core capabilities with planning, reasoning, automation, and control mechanisms. These features enable sophisticated workflows for complex development tasks, code review, automation, and multi-session management.

**Key advanced features include:**
- **Planning Mode**: Create detailed implementation plans before coding
- **Extended Thinking**: Deep reasoning for complex problems
- **Auto Mode**: Background safety classifier reviews each action before execution (Research Preview)
- **Background Tasks**: Run long operations without blocking the conversation
- **Permission Modes**: Control what Claude can do (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`)
- **Print Mode**: Run Claude Code non-interactively for automation and CI/CD (`claude -p`)
- **Session Management**: Manage multiple work sessions
- **Interactive Features**: Keyboard shortcuts, multi-line input, and command history
- **Voice Dictation**: Push-to-talk voice input with 20-language STT support
- **Channels**: MCP servers push messages into running sessions (Research Preview)
- **Remote Control**: Control Claude Code from Claude.ai or the Claude app
- **Web Sessions**: Run Claude Code in the browser at claude.ai/code
- **Desktop App**: Standalone app for visual diff review and multiple sessions
- **Task List**: Persistent task tracking across context compactions
- **Prompt Suggestions**: Smart command suggestions based on context
- **Git Worktrees**: Isolated worktree branches for parallel work
- **Sandboxing**: OS-level filesystem and network isolation
- **Managed Settings**: Enterprise deployment via plist, Registry, or managed files
- **Configuration**: Customize behavior with JSON configuration files

---

## Planning Mode

Planning mode allows Claude to think through complex tasks before implementing them, creating a detailed plan that you can review and approve.

### What is Planning Mode?

Planning mode is a two-phase approach:
1. **Planning Phase**: Claude analyzes the task and creates a detailed implementation plan
2. **Implementation Phase**: After approval, Claude executes the plan

### When to Use Planning Mode

✅ Use planning mode for:
- Complex multi-file refactoring
- New feature implementations
- Architectural changes
- Database migrations
- Major API redesigns

❌ Don't use planning mode for:
- Simple bug fixes
- Formatting changes
- Single-file edits
- Quick queries

### Activating Planning Mode

**Slash command**:
```bash
/plan Implement user authentication system
```

**CLI flag**:
```bash
claude --permission-mode plan
```

**Set as default**:
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**Keyboard shortcut**:
- `Shift + Tab` - Toggle permission modes (including plan)
- `Alt + M` - Toggle permission modes (Windows/Linux)

### Benefits of Planning Mode

- **Structured implementation approach**: Detailed breakdown of implementation steps
- **Review and approval**: Approve or adjust the plan before execution
- **Risk identification**: Identify potential issues before implementation
- **Clear phases**: Organized implementation phases and milestones

### Example: Feature Implementation

```
User: /plan Add a real-time notification system

Claude: I'll create a plan for implementing real-time notifications.

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

Estimated time: 3-4 hours
Files to modify: 12
New files to create: 8

Ready to proceed? (yes/no/modify plan)

User: yes

Claude: [Begins implementation following the plan]
```

### Plan Modifications

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[Shows modified plan with queue removed]

User: Looks good, proceed

Claude: [Implements modified plan]
```

### Planning Mode Configuration

Planning mode is activated via the CLI flag or slash command:

```bash
# Activate plan mode via CLI
claude --permission-mode plan

# Or use the /plan slash command inside the REPL
/plan Implement user authentication system
```

**Model alias for planning**: Use `opusplan` as a model alias to use Opus for planning and Sonnet for execution:

```bash
claude --model opusplan "design and implement the new API"
```

**Edit plan externally**: Press `Ctrl+G` to open the current plan in your external editor for detailed modifications.

> **v2.1.112 update**: Plan files are now named after the prompt that produced them (instead of random words), making them easier to browse and reuse.

> **v2.1.136 update — plan-mode write blocks are unconditional**: Plan mode now blocks all file writes, including when a matching `Edit(...)` rule exists in `permissions.allow`. Previously a permissive `Edit(...)` rule could let writes through in plan mode; that bypass is closed. If a workflow depended on the older behavior, exit plan mode (`Shift+Tab`) before editing.

---

## Ultraplan (Cloud Plan Drafting)

> **New in v2.1.101**: Ultraplan now auto-creates a Claude Code on the web cloud environment the first time you invoke it — no manual setup, no waiting for a container to warm up before the draft starts.

> **Note**: Ultraplan is a research preview and requires Claude Code v2.1.91 or newer.

`/ultraplan` hands a planning task from your local CLI to a Claude Code on the web session running in plan mode. Claude drafts the plan in the cloud while your terminal stays free for other work, then you review the draft in the browser and choose where to execute — in the same cloud session or teleported back to your terminal.

### When to Use Ultraplan

- You want a richer review surface than the terminal: inline comments, emoji reactions, an outline sidebar, and persistent history.
- You want hands-off drafting while you keep coding locally — the cloud session researches the repo and writes the plan without blocking your CLI.
- The plan needs stakeholder review before execution — a shareable web URL beats pasting terminal scrollback.

### Requirements

- A Claude Code on the web account.
- A GitHub repository (the cloud session clones your repo to draft against real code).
- **Not available** on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry.

### Three Ways to Launch

- **Command**: `/ultraplan <prompt>` — explicit invocation.
- **Keyword**: include the word `ultraplan` anywhere in a normal prompt and Claude routes the request to the cloud.
- **From a local plan**: after Claude finishes a plan locally, pick "No, refine with Ultraplan on Claude Code on the web" in the approval dialog to hand the draft off for deeper research.

### Usage Example

```bash
/ultraplan migrate the auth service from sessions to JWTs
```

Claude acknowledges, spins up the cloud environment (auto-created on first run in v2.1.101+), and returns a session link you can open in your browser.

### Status Indicators

| Status | Meaning |
|---|---|
| `◇ ultraplan` | Claude is researching your codebase and drafting the plan |
| `◇ ultraplan needs your input` | Claude has a clarifying question; open the session link to respond |
| `◆ ultraplan ready` | The plan is ready to review in your browser |

### Execution Options

Once the plan is ready, you have two execution paths. Approve the plan in the browser to execute in the same cloud session — Claude implements the changes remotely and opens a pull request from the web UI. Or choose "Approve plan and teleport back to terminal" to implement locally. The terminal teleport dialog offers three choices:

- **Implement here** — run the approved plan in your current terminal session.
- **Start new session** — open a fresh session in the same working directory and implement there.
- **Cancel** — saves the plan to a file so you can pick it up later.

> **Warning**: Remote Control disconnects when ultraplan starts. Both features share the claude.ai/code interface, so only one can be active at a time.

---

## Extended Thinking

Extended thinking allows Claude to spend more time reasoning about complex problems before providing a solution.

### What is Extended Thinking?

Extended thinking is a deliberate, step-by-step reasoning process where Claude:
- Breaks down complex problems
- Considers multiple approaches
- Evaluates trade-offs
- Reasons through edge cases

### Activating Extended Thinking

**Keyboard shortcut**:
- `Option + T` (macOS) / `Alt + T` (Windows/Linux) - Toggle extended thinking

**Automatic activation**:
- Enabled by default for all models (Opus 4.7, Sonnet 4.6, Haiku 4.5)
- Opus 4.7: Adaptive reasoning with effort levels: `low` (○), `medium` (◐), `high` (●), `xhigh` (Opus 4.7 only, default on Claude Code since Opus 4.7 launch, 2026-04-16), `max`. Opus 4.6 and Sonnet 4.6 also support `low`, `medium`, `high`, `max` (no `xhigh`). Opus 4.7 has a 1M-token native context window (1M context fix landed in v2.1.117 — before that, `/context` miscounted Opus 4.7 against a 200K window and triggered premature autocompact). Since v2.1.129, `/context` shows its visualization in-UI only; the ASCII viz no longer leaks into the conversation context (~1.6k tokens saved per call), so `/context` is safe to invoke freely.
- Pro/Max subscribers on Opus 4.6 / Sonnet 4.6: default effort was raised from `medium` to `high` in v2.1.117.
- Other models: Fixed budget up to 31,999 tokens

**Configuration methods**:
- Toggle: `Alt+T` / `Option+T`, or via `/config`
- View reasoning: `Ctrl+O` (verbose mode)
- Set effort: `/effort` command or `--effort` flag

**Custom budget**:
```bash
export MAX_THINKING_TOKENS=1024
```

**Effort level** (supported on Opus 4.7, Opus 4.6, and Sonnet 4.6):
```bash
export CLAUDE_CODE_EFFORT_LEVEL=xhigh   # low (○), medium (◐), high (●), xhigh (Opus 4.7 only, default), or max
```

**CLI flag**:
```bash
claude --effort high "complex architectural review"
```

**Slash command**:
```
/effort high
```

> **Note:** The keyword "ultrathink" in prompts activates deep reasoning mode. Effort levels `low`, `medium`, `high`, and `max` are supported on Opus 4.7, Opus 4.6, and Sonnet 4.6. `xhigh` (default on Opus 4.7) is Opus 4.7 only.

### Benefits of Extended Thinking

- **Deep reasoning**: Spend more time thinking about complex problems
- **Better architectural decisions**: Make informed choices with comprehensive evaluation
- **Consideration of edge cases**: Think through potential issues and scenarios
- **Thorough analysis**: Structured approach to complex problem-solving

### Example: Architectural Decision

```
User: ultrathink Should we use microservices or a monolith for our e-commerce platform?

Claude: Let me think through this architectural decision carefully...

<extended_thinking>
## Context Analysis
- Team size: 5 developers
- Expected traffic: 10k daily users initially
- Need to scale to 100k+ users
- Limited DevOps resources
- 6-month timeline to MVP

## Approach 1: Microservices
Pros:
+ Independent scaling
+ Technology flexibility
+ Team independence
+ Fault isolation

Cons:
- Operational complexity
- Network overhead
- Distributed tracing needed
- Requires DevOps expertise
- Slower initial development

## Approach 2: Monolith
Pros:
+ Simpler deployment
+ Faster initial development
+ Easier debugging
+ Lower operational overhead
+ Single codebase

Cons:
- Scaling challenges later
- All-or-nothing deployments
- Technology lock-in
- Potential for tight coupling

## Decision Factors
1. Team size (5 devs) → Favors monolith
2. DevOps resources (limited) → Favors monolith
3. Timeline (6 months) → Favors monolith
4. Future scale (100k users) → Achievable with monolith + caching
5. Complexity budget → Limited

## Recommendation
Start with a **modular monolith**:
- Single deployment unit
- Clear module boundaries
- Clean interfaces between modules
- Prepare for future extraction to microservices if needed

This gives you:
✓ Fast initial development
✓ Low operational complexity
✓ Option to extract services later
✓ Clear architecture

Migration path: When you reach 50k+ users or specific modules need independent scaling, extract those modules into microservices.
</extended_thinking>

**Recommendation**: Implement a modular monolith with clean module boundaries.

This approach balances your current constraints (team size, timeline, DevOps resources) with future scalability needs. You can migrate specific modules to microservices later when there's a clear business need.
```

### Extended Thinking Configuration

Extended thinking is controlled via environment variables, keyboard shortcuts, and CLI flags:

```bash
# Set thinking token budget
export MAX_THINKING_TOKENS=16000

# Set effort level (Opus 4.7, Opus 4.6, Sonnet 4.6): low (○), medium (◐), high (●), xhigh (Opus 4.7 only, default), or max
export CLAUDE_CODE_EFFORT_LEVEL=xhigh
```

Toggle during a session with `Alt+T` / `Option+T`, set effort with `/effort`, or configure via `/config`.

---

## Auto Mode

Auto Mode is a Research Preview permission mode (March 2026) that uses a background safety classifier to review each action before execution. It allows Claude to work autonomously while blocking dangerous operations.

### Requirements

- **Plan**: Team, Enterprise, or API (not available on Pro or Max plans)
- **Model**: Claude Sonnet 4.6 or Opus 4.7
- **Provider**: Anthropic API only (not supported on Bedrock, Vertex, or Foundry)
- **Classifier**: Runs on Claude Sonnet 4.6 (adds extra token cost)

### Enabling Auto Mode

```bash
# Unlock auto mode with CLI flag (no longer required for Max subscribers on Opus 4.7 — access it directly)
claude --enable-auto-mode

# Then cycle to it with Shift+Tab in the REPL
```

> **v2.1.112 update**: Auto mode no longer requires the `--enable-auto-mode` flag. Max subscribers access it directly on Opus 4.7.

Or set it as the default permission mode:

```bash
claude --permission-mode auto
```

Setting via config:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### How the Classifier Works

The background classifier evaluates each action using the following decision order:

1. **Allow/deny rules** -- Explicit permission rules are checked first
2. **Read-only/edits auto-approved** -- File reads and edits pass automatically
3. **Classifier** -- The background classifier reviews the action
4. **Fallback** -- Falls back to prompting after 3 consecutive or 20 total blocks

### Default Blocked Actions

Auto mode blocks the following by default:

| Blocked Action | Example |
|----------------|---------|
| Pipe-to-shell installs | `curl \| bash` |
| Sending sensitive data externally | API keys, credentials over network |
| Production deploys | Deploy commands targeting production |
| Mass deletion | `rm -rf` on large directories |
| IAM changes | Permission and role modifications |
| Force push to main | `git push --force origin main` |

### Default Allowed Actions

| Allowed Action | Example |
|----------------|---------|
| Local file operations | Read, write, edit project files |
| Declared dependency installs | `npm install`, `pip install` from manifest |
| Read-only HTTP | `curl` for fetching documentation |
| Pushing to current branch | `git push origin feature-branch` |

### Configuring Auto Mode

**Print default rules as JSON**:
```bash
claude auto-mode defaults
```

**Configure trusted infrastructure** via the `autoMode.environment` managed setting for enterprise deployments. This allows administrators to define trusted CI/CD environments, deployment targets, and infrastructure patterns.

#### Extending defaults with `"$defaults"` (v2.1.118)

Since v2.1.118, `autoMode.allow`, `autoMode.soft_deny`, and `autoMode.environment` accept a `"$defaults"` token that **appends** your rules to the built-in list instead of replacing it. Before v2.1.118, any user-defined array silently clobbered the built-ins.

#### Unconditional blocks with `autoMode.hard_deny` (v2.1.136)

`autoMode.hard_deny` (v2.1.136+) is an array of classifier rules that block a class of actions **regardless of inferred user intent**. Use this for actions that must never run in auto mode — for example, `rm -rf` on root paths or `git push --force` on protected branches. Unlike `soft_deny`, hard-deny rules are not negotiable by the classifier.

```json
{
  "autoMode": {
    "hard_deny": ["Bash(rm -rf /:*)", "Bash(git push --force*)"]
  }
}
```

**Before (replaces built-ins — pre-v2.1.118 behavior):**

```json
{
  "autoMode": {
    "allow": ["Bash(gh pr list:*)"]
  }
}
```

**After (extends built-ins — v2.1.118+):**

```json
{
  "autoMode": {
    "allow": ["$defaults", "Bash(gh pr list:*)"],
    "soft_deny": ["$defaults", "Bash(kubectl delete:*)"],
    "environment": ["$defaults", "trusted-ci.internal"]
  }
}
```

Use `"$defaults"` to keep the shipped baseline rules while layering organization- or project-specific additions on top.

### Fallback Behavior

When the classifier is uncertain, auto mode falls back to prompting the user:
- After **3 consecutive** classifier blocks
- After **20 total** classifier blocks in a session

This ensures the user always retains control when the classifier cannot confidently approve an action.

### Seeding Auto-Mode-Equivalent Permissions (No Team Plan Required)

If you don't have a Team plan or want a simpler approach without the background classifier, you can seed your `~/.claude/settings.json` with a conservative baseline of safe permission rules. The script starts with read-only and local-inspection rules, then lets you opt into edits, tests, local git writes, package installs, and GitHub write actions only when you want them.

**File:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Preview what would be added (no changes written)
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Apply the conservative baseline
python3 09-advanced-features/setup-auto-mode-permissions.py

# Add more capability only when you need it
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

The script adds rules across these categories:

| Category | Examples |
|----------|---------|
| Core read-only tools | `Read(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)`, `WebFetch(*)` |
| Local inspection | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)`, `Bash(cat:*)` |
| Optional edits | `Edit(*)`, `Write(*)`, `NotebookEdit(*)` |
| Optional test/build | `Bash(pytest:*)`, `Bash(python3 -m pytest:*)`, `Bash(cargo test:*)` |
| Optional git writes | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git stash:*)` |
| Git (local write) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Package managers | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| Build & test | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Common shell | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

Dangerous operations (`rm -rf`, `sudo`, force push, `DROP TABLE`, `terraform destroy`, etc.) are intentionally excluded. The script is idempotent — running it twice won't duplicate rules.

---

## Background Tasks

Background tasks allow long-running operations to execute without blocking your conversation.

### What Are Background Tasks?

Background tasks run asynchronously while you continue working:
- Long test suites
- Build processes
- Database migrations
- Deployment scripts
- Analysis tools

**Basic Usage:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### Starting Background Tasks

```
User: Run the full test suite in the background

Claude: Starting tests in background (task-id: bg-1234)
You can continue working while tests run.

[You can continue the conversation]

User: Meanwhile, let's refactor the auth module

Claude: [Works on auth module while tests run in background]

[Later, when tests complete]

Claude: 📢 Background task bg-1234 completed:
✅ 245 tests passed
❌ 3 tests failed
View results: /task show bg-1234
```

### Managing Background Tasks

**List active tasks**:
```
User: /task list

Active background tasks:
1. [bg-1234] Running tests (50% complete, 2min remaining)
2. [bg-1235] Building Docker image (25% complete, 8min remaining)
3. [bg-1236] Deploying to staging (90% complete, 30sec remaining)
```

**Check task status**:
```
User: /task status bg-1234

Task bg-1234: Running tests
Status: In progress
Progress: 120/245 tests (49%)
Started: 2025-11-08 10:30:15
Estimated completion: 2025-11-08 10:34:22
```

**View task output**:
```
User: /task show bg-1234

[Shows live output from the test run]
```

**Cancel task**:
```
User: /task cancel bg-1234

Cancelled background task bg-1234
```

### Example: Parallel Development

```
User: Run the build in the background

Claude: Starting build... (task-id: bg-5001)

User: Also run the linter in background

Claude: Starting linter... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [Implements API endpoint while build and linter run]

[10 minutes later]

Claude: 📢 Build completed successfully (bg-5001)
📢 Linter found 12 issues (bg-5002)

User: Show me the linter issues

Claude: [Shows linter output from bg-5002]
```

### Configuration

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## Monitor Tool (Event-Driven Streams)

> **New in v2.1.98**: The Monitor tool lets Claude watch a background command's stdout and react the moment a matching event appears — replacing polling loops and `sleep` for waiting on long-running processes.

Monitor attaches to any shell command that writes to stdout. Each stdout line from the command becomes a notification that wakes the session. Claude specifies the command; the harness streams output and delivers events as they fire. See the related [Background Tasks](#background-tasks) section for launching the underlying processes.

### Why It Matters

Polling with `/loop` or `sleep` burns a full API round-trip every cycle, whether or not anything changed. Monitor stays silent until an event fires, consuming **zero tokens** while the command is quiet. When an event does occur, Claude reacts immediately — no delayed discovery waiting for the next poll tick. For anything that runs longer than a few minutes, this is both cheaper and faster than poll loops.

### Two Common Patterns

**Stream filters** watch continuous output from a long-running source. The command runs forever; every matching line is an event.

```bash
tail -f /var/log/app.log | grep --line-buffered "ERROR"
```

**Poll-and-emit filters** check a source periodically and only emit when something changes. Use this for APIs, databases, or anything without a native stream.

```bash
last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
while true; do
  gh api "repos/owner/repo/issues/123/comments?since=$last" || true
  last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  sleep 30
done
```

### Concrete Example

"Start my dev server and monitor it for errors." Claude launches the server as a background task, attaches a Monitor filter (`tail -F server.log | grep --line-buffered -E "ERROR|FATAL"`), and the session goes quiet. The moment an error line appears in the log, Claude wakes up, reads the error, and can react — restart the server, fix the bug, or surface it to you — without you having to check in.

> **Warning**: When piping into `grep`, **always** use `grep --line-buffered`. Without it, grep buffers stdout in 4KB chunks, which can delay events by minutes on low-traffic streams. This is the #1 way Monitor breaks in practice — if your filter seems silent when it shouldn't be, check for the `--line-buffered` flag first.

---

## Scheduled Tasks

Scheduled Tasks let you run prompts automatically on a recurring schedule or as one-time reminders. Tasks are session-scoped — they run while Claude Code is active and are cleared when the session ends. Available since v2.1.72+.

### The `/loop` command

```bash
# Explicit interval
/loop 5m check if the deployment finished

# Natural language
/loop check build status every 30 minutes
```

Standard 5-field cron expressions are also supported for precise scheduling.

### One-time reminders

Set reminders that fire once at a specific time:

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### Managing scheduled tasks

| Tool | Description |
|------|-------------|
| `CronCreate` | Create a new scheduled task |
| `CronList` | List all active scheduled tasks. Since v2.1.136, output also includes the qualifier(s) and the scheduled prompt body, so you can audit what each cron will run without opening it. |
| `CronDelete` | Remove a scheduled task |

**Limits and behavior**:
- Up to **50 scheduled tasks** per session
- Session-scoped — cleared when the session ends
- Recurring tasks auto-expire after **3 days**
- Tasks only fire while Claude Code is running — no catch-up for missed fires

### Behavior details

| Aspect | Detail |
|--------|--------|
| **Recurring jitter** | Up to 10% of the interval (max 15 minutes) |
| **One-shot jitter** | Up to 90 seconds on :00/:30 boundaries |
| **Missed fires** | No catch-up — skipped if Claude Code was not running |
| **Persistence** | Not persisted across restarts |

### Cloud Scheduled Tasks

Use `/schedule` to create Cloud scheduled tasks that run on Anthropic infrastructure:

```
/schedule daily at 9am run the test suite and report failures
```

Cloud scheduled tasks persist across restarts and do not require Claude Code to be running locally.

### Disabling scheduled tasks

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

### Example: monitoring a deployment

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **Tip**: Scheduled tasks are session-scoped. For persistent automation that survives restarts, use CI/CD pipelines, GitHub Actions, or Desktop App scheduled tasks instead.

---

## Permission Modes

Permission modes control what actions Claude can take without explicit approval.

### Available Permission Modes

| Mode | Behavior |
|---|---|
| `default` | Read files only; prompts for all other actions |
| `acceptEdits` | Read and edit files; prompts for commands |
| `plan` | Read files only (research mode, no edits) |
| `auto` | All actions with background safety classifier checks (Research Preview) |
| `bypassPermissions` | All actions, no permission checks (dangerous) |
| `dontAsk` | Only pre-approved tools execute; all others denied |

Cycle through modes with `Shift+Tab` in the CLI. Set a default with the `--permission-mode` flag or the `permissions.defaultMode` setting.

> **`--dangerously-skip-permissions` extended path coverage (v2.1.121, v2.1.126)**: The `--dangerously-skip-permissions` CLI flag (and equivalent `bypassPermissions` mode) now bypasses prompts for writes to a much broader allowlist — `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/`, `.git/`, `.vscode/`, and shell config files. Catastrophic removal commands (`rm -rf /`, etc.) still prompt regardless of mode. Treat the flag as a sharper tool than before; use it only in throwaway sandboxes.

> **Windows shell detection (v2.1.120, v2.1.126)**: Git for Windows / Git Bash is no longer required. When Git Bash is absent, Claude Code uses PowerShell as the shell tool. From v2.1.126 PowerShell is the *primary* shell when the PowerShell tool is enabled, and detection covers PowerShell 7 installed via the Microsoft Store, MSI without PATH, or as a `.NET global tool`.

### Activation Methods

**Keyboard shortcut**:
```bash
Shift + Tab  # Cycle through all 6 modes
```

**Slash command**:
```bash
/plan                  # Enter plan mode
```

**CLI flag**:
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**Setting**:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Permission Mode Examples

#### Default Mode
Claude asks for confirmation on significant actions:

```
User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)
```

#### Plan Mode
Review implementation plan before execution:

```
User: /plan Implement user authentication system

Claude: I'll create a plan for implementing authentication.

## Implementation Plan
[Detailed plan with phases and steps]

Ready to proceed? (yes/no/modify)
```

#### Accept Edits Mode
Automatically accept file modifications:

```
User: acceptEdits
User: Fix the bug in auth.ts

Claude: [Makes changes without asking]
```

### Use Cases

**Code Review**:
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [Reads code, provides feedback, but cannot modify]
```

**Pair Programming**:
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [Asks for approval before each change]
```

**Automated Tasks**:
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [Auto-accepts file edits without asking]
```

---

## Headless Mode

Print mode (`claude -p`) allows Claude Code to run without interactive input, perfect for automation and CI/CD. This is the non-interactive mode, replacing the older `--headless` flag.

### What is Print Mode?

Print mode enables:
- Automated script execution
- CI/CD integration
- Batch processing
- Scheduled tasks

### Running in Print Mode (Non-Interactive)

```bash
# Run specific task
claude -p "Run all tests"

# Process piped content
cat error.log | claude -p "Analyze these errors"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### Additional Print Mode Usage Examples

```bash
# Run a specific task with output capture
claude -p "Run all tests and generate coverage report"

# With structured output
claude -p --output-format json "Analyze code quality"

# With input from stdin
echo "Analyze code quality" | claude -p "explain this"
```

### Example: CI/CD Integration

**GitHub Actions**:
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### Print Mode Configuration

Print mode (`claude -p`) supports several flags for automation:

```bash
# Limit autonomous turns
claude -p --max-turns 5 "refactor this module"

# Structured JSON output
claude -p --output-format json "analyze this codebase"

# With schema validation
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# Disable session persistence
claude -p --no-session-persistence "one-off analysis"
```

---

## Session Management

Manage multiple Claude Code sessions effectively.

### Session Management Commands

| Command | Description |
|---------|-------------|
| `/resume` | Resume a conversation by ID or name |
| `/rename` | Name the current session |
| `/fork` | Fork current session into a new branch |
| `claude -c` | Continue most recent conversation |
| `claude -r "session"` | Resume session by name or ID |

### Resuming Sessions

**Continue last conversation**:
```bash
claude -c
```

**Resume a named session**:
```bash
claude -r "auth-refactor" "finish this PR"
```

**Rename the current session** (inside the REPL):
```
/rename auth-refactor
```

### Forking Sessions

Fork a session to try an alternative approach without losing the original:

```
/fork
```

Or from the CLI:
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### Session Persistence

Sessions are automatically saved and can be resumed:

```bash
# Continue last conversation
claude -c

# Resume specific session by name or ID
claude -r "auth-refactor"

# Resume and fork for experimentation
claude --resume auth-refactor --fork-session "alternative approach"
```

### Session Recap (v2.1.108)

When you return to a session after being away, Claude can show a brief recap of what was accomplished. This is enabled by default for users with telemetry disabled (Bedrock, Vertex, Foundry users).

> **OTEL telemetry — re-enable feedback survey (v2.1.136+)**: Organizations capturing OpenTelemetry data can re-enable Anthropic's session-quality survey by setting `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL=1`. The survey is off by default in OTEL deployments because it was previously redirected away from telemetry pipelines.

**Control recap behavior:**

```bash
/recap                                 # manually trigger a recap
/config                                # toggle auto-recap on/off
```

Or via environment variable:
```bash
CLAUDE_CODE_ENABLE_AWAY_SUMMARY=0 claude   # disable recap
CLAUDE_CODE_ENABLE_AWAY_SUMMARY=1 claude   # force enable recap
```

---

## Interactive Features

### Keyboard Shortcuts

Claude Code supports keyboard shortcuts for efficiency. Here's the complete reference from official docs:

| Shortcut | Description |
|----------|-------------|
| `Ctrl+C` | Cancel current input/generation |
| `Ctrl+D` | Exit Claude Code |
| `Ctrl+G` | Edit plan in external editor |
| `Ctrl+L` | Clear terminal screen |
| `Ctrl+O` | Toggle verbose output (view reasoning) |
| `Ctrl+R` | Reverse search history. Defaults to **all prompts across all projects** (v2.1.129+); press `Ctrl+S` inside the picker to narrow to the current project. Earlier versions defaulted to project-only. |
| `Ctrl+T` | Toggle task list view |
| `Ctrl+B` | Background running tasks |
| `Esc+Esc` | Rewind code/conversation |
| `Shift+Tab` / `Alt+M` | Toggle permission modes |
| `Option+P` / `Alt+P` | Switch model |
| `Option+T` / `Alt+T` | Toggle extended thinking |

**Line Editing (standard readline shortcuts):**

| Shortcut | Action |
|----------|--------|
| `Ctrl + A` | Move to line start |
| `Ctrl + E` | Move to line end |
| `Ctrl + K` | Cut to end of line |
| `Ctrl + U` | Cut to start of line |
| `Ctrl + W` | Delete word backward |
| `Ctrl + Y` | Paste (yank) |
| `Tab` | Autocomplete |
| `↑ / ↓` | Command history |

### Customizing keybindings

Create custom keyboard shortcuts by running `/keybindings`, which opens `~/.claude/keybindings.json` for editing (v2.1.18+).

**Configuration format**:

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

Set a binding to `null` to unbind a default shortcut.

### Available contexts

Keybindings are scoped to specific UI contexts:

| Context | Key Actions |
|---------|-------------|
| **Chat** | `submit`, `cancel`, `cycleMode`, `modelPicker`, `thinkingToggle`, `undo`, `externalEditor`, `stash`, `imagePaste` |
| **Confirmation** | `yes`, `no`, `previous`, `next`, `nextField`, `cycleMode`, `toggleExplanation` |
| **Global** | `interrupt`, `exit`, `toggleTodos`, `toggleTranscript` |
| **Autocomplete** | `accept`, `dismiss`, `next`, `previous` |
| **HistorySearch** | `search`, `previous`, `next` |
| **Settings** | Context-specific settings navigation |
| **Tabs** | Tab switching and management |
| **Help** | Help panel navigation |

There are 18 contexts total including `Transcript`, `Task`, `ThemePicker`, `Attachments`, `Footer`, `MessageSelector`, `DiffDialog`, `ModelPicker`, and `Select`.

### Chord support

Keybindings support chord sequences (multi-key combinations):

```
"ctrl+k ctrl+s"   → Two-key sequence: press ctrl+k, then ctrl+s
"ctrl+shift+p"    → Simultaneous modifier keys
```

**Keystroke syntax**:
- **Modifiers**: `ctrl`, `alt` (or `opt`), `shift`, `meta` (or `cmd`)
- **Uppercase implies Shift**: `K` is equivalent to `shift+k`
- **Special keys**: `escape`, `enter`, `return`, `tab`, `space`, `backspace`, `delete`, arrow keys

### Reserved and conflicting keys

| Key | Status | Notes |
|-----|--------|-------|
| `Ctrl+C` | Reserved | Cannot be rebound (interrupt) |
| `Ctrl+D` | Reserved | Cannot be rebound (exit) |
| `Ctrl+B` | Terminal conflict | tmux prefix key |
| `Ctrl+A` | Terminal conflict | GNU Screen prefix key |
| `Ctrl+Z` | Terminal conflict | Process suspend |

> **Tip**: If a shortcut does not work, check for conflicts with your terminal emulator or multiplexer.

### Tab Completion

Claude Code provides intelligent tab completion:

```
User: /rew<TAB>
→ /rewind

User: /plu<TAB>
→ /plugin

User: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### Command History

Access previous commands:

```
User: <↑>  # Previous command
User: <↓>  # Next command
User: Ctrl+R  # Search history

(reverse-i-search)`test': run all tests
```

### Multi-line Input

For complex queries, use multi-line mode:

```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

**Example:**

```
User: \
> Implement a user authentication system
> with the following requirements:
> - JWT tokens
> - Email verification
> - Password reset
> - 2FA support
> \end

Claude: [Processes the multi-line request]
```

### Inline Editing

Edit commands before sending:

```
User: Deploy to prodcution<Backspace><Backspace>uction

[Edit in-place before sending]
```

### Vim Mode

Enable Vi/Vim keybindings for text editing:

**Activation**:
- Enable via `/config` (toggle "Editor / Vim mode") or in `~/.claude/settings.json` under `editorMode: "vim"`. The standalone `/vim` slash command was removed (see [issue #43370](https://github.com/anthropics/claude-code/issues/43370)); vim mode is now configuration-driven.
- Mode switching with `Esc` for NORMAL, `i/a/o` for INSERT, `v` for VISUAL, `V` for VISUAL-LINE (v2.1.118+)

**Navigation keys**:
- `h` / `l` - Move left/right
- `j` / `k` - Move down/up
- `w` / `b` / `e` - Move by word
- `0` / `$` - Move to line start/end
- `gg` / `G` - Jump to start/end of text

**Text objects**:
- `iw` / `aw` - Inner/around word
- `i"` / `a"` - Inner/around quoted string
- `i(` / `a(` - Inner/around parentheses

**Visual modes (v2.1.118+)**:

| Key | Mode | Behavior |
|-----|------|----------|
| `v` | Visual | Character-wise selection with visual feedback; extend with motion keys |
| `V` | Visual-line | Line-wise selection; always selects whole lines |
| `y` | Yank | Copy the current visual selection |
| `d` / `x` | Delete | Delete the current visual selection |
| `c` | Change | Delete selection and enter INSERT mode |
| `Esc` | Exit | Return to NORMAL mode |

Visual selections are highlighted in the input field so you can see exactly what will be yanked, deleted, or changed before you commit the operator.

### Bash Mode

Execute shell commands directly with `!` prefix:

```bash
! npm test
! git status
! cat src/index.js
```

Use this for quick command execution without switching contexts.

---

## TUI Mode (Fullscreen)

> **New in v2.1.110**

TUI (Text User Interface) mode renders Claude Code in fullscreen with flicker-free output — ideal for terminal multiplexers like tmux or iTerm2 split panes.

### Enabling TUI Mode

Toggle TUI mode with the `/tui` command or launch with the `--tui` flag:

```bash
/tui          # toggle from within a session
claude --tui  # start directly in TUI mode
```

### Configuration

| Setting | Description | Default |
|---------|-------------|---------|
| `autoScrollEnabled` | Auto-scroll to latest message | `true` |

Disable auto-scroll via `/config` or `settings.json`:

```json
{
  "autoScrollEnabled": false
}
```

### Focus View

The `/focus` command toggles focus view — a distraction-free display showing only the most relevant output. `Ctrl+O` now toggles between normal and verbose transcript only (focus view is `/focus`).

---

## Voice Dictation

Voice Dictation provides push-to-talk voice input for Claude Code, allowing you to speak your prompts instead of typing them.

### Activating Voice Dictation

```
/voice
```

### Features

| Feature | Description |
|---------|-------------|
| **Push-to-talk** | Hold a key to record, release to send |
| **20 languages** | Speech-to-text supports 20 languages |
| **Custom keybinding** | Configure the push-to-talk key via `/keybindings` |
| **Account requirement** | Requires a Claude.ai account for STT processing |

### Configuration

Customize the push-to-talk keybinding in your keybindings file (`/keybindings`). Voice dictation uses your Claude.ai account for speech-to-text processing.

---

## Channels

Channels is a Research Preview feature that pushes events from external services into a running Claude Code session via MCP servers. Sources include Telegram, Discord, iMessage, and arbitrary webhooks, allowing Claude to react to real-time notifications without polling.

> **Auth (v2.1.128+)**: `--channels` now works with both Pro/Max OAuth **and** API-key (console) authentication. Earlier releases required OAuth.

### Subscribing to Channels

```bash
# Subscribe to channel plugins at startup
claude --channels discord,telegram

# Subscribe to multiple sources
claude --channels discord,telegram,imessage,webhooks
```

### Supported Integrations

| Integration | Description |
|-------------|-------------|
| **Discord** | Receive and respond to Discord messages in your session |
| **Telegram** | Receive and respond to Telegram messages in your session |
| **iMessage** | Receive iMessage notifications in your session |
| **Webhooks** | Receive events from arbitrary webhook sources |

### Configuration

Configure channels with the `--channels` flag at startup. For enterprise deployments, use the managed setting to control which channel plugins are permitted:

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

The `allowedChannelPlugins` managed setting controls which channel plugins are permitted across the organization.

### How It Works

1. MCP servers act as channel plugins that connect to external services
2. Incoming messages and events are pushed into the active Claude Code session
3. Claude can read and respond to messages within the session context
4. Channel plugins must be approved via the `allowedChannelPlugins` managed setting
5. No polling required — events are pushed in real time

---

## Chrome Integration

Chrome Integration connects Claude Code to your Chrome or Microsoft Edge browser for live web automation and debugging. This is a beta feature available since v2.0.73+ (Edge support added in v1.0.36+).

### Enabling Chrome Integration

**At startup**:

```bash
claude --chrome      # Enable Chrome connection
claude --no-chrome   # Disable Chrome connection
```

**Within a session**:

```
/chrome
```

Select "Enabled by default" to activate Chrome Integration for all future sessions. Claude Code shares your browser's login state, so it can interact with authenticated web apps.

### Capabilities

| Capability | Description |
|------------|-------------|
| **Live debugging** | Read console logs, inspect DOM elements, debug JavaScript in real time |
| **Design verification** | Compare rendered pages against design mockups |
| **Form validation** | Test form submissions, input validation, and error handling |
| **Web app testing** | Interact with authenticated apps (Gmail, Google Docs, Notion, etc.) |
| **Data extraction** | Scrape and process content from web pages |
| **Session recording** | Record browser interactions as GIF files |

### Site-level permissions

The Chrome extension manages per-site access. Grant or revoke access for specific sites at any time through the extension popup. Claude Code only interacts with sites you have explicitly allowed.

### How it works

Claude Code controls the browser in a visible window — you can watch actions happen in real time. When the browser encounters a login page or CAPTCHA, Claude pauses and waits for you to handle it manually before continuing.

### Known limitations

- **Browser support**: Chrome and Edge only — Brave, Arc, and other Chromium browsers are not supported
- **WSL**: Not available in Windows Subsystem for Linux
- **Third-party providers**: Not supported with Bedrock, Vertex, or Foundry API providers
- **Service worker idle**: The Chrome extension service worker may go idle during extended sessions

> **Tip**: Chrome Integration is a beta feature. Browser support may expand in future releases.

---

## Remote Control

Remote Control lets you continue a locally running Claude Code session from your phone, tablet, or any browser. Your local session keeps running on your machine — nothing moves to the cloud. Available on Pro, Max, Team, and Enterprise plans (v2.1.51+).

### Starting Remote Control

**From the CLI**:

```bash
# Start with default session name
claude remote-control

# Start with a custom name
claude remote-control --name "Auth Refactor"
```

**From within a session**:

```
/remote-control
/remote-control "Auth Refactor"
```

**Available flags**:

| Flag | Description |
|------|-------------|
| `--name "title"` | Custom session title for easy identification |
| `--verbose` | Show detailed connection logs |
| `--sandbox` | Enable filesystem and network isolation |
| `--no-sandbox` | Disable sandboxing (default) |

### Connecting to a session

Three ways to connect from another device:

1. **Session URL** — Printed to the terminal when the session starts; open in any browser
2. **QR code** — Press `spacebar` after starting to display a scannable QR code
3. **Find by name** — Browse your sessions at claude.ai/code or in the Claude mobile app (iOS/Android)

### Security

- **No inbound ports** opened on your machine
- **Outbound HTTPS only** over TLS
- **Scoped credentials** — multiple short-lived, narrowly scoped tokens
- **Session isolation** — each remote session is independent

### Remote Control vs Claude Code on the web

| Aspect | Remote Control | Claude Code on Web |
|--------|---------------|-------------------|
| **Execution** | Runs on your machine | Runs on Anthropic cloud |
| **Local tools** | Full access to local MCP servers, files, and CLI | No local dependencies |
| **Use case** | Continue local work from another device | Start fresh from any browser |

### Limitations

- One remote session per Claude Code instance
- Terminal must stay open on the host machine
- Session times out after ~10 minutes if the network is unreachable

### Use cases

- Control Claude Code from a mobile device or tablet while away from your desk
- Use the richer claude.ai UI while maintaining local tool execution
- Quick code reviews on the go with your full local development environment

### Push Notifications (v2.1.110)

When Remote Control is active and "Push when Claude decides" is enabled in `/config`, Claude can send mobile push notifications to your phone — for example, when a long task completes or needs your input.

To enable:
1. Activate Remote Control: `/remote-control` or `claude --rc`
2. Open `/config` and enable **Push when Claude decides**

Push notifications require a Claude subscription and the Claude mobile app.

### Disabling Remote Control (`disableRemoteControl`, v2.1.128+)

Admins on Team or Enterprise plans can block Remote Control entirely with the `disableRemoteControl` setting. When `true`, both `claude remote-control` and `/remote-control` refuse to start.

```json
{
  "disableRemoteControl": true
}
```

The setting is honored at the **managed/policy** scope (e.g., `/Library/Application Support/ClaudeCode/managed-settings.json` on macOS) so it cannot be overridden by individual users. Useful when local-only execution must be enforced organization-wide.

---

## Web Sessions

Web Sessions allow you to run Claude Code directly in the browser at claude.ai/code, or create web sessions from the CLI.

### Creating a Web Session

```bash
# Create a new web session from the CLI
claude --remote "implement the new API endpoints"
```

This starts a Claude Code session on claude.ai that you can access from any browser.

### Resuming Web Sessions Locally

If you started a session on the web and want to continue it locally:

```bash
# Resume a web session in the local terminal
claude --teleport
```

Or from within an interactive REPL:
```
/teleport
```

### Use Cases

- Start work on one machine and continue on another
- Share a session URL with team members
- Use the web UI for visual diff review, then switch to terminal for execution

---

## Desktop App

The Claude Code Desktop App provides a standalone application with visual diff review, parallel sessions, and integrated connectors. Available for macOS and Windows (Pro, Max, Team, and Enterprise plans).

### Installation

Download from [claude.ai](https://claude.ai) for your platform:
- **macOS**: Universal build (Apple Silicon and Intel)
- **Windows**: x64 and ARM64 installers available

See the [Desktop Quickstart](https://code.claude.com/docs/en/desktop-quickstart) for setup instructions.

### Handing off from CLI

Transfer your current CLI session to the Desktop App:

```
/desktop
```

### Core features

| Feature | Description |
|---------|-------------|
| **Diff view** | File-by-file visual review with inline comments; Claude reads comments and revises |
| **App preview** | Auto-starts dev servers with an embedded browser for live verification |
| **PR monitoring** | GitHub CLI integration with auto-fix CI failures and auto-merge when checks pass |
| **Parallel sessions** | Multiple sessions in the sidebar with automatic Git worktree isolation |
| **Scheduled tasks** | Recurring tasks (hourly, daily, weekdays, weekly) that run while the app is open |
| **Rich rendering** | Code, markdown, and diagram rendering with syntax highlighting |

### App preview configuration

Configure dev server behavior in `.claude/launch.json`:

```json
{
  "command": "npm run dev",
  "port": 3000,
  "readyPattern": "ready on",
  "persistCookies": true
}
```

### Connectors

Connect external services for richer context:

| Connector | Capability |
|-----------|------------|
| **GitHub** | PR monitoring, issue tracking, code review |
| **Slack** | Notifications, channel context |
| **Linear** | Issue tracking, sprint management |
| **Notion** | Documentation, knowledge base access |
| **Asana** | Task management, project tracking |
| **Calendar** | Schedule awareness, meeting context |

> **Note**: Connectors are not available for remote (cloud) sessions.

### Remote and SSH sessions

- **Remote sessions**: Run on Anthropic cloud infrastructure; continue even when the app is closed. Accessible from claude.ai/code or the Claude mobile app
- **SSH sessions**: Connect to remote machines over SSH with full access to the remote filesystem and tools. Claude Code must be installed on the remote machine

### Permission modes in Desktop

The Desktop App supports the same 4 permission modes as the CLI:

| Mode | Behavior |
|------|----------|
| **Ask permissions** (default) | Review and approve every edit and command |
| **Auto accept edits** | File edits auto-approved; commands require manual approval |
| **Plan mode** | Review approach before any changes are made |
| **Bypass permissions** | Automatic execution (sandbox-only, admin-controlled) |

### Enterprise features

- **Admin console**: Control Code tab access and permission settings for the organization
- **MDM deployment**: Deploy via MDM on macOS or MSIX on Windows
- **SSO integration**: Require single sign-on for organization members
- **Managed settings**: Centrally manage team configuration and model availability

---

## Task List

The Task List feature provides persistent task tracking that survives context compactions (when the conversation history is trimmed to fit the context window).

### Toggling the Task List

Press `Ctrl+T` to toggle the task list view on or off during a session.

### Persistent Tasks

Tasks persist across context compactions, ensuring that long-running work items are not lost when the conversation context is trimmed. This is particularly useful for complex, multi-step implementations.

### Named Task Directories

Use the `CLAUDE_CODE_TASK_LIST_ID` environment variable to create named task directories shared across sessions:

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

This allows multiple sessions to share the same task list, making it useful for team workflows or multi-session projects.

---

## Prompt Suggestions

Prompt Suggestions display grayed-out example commands based on your git history and current conversation context.

### How It Works

- Suggestions appear as grayed-out text below your input prompt
- Press `Tab` to accept the suggestion
- Press `Enter` to accept and immediately submit
- Suggestions are context-aware, drawing from git history and conversation state

### Disabling Prompt Suggestions

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git Worktrees

Git Worktrees allow you to start Claude Code in an isolated worktree, enabling parallel work on different branches without stashing or switching.

### Starting in a Worktree

```bash
# Start Claude Code in an isolated worktree
claude --worktree
# or
claude -w
```

### Worktree Location

Worktrees are created at:
```
<repo>/.claude/worktrees/<name>
```

### Sparse Checkout for Monorepos

Use the `worktree.sparsePaths` setting to perform sparse-checkout in monorepos, reducing disk usage and clone time:

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### Base Branch Reference (`worktree.baseRef`)

**`worktree.baseRef`** (added v2.1.133) — controls whether `claude --worktree` branches from `origin/<default>` or local `HEAD`.

- `"fresh"` (default) — branch from `origin/<default-branch>`, ignoring local unpushed commits. **This reverts the behavior introduced in v2.1.128**, so users who relied on local-HEAD branching after v2.1.128 must opt back in.
- `"head"` — branch from local `HEAD`, preserving unpushed commits.

Set in `~/.claude/settings.json`:

```json
{ "worktree": { "baseRef": "head" } }
```

### Worktree Tools and Hooks

| Item | Description |
|------|-------------|
| `ExitWorktree` | Tool to exit and clean up the current worktree |
| `WorktreeCreate` | Hook event fired when a worktree is created |
| `WorktreeRemove` | Hook event fired when a worktree is removed |

### Auto-Cleanup

If no changes are made in the worktree, it is automatically cleaned up when the session ends.

### Use Cases

- Work on a feature branch while keeping main branch untouched
- Run tests in isolation without affecting the working directory
- Try experimental changes in a disposable environment
- Sparse-checkout specific packages in monorepos for faster startup

---

## Sandboxing

Sandboxing provides OS-level filesystem and network isolation for Bash commands executed by Claude Code. This is complementary to permission rules and provides an additional security layer.

### Enabling Sandboxing

**Slash command**:
```
/sandbox
```

**CLI flags**:
```bash
claude --sandbox       # Enable sandboxing
claude --no-sandbox    # Disable sandboxing
```

### Configuration Settings

| Setting | Description |
|---------|-------------|
| `sandbox.enabled` | Enable or disable sandboxing |
| `sandbox.failIfUnavailable` | Fail if sandboxing cannot be activated |
| `sandbox.filesystem.allowWrite` | Paths allowed for write access |
| `sandbox.filesystem.allowRead` | Paths allowed for read access |
| `sandbox.filesystem.denyRead` | Paths denied for read access |
| `sandbox.network.allowedDomains` | Domains Bash-launched processes are allowed to reach (supports `*.` wildcard) |
| `sandbox.network.deniedDomains` | Domains to block even when `allowedDomains` wildcard would otherwise permit them (v2.1.113+) |
| `sandbox.enableWeakerNetworkIsolation` | Enable weaker network isolation on macOS |
| `sandbox.bwrapPath` | (v2.1.133+, Linux/WSL) Path to the `bubblewrap` binary. Default: `$PATH` lookup. |
| `sandbox.socatPath` | (v2.1.133+, Linux/WSL) Path to the `socat` binary. Default: `$PATH` lookup. |

**Linux/WSL binary paths** (v2.1.133+) — point Claude Code at non-standard install locations:

```json
{
  "sandbox": {
    "bwrapPath": "/opt/bubblewrap/bin/bwrap",
    "socatPath": "/opt/socat/bin/socat"
  }
}
```

Example of `deniedDomains` overriding a broad wildcard (v2.1.113+):

```json
{
  "sandbox": {
    "network": {
      "allowedDomains": ["*.example.com"],
      "deniedDomains": ["evil.example.com"]
    }
  }
}
```

The wildcard lets everything on `example.com` through, but `deniedDomains` still blocks the specifically-named host.

### Example Configuration

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    },
    "enableWeakerNetworkIsolation": true
  }
}
```

### How It Works

- Bash commands run in a sandboxed environment with restricted filesystem access
- Network access can be isolated to prevent unintended external connections
- Works alongside permission rules for defense in depth
- On macOS, use `sandbox.enableWeakerNetworkIsolation` for network restrictions (full network isolation is not available on macOS)

### Use Cases

- Running untrusted or generated code safely
- Preventing accidental modifications to files outside the project
- Restricting network access during automated tasks

---

## Managed Settings (Enterprise)

Managed Settings enable enterprise administrators to deploy Claude Code configuration across an organization using platform-native management tools.

### Deployment Methods

| Platform | Method | Since |
|----------|--------|-------|
| macOS | Managed plist files (MDM) | v2.1.51+ |
| Windows | Windows Registry | v2.1.51+ |
| Cross-platform | Managed configuration files | v2.1.51+ |
| Cross-platform | Managed drop-ins (`managed-settings.d/` directory) | v2.1.83+ |

### Managed Drop-ins

Since v2.1.83, administrators can deploy multiple managed settings files into a `managed-settings.d/` directory. Files are merged in alphabetical order, allowing modular configuration across teams:

```
~/.claude/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### Available Managed Settings

| Setting | Description |
|---------|-------------|
| `disableBypassPermissionsMode` | Prevent users from enabling bypass permissions |
| `availableModels` | Restrict which models users can select |
| `allowedChannelPlugins` | Control which channel plugins are permitted |
| `autoMode.environment` | Configure trusted infrastructure for auto mode |
| `wslInheritsWindowsSettings` | Windows/WSL only (v2.1.118+): when `true`, Claude Code running inside WSL inherits managed settings from the Windows host, so enterprise policies deployed via Registry/MDM apply uniformly across the Windows and WSL shells |
| `parentSettingsBehavior` | (v2.1.133+, admin-tier) Controls how the SDK's `managedSettings` merges with parent-process settings. `"first-wins"` keeps existing precedence (earlier setting wins on conflict); `"merge"` deep-merges values. |
| Custom policies | Organization-specific permission and tool policies |

### Example: macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>disableBypassPermissionsMode</key>
  <true/>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## Configuration and Settings

### Configuration File Locations

1. **Global config**: `~/.claude/config.json`
2. **Project config**: `./.claude/config.json`
3. **User config**: `~/.config/claude-code/settings.json`

### Complete Configuration Example

**Core advanced features configuration:**

```json
{
  "permissions": {
    "mode": "default"
  },
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh"
  },
  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    }
  }
}
```

**Extended configuration example:**

```json
{
  "permissions": {
    "mode": "default",
    "allowedTools": ["Bash(git log:*)", "Read"],
    "disallowedTools": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": ["eslint --fix ${file_path}"] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": ["~/.claude/hooks/security-scan.sh"] }],
    "Stop": [{ "hooks": ["~/.claude/hooks/notify.sh"] }]
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### Environment Variables

Override config with environment variables:

```bash
# Model selection
export ANTHROPIC_MODEL=claude-opus-4-7
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-7
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# API configuration
export ANTHROPIC_API_KEY=sk-ant-...

# Thinking configuration
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=xhigh   # low, medium, high, xhigh (Opus 4.7 only, default), or max (supported on Opus 4.7, Opus 4.6, Sonnet 4.6)

# Feature toggles
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # Set by --bare flag

# MCP configuration
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Prompt caching
export ENABLE_PROMPT_CACHING_1H=1      # Use 1-hour prompt cache TTL (default is 5 min)

# Task management
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Agent teams (experimental)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Subagent and plugin configuration
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=1

# Subprocess and streaming
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000

# Output and package manager (v2.1.129+)
export CLAUDE_CODE_FORCE_SYNC_OUTPUT=1                      # Force synchronous output for terminals where auto-detect misses (Emacs eat, etc.)
export CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1            # Enable background upgrades for Homebrew/WinGet installs
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1         # Opt in to /v1/models gateway discovery when ANTHROPIC_BASE_URL is set
```

> **v2.1.108**: `ENABLE_PROMPT_CACHING_1H=1` — use a 1-hour prompt cache TTL instead of the default 5-minute TTL. Reduces cache misses in long, stable sessions. (v2.1.129 fixes a regression where the 1-hour TTL was silently downgraded to 5 minutes.)

> **v2.1.129**: `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` forces synchronous output for terminals whose capability auto-detection fails (e.g., Emacs `eat`). `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1` enables background upgrades on Homebrew/WinGet installs, which otherwise never auto-update.

### Configuration Management Commands

```
User: /config
[Opens interactive configuration menu]
```

The `/config` command provides an interactive menu to toggle settings such as:
- Extended thinking on/off
- Verbose output
- Permission mode
- Model selection

### Per-Project Configuration

Create `.claude/config.json` in your project:

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": ["npm test && npm run lint"] }]
  },
  "permissions": {
    "mode": "default"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

## Agent Teams

Agent Teams is an experimental feature that enables multiple Claude Code instances to collaborate on a task. It is disabled by default.

### Enabling Agent Teams

Enable via environment variable or settings:

```bash
# Environment variable
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

Or add to your settings JSON:

```json
{
  "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
}
```

### How Agent Teams Work

- A **team lead** coordinates the overall task and delegates subtasks to teammates
- **Teammates** work independently, each with their own context window
- A **shared task list** enables self-coordination between team members
- Use subagent definitions (`.claude/agents/` or `--agents` flag) to define teammate roles and specializations

### Display Modes

Agent Teams support two display modes, configured with the `--teammate-mode` flag:

| Mode | Description |
|------|-------------|
| `in-process` (default) | Teammates run within the same terminal process |
| `tmux` | Each teammate gets a dedicated split pane (requires tmux or iTerm2) |
| `auto` | Automatically selects the best display mode |

```bash
# Use tmux split panes for teammate display
claude --teammate-mode tmux

# Explicitly use in-process mode
claude --teammate-mode in-process
```

### Use Cases

- Large refactoring tasks where different teammates handle different modules
- Parallel code review and implementation
- Coordinated multi-file changes across a codebase

> **Note**: Agent Teams is experimental and may change in future releases. See [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) for the full reference.

---

## Best Practices

### Planning Mode
- ✅ Use for complex multi-step tasks
- ✅ Review plans before approving
- ✅ Modify plans when needed
- ❌ Don't use for simple tasks

### Extended Thinking
- ✅ Use for architectural decisions
- ✅ Use for complex problem-solving
- ✅ Review the thinking process
- ❌ Don't use for simple queries

### Background Tasks
- ✅ Use for long-running operations
- ✅ Monitor task progress
- ✅ Handle task failures gracefully
- ❌ Don't start too many concurrent tasks

### Permissions
- ✅ Use `plan` for code review (read-only)
- ✅ Use `default` for interactive development
- ✅ Use `acceptEdits` for automation workflows
- ✅ Use `auto` for autonomous work with safety guardrails
- ❌ Don't use `bypassPermissions` unless absolutely necessary

### Sessions
- ✅ Use separate sessions for different tasks
- ✅ Save important session states
- ✅ Clean up old sessions
- ❌ Don't mix unrelated work in one session

---

## Additional Resources

For more information about Claude Code and related features:

- [Official Interactive Mode Documentation](https://code.claude.com/docs/en/interactive-mode)
- [Official Headless Mode Documentation](https://code.claude.com/docs/en/headless)
- [CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Checkpoints Guide](../08-checkpoints/) - Session management and rewinding
- [Slash Commands](../01-slash-commands/) - Command reference
- [Memory Guide](../02-memory/) - Persistent context
- [Skills Guide](../03-skills/) - Autonomous capabilities
- [Subagents Guide](../04-subagents/) - Delegated task execution
- [MCP Guide](../05-mcp/) - External data access
- [Hooks Guide](../06-hooks/) - Event-driven automation
- [Plugins Guide](../07-plugins/) - Bundled extensions
- [Official Scheduled Tasks Documentation](https://code.claude.com/docs/en/scheduled-tasks)
- [Official Chrome Integration Documentation](https://code.claude.com/docs/en/chrome)
- [Official Remote Control Documentation](https://code.claude.com/docs/en/remote-control)
- [Official Keybindings Documentation](https://code.claude.com/docs/en/keybindings)
- [Official Desktop App Documentation](https://code.claude.com/docs/en/desktop)
- [Official Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams)

---

**Last Updated**: May 9, 2026
**Claude Code Version**: 2.1.138
**Sources**:
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/interactive-mode
- https://code.claude.com/docs/en/settings
- https://www.anthropic.com/news/claude-opus-4-7
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.118
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
