<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 示例 - 快速参考卡（Quick Reference Card）

## 🚀 安装速查命令

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

## 📋 功能速查表

| 功能 | 安装位置 | 用法 |
|---------|-------------|-------|
| **Slash Commands (55+)** | `.claude/commands/*.md` | `/command-name` |
| **Memory** | `./CLAUDE.md` | 自动加载 |
| **Skills** | `.claude/skills/*/SKILL.md` | 自动触发 |
| **Subagents** | `.claude/agents/*.md` | 自动委派 |
| **MCP** | `.mcp.json` (project) or `~/.claude.json` (user) | `/mcp__server__action` |
| **Hooks (25 events)** | `~/.claude/hooks/*.sh` | 事件触发（4 types） |
| **Plugins** | 通过 `/plugin install` | 打包全部能力 |
| **Checkpoints** | 内置 | `Esc+Esc` or `/rewind` |
| **Planning Mode** | 内置 | `/plan <task>` |
| **Permission Modes (6)** | 内置 | `--allowedTools`, `--permission-mode` |
| **Sessions** | 内置 | `/session <command>` |
| **Background Tasks** | 内置 | Run in background |
| **Remote Control** | 内置 | WebSocket API |
| **Web Sessions** | 内置 | `claude web` |
| **Git Worktrees** | 内置 | `/worktree` |
| **Auto Memory** | 内置 | 自动保存到 CLAUDE.md |
| **Task List** | 内置 | `/task list` |
| **Bundled Skills (5)** | 内置 | `/simplify`, `/loop`, `/claude-api`, `/voice`, `/browse` |

---

## 🎯 常见场景

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
# Install hooks (25 events, 4 types: command, http, prompt, agent)
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

## 📁 文件位置参考

```text
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

## 🔍 快速查找示例

### 按类别
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

### 按场景
- **Performance**: `01-slash-commands/optimize.md`
- **Security**: `04-subagents/secure-reviewer.md`
- **Testing**: `04-subagents/test-engineer.md`
- **Docs**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### 按复杂度
- **Simple**: Slash commands
- **Medium**: Subagents, Memory
- **Advanced**: Skills, Hooks
- **Complete**: Plugins

---

## 🎓 学习路径

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

## New Features（March 2026）

| Feature | Description | Usage |
|---------|-------------|-------|
| **Auto Mode** | 背景分类器支持的全自治模式 | `--enable-auto-mode`，或 `Shift+Tab` 循环切换 |
| **Channels** | Discord 与 Telegram 集成 | `--channels`，Discord/Telegram bots |
| **Voice Dictation** | 语音输入命令与上下文 | `/voice` |
| **Hooks (25 events)** | 扩展 Hook 系统（4 types） | command, http, prompt, agent hook types |
| **MCP Elicitation** | MCP 运行时请求用户输入 | 服务端需要澄清时自动触发 |
| **WebSocket MCP** | MCP 的 WebSocket 传输 | 在 `.mcp.json` 使用 `ws://` |
| **Plugin LSP** | 插件支持 Language Server Protocol | `userConfig`、`${CLAUDE_PLUGIN_DATA}` |
| **Remote Control** | 通过 WebSocket API 控制 Claude Code | `claude --remote` |
| **Web Sessions** | 浏览器版 Claude Code | `claude web` |
| **Desktop App** | 原生桌面应用 | 从 claude.ai/download 下载 |
| **Task List** | 管理后台任务 | `/task list`, `/task status <id>` |
| **Auto Memory** | 从对话自动沉淀 memory | Claude 自动写入 CLAUDE.md |
| **Git Worktrees** | 并行开发隔离工作区 | `/worktree` |
| **Model Selection** | 在 Sonnet 4.6 与 Opus 4.6 间切换 | `/model` 或 `--model` |
| **Agent Teams** | 多 agents 协同 | `CLAUDE_AGENT_TEAMS=1` |
| **Scheduled Tasks** | `/loop` 周期任务 | `/loop 5m /command` 或 CronCreate |
| **Chrome Integration** | 浏览器自动化 | `--chrome` 或 `/chrome` |
| **Keyboard Customization** | 自定义快捷键 | `/keybindings` |

---

## Tips & Tricks

### 定制建议
- 先按示例原样跑通
- 再按业务场景逐步改造
- 团队共享前先本地验证
- 配置纳入版本控制

### 最佳实践
- 用 memory 固化团队标准
- 用 plugins 承载完整流程
- 用 subagents 处理复杂任务
- 用 slash commands 处理高频快操作

### 故障排查
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

## 📊 功能矩阵

| Need | Use This | Example |
|------|----------|---------|
| Quick shortcut | Slash Command (55+) | `01-slash-commands/optimize.md` |
| Team standards | Memory | `02-memory/project-CLAUDE.md` |
| Auto workflow | Skill | `03-skills/code-review/` |
| Specialized task | Subagent | `04-subagents/code-reviewer.md` |
| External data | MCP (+ Elicitation, WebSocket) | `05-mcp/github-mcp.json` |
| Event automation | Hook (25 events, 4 types) | `06-hooks/pre-commit.sh` |
| Complete solution | Plugin (+ LSP support) | `07-plugins/pr-review/` |
| Safe experiment | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| Fully autonomous | Auto Mode | `--enable-auto-mode` or `Shift+Tab` |
| Chat integrations | Channels | `--channels` (Discord, Telegram) |
| CI/CD pipeline | CLI | `10-cli/README.md` |

---

## 🔗 快速链接

- **Main Guide**: `README.md`
- **Complete Index**: `INDEX.md`
- **Summary**: `EXAMPLES_SUMMARY.md`
- **Original Guide**: `claude_concepts_guide.md`

---

## 📞 常见问题

**Q: 我应该先用哪一种？**  
A: 从 slash commands 开始，按需叠加能力。

**Q: 能混用这些能力吗？**  
A: 可以。它们是为组合而设计的。Memory + Commands + MCP 会非常强。

**Q: 如何给团队共享？**  
A: 将 `.claude/` 目录纳入 git。

**Q: 凭据怎么处理？**  
A: 使用环境变量，不要硬编码。

**Q: 示例可以改吗？**  
A: 完全可以。它们本来就是可定制模板。

---

## ✅ 清单

入门清单：

- [ ] 阅读 `README.md`
- [ ] 安装 1 个 slash command
- [ ] 跑通该命令
- [ ] 创建项目 `CLAUDE.md`
- [ ] 安装 1 个 subagent
- [ ] 配置 1 个 MCP 集成
- [ ] 安装 1 个 skill
- [ ] 体验 1 个完整 plugin
- [ ] 按需定制
- [ ] 与团队共享

---

**Quick Start**: `cat README.md`

**Full Index**: `cat INDEX.md`

**This Card**: 建议常驻收藏，便于随时查阅。
