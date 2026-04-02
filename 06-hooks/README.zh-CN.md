<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks

Hooks 是在 Claude Code 会话中，针对特定事件自动执行的脚本机制。它可用于自动化、校验、权限控制与自定义工作流。

## Overview

Hooks 本质是事件触发的自动动作（shell 命令、HTTP webhook、LLM prompt、或 subagent 评估）。当 Claude Code 内发生指定事件时，hook 自动执行。Hook 通过 JSON stdin 接收输入，并通过退出码与 JSON 输出返回结果。

**Key features:**
- 事件驱动自动化
- JSON 输入/输出
- 支持 command / prompt / http / agent 四类 hook
- 支持按工具名模式匹配

## Configuration

Hooks 可配置在以下位置：

- `~/.claude/settings.json` - 用户级（全项目）
- `.claude/settings.json` - 项目级（可共享/可提交）
- `.claude/settings.local.json` - 本地项目级（不提交）
- Managed policy - 组织级策略
- 插件 `hooks/hooks.json` - 插件作用域 hooks
- Skill/Agent frontmatter - 组件生命周期 hooks

### Basic Configuration Structure

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

**Key fields:**

| Field | Description | Example |
|-------|-------------|---------|
| `matcher` | 匹配工具名模式（区分大小写） | `"Write"`, `"Edit\|Write"`, `"*"` |
| `hooks` | hook 定义数组 | `[{ "type": "command", ... }]` |
| `type` | hook 类型：`"command"`（bash）、`"prompt"`（LLM）、`"http"`（webhook）、`"agent"`（subagent） | `"command"` |
| `command` | 要执行的 shell 命令 | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | 可选超时秒数（默认 60） | `30` |
| `once` | 若为 `true`，每会话仅执行一次 | `true` |

### Matcher Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| 精确匹配 | 匹配单个工具 | `"Write"` |
| 正则模式 | 匹配多个工具 | `"Edit\|Write"` |
| 通配符 | 匹配全部工具 | `"*"` 或 `""` |
| MCP 工具模式 | server+tool 匹配 | `"mcp__memory__.*"` |

## Hook Types

Claude Code 支持四类 hooks：

### Command Hooks

默认类型。执行 shell 命令，通过 JSON stdin/stdout 与退出码通信。

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

### HTTP Hooks

> v2.1.63 新增。

HTTP hooks 会把与 command hooks 相同的 JSON 输入 POST 到远程 webhook，并接收 JSON 响应。若开启 sandbox，HTTP hooks 也走 sandbox。出于安全考虑，URL 中环境变量插值需要显式配置 `allowedEnvVars`。

```json
{
  "hooks": {
    "PostToolUse": [{
      "type": "http",
      "url": "https://my-webhook.example.com/hook",
      "matcher": "Write"
    }]
  }
}
```

**Key properties:**
- `"type": "http"`：声明 HTTP hook
- `"url"`：webhook 端点
- sandbox 开启时经 sandbox 路由
- URL 使用环境变量时需显式 `allowedEnvVars`

### Prompt Hooks

由 LLM 评估的 hooks。`prompt` 内容会交给 Claude 判断，常用于 `Stop` 与 `SubagentStop` 的智能完成校验。

```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude completed all requested tasks.",
  "timeout": 30
}
```

LLM 将返回结构化判定（见后文 Prompt-Based Hooks）。

### Agent Hooks

基于 subagent 的校验 hooks，会拉起专用 agent 进行复杂检查。与 prompt hook（单轮 LLM 判断）不同，agent hook 可调用工具并做多步推理。

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

**Key properties:**
- `"type": "agent"`：声明 agent hook
- `"prompt"`：subagent 任务描述
- 可使用 Read/Grep/Bash 等工具执行检查
- 返回结构化判定（类似 prompt hooks）

## Hook Events

Claude Code 目前支持 **25 个 hook 事件**：

