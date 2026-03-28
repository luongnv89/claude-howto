<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks

Hooks là các script tự động chạy khi phản ứng với các sự kiện cụ thể trong phiên Claude Code. Chúng cho phép tự động hóa, xác thực, quản lý quyền và các quy trình làm việc tùy chỉnh.

## Tổng quan

Hooks là các hành động tự động (lệnh shell, HTTP webhooks, LLM prompts hoặc đánh giá subagent) chạy tự động khi các sự kiện cụ thể xảy ra trong Claude Code. Chúng nhận đầu vào JSON và giao tiếp kết quả qua exit codes và đầu ra JSON.

**Tính năng chính:**
- Tự động hóa theo sự kiện
- Đầu vào/đầu ra dạng JSON
- Hỗ trợ hook loại command, prompt, HTTP và agent
- Khớp pattern cho hooks theo tool cụ thể

## Cấu hình

Hooks được cấu hình trong các file settings với cấu trúc cụ thể:

- `~/.claude/settings.json` - Cài đặt người dùng (tất cả dự án)
- `.claude/settings.json` - Cài đặt dự án (có thể chia sẻ, commit được)
- `.claude/settings.local.json` - Cài đặt dự án cục bộ (không commit)
- Managed policy - Cài đặt toàn tổ chức
- Plugin `hooks/hooks.json` - Hooks theo phạm vi plugin
- Frontmatter Skill/Agent - Hooks theo vòng đời component

### Cấu trúc cơ bản

