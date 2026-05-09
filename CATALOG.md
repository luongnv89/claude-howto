<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code Feature Catalog

> Quick reference guide to all Claude Code features: commands, agents, skills, plugins, and hooks.

**Navigation**: [Commands](#slash-commands) | [Permission Modes](#permission-modes) | [Subagents](#subagents) | [Skills](#skills) | [Plugins](#plugins) | [MCP Servers](#mcp-servers) | [Hooks](#hooks) | [Memory](#memory-files) | [New Features](#new-features-may-2026)

---

## Summary

| Feature | Built-in | Examples | Total | Reference |
|---------|----------|----------|-------|-----------|
| **Slash Commands** | 60+ | 8 | 68+ | [01-slash-commands/](01-slash-commands/) |
| **Subagents** | 6 | 11 | 17 | [04-subagents/](04-subagents/) |
| **Skills** | 5 bundled | 6 | 11 | [03-skills/](03-skills/) |
| **Plugins** | - | 3 | 3 | [07-plugins/](07-plugins/) |
| **MCP Servers** | 1 | 8 | 9 | [05-mcp/](05-mcp/) |
| **Hooks** | 28 events | 8 | 8 | [06-hooks/](06-hooks/) |
| **Memory** | 7 types | 3 | 3 | [02-memory/](02-memory/) |
| **Total** | **99** | **47** | **121** | |

---

## Slash Commands

Commands are user-invoked shortcuts that execute specific actions.

### Built-in Commands

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/help` | Show help information | Get started, learn commands |
| `/btw` | Ephemeral side question — doesn't pollute main context | Quick tangent questions |
| `/chrome` | Configure Chrome integration | Browser automation |
| `/clear` | Clear conversation history | Start fresh, reduce context |
| `/diff` | Interactive diff viewer | Review changes |
| `/config` | View/edit configuration | Customize behavior |
| `/status` | Show session status | Check current state |
| `/agents` | List available agents | See delegation options |
| `/skills` | List available skills | See auto-invoke capabilities |
| `/hooks` | List configured hooks | Debug automation |
| `/insights` | Analyze session patterns | Session optimization |
| `/install-slack-app` | Install Claude Slack app | Slack integration |
| `/keybindings` | Customize keyboard shortcuts | Key customization |
| `/mcp` | List MCP servers | Check external integrations |
| `/memory` | View loaded memory files | Debug context loading |
| `/mobile` | Generate mobile QR code | Mobile access |
| `/passes` | View usage passes | Subscription info |
| `/plugin` | Manage plugins | Install/remove extensions |
| `/plan` | Enter planning mode | Complex implementations |
| `/proactive` | Alias for `/loop` (v2.1.105) | Same as `/loop` |
| `/recap` | Show session recap when returning to a session | After being away, get context on what was done |
| `/rewind` | Rewind to checkpoint | Undo changes, explore alternatives |
| `/checkpoint` | Manage checkpoints | Save/restore states |
| `/cost` | Shortcut alias that opens the cost tab of `/usage` (v2.1.118+) | Monitor spending |
| `/context` | Show context window usage | Manage conversation length |
| `/export` | Export conversation | Save for reference |
| `/extra-usage` | Configure extra usage limits | Rate limit management |
| `/feedback` | Submit feedback or bug report | Report issues |
| `/login` | Authenticate with Anthropic | Access features |
| `/logout` | Sign out | Switch accounts |
| `/sandbox` | Toggle sandbox mode | Safe command execution |
| `/doctor` | Run diagnostics | Troubleshoot issues |
| `/reload-plugins` | Reload installed plugins | Plugin management |
| `/release-notes` | Show release notes | Check new features |
| `/remote-control` | Enable remote control | Remote access |
| `/permissions` | Manage permissions | Control access |
| `/session` | Manage sessions | Multi-session workflows |
| `/rename` | Rename current session | Organize sessions |
| `/resume` | Resume previous session | Continue work |
| `/todo` | View/manage todo list | Track tasks |
| `/tui` | Toggle fullscreen TUI (text user interface) mode | Flicker-free rendering in fullscreen/tmux |
| `/tasks` | View background tasks | Monitor async operations |
| `/copy` | Copy last response to clipboard | Share output quickly |
| `/teleport` | Transfer session to another machine | Continue work remotely |
| `/desktop` | Open Claude Desktop app | Switch to desktop interface |
| `/theme` | Change color theme; v2.1.118 added custom named themes via `~/.claude/themes/<name>.json` (plugins can ship a `themes/` dir) | Customize appearance |
| `/usage` | Canonical command for usage/cost/stats — merged `/cost` and `/stats` into a single tabbed view (v2.1.118) | Monitor quota and costs |
| `/focus` | Toggle focus view (distraction-free output display) | Reduce visual noise during long tasks |
| `/fork` | Fork current conversation | Explore alternatives |
| `/stats` | Shortcut alias that opens the stats tab of `/usage` (v2.1.118+) | Review session metrics |
| `/statusline` | Configure status line | Customize status display |
| `/stickers` | View session stickers | Fun rewards |
| `/fast` | Toggle fast output mode | Speed up responses |
| `/terminal-setup` | Configure terminal integration | Setup terminal features |
| `/undo` | Alias for `/rewind` (v2.1.108) | Same as `/rewind` |
| `/upgrade` | Check for updates | Version management |
| `/team-onboarding` | Generate a teammate ramp-up guide from this project's Claude Code usage | Onboarding new teammates (v2.1.101) |
| `/ultraplan` | Hand a planning task to a Claude Code web session in plan mode | Heavy planning offload (Research Preview, v2.1.91+) |
| `/ultrareview` | Run a cloud multi-agent code review over your current changes | Deep pre-merge review across multiple agents (v2.1.112) |
| `/less-permission-prompts` | Scan transcripts and propose a prioritized allowlist for common read-only tools | Reduce repeat permission prompts in a project (v2.1.112) |

### Custom Commands (Examples)

| Command | Description | When to Use | Scope | Installation |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | Analyze code for optimization | Performance improvement | Project | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | Prepare pull request | Before submitting PRs | Project | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | Generate API documentation | Document APIs | Project | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | Create git commit with context | Commit changes | User | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | Stage, commit, and push | Quick deployment | User | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | Restructure documentation | Improve docs | Project | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | Setup CI/CD pipeline | New projects | Project | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | Expand test coverage | Improve testing | Project | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **Scope**: `User` = personal workflows (`~/.claude/commands/`), `Project` = team-shared (`.claude/commands/`)

**Reference**: [01-slash-commands/](01-slash-commands/) | [Official Docs](https://code.claude.com/docs/en/interactive-mode)

**Quick Install (All Custom Commands)**:
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## Permission Modes

Claude Code supports 6 permission modes that control how tool use is authorized.

| Mode | Description | When to Use |
|------|-------------|-------------|
| `default` | Prompt for each tool call | Standard interactive use |
| `acceptEdits` | Auto-accept file edits, prompt for others | Trusted editing workflows |
| `plan` | Read-only tools only, no writes | Planning and exploration |
| `auto` | Accept all tools without prompting | Fully autonomous operation (Research Preview) |
| `bypassPermissions` | Skip all permission checks | CI/CD, headless environments |
| `dontAsk` | Skip tools that would require permission | Non-interactive scripting |

> **Note**: `auto` mode is a Research Preview feature (March 2026). Use `bypassPermissions` only in trusted, sandboxed environments.

**Reference**: [Official Docs](https://code.claude.com/docs/en/permissions)

---

## Subagents

Specialized AI assistants with isolated contexts for specific tasks.

### Built-in Subagents

| Agent | Description | Tools | Model | When to Use |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | Multi-step tasks, research | All tools | Inherits model | Complex research, multi-file tasks |
| **Plan** | Implementation planning | Read, Glob, Grep, Bash | Inherits model | Architecture design, planning |
| **Explore** | Codebase exploration | Read, Glob, Grep | Haiku 4.5 | Quick searches, understanding code |
| **Bash** | Command execution | Bash | Inherits model | Git operations, terminal tasks |
| **statusline-setup** | Status line configuration | Bash, Read, Write | Sonnet 4.6 | Configure status line display |
| **Claude Code Guide** | Help and documentation | Read, Glob, Grep | Haiku 4.5 | Getting help, learning features |

### Subagent Configuration Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Agent identifier |
| `description` | string | What the agent does |
| `model` | string | Model override (e.g., `haiku-4.5`) |
| `tools` | array | Allowed tools list |
| `effort` | string | Reasoning effort level (`low`, `medium`, `high`) |
| `initialPrompt` | string | System prompt injected at agent start |
| `disallowedTools` | array | Tools explicitly denied to this agent |

### Custom Subagents (Examples)

| Agent | Description | When to Use | Scope | Installation |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | Comprehensive code quality | Code review sessions | Project | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | Feature architecture design | New feature planning | Project | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | Deep codebase analysis | Understanding existing features | Project | `cp 04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | Clean Code principles review | Maintainability review | Project | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | Test strategy & coverage | Test planning | Project | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | Technical documentation | API docs, guides | Project | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | Security-focused review | Security audits | Project | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | Full feature implementation | Feature development | Project | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | Root cause analysis | Bug investigation | User | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL queries, data analysis | Data tasks | User | `cp 04-subagents/data-scientist.md .claude/agents/` |
| `performance-optimizer` | Profiling & performance tuning | Bottleneck investigation | Project | `cp 04-subagents/performance-optimizer.md .claude/agents/` |

> **Scope**: `User` = personal (`~/.claude/agents/`), `Project` = team-shared (`.claude/agents/`)

**Reference**: [04-subagents/](04-subagents/) | [Official Docs](https://code.claude.com/docs/en/sub-agents)

**Quick Install (All Custom Agents)**:
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## Skills

Auto-invoked capabilities with instructions, scripts, and templates.

### Example Skills

| Skill | Description | When Auto-Invoked | Scope | Installation |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | Comprehensive code review | "Review this code", "Check quality" | Project | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | Brand consistency checker | Writing marketing copy | Project | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | API documentation generator | "Generate docs", "Document API" | Project | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | Systematic code refactoring (Martin Fowler) | "Refactor this", "Clean up code" | User | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **Scope**: `User` = personal (`~/.claude/skills/`), `Project` = team-shared (`.claude/skills/`)

### Skill Structure

```
~/.claude/skills/skill-name/
├── SKILL.md          # Skill definition & instructions
├── scripts/          # Helper scripts
└── templates/        # Output templates
```

### Skill Frontmatter Fields

Skills support YAML frontmatter in `SKILL.md` for configuration:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Skill display name |
| `description` | string | What the skill does |
| `autoInvoke` | array | Trigger phrases for auto-invocation |
| `effort` | string | Reasoning effort level (`low`, `medium`, `high`) |
| `shell` | string | Shell to use for scripts (`bash`, `zsh`, `sh`) |

**Reference**: [03-skills/](03-skills/) | [Official Docs](https://code.claude.com/docs/en/skills)

**Quick Install (All Skills)**:
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### Bundled Skills

| Skill | Description | When Auto-Invoked |
|-------|-------------|-------------------|
| `/simplify` | Review code for quality | After writing code |
| `/batch` | Run prompts on multiple files | Batch operations |
| `/debug` | Debug failing tests/errors | Debugging sessions |
| `/loop` | Run prompts on interval | Recurring tasks |
| `/claude-api` | Build apps with Claude API | API development |

---

## Plugins

Bundled collections of commands, agents, MCP servers, and hooks.

### Example Plugins

| Plugin | Description | Components | When to Use | Scope | Installation |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | PR review workflow | 3 commands, 3 agents, GitHub MCP | Code reviews | Project | `/plugin install pr-review` |
| `devops-automation` | Deployment & monitoring | 4 commands, 3 agents, K8s MCP | DevOps tasks | Project | `/plugin install devops-automation` |
| `documentation` | Doc generation suite | 4 commands, 3 agents, templates | Documentation | Project | `/plugin install documentation` |

> **Scope**: `Project` = team-shared, `User` = personal workflows

### Plugin Structure

```
.claude-plugin/
├── plugin.json       # Manifest file
├── commands/         # Slash commands
├── agents/           # Subagents
├── skills/           # Skills
├── mcp/              # MCP configurations
├── hooks/            # Hook scripts
└── scripts/          # Utility scripts
```

**Reference**: [07-plugins/](07-plugins/) | [Official Docs](https://code.claude.com/docs/en/plugins)

**Plugin Management Commands**:
```bash
/plugin list              # List installed plugins
/plugin install <name>    # Install plugin
/plugin remove <name>     # Remove plugin
/plugin update <name>     # Update plugin
```

---

## MCP Servers

Model Context Protocol servers for external tool and API access.

### Common MCP Servers

| Server | Description | When to Use | Scope | Installation |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | PR management, issues, code | GitHub workflows | Project | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL queries, data access | Database operations | Project | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | Advanced file operations | Complex file tasks | User | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | Team communication | Notifications, updates | Project | Configure in settings |
| **Google Docs** | Document access | Doc editing, review | Project | Configure in settings |
| **Asana** | Project management | Task tracking | Project | Configure in settings |
| **Stripe** | Payment data | Financial analysis | Project | Configure in settings |
| **Memory** | Persistent memory | Cross-session recall | User | Configure in settings |
| **Context7** | Library documentation | Up-to-date docs lookup | Built-in | Built-in |

> **Scope**: `Project` = team (`.mcp.json`), `User` = personal (`~/.claude.json`), `Built-in` = pre-installed

### MCP Configuration Example

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Reference**: [05-mcp/](05-mcp/) | [MCP Protocol Docs](https://modelcontextprotocol.io)

**Quick Install (GitHub MCP)**:
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## Hooks

Event-driven automation that executes shell commands on Claude Code events.

### Hook Events

| Event | Description | When Triggered | Use Cases |
|-------|-------------|----------------|-----------|
| `SessionStart` | Session begins/resumes | Session initialization | Setup tasks |
| `InstructionsLoaded` | Instructions loaded | CLAUDE.md or rules file loaded | Custom instruction handling |
| `UserPromptSubmit` | Before prompt processing | User sends message | Input validation |
| `PreToolUse` | Before tool execution | Before any tool runs | Validation, logging |
| `PermissionRequest` | Permission dialog shown | Before sensitive actions | Custom approval flows |
| `PostToolUse` | After tool succeeds | After any tool completes | Formatting, notifications |
| `PostToolUseFailure` | Tool execution fails | After tool error | Error handling, logging |
| `Notification` | Notification sent | Claude sends notification | External alerts |
| `SubagentStart` | Subagent spawned | Subagent task starts | Initialize subagent context |
| `SubagentStop` | Subagent finishes | Subagent task complete | Chain actions |
| `Stop` | Claude finishes responding | Response complete | Cleanup, reporting |
| `StopFailure` | API error ends turn | API error occurs | Error recovery, logging |
| `TeammateIdle` | Teammate agent idle | Agent team coordination | Distribute work |
| `TaskCompleted` | Task marked complete | Task done | Post-task processing |
| `TaskCreated` | Task created via TaskCreate | New task created | Task tracking, logging |
| `ConfigChange` | Configuration updated | Settings modified | React to config changes |
| `CwdChanged` | Working directory changes | Directory changed | Directory-specific setup |
| `FileChanged` | Watched file changes | File modified | File monitoring, rebuild |
| `PreCompact` | Before compact operation | Context compression | State preservation |
| `PostCompact` | After compaction completes | Compaction done | Post-compact actions |
| `WorktreeCreate` | Worktree being created | Git worktree created | Setup worktree environment |
| `WorktreeRemove` | Worktree being removed | Git worktree removed | Cleanup worktree resources |
| `Elicitation` | MCP server requests input | MCP elicitation | Input validation |
| `ElicitationResult` | User responds to elicitation | User responds | Response processing |
| `SessionEnd` | Session terminates | Session termination | Cleanup, save state |

### Example Hooks

| Hook | Description | Event | Scope | Installation |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | Command validation | PreToolUse:Bash | Project | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | Security scanning | PostToolUse:Write | Project | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | Auto-formatting | PostToolUse:Write | User | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | Prompt validation | UserPromptSubmit | Project | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | Token usage tracking | Stop | User | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | Pre-commit validation | PreToolUse:Bash | Project | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | Command logging | PostToolUse:Bash | User | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |
| `dependency-check.sh` | Vulnerability scan on manifest changes | PostToolUse:Write | Project | `cp 06-hooks/dependency-check.sh .claude/hooks/` |

> **Scope**: `Project` = team (`.claude/settings.json`), `User` = personal (`~/.claude/settings.json`)

### Hook Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "~/.claude/hooks/validate-bash.py"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "~/.claude/hooks/format-code.sh"
      }
    ]
  }
}
```

**Reference**: [06-hooks/](06-hooks/) | [Official Docs](https://code.claude.com/docs/en/hooks)

**Quick Install (All Hooks)**:
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## Memory Files

Persistent context loaded automatically across sessions.

### Memory Types

| Type | Location | Scope | When to Use |
|------|----------|-------|-------------|
| **Managed Policy** | Org-managed policies | Organization | Enforce org-wide standards |
| **Project** | `./CLAUDE.md` | Project (team) | Team standards, project context |
| **Project Rules** | `.claude/rules/` | Project (team) | Modular project rules |
| **User** | `~/.claude/CLAUDE.md` | User (personal) | Personal preferences |
| **User Rules** | `~/.claude/rules/` | User (personal) | Modular personal rules |
| **Local** | `./CLAUDE.local.md` | Local (git-ignored) | Machine-specific local overrides (gitignored). Documented at https://code.claude.com/docs/en/memory as a supported per-developer override file. |
| **Auto Memory** | Automatic | Session | Auto-captured insights and corrections |

> **Scope**: `Organization` = managed by admins, `Project` = shared with team via git, `User` = personal preferences, `Local` = not committed, `Session` = auto-managed

**Reference**: [02-memory/](02-memory/) | [Official Docs](https://code.claude.com/docs/en/memory)

**Quick Install**:
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## New Features (May 2026)

| Feature | Description | How to Use |
|---------|-------------|------------|
| **/focus** | Toggle focus view for distraction-free output display (v2.1.110) | Run `/focus` to reduce visual noise during long tasks |
| **/proactive** | Alias for `/loop` — same recurring-task behavior (v2.1.105) | Use `/proactive` interchangeably with `/loop` |
| **/recap** | Show a session recap when returning to an existing session (v2.1.108) | Run `/recap` after being away to get context on what was done |
| **/tui** | Toggle fullscreen TUI (text user interface) mode for flicker-free rendering (v2.1.110) | Use `/tui` in fullscreen terminals or tmux |
| **/undo** | Alias for `/rewind` — reverts to the previous checkpoint (v2.1.108) | Use `/undo` interchangeably with `/rewind` |
| **Monitor Tool** | Watch a background command's stdout stream and react to events instead of polling (v2.1.98+) | Use the Monitor tool via [Advanced Features](09-advanced-features/) |
| **/team-onboarding** | Auto-generate a teammate ramp-up guide from the project's Claude Code setup (v2.1.101) | Run `/team-onboarding` in your project |
| **Ultraplan auto-create** | Cloud environment created automatically on first `/ultraplan` invocation — no manual setup required (v2.1.101) | Use `/ultraplan <prompt>` |
| **Remote Control** | Control Claude Code sessions remotely via API | Use the remote control API to send prompts and receive responses programmatically |
| **Web Sessions** | Run Claude Code in a browser-based environment | Access via `claude web` or through the Anthropic Console |
| **Desktop App** | Native desktop application for Claude Code | Use `/desktop` or download from Anthropic website |
| **Agent Teams** | Coordinate multiple agents working on related tasks | Configure teammate agents that collaborate and share context |
| **Task List** | Background task management and monitoring | Use `/tasks` to view and manage background operations |
| **Prompt Suggestions** | Context-aware command suggestions | Suggestions appear automatically based on current context |
| **Git Worktrees** | Isolated git worktrees for parallel development | Use worktree commands for safe parallel branch work |
| **Sandboxing** | Isolated execution environments for safety | Use `/sandbox` to toggle; runs commands in restricted environments |
| **MCP OAuth** | OAuth authentication for MCP servers | Configure OAuth credentials in MCP server settings for secure access |
| **MCP Tool Search** | Search and discover MCP tools dynamically | Use tool search to find available MCP tools across connected servers |
| **Scheduled Tasks** | Set up recurring tasks with `/loop` and cron tools | Use `/loop 5m /command` or CronCreate tool |
| **Chrome Integration** | Browser automation with headless Chromium | Use `--chrome` flag or `/chrome` command |
| **Keyboard Customization** | Customize keybindings including chord support | Use `/keybindings` or edit `~/.claude/keybindings.json` |
| **Auto Mode** | Fully autonomous operation without permission prompts (Research Preview) | Use `--mode auto` or `/permissions auto`; March 2026 |
| **Channels** | Multi-channel communication (Telegram, Slack, etc.) (Research Preview) | Configure channel plugins; March 2026 |
| **Voice Dictation** | Voice input for prompts | Use microphone icon or voice keybinding |
| **Agent Hook Type** | Hooks that spawn a subagent instead of running a shell command | Set `"type": "agent"` in hook configuration |
| **Prompt Hook Type** | Hooks that inject prompt text into the conversation | Set `"type": "prompt"` in hook configuration |
| **MCP Elicitation** | MCP servers can request user input during tool execution | Handle via `Elicitation` and `ElicitationResult` hook events |
| **Plugin LSP Support** | Language Server Protocol integration via plugins | Configure LSP servers in `plugin.json` for editor features |
| **Managed Drop-ins** | Organization-managed drop-in configurations (v2.1.83) | Admin-configured via managed policies; auto-applied to all users |

---

## Quick Reference Matrix

### Feature Selection Guide

| Need | Recommended Feature | Why |
|------|---------------------|-----|
| Quick shortcut | Slash Command | Manual, immediate |
| Persistent context | Memory | Auto-loaded |
| Complex automation | Skill | Auto-invoked |
| Specialized task | Subagent | Isolated context |
| External data | MCP Server | Real-time access |
| Event automation | Hook | Event-triggered |
| Complete solution | Plugin | All-in-one bundle |

### Installation Priority

| Priority | Feature | Command |
|----------|---------|---------|
| 1. Essential | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. Daily Use | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. Quality | Subagents | `cp 04-subagents/*.md .claude/agents/` |
| 4. Automation | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. External | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. Advanced | Skills | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. Complete | Plugins | `/plugin install pr-review` |

---

## Complete One-Command Installation

Install all examples from this repository:

```bash
# Create directories
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# Install all features
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## Additional Resources

- [Official Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Learning Roadmap](LEARNING-ROADMAP.md)
- [Main README](README.md)

---

**Last Updated**: May 9, 2026
**Claude Code Version**: 2.1.138
**Sources**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/hooks
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
