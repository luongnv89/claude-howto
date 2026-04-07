<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 示例 - 速查卡

## 🚀 安装速命令

### Slash Commands
```bash
# 安装全部
cp 01-slash-commands/*.md .claude/commands/

# 安装单个
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memory
```bash
# 项目 memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 个人 memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills
```bash
# 个人 skills
cp -r 03-skills/code-review ~/.claude/skills/

# 项目 skills
cp -r 03-skills/code-review .claude/skills/
```

### Subagents
```bash
# 安装全部
cp 04-subagents/*.md .claude/agents/

# 安装单个
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# 设置凭据
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 安装配置（项目级）
cp 05-mcp/github-mcp.json .mcp.json

# 或者用户级：添加到 ~/.claude.json
```

### Hooks
```bash
# 安装 hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 在 settings 中配置（~/.claude/settings.json）
```

### Plugins
```bash
# 从示例安装（如果已发布）
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints
```bash
# 每次用户提示后都会自动创建 checkpoint
# 回退：按两次 Esc 或使用：
/rewind

# 然后选择：恢复代码和对话、恢复对话、
# 恢复代码、从这里开始总结，或算了
```

### Advanced Features
```bash
# 在 settings 中配置（.claude/settings.json）
# 参见 09-advanced-features/config-examples.json

# planning mode
/plan 任务描述

# 权限模式（使用 --permission-mode 参数）
# default          - 风险操作需要审批
# acceptEdits      - 自动接受文件编辑，其他操作仍需审批
# plan             - 只读分析，不做修改
# dontAsk          - 除危险操作外全部接受
# auto             - 后台分类器自动决定权限
# bypassPermissions - 全部接受（需要 --dangerously-skip-permissions）

