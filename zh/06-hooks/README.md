<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks

Hooks（钩子）是在 Claude Code 会话期间响应特定事件而自动执行的脚本。它们支持自动化、校验、权限管理和自定义工作流。

## 概览

Hooks 是自动化动作（shell 命令、HTTP webhook、LLM 提示词、MCP 工具调用或子代理评估），在 Claude Code 中发生特定事件时自动执行。它们接收 JSON 输入，并通过退出码和 JSON 输出传递结果。

**核心特性：**
- 事件驱动的自动化
- 基于 JSON 的输入/输出
- 支持 `command`、`http`、`mcp_tool`、`prompt` 和 `agent` 五种 hook 类型
- 面向特定工具的 hook 支持模式匹配

## 配置

Hooks 在 settings 文件中以特定结构配置：

- `~/.claude/settings.json` - 用户设置（所有项目）
- `.claude/settings.json` - 项目设置（可共享、可提交）
- `.claude/settings.local.json` - 本地项目设置（不提交）
- 托管策略 - 组织级设置
- 插件 `hooks/hooks.json` - 插件作用域的 hooks
- Skill/Agent frontmatter - 组件生命周期 hooks

### 基本配置结构

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**关键字段：**

| 字段 | 说明 | 示例 |
|-------|-------------|---------|
| `matcher` | 匹配工具名称的模式（区分大小写） | `"Write"`、`"Edit\|Write"`、`"*"` |
| `hooks` | hook 定义数组 | `[{ "type": "command", ... }]` |
| `type` | hook 类型：`"command"`（bash）、`"prompt"`（LLM）、`"http"`（webhook）、`"mcp_tool"`（MCP 工具调用，v2.1.118+）或 `"agent"`（子代理） | `"command"` |
| `command` | 要执行的 shell 命令 | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | 可选的超时时间（秒）。默认值：command/http/mcp_tool 为 600，prompt 为 30，agent 为 60。对于 prompt 和 agent hook，小于 1 的值按 1 秒计（v2.1.312+）。 | `30` |
| `once` | 若为 `true`，该 hook 在第一次成功运行后被移除（失败/被阻止/超时的运行会保留它）。仅限 Skill frontmatter；在 settings 和 agent frontmatter 中被忽略 | `true` |
| `async` | 若为 `true`，在后台运行且不阻塞 | `true` |
| `asyncRewake` | 若为 `true`，在后台运行并在退出码为 2 时唤醒 Claude。隐含 `async`。 | `true` |
| `shell` | 接受 `"bash"` 或 `"powershell"`。默认为 `"bash"`；在未安装 Git Bash 的 Windows 上默认为 `"powershell"`。PowerShell hook 的退出码 2 自 v2.1.309 起才能产生阻塞；依赖 PowerShell 守卫 hook 前请先升级。 | `"bash"` |
| `statusMessage` | hook 运行期间显示的自定义加载提示消息 | `"Formatting…"` |
| `onFailure` | 当 command 或 HTTP hook 失败（无法启动、超时、以非预期退出码退出）时对动作的处理方式：`"continue"`（默认）或 `"block"`（v2.1.295+）。Agent SDK 的 hook 回调通过在 matcher 上设置该项来生效：TypeScript（Agent SDK v0.3.317+）中为 `onFailure: "block"`，Python（v0.2.177+）中为 `on_failure="block"`，表示回调失败时阻止动作，而不是放行。 | `"block"` |

> **注意**：部分事件会降低默认超时。`UserPromptSubmit` 将 `command`、`http` 和 `mcp_tool` 的默认值降为 30 秒，`MessageDisplay` 降为 10 秒。`SessionEnd` hook 共享 1.5 秒的预算；如果你的设置中为单个 hook 配置了更长的 `timeout`，Claude Code 会将该预算相应上调，上限 60 秒。在 `claude -p` 和 Agent SDK 会话中，hook 运行较久时 Claude Code 每 30 秒发送一次进度心跳（v2.1.323），因此包含该版本后，Claude Desktop 等宿主不会把这一轮当作挂起而结束。

### Matcher 模式

| 模式 | 说明 | 示例 |
|---------|-------------|---------|
| 精确字符串 | 匹配特定工具 | `"Write"` |
| 正则模式 | 匹配多个工具 | `"Edit\|Write"` |
| 逗号分隔 | 匹配列表中的任意工具（v2.1.191+） | `"Write,Edit"` |
| 通配符 | 匹配所有工具 | `"*"` 或 `""` |
| MCP 工具 | 服务器与工具模式 | `"mcp__memory__.*"` |

> **Matcher 自 v2.1.195 起按精确匹配。** 带连字符的标识符（例如含连字符的 MCP 工具名）不再意外地以子串方式匹配到另一个工具。像 `"Write,Edit"` 这样的逗号分隔 matcher 会对列表中的任意工具触发——更早的版本会让它们静默地永不触发。

**InstructionsLoaded 的 matcher 取值：**

| Matcher 取值 | 说明 |
|---------------|-------------|
| `session_start` | 会话启动时加载的指令 |
| `nested_traversal` | 嵌套目录遍历时加载的指令 |
| `path_glob_match` | 通过路径 glob 模式匹配加载的指令 |

### 使用 `if` 条件收窄范围（工具参数路径）

`matcher` 字段按**工具名称**选择 hook（`"Write"`、`"Edit|Write"`、`"*"`）。要在**工具参数**层面做更细的过滤——例如只在编辑触及 `src/` 时运行 hook，或拦截对密钥文件的读取——可以在单个 hook handler 上添加 `if` 条件。它与工具名 matcher 的分工是：`matcher` 决定*哪个工具*，`if` 决定*哪一次调用*。