```json
{
  "hooks": {
    "TênSựKiện": [
      {
        "matcher": "PatternTool",
        "hooks": [
          {
            "type": "command",
            "command": "lệnh-của-bạn",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**Các trường chính:**

| Trường | Mô tả | Ví dụ |
|--------|-------|-------|
| `matcher` | Pattern khớp tên tool (phân biệt chữ hoa/thường) | `"Write"`, `"Edit\|Write"`, `"*"` |
| `hooks` | Mảng định nghĩa hook | `[{ "type": "command", ... }]` |
| `type` | Loại hook: `"command"` (bash), `"prompt"` (LLM), `"http"` (webhook), hoặc `"agent"` (subagent) | `"command"` |
| `command` | Lệnh shell cần thực thi | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | Timeout tùy chọn tính bằng giây (mặc định 60) | `30` |
| `once` | Nếu `true`, chỉ chạy hook một lần mỗi phiên | `true` |

### Patterns cho Matcher

| Pattern | Mô tả | Ví dụ |
|---------|-------|-------|
| Chuỗi chính xác | Khớp tool cụ thể | `"Write"` |
| Regex pattern | Khớp nhiều tools | `"Edit\|Write"` |
| Ký tự đại diện | Khớp tất cả tools | `"*"` hoặc `""` |
| MCP tools | Pattern server và tool | `"mcp__memory__.*"` |

## Các loại Hook

Claude Code hỗ trợ bốn loại hook:

### Command Hooks

Loại hook mặc định. Thực thi một lệnh shell và giao tiếp qua JSON stdin/stdout và exit codes.

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

### HTTP Hooks

> Thêm vào từ v2.1.63.

Các endpoint webhook từ xa nhận cùng đầu vào JSON như command hooks. HTTP hooks POST JSON đến URL và nhận phản hồi JSON. HTTP hooks được định tuyến qua sandbox khi bật sandboxing. Nội suy biến môi trường trong URL yêu cầu danh sách `allowedEnvVars` rõ ràng vì lý do bảo mật.

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

**Thuộc tính chính:**
- `"type": "http"` -- xác định đây là HTTP hook
- `"url"` -- URL endpoint webhook
- Định tuyến qua sandbox khi sandbox được bật
- Yêu cầu danh sách `allowedEnvVars` rõ ràng cho bất kỳ nội suy biến môi trường nào trong URL

### Prompt Hooks

Các prompts được LLM đánh giá, trong đó nội dung hook là một prompt mà Claude đánh giá. Chủ yếu dùng với sự kiện `Stop` và `SubagentStop` để kiểm tra hoàn thành tác vụ thông minh.

```json
{
  "type": "prompt",
  "prompt": "Đánh giá xem Claude có hoàn thành tất cả tác vụ được yêu cầu không.",
  "timeout": 30
}
```

LLM đánh giá prompt và trả về quyết định có cấu trúc (xem [Hooks dựa trên Prompt](#hooks-dựa-trên-prompt) để biết chi tiết).

### Agent Hooks

Hooks xác minh dựa trên subagent — tạo ra một agent chuyên dụng để đánh giá điều kiện hoặc thực hiện kiểm tra phức tạp. Không giống prompt hooks (đánh giá LLM một lượt), agent hooks có thể dùng tools và thực hiện lý luận nhiều bước.

```json
{
  "type": "agent",
  "prompt": "Xác minh các thay đổi code tuân theo hướng dẫn kiến trúc. Kiểm tra tài liệu thiết kế liên quan và so sánh.",
  "timeout": 120
}
```

**Thuộc tính chính:**
- `"type": "agent"` -- xác định đây là agent hook
- `"prompt"` -- mô tả tác vụ cho subagent
- Agent có thể dùng tools (Read, Grep, Bash, v.v.) để thực hiện đánh giá
- Trả về quyết định có cấu trúc tương tự prompt hooks

## Các sự kiện Hook

Claude Code hỗ trợ **25 sự kiện hook**:

| Sự kiện | Khi nào kích hoạt | Đầu vào Matcher | Có thể chặn | Dùng phổ biến |
|---------|------------------|-----------------|-------------|--------------|
| **SessionStart** | Phiên bắt đầu/tiếp tục/xóa/compact | startup/resume/clear/compact | Không | Thiết lập môi trường |
| **InstructionsLoaded** | Sau khi tải CLAUDE.md hoặc file quy tắc | (không có) | Không | Sửa/lọc hướng dẫn |
| **UserPromptSubmit** | Người dùng gửi prompt | (không có) | Có | Xác thực prompts |
| **PreToolUse** | Trước khi thực thi tool | Tên tool | Có (allow/deny/ask) | Xác thực, sửa đầu vào |
| **PermissionRequest** | Hộp thoại quyền hiển thị | Tên tool | Có | Tự động chấp nhận/từ chối |
| **PostToolUse** | Sau khi tool thành công | Tên tool | Không | Thêm ngữ cảnh, phản hồi |
| **PostToolUseFailure** | Thực thi tool thất bại | Tên tool | Không | Xử lý lỗi, ghi log |
| **Notification** | Thông báo được gửi | Loại thông báo | Không | Thông báo tùy chỉnh |
| **SubagentStart** | Subagent được tạo | Tên loại agent | Không | Thiết lập subagent |
| **SubagentStop** | Subagent hoàn thành | Tên loại agent | Có | Xác thực subagent |
| **Stop** | Claude hoàn thành phản hồi | (không có) | Có | Kiểm tra hoàn thành tác vụ |
| **StopFailure** | Lỗi API kết thúc lượt | (không có) | Không | Phục hồi lỗi, ghi log |
| **TeammateIdle** | Thành viên nhóm agent nhàn rỗi | (không có) | Có | Phối hợp thành viên |
| **TaskCompleted** | Tác vụ được đánh dấu hoàn thành | (không có) | Có | Hành động sau tác vụ |
| **TaskCreated** | Tác vụ được tạo qua TaskCreate | (không có) | Không | Theo dõi tác vụ, ghi log |
| **ConfigChange** | File cấu hình thay đổi | (không có) | Có (trừ policy) | Phản ứng cập nhật cấu hình |
| **CwdChanged** | Thư mục làm việc thay đổi | (không có) | Không | Thiết lập theo thư mục |
| **FileChanged** | File được theo dõi thay đổi | (không có) | Không | Giám sát file, rebuild |
| **PreCompact** | Trước khi compact ngữ cảnh | manual/auto | Không | Hành động trước compact |
| **PostCompact** | Sau khi compact hoàn thành | (không có) | Không | Hành động sau compact |
| **WorktreeCreate** | Worktree đang được tạo | (không có) | Có (trả về path) | Khởi tạo worktree |
| **WorktreeRemove** | Worktree đang bị xóa | (không có) | Không | Dọn dẹp worktree |
| **Elicitation** | MCP server yêu cầu đầu vào người dùng | (không có) | Có | Xác thực đầu vào |
| **ElicitationResult** | Người dùng phản hồi elicitation | (không có) | Có | Xử lý phản hồi |
| **SessionEnd** | Phiên kết thúc | (không có) | Không | Dọn dẹp, ghi log cuối |

### PreToolUse

Chạy sau khi Claude tạo tham số tool và trước khi xử lý. Dùng để xác thực hoặc sửa đầu vào tool.

**Cấu hình:**
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

**Matchers phổ biến:** `Task`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**Kiểm soát đầu ra:**
- `permissionDecision`: `"allow"`, `"deny"`, hoặc `"ask"`
- `permissionDecisionReason`: Giải thích cho quyết định
- `updatedInput`: Tham số đầu vào tool đã được sửa

### PostToolUse

Chạy ngay sau khi tool hoàn thành. Dùng để xác minh, ghi log, hoặc cung cấp ngữ cảnh lại cho Claude.

**Cấu hình:**
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

**Kiểm soát đầu ra:**
- Quyết định `"block"` nhắc Claude với phản hồi
- `additionalContext`: Ngữ cảnh thêm cho Claude

### UserPromptSubmit

Chạy khi người dùng gửi prompt, trước khi Claude xử lý.

**Cấu hình:**
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

**Kiểm soát đầu ra:**
- `decision`: `"block"` để ngăn xử lý
- `reason`: Giải thích nếu bị chặn
- `additionalContext`: Ngữ cảnh thêm vào prompt

### Stop và SubagentStop

Chạy khi Claude hoàn thành phản hồi (Stop) hoặc subagent hoàn thành (SubagentStop). Hỗ trợ đánh giá dựa trên prompt để kiểm tra hoàn thành tác vụ thông minh.

**Trường đầu vào bổ sung:** Cả hai hook `Stop` và `SubagentStop` nhận trường `last_assistant_message` trong đầu vào JSON, chứa tin nhắn cuối cùng từ Claude hoặc subagent trước khi dừng. Hữu ích để đánh giá hoàn thành tác vụ.

**Cấu hình:**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Đánh giá xem Claude có hoàn thành tất cả tác vụ được yêu cầu không.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### SubagentStart

Chạy khi subagent bắt đầu thực thi. Đầu vào matcher là tên loại agent, cho phép hooks nhắm mục tiêu các loại subagent cụ thể.

**Cấu hình:**
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

Chạy khi phiên bắt đầu hoặc tiếp tục. Có thể duy trì biến môi trường.

**Matchers:** `startup`, `resume`, `clear`, `compact`

**Tính năng đặc biệt:** Dùng `CLAUDE_ENV_FILE` để duy trì biến môi trường (cũng có sẵn trong hooks `CwdChanged` và `FileChanged`):

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

Chạy khi phiên kết thúc để dọn dẹp hoặc ghi log cuối. Không thể chặn quá trình kết thúc.

**Giá trị trường reason:**
- `clear` - Người dùng xóa phiên
- `logout` - Người dùng đăng xuất
- `prompt_input_exit` - Người dùng thoát qua prompt input
- `other` - Lý do khác

**Cấu hình:**
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

### Sự kiện Notification

Các matchers cập nhật cho sự kiện thông báo:
- `permission_prompt` - Thông báo yêu cầu quyền
- `idle_prompt` - Thông báo trạng thái nhàn rỗi
- `auth_success` - Xác thực thành công
- `elicitation_dialog` - Hộp thoại hiển thị cho người dùng

## Hooks theo phạm vi Component

Hooks có thể gắn vào các component cụ thể (skills, agents, commands) trong frontmatter của chúng:

**Trong SKILL.md, agent.md, hoặc command.md:**

```yaml
---
name: secure-operations
description: Thực hiện các thao tác với kiểm tra bảo mật
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

