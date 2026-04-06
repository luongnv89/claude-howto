<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 功能目录

> 一份关于 Claude Code 所有功能的快速参考：命令、agents、skills、plugins 和 hooks。

**导航**: [命令](#斜杠命令) | [权限模式](#权限模式) | [Subagents](#subagents) | [Skills](#skills) | [Plugins](#plugins) | [MCP Servers](#mcp-servers) | [Hooks](#hooks) | [Memory](#memory-files) | [2026 年 3 月新功能](#2026-年-3-月新功能)

---

## 概览

| 功能 | 内置 | 示例 | 总数 | 参考 |
|---------|----------|----------|-------|-----------|
| **Slash Commands** | 55+ | 8 | 63+ | [01-slash-commands/README.md](01-slash-commands/README.md) |
| **Subagents** | 6 | 10 | 16 | [04-subagents/README.md](04-subagents/README.md) |
| **Skills** | 5 个内置 | 4 | 9 | [03-skills/README.md](03-skills/README.md) |
| **Plugins** | - | 3 | 3 | [07-plugins/README.md](07-plugins/README.md) |
| **MCP Servers** | 1 | 8 | 9 | [05-mcp/README.md](05-mcp/README.md) |
| **Hooks** | 25 个事件 | 7 | 7 | [06-hooks/README.md](06-hooks/README.md) |
| **Memory** | 7 种类型 | 3 | 3 | [02-memory/README.md](02-memory/README.md) |
| **总计** | **99** | **43** | **117** | |

---

## 斜杠命令

命令是用户手动触发的快捷操作，用来执行特定任务。

### 内置命令

| 命令 | 说明 | 适用场景 |
|---------|-------------|-------------|
| `/help` | 显示帮助信息 | 开始上手、学习命令 |
| `/btw` | 提出不写入上下文的插话问题 | 临时补充问题 |
| `/chrome` | 配置 Chrome 集成 | 浏览器自动化 |
| `/clear` | 清空对话历史 | 重新开始、减少上下文 |
| `/diff` | 交互式 diff 查看器 | 审查变更 |
| `/config` | 查看/编辑配置 | 自定义行为 |
| `/status` | 显示会话状态 | 检查当前状态 |
| `/agents` | 列出可用 agents | 查看委派选项 |
| `/skills` | 列出可用 skills | 查看可自动触发的能力 |
| `/hooks` | 列出已配置的 hooks | 调试自动化 |
| `/insights` | 分析会话模式 | 优化会话使用 |
| `/install-slack-app` | 安装 Claude Slack 应用 | Slack 集成 |
| `/keybindings` | 自定义键盘快捷键 | 按键定制 |
| `/mcp` | 列出 MCP servers | 检查外部集成 |
| `/memory` | 查看已加载的 memory 文件 | 调试上下文加载 |
| `/mobile` | 生成移动端二维码 | 手机访问 |
| `/passes` | 查看使用通行证 | 订阅信息 |
| `/plugin` | 管理 plugins | 安装/移除扩展 |
| `/plan` | 进入规划模式 | 复杂实现 |
| `/rewind` | 回退到 checkpoint | 撤销变更、探索替代方案 |
| `/checkpoint` | 管理 checkpoints | 保存/恢复状态 |
| `/cost` | 显示 token 消耗 | 监控开销 |
| `/context` | 显示上下文窗口使用情况 | 管理对话长度 |
| `/export` | 导出对话 | 保存以供参考 |
| `/extra-usage` | 配置额外用量限制 | 限流管理 |
| `/feedback` | 提交反馈或 bug 报告 | 报告问题 |
| `/login` | 通过 Anthropic 认证 | 访问功能 |
| `/logout` | 登出 | 切换账号 |
| `/sandbox` | 切换 sandbox 模式 | 安全执行命令 |
| `/vim` | 切换 vim 模式 | 类 Vim 编辑 |
| `/doctor` | 运行诊断 | 排查问题 |
| `/reload-plugins` | 重新加载已安装的 plugins | 插件管理 |
| `/release-notes` | 显示更新说明 | 查看新功能 |
| `/remote-control` | 启用远程控制 | 远程访问 |
| `/permissions` | 管理权限 | 控制访问 |
| `/session` | 管理会话 | 多会话工作流 |
| `/rename` | 重命名当前会话 | 组织会话 |
| `/resume` | 恢复之前的会话 | 继续工作 |
| `/todo` | 查看/管理待办列表 | 跟踪任务 |
| `/tasks` | 查看后台任务 | 监控异步操作 |
| `/copy` | 复制最后一次回复到剪贴板 | 快速分享输出 |
| `/teleport` | 将会话转移到另一台机器 | 远程继续工作 |
| `/desktop` | 打开 Claude Desktop 应用 | 切换桌面界面 |
| `/theme` | 更改颜色主题 | 自定义外观 |
| `/usage` | 显示 API 使用统计 | 监控配额和消耗 |
| `/fork` | 分叉当前对话 | 探索替代方案 |
| `/stats` | 显示会话统计 | 查看会话指标 |
| `/statusline` | 配置状态栏 | 自定义状态显示 |
| `/stickers` | 查看会话贴纸 | 趣味奖励 |
| `/fast` | 切换快速输出模式 | 加快响应 |
| `/terminal-setup` | 配置终端集成 | 设置终端特性 |
| `/upgrade` | 检查更新 | 版本管理 |

### 自定义命令（示例）

| 命令 | 说明 | 适用场景 | 作用域 | 安装 |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | 分析代码以做优化 | 性能改进 | 项目 | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | 准备 Pull Request | 提交 PR 前 | 项目 | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | 生成 API 文档 | 编写 API 文档 | 项目 | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | 结合上下文创建 git commit | 提交变更 | 用户 | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | 先暂存、提交再 push | 快速发布 | 用户 | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | 重构文档结构 | 改进文档 | 项目 | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | 搭建 CI/CD 流水线 | 新项目 | 项目 | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | 扩展测试覆盖率 | 改进测试 | 项目 | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **作用域**: `User` = 个人工作流（`~/.claude/commands/`），`Project` = 团队共享（`.claude/commands/`）

**参考**: [01-slash-commands/README.md](01-slash-commands/README.md) | [官方文档](https://code.claude.com/docs/en/interactive-mode)

**快速安装（所有自定义命令）**：
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## 权限模式

Claude Code 提供 6 种权限模式，用来控制工具调用如何被授权。

| 模式 | 说明 | 适用场景 |
|------|-------------|-------------|
| `default` | 每次工具调用都询问 | 标准交互式使用 |
| `acceptEdits` | 自动接受文件编辑，其他情况仍询问 | 可信编辑工作流 |
| `plan` | 只允许只读工具，不允许写入 | 规划与探索 |
| `auto` | 不再提示，自动接受所有工具 | 完全自主运行（Research Preview） |
| `bypassPermissions` | 跳过所有权限检查 | CI/CD、无头环境 |
| `dontAsk` | 跳过需要权限的工具 | 非交互脚本 |

> **注意**：`auto` 模式是 Research Preview 功能（2026 年 3 月）。只有在可信且已隔离的环境中才使用 `bypassPermissions`。

**参考**: [官方文档](https://code.claude.com/docs/en/permissions)

---

## Subagents

为特定任务准备的专门化 AI 助手，拥有隔离上下文。

### 内置 Subagents

| Agent | 说明 | 工具 | 模型 | 适用场景 |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | 多步任务、研究 | 所有工具 | 继承当前模型 | 复杂研究、多文件任务 |
| **Plan** | 实现规划 | Read、Glob、Grep、Bash | 继承当前模型 | 架构设计、规划 |
| **Explore** | 代码库探索 | Read、Glob、Grep | Haiku 4.5 | 快速搜索、理解代码 |
| **Bash** | 命令执行 | Bash | 继承当前模型 | git 操作、终端任务 |
| **statusline-setup** | 状态栏配置 | Bash、Read、Write | Sonnet 4.6 | 配置状态栏显示 |
| **Claude Code Guide** | 帮助与文档 | Read、Glob、Grep | Haiku 4.5 | 获取帮助、学习功能 |

### Subagent 配置字段

| 字段 | 类型 | 说明 |
|-------|------|-------------|
| `name` | string | agent 标识 |
| `description` | string | 这个 agent 的用途 |
| `model` | string | 模型覆盖值（例如 `haiku-4.5`） |
| `tools` | array | 允许使用的工具列表 |
| `effort` | string | 推理强度等级（`low`、`medium`、`high`） |
| `initialPrompt` | string | agent 启动时注入的 system prompt |
| `disallowedTools` | array | 明确禁止该 agent 使用的工具 |

### 自定义 Subagents（示例）

| Agent | 说明 | 适用场景 | 作用域 | 安装 |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | 全面的代码质量检查 | 代码审查会话 | 项目 | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | 功能架构设计 | 新功能规划 | 项目 | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | 深入分析代码库 | 理解已有功能 | 项目 | `cp 04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | 按 Clean Code 原则审查 | 可维护性审查 | 项目 | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | 测试策略与覆盖率 | 测试规划 | 项目 | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | 技术文档编写 | API 文档、指南 | 项目 | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | 面向安全的审查 | 安全审计 | 项目 | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | 完整功能实现 | 功能开发 | 项目 | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | 根因分析 | Bug 调查 | 用户 | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL 查询、数据分析 | 数据任务 | 用户 | `cp 04-subagents/data-scientist.md .claude/agents/` |

> **作用域**: `User` = 个人（`~/.claude/agents/`），`Project` = 团队共享（`.claude/agents/`）

**参考**: [04-subagents/README.md](04-subagents/README.md) | [官方文档](https://code.claude.com/docs/en/sub-agents)

**快速安装（所有自定义 agents）**：
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## Skills

可自动触发的能力包，包含说明、脚本和模板。

### 示例 Skills

| Skill | 说明 | 何时自动触发 | 作用域 | 安装 |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | 全面的代码审查 | “Review this code”, “Check quality” | 项目 | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | 品牌一致性检查器 | 编写营销文案时 | 项目 | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | API 文档生成器 | “Generate docs”, “Document API” | 项目 | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | 系统化代码重构（Martin Fowler） | “Refactor this”, “Clean up code” | 用户 | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **作用域**: `User` = 个人（`~/.claude/skills/`），`Project` = 团队共享（`.claude/skills/`）

### Skill 结构

```
~/.claude/skills/skill-name/
├── SKILL.md          # skill 定义与说明
├── scripts/          # 辅助脚本
└── templates/        # 输出模板
```

### Skill Frontmatter 字段

Skills 支持在 `SKILL.md` 中使用 YAML frontmatter 进行配置：

| 字段 | 类型 | 说明 |
|-------|------|-------------|
| `name` | string | skill 显示名称 |
| `description` | string | 这个 skill 的作用 |
| `autoInvoke` | array | 自动触发的关键词 |
| `effort` | string | 推理强度等级（`low`、`medium`、`high`） |
| `shell` | string | 脚本使用的 shell（`bash`、`zsh`、`sh`） |

**参考**: [03-skills/README.md](03-skills/README.md) | [官方文档](https://code.claude.com/docs/en/skills)

**快速安装（所有 skills）**：
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### 内置 Skills

| Skill | 说明 | 何时自动触发 |
|-------|-------------|-------------------|
| `/simplify` | 审查代码质量 | 写完代码后 |
| `/batch` | 对多个文件运行提示词 | 批量操作 |
| `/debug` | 调试失败的测试/错误 | 调试会话 |
| `/loop` | 按间隔运行提示词 | 周期性任务 |
| `/claude-api` | 使用 Claude API 构建应用 | API 开发 |

---

## Plugins

把 commands、agents、MCP servers 和 hooks 打包在一起的集合。

### 示例 Plugins

| Plugin | 说明 | 组件 | 适用场景 | 作用域 | 安装 |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | PR 审查工作流 | 3 个 commands、3 个 agents、GitHub MCP | 代码审查 | 项目 | `/plugin install pr-review` |
| `devops-automation` | 部署与监控 | 4 个 commands、3 个 agents、K8s MCP | DevOps 任务 | 项目 | `/plugin install devops-automation` |
| `documentation` | 文档生成套件 | 4 个 commands、3 个 agents、模板 | 文档编写 | 项目 | `/plugin install documentation` |

> **作用域**: `Project` = 团队共享，`User` = 个人工作流

### Plugin 结构

```
.claude-plugin/
├── plugin.json       # manifest 文件
├── commands/         # Slash commands
├── agents/           # Subagents
├── skills/           # Skills
├── mcp/              # MCP 配置
├── hooks/            # Hook 脚本
└── scripts/          # 工具脚本
```

**参考**: [07-plugins/README.md](07-plugins/README.md) | [官方文档](https://code.claude.com/docs/en/plugins)

**Plugin 管理命令**：
```bash
/plugin list              # 列出已安装的 plugins
/plugin install <name>    # 安装 plugin
/plugin remove <name>     # 移除 plugin
/plugin update <name>     # 更新 plugin
```

---

## MCP Servers

用于访问外部工具和 API 的 Model Context Protocol servers。

### 常见 MCP Servers

| Server | 说明 | 适用场景 | 作用域 | 安装 |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | PR 管理、issues、代码 | GitHub 工作流 | 项目 | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL 查询、数据访问 | 数据库操作 | 项目 | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | 高级文件操作 | 复杂文件任务 | 用户 | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | 团队沟通 | 通知、更新 | 项目 | 在设置中配置 |
| **Google Docs** | 文档访问 | 文档编辑、审阅 | 项目 | 在设置中配置 |
| **Asana** | 项目管理 | 任务跟踪 | 项目 | 在设置中配置 |
| **Stripe** | 支付数据 | 财务分析 | 项目 | 在设置中配置 |
| **Memory** | 持久记忆 | 跨会话回忆 | 用户 | 在设置中配置 |
| **Context7** | 库文档 | 查找最新文档 | 内置 | 内置 |

> **作用域**: `Project` = 团队（`.mcp.json`），`User` = 个人（`~/.claude.json`），`Built-in` = 预装

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

**参考**: [05-mcp/README.md](05-mcp/README.md) | [MCP 协议文档](https://modelcontextprotocol.io)

**快速安装（GitHub MCP）**：
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## Hooks

在 Claude Code 事件发生时执行的事件驱动自动化。

### Hook 事件

| 事件 | 说明 | 触发时机 | 使用场景 |
|-------|-------------|----------------|-----------|
| `SessionStart` | 会话开始/恢复 | 会话初始化 | 初始化任务 |
| `InstructionsLoaded` | 指令已加载 | `CLAUDE.md` 或规则文件加载 | 自定义指令处理 |
| `UserPromptSubmit` | 提示词提交前 | 用户发送消息 | 输入校验 |
| `PreToolUse` | 工具执行前 | 任意工具运行之前 | 校验、日志 |
| `PermissionRequest` | 显示权限对话框 | 敏感操作前 | 自定义审批流程 |
| `PostToolUse` | 工具成功后 | 任意工具完成后 | 格式化、通知 |
| `PostToolUseFailure` | 工具执行失败 | 工具报错后 | 错误处理、日志 |
| `Notification` | 发送通知时 | Claude 发送通知 | 外部提醒 |
| `SubagentStart` | 启动 subagent | subagent 任务开始 | 初始化上下文 |
| `SubagentStop` | subagent 完成 | subagent 任务结束 | 链式动作 |
| `Stop` | Claude 完成响应 | 响应完成 | 清理、汇报 |
| `StopFailure` | API 错误导致结束 | API 错误发生 | 错误恢复、日志 |
| `TeammateIdle` | 队友 agent 空闲 | agent team 协调 | 分配工作 |
| `TaskCompleted` | 任务标记完成 | 任务完成 | 任务后处理 |
| `TaskCreated` | 通过 TaskCreate 创建任务 | 新任务创建 | 任务追踪、日志 |
| `ConfigChange` | 配置更新 | 设置被修改 | 响应配置变化 |
| `CwdChanged` | 当前工作目录变化 | 目录切换 | 目录级初始化 |
| `FileChanged` | 监控文件发生变化 | 文件被修改 | 文件监控、重建 |
| `PreCompact` | 压缩前 | 上下文压缩前 | 状态保留 |
| `PostCompact` | 压缩完成后 | 压缩完成 | 压缩后动作 |
| `WorktreeCreate` | worktree 创建中 | git worktree 创建 | 设置 worktree 环境 |
| `WorktreeRemove` | worktree 被移除 | git worktree 删除 | 清理 worktree 资源 |
| `Elicitation` | MCP server 请求输入 | MCP elicitation | 输入校验 |
| `ElicitationResult` | 用户响应 elicitation | 用户回答 | 响应处理 |
| `SessionEnd` | 会话结束 | 会话终止 | 清理、保存状态 |

### 示例 Hooks

| Hook | 说明 | 事件 | 作用域 | 安装 |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | 命令校验 | PreToolUse:Bash | 项目 | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | 安全扫描 | PostToolUse:Write | 项目 | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | 自动格式化 | PostToolUse:Write | 用户 | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | 提示词校验 | UserPromptSubmit | 项目 | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | token 使用跟踪 | Stop | 用户 | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | 提交前校验 | PreToolUse:Bash | 项目 | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | 命令日志记录 | PostToolUse:Bash | 用户 | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |

> **作用域**: `Project` = 团队（`.claude/settings.json`），`User` = 个人（`~/.claude/settings.json`）

### Hook 配置

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

**参考**: [06-hooks/README.md](06-hooks/README.md) | [官方文档](https://code.claude.com/docs/en/hooks)

**快速安装（所有 hooks）**：
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## Memory Files

会在多个会话之间自动加载的持久上下文。

### Memory 类型

| 类型 | 位置 | 作用域 | 适用场景 |
|------|----------|-------|-------------|
| **Managed Policy** | 组织管理的策略 | Organization | 统一组织标准 |
| **Project** | `./CLAUDE.md` | Project（团队） | 团队规范、项目上下文 |
| **Project Rules** | `.claude/rules/` | Project（团队） | 模块化项目规则 |
| **User** | `~/.claude/CLAUDE.md` | User（个人） | 个人偏好 |
| **User Rules** | `~/.claude/rules/` | User（个人） | 模块化个人规则 |
| **Local** | `./CLAUDE.local.md` | Local（git 忽略） | 机器特定覆盖（截至 2026 年 3 月不在官方文档中，可能是历史遗留） |
| **Auto Memory** | 自动 | Session | 自动捕捉的洞察和修正 |

> **作用域**: `Organization` = 管理员管理，`Project` = 通过 git 与团队共享，`User` = 个人偏好，`Local` = 不提交，`Session` = 自动管理

**参考**: [02-memory/README.md](02-memory/README.md) | [官方文档](https://code.claude.com/docs/en/memory)

**快速安装**：
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## 2026 年 3 月新功能

| 功能 | 说明 | 使用方式 |
|---------|-------------|------------|
| **Remote Control** | 通过 API 远程控制 Claude Code 会话 | 使用远程控制 API 以编程方式发送提示并接收响应 |
| **Web Sessions** | 在浏览器环境中运行 Claude Code | 通过 `claude web` 或 Anthropic Console 访问 |
| **Desktop App** | Claude Code 的原生桌面应用 | 使用 `/desktop` 或从 Anthropic 网站下载 |
| **Agent Teams** | 协调多个 agent 共同处理相关任务 | 配置协作并共享上下文的 teammate agents |
| **Task List** | 后台任务管理与监控 | 使用 `/tasks` 查看和管理后台操作 |
| **Prompt Suggestions** | 上下文感知的命令建议 | 根据当前上下文自动出现建议 |
| **Git Worktrees** | 用于并行开发的隔离 git worktree | 使用 worktree 命令进行安全的并行分支工作 |
| **Sandboxing** | 安全隔离的执行环境 | 使用 `/sandbox` 切换，在受限环境中运行命令 |
| **MCP OAuth** | 为 MCP servers 提供 OAuth 认证 | 在 MCP server 设置中配置 OAuth 凭据以安全访问 |
| **MCP Tool Search** | 动态搜索和发现 MCP 工具 | 使用工具搜索查找已连接 server 上可用的 MCP 工具 |
| **Scheduled Tasks** | 使用 `/loop` 和 cron 工具设置周期任务 | 使用 `/loop 5m /command` 或 CronCreate 工具 |
| **Chrome Integration** | 使用无头 Chromium 做浏览器自动化 | 使用 `--chrome` 标志或 `/chrome` 命令 |
| **Keyboard Customization** | 自定义按键映射并支持 chord | 使用 `/keybindings` 或编辑 `~/.claude/keybindings.json` |
| **自动模式（Auto Mode）** | 无需权限提示的完全自主运行（Research Preview） | 使用 `--mode auto` 或 `/permissions auto`；2026 年 3 月 |
| **通道（Channels）** | 多通道通信（Telegram、Slack 等）（Research Preview） | 配置 channel plugins；2026 年 3 月 |
| **语音输入（Voice Dictation）** | 用语音输入提示词 | 使用麦克风图标或语音快捷键 |
| **Agent Hook Type** | 触发 subagent 而不是执行 shell 命令的 hook | 在 hook 配置中设置 `"type": "agent"` |
| **Prompt Hook Type** | 将 prompt 文本注入对话的 hook | 在 hook 配置中设置 `"type": "prompt"` |
| **MCP Elicitation** | MCP servers 可在工具执行期间请求用户输入 | 通过 `Elicitation` 和 `ElicitationResult` hook 事件处理 |
| **WebSocket MCP Transport** | 用 WebSocket 连接 MCP server | 在 MCP server 配置中使用 `"transport": "websocket"` |
| **Plugin LSP Support** | 通过 plugins 集成 Language Server Protocol | 在 `plugin.json` 中配置 LSP servers，以获得编辑器能力 |
| **Managed Drop-ins** | 组织管理的 drop-in 配置（v2.1.83） | 通过 managed policies 由管理员配置，自动应用到所有用户 |

---

## 快速参考矩阵

### 功能选择指南

| 需求 | 推荐功能 | 原因 |
|------|---------------------|-----|
| 快捷命令 | Slash Command | 手动、立即执行 |
| 持久上下文 | Memory | 自动加载 |
| 复杂自动化 | Skill | 自动触发 |
| 专门任务 | Subagent | 隔离上下文 |
| 外部数据 | MCP Server | 实时访问 |
| 事件自动化 | Hook | 事件触发 |
| 完整解决方案 | Plugin | 一体化打包 |

### 安装优先级

| 优先级 | 功能 | 命令 |
|----------|---------|---------|
| 1. 必装 | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. 日常使用 | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. 质量提升 | Subagents | `cp 04-subagents/*.md .claude/agents/` |
| 4. 自动化 | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/` |
| 5. 集成 | MCP Servers | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. 全量打包 | Plugins | `/plugin install <name>` |

---

## 一条命令完成安装

```bash
# 创建目录
mkdir -p .claude/commands .claude/agents ~/.claude/hooks ~/.claude/skills

# 安装所有功能
cp 01-slash-commands/*.md .claude/commands/
cp 04-subagents/*.md .claude/agents/
cp -r 03-skills/* ~/.claude/skills/
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 配置 MCP
export GITHUB_TOKEN="your_token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 使用 Plugins
/plugin install pr-review
/plugin install devops-automation
```

---

## 其他资源

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - 现成 skills 集合
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) - Claude Code 的创造者分享了他的系统化工作流：并行 agents、共享 `CLAUDE.md`、Plan mode、slash commands、subagents，以及用于长时间自主会话的验证 hooks。