`if` 使用[权限规则语法](https://code.claude.com/docs/en/permissions)（`ToolName(pattern)`），针对工具名称**和**其参数一起求值。对 `Read`/`Edit`/`Write`，路径模式遵循 gitignore 语义，锚点与权限规则相同：裸名称如 `.env` 在任意深度匹配，`src/**` 相对于当前目录，`/src/**` 相对于项目根，`~/...` 相对于你的主目录，`//...` 是绝对文件系统路径。

`if` 字段位于 **hook handler 层级**——它是 `type` 和 `command` 的同级字段，位于 `hooks` 数组内——而不是放在 `matcher` 上：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "if": "Edit(src/**)",
            "command": "./hooks/lint-src.sh"
          }
        ]
      },
      {
        "matcher": "Read",
        "hooks": [
          {
            "type": "command",
            "if": "Read(.env)",
            "command": "./hooks/block-secret-read.sh"
          }
        ]
      }
    ]
  }
}
```

有效的 `if` 模式示例：`Edit(src/**)`（`src/` 下的编辑）、`Read(~/.ssh/**)`（读取任意 SSH 密钥）、`Read(.env)`（当前目录及以下的任意 `.env`）、`Bash(git push *)`（仅 `git push` 子命令）。

> **v2.1.214 更新**：hook `if` 条件中的单段 `dir/**` 模式（如 `Edit(src/**)`）现在只匹配 `<cwd>/dir`——不再匹配树中任意深度的该目录。之前 `src/**` 也会匹配 `foo/src/**`。若需要任意深度匹配，请使用 `**/dir/**`。**重要**：这一收窄只适用于 hook 的 `if:` 条件和允许规则的自动批准——deny/ask 权限规则仍然在任意深度匹配 `dir/**`。

> **v2.1.314 更新**：诸如 `Monitor(tail *)` 的 `if` 模式会匹配 Monitor 工具启动的 shell 命令，方式与 `Bash(tail *)` 匹配 Bash 的命令相同。matcher 为 `Bash` 的 hook 也会在 Monitor 的 shell 命令上运行；它们可以阻止或请求确认，但不能批准或重写这些命令。

## Hook 类型

Claude Code 支持五种 hook 类型：

### Command Hooks

默认的 hook 类型。执行 shell 命令，通过 JSON stdin/stdout 和退出码通信。

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

#### Exec 形式（`args`）

> v2.1.139 新增。

除了 shell 形式的 `"command": "..."`，command hook 还可以通过 `args` 数组用 `execve()` 直接启动一个二进制程序。没有 shell 解析，因此路径占位符不需要加引号，配置对 shell 注入类 bug 免疫。

```json
{
  "type": "command",
  "command": "python3",
  "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/validate.py", "--strict"],
  "timeout": 60
}
```

`command` 始终是必需的：设置 `args` 时，`command` 是要启动的可执行文件（从 `PATH` 解析），`args` 是其参数向量。需要管道、重定向、`&&` 链接或 shell 展开时使用 shell 形式（省略 `args`）；调用单个二进制程序加参数时使用 `args`。

### HTTP Hooks

> v2.1.63 新增。

远程 webhook 端点，接收与 command hook 相同的 JSON 输入。HTTP hook 向该 URL POST JSON 并接收 JSON 响应。启用沙箱时，HTTP hook 经由沙箱路由。出于安全考虑，header 值中的环境变量插值需要显式的 `allowedEnvVars` 列表。

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": [{
        "type": "http",
        "url": "https://my-webhook.example.com/hook"
      }]
    }]
  }
}
```

**关键属性：**
- `"type": "http"` -- 标识这是一个 HTTP hook
- `"url"` -- webhook 端点 URL
- 启用沙箱时经沙箱路由
- `headers` 值中的任何环境变量插值都需要显式的 `allowedEnvVars` 列表

### Prompt Hooks

由 LLM 评估的提示词，hook 内容是一个由 Claude 评估的 prompt。主要与 `Stop` 和 `SubagentStop` 事件配合，用于智能的任务完成检查。

```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude completed all requested tasks.",
  "timeout": 30
}
```

LLM 评估该 prompt 并返回结构化决策（详见 [基于 Prompt 的 Hooks](#基于-prompt-的-hooks)）。

### MCP Tool Hooks

> v2.1.118 新增。

`mcp_tool` 类型直接调用一个已配置的 MCP 工具；配置引用 MCP 服务器和工具名，而不是 shell 命令或 URL。当校验或反应逻辑已经存在于你配置的某个 MCP 服务器中时，这非常有用。

```json
{
  "matcher": "Edit",
  "hooks": [{
    "type": "mcp_tool",
    "server": "my-mcp-server",
    "tool": "validate_edit",
    "input": { "file_path": "${tool_input.file_path}" }
  }]
}
```

**关键属性：**
- `"type": "mcp_tool"` -- 标识这是一个 MCP 工具 hook
- `"server"` -- 已配置的 MCP 服务器名称
- `"tool"` -- 要调用的该服务器上的工具名
- `"input"` -- 传给工具的可选参数；字符串值支持来自 hook JSON 输入的 `${path}` 替换，例如 `"${tool_input.file_path}"`

工具的参数来自 `input`（带 `${path}` 替换），而不是直接来自 hook 输入。配置 MCP 服务器见 [MCP 服务器配置](../05-mcp/README.md)。如果 Claude Code 无法读取工具的答案（例如来自 stdio 或 HTTP 服务器的超过 16 MiB 的答案），`PreToolUse` 的 `mcp_tool` hook 不会给出裁决，该工具调用将被拒绝（v2.1.321；更早的版本会跳过该 hook）。

### Agent Hooks

基于子代理的验证 hook，会启动一个专用 agent 来评估条件或执行复杂检查。与 prompt hook（单轮 LLM 评估）不同，agent hook 可以使用工具并进行多步推理。

> **注意**：Agent hook 是实验性功能，可能会有变化。

> **注意**：自 v2.1.280 起，agent hook 不再在 `PermissionRequest` 上运行——它的答案无法允许或拒绝该请求。在该事件上请使用返回决策对象的 command 或 HTTP hook（prompt hook 的 `ok: false` 对 `PermissionRequest` 无效）。

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

**关键属性：**
- `"type": "agent"` -- 标识这是一个 agent hook
- `"prompt"` -- 给子代理的任务描述
- agent 可以使用工具（Read、Grep、Bash 等）执行评估
- 返回与 prompt hook 类似的结构化决策

## Hook 事件

Claude Code 支持 **33 种 hook 事件**：

| 事件 | 触发时机 | Matcher 输入 | 可否阻止 | 常见用途 |
|-------|---------------|---------------|-----------|------------|
| **SessionStart** | 会话开始/恢复/清除/压缩 | startup/resume/clear/compact/fork | 否 | 环境准备 |
| **Setup** | `--init-only`，或配合 `-p` 的 `--init`/`--maintenance`（CI/脚本准备） | `init`/`maintenance` | 否 | 配置工具链、安装依赖 |
| **InstructionsLoaded** | CLAUDE.md 或规则文件加载后 | 加载原因（`session_start`/`nested_traversal`/`path_glob_match`/`include`/`compact`） | 否 | 审计/可观测性日志 |
| **UserPromptSubmit** | 用户提交 prompt | （无） | 是 | 校验 prompt |
| **UserPromptExpansion** | 用户输入的斜杠命令或 MCP prompt 展开为 prompt 时 | 命令名 | 是 | 转换或检查展开后的 prompt |
| **PreToolUse** | 工具执行前 | 工具名 | 是（allow/deny/ask/defer） | 校验、修改输入 |
| **PermissionRequest** | 权限对话框弹出时 | 工具名 | 是 | 自动批准/拒绝 |
| **PermissionDenied** | 自动模式拒绝某次工具调用时 | 工具名 | 否 | 日志、分析、策略执行 |
| **PostToolUse** | 工具成功完成后 | 工具名 | 否 | 补充上下文、反馈 |
| **PostToolUseFailure** | 工具执行失败时 | 工具名 | 否 | 错误处理、日志 |
| **PostToolBatch** | 一批工具使用完成后 | （无） | 是 | 聚合报告、批量校验 |
| **Notification** | 发送通知时 | 通知类型 | 否 | 自定义通知 |
| **MessageDisplay** | 助手消息文本显示时 | （无） | 否 | 转换或隐藏显示的消息文本（v2.1.152） |
| **SubagentStart** | 子代理被启动时 | Agent 类型名 | 否 | 子代理初始化 |
| **SubagentStop** | 子代理结束时 | Agent 类型名 | 是 | 子代理校验 |
| **Stop** | Claude 完成响应时 | （无） | 是 | 任务完成检查 |
| **StopFailure** | API 错误结束回合时 | 错误类型（`rate_limit`、`overloaded`、`server_error` 等） | 否 | 错误恢复、日志 |
| **TeammateIdle** | Agent 团队成员空闲时 | （无） | 是 | 团队成员协调 |
| **TaskCompleted** | 任务被标记完成时 | （无） | 是 | 任务后处理动作 |
| **TaskCreated** | 通过 TaskCreate 创建任务时 | （无） | 是 | 任务跟踪、日志 |
| **ConfigChange** | 配置文件变更时 | 配置来源（`user_settings`/`project_settings`/`local_settings`/`policy_settings`/`skills`） | 是（policy 除外） | 响应配置更新 |
| **CwdChanged** | 工作目录变更时 | （无） | 否 | 目录相关设置 |
| **DirectoryAdded** | 会话中途通过 `/add-dir` 或 SDK 的 `register_repo_root` 控制请求注册新工作目录时（v2.1.219） | `slash_command`/`register_repo_root` | 否 | 为新加入的目录配置工具 |
| **FileChanged** | 被监视的文件变更时 | 要监视的文件名（如 `.envrc\|.env`） | 否 | 文件监视、重新构建 |
| **PreCompact** | 上下文压缩前 | manual/auto | 是 | 压缩前动作 |
| **PostCompact** | 压缩完成后 | （无） | 否 | 压缩后动作 |
| **PreModelSwitch** | Claude Code 应用请求的模型切换前 | 被切换到的模型的规范名（来自 `to_model`） | 是 | 门禁或否决模型变更 |
| **PostModelSwitch** | 会话模型变更后，包括 Claude Code 自行做出的变更（如恢复会话时还原模型） | 被切换到的模型的规范名（来自 `to_model`） | 否 | 记录或响应模型变更 |
| **WorktreeCreate** | 正在创建 worktree 时 | （无） | 是（路径返回值） | worktree 初始化 |
| **WorktreeRemove** | 正在移除 worktree 时 | （无） | 是（非零退出码使移除失败） | worktree 清理 |
| **Elicitation** | MCP 服务器请求用户输入时 | MCP 服务器名 | 是 | 输入校验 |
| **ElicitationResult** | 用户响应 elicitation 时 | MCP 服务器名 | 是 | 响应处理 |
| **SessionEnd** | 会话终止时 | 结束原因（`clear`/`resume`/`logout`/`prompt_input_exit`/`other`） | 否 | 清理、最终日志 |

`PreModelSwitch` 和 `PostModelSwitch` 需要 v2.1.251 或更高版本。两者都接收 `from_model` 和 `to_model`；matcher 针对 `to_model` 派生的规范名求值（例如 `claude-opus-5`、`.*opus.*`）。它们的 `command`、`http` 和 `mcp_tool` 超时默认值降为 30 秒。

> **`TaskCreated` 和 `TaskCompleted` 需要启用 todo 工具（v2.1.233）。** 这两个事件由 todo/任务跟踪工具（`TaskCreate`/`Get`/`Update`/`List`、`TodoWrite`）触发，这些工具**默认仅在 Claude 3.x 模型、Opus 4 至 4.7、Sonnet 4 至 4.6 以及 Haiku 4.5 上可用**。在其他模型上这些 hook 仍是合法配置，只是永远不会触发——没有输出也没有报错。设置 `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` 可以恢复这些工具，从而恢复这些事件。

> **PostToolUse 时长（v2.1.119）：** `PostToolUse` 和 `PostToolUseFailure` 的 hook 输入现在包含 `duration_ms`——详见 [PostToolUse](#posttooluse) 一节。

### PreToolUse

在 Claude 生成工具参数之后、处理之前运行。用它来校验或修改工具输入。

**配置：**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py"
          }
        ]
      }
    ]
  }
}
```

**常用 matcher：** `Agent`、`Bash`、`Glob`、`Grep`、`Read`、`Edit`、`Write`、`WebFetch`、`WebSearch`

**输出控制：**
- `permissionDecision`：`"allow"`、`"deny"`、`"ask"` 或 `"defer"`
  - `"allow"` 跳过权限提示（需要用户交互的工具，以及组织设为 `ask` 的连接器工具除外）
  - `"deny"` 阻止该工具调用
  - `"ask"` 提示用户确认；提示中会注明该 hook 来自哪个插件或 skill（v2.1.301）。在自动模式下，调用会进入确认提示而不是分类器——例外是分类器仍然可以拒绝 Claude Code 自身检查标记的调用（受保护路径、未沙箱化的重试），且 `SubagentHandback` 调用不经提示直接运行——返回 `"deny"` 可阻止一次
  - `"defer"` 结束当前回合，以便稍后恢复执行该工具；仅在配合 `-p` 的非交互模式下有效，且仅当 Claude 在该回合只做了一次工具调用时有效（交互式会话记录警告并忽略）；结果携带 `stop_reason: "tool_deferred"`。对该取值，`permissionDecisionReason`、`updatedInput` 和 `additionalContext` 都会被忽略。无法兑现的 `defer` 不再吞掉另一个 hook 的 `ask`（v2.1.321）。如果恢复时被推迟调用的工具已不存在（`stop_reason: "tool_deferred_unavailable"`），调用保持挂起且运行以退出码 1 结束（v2.1.319）；要丢弃它，请带上 `CLAUDE_CODE_DROP_UNAVAILABLE_DEFERRED_TOOL=1` 并附带 prompt 恢复运行。
  - 无论 hook 返回什么，deny 和 ask 规则仍会被评估。当多个 `PreToolUse` hook 意见不一致时，优先级为 `deny` > `defer` > `ask` > `allow`
- `permissionDecisionReason`：决策说明。`"ask"` 时展示给用户（不给 Claude）；`"deny"` 时展示给 Claude；`"allow"` 和 `"defer"` 时只写入调试日志
- `updatedInput`：替换后的工具输入（整体替换输入对象）。自 v2.1.300 起，它像 Claude 自己的输入一样接受校验——未知键会被丢弃，工具拒绝的输入会导致调用被拒绝。当多个 `PreToolUse` hook 对同一次调用都返回 `updatedInput` 时，Claude Code 不会合并这些改写，也不保证工具最终使用哪一个，因此请让每个工具的输入只由一个 hook 改写。

### PostToolUse

工具完成后立即运行。自 v2.1.319 起，如果用 `Ctrl+Enter` 发送的消息在工具运行中结束回合、随后工具完成，`PostToolUse` hook 仍会在其结果上运行，并有 10 秒时间完成（更久的工作请使用 `async: true`）；`Esc` 会取消它们。用于验证、记录日志或向 Claude 提供上下文。

**配置：**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py"
          }
        ]
      }
    ]
  }
}
```

**输出控制：**
- `"block"` 决策会携带反馈提示 Claude
- `additionalContext`：为 Claude 补充的上下文

**附加输入字段（v2.1.119）：**

| 字段 | 类型 | 说明 |
|-------|------|-------------|
| `duration_ms` | number | 工具执行耗时（毫秒）。不含权限提示和 PreToolUse hook 执行所耗时间。在 `PostToolUse` 和 `PostToolUseFailure` hook 上都可用。 |

#### 可恢复的阻止（`continueOnBlock`，v2.1.139）

command hook 在 `PostToolUse` 上返回 `"decision": "block"` 时，会把 `reason` 加在工具结果旁边；Claude 仍能看到原始输出。`continueOnBlock` 是 **prompt** hook 的字段（command 和 agent hook 没有它）：默认情况下，prompt hook 在 `PostToolUse` 上返回 `ok: false` 会结束回合并把原因显示为一行警告。在该 prompt hook 上设置 `"continueOnBlock": true` 则会把原因回传给 Claude 并继续回合，让模型可以读取反馈后重试或调整。

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Check this edit against our write policy (for example, read-only paths). Hook input: $ARGUMENTS",
            "continueOnBlock": true
          }
        ]
      }
    ]
  }
}
```

当 hook 的 `reason` 是 Claude 可以据此行动的内容时（例如"该文件只读，请写到别处"）使用它；当阻止必须彻底终止回合时不要使用。

### UserPromptSubmit

用户提交 prompt 时、Claude 处理之前运行。自 v2.1.299 起，它在 skill 或自定义命令展开之前运行，因此阻止该 prompt 同时也会阻止该命令的 `!` shell 行；`UserPromptExpansion` 在其后触发。

**配置：**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py"
          }
        ]
      }
    ]
  }
}
```

**输出控制：**
- `decision`：`"block"` 阻止处理
- `reason`：被阻止时的说明
- `additionalContext`：附加到 prompt 的上下文

### Stop 与 SubagentStop

在 Claude 完成响应（Stop）或子代理完成（SubagentStop）时运行。支持基于 prompt 的评估，用于智能的任务完成检查。

**附加输入字段：** `Stop` 和 `SubagentStop` hook 的 JSON 输入都包含 `last_assistant_message` 字段，内容是 Claude 或子代理停止前的最后一条消息。这对评估任务完成情况很有用。

**配置：**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Evaluate if Claude completed all requested tasks.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

> **连续阻止的安全上限（v2.1.143）**：如果 `Stop` hook 在同一回合内连续 **8 次**返回 `"decision": "block"`（或设置 `continue: false`），Claude Code 会覆盖下一次阻止并结束回合。可用环境变量 `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=<整数>` 覆盖该阈值（设为 `0` 完全禁用上限）。这可以防止有 bug 的 Stop hook 让回合无限循环。

**返回字段（v2.1.163）：** `Stop` 或 `SubagentStop` hook 可以返回 `hookSpecificOutput.additionalContext` 向 Claude 提供反馈并**继续回合且不显示错误标签**。以前，从 Stop hook 影响模型很别扭；现在 hook 可以干净地注入上下文，避免旧反馈路径（如 `"decision": "block"`）的错误标签行为。

```json
{
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "additionalContext": "Reminder: run the test suite before declaring done."
  }
}
```

### SubagentStart

子代理开始执行时运行。matcher 输入是 agent 类型名，允许 hook 针对特定子代理类型。

**配置：**
```json
{
  "hooks": {
    "SubagentStart": [
      {
        "matcher": "code-review",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/subagent-init.sh"
          }
        ]
      }
    ]
  }
}
```

### SessionStart

会话开始或恢复时运行。可以持久化环境变量。

**Matcher：** `startup`、`resume`、`clear`、`compact`、`fork`

> **v2.1.214 更新**：fork 出的会话现在报告来源 `"fork"`——之前报告 `"resume"`。

**特殊能力：** 用 `CLAUDE_ENV_FILE` 持久化环境变量（在 `CwdChanged` 和 `FileChanged` hook 中也可用）：

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

**会话级输出（v2.1.152）：** `SessionStart` hook 可以返回 JSON 来重新扫描 skill 并设置会话标题：

```json
{
  "reloadSkills": true,
  "hookSpecificOutput": {
    "sessionTitle": "Payments migration"
  }
}
```

顶层 `reloadSkills: true` 会在同一会话内触发 skill 重新扫描（与 `/reload-skills` 命令相同的效果），使 hook 刚安装的 skill 立即可用。`hookSpecificOutput.sessionTitle` 在启动和恢复时设置会话的显示标题。

### SessionEnd

会话结束时运行，用于清理或最终日志记录。无法阻止终止。

**Reason 字段取值：**
- `clear` - 用户清除了会话
- `resume` - 通过交互式 `/resume` 切换会话
- `logout` - 用户退出登录
- `prompt_input_exit` - 用户通过 prompt 输入退出
- `other` - 其他原因

**配置：**
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-cleanup.sh\""
          }
        ]
      }
    ]
  }
}
```

### Notification 事件

通知事件的 matcher 取值：
- `permission_prompt` - 权限请求通知
- `idle_prompt` - 空闲状态通知
- `auth_success` - 认证成功
- `elicitation_dialog` - MCP 服务器打开了 elicitation 表单
- `elicitation_url_dialog` - MCP 服务器要求你打开一个浏览器 URL
- `elicitation_complete` - URL 模式的 elicitation 已报告完成
- `elicitation_response` - elicitation 响应已发回服务器
- `agent_needs_input` - 后台 agent 需要输入（v2.1.198）
- `agent_completed` - 后台 agent 已完成（v2.1.198）
- `quota_auto_resume_fired` / `quota_auto_resume_stale` / `quota_auto_resume_disabled` - 用量限额自动恢复的结果（v2.1.234）
- `plugin_notification` - 某个 mod 通过 `$.ui.notify` 发出了通知；除非该 mod 自行设置，hook 的 `title` 就是 mod 的名字

### PreModelSwitch

在 Claude Code **应用**请求的模型切换**之前**运行——例如你运行 `/model` 时，或某个组件请求更换模型时。需要 v2.1.251 或更高版本。

**Matcher：** 被切换到的模型的规范名，派生自 `to_model`。可以精确匹配某个模型（`claude-opus-5`），也可以用正则匹配一个系列（`.*opus.*`）。

**输入字段：** 除公共字段外，hook 还接收 `from_model`（切换前使用的模型）和 `to_model`（请求切换到的模型）。

**可否阻止：** 可以。退出码 `2` 阻止切换并把 stderr 显示为错误，会话保持当前模型。用它来门禁或否决模型变更——例如让成本敏感的项目用不上最贵的模型。

**超时：** 该事件把 `command`、`http` 和 `mcp_tool` 的默认超时降为 30 秒。

**配置：**
```json
{
  "hooks": {
    "PreModelSwitch": [
      {
        "matcher": ".*opus.*",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/gate-model-switch.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# gate-model-switch.sh - refuse a switch to Opus on this project
input=$(cat)
to_model=$(echo "$input" | jq -r '.to_model')

if [[ "$to_model" == *opus* ]]; then
  echo "This project is budgeted for Sonnet; staying on the current model." >&2
  exit 2
fi

exit 0
```

### PostModelSwitch

会话模型**变更之后**运行。它也会在 Claude Code 自行变更模型时触发——例如恢复会话时还原之前选择的模型——而不仅是应用户请求的切换。需要 v2.1.251 或更高版本。

**Matcher：** 与 `PreModelSwitch` 相同——派生自 `to_model` 的规范名。

**输入字段：** `from_model` 和 `to_model`，以及公共字段。

**可否阻止：** 否。切换已经发生；hook 只能观察和响应。

**超时：** 该事件把 `command`、`http` 和 `mcp_tool` 的默认超时降为 30 秒。

**配置：**
```json
{
  "hooks": {
    "PostModelSwitch": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/log-model-switch.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# log-model-switch.sh - append every model change to a session log
input=$(cat)
from=$(echo "$input" | jq -r '.from_model')
to=$(echo "$input" | jq -r '.to_model')

echo "$(date -Iseconds) $from -> $to" >> ~/.claude/model-switches.log
exit 0
```

## 组件作用域的 Hooks

Hooks 可以在组件（skill、agent、命令）的 frontmatter 中挂载到特定组件：

**在 SKILL.md、agent.md 或 command.md 中：**

```yaml
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/check.sh"
          once: true  # Skill frontmatter only: removed after first successful run
---
```

**支持的事件：** 所有 hook 事件。子代理 hook 只在该子代理运行期间生效（`Stop` → `SubagentStop`）；skill hook 在该 skill 被调用时注册，并在会话剩余时间内保持有效。自 v2.1.304 起，同一来源（你的项目、你的个人 skill 目录或一个插件）的 skill 每个会话最多注册 1,024 个 hook 和 16,384 个 matcher 字符；超限的 skill 一个 hook 都不会注册（在 `claude --debug` 日志中搜索 `registers none of its hooks`）。

这样可以直接在使用它们的组件中定义 hook，把相关代码放在一起。

### 子代理 frontmatter 中的 Hooks

当 `Stop` hook 定义在子代理的 frontmatter 中时，它会自动转换为限定于该子代理的 `SubagentStop` hook。这确保 stop hook 只在该特定子代理完成时触发，而不是主会话停止时。

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # The above Stop hook auto-converts to SubagentStop for this subagent
---
```

**需要工作区信任（v2.1.218）：** **项目**级子代理的 frontmatter hook 现在要求先接受该 agent 文件所在文件夹的工作区信任才能运行。v2.1.218 之前，这些 hook 可以来自你未信任的文件夹。哪些作用域豁免见[子代理文档](https://code.claude.com/docs/en/sub-agents#hooks-in-subagent-frontmatter)。

## PermissionRequest 事件

以自定义输出格式处理权限请求：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow|deny",
      "updatedInput": {},
      "message": "Custom message",
      "interrupt": false
    }
  }
}
```

## Hook 输入与输出

### JSON 输入（经 stdin）

所有 hook 通过 stdin 接收 JSON 输入：

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.js",
    "content": "..."
  },
  "tool_use_id": "toolu_01ABC123...",
  "agent_id": "agent-abc123",
  "agent_type": "security-reviewer",
  "worktree": "/path/to/worktree",
  "effort": { "level": "medium" }
}
```

**公共字段：**

| 字段 | 说明 |
|-------|-------------|
| `session_id` | 会话唯一标识 |
| `transcript_path` | 会话转录文件的路径 |
| `cwd` | 当前工作目录 |
| `prompt_id` | 正在处理的 prompt 的 UUID；与 OpenTelemetry 的 `prompt.id` 属性关联（v2.1.196） |
| `hook_event_name` | 触发该 hook 的事件名 |
| `agent_id` | 运行该 hook 的 agent 标识 |
| `agent_type` | Agent 名称（例如 `"Explore"` 或 `"security-reviewer"`）；仅在会话使用 `--agent` 或 hook 在子代理内触发时存在 |
| `worktree` | agent 所在 git worktree 的路径（如在 worktree 中运行） |
| `effort.level` | （v2.1.133+）hook 运行时的 effort 等级设置，包括 skill、子代理或 `ultrathink` 的等级：`low`、`medium`、`high`、`xhigh` 或 `max`。刚更改的等级可能在生效前就出现在这里 |

### 退出码

| 退出码 | 含义 | 行为 |
|-----------|---------|----------|
| **0** | 成功 | 继续，解析 JSON stdout |
| **2** | 阻塞性错误 | 阻止操作，stderr 显示为错误 |
| **其他** | 非阻塞性错误 | 继续；转录中以 `<hook 名称> hook error` 通知显示 stderr 的第一行 |

### JSON 输出（stdout，退出码 0）

```json
{
  "continue": true,
  "stopReason": "Optional message if stopping",
  "suppressOutput": false,
  "systemMessage": "Optional warning message",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "File is in allowed directory",
    "updatedInput": {
      "file_path": "/modified/path.js"
    }
  }
}
```

> **作用范围（v2.1.121+）：** `hookSpecificOutput.updatedToolOutput` 现在对**所有**工具生效，而不仅是 MCP 工具。挂在 `Bash`、`Edit`、`Read` 等工具上的 `PostToolUse` hook 可以在 Claude 看到之前改写工具输出——可用于抹除密钥、规范化 diff 或过滤嘈杂的命令输出。该值必须符合工具的输出结构——`Bash` 返回带 `stdout`、`stderr`、`interrupted` 和 `isImage` 的对象；对内置工具，不匹配的值会被忽略并使用原始输出。示例（去除 `Bash` 输出中的 ANSI 颜色码）：
>
> ```json
> {
>   "hookSpecificOutput": {
>     "hookEventName": "PostToolUse",
>     "updatedToolOutput": {
>       "stdout": "<output with ANSI escapes removed>",
>       "stderr": "",
>       "interrupted": false,
>       "isImage": false
>     }
>   }
> }
> ```

> **`retry`（PermissionDenied）**：用 JSON `hookSpecificOutput.retry: true` 告诉模型可以重试被拒绝的工具调用。

> **已弃用的 `PreToolUse` 决策形式**：对 `PreToolUse`，顶层的 `decision` 和 `reason` 字段**已弃用**——请改用 `hookSpecificOutput.permissionDecision`（`allow` / `deny` / `ask` / `defer`）和 `permissionDecisionReason`。决策之间的优先级为 `deny` > `defer` > `ask` > `allow`。另请注意：`suppressOutput` 会被接受但**没有任何效果**。

> **输出上限**：hook 的 `additionalContext`、`systemMessage` 和 `initialUserMessage` 字符串以及它的纯 stdout 各自上限为 10,000 字符。更长的输出会保存为会话目录中的一个文件，并以该文件路径和前 2,000 字符的预览替代；Claude 不会被要求读取该文件。自 v2.1.314 起，这也适用于 `PreCompact` hook——其超大输出可能导致压缩失败或重复。

#### `terminalSequence`（v2.1.141）

Hook 可以通过在 JSON 输出中设置 `terminalSequence` 发出原始 OSC（操作系统命令）转义序列。hook 返回时，宿主会把该序列写入其控制终端——无需自备 TTY 即可实现桌面通知、窗口标题更新和终端铃声。

| 字段 | 类型 | 说明 |
|-------|------|-------------|
| `terminalSequence` | string | 原始转义序列（通常是 OSC 9 / OSC 0 / OSC 777）。原样写入宿主终端。 |

示例——长任务完成时发出 OSC 9 桌面通知。ESC 和 BEL 需写成 JSON 转义（`\u001b`、`\u0007`），或用 `printf` 与 `jq` 构造；JSON 字符串中的原始控制字节会导致解析失败：

```json
{
  "terminalSequence": "\u001b]9;Task complete\u0007"
}
```

把它配置在 `Stop` hook 上，通知就会在 Claude 完成一轮时发出。序列支持取决于终端：iTerm2、Windows Terminal 和 WezTerm 支持 OSC 9，Kitty 使用 OSC 99。

## 环境变量

| 变量 | 可用范围 | 说明 |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | 所有 hook | 项目根的绝对路径 |
| `CLAUDE_ENV_FILE` | SessionStart、CwdChanged、FileChanged | 用于持久化环境变量的文件路径 |
| `CLAUDE_CODE_REMOTE` | 所有 hook | 在远程环境中运行时为 `"true"` |
| `${CLAUDE_PLUGIN_ROOT}` | 插件 hook | 插件目录的路径 |
| `${CLAUDE_PLUGIN_DATA}` | 插件 hook | 插件数据目录的路径 |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd hook | SessionEnd hook 的可配置超时（毫秒），覆盖默认值 |
| `CLAUDE_CODE_SESSION_ID` | Bash 工具子进程（v2.1.132+） | 会话 UUID；与 hook 输入 JSON 中的 `session_id` 字段一致。用于将 bash 日志与 hook 遥测关联。 |
| `CLAUDE_EFFORT` | Bash 工具子进程与 hook 命令（v2.1.133+） | 子进程启动时的 effort 等级设置（`low`/`medium`/`high`/`xhigh`/`max`）；与 hook 输入 JSON 中的 `effort.level` 一致。 |
| `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` | 进程级（v2.1.143+） | Stop hook 连续阻止多少次后，Claude Code 覆盖下一次阻止并结束回合（默认 `8`）。设为 `0` 禁用上限。 |

## 基于 Prompt 的 Hooks

对 `Stop` 和 `SubagentStop` 事件，可以使用基于 LLM 的评估：

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if all tasks are complete. Return your decision.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**LLM 响应结构：**
```json
{
  "ok": false,
  "reason": "Tests were not run after the last edit"
}
```

`ok: true` 放行动作；`ok` 为 `false` 时必须提供 `reason`。

## 示例

### 示例 1：Bash 命令校验器（PreToolUse）

**文件：** `.claude/hooks/validate-bash.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"\brm\s+-rf\s+/", "Blocking dangerous rm -rf / command"),
    (r"\bsudo\s+rm", "Blocking sudo rm command"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name != "Bash":
        sys.exit(0)

    command = input_data.get("tool_input", {}).get("command", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, command):
            print(message, file=sys.stderr)
            sys.exit(2)  # Exit 2 = blocking error

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**配置：**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\""
          }
        ]
      }
    ]
  }
}
```

### 示例 2：安全扫描器（PostToolUse）

**文件：** `.claude/hooks/security-scan.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

SECRET_PATTERNS = [
    (r"password\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded password"),
    (r"api[_-]?key\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded API key"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    file_path = tool_input.get("file_path", "")

    warnings = []
    for pattern, message in SECRET_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            warnings.append(message)

    if warnings:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Security warnings for {file_path}: " + "; ".join(warnings)
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### 示例 3：自动格式化代码（PostToolUse）

**文件：** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# Read JSON from stdin
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# Format based on file extension
case "$FILE_PATH" in
    *.js|*.jsx|*.ts|*.tsx|*.json)
        command -v prettier &>/dev/null && prettier --write "$FILE_PATH" 2>/dev/null
        ;;
    *.py)
        command -v black &>/dev/null && black "$FILE_PATH" 2>/dev/null
        ;;
    *.go)
        command -v gofmt &>/dev/null && gofmt -w "$FILE_PATH" 2>/dev/null
        ;;
esac

exit 0
```

### 示例 4：Prompt 校验器（UserPromptSubmit）

**文件：** `.claude/hooks/validate-prompt.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"delete\s+(all\s+)?database", "Dangerous: database deletion"),
    (r"rm\s+-rf\s+/", "Dangerous: root deletion"),
]

def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("prompt", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            output = {
                "decision": "block",
                "reason": f"Blocked: {message}"
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### 示例 5：智能 Stop Hook（基于 Prompt）

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if Claude completed all requested tasks. Check: 1) Were all files created/modified? 2) Were there unresolved errors? If incomplete, explain what's missing.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### 示例 6：上下文用量跟踪器（Hook 成对使用）

用 `UserPromptSubmit`（消息前）和 `Stop`（响应后）hook 配合，跟踪每次请求的 token 消耗。

**文件：** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
Context Usage Tracker - Tracks token consumption per request.

Uses UserPromptSubmit as "pre-message" hook and Stop as "post-response" hook
to calculate the delta in token usage for each request.

Token Counting Methods:
1. Character estimation (default): ~4 chars per token, no dependencies
2. tiktoken (optional): More accurate (~90-95%), requires: pip install tiktoken
"""
import json
import os
import sys
import tempfile

# Configuration
CONTEXT_LIMIT = 1000000  # 1M on Opus/Sonnet/Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Sonnet 4.6; 200000 on Haiku 4.5 (adjust for your model)
USE_TIKTOKEN = False    # Set True if tiktoken is installed for better accuracy


def get_state_file(session_id: str) -> str:
    """Get temp file path for storing pre-message token count, isolated by session."""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    Count tokens in text.

    Uses tiktoken with p50k_base encoding if available (~90-95% accuracy),
    otherwise falls back to character estimation (~80-90% accuracy).
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # Fall back to estimation

    # Character-based estimation: ~4 characters per token for English
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """Read and concatenate all content from transcript file."""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # Extract text content from various message formats
                if "message" in entry:
                    msg = entry["message"]
                    if isinstance(msg.get("content"), str):
                        content.append(msg["content"])
                    elif isinstance(msg.get("content"), list):
                        for block in msg["content"]:
                            if isinstance(block, dict) and block.get("type") == "text":
                                content.append(block.get("text", ""))
            except json.JSONDecodeError:
                continue

    return "\n".join(content)


def handle_user_prompt_submit(data: dict) -> None:
    """Pre-message hook: Save current token count before request."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # Save to temp file for later comparison
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """Post-response hook: Calculate and report token delta."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # Load pre-message count
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # Calculate delta
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # Report usage
    method = "tiktoken" if USE_TIKTOKEN else "estimated"
    print(f"Context ({method}): ~{current_tokens:,} tokens ({percentage:.1f}% used, ~{remaining:,} remaining)", file=sys.stderr)
    if delta_tokens > 0:
        print(f"This request: ~{delta_tokens:,} tokens", file=sys.stderr)


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")

    if event == "UserPromptSubmit":
        handle_user_prompt_submit(data)
    elif event == "Stop":
        handle_stop(data)

    sys.exit(0)


if __name__ == "__main__":
    main()
```

**配置：**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ]
  }
}
```

**工作原理：**
1. `UserPromptSubmit` 在 prompt 被处理前触发——保存当前 token 数
2. `Stop` 在 Claude 响应后触发——计算差值并报告用量
3. 每个会话通过临时文件名中的 `session_id` 隔离

**Token 计数方式：**

| 方式 | 准确度 | 依赖 | 速度 |
|--------|----------|--------------|-------|
| 字符估算 | 约 80-90% | 无 | <1ms |
| tiktoken（p50k_base） | 约 90-95% | `pip install tiktoken` | <10ms |

> **注意：** Anthropic 没有发布官方的离线分词器。两种方式都是近似值。转录内容包括用户 prompt、Claude 的响应和工具输出；自 v2.1.300 起，它还会记录每次 API 请求的 system prompt、工具和参数。

### 示例 7：播种自动模式权限（一次性安装脚本）

一个一次性安装脚本，向 `~/.claude/settings.json` 播种与 Claude Code 自动模式基线等效的安全权限规则——默认 32 条，开启所有类别开关后最多 58 条——不需要任何 hook，也不会记住未来的选择。运行一次即可；可安全重复运行（跳过已存在的规则）。

**文件：** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Preview what would be added
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Apply
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**会添加的内容：**

| 类别 | 示例 |
|----------|---------|
| 内置工具 | `Read(*)`、`Grep(*)`、`Agent(*)`、`WebSearch(*)` |
| 可选编辑（--include-edits） | `Edit(*)` |
| Git 读取 | `Bash(git status:*)`、`Bash(git log:*)`、`Bash(git diff:*)` |
| Git 写入（本地） | `Bash(git add:*)`、`Bash(git commit:*)`、`Bash(git checkout:*)` |
| 包管理器 | `Bash(npm ci:*)`、`Bash(npm install:*)`、`Bash(pip install:*)`、`Bash(pip3 install:*)` |
| 构建与测试 | `Bash(make:*)`、`Bash(pytest:*)`、`Bash(go test:*)` |
| 常用 shell | `Bash(ls:*)`、`Bash(cat:*)`、`Bash(wc:*)` |
| GitHub CLI | `Bash(gh pr view:*)`、`Bash(gh pr create:*)`、`Bash(gh issue list:*)` |

**刻意排除的内容**（该脚本永不添加）：
- `rm -rf`、`sudo`、强推、`git reset --hard`
- `DROP TABLE`、`kubectl delete`、`terraform destroy`
- `npm publish`、`curl | bash`、生产部署

### 示例 8：学习进度记录器（SessionEnd）

在每次 Claude Code 会话结束时记录你学习了哪些模块。进度存储在 `~/.claude-howto-progress.json`——仓库之外，因此 `git pull` 不会覆盖它。

**为什么用 `SessionEnd` 而不是 `Stop`？**
`Stop` 在 Claude 的*每一次*响应后触发。`SessionEnd` 只在会话终止时触发一次——正是会话结束日记需要的时机。

**为什么没有交互式提示？**
Hooks 运行时没有控制终端，`/dev/tty` 不可用，hook 无法向你提问。启动 Claude Code 时通过环境变量传入模块（和可选备注），例如 `CLAUDE_HOWTO_MODULES=06,07 claude`。

**文件：** `06-hooks/session-end.sh`

```bash
#!/usr/bin/env bash
# SessionEnd hook: records the modules worked on, then appends a session record
# to ~/.claude-howto-progress.json for persistent learning progress tracking.

PROGRESS_FILE="$HOME/.claude-howto-progress.json"

# Guard: only run inside this repo
if [[ "$CLAUDE_PROJECT_DIR" != *"claude-howto"* ]] && [[ "$PWD" != *"claude-howto"* ]]; then
  exit 0
fi

if [ ! -f "$PROGRESS_FILE" ]; then
  echo '{"sessions":[]}' > "$PROGRESS_FILE"
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H:%M")

# Modules worked on, e.g. launch with: CLAUDE_HOWTO_MODULES=06,07 claude
# 01=Slash  02=Memory  03=Skills  04=Subagents  05=MCP
# 06=Hooks  07=Plugins 08=Checkpoints 09=Advanced 10=CLI
INPUT="${CLAUDE_HOWTO_MODULES:-}"

if [ -z "$INPUT" ] || [ "$INPUT" = "skip" ]; then
  exit 0
fi

MODULES_JSON=$(echo "$INPUT" | tr ',' '\n' | tr -d ' ' | while read -r m; do
  case "$m" in
    01) echo '"01-slash-commands"' ;;
    02) echo '"02-memory"' ;;
    03) echo '"03-skills"' ;;
    04) echo '"04-subagents"' ;;
    05) echo '"05-mcp"' ;;
    06) echo '"06-hooks"' ;;
    07) echo '"07-plugins"' ;;
    08) echo '"08-checkpoints"' ;;
    09) echo '"09-advanced-features"' ;;
    10) echo '"10-cli"' ;;
    *)  echo "\"$m\"" ;;
  esac
done | paste -sd ',' -)

# Optional notes, e.g. CLAUDE_HOWTO_NOTES="tried the pre-commit example"
NOTES="${CLAUDE_HOWTO_NOTES:-}"

# Pass NOTES as a separate argument so Python handles JSON escaping —
# avoids broken JSON when notes contain quotes or backslashes.
python3 - "$PROGRESS_FILE" "$DATE" "$TIME" "$MODULES_JSON" "$NOTES" <<'PYEOF'
import sys, json

path, date, time_str, modules_raw, notes = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]

new_session = {
    "date": date,
    "time": time_str,
    "modules": json.loads(f"[{modules_raw}]") if modules_raw else [],
    "notes": notes,
}

with open(path, 'r') as f:
    data = json.load(f)

data.setdefault('sessions', []).append(new_session)

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

echo " Saved to $PROGRESS_FILE"
```

**安装** —— 把脚本复制到项目的 hook 目录，让 `settings.json` 中的路径可以解析：

```bash
mkdir -p .claude/hooks
cp 06-hooks/session-end.sh .claude/hooks/
chmod +x .claude/hooks/session-end.sh
```

**配置**（在 `.claude/settings.json` 中）：

```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-end.sh\"",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

SessionEnd hook 默认共享 1.5 秒预算。为单个 hook 设置 `"timeout"`（秒）会把预算上调到该值，上限 60 秒；没有自带 `timeout` 的 hook 在 1.5 秒后被取消。

**输出 —— `~/.claude-howto-progress.json`：**

```json
{
  "sessions": [
    {
      "date": "2026-04-18",
      "time": "14:32",
      "modules": ["06-hooks", "07-plugins"],
      "notes": "Installed first hook, tried pre-commit example"
    }
  ]
}
```

**演示的关键模式：**

| 模式 | 为什么重要 |
|---------|----------------|
| `SessionEnd` 事件 | 退出时触发一次——不像 `Stop` 那样每次响应后都触发 |
| `INPUT="${CLAUDE_HOWTO_MODULES:-}"` | Hooks 没有终端（`/dev/tty` 不可用），输入来自环境变量 |
| `"timeout": 10` | SessionEnd hook 若不设置自己的 `timeout`，1.5 秒后被取消 |
| `$CLAUDE_PROJECT_DIR` | 可移植路径——绝不硬编码 `/Users/yourname/...` |
| 顶部的守卫子句 | 若被全局安装，避免在无关项目中运行 |
| 存储在仓库之外 | `~/` 路径在 `git pull` 时不会被覆盖 |

**配套：可视化进度跟踪器**

要获得覆盖全部 10 个模块的完整复选框 UI，在浏览器中打开自带的跟踪器：

```bash
open ../../local-progress/index.html
```

进度存储在浏览器 `localStorage` 中（绝不写入仓库内的磁盘）。用**导出**按钮把快照保存为 JSON，用**导入**恢复。

## 插件 Hooks

插件可以在其 `hooks/hooks.json` 文件中包含 hooks：

**文件：** `plugins/hooks/hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/validate.sh"
          }
        ]
      }
    ]
  }
}
```

**插件 Hooks 中的环境变量：**
- `${CLAUDE_PLUGIN_ROOT}` - 插件目录的路径
- `${CLAUDE_PLUGIN_DATA}` - 插件数据目录的路径

这让插件可以携带自定义的校验和自动化 hook。

## MCP 工具 Hooks

MCP 工具遵循 `mcp__<server>__<tool>` 模式：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"systemMessage\": \"Memory operation logged\"}'"
          }
        ]
      }
    ]
  }
}
```

## 安全注意事项

### 免责声明

**使用风险自负**：Hooks 会执行任意 shell 命令。你独自承担以下责任：
- 你配置的命令
- 文件访问/修改权限
- 潜在的数据丢失或系统损坏
- 在生产使用前于安全环境中测试 hook

### 安全说明

- **需要工作区信任：** `statusLine` 和 `fileSuggestion` hook 输出命令现在需要先接受工作区信任才会生效。
- **状态栏终端尺寸（v2.1.153）：** 状态栏命令脚本现在会收到 `COLUMNS` 和 `LINES` 环境变量，脚本可以据此适配终端宽高（例如 `[ "$COLUMNS" -lt 80 ] && short_output`）。
- **HTTP hook 与环境变量：** HTTP hook 需要显式的 `allowedEnvVars` 列表才能在 header 值中使用环境变量插值。这防止敏感环境变量意外泄露给远程端点。
- **托管设置层级：** `disableAllHooks` 设置现在遵循托管设置层级，组织级设置可以强制禁用 hooks，个人用户无法覆盖。
- **PowerShell 自动批准（v2.1.119）：** PowerShell 工具命令可在权限模式下自动批准，与 Bash 一致。为以 PowerShell 为 shell 工具运行 Claude Code 的 Windows 用户带来对等体验。
- **Bash 裸环境变量自动批准已封堵（v2.1.145）：** v2.1.145 之前，形如 `FOO=bar somecommand` 的 Bash 命令（裸变量赋值与非白名单命令内联）可能在仅 `FOO=bar` 本身位于允许列表时被自动批准。v2.1.145 封堵了这一点——此类命令现在会进入权限提示。依赖该隐式放行的脚本会开始提示；请用覆盖完整命令（而不只是变量赋值）的 `Bash(...)` 权限规则显式重新允许。

### 最佳实践

| 应该 | 不应该 |
|-----|-------|
| 校验并清洗所有输入 | 盲目信任输入数据 |
| 给 shell 变量加引号：`"$VAR"` | 不加引号：`$VAR` |
| 阻止路径穿越（`..`） | 允许任意路径 |
| 用 `$CLAUDE_PROJECT_DIR` 拼绝对路径 | 硬编码路径 |
| 跳过敏感文件（`.env`、`.git/`、密钥） | 处理所有文件 |
| 先在隔离环境中测试 hook | 部署未测试的 hook |
| HTTP hook 使用显式 `allowedEnvVars` | 向 webhook 暴露所有环境变量 |

## 调试

### 启用调试模式

用调试标志运行 Claude 以查看详细的 hook 日志：

```bash
claude --debug
```

### 详细模式

在 Claude Code 中按 `Ctrl+O` 启用详细模式，查看 hook 执行进度。

### 独立测试 Hooks

```bash
# Test with sample JSON input
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# Check exit code
echo $?
```

## 完整配置示例

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/format-code.sh\"",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py\""
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-init.sh\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Verify all tasks are complete before stopping.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Hook 执行细节

| 方面 | 行为 |
|--------|----------|
| **超时** | command/http/mcp_tool 默认 600 秒（prompt 30 秒，agent 60 秒）；可按 hook 配置 |
| **并行化** | 所有匹配的 hook 并行运行；自 v2.1.312 起，每个会话同时最多运行 24 个 prompt 或 agent hook（含子代理），另有最多 12 个已等待超过其事件超时的 hook，其余排队等待（v2.1.302–v2.1.311：单个事件最多 12 个）。 |
| **去重** | 相同的 hook 命令会被去重 |
| **环境** | 在当前目录中以 Claude Code 的环境运行 |

## 故障排查

### Hook 未执行
- 确认 JSON 配置语法正确
- 检查 matcher 模式与工具名称匹配
- 确保脚本存在且可执行：`chmod +x script.sh`
- 运行 `claude --debug` 查看 hook 执行日志
- 确认 hook 从 stdin（而非命令参数）读取 JSON

### Hook 意外阻止
- 用示例 JSON 测试 hook：`echo '{"tool_name": "Write", ...}' | ./hook.py`
- 检查退出码：放行应为 0，阻止应为 2
- 检查 stderr 输出（退出码 2 时会显示）

### JSON 解析错误
- 始终从 stdin 读取，不要从命令参数读取
- 使用正确的 JSON 解析（不要做字符串处理）
- 优雅处理缺失字段

## 安装

### 第 1 步：创建 Hooks 目录
```bash
mkdir -p ~/.claude/hooks
```

### 第 2 步：复制示例 Hooks
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### 第 3 步：在 Settings 中配置
用上面展示的 hook 配置编辑 `~/.claude/settings.json` 或 `.claude/settings.json`。

## 相关概念

- **[检查点与回退](../08-checkpoints/README.md)** - 保存和恢复会话状态
- **[斜杠命令](../01-slash-commands/README.md)** - 创建自定义斜杠命令
- **[Skills](../03-skills/README.md)** - 可复用的自主能力
- **[子代理](../04-subagents/README.md)** - 委派任务执行
- **[插件](../07-plugins/README.md)** - 打包的扩展集合
- **[高级特性](../09-advanced-features/README.md)** - 探索 Claude Code 的高级能力

## 更多资源

- **[官方 Hooks 文档](https://code.claude.com/docs/en/hooks)** - 完整的 hooks 参考
- **[CLI 参考](https://code.claude.com/docs/en/cli-reference)** - 命令行界面文档
- **[Memory 指南](../02-memory/README.md)** - 持久化上下文配置

---

**最后更新**: 2026 年 11 月 13 日
**Claude Code 版本**: 2.1.323
**来源**:
- https://code.claude.com/docs/en/hooks
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/plugins/manifest-reference#quoting-and-path-separators
- https://github.com/anthropics/claude-code/releases/tag/v2.1.295
- https://code.claude.com/docs/en/hooks#pretooluse
- https://code.claude.com/docs/en/hooks#pretooluse-decision-control
- https://code.claude.com/docs/en/hooks#hook-lifecycle
- https://code.claude.com/docs/en/hooks#userpromptsubmit-input
- https://code.claude.com/docs/en/changelog#2-1-299
- https://code.claude.com/docs/en/changelog#2-1-300
- https://code.claude.com/docs/en/changelog#2-1-301
- https://code.claude.com/docs/en/changelog#2-1-302
- https://code.claude.com/docs/en/hooks#defer-a-tool-call-for-later
- https://code.claude.com/docs/en/hooks-guide#limitations
- https://code.claude.com/docs/en/hooks#notification
- https://code.claude.com/docs/en/changelog#2-1-304
- https://code.claude.com/docs/en/hooks#limits-on-skill-hooks
- https://code.claude.com/docs/en/changelog#2-1-309
- https://code.claude.com/docs/en/hooks#failed-hooks-on-windows-without-git-bash
- https://code.claude.com/docs/en/changelog#2-1-312
- https://code.claude.com/docs/en/changelog#2-1-314
- https://code.claude.com/docs/en/hooks#pretooluse-ask-decisions-in-auto-mode
- https://code.claude.com/docs/en/hooks#common-input-fields
- https://code.claude.com/docs/en/hooks#json-output
- https://code.claude.com/docs/en/env-vars#variables
- https://code.claude.com/docs/en/model-config#extended-context
- https://code.claude.com/docs/en/agent-sdk/hooks#block-the-action-when-a-callback-fails
- https://code.claude.com/docs/en/hooks#mcp-tool-hook-fields
- https://code.claude.com/docs/en/changelog#2-1-321
- https://code.claude.com/docs/en/changelog#2-1-319
- https://code.claude.com/docs/en/hooks#posttooluse-after-an-interrupt
- https://code.claude.com/docs/en/changelog#2-1-323
**兼容模型**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
