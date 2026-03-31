<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 示例 - 快速参考卡

## 🚀 安装快捷命令

### Slash Commands（斜杠命令）
```bash
# 安装全部
cp 01-slash-commands/*.md .claude/commands/

# 安装指定命令
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memory（记忆）
```bash
# 项目记忆
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 个人记忆
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills（技能）
```bash
# 个人技能
cp -r 03-skills/code-review ~/.claude/skills/

# 项目技能
cp -r 03-skills/code-review .claude/skills/
```

### Subagents（子智能体）
```bash
# 安装全部
cp 04-subagents/*.md .claude/agents/

# 安装指定
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# 设置凭据
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 安装配置（项目范围）
cp 05-mcp/github-mcp.json .mcp.json

# 或用户范围：添加到 ~/.claude.json
```

### Hooks（钩子）
```bash
# 安装 hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 在设置文件中配置 (~/.claude/settings.json)
```

### Plugins（插件）
```bash
# 从示例安装（如已发布）
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints（检查点）
```bash
# 每次用户提示时会自动创建检查点
# 如需回退，按两次 Esc 或使用：
/rewind

# 然后选择：恢复代码和对话、恢复对话、
# 恢复代码、从此处摘要，或取消
```

### Advanced Features（高级功能）
```bash
# 在设置文件中配置 (.claude/settings.json)
# 参见 09-advanced-features/config-examples.json

# 规划模式
/plan Task description

# 权限模式（使用 --permission-mode 标志）
# default        - 对风险操作请求确认
# acceptEdits    - 自动接受文件编辑，其他操作仍需确认
# plan           - 只读分析，不做任何修改
# dontAsk        - 接受所有操作，除高危操作外
# auto           - 后台分类器自动决定权限
# bypassPermissions - 接受所有操作（需要 --dangerously-skip-permissions）