Điều này cho phép định nghĩa hooks trực tiếp trong component sử dụng chúng, giữ code liên quan ở cùng nơi.

### Hooks trong Frontmatter Subagent

Khi hook `Stop` được định nghĩa trong frontmatter của subagent, nó tự động được chuyển đổi thành hook `SubagentStop` có phạm vi theo subagent đó. Điều này đảm bảo hook stop chỉ kích hoạt khi subagent cụ thể đó hoàn thành, không phải khi phiên chính dừng.

```yaml
---
name: code-review-agent
description: Subagent review code tự động
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Xác minh review code đã đầy đủ và hoàn chỉnh."
  # Hook Stop ở trên tự động chuyển thành SubagentStop cho subagent này
---
```

## Sự kiện PermissionRequest

Xử lý yêu cầu quyền với định dạng đầu ra tùy chỉnh:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow|deny",
      "updatedInput": {},
      "message": "Tin nhắn tùy chỉnh",
      "interrupt": false
    }
  }
}
```

## Đầu vào và Đầu ra của Hook

### Đầu vào JSON (qua stdin)

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

| Trường | Mô tả |
|--------|-------|
| `session_id` | Định danh phiên duy nhất |
| `transcript_path` | Đường dẫn đến file transcript hội thoại |
| `cwd` | Thư mục làm việc hiện tại |
| `hook_event_name` | Tên sự kiện đã kích hoạt hook |
| `agent_id` | Định danh agent đang chạy hook này |
| `agent_type` | Loại agent (`"main"`, tên loại subagent, v.v.) |
| `worktree` | Đường dẫn đến git worktree, nếu agent đang chạy trong đó |

### Exit Codes

| Exit Code | Ý nghĩa | Hành vi |
|-----------|---------|---------|
| **0** | Thành công | Tiếp tục, phân tích JSON stdout |
| **2** | Lỗi chặn | Chặn thao tác, stderr hiển thị như lỗi |
| **Khác** | Lỗi không chặn | Tiếp tục, stderr hiển thị ở chế độ verbose |

### Đầu ra JSON (stdout, exit code 0)

```json
{
  "continue": true,
  "stopReason": "Tin nhắn tùy chọn nếu dừng",
  "suppressOutput": false,
  "systemMessage": "Tin nhắn cảnh báo tùy chọn",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "File ở trong thư mục được phép",
    "updatedInput": {
      "file_path": "/modified/path.js"
    }
  }
}
```

## Biến môi trường

| Biến | Phạm vi | Mô tả |
|------|---------|-------|
| `CLAUDE_PROJECT_DIR` | Tất cả hooks | Đường dẫn tuyệt đối đến thư mục gốc dự án |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | Đường dẫn file để duy trì biến môi trường |
| `CLAUDE_CODE_REMOTE` | Tất cả hooks | `"true"` nếu đang chạy trong môi trường remote |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin hooks | Đường dẫn đến thư mục plugin |
| `${CLAUDE_PLUGIN_DATA}` | Plugin hooks | Đường dẫn đến thư mục data của plugin |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd hooks | Timeout có thể cấu hình tính bằng milliseconds cho SessionEnd hooks (ghi đè mặc định) |

## Hooks dựa trên Prompt

Với sự kiện `Stop` và `SubagentStop`, bạn có thể dùng đánh giá dựa trên LLM:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review xem tất cả tác vụ đã hoàn thành chưa. Trả về quyết định của bạn.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**Schema phản hồi LLM:**
```json
{
  "decision": "approve",
  "reason": "Tất cả tác vụ đã hoàn thành thành công",
  "continue": false,
  "stopReason": "Tác vụ hoàn thành"
}
```

## Ví dụ

### Ví dụ 1: Trình xác thực lệnh Bash (PreToolUse)

**File:** `.claude/hooks/validate-bash.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"\brm\s+-rf\s+/", "Chặn lệnh nguy hiểm rm -rf /"),
    (r"\bsudo\s+rm", "Chặn lệnh sudo rm"),
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
            sys.exit(2)  # Exit 2 = lỗi chặn

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**Cấu hình:**
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

