<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks / Hooks

Hooks là các script tự động thực thi để phản hồi các sự kiện cụ thể trong các phiên Claude Code. Chúng cho phép tự động hóa, xác thực, quản lý quyền, và workflows tùy chỉnh.

## Tổng Quan / Overview

Hooks là các hành động tự động (lệnh shell, HTTP webhooks, prompts LLM, hoặc đánh giá subagent) thực thi tự động khi các sự kiện cụ thể xảy ra trong Claude Code. Chúng nhận đầu vào JSON và giao tiếp kết quả qua exit codes và đầu ra JSON.

**Tính năng chính:**
- Tự động hóa dựa trên sự kiện
- Đầu vào/ra dựa trên JSON
- Hỗ trợ cho các loại hook command, prompt, HTTP, và agent
- Khớp mẫu cho các hooks cụ thể theo công cụ

## Cấu Hình / Configuration

Hooks được cấu hình trong các file settings với cấu trúc cụ thể:

- `~/.claude/settings.json` - Cài đặt người dùng (tất cả projects)
- `.claude/settings.json` - Cài đặt project (có thể chia sẻ, được commit)
- `.claude/settings.local.json` - Cài đặt project local (không được commit)
- Managed policy - Cài đặt toàn tổ chức
- Plugin `hooks/hooks.json` - Hooks scoped plugin
- Skill/Agent frontmatter - Hooks vòng đời component

### Cấu Trúc Cấu Hình Cơ Bản / Basic Configuration Structure

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

**Các trường chính:**

| Trường | Mô Tả | Ví Dụ |
|-------|-------------|---------|
| `matcher` | Mẫu để khớp tên công cụ (phân biệt hoa/thường) | `"Write"`, `"Edit\|Write"`, `"*"` |
| `hooks` | Mảng định nghĩa hook | `[{ "type": "command", ... }]` |
| `type` | Loại hook: `"command"` (bash), `"prompt"` (LLM), `"http"` (webhook), hoặc `"agent"` (subagent) | `"command"` |
| `command` | Lệnh shell để thực thi | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | Timeout tùy chọn tính bằng giây (mặc định 60) | `30` |
| `once` | Nếu `true`, chạy hook chỉ một lần mỗi phiên | `true` |

### Các Mẫu Matcher / Matcher Patterns

| Mẫu | Mô Tả | Ví Dụ |
|---------|-------------|---------|
| Chuỗi chính xác | Khớp công cụ cụ thể | `"Write"` |
| Mẫu regex | Khớp nhiều công cụ | `"Edit\|Write"` |
| Wildcard | Khớp tất cả công cụ | `"*"` hoặc `""` |
| Công cụ MCP | Mẫu server và công cụ | `"mcp__memory__.*"` |

## Các Loại Hook / Hook Types

Claude Code hỗ trợ bốn loại hook:

### Command Hooks / Hooks Lệnh

Loại hook mặc định. Thực thi một lệnh shell và giao tiếp qua JSON stdin/stdout và exit codes.

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

### HTTP Hooks / Hooks HTTP

> Thêm vào v2.1.63.

Các endpoints webhook từ xa nhận cùng đầu vào JSON như command hooks. HTTP hooks POST JSON đến URL và nhận phản hồi JSON. HTTP hooks được định tuyến qua sandbox khi sandboxing được bật. Nội suy biến môi trường trong URLs yêu cầu danh sách `allowedEnvVars` rõ ràng để bảo mật.

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

**Các thuộc tính chính:**
- `"type": "http"` -- xác định đây là một HTTP hook
- `"url"` -- URL endpoint webhook
- Được định tuyến qua sandbox khi sandbox được bật
- Yêu cầu danh sách `allowedEnvVars` rõ ràng cho bất kỳ nội suy biến môi trường nào trong URL

### Prompt Hooks / Hooks Prompt

Prompts được đánh giá bởi LLM nơi nội dung hook là một prompt mà Claude đánh giá. Chủ yếu được sử dụng với các sự kiện `Stop` và `SubagentStop` để kiểm tra hoàn thành tác vụ thông minh.

```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude completed all requested tasks.",
  "timeout": 30
}
```

