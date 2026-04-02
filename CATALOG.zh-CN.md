<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 功能目录（Feature Catalog）

> Claude Code 全部能力的速查手册：commands、agents、skills、plugins、hooks。

**导航**： [Commands](#slash-commands) | [Permission Modes](#permission-modes) | [Subagents](#subagents) | [Skills](#skills) | [Plugins](#plugins) | [MCP Servers](#mcp-servers) | [Hooks](#hooks) | [Memory](#memory-files) | [New Features](#new-features-march-2026)

---

## 概览

| 功能 | 内置 | 示例 | 总计 | 参考 |
|---------|----------|----------|-------|-----------|
| **Slash Commands** | 55+ | 8 | 63+ | [01-slash-commands/](01-slash-commands/README.zh-CN.md) |
| **Subagents** | 6 | 10 | 16 | [04-subagents/](04-subagents/README.zh-CN.md) |
| **Skills** | 5 bundled | 4 | 9 | [03-skills/](03-skills/README.zh-CN.md) |
| **Plugins** | - | 3 | 3 | [07-plugins/](07-plugins/README.zh-CN.md) |
| **MCP Servers** | 1 | 8 | 9 | [05-mcp/](05-mcp/README.zh-CN.md) |
| **Hooks** | 25 events | 7 | 7 | [06-hooks/](06-hooks/README.zh-CN.md) |
| **Memory** | 7 types | 3 | 3 | [02-memory/](02-memory/README.zh-CN.md) |
| **Total** | **99** | **43** | **117** | |

---

## Slash Commands

Commands 是由用户手动触发、执行特定动作的快捷命令。

### 内置命令

| Command | 说明 | 适用场景 |
|---------|-------------|-------------|
| `/help` | 显示帮助信息 | 入门、查看命令 |
| `/btw` | 不写入上下文的侧向提问 | 临时插问 |
| `/chrome` | 配置 Chrome 集成 | 浏览器自动化 |
| `/clear` | 清空对话历史 | 重新开始、压缩上下文 |
| `/diff` | 交互式 diff 查看器 | 审查变更 |
| `/config` | 查看/编辑配置 | 自定义行为 |
| `/status` | 显示会话状态 | 查看当前状态 |
| `/agents` | 列出可用 agents | 查看可委派选项 |
| `/skills` | 列出可用 skills | 查看自动能力 |
| `/hooks` | 列出已配置 hooks | 排查自动化问题 |
| `/insights` | 分析会话模式 | 会话优化 |
| `/install-slack-app` | 安装 Claude Slack 应用 | Slack 集成 |
| `/keybindings` | 自定义快捷键 | 键位定制 |
| `/mcp` | 列出 MCP servers | 检查外部集成 |
| `/memory` | 查看已加载 memory 文件 | 排查上下文加载 |
| `/mobile` | 生成移动端二维码 | 手机访问 |
| `/passes` | 查看 usage passes | 订阅信息 |
| `/plugin` | 管理插件 | 安装/移除扩展 |
| `/plan` | 进入 planning mode | 复杂实现任务 |
| `/rewind` | 回退到 checkpoint | 撤销变更、探索分支 |
| `/checkpoint` | 管理 checkpoints | 保存/恢复状态 |
| `/cost` | 显示 token 成本 | 监控开销 |
| `/context` | 显示上下文窗口占用 | 管理会话长度 |
| `/export` | 导出会话 | 存档参考 |
| `/extra-usage` | 配置额外配额 | 速率限制管理 |
| `/feedback` | 提交反馈或 bug | 问题上报 |
| `/login` | 与 Anthropic 账户认证 | 启用功能 |
| `/logout` | 退出登录 | 切换账号 |
| `/sandbox` | 切换 sandbox 模式 | 安全执行命令 |
| `/vim` | 切换 vim 模式 | Vim 风格输入 |
| `/doctor` | 运行诊断 | 故障排查 |
| `/reload-plugins` | 重载插件 | 插件管理 |
| `/release-notes` | 查看版本说明 | 了解新功能 |
| `/remote-control` | 启用远程控制 | 远程访问 |
| `/permissions` | 管理权限 | 控制访问边界 |
| `/session` | 管理会话 | 多会话工作流 |
| `/rename` | 重命名当前会话 | 会话整理 |
| `/resume` | 恢复历史会话 | 延续工作 |
| `/todo` | 查看/管理待办 | 任务追踪 |
| `/tasks` | 查看后台任务 | 监控异步执行 |
| `/copy` | 复制上一条回复 | 快速分享输出 |
| `/teleport` | 将会话迁移到另一台机器 | 跨设备续作 |
| `/desktop` | 打开 Claude Desktop | 切换桌面端 |
| `/theme` | 切换主题 | 外观定制 |
| `/usage` | 显示 API 使用统计 | 监控配额与成本 |
| `/fork` | 分叉当前会话 | 探索替代方案 |
| `/stats` | 显示会话统计 | 回顾指标 |
| `/statusline` | 配置状态栏 | 定制状态显示 |
| `/stickers` | 查看会话贴纸 | 趣味奖励 |
| `/fast` | 切换快速输出模式 | 加速响应 |
| `/terminal-setup` | 配置终端集成 | 终端能力设置 |
| `/upgrade` | 检查更新 | 版本管理 |

### 自定义命令（示例）

| Command | 说明 | 适用场景 | 作用域 | 安装方式 |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | 分析代码优化点 | 性能优化 | Project | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | 准备 Pull Request | 提交 PR 前 | Project | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | 生成 API 文档 | 文档产出 | Project | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | 基于上下文生成提交 | 提交代码 | User | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | add/commit/push 一体化 | 快速推送 | User | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | 重构文档结构 | 文档改进 | Project | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | 初始化 CI/CD 流水线 | 新项目 | Project | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | 扩展单测覆盖 | 测试增强 | Project | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **Scope**: `User` = 个人工作流（`~/.claude/commands/`），`Project` = 团队共享（`.claude/commands/`）

**参考**： [01-slash-commands/](01-slash-commands/README.zh-CN.md) | [Official Docs](https://code.claude.com/docs/en/interactive-mode)

**一键安装全部自定义命令**：
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## Permission Modes

Claude Code 支持 6 种权限模式，用于控制工具调用授权方式。

| Mode | 说明 | 适用场景 |
|------|-------------|-------------|
| `default` | 每次工具调用都询问 | 标准交互使用 |
| `acceptEdits` | 自动接受文件编辑，其他操作询问 | 可信编辑工作流 |
| `plan` | 仅允许只读工具，不写入 | 规划与探索 |
| `auto` | 自动接受工具调用，不弹窗 | 全自治运行（Research Preview） |
| `bypassPermissions` | 跳过全部权限检查 | CI/CD、无头环境 |
| `dontAsk` | 跳过需授权的工具调用 | 非交互脚本 |

> **注意**：`auto` 属于 Research Preview（2026 年 3 月）。`bypassPermissions` 仅建议在可信、隔离环境中使用。

**参考**： [Official Docs](https://code.claude.com/docs/en/permissions)

---

## Subagents

Subagents 是用于特定任务、具备隔离上下文的专用 AI 助手。

### 内置 Subagents

| Agent | 说明 | 工具 | 模型 | 适用场景 |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | 多步骤任务、研究 | 全工具 | 继承主模型 | 复杂调研、多文件任务 |
| **Plan** | 实现规划 | Read, Glob, Grep, Bash | 继承主模型 | 架构设计、任务规划 |
| **Explore** | 代码库探索 | Read, Glob, Grep | Haiku 4.5 | 快速检索、理解代码 |
| **Bash** | 命令执行 | Bash | 继承主模型 | Git 操作、终端任务 |
| **statusline-setup** | 状态栏配置 | Bash, Read, Write | Sonnet 4.6 | 配置状态栏显示 |
| **Claude Code Guide** | 帮助与文档 | Read, Glob, Grep | Haiku 4.5 | 功能答疑、学习指导 |

### Subagent 配置字段

| Field | 类型 | 说明 |
|-------|------|-------------|
| `name` | string | Agent 标识名 |
| `description` | string | Agent 职责描述 |
| `model` | string | 模型覆盖（如 `haiku-4.5`） |
| `tools` | array | 允许的工具列表 |
| `effort` | string | 推理强度（`low`, `medium`, `high`） |
| `initialPrompt` | string | Agent 启动时注入的系统提示 |
| `disallowedTools` | array | 显式禁用工具 |

### 自定义 Subagents（示例）

| Agent | 说明 | 适用场景 | 作用域 | 安装方式 |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | 综合代码质量审查 | 代码评审 | Project | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | 功能架构设计 | 新功能设计 | Project | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | 深度代码库分析 | 理解现有系统 | Project | `cp 04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | Clean Code 原则审查 | 可维护性评审 | Project | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | 测试策略与覆盖分析 | 测试规划 | Project | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | 技术文档编写 | API 文档、指南 | Project | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | 安全专项审查 | 安全审计 | Project | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | 端到端功能实现 | 功能开发 | Project | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | 根因分析 | 问题定位 | User | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL/数据分析 | 数据任务 | User | `cp 04-subagents/data-scientist.md .claude/agents/` |

> **Scope**: `User` = 个人（`~/.claude/agents/`），`Project` = 团队共享（`.claude/agents/`）

**参考**： [04-subagents/](04-subagents/README.zh-CN.md) | [Official Docs](https://code.claude.com/docs/en/sub-agents)

**一键安装全部自定义 agents**：
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## Skills

Skills 是带说明、脚本、模板的可自动触发能力模块。

### 示例 Skills

| Skill | 说明 | 自动触发场景 | 作用域 | 安装方式 |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | 综合代码审查 | “Review this code”, “Check quality” | Project | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | 品牌语气一致性检查 | 撰写营销文案 | Project | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | API 文档生成 | “Generate docs”, “Document API” | Project | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | 系统化重构（Martin Fowler） | “Refactor this”, “Clean up code” | User | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **Scope**: `User` = 个人（`~/.claude/skills/`），`Project` = 团队共享（`.claude/skills/`）

### Skill 结构

```text
~/.claude/skills/skill-name/
├── SKILL.md          # Skill 定义与说明
├── scripts/          # 辅助脚本
└── templates/        # 输出模板
```

### Skill Frontmatter 字段

`SKILL.md` 中可使用 YAML frontmatter 配置：

| Field | 类型 | 说明 |
|-------|------|-------------|
| `name` | string | Skill 显示名称 |
| `description` | string | Skill 功能描述 |
| `autoInvoke` | array | 自动触发短语 |
| `effort` | string | 推理强度（`low`, `medium`, `high`） |
| `shell` | string | 脚本使用 shell（`bash`, `zsh`, `sh`） |

**参考**： [03-skills/](03-skills/README.zh-CN.md) | [Official Docs](https://code.claude.com/docs/en/skills)

**一键安装全部 skills**：
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### Bundled Skills

| Skill | 说明 | 自动触发场景 |
|-------|-------------|-------------------|
| `/simplify` | 代码质量审查 | 代码编写后 |
| `/batch` | 多文件批处理 prompt | 批量操作 |
| `/debug` | 调试失败测试/错误 | 调试会话 |
| `/loop` | 按时间间隔重复执行 | 周期任务 |
| `/claude-api` | 使用 Claude API 开发 | API 开发 |

---

## Plugins

Plugins 是 commands、agents、MCP servers、hooks 的打包集合。

### 示例 Plugins

| Plugin | 说明 | 组件 | 适用场景 | 作用域 | 安装方式 |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | PR 评审流程 | 3 commands, 3 agents, GitHub MCP | 代码评审 | Project | `/plugin install pr-review` |
| `devops-automation` | 部署与监控 | 4 commands, 3 agents, K8s MCP | DevOps 任务 | Project | `/plugin install devops-automation` |
| `documentation` | 文档生成套件 | 4 commands, 3 agents, templates | 文档体系 | Project | `/plugin install documentation` |

> **Scope**: `Project` = 团队共享，`User` = 个人工作流

### Plugin 结构

```text
.claude-plugin/
├── plugin.json       # 清单文件
├── commands/         # Slash commands
├── agents/           # Subagents
├── skills/           # Skills
├── mcp/              # MCP 配置
├── hooks/            # Hook 脚本
└── scripts/          # 工具脚本
```

**参考**： [07-plugins/](07-plugins/README.zh-CN.md) | [Official Docs](https://code.claude.com/docs/en/plugins)

**插件管理命令**：
```bash
/plugin list              # 列出已安装插件
/plugin install <name>    # 安装插件
/plugin remove <name>     # 卸载插件
/plugin update <name>     # 更新插件
```

---

## MCP Servers

Model Context Protocol servers 用于访问外部工具和 API。

### 常见 MCP Servers

| Server | 说明 | 适用场景 | 作用域 | 安装方式 |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | PR、Issue、代码操作 | GitHub 工作流 | Project | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL 查询、数据访问 | 数据库操作 | Project | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | 高阶文件操作 | 复杂文件任务 | User | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | 团队沟通 | 通知、更新 | Project | 在 settings 中配置 |
| **Google Docs** | 文档访问 | 文档编辑、审阅 | Project | 在 settings 中配置 |
| **Asana** | 项目管理 | 任务跟踪 | Project | 在 settings 中配置 |
| **Stripe** | 支付数据 | 财务分析 | Project | 在 settings 中配置 |
| **Memory** | 持久记忆 | 跨会话回忆 | User | 在 settings 中配置 |
| **Context7** | 库文档检索 | 最新文档查询 | Built-in | 内置 |

> **Scope**: `Project` = 团队（`.mcp.json`），`User` = 个人（`~/.claude.json`），`Built-in` = 预装

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

**参考**： [05-mcp/](05-mcp/README.zh-CN.md) | [MCP Protocol Docs](https://modelcontextprotocol.io)

**快速安装 GitHub MCP**：
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## Hooks

Hooks 是事件驱动自动化，在 Claude Code 事件发生时执行 shell 命令。

### Hook 事件

| Event | 说明 | 触发时机 | 用途 |
|-------|-------------|----------------|-----------|
| `SessionStart` | 会话开始/恢复 | 初始化阶段 | 预置任务 |
| `InstructionsLoaded` | 指令加载 | CLAUDE.md 或规则加载后 | 定制指令处理 |
| `UserPromptSubmit` | 处理 prompt 前 | 用户发送消息时 | 输入校验 |
| `PreToolUse` | 工具执行前 | 任意工具运行前 | 校验、审计 |
| `PermissionRequest` | 权限弹窗前 | 敏感操作前 | 自定义审批流 |
| `PostToolUse` | 工具成功后 | 工具完成后 | 格式化、通知 |
| `PostToolUseFailure` | 工具失败后 | 工具报错后 | 错误处理、日志 |
| `Notification` | 通知发送时 | Claude 发通知 | 外部告警 |
| `SubagentStart` | 子代理启动 | 子任务开始 | 初始化子上下文 |
| `SubagentStop` | 子代理结束 | 子任务完成 | 串联后续动作 |
| `Stop` | Claude 响应结束 | 回复完成 | 清理、汇总 |
| `StopFailure` | API 错误中断 | API 出错 | 恢复、日志 |
| `TeammateIdle` | teammate 空闲 | 团队协作中 | 任务再分配 |
| `TaskCompleted` | 任务完成 | 标记完成时 | 后处理 |
| `TaskCreated` | 任务创建 | TaskCreate 后 | 跟踪、审计 |
| `ConfigChange` | 配置更新 | settings 修改后 | 响应配置变更 |
| `CwdChanged` | 工作目录切换 | 目录变化时 | 目录级初始化 |
| `FileChanged` | 监听文件变化 | 文件被修改时 | 触发重建/检测 |
| `PreCompact` | compact 前 | 上下文压缩前 | 状态保存 |
| `PostCompact` | compact 后 | 压缩完成后 | 后置动作 |
| `WorktreeCreate` | worktree 创建 | git worktree 创建时 | 环境初始化 |
| `WorktreeRemove` | worktree 删除 | git worktree 移除时 | 资源清理 |
| `Elicitation` | MCP 请求用户输入 | 工具执行中需补充输入 | 输入校验 |
| `ElicitationResult` | 用户回应 elicitation | 用户提交回应后 | 结果处理 |
| `SessionEnd` | 会话结束 | 终止时 | 清理与持久化 |

### 示例 Hooks

| Hook | 说明 | Event | 作用域 | 安装方式 |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | 命令校验 | PreToolUse:Bash | Project | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | 安全扫描 | PostToolUse:Write | Project | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | 自动格式化 | PostToolUse:Write | User | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | prompt 校验 | UserPromptSubmit | Project | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | token 使用追踪 | Stop | User | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | 提交前校验 | PreToolUse:Bash | Project | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | 命令日志 | PostToolUse:Bash | User | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |

> **Scope**: `Project` = 团队（`.claude/settings.json`），`User` = 个人（`~/.claude/settings.json`）

### Hook 配置示例

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

**参考**： [06-hooks/](06-hooks/README.zh-CN.md) | [Official Docs](https://code.claude.com/docs/en/hooks)

**一键安装全部 hooks**：
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## Memory Files

Memory 文件用于跨会话自动加载持久上下文。

### Memory 类型

| 类型 | 位置 | 作用域 | 适用场景 |
|------|----------|-------|-------------|
| **Managed Policy** | 组织托管策略 | Organization | 统一企业规范 |
| **Project** | `./CLAUDE.md` | Project (team) | 团队标准、项目上下文 |
| **Project Rules** | `.claude/rules/` | Project (team) | 模块化项目规则 |
| **User** | `~/.claude/CLAUDE.md` | User (personal) | 个人偏好 |
| **User Rules** | `~/.claude/rules/` | User (personal) | 模块化个人规则 |
| **Local** | `./CLAUDE.local.md` | Local (git-ignored) | 机器级覆盖（截至 2026-03 官方文档未明确，可能为历史能力） |
| **Auto Memory** | 自动维护 | Session | 自动沉淀偏好与纠偏 |

> **Scope**: `Organization` = 管理员下发，`Project` = 团队共享，`User` = 个人层，`Local` = 不提交，`Session` = 系统自动管理

**参考**： [02-memory/](02-memory/README.zh-CN.md) | [Official Docs](https://code.claude.com/docs/en/memory)

**快速安装**：
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## New Features (March 2026)

| Feature | 说明 | 使用方式 |
|---------|-------------|------------|
| **Remote Control** | 通过 API 远程控制 Claude Code 会话 | 使用 remote control API 以编程方式发送 prompt 与接收响应 |
| **Web Sessions** | 在浏览器环境运行 Claude Code | `claude web` 或通过 Anthropic Console |
| **Desktop App** | Claude Code 原生桌面应用 | 使用 `/desktop` 或官网下载安装 |
| **Agent Teams** | 协调多个 agent 协作处理相关任务 | 配置 teammate agents 实现协同与共享上下文 |
| **Task List** | 后台任务管理与监控 | 使用 `/tasks` 查看和管理 |
| **Prompt Suggestions** | 上下文感知命令建议 | 基于当前上下文自动展示建议 |
| **Git Worktrees** | 隔离 git 工作树并行开发 | 使用 worktree 命令进行并行分支工作 |
| **Sandboxing** | 安全隔离执行环境 | 使用 `/sandbox` 切换；命令在受限环境执行 |
| **MCP OAuth** | MCP server 的 OAuth 认证 | 在 MCP 配置中设置 OAuth 凭据 |
| **MCP Tool Search** | 动态检索和发现 MCP 工具 | 跨已连接 servers 搜索可用工具 |
| **Scheduled Tasks** | 用 `/loop` 与 cron 工具配置周期任务 | `/loop 5m /command` 或 CronCreate |
| **Chrome Integration** | 基于 headless Chromium 的浏览器自动化 | `--chrome` 或 `/chrome` |
| **Keyboard Customization** | 快捷键定制（含 chord 支持） | `/keybindings` 或编辑 `~/.claude/keybindings.json` |
| **Auto Mode** | 无权限弹窗全自治运行（Research Preview） | `--mode auto` 或 `/permissions auto`（2026-03） |
| **Channels** | 多通道通信（Telegram/Slack 等）（Research Preview） | 配置 channel plugins（2026-03） |
| **Voice Dictation** | 语音输入 prompt | 麦克风图标或语音快捷键 |
| **Agent Hook Type** | hook 通过 subagent 执行而非 shell 命令 | 在 hook 配置中设置 `"type": "agent"` |
| **Prompt Hook Type** | hook 向会话注入 prompt 文本 | 在 hook 配置中设置 `"type": "prompt"` |
| **MCP Elicitation** | MCP server 执行期间可向用户请求输入 | 通过 `Elicitation` 和 `ElicitationResult` 事件处理 |
| **WebSocket MCP Transport** | MCP 连接支持 WebSocket 传输 | 在 MCP 配置中设置 `"transport": "websocket"` |
| **Plugin LSP Support** | 插件支持 Language Server Protocol 集成 | 在 `plugin.json` 中配置 LSP servers |
| **Managed Drop-ins** | 组织托管的 drop-in 配置（v2.1.83） | 管理员策略下发，自动应用到全部用户 |

---

## Quick Reference Matrix

### 功能选型

| 需求 | 推荐功能 | 原因 |
|------|---------------------|-----|
| 快捷操作 | Slash Command | 手动触发、立即生效 |
| 持久上下文 | Memory | 自动加载 |
| 复杂自动化 | Skill | 自动触发 |
| 专项任务 | Subagent | 隔离上下文 |
| 外部数据 | MCP Server | 实时访问 |
| 事件自动化 | Hook | 事件触发 |
| 完整方案 | Plugin | 一体化打包 |

### 安装优先级

| 优先级 | 功能 | 命令 |
|----------|---------|---------|
| 1. Essential | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. Daily Use | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. Quality | Subagents | `cp 04-subagents/*.md .claude/agents/` |
| 4. Automation | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. External | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. Advanced | Skills | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. Complete | Plugins | `/plugin install pr-review` |

---

## 一条命令安装全部示例

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

## 其他资源

- [Official Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Learning Roadmap](LEARNING-ROADMAP.zh-CN.md)
- [Main README](README.zh-CN.md)

---

**Last Updated**: March 2026