### Ví dụ 2: Quét bảo mật (PostToolUse)

**File:** `.claude/hooks/security-scan.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

SECRET_PATTERNS = [
    (r"password\s*=\s*['\"][^'\"]+['\"]", "Có thể có password hardcoded"),
    (r"api[_-]?key\s*=\s*['\"][^'\"]+['\"]", "Có thể có API key hardcoded"),
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
                "additionalContext": f"Cảnh báo bảo mật cho {file_path}: " + "; ".join(warnings)
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Ví dụ 3: Tự động format code (PostToolUse)

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

# Format theo phần mở rộng file
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

### Ví dụ 4: Xác thực Prompt (UserPromptSubmit)

**File:** `.claude/hooks/validate-prompt.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"delete\s+(all\s+)?database", "Nguy hiểm: xóa database"),
    (r"rm\s+-rf\s+/", "Nguy hiểm: xóa root"),
]

def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("user_prompt", "") or input_data.get("prompt", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            output = {
                "decision": "block",
                "reason": f"Bị chặn: {message}"
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Ví dụ 5: Hook Stop thông minh (Dựa trên Prompt)

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review xem Claude đã hoàn thành tất cả tác vụ được yêu cầu chưa. Kiểm tra: 1) Tất cả file đã được tạo/sửa chưa? 2) Có lỗi chưa giải quyết không? Nếu chưa hoàn thành, giải thích còn thiếu gì.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### Ví dụ 6: Theo dõi sử dụng Context (Cặp Hooks)