# 会话管理
/resume                # 恢复之前的对话
/rename "name"         # 命名当前会话
/fork                  # 分叉当前会话
claude -c              # 继续最近的对话
claude -r "session"    # 按名称/ID 恢复会话
```

---

## 📋 功能速览

| 功能 | 安装路径 | 用法 |
|------|----------|------|
| **Slash Commands（55+）** | `.claude/commands/*.md` | `/command-name` |
| **Memory** | `./CLAUDE.md` | 自动加载 |
| **Skills** | `.claude/skills/*/SKILL.md` | 自动触发 |
| **Subagents** | `.claude/agents/*.md` | 自动委派 |
| **MCP** | `.mcp.json`（项目）或 `~/.claude.json`（用户） | `/mcp__server__action` |
| **Hooks（25 个事件）** | `~/.claude/hooks/*.sh` | 事件触发（4 类） |
| **Plugins** | 通过 `/plugin install` | 打包所有能力 |
| **Checkpoints** | 内置 | `Esc+Esc` 或 `/rewind` |
| **Planning Mode** | 内置 | `/plan <task>` |
| **Permission Modes（6 种）** | 内置 | `--allowedTools`、`--permission-mode` |
| **Sessions** | 内置 | `/session <command>` |
| **Background Tasks** | 内置 | 在后台运行 |
| **Remote Control** | 内置 | WebSocket API |
| **Web Sessions** | 内置 | `claude web` |
| **Git Worktrees** | 内置 | `/worktree` |
| **Auto Memory** | 内置 | 自动保存到 `CLAUDE.md` |
| **Task List** | 内置 | `/task list` |
| **Bundled Skills（5 个）** | 内置 | `/simplify`、`/loop`、`/claude-api`、`/voice`、`/browse` |

---

## 🎯 常见使用场景

### 代码审查
```bash
# 方法 1：slash command
cp 01-slash-commands/optimize.md .claude/commands/
# 使用：/optimize

# 方法 2：subagent
cp 04-subagents/code-reviewer.md .claude/agents/
# 使用：自动委派

# 方法 3：skill
cp -r 03-skills/code-review ~/.claude/skills/
# 使用：自动触发

# 方法 4：插件（推荐）
/plugin install pr-review
# 使用：/review-pr
```

### 文档
```bash
# slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# 插件（完整方案）
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
# 项目 memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 按你的团队规范编辑
vim CLAUDE.md
```

### 自动化与 Hooks
```bash
# 安装 hooks（25 个事件，4 类：command、http、prompt、agent）
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 示例：
# - 提交前测试：pre-commit.sh
# - 自动格式化代码：format-code.sh
# - 安全扫描：security-scan.sh

# 用 Auto Mode 实现全自动工作流
claude --enable-auto-mode -p "重构并测试 auth 模块"
# 或者用 Shift+Tab 在模式间切换
```

### 安全重构
```bash
# 每次提示前都会自动创建 checkpoint
# 试着重构
# 如果成功：继续
# 如果失败：按 Esc+Esc 或使用 /rewind 返回
```

### 复杂实现
```bash
# 使用 planning mode
/plan 实现用户认证系统

# Claude 会创建详细计划
# 你可以审阅并批准
# Claude 会系统化地执行实现
```

### CI/CD 集成
```bash
# 以 headless 模式运行（非交互）
claude -p "运行所有测试并生成报告"

# 在 CI 中搭配权限模式
claude -p "运行测试" --permission-mode dontAsk

# 使用 Auto Mode 实现完全自治的 CI 任务
claude --enable-auto-mode -p "运行测试并修复失败项"

# 结合 hooks 做自动化
# 参见 09-advanced-features/README.md
```

### 学习与实验
```bash
# 用 plan mode 做安全分析
claude --permission-mode plan

# 安全实验 - checkpoint 会自动创建
# 如果需要回退：按 Esc+Esc 或使用 /rewind
```

### Agent 团队
```bash
# 启用 agent 团队
export CLAUDE_AGENT_TEAMS=1

# 或者在 settings.json 中
{ "agentTeams": { "enabled": true } }

# 用这句话开始："使用团队方式实现功能 X"
```

### 定时任务
```bash
# 每 5 分钟运行一次命令
/loop 5m /check-status

# 一次性提醒
/loop 30m "提醒我检查部署"
```

---

## 📁 文件位置参考

```text
Your Project/
├── .claude/
│   ├── commands/              # Slash commands 放这里
│   ├── agents/                # Subagents 放这里
│   ├── skills/                # 项目 skills 放这里
│   └── settings.json          # 项目设置（hooks 等）
├── .mcp.json                  # MCP 配置（项目级）
├── CLAUDE.md                  # 项目 memory
└── src/
    └── api/
        └── CLAUDE.md          # 目录级 memory

User Home/
├── .claude/
│   ├── commands/              # 个人命令
│   ├── agents/                # 个人 agents
│   ├── skills/                # 个人 skills
│   ├── hooks/                 # hook 脚本
│   ├── settings.json          # 用户设置
│   ├── managed-settings.d/    # 托管设置（企业/组织）
│   └── CLAUDE.md              # 个人 memory
└── .claude.json               # 个人 MCP 配置（用户级）
```

---

## 🔍 查找示例

### 按分类
- **Slash Commands**：`01-slash-commands/`
- **Memory**：`02-memory/`
- **Skills**：`03-skills/`
- **Subagents**：`04-subagents/`
- **MCP**：`05-mcp/`
- **Hooks**：`06-hooks/`
- **Plugins**：`07-plugins/`
- **Checkpoints**：`08-checkpoints/`
- **Advanced Features**：`09-advanced-features/`
- **CLI**：`10-cli/`

### 按使用场景
- **性能**：`01-slash-commands/optimize.md`
- **安全**：`04-subagents/secure-reviewer.md`
- **测试**：`04-subagents/test-engineer.md`
- **文档**：`03-skills/doc-generator/`
- **DevOps**：`07-plugins/devops-automation/`

### 按复杂度
- **简单**：Slash commands
- **中等**：Subagents、Memory
- **高级**：Skills、Hooks
- **完整**：Plugins

---

## 🎓 学习路径

### 第 1 天
```bash
# 阅读总览
cat README.md

# 安装一个命令
cp 01-slash-commands/optimize.md .claude/commands/

# 试用
/optimize
```

### 第 2-3 天
```bash
# 设置 memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# 安装 subagent
cp 04-subagents/code-reviewer.md .claude/agents/
```

### 第 4-5 天
```bash
# 设置 MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# 试用 MCP 命令
/mcp__github__list_prs
```

### 第 2 周
```bash
# 安装 skill
cp -r 03-skills/code-review ~/.claude/skills/

# 让它自动触发
# 直接说：“Review this code for issues”
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

## 🆕 新功能（2026 年 3 月）

| 功能 | 说明 | 用法 |
|------|------|------|
| **Auto Mode** | 通过后台分类器实现完全自治 | `--enable-auto-mode` 参数，`Shift+Tab` 切换模式 |
| **Channels** | Discord 和 Telegram 集成 | `--channels` 参数，Discord / Telegram bot |
| **Voice Dictation** | 对 Claude 说出命令和上下文 | `/voice` 命令 |
| **Hooks（25 个事件）** | 扩展后的 hook 系统，包含 4 类 | command、http、prompt、agent hook 类型 |
| **MCP Elicitation** | MCP server 可在运行时请求用户输入 | 当 server 需要澄清时自动提示 |
| **WebSocket MCP** | MCP 的 WebSocket 传输 | 在 `.mcp.json` 中配置 `ws://` URL |
| **Plugin LSP** | 插件支持 Language Server Protocol | `userConfig`、`${CLAUDE_PLUGIN_DATA}` 变量 |
| **Remote Control** | 通过 WebSocket API 控制 Claude Code | `claude --remote` 用于外部集成 |
| **Web Sessions** | 基于浏览器的 Claude Code 接口 | 使用 `claude web` 打开 |
| **Desktop App** | 原生桌面应用 | 从 claude.ai/download 下载 |
| **Task List** | 管理后台任务 | `/task list`、`/task status <id>` |
| **Auto Memory** | 从对话中自动保存记忆 | Claude 会自动保存关键上下文到 `CLAUDE.md` |
| **Git Worktrees** | 用于并行开发的隔离工作区 | 使用 `/worktree` 创建隔离空间 |
| **Model Selection** | 在 Sonnet 4.6 和 Opus 4.6 之间切换 | `/model` 或 `--model` 参数 |
| **Agent Teams** | 协调多个 agent 执行任务 | 通过环境变量 `CLAUDE_AGENT_TEAMS=1` 启用 |
| **Scheduled Tasks** | 使用 `/loop` 运行周期任务 | `/loop 5m /command` 或 CronCreate 工具 |
| **Chrome Integration** | 浏览器自动化 | `--chrome` 参数或 `/chrome` 命令 |
| **Keyboard Customization** | 自定义按键绑定 | `/keybindings` 命令 |

---

## 💡 小技巧

### 自定义
- 先原样使用示例
- 再按需求修改
- 分享给团队前先测试
- 对配置做版本控制

### 最佳实践
- 用 memory 保存团队规范
- 用 plugins 做完整工作流
- 用 subagents 处理复杂任务
- 用 slash commands 处理快速任务

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

| 需求 | 用这个 | 示例 |
|------|--------|------|
| 快速快捷操作 | Slash Command（55+） | `01-slash-commands/optimize.md` |
| 团队规范 | Memory | `02-memory/project-CLAUDE.md` |
| 自动化工作流 | Skill | `03-skills/code-review/` |
| 专门任务 | Subagent | `04-subagents/code-reviewer.md` |
| 外部数据 | MCP（+ Elicitation、WebSocket） | `05-mcp/github-mcp.json` |
| 事件自动化 | Hook（25 个事件、4 类） | `06-hooks/pre-commit.sh` |
| 完整方案 | Plugin（+ LSP 支持） | `07-plugins/pr-review/` |
| 安全实验 | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| 完全自治 | Auto Mode | `--enable-auto-mode` 或 `Shift+Tab` |
| 聊天集成 | Channels | `--channels`（Discord、Telegram） |
| CI/CD 流水线 | CLI | `10-cli/README.md` |

---

## 🔗 快速链接

- **主指南**：`README.md`
- **完整索引**：`INDEX.md`
- **速查卡**：`QUICK_REFERENCE.md`
- **原始指南**：`claude_concepts_guide.md`

---

## 📞 常见问题

**问：我应该先用哪个？**
答：先从 slash commands 开始，按需逐步添加功能。

**问：我可以混用多个功能吗？**
答：可以！它们可以一起工作。Memory + Commands + MCP 很强大。

**问：怎么分享给团队？**
答：把 `.claude/` 目录提交到 git。

**问：敏感信息怎么办？**
答：用环境变量，不要硬编码。

**问：我可以改这些示例吗？**
答：当然可以！它们本来就是可定制的模板。

---

## ✅ 检查清单

入门清单：

- [ ] 阅读 `README.md`
- [ ] 安装 1 个 slash command
- [ ] 试用该命令
- [ ] 创建项目 `CLAUDE.md`
- [ ] 安装 1 个 subagent
- [ ] 配置 1 个 MCP 集成
- [ ] 安装 1 个 skill
- [ ] 试用一个完整插件
- [ ] 按你的需求定制
- [ ] 与团队共享

---

**快速开始**：`cat README.md`

**完整索引**：`cat INDEX.md`

**这张卡片**：建议随手保留，方便快速查阅！