LLM đánh giá prompt và trả về một quyết định có cấu trúc (xem [Prompt-Based Hooks](#hooks-dựa-trên-prompt--prompt-based-hooks) để biết chi tiết).

### Agent Hooks / Hooks Agent

Hooks xác thực dựa trên subagent mà spawn một agent chuyên dụng để đánh giá điều kiện hoặc thực hiện các kiểm tra phức tạp. Khác với prompt hooks (đánh giá LLM một turn), agent hooks có thể sử dụng các công cụ và thực hiện suy luận đa bước.

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

**Các thuộc tính chính:**
- `"type": "agent"` -- xác định đây là một agent hook
- `"prompt"` -- mô tả nhiệm vụ cho subagent
- Agent có thể sử dụng các công cụ (Read, Grep, Bash, v.v.) để thực hiện đánh giá của nó
- Trả về một quyết định có cấu trúc tương tự như prompt hooks

## Các Sự Kiện Hook / Hook Events

Claude Code hỗ trợ **25 sự kiện hook**:

| Sự Kiện | Khi Được Kích Hoạt | Matcher Input | Có Chặn | Sử Dụng Phổ Biến |
|-------|---------------|---------------|-----------|------------|
| **SessionStart** | Phiên bắt đầu/tiếp tục/xóa/dồn | startup/resume/clear/compact | Không | Thiết lập môi trường |
| **InstructionsLoaded** | Sau khi CLAUDE.md hoặc file rules được tải | (none) | Không | Sửa đổi/bộ lọc hướng dẫn |
| **UserPromptSubmit** | Người dùng gửi prompt | (none) | Có | Xác thực prompts |
| **PreToolUse** | Trước khi thực thi công cụ | Tên công cụ | Có (allow/deny/ask) | Xác thực, sửa đổi đầu vào |
| **PermissionRequest** | Hộp thoại quyền được hiển thị | Tên công cụ | Có | Tự động phê duyệt/từ chối |
| **PostToolUse** | Sau khi công cụ thành công | Tên công cụ | Không | Thêm ngữ cảnh, feedback |
| **PostToolUseFailure** | Thực thi công cụ thất bại | Tên công cụ | Không | Xử lý lỗi, logging |
| **Notification** | Thông báo được gửi | Loại thông báo | Không | Thông báo tùy chỉnh |
| **SubagentStart** | Subagent được spawn | Tên loại agent | Không | Thiết lập subagent |
| **SubagentStop** | Subagent hoàn thành | Tên loại agent | Có | Xác thực subagent |
| **Stop** | Claude hoàn thành phản hồi | (none) | Có | Kiểm tra hoàn thành tác vụ |
| **StopFailure** | Lỗi API kết thúc turn | (none) | Không | Phục hồi lỗi, logging |
| **TeammateIdle** | Đồng nghiệp nhóm agent rảnh | (none) | Có | Phối hợp đồng nghiệp |
| **TaskCompleted** | Nhiệm vụ được đánh dấu hoàn thành | (none) | Có | Hành động sau tác vụ |
| **TaskCreated** | Nhiệm vụ được tạo qua TaskCreate | (none) | Không | Theo dõi nhiệm vụ, logging |
| **ConfigChange** | File config thay đổi | (none) | Có (trừ policy) | Phản hồi cập nhật config |
| **CwdChanged** | Thư mục làm việc thay đổi | (none) | Không | Thiết lập cụ thể thư mục |
| **FileChanged** | File được watch thay đổi | (none) | Không | Giám sát file, rebuild |
| **PreCompact** | Trước khi dồn ngữ cảnh | manual/auto | Không | Hành động pre-dồn |
| **PostCompact** | Sau khi dồn hoàn thành | (none) | Không | Hành động post-dồn |
| **WorktreeCreate** | Worktree đang được tạo | (none) | Có (trả về path) | Khởi tạo worktree |
| **WorktreeRemove** | Worktree đang được xóa | (none) | Không | Dọn dẹp worktree |
| **Elicitation** | MCP server yêu cầu đầu vào người dùng | (none) | Có | Xác thực đầu vào |
| **ElicitationResult** | Người dùng phản hồi elicitation | (none) | Có | Xử lý phản hồi |
| **SessionEnd** | Phiên kết thúc | (none) | Không | Dọn dẹp, logging cuối |

### PreToolUse

Chạy sau khi Claude tạo tham số công cụ và trước khi xử lý. Sử dụng điều này để xác thực hoặc sửa đổi đầu vào công cụ.

**Cấu Hình:**
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

**Các matcher phổ biến:** `Task`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**Điều khiển đầu ra:**
- `permissionDecision`: `"allow"`, `"deny"`, hoặc `"ask"`
- `permissionDecisionReason`: Giải thích cho quyết định
- `updatedInput`: Các tham số đầu vào công cụ đã sửa đổi

### PostToolUse

Chạy ngay sau khi công cụ hoàn thành. Sử dụng để xác minh, logging, hoặc cung cấp ngữ cảnh trở lại Claude.

**Cấu Hình:**
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

**Điều khiển đầu ra:**
- Quyết định `"block"` nhắc Claude với feedback
- `additionalContext`: Ngữ cảnh được thêm vào cho Claude

### UserPromptSubmit

Chạy khi người dùng gửi prompt, trước khi Claude xử lý nó.

**Cấu Hình:**
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

**Điều khiển đầu ra:**
- `decision`: `"block"` để ngăn chặn xử lý
- `reason`: Giải thích nếu bị chặn
- `additionalContext`: Ngữ cảnh được thêm vào prompt

### Stop và SubagentStop / Stop and SubagentStop

Chạy khi Claude hoàn thành phản hồi (Stop) hoặc một subagent hoàn thành (SubagentStop). Hỗ trợ đánh giá dựa trên prompt để kiểm tra hoàn thành tác vụ thông minh.

**Trường đầu vào thêm:** Cả hai hooks `Stop` và `SubagentStop` nhận một trường `last_assistant_message` trong đầu vào JSON của chúng, chứa thông báo cuối cùng từ Claude hoặc subagent trước khi dừng. Điều này hữu ích để đánh giá hoàn thành tác vụ.

**Cấu Hình:**
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

Chạy khi một subagent bắt đầu thực thi. Matcher input là tên loại agent, cho phép hooks nhắm đến các loại subagent cụ thể.

**Cấu Hình:**
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

Chạy khi phiên bắt đầu hoặc tiếp tục. Có thể persist các biến môi trường.

**Matchers:** `startup`, `resume`, `clear`, `compact`

**Tính năng đặc biệt:** Sử dụng `CLAUDE_ENV_FILE` để persist các biến môi trường (cũng có sẵn trong các hooks `CwdChanged` và `FileChanged`):

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

Chạy khi phiên kết thúc để thực hiện dọn dẹp hoặc logging cuối cùng. Không thể chấm dứt sự kết thúc.

**Các giá trị trường reason:**
- `clear` - Người dùng xóa phiên
- `logout` - Người dùng đăng xuất
- `prompt_input_exit` - Người dùng thoát qua đầu vào prompt
- `other` - Lý do khác

**Cấu Hình:**
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

### Sự Kiện Notification / Notification Event

Các matcher được cập nhật cho các sự kiện thông báo:
- `permission_prompt` - Thông báo yêu cầu quyền
- `idle_prompt` - Thông báo trạng thái rảnh
- `auth_success` - Xác thực thành công
- `elicitation_dialog` - Hộp thoại được hiển thị cho người dùng

## Hooks Scoped Component / Component-Scoped Hooks

Hooks có thể được gắn vào các component cụ thể (skills, agents, commands) trong frontmatter của chúng:

**Trong SKILL.md, agent.md, hoặc command.md:**

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
          once: true  # Chỉ chạy một lần mỗi phiên
---
```

**Các sự kiện được hỗ trợ cho component hooks:** `PreToolUse`, `PostToolUse`, `Stop`

Điều này cho phép định nghĩa hooks trực tiếp trong component sử dụng chúng, giữ code liên quan cùng nhau.

### Hooks trong Frontmatter Subagent / Hooks in Subagent Frontmatter

Khi một hook `Stop` được định nghĩa trong frontmatter của một subagent, nó tự động được chuyển đổi thành một hook `SubagentStop` scoped cho subagent đó. Điều này đảm bảo rằng hook stop chỉ kích hoạt khi subagent cụ thể đó hoàn thành, thay vì khi phiên chính dừng.

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # Hook Stop ở trên tự chuyển thành SubagentStop cho subagent này
---
```

## Sự Kiện PermissionRequest / PermissionRequest Event

Xử lý các yêu cầu quyền với định dạng đầu ra tùy chỉnh:

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

## Đầu Vào Và Đầu Ra Hook / Hook Input and Output

### Đầu Vào JSON (qua stdin) / JSON Input (via stdin)

Tất cả hooks nhận đầu vào JSON qua stdin:

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

**Các trường phổ biến:**

| Trường | Mô Tả |
|-------|-------------|
| `session_id` | Định danh phiên duy nhất |
| `transcript_path` | Đường dẫn đến file transcript hội thoại |
| `cwd` | Thư mục làm việc hiện tại |
| `hook_event_name` | Tên của sự kiện kích hoạt hook |
| `agent_id` | Định danh của agent chạy hook này |
| `agent_type` | Loại agent (`"main"`, tên loại subagent, v.v.) |
| `worktree` | Đường dẫn đến git worktree, nếu agent chạy trong một |

### Exit Codes

| Exit Code | Ý Nghĩa | Hành Vi |
|-----------|---------|----------|
| **0** | Thành công | Tiếp tục, phân tích cú pháp JSON stdout |
| **2** | Lỗi chặn | Chặn thao tác, stderr được hiển thị như lỗi |
| **Khác** | Lỗi không chặn | Tiếp tục, stderr được hiển thị trong chế độ verbose |

### Đầu Ra JSON (stdout, exit code 0) / JSON Output (stdout, exit code 0)

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

## Các Biến Môi Trường / Environment Variables

| Biến | Khả Dụng | Mô Tả |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | Tất cả hooks | Đường dẫn tuyệt đối đến thư mục gốc project |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | Đường dẫn file để persist env vars |
| `CLAUDE_CODE_REMOTE` | Tất cả hooks | `"true"` nếu chạy trong môi trường từ xa |
| `${CLAUDE_PLUGIN_ROOT}` | Hooks plugin | Đường dẫn đến thư mục plugin |
| `${CLAUDE_PLUGIN_DATA}` | Hooks plugin | Đường dẫn đến thư mục dữ liệu plugin |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | Hooks SessionEnd | Timeout có thể cấu hình tính bằng mili giây cho hooks SessionEnd (ghi đè mặc định) |

## Hooks Dựa Trên Prompt / Prompt-Based Hooks

Đối với các sự kiện `Stop` và `SubagentStop`, bạn có thể sử dụng đánh giá dựa trên LLM:

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

**Schema Phản Hồi LLM:**
```json
{
  "decision": "approve",
  "reason": "All tasks completed successfully",
  "continue": false,
  "stopReason": "Task complete"
}
```

## Ví Dụ / Examples

### Ví Dụ 1: Trình Xác Thực Lệnh Bash (PreToolUse) / Example 1: Bash Command Validator

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

### Ví Dụ 2: Bộ Quét Bảo Mật (PostToolUse) / Example 2: Security Scanner

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

### Ví Dụ 3: Tự Động Format Code (PostToolUse) / Example 3: Auto-Format Code

**File:** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# Đọc JSON từ stdin
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# Format dựa trên phần mở rộng file
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

### Ví Dụ 4: Trình Xác Thực Prompt (UserPromptSubmit) / Example 4: Prompt Validator

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

### Ví Dụ 5: Stop Hook Thông Minh (Dựa Trên Prompt) / Example 5: Intelligent Stop Hook

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

## Hooks Plugin / Plugin Hooks

Plugins có thể bao gồm hooks trong file `hooks/hooks.json` của chúng:

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

**Các Biến Môi Trường Trong Hooks Plugin:**
- `${CLAUDE_PLUGIN_ROOT}` - Đường dẫn đến thư mục plugin
- `${CLAUDE_PLUGIN_DATA}` - Đường dẫn đến thư mục dữ liệu plugin

Điều này cho phép các plugins bao gồm các hook xác thực và tự động hóa tùy chỉnh.

## Hooks Công Cụ MCP / MCP Tool Hooks

Các công cụ MCP theo mẫu `mcp__<server>__<tool>`:

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

## Cân Nhắc Bảo Mật / Security Considerations

### Tuyên Bố Từ Chối Trách Nhiệm / Disclaimer

**SỬ DỤNG VỚI RỦI RO RIÊNG CỦA BẠN**: Hooks thực thi các lệnh shell tùy ý. Bạn chịu trách nhiệm duy nhất cho:
- Các lệnh bạn cấu hình
- Quyền truy cập/sửa đổi file
- Mất dữ liệu hoặc hư hại hệ thống tiềm ẩn
- Testing hooks trong môi trường an toàn trước khi sử dụng production

### Ghi Chú Bảo Mật / Security Notes

- **Cần tin cậy workspace:** Các output commands hook `statusLine` và `fileSuggestion` bây giờ yêu cầu chấp nhận tin cậy workspace trước khi chúng có hiệu lực.
- **HTTP hooks và biến môi trường:** HTTP hooks yêu cầu danh sách `allowedEnvVars` rõ ràng để sử dụng nội suy biến môi trường trong URLs. Điều này ngăn chặn lộ vô ý các biến môi trường nhạy cảm đến các endpoints từ xa.
- **Phân cấp settings được quản lý:** Cài đặt `disableAllHooks` bây giờ tôn trọng phân cấp settings được quản lý, nghĩa là settings cấp tổ chức có thể thực thi vô hiệu hóa hook mà người dùng cá nhân không thể ghi đè.

### Thực Hành Tốt Nhất / Best Practices

| Nên | Không Nên |
|-----|-------|
| Xác thực và vệ sinh tất cả đầu vào | Tin tưởng dữ liệu đầu vào mù quáng |
| Trích dẫn biến shell: `"$VAR"` | Sử dụng không trích dẫn: `$VAR` |
| Chặn đường dẫn path traversal (`..`) | Cho phép các đường dẫn tùy ý |
| Sử dụng đường dẫn tuyệt đối với `$CLAUDE_PROJECT_DIR` | Hardcode các đường dẫn |
| Bỏ qua các file nhạy cảm (`.env`, `.git/`, keys) | Xử lý tất cả các files |
| Test hooks trong cô lập trước | Triển khai hooks chưa được test |
| Sử dụng `allowedEnvVars` rõ ràng cho HTTP hooks | Lộ tất cả env vars cho webhooks |

## Gỡ Lỗi / Debugging

### Kích Hoạt Chế Độ Debug / Enable Debug Mode

Chạy Claude với cờ debug để xem logs chi tiết hook:

```bash
claude --debug
```

### Chế Độ Verbose / Verbose Mode

Sử dụng `Ctrl+O` trong Claude Code để kích hoạt chế độ verbose và xem tiến độ thực thi hook.

### Test Hooks Độc Lập / Test Hooks Independently

```bash
# Test với đầu vào JSON mẫu
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# Kiểm tra exit code
echo $?
```

## Cài Đặt / Installation

### Bước 1: Tạo Thư Mục Hooks
```bash
mkdir -p ~/.claude/hooks
```

### Bước 2: Sao Chép Hooks Ví Dụ
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### Bước 3: Cấu Hình Trong Settings
Chỉnh sửa `~/.claude/settings.json` hoặc `.claude/settings.json` với cấu hình hook được hiển thị ở trên.

## Các Khái Niệm Liên Quan / Related Concepts

- **[Checkpoints và Rewind](../08-checkpoints/)** - Lưu và khôi phục trạng thái hội thoại
- **[Slash Commands](../01-slash-commands/)** - Tạo các lệnh slash tùy chỉnh
- **[Skills](../03-skills/)** - Các khả năng tự động có thể tái sử dụng
- **[Subagents](../04-subagents/)** - Thực thi nhiệm vụ được ủy quyền
- **[Plugins](../07-plugins/)** - Các gói mở rộng được đóng gói
- **[Tính Năng Nâng Cao](../09-advanced-features/)** - Khám phá các khả năng nâng cao của Claude Code

## Tài Nguyên Thêm / Additional Resources

- **[Tài Liệu Hooks Chính Thức](https://code.claude.com/docs/en/hooks)** - Tham chiếu hooks hoàn chỉnh
- **[CLI Reference](https://code.claude.com/docs/en/cli-reference)** - Tài liệu giao diện dòng lệnh
- **[Hướng Dẫn Memory](../02-memory/)** - Cấu hình ngữ cảnh liên tục