Theo dõi mức tiêu thụ token mỗi request bằng cách dùng hooks `UserPromptSubmit` (trước tin nhắn) và `Stop` (sau phản hồi) cùng nhau.

**File:** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
Context Usage Tracker - Theo dõi tiêu thụ token mỗi request.

Dùng UserPromptSubmit làm hook "pre-message" và Stop làm hook "post-response"
để tính delta sử dụng token cho mỗi request.

Phương pháp đếm Token:
1. Ước tính ký tự (mặc định): ~4 ký tự mỗi token, không cần dependency
2. tiktoken (tùy chọn): Chính xác hơn (~90-95%), yêu cầu: pip install tiktoken
"""
import json
import os
import sys
import tempfile

# Cấu hình
CONTEXT_LIMIT = 128000  # Cửa sổ ngữ cảnh của Claude (điều chỉnh theo model)
USE_TIKTOKEN = False    # Đặt True nếu tiktoken được cài để có độ chính xác tốt hơn


def get_state_file(session_id: str) -> str:
    """Lấy đường dẫn file tạm để lưu số token trước tin nhắn, cô lập theo phiên."""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    Đếm token trong văn bản.

    Dùng tiktoken với mã hóa p50k_base nếu có (~90-95% chính xác),
    ngược lại dùng ước tính ký tự (~80-90% chính xác).
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # Dùng ước tính thay thế

    # Ước tính dựa trên ký tự: ~4 ký tự mỗi token cho tiếng Anh
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """Đọc và nối tất cả nội dung từ file transcript."""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
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
    """Hook trước tin nhắn: Lưu số token hiện tại trước request."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """Hook sau phản hồi: Tính và báo cáo delta token."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    method = "tiktoken" if USE_TIKTOKEN else "ước tính"
    print(f"Context ({method}): ~{current_tokens:,} tokens ({percentage:.1f}% đã dùng, ~{remaining:,} còn lại)", file=sys.stderr)
    if delta_tokens > 0:
        print(f"Request này: ~{delta_tokens:,} tokens", file=sys.stderr)


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

**Cấu hình:**
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

**Cách hoạt động:**
1. `UserPromptSubmit` kích hoạt trước khi prompt của bạn được xử lý — lưu số token hiện tại
2. `Stop` kích hoạt sau khi Claude phản hồi — tính delta và báo cáo mức sử dụng
3. Mỗi phiên được cô lập qua `session_id` trong tên file tạm

**Phương pháp đếm Token:**

| Phương pháp | Độ chính xác | Dependency | Tốc độ |
|-------------|-------------|-----------|--------|
| Ước tính ký tự | ~80-90% | Không có | <1ms |
| tiktoken (p50k_base) | ~90-95% | `pip install tiktoken` | <10ms |

> **Lưu ý:** Anthropic chưa phát hành tokenizer offline chính thức. Cả hai phương pháp đều là xấp xỉ. Transcript bao gồm prompts người dùng, phản hồi của Claude và đầu ra tool, nhưng KHÔNG bao gồm system prompts hoặc ngữ cảnh nội bộ.

### Ví dụ 7: Chế độ Tự động Thích nghi (PostToolUse)

Tự động học từ các lần bạn chấp nhận tool và cập nhật quyền trong `~/.claude/settings.json`. Mỗi khi bạn chấp nhận thực thi tool, hook tổng quát hóa lệnh thành một quy tắc quyền có thể tái sử dụng — để bạn không bao giờ phải chấp nhận cùng loại lệnh hai lần. Các lệnh nguy hiểm/không thể hoàn tác **không bao giờ** được ghi nhớ.

Khi chạy lần đầu, nó gieo cấu hình ban đầu với các quyền nền tương đương auto-mode (đọc/ghi file, git, package managers, CLI tools phổ biến).