| Event | When Triggered | Matcher Input | Can Block | Common Use |
|-------|---------------|---------------|-----------|------------|
| **SessionStart** | 会话开始/恢复/clear/compact | startup/resume/clear/compact | No | 环境初始化 |
| **InstructionsLoaded** | CLAUDE.md 或规则文件加载后 | (none) | No | 过滤/改写指令 |
| **UserPromptSubmit** | 用户提交 prompt 时 | (none) | Yes | prompt 校验 |
| **PreToolUse** | 工具执行前 | Tool name | Yes (allow/deny/ask) | 校验/改写输入 |
| **PermissionRequest** | 权限弹窗出现时 | Tool name | Yes | 自动放行/拒绝 |
| **PostToolUse** | 工具成功后 | Tool name | No | 回传上下文、审计 |
| **PostToolUseFailure** | 工具失败后 | Tool name | No | 错误处理、日志 |
| **Notification** | 发送通知时 | Notification type | No | 自定义通知 |
| **SubagentStart** | subagent 启动时 | Agent type name | No | subagent 初始化 |
| **SubagentStop** | subagent 结束时 | Agent type name | Yes | subagent 结果校验 |
| **Stop** | Claude 回答结束时 | (none) | Yes | 完成度检查 |
| **StopFailure** | API 错误导致回合结束 | (none) | No | 错误恢复、日志 |
| **TeammateIdle** | agent team 队友空闲 | (none) | Yes | 团队协作调度 |
| **TaskCompleted** | 任务标记完成 | (none) | Yes | 任务后处理 |
| **TaskCreated** | 通过 TaskCreate 创建任务 | (none) | No | 任务跟踪 |
| **ConfigChange** | 配置文件变化 | (none) | Yes（policy 除外） | 响应配置更新 |
| **CwdChanged** | 当前目录变更 | (none) | No | 目录级初始化 |
| **FileChanged** | 被监听文件变化 | (none) | No | 文件监听、重建 |
| **PreCompact** | 上下文压缩前 | manual/auto | No | 压缩前动作 |
| **PostCompact** | 上下文压缩后 | (none) | No | 压缩后动作 |
| **WorktreeCreate** | worktree 创建时 | (none) | Yes（可返回路径） | worktree 初始化 |
| **WorktreeRemove** | worktree 移除时 | (none) | No | worktree 清理 |
| **Elicitation** | MCP 请求用户输入时 | (none) | Yes | 输入校验 |
| **ElicitationResult** | 用户响应 elicitation 后 | (none) | Yes | 响应处理 |
| **SessionEnd** | 会话结束 | (none) | No | 清理、收尾日志 |

### PreToolUse

在 Claude 生成工具参数后、执行前触发。用于校验或改写工具输入。

**Configuration:**
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

**常见 matcher:** `Task`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**输出控制字段：**
- `permissionDecision`: `"allow"` / `"deny"` / `"ask"`
- `permissionDecisionReason`: 判定原因
- `updatedInput`: 改写后的工具输入

### PostToolUse

工具成功后立即触发。可做校验、日志、回传上下文。

**Configuration:**
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

**输出控制字段：**
- `"block"`：阻断并给 Claude 反馈
- `additionalContext`：附加给 Claude 的上下文

### UserPromptSubmit

用户提交 prompt 时触发（Claude 处理前）。

**Configuration:**
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

**输出控制字段：**
- `decision`: `"block"` 可阻止处理
- `reason`: 阻断原因
- `additionalContext`: 注入额外上下文

### Stop and SubagentStop

`Stop` 在 Claude 完成回答时触发；`SubagentStop` 在 subagent 完成时触发。两者支持 prompt-based 智能完结校验。

**额外输入字段：**`Stop` 与 `SubagentStop` 均可在输入 JSON 中获得 `last_assistant_message`，即停止前最后一条消息。

**Configuration:**
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

### SubagentStart

subagent 启动时触发。matcher 输入是 agent 类型名，可精确绑定某类 subagent。

**Configuration:**
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

会话启动或恢复时触发。可用于持久化环境变量。

**Matchers:** `startup`, `resume`, `clear`, `compact`

**Special feature:** 使用 `CLAUDE_ENV_FILE` 持久化环境变量（`CwdChanged` 与 `FileChanged` 同样可用）：

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

会话结束时触发，可做清理与收尾日志，不能阻断退出。

**Reason 字段取值：**
- `clear`
- `logout`
- `prompt_input_exit`
- `other`

**Configuration:**
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

### Notification Event

通知事件 matcher 更新为：
- `permission_prompt`
- `idle_prompt`
- `auth_success`
- `elicitation_dialog`

## Component-Scoped Hooks

hooks 可写在 skill/agent/command frontmatter 内：

**In SKILL.md, agent.md, or command.md:**

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
          once: true  # Only run once per session
---
```

**组件 hooks 支持事件：**`PreToolUse`, `PostToolUse`, `Stop`

### Hooks in Subagent Frontmatter

如果在 subagent frontmatter 中定义 `Stop` hook，它会自动转为仅该 subagent 生效的 `SubagentStop`。

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # 上面的 Stop 会自动转换为该 subagent 的 SubagentStop
---
```