# 会话管理
/resume                # 恢复上一次对话
/rename "name"         # 为当前会话命名
/fork                  # 分叉当前会话
claude -c              # 继续最近的对话
claude -r "session"    # 按名称/ID 恢复会话
```

---

## 📋 功能速查表

| 功能 | 安装路径 | 使用方式 |
|---------|-------------|-------|
| **Slash Commands（55+）** | `.claude/commands/*.md` | `/command-name` |
| **Memory（记忆）** | `./CLAUDE.md` | 自动加载 |
| **Skills（技能）** | `.claude/skills/*/SKILL.md` | 自动调用 |
| **Subagents（子智能体）** | `.claude/agents/*.md` | 自动委派 |
| **MCP** | `.mcp.json`（项目）或 `~/.claude.json`（用户） | `/mcp__server__action` |
| **Hooks（25 个事件）** | `~/.claude/hooks/*.sh` | 事件触发（4 种类型） |
| **Plugins（插件）** | 通过 `/plugin install` | 打包所有功能 |
| **Checkpoints（检查点）** | 内置 | `Esc+Esc` 或 `/rewind` |
| **Planning Mode（规划模式）** | 内置 | `/plan <task>` |
| **Permission Modes（6 种）** | 内置 | `--allowedTools`、`--permission-mode` |
| **Sessions（会话）** | 内置 | `/session <command>` |
| **Background Tasks（后台任务）** | 内置 | 在后台运行 |
| **Remote Control（远程控制）** | 内置 | WebSocket API |
| **Web Sessions（网页会话）** | 内置 | `claude web` |
| **Git Worktrees** | 内置 | `/worktree` |
| **Auto Memory（自动记忆）** | 内置 | 自动保存到 CLAUDE.md |
| **Task List（任务列表）** | 内置 | `/task list` |
| **Bundled Skills（5 个内置技能）** | 内置 | `/simplify`、`/loop`、`/claude-api`、`/voice`、`/browse` |

---

## 🎯 常见使用场景

### 代码审查
```bash
# 方式一：Slash command
cp 01-slash-commands/optimize.md .claude/commands/
# 使用：/optimize

# 方式二：Subagent
cp 04-subagents/code-reviewer.md .claude/agents/
# 使用：自动委派

# 方式三：Skill
cp -r 03-skills/code-review ~/.claude/skills/
# 使用：自动调用

# 方式四：Plugin（推荐）
/plugin install pr-review
# 使用：/review-pr
```

### 文档生成
```bash
# Slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Plugin（完整方案）
/plugin install documentation
```

### DevOps
```bash
# 完整插件
/plugin install devops-automation

# 命令：/deploy、/rollback、/status、/incident
```

### 团队规范
```bash
# 项目记忆
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 按团队需求编辑
vim CLAUDE.md
```

### 自动化与 Hooks
```bash
# 安装 hooks（25 个事件，4 种类型：command、http、prompt、agent）
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 示例：
# - 提交前测试：pre-commit.sh
# - 自动格式化代码：format-code.sh
# - 安全扫描：security-scan.sh

# 使用 Auto Mode 实现全自动工作流
claude --enable-auto-mode -p "Refactor and test the auth module"
# 或通过 Shift+Tab 交互切换模式
```

### 安全重构
```bash
# 每次提示前会自动创建检查点
# 尝试重构
# 成功：继续
# 失败：按 Esc+Esc 或使用 /rewind 回退
```

### 复杂实现
```bash
# 使用规划模式
/plan Implement user authentication system

# Claude 创建详细计划
# 审阅并批准
# Claude 系统性地执行实现
```

### CI/CD 集成
```bash
# 以无头模式运行（非交互式）
claude -p "Run all tests and generate report"

# 为 CI 使用权限模式
claude -p "Run tests" --permission-mode dontAsk

# 使用 Auto Mode 实现完全自主的 CI 任务
claude --enable-auto-mode -p "Run tests and fix failures"

# 结合 hooks 实现自动化
# 参见 09-advanced-features/README.md
```

### 学习与实验
```bash
# 使用 plan 模式进行安全分析
claude --permission-mode plan

# 安全实验——检查点会自动创建
# 如需回退：按 Esc+Esc 或使用 /rewind
```

### 智能体团队
```bash
# 启用智能体团队
export CLAUDE_AGENT_TEAMS=1

# 或在 settings.json 中配置
{ "agentTeams": { "enabled": true } }

# 启动方式："Implement feature X using a team approach"
```

### 定时任务
```bash
# 每 5 分钟运行一次命令
/loop 5m /check-status

# 一次性提醒
/loop 30m "remind me to check the deploy"
```

---

## 📁 文件位置参考

```
你的项目/
├── .claude/
│   ├── commands/              # 斜杠命令存放位置
│   ├── agents/                # 子智能体存放位置
│   ├── skills/                # 项目技能存放位置
│   └── settings.json          # 项目设置（hooks 等）
├── .mcp.json                  # MCP 配置（项目范围）
├── CLAUDE.md                  # 项目记忆
└── src/
    └── api/
        └── CLAUDE.md          # 目录级记忆

用户主目录/
├── .claude/
│   ├── commands/              # 个人命令
│   ├── agents/                # 个人智能体
│   ├── skills/                # 个人技能
│   ├── hooks/                 # Hook 脚本
│   ├── settings.json          # 用户设置
│   ├── managed-settings.d/    # 托管设置（企业/组织）
│   └── CLAUDE.md              # 个人记忆
└── .claude.json               # 个人 MCP 配置（用户范围）
```

---

## 🔍 查找示例

### 按类别
- **Slash Commands**：`01-slash-commands/`
- **Memory**：`02-memory/`
- **Skills**：`03-skills/`
- **Subagents**：`04-subagents/`
- **MCP**：`05-mcp/`
- **Hooks**：`06-hooks/`
- **Plugins**：`07-plugins/`
- **Checkpoints**：`08-checkpoints/`
- **高级功能**：`09-advanced-features/`
- **CLI**：`10-cli/`

### 按使用场景
- **性能优化**：`01-slash-commands/optimize.md`
- **安全审查**：`04-subagents/secure-reviewer.md`
- **测试**：`04-subagents/test-engineer.md`
- **文档**：`03-skills/doc-generator/`
- **DevOps**：`07-plugins/devops-automation/`

### 按复杂度
- **简单**：Slash commands
- **中等**：Subagents、Memory
- **进阶**：Skills、Hooks
- **完整方案**：Plugins

---

## 🎓 学习路径

### 第 1 天
```bash
# 阅读概览
cat README.md

# 安装一个命令
cp 01-slash-commands/optimize.md .claude/commands/

# 试用
/optimize
```

### 第 2-3 天
```bash
# 设置记忆
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# 安装子智能体
cp 04-subagents/code-reviewer.md .claude/agents/
```

### 第 4-5 天
```bash
# 配置 MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# 试用 MCP 命令
/mcp__github__list_prs
```

### 第 2 周
```bash
# 安装技能
cp -r 03-skills/code-review ~/.claude/skills/

# 让其自动调用
# 只需说："Review this code for issues"
```

### 第 3 周及以后
```bash
# 安装完整插件
/plugin install pr-review

# 使用打包功能
/review-pr
/check-security
/check-tests
```

---

## 新特性（2026 年 3 月）

| 功能 | 说明 | 使用方式 |
|---------|-------------|-------|
| **Auto Mode（自动模式）** | 后台分类器驱动的完全自主操作 | `--enable-auto-mode` 标志，`Shift+Tab` 切换模式 |
| **Channels（频道）** | Discord 和 Telegram 集成 | `--channels` 标志，Discord/Telegram 机器人 |
| **Voice Dictation（语音听写）** | 通过语音向 Claude 发送命令和上下文 | `/voice` 命令 |
| **Hooks（25 个事件）** | 扩展的 hook 系统，支持 4 种类型 | command、http、prompt、agent 钩子类型 |
| **MCP Elicitation** | MCP 服务器可在运行时请求用户输入 | 服务器需要澄清时自动提示 |
| **WebSocket MCP** | 用于 MCP 连接的 WebSocket 传输 | 在 `.mcp.json` 中使用 `ws://` URL 配置 |
| **Plugin LSP** | 插件的语言服务器协议支持 | `userConfig`、`${CLAUDE_PLUGIN_DATA}` 变量 |
| **Remote Control（远程控制）** | 通过 WebSocket API 控制 Claude Code | `claude --remote` 用于外部集成 |
| **Web Sessions（网页会话）** | 基于浏览器的 Claude Code 界面 | `claude web` 启动 |
| **Desktop App（桌面应用）** | 原生桌面应用程序 | 从 claude.ai/download 下载 |
| **Task List（任务列表）** | 管理后台任务 | `/task list`、`/task status <id>` |
| **Auto Memory（自动记忆）** | 从对话中自动保存记忆 | Claude 自动将关键上下文保存到 CLAUDE.md |
| **Git Worktrees** | 用于并行开发的隔离工作区 | `/worktree` 创建隔离工作区 |
| **Model Selection（模型选择）** | 在 Sonnet 4.6 和 Opus 4.6 之间切换 | `/model` 或 `--model` 标志 |
| **Agent Teams（智能体团队）** | 协调多个智能体共同完成任务 | 通过 `CLAUDE_AGENT_TEAMS=1` 环境变量启用 |
| **Scheduled Tasks（定时任务）** | 使用 `/loop` 实现周期性任务 | `/loop 5m /command` 或 CronCreate 工具 |
| **Chrome Integration（Chrome 集成）** | 浏览器自动化 | `--chrome` 标志或 `/chrome` 命令 |
| **Keyboard Customization（键盘自定义）** | 自定义快捷键 | `/keybindings` 命令 |

---

## 技巧与窍门

### 自定义
- 直接从示例开始使用
- 按需修改以适配你的项目
- 共享给团队前先测试
- 对配置文件进行版本控制

### 最佳实践
- 用 memory 管理团队规范
- 用 plugins 构建完整工作流
- 用 subagents 处理复杂任务
- 用 slash commands 完成快速操作

### 故障排查
```bash
# 检查文件位置
ls -la .claude/commands/
ls -la .claude/agents/

# 验证 YAML 语法
head -20 .claude/agents/code-reviewer.md

# 测试 MCP 连接
echo $GITHUB_TOKEN
```

---

## 📊 功能矩阵

| 需求 | 使用此功能 | 示例 |
|------|----------|---------|
| 快捷操作 | Slash Command（55+） | `01-slash-commands/optimize.md` |
| 团队规范 | Memory | `02-memory/project-CLAUDE.md` |
| 自动工作流 | Skill | `03-skills/code-review/` |
| 专项任务 | Subagent | `04-subagents/code-reviewer.md` |
| 外部数据 | MCP（+ Elicitation、WebSocket） | `05-mcp/github-mcp.json` |
| 事件自动化 | Hook（25 个事件，4 种类型） | `06-hooks/pre-commit.sh` |
| 完整方案 | Plugin（+ LSP 支持） | `07-plugins/pr-review/` |
| 安全实验 | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| 完全自主 | Auto Mode | `--enable-auto-mode` 或 `Shift+Tab` |
| 聊天集成 | Channels | `--channels`（Discord、Telegram） |
| CI/CD 流水线 | CLI | `10-cli/README.md` |

---

## 🔗 快速链接

- **主指南**：`README.md`
- **完整索引**：`INDEX.md`
- **摘要**：`EXAMPLES_SUMMARY.md`
- **原始指南**：`claude_concepts_guide.md`

---

## 📞 常见问题

**Q：我该用哪个功能？**
A：从 slash commands 开始，按需逐步添加功能。

**Q：可以混合使用多个功能吗？**
A：可以！它们可以协同工作。Memory + Commands + MCP = 强大组合。

**Q：如何与团队共享？**
A：将 `.claude/` 目录提交到 git 即可。

**Q：如何处理敏感信息？**
A：使用环境变量，切勿硬编码。

**Q：可以修改示例吗？**
A：当然！这些都是可自定义的模板。

---

## ✅ 检查清单

入门检查清单：

- [ ] 阅读 `README.md`
- [ ] 安装 1 个 slash command
- [ ] 试用该命令
- [ ] 创建项目 `CLAUDE.md`
- [ ] 安装 1 个 subagent
- [ ] 配置 1 个 MCP 集成
- [ ] 安装 1 个 skill
- [ ] 试用一个完整的 plugin
- [ ] 按需自定义
- [ ] 与团队共享

---

**快速开始**：`cat README.md`

**完整索引**：`cat INDEX.md`

**本卡片**：随时备查，快速参考！
