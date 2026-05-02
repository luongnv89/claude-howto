<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code Examples - Quick Reference Card

## 🚀 Installation Quick Commands

### Slash Commands
```bash
# Install all
cp 01-slash-commands/*.md .claude/commands/

# Install specific
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memory
```bash
# Project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Personal memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills
```bash
# Personal skills
cp -r 03-skills/code-review ~/.claude/skills/

# Project skills
cp -r 03-skills/code-review .claude/skills/
```

### Subagents
```bash
# Install all
cp 04-subagents/*.md .claude/agents/

# Install specific
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# Set credentials
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Install config (project scope)
cp 05-mcp/github-mcp.json .mcp.json

# Or user scope: add to ~/.claude.json
```

### Hooks
```bash
# Install hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Configure in settings (~/.claude/settings.json)
```

### Plugins
```bash
# Install from examples (if published)
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints
```bash
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind

# Then choose: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, or Never mind
```

### Advanced Features
```bash
# Configure in settings (.claude/settings.json)
# See 09-advanced-features/config-examples.json

# Planning mode
/plan Task description

# Permission modes (use --permission-mode flag)
# default        - Ask for approval on risky actions
# acceptEdits    - Auto-accept file edits, ask for others
# plan           - Read-only analysis, no modifications
# dontAsk        - Accept all actions except risky ones
# auto           - Background classifier decides permissions automatically
# bypassPermissions - Accept all actions (requires --dangerously-skip-permissions)