## PermissionRequest Event

`PermissionRequest` 使用专用输出格式：

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

## Hook Input and Output

### JSON Input（stdin）

所有 hooks 都通过 stdin 接收 JSON：

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
  "agent_type": "main",
  "worktree": "/path/to/worktree"
}
```

**Common fields:**

| Field | Description |
|-------|-------------|
| `session_id` | 唯一会话 ID |
| `transcript_path` | 会话 transcript 文件路径 |
| `cwd` | 当前工作目录 |
| `hook_event_name` | 触发 hook 的事件名 |
| `agent_id` | 执行该 hook 的 agent ID |
| `agent_type` | agent 类型（如 `"main"` 或具体 subagent 类型） |
| `worktree` | 若在 worktree 中运行，则为其路径 |

### Exit Codes

| Exit Code | Meaning | Behavior |
|-----------|---------|----------|
| **0** | 成功 | 继续，并解析 stdout JSON |
| **2** | 阻断错误 | 阻断操作，stderr 显示错误 |
| **Other** | 非阻断错误 | 继续，verbose 模式下显示 stderr |

### JSON Output（stdout，exit code 0）

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

## Environment Variables

| Variable | Availability | Description |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | All hooks | 项目根目录绝对路径 |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | 持久化环境变量文件路径 |
| `CLAUDE_CODE_REMOTE` | All hooks | 在远程环境运行时为 `"true"` |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin hooks | 插件目录路径 |
| `${CLAUDE_PLUGIN_DATA}` | Plugin hooks | 插件数据目录路径 |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd hooks | SessionEnd hooks 超时（毫秒） |

## Prompt-Based Hooks

对 `Stop` / `SubagentStop` 可使用 LLM 评估：

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

**LLM Response Schema:**
```json
{
  "decision": "approve",
  "reason": "All tasks completed successfully",
  "continue": false,
  "stopReason": "Task complete"
}
```

## Examples

### Example 1: Bash Command Validator (PreToolUse)

**File:** `.claude/hooks/validate-bash.py`

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

**Configuration:**
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

### Example 2: Security Scanner (PostToolUse)

**File:** `.claude/hooks/security-scan.py`

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

### Example 3: Auto-Format Code (PostToolUse)

**File:** `.claude/hooks/format-code.sh`

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

### Example 4: Prompt Validator (UserPromptSubmit)

**File:** `.claude/hooks/validate-prompt.py`

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
    prompt = input_data.get("user_prompt", "") or input_data.get("prompt", "")

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

### Example 5: Intelligent Stop Hook (Prompt-Based)

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

### Example 6: Context Usage Tracker (Hook Pairs)

通过组合 `UserPromptSubmit`（前置）+ `Stop`（后置）来跟踪每次请求 token 消耗。

**File:** `.claude/hooks/context-tracker.py`

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
CONTEXT_LIMIT = 128000  # Claude's context window (adjust for your model)
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

**Configuration:**
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

**How it works:**
1. `UserPromptSubmit` 在 prompt 处理前触发：保存当前 token 计数
2. `Stop` 在 Claude 响应后触发：计算差值并输出
3. 用 `session_id` 隔离不同会话的状态文件

**Token Counting Methods:**

| Method | Accuracy | Dependencies | Speed |
|--------|----------|--------------|-------|
| 字符估算 | ~80-90% | 无 | <1ms |
| tiktoken (p50k_base) | ~90-95% | `pip install tiktoken` | <10ms |

> **Note:** Anthropic 尚未发布官方离线 tokenizer。两种方法都是近似值。transcript 包含用户消息、Claude 回复与工具输出，但不含系统提示与内部上下文。

### Example 7: Seed Auto-Mode Permissions (One-Time Setup Script)

这是一次性脚本：向 `~/.claude/settings.json` 注入约 67 条安全权限规则，对齐 Claude Code auto-mode 基线；无需 hooks，也不依赖后续“记住我的选择”。可重复运行（已存在规则会跳过）。

**File:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# 预览变更
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# 应用变更
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**会添加的规则类别：**

| Category | Examples |
|----------|---------|
| Built-in tools | `Read(*)`, `Edit(*)`, `Write(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)` |
| Git read | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)` |
| Git write (local) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Package managers | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| Build & test | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Common shell | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

