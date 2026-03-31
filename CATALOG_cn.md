<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 功能目录

> Claude Code 所有功能快速参考指南：命令、智能体、技能、插件和钩子。

**导航**：[命令](#slash-commands) | [权限模式](#permission-modes) | [子智能体](#subagents) | [技能](#skills) | [插件](#plugins) | [MCP 服务器](#mcp-servers) | [钩子](#hooks) | [记忆文件](#memory-files) | [新功能](#new-features-march-2026)

---

## 概览

| 功能 | 内置数量 | 示例数量 | 合计 | 参考目录 |
|---------|----------|----------|-------|-----------|
| **Slash Commands** | 55+ | 8 | 63+ | [01-slash-commands/](01-slash-commands/) |
| **子智能体（Subagents）** | 6 | 10 | 16 | [04-subagents/](04-subagents/) |
| **技能（Skills）** | 5 个内置 | 4 | 9 | [03-skills/](03-skills/) |
| **插件（Plugins）** | - | 3 | 3 | [07-plugins/](07-plugins/) |
| **MCP 服务器** | 1 | 8 | 9 | [05-mcp/](05-mcp/) |
| **钩子（Hooks）** | 25 个事件 | 7 | 7 | [06-hooks/](06-hooks/) |
| **记忆（Memory）** | 7 种类型 | 3 | 3 | [02-memory/](02-memory/) |
| **合计** | **99** | **43** | **117** | |

---

## Slash Commands

命令是用户主动调用的快捷方式，用于执行特定操作。

### 内置命令

| 命令 | 描述 | 使用场景 |
|---------|-------------|-------------|
| `/help` | 显示帮助信息 | 入门引导、了解命令 |
| `/btw` | 不加入上下文的附加提问 | 快速的旁枝问题 |
| `/chrome` | 配置 Chrome 集成 | 浏览器自动化 |
| `/clear` | 清除对话历史 | 重新开始、减少上下文 |
| `/diff` | 交互式差异查看器 | 查看变更内容 |
| `/config` | 查看/编辑配置 | 自定义行为 |
| `/status` | 显示会话状态 | 查看当前状态 |
| `/agents` | 列出可用智能体 | 查看委托选项 |
| `/skills` | 列出可用技能 | 查看自动调用能力 |
| `/hooks` | 列出已配置的钩子 | 调试自动化 |
| `/insights` | 分析会话模式 | 会话优化 |
| `/install-slack-app` | 安装 Claude Slack 应用 | Slack 集成 |
| `/keybindings` | 自定义键盘快捷键 | 按键自定义 |
| `/mcp` | 列出 MCP 服务器 | 检查外部集成 |
| `/memory` | 查看已加载的记忆文件 | 调试上下文加载 |
| `/mobile` | 生成移动端二维码 | 移动端访问 |
| `/passes` | 查看使用配额 | 订阅信息 |
| `/plugin` | 管理插件 | 安装/移除扩展 |
| `/plan` | 进入规划模式 | 复杂实现规划 |
| `/rewind` | 回退到检查点 | 撤销更改、探索替代方案 |
| `/checkpoint` | 管理检查点 | 保存/恢复状态 |
| `/cost` | 显示 token 使用成本 | 监控花费 |
| `/context` | 显示上下文窗口使用情况 | 管理对话长度 |
| `/export` | 导出对话 | 保存备份 |
| `/extra-usage` | 配置额外使用限制 | 频率限制管理 |
| `/feedback` | 提交反馈或错误报告 | 报告问题 |
| `/login` | 向 Anthropic 进行身份验证 | 访问功能 |
| `/logout` | 退出登录 | 切换账号 |
| `/sandbox` | 切换沙箱模式 | 安全命令执行 |
| `/vim` | 切换 vim 模式 | Vim 风格编辑 |
| `/doctor` | 运行诊断 | 排查问题 |
| `/reload-plugins` | 重新加载已安装的插件 | 插件管理 |
| `/release-notes` | 显示发布说明 | 查看新功能 |
| `/remote-control` | 启用远程控制 | 远程访问 |
| `/permissions` | 管理权限 | 控制访问 |
| `/session` | 管理会话 | 多会话工作流 |
| `/rename` | 重命名当前会话 | 整理会话 |
| `/resume` | 恢复上一个会话 | 继续工作 |
| `/todo` | 查看/管理待办列表 | 跟踪任务 |
| `/tasks` | 查看后台任务 | 监控异步操作 |
| `/copy` | 复制最后一条回复到剪贴板 | 快速分享输出 |
| `/teleport` | 将会话传输到另一台机器 | 远程继续工作 |
| `/desktop` | 打开 Claude 桌面应用 | 切换到桌面界面 |
| `/theme` | 更改颜色主题 | 自定义外观 |
| `/usage` | 显示 API 使用统计 | 监控配额和成本 |
| `/fork` | 分叉当前对话 | 探索替代方案 |
| `/stats` | 显示会话统计信息 | 查看会话指标 |
| `/statusline` | 配置状态栏 | 自定义状态显示 |
| `/stickers` | 查看会话贴纸 | 趣味奖励 |
| `/fast` | 切换快速输出模式 | 加速响应 |
| `/terminal-setup` | 配置终端集成 | 设置终端功能 |
| `/upgrade` | 检查更新 | 版本管理 |

### 自定义命令（示例）

| 命令 | 描述 | 使用场景 | 作用域 | 安装方式 |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | 分析代码以进行优化 | 性能优化 | 项目 | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | 准备 Pull Request | 提交 PR 之前 | 项目 | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | 生成 API 文档 | 接口文档编写 | 项目 | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | 创建带有上下文的 git 提交 | 提交变更 | 用户 | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | 暂存、提交并推送 | 快速部署 | 用户 | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | 重构文档结构 | 改善文档 | 项目 | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | 设置 CI/CD 流水线 | 新项目初始化 | 项目 | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | 扩展测试覆盖率 | 改善测试 | 项目 | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **作用域**：`User`（用户）= 个人工作流（`~/.claude/commands/`），`Project`（项目）= 团队共享（`.claude/commands/`）

**参考**：[01-slash-commands/](01-slash-commands/) | [官方文档](https://code.claude.com/docs/en/interactive-mode)

**快速安装（全部自定义命令）**：
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## Permission Modes

Claude Code 支持 6 种权限模式，用于控制工具调用的授权方式。

| 模式 | 描述 | 使用场景 |
|------|-------------|-------------|
| `default` | 每次工具调用前提示确认 | 标准交互式使用 |
| `acceptEdits` | 自动接受文件编辑，其他操作仍提示 | 受信任的编辑工作流 |
| `plan` | 仅只读工具，不允许写操作 | 规划和探索阶段 |
| `auto` | 无需提示，自动接受所有工具调用（研究预览版） | 完全自主操作 |
| `bypassPermissions` | 跳过所有权限检查 | CI/CD、无头环境 |
| `dontAsk` | 跳过需要权限的工具调用 | 非交互式脚本 |

> **注意**：`auto` 模式为研究预览版功能（2026 年 3 月）。`bypassPermissions` 仅应在受信任的沙箱环境中使用。

**参考**：[官方文档](https://code.claude.com/docs/en/permissions)

---

## Subagents

具有独立上下文的专业 AI 助手，用于执行特定任务。

### 内置子智能体

| 智能体 | 描述 | 可用工具 | 模型 | 使用场景 |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | 多步骤任务、研究 | 所有工具 | 继承主模型 | 复杂研究、多文件任务 |
| **Plan** | 实现规划 | Read, Glob, Grep, Bash | 继承主模型 | 架构设计、规划 |
| **Explore** | 代码库探索 | Read, Glob, Grep | Haiku 4.5 | 快速搜索、理解代码 |
| **Bash** | 命令执行 | Bash | 继承主模型 | Git 操作、终端任务 |
| **statusline-setup** | 状态栏配置 | Bash, Read, Write | Sonnet 4.6 | 配置状态栏显示 |
| **Claude Code Guide** | 帮助与文档 | Read, Glob, Grep | Haiku 4.5 | 获取帮助、学习功能 |

### 子智能体配置字段

| 字段 | 类型 | 描述 |
|-------|------|-------------|
| `name` | string | 智能体标识符 |
| `description` | string | 智能体的功能说明 |
| `model` | string | 模型覆盖（如 `haiku-4.5`） |
| `tools` | array | 允许使用的工具列表 |
| `effort` | string | 推理能力等级（`low`、`medium`、`high`） |
| `initialPrompt` | string | 智能体启动时注入的系统提示词 |
| `disallowedTools` | array | 明确禁止该智能体使用的工具 |

### 自定义子智能体（示例）

| 智能体 | 描述 | 使用场景 | 作用域 | 安装方式 |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | 全面的代码质量审查 | 代码审查会话 | 项目 | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | 功能架构设计 | 新功能规划 | 项目 | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | 深度代码库分析 | 理解已有功能 | 项目 | `cp 04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | Clean Code 原则审查 | 可维护性审查 | 项目 | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | 测试策略与覆盖率 | 测试规划 | 项目 | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | 技术文档撰写 | API 文档、指南 | 项目 | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | 以安全为重点的审查 | 安全审计 | 项目 | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | 完整功能实现 | 功能开发 | 项目 | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | 根因分析 | Bug 调查 | 用户 | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL 查询、数据分析 | 数据任务 | 用户 | `cp 04-subagents/data-scientist.md .claude/agents/` |

> **作用域**：`User`（用户）= 个人（`~/.claude/agents/`），`Project`（项目）= 团队共享（`.claude/agents/`）

**参考**：[04-subagents/](04-subagents/) | [官方文档](https://code.claude.com/docs/en/sub-agents)

**快速安装（全部自定义智能体）**：
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## Skills

带有指令、脚本和模板的自动调用能力。

### 示例技能

| 技能 | 描述 | 自动触发时机 | 作用域 | 安装方式 |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | 全面代码审查 | "Review this code"、"Check quality" | 项目 | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | 品牌一致性检查 | 撰写营销文案时 | 项目 | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | API 文档生成器 | "Generate docs"、"Document API" | 项目 | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | 系统化代码重构（Martin Fowler 原则） | "Refactor this"、"Clean up code" | 用户 | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **作用域**：`User`（用户）= 个人（`~/.claude/skills/`），`Project`（项目）= 团队共享（`.claude/skills/`）

### 技能目录结构

```
~/.claude/skills/skill-name/
├── SKILL.md          # 技能定义与指令
├── scripts/          # 辅助脚本
└── templates/        # 输出模板
```

### 技能 Frontmatter 字段

技能在 `SKILL.md` 中支持 YAML frontmatter 进行配置：

| 字段 | 类型 | 描述 |
|-------|------|-------------|
| `name` | string | 技能显示名称 |
| `description` | string | 技能功能说明 |
| `autoInvoke` | array | 自动触发的关键短语 |
| `effort` | string | 推理能力等级（`low`、`medium`、`high`） |
| `shell` | string | 脚本使用的 Shell（`bash`、`zsh`、`sh`） |

**参考**：[03-skills/](03-skills/) | [官方文档](https://code.claude.com/docs/en/skills)

**快速安装（全部技能）**：
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### 内置技能

| 技能 | 描述 | 自动触发时机 |
|-------|-------------|-------------------|
| `/simplify` | 审查代码质量 | 编写代码后 |
| `/batch` | 对多个文件批量执行提示词 | 批量操作 |
| `/debug` | 调试失败的测试或错误 | 调试会话 |
| `/loop` | 定时循环执行提示词 | 周期性任务 |
| `/claude-api` | 使用 Claude API 构建应用 | API 开发 |

---

## Plugins

命令、智能体、MCP 服务器和钩子的打包集合。

### 示例插件

| 插件 | 描述 | 组成内容 | 使用场景 | 作用域 | 安装方式 |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | PR 审查工作流 | 3 个命令、3 个智能体、GitHub MCP | 代码审查 | 项目 | `/plugin install pr-review` |
| `devops-automation` | 部署与监控 | 4 个命令、3 个智能体、K8s MCP | DevOps 任务 | 项目 | `/plugin install devops-automation` |
| `documentation` | 文档生成套件 | 4 个命令、3 个智能体、模板 | 文档编写 | 项目 | `/plugin install documentation` |

> **作用域**：`Project`（项目）= 团队共享，`User`（用户）= 个人工作流

### 插件目录结构

```
.claude-plugin/
├── plugin.json       # 清单文件
├── commands/         # Slash commands
├── agents/           # 子智能体
├── skills/           # 技能
├── mcp/              # MCP 配置
├── hooks/            # 钩子脚本
└── scripts/          # 实用脚本
```

**参考**：[07-plugins/](07-plugins/) | [官方文档](https://code.claude.com/docs/en/plugins)

**插件管理命令**：
```bash
/plugin list              # 列出已安装的插件
/plugin install <name>    # 安装插件
/plugin remove <name>     # 移除插件
/plugin update <name>     # 更新插件
```

---

## MCP Servers

用于访问外部工具和 API 的模型上下文协议（Model Context Protocol）服务器。

### 常用 MCP 服务器

| 服务器 | 描述 | 使用场景 | 作用域 | 安装方式 |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | PR 管理、Issues、代码 | GitHub 工作流 | 项目 | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL 查询、数据访问 | 数据库操作 | 项目 | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | 高级文件操作 | 复杂文件任务 | 用户 | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | 团队沟通 | 通知、更新 | 项目 | 在设置中配置 |
| **Google Docs** | 文档访问 | 文档编辑、审查 | 项目 | 在设置中配置 |
| **Asana** | 项目管理 | 任务追踪 | 项目 | 在设置中配置 |
| **Stripe** | 支付数据 | 财务分析 | 项目 | 在设置中配置 |
| **Memory** | 持久化记忆 | 跨会话召回 | 用户 | 在设置中配置 |
| **Context7** | 库文档查询 | 获取最新文档 | 内置 | 内置 |

> **作用域**：`Project`（项目）= 团队（`.mcp.json`），`User`（用户）= 个人（`~/.claude.json`），`Built-in`（内置）= 预安装

### MCP 配置示例

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

**参考**：[05-mcp/](05-mcp/) | [MCP 协议文档](https://modelcontextprotocol.io)

**快速安装（GitHub MCP）**：
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## Hooks

事件驱动的自动化，在 Claude Code 事件发生时执行 Shell 命令。

### 钩子事件

| 事件 | 描述 | 触发时机 | 使用场景 |
|-------|-------------|----------------|-----------|
| `SessionStart` | 会话开始/恢复 | 会话初始化时 | 初始化设置 |
| `InstructionsLoaded` | 指令已加载 | 加载 CLAUDE.md 或规则文件时 | 自定义指令处理 |
| `UserPromptSubmit` | 提示词处理前 | 用户发送消息时 | 输入验证 |
| `PreToolUse` | 工具执行前 | 任何工具运行前 | 验证、日志记录 |
| `PermissionRequest` | 显示权限对话框 | 敏感操作前 | 自定义审批流程 |
| `PostToolUse` | 工具执行成功后 | 任何工具完成后 | 格式化、通知 |
| `PostToolUseFailure` | 工具执行失败 | 工具报错后 | 错误处理、日志记录 |
| `Notification` | 发送通知 | Claude 发送通知时 | 外部告警 |
| `SubagentStart` | 子智能体启动 | 子智能体任务开始时 | 初始化子智能体上下文 |
| `SubagentStop` | 子智能体结束 | 子智能体任务完成时 | 串联后续操作 |
| `Stop` | Claude 响应完成 | 响应结束时 | 清理、报告 |
| `StopFailure` | API 错误终止轮次 | API 出现错误时 | 错误恢复、日志记录 |
| `TeammateIdle` | 队友智能体空闲 | 智能体团队协调时 | 分配工作 |
| `TaskCompleted` | 任务标记为完成 | 任务完成时 | 任务后处理 |
| `TaskCreated` | 通过 TaskCreate 创建任务 | 新任务创建时 | 任务跟踪、日志记录 |
| `ConfigChange` | 配置已更新 | 设置修改时 | 响应配置变更 |
| `CwdChanged` | 工作目录变更 | 目录切换时 | 目录特定初始化 |
| `FileChanged` | 被监视文件变更 | 文件修改时 | 文件监控、重新构建 |
| `PreCompact` | 压缩操作前 | 上下文压缩前 | 状态保存 |
| `PostCompact` | 压缩完成后 | 压缩完成时 | 压缩后处理 |
| `WorktreeCreate` | 工作树正在创建 | Git 工作树创建时 | 设置工作树环境 |
| `WorktreeRemove` | 工作树正在移除 | Git 工作树移除时 | 清理工作树资源 |
| `Elicitation` | MCP 服务器请求输入 | MCP elicitation 时 | 输入验证 |
| `ElicitationResult` | 用户响应 elicitation | 用户作出响应时 | 响应处理 |
| `SessionEnd` | 会话终止 | 会话结束时 | 清理、保存状态 |

### 示例钩子

| 钩子 | 描述 | 事件 | 作用域 | 安装方式 |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | 命令验证 | PreToolUse:Bash | 项目 | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | 安全扫描 | PostToolUse:Write | 项目 | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | 自动代码格式化 | PostToolUse:Write | 用户 | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | 提示词验证 | UserPromptSubmit | 项目 | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | Token 使用量追踪 | Stop | 用户 | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | 提交前验证 | PreToolUse:Bash | 项目 | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | 命令日志记录 | PostToolUse:Bash | 用户 | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |

> **作用域**：`Project`（项目）= 团队（`.claude/settings.json`），`User`（用户）= 个人（`~/.claude/settings.json`）

### 钩子配置

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

**参考**：[06-hooks/](06-hooks/) | [官方文档](https://code.claude.com/docs/en/hooks)

**快速安装（全部钩子）**：
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## Memory Files

跨会话自动加载的持久化上下文。

### 记忆类型

| 类型 | 存储位置 | 作用域 | 使用场景 |
|------|----------|-------|-------------|
| **Managed Policy** | 组织管理的策略 | 组织 | 执行全组织统一标准 |
| **Project** | `./CLAUDE.md` | 项目（团队） | 团队规范、项目背景 |
| **Project Rules** | `.claude/rules/` | 项目（团队） | 模块化项目规则 |
| **User** | `~/.claude/CLAUDE.md` | 用户（个人） | 个人偏好设置 |
| **User Rules** | `~/.claude/rules/` | 用户（个人） | 模块化个人规则 |
| **Local** | `./CLAUDE.local.md` | 本地（git 忽略） | 机器特定覆盖配置（截至 2026 年 3 月官方文档未收录，可能为遗留功能） |
| **Auto Memory** | 自动管理 | 会话 | 自动捕获的洞察与纠正信息 |

> **作用域**：`Organization`（组织）= 由管理员管理，`Project`（项目）= 通过 git 与团队共享，`User`（用户）= 个人偏好，`Local`（本地）= 不提交，`Session`（会话）= 自动管理

**参考**：[02-memory/](02-memory/) | [官方文档](https://code.claude.com/docs/en/memory)

**快速安装**：
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## New Features (March 2026)

| 功能 | 描述 | 使用方式 |
|---------|-------------|------------|
| **Remote Control** | 通过 API 远程控制 Claude Code 会话 | 使用远程控制 API 以编程方式发送提示词并接收响应 |
| **Web Sessions** | 在基于浏览器的环境中运行 Claude Code | 通过 `claude web` 或 Anthropic Console 访问 |
| **Desktop App** | Claude Code 原生桌面应用 | 使用 `/desktop` 或从 Anthropic 官网下载 |
| **Agent Teams** | 协调多个智能体协同处理相关任务 | 配置队友智能体，使其相互协作并共享上下文 |
| **Task List** | 后台任务管理与监控 | 使用 `/tasks` 查看和管理后台操作 |
| **Prompt Suggestions** | 基于上下文的命令建议 | 建议根据当前上下文自动出现 |
| **Git Worktrees** | 隔离的 Git 工作树，支持并行开发 | 使用工作树命令安全地并行分支开发 |
| **Sandboxing** | 隔离的执行环境，提升安全性 | 使用 `/sandbox` 切换；在受限环境中运行命令 |
| **MCP OAuth** | MCP 服务器的 OAuth 身份验证 | 在 MCP 服务器设置中配置 OAuth 凭据以实现安全访问 |
| **MCP Tool Search** | 动态搜索和发现 MCP 工具 | 使用工具搜索在已连接的服务器中查找可用 MCP 工具 |
| **Scheduled Tasks** | 使用 `/loop` 和 cron 工具设置周期性任务 | 使用 `/loop 5m /command` 或 CronCreate 工具 |
| **Chrome Integration** | 使用无头 Chromium 进行浏览器自动化 | 使用 `--chrome` 参数或 `/chrome` 命令 |
| **Keyboard Customization** | 自定义键位绑定，包括组合键支持 | 使用 `/keybindings` 或编辑 `~/.claude/keybindings.json` |
| **Auto Mode** | 无需权限提示的完全自主操作（研究预览版） | 使用 `--mode auto` 或 `/permissions auto`；2026 年 3 月 |
| **Channels** | 多渠道通信（Telegram、Slack 等）（研究预览版） | 配置渠道插件；2026 年 3 月 |
| **Voice Dictation** | 语音输入提示词 | 使用麦克风图标或语音快捷键 |
| **Agent Hook Type** | 钩子可以启动子智能体而非运行 Shell 命令 | 在钩子配置中设置 `"type": "agent"` |
| **Prompt Hook Type** | 钩子可以向对话中注入提示词文本 | 在钩子配置中设置 `"type": "prompt"` |
| **MCP Elicitation** | MCP 服务器可在工具执行期间请求用户输入 | 通过 `Elicitation` 和 `ElicitationResult` 钩子事件处理 |
| **WebSocket MCP Transport** | MCP 服务器连接的 WebSocket 传输方式 | 在 MCP 服务器配置中使用 `"transport": "websocket"` |
| **Plugin LSP Support** | 通过插件集成语言服务器协议（LSP） | 在 `plugin.json` 中配置 LSP 服务器以获得编辑器功能 |
| **Managed Drop-ins** | 组织管理的插入式配置（v2.1.83） | 由管理员通过管理策略配置，自动应用于所有用户 |

---

## 快速参考矩阵

### 功能选择指南

| 需求 | 推荐功能 | 原因 |
|------|---------------------|-----|
| 快速快捷操作 | Slash Command | 手动触发，即时响应 |
| 持久化上下文 | Memory | 自动加载 |
| 复杂自动化 | Skill | 自动调用 |
| 专项任务 | Subagent | 独立上下文 |
| 外部数据获取 | MCP Server | 实时访问 |
| 事件自动化 | Hook | 事件触发 |
| 完整解决方案 | Plugin | 一体化打包 |

### 安装优先级

| 优先级 | 功能 | 命令 |
|----------|---------|---------|
| 1. 必要 | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. 日常使用 | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. 质量保障 | Subagents | `cp 04-subagents/*.md .claude/agents/` |
| 4. 自动化 | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. 外部集成 | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. 进阶功能 | Skills | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. 完整方案 | Plugins | `/plugin install pr-review` |

---

## 一键安装全部示例

安装本仓库中的所有示例：

```bash
# 创建目录
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# 安装所有功能
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## 延伸阅读

- [Claude Code 官方文档](https://code.claude.com/docs/en/overview)
- [MCP 协议规范](https://modelcontextprotocol.io)
- [学习路线图](LEARNING-ROADMAP.md)
- [主 README](README.md)

---

**最后更新**：2026 年 3 月