# Session management
/resume                # Resume a previous conversation
/rename "name"         # Name the current session
/fork                  # Fork the current session
claude -c              # Continue most recent conversation
claude -r "session"    # Resume session by name/ID
```

---

## 📋 Feature Cheat Sheet

| Feature | Install Path | Usage |
|---------|-------------|-------|
| **Slash Commands (55+)** | `.claude/commands/*.md` | `/command-name` |
| **Memory** | `./CLAUDE.md` | Auto-loaded |
| **Skills** | `.claude/skills/*/SKILL.md` | Auto-invoked |
| **Subagents** | `.claude/agents/*.md` | Auto-delegated |
| **MCP** | `.mcp.json` (project) or `~/.claude.json` (user) | `/mcp__server__action` |
| **Hooks (28 events)** | `~/.claude/hooks/*.sh` | Event-triggered (5 types) |
| **Plugins** | Via `/plugin install` | Bundles all |
| **Checkpoints** | Built-in | `Esc+Esc` or `/rewind` |
| **Planning Mode** | Built-in | `/plan <task>` |
| **Permission Modes (6)** | Built-in | `--allowedTools`, `--permission-mode` |
| **Sessions** | Built-in | `/session <command>` |
| **Background Tasks** | Built-in | Run in background |
| **Remote Control** | Built-in | WebSocket API |
| **Web Sessions** | Built-in | `claude web` |
| **Git Worktrees** | Built-in | `/worktree` |
| **Auto Memory** | Built-in | Auto-saves to CLAUDE.md |
| **Task List** | Built-in | `/task list` |
| **Bundled Skills (5)** | Built-in | `/simplify`, `/loop`, `/claude-api`, `/voice`, `/browse` |

---

## 🎯 Common Use Cases

### Code Review
```bash
# Method 1: Slash command
cp 01-slash-commands/optimize.md .claude/commands/
# Use: /optimize

# Method 2: Subagent
cp 04-subagents/code-reviewer.md .claude/agents/
# Use: Auto-delegated

# Method 3: Skill
cp -r 03-skills/code-review ~/.claude/skills/
# Use: Auto-invoked

# Method 4: Plugin (best)
/plugin install pr-review
# Use: /review-pr
```

### Documentation
```bash
# Slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Plugin (complete solution)
/plugin install documentation
```

### DevOps
```bash
# Complete plugin
/plugin install devops-automation

# Commands: /deploy, /rollback, /status, /incident
```

### Team Standards
```bash
# Project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Edit for your team
vim CLAUDE.md
```

### Automation & Hooks
```bash
# Install hooks (28 events, 5 types: command, http, mcp_tool, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Examples:
# - Pre-commit tests: pre-commit.sh
# - Auto-format code: format-code.sh
# - Security scanning: security-scan.sh

# Auto Mode for fully autonomous workflows
claude --enable-auto-mode -p "Refactor and test the auth module"
# Or cycle modes interactively with Shift+Tab
```

### Safe Refactoring
```bash
# Checkpoints are created automatically before each prompt
# Try refactoring
# If it works: continue
# If it fails: press Esc+Esc or use /rewind to go back
```

### Complex Implementation
```bash
# Use planning mode
/plan Implement user authentication system

# Claude creates detailed plan
# Review and approve
# Claude implements systematically
```

### CI/CD Integration
```bash
# Run in headless mode (non-interactive)
claude -p "Run all tests and generate report"

# With permission mode for CI
claude -p "Run tests" --permission-mode dontAsk

# With Auto Mode for fully autonomous CI tasks
claude --enable-auto-mode -p "Run tests and fix failures"

# With hooks for automation
# See 09-advanced-features/README.md
```

### Learning & Experimentation
```bash
# Use plan mode for safe analysis
claude --permission-mode plan

# Experiment safely - checkpoints are created automatically
# If you need to rewind: press Esc+Esc or use /rewind
```

### Agent Teams
```bash
# Enable agent teams
export CLAUDE_AGENT_TEAMS=1

# Or in settings.json
{ "agentTeams": { "enabled": true } }

# Start with: "Implement feature X using a team approach"
```

### Scheduled Tasks
```bash
# Run a command every 5 minutes
/loop 5m /check-status

# One-time reminder
/loop 30m "remind me to check the deploy"
```

---

## 📁 File Locations Reference

```
Your Project/
├── .claude/
│   ├── commands/              # Slash commands go here
│   ├── agents/                # Subagents go here
│   ├── skills/                # Project skills go here
│   └── settings.json          # Project settings (hooks, etc.)
├── .mcp.json                  # MCP configuration (project scope)
├── CLAUDE.md                  # Project memory
└── src/
    └── api/
        └── CLAUDE.md          # Directory-specific memory

User Home/
├── .claude/
│   ├── commands/              # Personal commands
│   ├── agents/                # Personal agents
│   ├── skills/                # Personal skills
│   ├── hooks/                 # Hook scripts
│   ├── settings.json          # User settings
│   ├── managed-settings.d/    # Managed settings (enterprise/org)
│   └── CLAUDE.md              # Personal memory
└── .claude.json               # Personal MCP config (user scope)
```

---

## 🔍 Finding Examples

### By Category
- **Slash Commands**: `01-slash-commands/`
- **Memory**: `02-memory/`
- **Skills**: `03-skills/`
- **Subagents**: `04-subagents/`
- **MCP**: `05-mcp/`
- **Hooks**: `06-hooks/`
- **Plugins**: `07-plugins/`
- **Checkpoints**: `08-checkpoints/`
- **Advanced Features**: `09-advanced-features/`
- **CLI**: `10-cli/`

### By Use Case
- **Performance**: `01-slash-commands/optimize.md`
- **Security**: `04-subagents/secure-reviewer.md`
- **Testing**: `04-subagents/test-engineer.md`
- **Docs**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### By Complexity
- **Simple**: Slash commands
- **Medium**: Subagents, Memory
- **Advanced**: Skills, Hooks
- **Complete**: Plugins

---

## 🎓 Learning Path

### Day 1
```bash
# Read overview
cat README.md

# Install a command
cp 01-slash-commands/optimize.md .claude/commands/

# Try it
/optimize
```

### Day 2-3
```bash
# Set up memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# Install subagent
cp 04-subagents/code-reviewer.md .claude/agents/
```

### Day 4-5
```bash
# Set up MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# Try MCP commands
/mcp__github__list_prs
```

### Week 2
```bash
# Install skill
cp -r 03-skills/code-review ~/.claude/skills/

# Let it auto-invoke
# Just say: "Review this code for issues"
```

### Week 3+
```bash
# Install complete plugin
/plugin install pr-review

# Use bundled features
/review-pr
/check-security
/check-tests
```

---

## New Features (March 2026)

| Feature | Description | Usage |
|---------|-------------|-------|
| **Auto Mode** | Fully autonomous operation with background classifier | `--enable-auto-mode` flag, `Shift+Tab` to cycle modes |
| **Channels** | Discord and Telegram integration | `--channels` flag, Discord/Telegram bots |
| **Voice Dictation** | Speak commands and context to Claude | `/voice` command |
| **Hooks (28 events)** | Expanded hook system with 5 types | command, http, mcp_tool, prompt, agent hook types |
| **MCP Elicitation** | MCP servers can request user input at runtime | Auto-prompted when server needs clarification |
| **Plugin LSP** | Language Server Protocol support for plugins | `userConfig`, `${CLAUDE_PLUGIN_DATA}` variable |
| **Remote Control** | Control Claude Code via WebSocket API | `claude --remote` for external integrations |
| **Web Sessions** | Browser-based Claude Code interface | `claude web` to launch |
| **Desktop App** | Native desktop application | Download from claude.ai/download |
| **Task List** | Manage background tasks | `/task list`, `/task status <id>` |
| **Auto Memory** | Automatic memory saving from conversations | Claude auto-saves key context to CLAUDE.md |
| **Git Worktrees** | Isolated workspaces for parallel development | `/worktree` to create isolated workspace |
| **Model Selection** | Switch between Sonnet 4.6, Opus 4.7, and Haiku 4.5 | `/model` or `--model` flag |
| **Agent Teams** | Coordinate multiple agents on tasks | Enable with `CLAUDE_AGENT_TEAMS=1` env var |
| **Scheduled Tasks** | Recurring tasks with `/loop` | `/loop 5m /command` or CronCreate tool |
| **Chrome Integration** | Browser automation | `--chrome` flag or `/chrome` command |
| **Keyboard Customization** | Custom keybindings | `/keybindings` command |

---

## Tips & Tricks

### Customization
- Start with examples as-is
- Modify to fit your needs
- Test before sharing with team
- Version control your configurations

### Best Practices
- Use memory for team standards
- Use plugins for complete workflows
- Use subagents for complex tasks
- Use slash commands for quick tasks

### Troubleshooting
```bash
# Check file locations
ls -la .claude/commands/
ls -la .claude/agents/

# Verify YAML syntax
head -20 .claude/agents/code-reviewer.md

# Test MCP connection
echo $GITHUB_TOKEN
```

---

## 📊 Feature Matrix

| Need | Use This | Example |
|------|----------|---------|
| Quick shortcut | Slash Command (55+) | `01-slash-commands/optimize.md` |
| Team standards | Memory | `02-memory/project-CLAUDE.md` |
| Auto workflow | Skill | `03-skills/code-review/` |
| Specialized task | Subagent | `04-subagents/code-reviewer.md` |
| External data | MCP (+ Elicitation) | `05-mcp/github-mcp.json` |
| Event automation | Hook (28 events, 5 types) | `06-hooks/pre-commit.sh` |
| Complete solution | Plugin (+ LSP support) | `07-plugins/pr-review/` |
| Safe experiment | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| Fully autonomous | Auto Mode | `--enable-auto-mode` or `Shift+Tab` |
| Chat integrations | Channels | `--channels` (Discord, Telegram) |
| CI/CD pipeline | CLI | `10-cli/README.md` |

---

## 🔗 Quick Links

- **Main Guide**: `README.md`
- **Complete Index**: `INDEX.md`
- **Summary**: `EXAMPLES_SUMMARY.md`
- **Original Guide**: `claude_concepts_guide.md`

---

## 📞 Common Questions

**Q: Which should I use?**
A: Start with slash commands, add features as needed.

**Q: Can I mix features?**
A: Yes! They work together. Memory + Commands + MCP = powerful.

**Q: How do I share with team?**
A: Commit `.claude/` directory to git.

**Q: What about secrets?**
A: Use environment variables, never hardcode.

**Q: Can I modify examples?**
A: Absolutely! They're templates to customize.

---

## ✅ Checklist

Getting started checklist:

- [ ] Read `README.md`
- [ ] Install 1 slash command
- [ ] Try the command
- [ ] Create project `CLAUDE.md`
- [ ] Install 1 subagent
- [ ] Set up 1 MCP integration
- [ ] Install 1 skill
- [ ] Try a complete plugin
- [ ] Customize for your needs
- [ ] Share with team

---

**Quick Start**: `cat README.md`

**Full Index**: `cat INDEX.md`

**This Card**: Keep it handy for quick reference!

---
**Last Updated**: May 2, 2026
**Claude Code Version**: 2.1.126
**Sources**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/commands
- https://github.com/anthropics/claude-code/releases/tag/v2.1.126
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