**明确排除（绝不自动加入）：**
- `rm -rf`、`sudo`、force push、`git reset --hard`
- `DROP TABLE`、`kubectl delete`、`terraform destroy`
- `npm publish`、`curl | bash`、生产环境部署

## Plugin Hooks

插件可在 `hooks/hooks.json` 内置 hooks：

**File:** `plugins/hooks/hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"
          }
        ]
      }
    ]
  }
}
```

**插件 hooks 可用变量：**
- `${CLAUDE_PLUGIN_ROOT}`
- `${CLAUDE_PLUGIN_DATA}`

## MCP Tool Hooks

MCP 工具名模式：`mcp__<server>__<tool>`

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

## Security Considerations

### Disclaimer

**风险自担（USE AT YOUR OWN RISK）**：hooks 可执行任意 shell 命令。你需自行负责：
- 配置的命令行为
- 文件访问与修改权限
- 潜在数据丢失或系统损坏
- 在生产前于安全环境充分测试

### Security Notes

- **需要 workspace trust：** `statusLine` 与 `fileSuggestion` hook 输出命令，需先接受 workspace trust 才会生效。
- **HTTP hooks 环境变量：** URL 环境变量插值需显式 `allowedEnvVars`，防止敏感变量外泄。
- **managed 设置优先级：** `disableAllHooks` 遵循 managed settings 层级，组织策略可强制禁用 hooks（个人不可覆盖）。

### Best Practices

| Do | Don't |
|-----|-------|
| 校验并清洗所有输入 | 盲目信任输入 |
| 变量加引号：`"$VAR"` | 不加引号：`$VAR` |
| 拦截路径穿越（`..`） | 允许任意路径 |
| 用 `$CLAUDE_PROJECT_DIR` 绝对路径 | 硬编码路径 |
| 跳过敏感文件（`.env`、`.git/`、密钥） | 对所有文件一视同仁 |
| 先单独测试 hook | 未测试直接上线 |
| HTTP hooks 显式配置 `allowedEnvVars` | 向 webhook 暴露全部 env |

## Debugging

### Enable Debug Mode

```bash
claude --debug
```

### Verbose Mode

在 Claude Code 中按 `Ctrl+O` 开启 verbose，可看到 hook 执行过程。

### Test Hooks Independently

```bash
# 用样例 JSON 测试
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# 查看退出码
echo $?
```

## Complete Configuration Example

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

## Hook Execution Details

| Aspect | Behavior |
|--------|----------|
| **Timeout** | 默认 60 秒，可按 command 覆盖 |
| **Parallelization** | 所有匹配 hook 并行执行 |
| **Deduplication** | 相同 hook command 去重 |
| **Environment** | 在当前目录 + Claude Code 环境变量中运行 |

## Troubleshooting

### Hook Not Executing
- 检查 JSON 配置语法
- 检查 matcher 是否匹配目标工具名
- 检查脚本存在且可执行：`chmod +x script.sh`
- 运行 `claude --debug` 查看 hook 日志
- 确认 hook 从 stdin 读 JSON（不是命令参数）

### Hook Blocks Unexpectedly
- 用样例 JSON 测试：`echo '{"tool_name": "Write", ...}' | ./hook.py`
- 检查退出码：0 放行，2 阻断
- 查看 stderr（退出码 2 时会展示）

### JSON Parsing Errors
- 始终从 stdin 读取
- 用标准 JSON 解析，避免字符串拼接
- 对缺失字段做兼容处理

## Installation

### Step 1: Create Hooks Directory
```bash
mkdir -p ~/.claude/hooks
```

### Step 2: Copy Example Hooks
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### Step 3: Configure in Settings
编辑 `~/.claude/settings.json` 或 `.claude/settings.json`，填入上文 hook 配置。

## Related Concepts

- **[Checkpoints and Rewind](../08-checkpoints/)** - 保存/恢复会话状态
- **[Slash Commands](../01-slash-commands/)** - 自定义快捷命令
- **[Skills](../03-skills/)** - 可复用自动能力
- **[Subagents](../04-subagents/)** - 委派式任务执行
- **[Plugins](../07-plugins/)** - 打包扩展能力
- **[Advanced Features](../09-advanced-features/)** - 更多高级能力

## Additional Resources

- **[Official Hooks Documentation](https://code.claude.com/docs/en/hooks)** - 官方完整参考
- **[CLI Reference](https://code.claude.com/docs/en/cli-reference)** - CLI 文档
- **[Memory Guide](../02-memory/)** - 持久上下文配置