**File:** `.claude/hooks/auto-adapt-mode.py`

```python
#!/usr/bin/env python3
"""
auto-adapt-mode: Học từ các lần user chấp nhận tool và cập nhật cấu hình Claude.

Loại Hook: PostToolUse
Sự kiện: Kích hoạt sau khi tool được thực thi thành công (nghĩa là user đã chấp nhận)
"""

import json
import os
import sys
import re
from pathlib import Path

SETTINGS_PATH = Path.home() / ".claude" / "settings.json"
LOG_PATH = Path.home() / ".claude" / "auto-adapt-mode.log"

# Nền tảng auto-mode: các thao tác an toàn, cục bộ, có thể hoàn tác
AUTO_MODE_BASELINE = [
    "Read(*)", "Edit(*)", "Write(*)", "Glob(*)", "Grep(*)",
    "Bash(git status:*)", "Bash(git log:*)", "Bash(git diff:*)",
    "Bash(git add:*)", "Bash(git commit:*)", "Bash(git checkout:*)",
    "Bash(npm install:*)", "Bash(npm test:*)", "Bash(npm run:*)",
    "Bash(pip install:*)", "Bash(pytest:*)",
    "Bash(ls:*)", "Bash(cat:*)", "Bash(find:*)", "Bash(mkdir:*)",
    "Bash(cp:*)", "Bash(mv:*)", "Bash(chmod:*)",
    "Bash(gh pr view:*)", "Bash(gh issue list:*)",
    "Agent(*)", "Skill(*)", "WebSearch(*)", "WebFetch(*)",
    # ... (danh sách đầy đủ bao gồm 70+ pattern an toàn)
]

# Các lệnh KHÔNG BAO GIỜ được tự động ghi nhớ
DANGEROUS_PATTERNS = [
    r"rm\s+(-[a-zA-Z]*r[a-zA-Z]*|--recursive)",   # rm -rf
    r"git\s+push\s+(-[a-zA-Z]*f|--force)",          # force push
    r"git\s+reset\s+--hard",                         # hard reset
    r"DROP\s+(TABLE|DATABASE)",                       # SQL phá hủy
    r"curl\s+.*\|\s*(bash|sh)",                       # pipe to shell
    r"sudo\b",                                        # leo thang đặc quyền
    r"docker\s+(rm|rmi|system\s+prune)",              # container phá hủy
    r"kubectl\s+delete",                              # k8s phá hủy
    r"terraform\s+destroy",                           # hạ tầng phá hủy
    r"npm\s+publish",                                 # publish không thể hoàn tác
    r"deploy\s+.*prod",                               # deploy production
    # ... (danh sách đầy đủ bao gồm 25+ pattern)
]


def is_dangerous_command(command: str) -> bool:
    """Kiểm tra xem lệnh bash có khớp với pattern nguy hiểm không."""
    return any(re.search(p, command, re.IGNORECASE) for p in DANGEROUS_PATTERNS)


def generalize_tool_permission(tool_name: str, tool_input: dict) -> str | None:
    """Chuyển đổi một lần gọi tool cụ thể thành quy tắc quyền tổng quát."""
    if tool_name == "Bash":
        command = tool_input.get("command", "")
        if not command or is_dangerous_command(command):
            return None
        parts = command.strip().split()
        base = parts[0]
        compound = ["git", "npm", "npx", "pip", "cargo", "go", "gh", "python3"]
        if base in compound and len(parts) > 1:
            sub = parts[1]
            if sub.lower() in {"rm", "delete", "destroy", "publish"}:
                return None
            return f"Bash({base} {sub}:*)"
        return f"Bash({base}:*)"
    elif tool_name == "Bash":  # Không bao giờ cho phép Bash(*) chung
        return None
    else:
        return f"{tool_name}(*)"


def main():
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    tool_name = hook_input.get("tool_name", "")
    tool_input = hook_input.get("tool_input", {})
    if not tool_name:
        sys.exit(0)

    settings = json.load(open(SETTINGS_PATH)) if SETTINGS_PATH.exists() else {}
    allow = settings.setdefault("permissions", {}).setdefault("allow", [])

    marker = Path.home() / ".claude" / ".auto-adapt-mode-initialized"
    if not marker.exists():
        existing = set(allow)
        for rule in AUTO_MODE_BASELINE:
            if rule not in existing:
                allow.append(rule)
        marker.touch()

    rule = generalize_tool_permission(tool_name, tool_input)
    if rule and rule not in allow:
        allow.append(rule)
        with open(SETTINGS_PATH, "w") as f:
            json.dump(settings, f, indent=2)
            f.write("\n")

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**Cấu hình:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/auto-adapt-mode.py\"",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

**Cách hoạt động:**
1. `PostToolUse` kích hoạt sau **mỗi** lần thực thi tool thành công (nghĩa là bạn đã chấp nhận)
2. Hook trích xuất tên tool và đầu vào, sau đó tổng quát hóa thành quy tắc quyền
3. Các lệnh phức hợp như `git push origin main` trở thành `Bash(git push:*)` — khớp với mọi biến thể `git push`
4. Quy tắc được thêm vào `~/.claude/settings.json` → `permissions.allow` nếu chưa có
5. Khi chạy lần đầu, gieo ~70 quyền nền tảng tương đương auto-mode

**Đảm bảo an toàn:**
- Các lệnh nguy hiểm (force push, rm -rf, sudo, DROP TABLE, v.v.) **không bao giờ** được ghi nhớ
- Các thao tác không thể hoàn tác (npm publish, terraform destroy, deploy prod) **luôn bị chặn**
- Các lệnh trong danh sách `deny` không bao giờ bị ghi đè
- Hook không bao giờ chặn thực thi tool (luôn thoát 0)
- File log tại `~/.claude/auto-adapt-mode.log` theo dõi tất cả quyết định để kiểm tra

**Ví dụ tổng quát hóa:**

| Bạn chấp nhận | Quy tắc được thêm | Bao phủ |
|--------------|------------------|---------|
| `git push origin main` | `Bash(git push:*)` | Tất cả biến thể git push |
| `npm run build` | `Bash(npm run:*)` | Tất cả npm scripts |
| `ls -la src/` | `Bash(ls:*)` | Tất cả lời gọi ls |
| `rm -rf /tmp/test` | *(bị chặn)* | Không bao giờ ghi nhớ |
| `git push --force` | *(bị chặn)* | Không bao giờ ghi nhớ |
| Tool `Write` | `Write(*)` | Tất cả ghi file |

> **Mẹo:** Xóa `~/.claude/.auto-adapt-mode-initialized` để gieo lại quyền nền tảng. Kiểm tra `~/.claude/auto-adapt-mode.log` để xem quy tắc nào được thêm và quy tắc nào bị chặn.

## Plugin Hooks

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

**Biến môi trường trong Plugin Hooks:**
- `${CLAUDE_PLUGIN_ROOT}` - Đường dẫn đến thư mục plugin
- `${CLAUDE_PLUGIN_DATA}` - Đường dẫn đến thư mục data của plugin

Điều này cho phép plugins bao gồm validation và automation hooks tùy chỉnh.

## MCP Tool Hooks

Các MCP tools theo pattern `mcp__<server>__<tool>`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"systemMessage\": \"Thao tác bộ nhớ đã được ghi log\"}'"
          }
        ]
      }
    ]
  }
}
```

## Cân nhắc bảo mật

### Tuyên bố miễn trách

**DÙNG TRÊN RỦI RO CỦA BẠN**: Hooks thực thi các lệnh shell tùy ý. Bạn hoàn toàn chịu trách nhiệm về:
- Các lệnh bạn cấu hình
- Quyền truy cập/sửa đổi file
- Khả năng mất dữ liệu hoặc hư hại hệ thống
- Kiểm tra hooks trong môi trường an toàn trước khi dùng production

### Lưu ý bảo mật

- **Yêu cầu tin cậy workspace:** Các lệnh hook output `statusLine` và `fileSuggestion` giờ yêu cầu chấp nhận tin cậy workspace trước khi có hiệu lực.
- **HTTP hooks và biến môi trường:** HTTP hooks yêu cầu danh sách `allowedEnvVars` rõ ràng để dùng nội suy biến môi trường trong URLs. Điều này ngăn vô tình rò rỉ biến môi trường nhạy cảm ra endpoint từ xa.
- **Thứ bậc cài đặt quản lý:** Cài đặt `disableAllHooks` giờ tôn trọng thứ bậc cài đặt quản lý, nghĩa là cài đặt cấp tổ chức có thể bắt buộc tắt hooks mà người dùng cá nhân không thể ghi đè.

### Thực hành tốt nhất

| Nên làm | Không nên làm |
|---------|--------------|
| Xác thực và làm sạch tất cả đầu vào | Tin tưởng dữ liệu đầu vào mù quáng |
| Quote biến shell: `"$VAR"` | Dùng không quote: `$VAR` |
| Chặn path traversal (`..`) | Cho phép đường dẫn tùy ý |
| Dùng đường dẫn tuyệt đối với `$CLAUDE_PROJECT_DIR` | Hardcode đường dẫn |
| Bỏ qua file nhạy cảm (`.env`, `.git/`, keys) | Xử lý tất cả file |
| Kiểm tra hooks riêng lẻ trước | Deploy hooks chưa được kiểm tra |
| Dùng `allowedEnvVars` rõ ràng cho HTTP hooks | Expose tất cả biến môi trường cho webhooks |

## Gỡ lỗi

### Bật chế độ Debug

Chạy Claude với cờ debug để xem log hook chi tiết:

```bash
claude --debug
```

### Chế độ Verbose

Dùng `Ctrl+O` trong Claude Code để bật chế độ verbose và xem tiến trình thực thi hook.

### Kiểm tra Hooks độc lập

```bash
# Kiểm tra với đầu vào JSON mẫu
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# Kiểm tra exit code
echo $?
```

## Ví dụ cấu hình đầy đủ

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
            "prompt": "Xác minh tất cả tác vụ đã hoàn thành trước khi dừng.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Chi tiết thực thi Hook

| Khía cạnh | Hành vi |
|-----------|---------|
| **Timeout** | 60 giây mặc định, có thể cấu hình cho mỗi lệnh |
| **Song song hóa** | Tất cả hooks khớp chạy song song |
| **Loại trùng lặp** | Các lệnh hook giống hệt được loại trùng |
| **Môi trường** | Chạy trong thư mục hiện tại với môi trường của Claude Code |

## Xử lý sự cố

### Hook không thực thi
- Kiểm tra cú pháp JSON cấu hình có đúng không
- Kiểm tra pattern matcher có khớp tên tool không
- Đảm bảo script tồn tại và có thể thực thi: `chmod +x script.sh`
- Chạy `claude --debug` để xem log thực thi hook
- Kiểm tra hook đọc JSON từ stdin (không phải đối số lệnh)

### Hook chặn bất ngờ
- Kiểm tra hook với JSON mẫu: `echo '{"tool_name": "Write", ...}' | ./hook.py`
- Kiểm tra exit code: phải là 0 để cho phép, 2 để chặn
- Kiểm tra đầu ra stderr (hiển thị khi exit code 2)

### Lỗi phân tích JSON
- Luôn đọc từ stdin, không phải đối số lệnh
- Dùng phân tích JSON đúng cách (không phải thao tác chuỗi)
- Xử lý các trường thiếu một cách nhẹ nhàng

## Cài đặt

### Bước 1: Tạo thư mục Hooks
```bash
mkdir -p ~/.claude/hooks
```

### Bước 2: Sao chép Hooks ví dụ
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### Bước 3: Cấu hình trong Settings
Chỉnh sửa `~/.claude/settings.json` hoặc `.claude/settings.json` với cấu hình hook hiển thị ở trên.

## Khái niệm liên quan

- **[Checkpoints và Rewind](../08-checkpoints/)** - Lưu và khôi phục trạng thái hội thoại
- **[Slash Commands](../01-slash-commands/)** - Tạo slash commands tùy chỉnh
- **[Skills](../03-skills/)** - Khả năng tự chủ có thể tái sử dụng
- **[Subagents](../04-subagents/)** - Thực thi tác vụ được ủy quyền
- **[Plugins](../07-plugins/)** - Gói mở rộng tích hợp sẵn
- **[Advanced Features](../09-advanced-features/)** - Khám phá các tính năng nâng cao của Claude Code

## Tài nguyên bổ sung

- **[Tài liệu Hooks chính thức](https://code.claude.com/docs/en/hooks)** - Tài liệu tham chiếu hooks đầy đủ
- **[Tài liệu CLI](https://code.claude.com/docs/en/cli-reference)** - Tài liệu giao diện dòng lệnh
- **[Hướng dẫn Memory](../02-memory/)** - Cấu hình ngữ cảnh liên tục
