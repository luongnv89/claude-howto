<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks / Hooks

Hooks là các script tự động thực thi để phản hồi các sự kiện cụ thể trong các phiên Claude Code. Chúng cho phép tự động hóa, xác thực, quản lý quyền, và workflows tùy chỉnh.

## Tổng Quan / Overview

Hooks là các hành động tự động (lệnh shell, HTTP webhooks, prompts LLM, lệnh gọi công cụ MCP, hoặc đánh giá subagent) thực thi tự động khi các sự kiện cụ thể xảy ra trong Claude Code. Chúng nhận đầu vào JSON và giao tiếp kết quả qua exit codes và đầu ra JSON.

**Tính năng chính:**
- Tự động hóa dựa trên sự kiện
- Đầu vào/ra dựa trên JSON
- Hỗ trợ các loại hook `command`, `http`, `mcp_tool`, `prompt`, và `agent`
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
| `type` | Loại hook: `"command"` (bash), `"prompt"` (LLM), `"http"` (webhook), `"mcp_tool"` (gọi công cụ MCP, từ v2.1.118), hoặc `"agent"` (subagent) | `"command"` |
| `command` | Lệnh shell để thực thi | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | Timeout tùy chọn tính bằng giây. Mặc định: 600 cho command/http/mcp_tool, 30 cho prompt, 60 cho agent. Với prompt hook và agent hook, giá trị dưới 1 được tính là 1 giây (v2.1.312+). | `30` |
| `once` | Nếu `true`, hook bị gỡ bỏ sau lần chạy thành công đầu tiên (lần chạy thất bại/bị chặn/hết thời gian vẫn giữ hook). Chỉ dùng trong frontmatter của skill; bị bỏ qua trong settings và frontmatter của agent | `true` |
| `async` | Nếu `true`, chạy nền mà không chặn | `true` |
| `asyncRewake` | Nếu `true`, chạy nền và đánh thức Claude khi mã thoát là 2. Ngầm bật `async`. | `true` |
| `shell` | Chấp nhận `"bash"` hoặc `"powershell"`. Mặc định `"bash"`, hoặc `"powershell"` trên Windows khi chưa cài Git Bash. Mã thoát 2 của hook PowerShell chỉ chặn được từ v2.1.309; hãy nâng cấp trước khi dựa vào một hook PowerShell làm lớp bảo vệ. | `"bash"` |
| `statusMessage` | Thông điệp spinner tùy chỉnh hiển thị khi hook đang chạy | `"Đang định dạng…"` |
| `onFailure` | Điều gì xảy ra với hành động khi một command hook hoặc HTTP hook thất bại (không khởi động được, hết thời gian, thoát với mã không mong đợi): `"continue"` (mặc định) hoặc `"block"` (v2.1.295+) | `"block"` |

> **Lưu ý**: Một số sự kiện hạ thấp timeout mặc định. `UserPromptSubmit` hạ mặc định của `command`, `http` và `mcp_tool` xuống 30 giây, còn `MessageDisplay` hạ xuống 10 giây. Các hook `SessionEnd` dùng chung ngân sách 1,5 giây; nếu cài đặt của bạn khai báo `timeout` dài hơn cho một hook, Claude Code nâng ngân sách đó cho khớp, tối đa 60 giây.

### Các Mẫu Matcher / Matcher Patterns

| Mẫu | Mô Tả | Ví Dụ |
|---------|-------------|---------|
| Chuỗi chính xác | Khớp công cụ cụ thể | `"Write"` |
| Mẫu regex | Khớp nhiều công cụ | `"Edit\|Write"` |
| Phân tách bằng dấu phẩy | Khớp bất kỳ công cụ nào trong danh sách (v2.1.191+) | `"Write,Edit"` |
| Wildcard | Khớp tất cả công cụ | `"*"` hoặc `""` |
| Công cụ MCP | Mẫu server và công cụ | `"mcp__memory__.*"` |

> **Matcher được khớp chính xác (v2.1.195+).** Một định danh có dấu gạch ngang (ví dụ tên công cụ MCP chứa dấu gạch ngang) không còn vô tình khớp chuỗi con với một công cụ khác. Các matcher phân tách bằng dấu phẩy như `"Write,Edit"` kích hoạt với bất kỳ công cụ nào trong danh sách — các bản build trước đó âm thầm không bao giờ kích hoạt chúng.

**Các giá trị matcher của InstructionsLoaded:**

| Giá Trị Matcher | Mô Tả |
|---------------|-------------|
| `session_start` | Instructions được tải khi khởi động phiên |
| `nested_traversal` | Instructions được tải khi duyệt thư mục lồng nhau |
| `path_glob_match` | Instructions được tải qua khớp mẫu glob đường dẫn |

### Thu Hẹp Bằng Điều Kiện `if` (đường dẫn trong tham số công cụ) / Narrowing with `if` conditions (tool-argument paths)

Trường `matcher` chọn hook theo **tên công cụ** (`"Write"`, `"Edit|Write"`, `"*"`). Để lọc hẹp hơn theo **tham số** của công cụ — ví dụ chỉ chạy hook khi một lần sửa chạm vào `src/`, hoặc để chặn việc đọc các file bí mật — hãy thêm điều kiện `if` vào từng hook handler. Điều này khác với matcher theo tên công cụ: `matcher` quyết định *công cụ nào*, còn `if` quyết định *lệnh gọi nào*.

`if` dùng [cú pháp permission rule](https://code.claude.com/docs/en/permissions) (`ToolName(pattern)`), được đánh giá dựa trên tên công cụ **và** tham số của nó cùng lúc. Với `Read`/`Edit`/`Write`, mẫu đường dẫn tuân theo ngữ nghĩa gitignore, với cùng các mốc neo như permission rules: một tên trần như `.env` khớp ở mọi độ sâu, `src/**` là tương đối so với thư mục hiện tại, `/src/**` so với thư mục gốc project, `~/...` so với thư mục home của bạn, và `//...` là đường dẫn tuyệt đối trên hệ thống file.

Trường `if` nằm ở **cấp hook handler** — ngang hàng với `type` và `command`, bên trong mảng `hooks` — chứ không nằm trên `matcher`:

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

Ví dụ các mẫu `if` hợp lệ: `Edit(src/**)` (sửa file trong `src/`), `Read(~/.ssh/**)` (đọc bất kỳ SSH key nào), `Read(.env)` (bất kỳ `.env` nào ở hoặc dưới thư mục hiện tại), `Bash(git push *)` (chỉ các lệnh con `git push`).

> **Cập nhật v2.1.214**: Mẫu `dir/**` một đoạn trong điều kiện `if` của hook (như `Edit(src/**)`) giờ chỉ khớp `<cwd>/dir` — không còn khớp thư mục đó ở mọi độ sâu trong cây. Trước đây `src/**` cũng khớp `foo/src/**`. Dùng `**/dir/**` nếu bạn cần khớp ở mọi độ sâu. **Quan trọng**: việc thu hẹp này chỉ áp dụng cho điều kiện `if:` của hook và tự động phê duyệt theo allow-rule — các permission rule deny/ask vẫn khớp `dir/**` ở mọi độ sâu.

> **Cập nhật v2.1.314**: Các mẫu `if` như `Monitor(tail *)` khớp với các lệnh shell mà công cụ Monitor khởi chạy, giống cách `Bash(tail *)` khớp với lệnh của Bash. Các hook có matcher là `Bash` cũng chạy trên các lệnh shell của Monitor; chúng có thể chặn hoặc hỏi, nhưng không thể phê duyệt hay viết lại các lệnh đó.

## Các Loại Hook / Hook Types

Claude Code hỗ trợ năm loại hook:

### Command Hooks / Hooks Lệnh

Loại hook mặc định. Thực thi một lệnh shell và giao tiếp qua JSON stdin/stdout và exit codes.

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

#### Dạng Exec (`args`) / Exec form (`args`)

> Thêm vào v2.1.139.

Thay vì dạng shell `"command": "..."`, một command hook có thể khởi chạy trực tiếp một binary qua `execve()` với mảng `args`. Không có bước phân tích shell, nên các placeholder đường dẫn không bao giờ cần đặt trong dấu nháy và cấu hình miễn nhiễm với lỗi shell injection.

```json
{
  "type": "command",
  "command": "python3",
  "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/validate.py", "--strict"],
  "timeout": 60
}
```

`command` luôn bắt buộc: khi đặt `args`, `command` là file thực thi cần khởi chạy (được tìm trên `PATH`) và `args` là vector tham số của nó. Bỏ `args` (dạng shell) khi bạn cần pipe, chuyển hướng, nối lệnh bằng `&&`, hoặc các phép mở rộng của shell; dùng `args` khi bạn gọi một binary với các tham số.

### HTTP Hooks / Hooks HTTP

> Thêm vào v2.1.63.

Các endpoints webhook từ xa nhận cùng đầu vào JSON như command hooks. HTTP hooks POST JSON đến URL và nhận phản hồi JSON. HTTP hooks được định tuyến qua sandbox khi sandboxing được bật. Nội suy biến môi trường vào giá trị header yêu cầu danh sách `allowedEnvVars` rõ ràng để bảo mật.

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

**Các thuộc tính chính:**
- `"type": "http"` -- xác định đây là một HTTP hook
- `"url"` -- URL endpoint webhook
- Được định tuyến qua sandbox khi sandbox được bật
- Yêu cầu danh sách `allowedEnvVars` rõ ràng cho bất kỳ nội suy biến môi trường nào trong giá trị `headers`

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

### MCP Tool Hooks / Hooks Công Cụ MCP

> Thêm vào v2.1.118.

Loại `mcp_tool` gọi trực tiếp một công cụ MCP đã được cấu hình; cấu hình tham chiếu đến tên MCP server và tên công cụ thay vì một lệnh shell hay URL. Hữu ích khi logic xác thực hoặc phản hồi đã nằm sẵn trong một MCP server bạn đã cấu hình.

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

**Các thuộc tính chính:**
- `"type": "mcp_tool"` -- xác định đây là một MCP tool hook
- `"server"` -- tên MCP server đã cấu hình
- `"tool"` -- tên công cụ cần gọi trên server đó
- `"input"` -- tham số tùy chọn truyền cho công cụ; giá trị chuỗi hỗ trợ thay thế `${path}` từ đầu vào JSON của hook, ví dụ `"${tool_input.file_path}"`

Tham số của công cụ lấy từ `input` (có thay thế `${path}`), không lấy trực tiếp từ đầu vào của hook. Xem [thiết lập MCP server](../05-mcp/README.md) để cấu hình MCP servers.

### Agent Hooks / Hooks Agent

Hooks xác thực dựa trên subagent mà spawn một agent chuyên dụng để đánh giá điều kiện hoặc thực hiện các kiểm tra phức tạp. Khác với prompt hooks (đánh giá LLM một turn), agent hooks có thể sử dụng các công cụ và thực hiện suy luận đa bước.

> **Lưu ý**: Agent hooks là tính năng thử nghiệm và có thể thay đổi.

> **Lưu ý**: Kể từ v2.1.280, agent hooks không chạy trên `PermissionRequest` — câu trả lời của chúng không bao giờ có thể cho phép hoặc từ chối yêu cầu. Hãy dùng hook command hoặc HTTP trả về đối tượng quyết định ở đó (`ok: false` của prompt hook không có tác dụng trên `PermissionRequest`).

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

Claude Code hỗ trợ **33 sự kiện hook**:

| Sự Kiện | Khi Được Kích Hoạt | Matcher Input | Có Chặn | Sử Dụng Phổ Biến |
|-------|---------------|---------------|-----------|------------|
| **SessionStart** | Phiên bắt đầu/tiếp tục/xóa/dồn | startup/resume/clear/compact/fork | Không | Thiết lập môi trường |
| **Setup** | `--init-only`, hoặc `--init`/`--maintenance` cùng `-p` (chuẩn bị CI/script) | `init`/`maintenance` | Không | Cài đặt công cụ, cài dependencies |
| **InstructionsLoaded** | Sau khi CLAUDE.md hoặc file rules được tải | Lý do tải (`session_start`/`nested_traversal`/`path_glob_match`/`include`/`compact`) | Không | Ghi log kiểm tra/quan sát |
| **UserPromptSubmit** | Người dùng gửi prompt | (none) | Có | Xác thực prompts |
| **UserPromptExpansion** | Slash command do người dùng nhập hoặc MCP prompt được mở rộng thành prompt | Tên lệnh | Có | Biến đổi hoặc kiểm tra prompt đã mở rộng |
| **PreToolUse** | Trước khi thực thi công cụ | Tên công cụ | Có (allow/deny/ask/defer) | Xác thực, sửa đổi đầu vào |
| **PermissionRequest** | Hộp thoại quyền được hiển thị | Tên công cụ | Có | Tự động phê duyệt/từ chối |
| **PermissionDenied** | Auto mode từ chối một lệnh gọi công cụ | Tên công cụ | Không | Logging, phân tích, thực thi chính sách |
| **PostToolUse** | Sau khi công cụ thành công | Tên công cụ | Không | Thêm ngữ cảnh, feedback |
| **PostToolUseFailure** | Thực thi công cụ thất bại | Tên công cụ | Không | Xử lý lỗi, logging |
| **PostToolBatch** | Sau khi một lô lệnh gọi công cụ hoàn tất | (none) | Có | Báo cáo tổng hợp, xác thực theo lô |
| **Notification** | Thông báo được gửi | Loại thông báo | Không | Thông báo tùy chỉnh |
| **MessageDisplay** | Trong khi văn bản phản hồi của assistant được hiển thị | (none) | Không | Biến đổi hoặc ẩn văn bản hiển thị (v2.1.152) |
| **SubagentStart** | Subagent được spawn | Tên loại agent | Không | Thiết lập subagent |
| **SubagentStop** | Subagent hoàn thành | Tên loại agent | Có | Xác thực subagent |
| **Stop** | Claude hoàn thành phản hồi | (none) | Có | Kiểm tra hoàn thành tác vụ |
| **StopFailure** | Lỗi API kết thúc turn | Loại lỗi (`rate_limit`, `overloaded`, `server_error`, …) | Không | Phục hồi lỗi, logging |
| **TeammateIdle** | Đồng nghiệp nhóm agent rảnh | (none) | Có | Phối hợp đồng nghiệp |
| **TaskCompleted** | Nhiệm vụ được đánh dấu hoàn thành | (none) | Có | Hành động sau tác vụ |
| **TaskCreated** | Nhiệm vụ được tạo qua TaskCreate | (none) | Có | Theo dõi nhiệm vụ, logging |
| **ConfigChange** | File config thay đổi | Nguồn config (`user_settings`/`project_settings`/`local_settings`/`policy_settings`/`skills`) | Có (trừ policy) | Phản hồi cập nhật config |
| **CwdChanged** | Thư mục làm việc thay đổi | (none) | Không | Thiết lập cụ thể thư mục |
| **DirectoryAdded** | Thư mục làm việc mới được đăng ký giữa phiên qua `/add-dir` hoặc control request `register_repo_root` của SDK (v2.1.219) | `slash_command`/`register_repo_root` | Không | Thiết lập công cụ cho thư mục vừa thêm |
| **FileChanged** | File được watch thay đổi | Tên file cần watch (ví dụ `.envrc\|.env`) | Không | Giám sát file, rebuild |
| **PreCompact** | Trước khi dồn ngữ cảnh | manual/auto | Có | Hành động pre-dồn |
| **PostCompact** | Sau khi dồn hoàn thành | (none) | Không | Hành động post-dồn |
| **PreModelSwitch** | Trước khi Claude Code áp dụng yêu cầu chuyển đổi model | Tên chuẩn của model sắp chuyển sang (từ `to_model`) | Có | Kiểm soát hoặc từ chối việc đổi model |
| **PostModelSwitch** | Sau khi model của phiên thay đổi, kể cả những thay đổi do chính Claude Code thực hiện (ví dụ khôi phục model khi tiếp tục phiên) | Tên chuẩn của model đã chuyển sang (từ `to_model`) | Không | Ghi log hoặc phản hồi thay đổi model |
| **WorktreeCreate** | Worktree đang được tạo | (none) | Có (trả về path) | Khởi tạo worktree |
| **WorktreeRemove** | Worktree đang được xóa | (none) | Có (exit khác 0 làm việc xóa thất bại) | Dọn dẹp worktree |
| **Elicitation** | MCP server yêu cầu đầu vào người dùng | Tên MCP server | Có | Xác thực đầu vào |
| **ElicitationResult** | Người dùng phản hồi elicitation | Tên MCP server | Có | Xử lý phản hồi |
| **SessionEnd** | Phiên kết thúc | Lý do kết thúc (`clear`/`resume`/`logout`/`prompt_input_exit`/`other`) | Không | Dọn dẹp, logging cuối |

`PreModelSwitch` và `PostModelSwitch` yêu cầu v2.1.251 trở lên. Cả hai nhận `from_model` và `to_model`; matcher được đánh giá dựa trên tên chuẩn suy ra từ `to_model` (ví dụ `claude-opus-5`, `.*opus.*`). Timeout mặc định cho `command`, `http` và `mcp_tool` của chúng được hạ xuống 30 giây.

> **`TaskCreated` và `TaskCompleted` cần bật todo tools (v2.1.233).** Hai
> sự kiện này phát ra từ các todo/task-tracking tools (`TaskCreate`/`Get`/`Update`/`List`,
> `TodoWrite`), vốn **chỉ khả dụng mặc định trên các model Claude 3.x, Opus 4 đến
> 4.7, Sonnet 4 đến 4.6 và Haiku 4.5**. Trên các model khác, hook vẫn là cấu hình
> hợp lệ nhưng đơn giản là không bao giờ chạy — không có output và cũng không có lỗi. Đặt
> `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` để khôi phục các tools, và do đó cả các sự kiện này.

> **Thời lượng PostToolUse (v2.1.119):** Đầu vào của hook `PostToolUse` và `PostToolUseFailure` giờ có thêm `duration_ms` — xem phần [PostToolUse](#posttooluse) để biết chi tiết.

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

**Các matcher phổ biến:** `Agent`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**Điều khiển đầu ra:**
- `permissionDecision`: `"allow"`, `"deny"`, `"ask"`, hoặc `"defer"`
  - `"allow"` bỏ qua prompt quyền (trừ các công cụ yêu cầu tương tác người dùng, và các công cụ connector mà tổ chức của bạn đặt thành `ask`)
  - `"deny"` ngăn lệnh gọi công cụ
  - `"ask"` nhắc người dùng xác nhận; prompt nêu tên plugin hoặc skill mà hook đến từ đó (v2.1.301). Ở auto mode, lệnh gọi sẽ đi tới prompt thay vì classifier, ngoại trừ việc classifier vẫn có thể từ chối các lệnh gọi bị chính các bước kiểm tra của Claude Code gắn cờ (đường dẫn được bảo vệ, lần thử lại không sandbox), và các lệnh gọi `SubagentHandback` chạy mà không có prompt — hãy trả về `"deny"` để chặn một lệnh như vậy
  - `"defer"` kết thúc turn để công cụ có thể được tiếp tục sau, và chỉ hoạt động ở chế độ không tương tác với `-p` (phiên tương tác ghi một cảnh báo vào log và bỏ qua nó); kết quả mang `stop_reason: "tool_deferred"`. `permissionDecisionReason`, `updatedInput` và `additionalContext` đều bị bỏ qua với giá trị này
  - Các quy tắc deny và ask vẫn được đánh giá bất kể hook trả về gì. Khi nhiều hook `PreToolUse` bất đồng, thứ tự ưu tiên là `deny` > `defer` > `ask` > `allow`
- `permissionDecisionReason`: Giải thích cho quyết định. Hiển thị cho người dùng (không phải Claude) với `"ask"`; hiển thị cho Claude với `"deny"`; với `"allow"` và `"defer"`, chỉ được ghi vào debug log
- `updatedInput`: Đầu vào công cụ thay thế (thay toàn bộ đối tượng đầu vào). Từ v2.1.300, nó được xác thực như đầu vào của chính Claude — các khóa không xác định bị loại bỏ, và đầu vào bị công cụ từ chối sẽ khiến lệnh gọi bị từ chối. Khi nhiều hook `PreToolUse` cùng trả về `updatedInput` cho cùng một lệnh gọi, Claude Code không gộp các bản viết lại và cũng không đảm bảo công cụ sẽ chạy với bản nào, vì vậy chỉ nên để một hook viết lại đầu vào của một công cụ nhất định.

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

**Các trường đầu vào bổ sung (v2.1.119):**

| Trường | Kiểu | Mô Tả |
|-------|------|-------------|
| `duration_ms` | number | Thời gian thực thi công cụ tính bằng mili giây. Không tính thời gian chờ ở prompt quyền và thời gian chạy hook PreToolUse. Có trên cả hook `PostToolUse` và `PostToolUseFailure`. |

#### Chặn Có Thể Phục Hồi (`continueOnBlock`, v2.1.139) / Recoverable blocks (`continueOnBlock`, v2.1.139)

Một command hook trả về `"decision": "block"` trên `PostToolUse` sẽ thêm `reason` bên cạnh kết quả công cụ; Claude vẫn thấy đầu ra gốc. `continueOnBlock` là một trường của **prompt** hook (command hook và agent hook không có): theo mặc định, một prompt hook trả về `ok: false` trên `PostToolUse` sẽ kết thúc turn và hiển thị lý do dưới dạng một dòng cảnh báo. Đặt `"continueOnBlock": true` trên prompt hook để thay vào đó gửi lý do lại cho Claude và tiếp tục turn, để model có thể đọc feedback rồi thử lại hoặc điều chỉnh.

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

Dùng cách này khi `reason` của hook là điều Claude có thể hành động theo (ví dụ "file này chỉ đọc; hãy ghi vào chỗ khác"); bỏ nó đi khi một lần chặn phải dừng hẳn turn.

### UserPromptSubmit

Chạy khi người dùng gửi prompt, trước khi Claude xử lý nó. Từ v2.1.299, hook chạy trước khi một skill hoặc lệnh tùy chỉnh được mở rộng, nên chặn prompt cũng sẽ dừng các dòng shell `!` của lệnh đó; `UserPromptExpansion` kích hoạt sau nó.

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

> **Giới hạn an toàn cho số lần chặn liên tiếp (v2.1.143)**: Nếu một hook `Stop` trả về `"decision": "block"` (hoặc đặt `continue: false`) **8 lần liên tiếp** trong cùng một turn, Claude Code sẽ ghi đè lần chặn tiếp theo và kết thúc turn. Ghi đè ngưỡng này bằng biến môi trường `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=<integer>` (đặt `0` để tắt hẳn giới hạn). Điều này ngăn một hook Stop bị lỗi lặp turn mãi mãi.

**Trường trả về (v2.1.163):** Một hook `Stop` hoặc `SubagentStop` có thể trả về `hookSpecificOutput.additionalContext` để gửi feedback cho Claude và **tiếp tục turn mà không hiển thị nhãn lỗi**. Trước đây, việc tác động lên model từ một hook Stop khá vụng về; giờ hook có thể chèn ngữ cảnh một cách gọn gàng, tránh hành vi nhãn lỗi của các cách gửi feedback cũ (như `"decision": "block"`).

```json
{
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "additionalContext": "Reminder: run the test suite before declaring done."
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

**Matchers:** `startup`, `resume`, `clear`, `compact`, `fork`

> **Cập nhật v2.1.214**: Một phiên được fork giờ báo cáo nguồn là `"fork"` — trước đây nó báo cáo `"resume"`.

**Tính năng đặc biệt:** Sử dụng `CLAUDE_ENV_FILE` để persist các biến môi trường (cũng có sẵn trong các hooks `CwdChanged` và `FileChanged`):

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

**Đầu ra theo phạm vi phiên (v2.1.152):** Một hook `SessionStart` có thể trả về JSON để quét lại skills và đặt tiêu đề phiên:

```json
{
  "reloadSkills": true,
  "hookSpecificOutput": {
    "sessionTitle": "Payments migration"
  }
}
```

`reloadSkills: true` ở cấp cao nhất kích hoạt việc quét lại skill ngay trong phiên đó (cùng hành động với lệnh `/reload-skills`), giúp các skill mà hook vừa cài đặt có thể dùng được ngay. `hookSpecificOutput.sessionTitle` đặt tiêu đề hiển thị của phiên khi khởi động và khi tiếp tục.

### SessionEnd

Chạy khi phiên kết thúc để thực hiện dọn dẹp hoặc logging cuối cùng. Không thể chặn việc kết thúc phiên.

**Các giá trị trường reason:**
- `clear` - Người dùng xóa phiên
- `resume` - Phiên được chuyển qua `/resume` tương tác
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
- `elicitation_dialog` - MCP server mở một form elicitation
- `elicitation_url_dialog` - MCP server yêu cầu bạn mở một URL trong trình duyệt
- `elicitation_complete` - Elicitation dạng URL báo đã hoàn tất
- `elicitation_response` - Phản hồi elicitation được gửi lại cho server
- `agent_needs_input` - Agent chạy nền cần đầu vào (v2.1.198)
- `agent_completed` - Agent chạy nền đã hoàn thành (v2.1.198)
- `quota_auto_resume_fired` / `quota_auto_resume_stale` / `quota_auto_resume_disabled` - Các kết quả của cơ chế tự động tiếp tục khi chạm giới hạn sử dụng (v2.1.234)
- `plugin_notification` - Một mod phát thông báo bằng `$.ui.notify`; `title` của hook là tên mod trừ khi mod tự đặt tiêu đề

### PreModelSwitch

Chạy **trước khi** Claude Code áp dụng một yêu cầu chuyển đổi model — ví dụ khi bạn chạy `/model`, hoặc khi một component yêu cầu model khác. Yêu cầu v2.1.251 trở lên.

**Matchers:** tên chuẩn của model sắp chuyển sang, suy ra từ `to_model`. Khớp một model chính xác (`claude-opus-5`) hoặc một họ model bằng regex (`.*opus.*`).

**Các trường đầu vào:** ngoài các trường chung, hook nhận `from_model` (model đang dùng trước khi chuyển) và `to_model` (model được yêu cầu).

**Có thể chặn:** có. Exit code `2` chặn việc chuyển đổi và hiển thị stderr như một lỗi, nên phiên giữ nguyên model hiện tại. Dùng điều này để kiểm soát hoặc từ chối việc đổi model — ví dụ để giữ một project nhạy cảm về chi phí tránh xa model đắt nhất.

**Timeout:** sự kiện này hạ timeout mặc định của `command`, `http` và `mcp_tool` xuống 30 giây.

**Cấu Hình:**
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
# gate-model-switch.sh - từ chối chuyển sang Opus trong project này
input=$(cat)
to_model=$(echo "$input" | jq -r '.to_model')

if [[ "$to_model" == *opus* ]]; then
  echo "This project is budgeted for Sonnet; staying on the current model." >&2
  exit 2
fi

exit 0
```

### PostModelSwitch

Chạy **sau khi** model của phiên đã thay đổi. Nó cũng kích hoạt với những thay đổi do chính Claude Code thực hiện — như khôi phục model đã chọn trước đó khi bạn tiếp tục một phiên — chứ không chỉ với các lần chuyển do bạn yêu cầu. Yêu cầu v2.1.251 trở lên.

**Matchers:** giống `PreModelSwitch` — tên chuẩn suy ra từ `to_model`.

**Các trường đầu vào:** `from_model` và `to_model`, cùng với các trường chung.

**Có thể chặn:** không. Việc chuyển đổi đã xảy ra; hook chỉ có thể quan sát và phản hồi.

**Timeout:** sự kiện này hạ timeout mặc định của `command`, `http` và `mcp_tool` xuống 30 giây.

**Cấu Hình:**
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
# log-model-switch.sh - ghi thêm mọi lần đổi model vào một file log phiên
input=$(cat)
from=$(echo "$input" | jq -r '.from_model')
to=$(echo "$input" | jq -r '.to_model')

echo "$(date -Iseconds) $from -> $to" >> ~/.claude/model-switches.log
exit 0
```

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
          once: true  # Chỉ trong frontmatter của skill: gỡ bỏ sau lần chạy thành công đầu tiên
---
```

**Các sự kiện được hỗ trợ:** mọi sự kiện hook. Hooks của subagent chỉ chạy khi subagent đang hoạt động (`Stop` → `SubagentStop`); hooks của skill được đăng ký khi skill được gọi và duy trì đến hết phiên. Từ v2.1.304, các skill của cùng một nguồn (project của bạn, thư mục skill cá nhân của bạn, hoặc một plugin) có thể đăng ký tối đa 1.024 hooks và 16.384 ký tự matcher mỗi phiên; một skill vượt quá giới hạn sẽ không đăng ký hook nào của nó (tìm `registers none of its hooks` trong log của `claude --debug`).

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

**Yêu cầu tin cậy workspace (v2.1.218):** Hooks trong frontmatter của một subagent **project** giờ yêu cầu chấp nhận tin cậy workspace cho thư mục chứa file agent trước khi chúng chạy. Trước v2.1.218, các hooks này có thể chạy từ những thư mục bạn chưa tin cậy. Xem [tài liệu subagents](https://code.claude.com/docs/en/sub-agents#hooks-in-subagent-frontmatter) để biết những phạm vi nào được miễn.

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
  "agent_type": "security-reviewer",
  "worktree": "/path/to/worktree",
  "effort": { "level": "medium" }
}
```

**Các trường phổ biến:**

| Trường | Mô Tả |
|-------|-------------|
| `session_id` | Định danh phiên duy nhất |
| `transcript_path` | Đường dẫn đến file transcript hội thoại |
| `cwd` | Thư mục làm việc hiện tại |
| `prompt_id` | UUID của prompt đang được xử lý; tương ứng với thuộc tính OpenTelemetry `prompt.id` (v2.1.196) |
| `hook_event_name` | Tên của sự kiện kích hoạt hook |
| `agent_id` | Định danh của agent chạy hook này |
| `agent_type` | Tên agent (ví dụ `"Explore"` hoặc `"security-reviewer"`); chỉ có khi phiên dùng `--agent` hoặc hook chạy bên trong subagent |
| `worktree` | Đường dẫn đến git worktree, nếu agent chạy trong một |
| `effort.level` | (v2.1.133+) Thiết lập mức effort khi hook chạy, bao gồm mức của skill, của subagent, hoặc của `ultrathink`: `low`, `medium`, `high`, `xhigh`, hoặc `max`. Một mức bạn vừa thay đổi có thể hiện ở đây trước khi nó bắt đầu có hiệu lực |

### Exit Codes

| Exit Code | Ý Nghĩa | Hành Vi |
|-----------|---------|----------|
| **0** | Thành công | Tiếp tục, phân tích cú pháp JSON stdout |
| **2** | Lỗi chặn | Chặn thao tác, stderr được hiển thị như lỗi |
| **Khác** | Lỗi không chặn | Tiếp tục; thông báo `<hook name> hook error` trong transcript hiển thị dòng đầu tiên của stderr |

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

> **Phạm vi (v2.1.121+):** `hookSpecificOutput.updatedToolOutput` giờ được áp dụng cho **mọi** công cụ, không chỉ công cụ MCP. Một hook `PostToolUse` trên `Bash`, `Edit`, `Read`, v.v. có thể viết lại đầu ra của công cụ trước khi Claude nhìn thấy — hữu ích để che giấu secrets, chuẩn hóa diffs, hoặc lọc đầu ra lệnh nhiều nhiễu. Giá trị phải khớp với cấu trúc đầu ra của công cụ — `Bash` trả về một đối tượng có `stdout`, `stderr`, `interrupted`, và `isImage`; với công cụ tích hợp sẵn, giá trị không khớp sẽ bị bỏ qua và đầu ra gốc được dùng. Ví dụ (loại bỏ mã màu ANSI khỏi đầu ra `Bash`):
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

> **`retry` (PermissionDenied)**: Dùng JSON `hookSpecificOutput.retry: true` để báo cho model biết nó có thể thử lại lệnh gọi công cụ đã bị từ chối.

> **Dạng quyết định `PreToolUse` đã lỗi thời**: Với `PreToolUse`, các trường `decision` và `reason` ở cấp cao nhất đã **lỗi thời** — hãy dùng `hookSpecificOutput.permissionDecision` (`allow` / `deny` / `ask` / `defer`) và `permissionDecisionReason` thay thế. Thứ tự ưu tiên giữa các quyết định là `deny` > `defer` > `ask` > `allow`. Cũng lưu ý rằng `suppressOutput` được chấp nhận nhưng **không có tác dụng**.

> **Giới hạn đầu ra**: các chuỗi `additionalContext`, `systemMessage` và `initialUserMessage` của một hook, cùng stdout thuần của nó, mỗi thứ bị giới hạn ở 10.000 ký tự. Đầu ra dài hơn được lưu vào một file trong thư mục phiên và được thay bằng đường dẫn của file cùng bản xem trước 2.000 ký tự đầu tiên; Claude không được yêu cầu đọc file đó. Từ v2.1.314, điều này cũng áp dụng cho các hook `PreCompact`, vốn có đầu ra rất lớn có thể khiến việc compaction thất bại hoặc lặp lại.

#### `terminalSequence` (v2.1.141)

Hooks có thể phát các chuỗi escape OSC (operating system command) thô bằng cách đặt `terminalSequence` trong đầu ra JSON. Host ghi chuỗi này ra terminal điều khiển của nó khi hook trả về — hữu ích cho thông báo desktop, cập nhật tiêu đề cửa sổ, và tiếng chuông terminal mà không cần TTY riêng.

| Trường | Kiểu | Mô Tả |
|-------|------|-------------|
| `terminalSequence` | string | Chuỗi escape thô (thường là OSC 9 / OSC 0 / OSC 777). Được ghi nguyên văn ra terminal của host. |

Ví dụ — phát một thông báo desktop OSC 9 khi một tác vụ dài hoàn thành. Viết ESC và BEL dưới dạng escape JSON (`\u001b`, `\u0007`) hoặc tạo giá trị bằng `printf` và `jq`; byte điều khiển thô bên trong chuỗi JSON sẽ gây lỗi phân tích cú pháp:

```json
{
  "terminalSequence": "\u001b]9;Task complete\u0007"
}
```

Cấu hình nó trên một hook `Stop` để thông báo được phát khi Claude kết thúc một turn. Việc hỗ trợ chuỗi escape phụ thuộc vào terminal; iTerm2, Windows Terminal, và WezTerm hỗ trợ OSC 9, còn Kitty dùng OSC 99.

## Các Biến Môi Trường / Environment Variables

| Biến | Khả Dụng | Mô Tả |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | Tất cả hooks | Đường dẫn tuyệt đối đến thư mục gốc project |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | Đường dẫn file để persist env vars |
| `CLAUDE_CODE_REMOTE` | Tất cả hooks | `"true"` nếu chạy trong môi trường từ xa |
| `${CLAUDE_PLUGIN_ROOT}` | Hooks plugin | Đường dẫn đến thư mục plugin |
| `${CLAUDE_PLUGIN_DATA}` | Hooks plugin | Đường dẫn đến thư mục dữ liệu plugin |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | Hooks SessionEnd | Timeout có thể cấu hình tính bằng mili giây cho hooks SessionEnd (ghi đè mặc định) |
| `CLAUDE_CODE_SESSION_ID` | Tiến trình con của công cụ Bash (v2.1.132+) | UUID của phiên; khớp với trường `session_id` trong đầu vào JSON của hook. Dùng để liên kết log bash với telemetry của hook. |
| `CLAUDE_EFFORT` | Tiến trình con của công cụ Bash và lệnh của hook (v2.1.133+) | Thiết lập mức effort khi tiến trình con khởi động (`low`/`medium`/`high`/`xhigh`/`max`); khớp với `effort.level` trong đầu vào JSON của hook. |
| `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` | Toàn tiến trình (v2.1.143+) | Số lần chặn liên tiếp tối đa của hook Stop trước khi Claude Code ghi đè lần chặn tiếp theo và kết thúc turn (mặc định `8`). Đặt `0` để tắt giới hạn. |

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
  "ok": false,
  "reason": "Tests were not run after the last edit"
}
```

`ok: true` cho phép hành động; `reason` là bắt buộc khi `ok` là `false`.

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
            sys.exit(2)  # Exit 2 = lỗi chặn

    sys.exit(0)

if __name__ == "__main__":
    main()
```

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
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\""
          }
        ]
      }
    ]
  }
}
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

### Ví Dụ 6: Theo Dõi Mức Dùng Ngữ Cảnh (Cặp Hook) / Example 6: Context Usage Tracker (Hook Pairs)

Theo dõi lượng token tiêu thụ cho mỗi request bằng cách dùng kết hợp hook `UserPromptSubmit` (trước tin nhắn) và `Stop` (sau phản hồi).

**File:** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
Context Usage Tracker - Theo dõi lượng token tiêu thụ cho mỗi request.

Dùng UserPromptSubmit làm hook "trước tin nhắn" và Stop làm hook "sau phản hồi"
để tính phần chênh lệch token sử dụng của mỗi request.

Các phương pháp đếm token:
1. Ước lượng theo ký tự (mặc định): ~4 ký tự mỗi token, không cần dependencies
2. tiktoken (tùy chọn): Chính xác hơn (~90-95%), yêu cầu: pip install tiktoken
"""
import json
import os
import sys
import tempfile

# Cấu hình
CONTEXT_LIMIT = 1000000  # 1M trên Opus/Sonnet/Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Sonnet 4.6; 200000 trên Haiku 4.5 (điều chỉnh theo model của bạn)
USE_TIKTOKEN = False    # Đặt True nếu đã cài tiktoken để chính xác hơn


def get_state_file(session_id: str) -> str:
    """Lấy đường dẫn file tạm để lưu số token trước tin nhắn, tách riêng theo phiên."""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    Đếm số token trong văn bản.

    Dùng tiktoken với encoding p50k_base nếu có (~90-95% chính xác),
    nếu không thì quay về ước lượng theo ký tự (~80-90% chính xác).
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # Quay về ước lượng

    # Ước lượng theo ký tự: ~4 ký tự mỗi token với tiếng Anh
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """Đọc và nối toàn bộ nội dung từ file transcript."""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # Trích xuất nội dung văn bản từ các định dạng tin nhắn khác nhau
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

    # Lưu vào file tạm để so sánh sau
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """Hook sau phản hồi: Tính và báo cáo phần chênh lệch token."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # Tải số token trước tin nhắn
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # Tính phần chênh lệch
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # Báo cáo mức sử dụng
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

**Cấu Hình:**
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
1. `UserPromptSubmit` kích hoạt trước khi prompt của bạn được xử lý - lưu số token hiện tại
2. `Stop` kích hoạt sau khi Claude phản hồi - tính phần chênh lệch và báo cáo mức sử dụng
3. Mỗi phiên được tách riêng qua `session_id` trong tên file tạm

**Các Phương Pháp Đếm Token:**

| Phương Pháp | Độ Chính Xác | Dependencies | Tốc Độ |
|--------|----------|--------------|-------|
| Ước lượng theo ký tự | ~80-90% | Không có | <1ms |
| tiktoken (p50k_base) | ~90-95% | `pip install tiktoken` | <10ms |

> **Lưu ý:** Anthropic chưa phát hành tokenizer offline chính thức. Cả hai phương pháp đều là ước lượng. Transcript bao gồm prompt của người dùng, phản hồi của Claude, và đầu ra công cụ; từ v2.1.300 nó cũng ghi lại system prompt, công cụ, và tham số của mỗi API request.

### Ví Dụ 7: Khởi Tạo Quyền Auto-Mode (Script Thiết Lập Một Lần) / Example 7: Seed Auto-Mode Permissions (One-Time Setup Script)

Một script thiết lập chạy một lần, nạp vào `~/.claude/settings.json` các permission rule an toàn tương đương với baseline auto-mode của Claude Code — 37 rule theo mặc định, tối đa 63 khi bật mọi cờ danh mục — mà không cần hook nào, và không ghi nhớ các lựa chọn về sau. Chạy một lần; có thể chạy lại an toàn (bỏ qua các rule đã có).

**File:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Xem trước những gì sẽ được thêm
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Áp dụng
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**Những gì được thêm:**

| Danh Mục | Ví Dụ |
|----------|---------|
| Công cụ tích hợp sẵn | `Read(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)` |
| Sửa file tùy chọn (--include-edits) | `Edit(*)` |
| Git đọc | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)` |
| Git ghi (local) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Trình quản lý package | `Bash(npm ci:*)`, `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(pip3 install:*)` |
| Build & test | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Shell thông dụng | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

**Những gì được cố ý loại trừ** (script này không bao giờ thêm):
- `rm -rf`, `sudo`, force push, `git reset --hard`
- `DROP TABLE`, `kubectl delete`, `terraform destroy`
- `npm publish`, `curl | bash`, deploy lên production

### Ví Dụ 8: Ghi Log Tiến Độ Học (SessionEnd) / Example 8: Learning Progress Logger (SessionEnd)

Ghi lại những module bạn đã học vào cuối mỗi phiên Claude Code. Tiến độ được lưu
trong `~/.claude-howto-progress.json` — nằm ngoài repo, nên vẫn còn sau `git pull` mà không
bị ghi đè.

**Tại sao dùng `SessionEnd` mà không phải `Stop`?**
`Stop` kích hoạt sau *mỗi* phản hồi của Claude. `SessionEnd` kích hoạt một lần khi phiên
kết thúc — đúng thứ bạn cần cho một mục nhật ký cuối phiên.

**Tại sao không có prompt tương tác?**
Hooks chạy mà không có terminal điều khiển, nên `/dev/tty` không khả dụng và hook không thể
hỏi bạn. Hãy truyền các module (và ghi chú tùy chọn) dưới dạng biến môi trường khi bạn
khởi chạy Claude Code, ví dụ `CLAUDE_HOWTO_MODULES=06,07 claude`.

**File:** `06-hooks/session-end.sh`

```bash
#!/usr/bin/env bash
# Hook SessionEnd: ghi nhận các module đã học, rồi thêm một bản ghi phiên
# vào ~/.claude-howto-progress.json để theo dõi tiến độ học lâu dài.

PROGRESS_FILE="$HOME/.claude-howto-progress.json"

# Bảo vệ: chỉ chạy bên trong repo này
if [[ "$CLAUDE_PROJECT_DIR" != *"claude-howto"* ]] && [[ "$PWD" != *"claude-howto"* ]]; then
  exit 0
fi

if [ ! -f "$PROGRESS_FILE" ]; then
  echo '{"sessions":[]}' > "$PROGRESS_FILE"
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H:%M")

# Các module đã học, ví dụ khởi chạy với: CLAUDE_HOWTO_MODULES=06,07 claude
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

# Ghi chú tùy chọn, ví dụ CLAUDE_HOWTO_NOTES="tried the pre-commit example"
NOTES="${CLAUDE_HOWTO_NOTES:-}"

# Truyền NOTES như một tham số riêng để Python xử lý việc escape JSON —
# tránh JSON bị hỏng khi ghi chú chứa dấu nháy hoặc dấu gạch chéo ngược.
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

**Cài đặt** — sao chép script vào thư mục hook của project để đường dẫn trong `settings.json` trỏ đúng:

```bash
mkdir -p .claude/hooks
cp 06-hooks/session-end.sh .claude/hooks/
chmod +x .claude/hooks/session-end.sh
```

**Cấu Hình** (trong `.claude/settings.json`):

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

Các hook SessionEnd có ngân sách mặc định 1,5 giây. Đặt `"timeout"` riêng cho hook (tính bằng giây) sẽ nâng ngân sách cho khớp, tối đa 60 giây; một hook không có `timeout` riêng sẽ bị hủy sau 1,5 giây.

**Đầu ra — `~/.claude-howto-progress.json`:**

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

**Các pattern chính được minh họa:**

| Pattern | Tại sao quan trọng |
|---------|----------------|
| Sự kiện `SessionEnd` | Kích hoạt một lần khi thoát — không phải sau mỗi phản hồi như `Stop` |
| `INPUT="${CLAUDE_HOWTO_MODULES:-}"` | Hooks không có terminal (`/dev/tty` không khả dụng), nên đầu vào lấy từ biến môi trường |
| `"timeout": 10` | Các hook SessionEnd bị hủy sau 1,5 giây trừ khi tự đặt `timeout` riêng |
| `$CLAUDE_PROJECT_DIR` | Đường dẫn khả chuyển — đừng bao giờ hardcode `/Users/yourname/...` |
| Mệnh đề bảo vệ ở đầu | Ngăn hook chạy trong các project không liên quan nếu được cài toàn cục |
| Lưu ngoài repo | Đường dẫn `~/` vẫn còn sau `git pull` mà không ghi đè dữ liệu của bạn |

**Công cụ đi kèm: trình theo dõi tiến độ trực quan**

Để có giao diện checkbox đầy đủ bao quát cả 10 module, hãy mở trình theo dõi đi kèm trong trình duyệt:

```bash
open local-progress/index.html
```

Tiến độ được lưu trong `localStorage` của trình duyệt (không bao giờ ghi ra đĩa bên trong repo).
Dùng nút **Export** để lưu một bản chụp dưới dạng JSON, và **Import** để khôi phục.

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
            "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/validate.sh"
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
- **Kích thước terminal cho status-line (v2.1.153):** Các script lệnh status-line giờ nhận biến môi trường `COLUMNS` và `LINES`, để script có thể điều chỉnh đầu ra theo chiều rộng/chiều cao terminal (ví dụ `[ "$COLUMNS" -lt 80 ] && short_output`).
- **HTTP hooks và biến môi trường:** HTTP hooks yêu cầu danh sách `allowedEnvVars` rõ ràng để sử dụng nội suy biến môi trường trong giá trị header. Điều này ngăn chặn lộ vô ý các biến môi trường nhạy cảm đến các endpoints từ xa.
- **Phân cấp settings được quản lý:** Cài đặt `disableAllHooks` bây giờ tôn trọng phân cấp settings được quản lý, nghĩa là settings cấp tổ chức có thể thực thi vô hiệu hóa hook mà người dùng cá nhân không thể ghi đè.
- **Tự động phê duyệt PowerShell (v2.1.119):** Các lệnh của công cụ PowerShell có thể được tự động phê duyệt trong permission mode, giống như Bash. Điều này mang lại sự tương đương cho người dùng Windows chạy Claude Code với các công cụ shell dựa trên PowerShell.
- **Đóng lỗ hổng tự động phê duyệt env-var trần trong Bash (v2.1.145):** Trước v2.1.145, một lệnh Bash dạng `FOO=bar somecommand` (một phép gán biến trần đi kèm một lệnh không nằm trong allowlist) có thể được tự động phê duyệt khi chỉ riêng `FOO=bar` nằm trong allowlist. v2.1.145 đã đóng lỗ hổng này — các lệnh như vậy giờ sẽ hiện prompt quyền. Các script dựa vào việc cho phép ngầm định này sẽ bắt đầu hiện prompt; hãy cho phép lại chúng một cách rõ ràng qua một permission rule `Bash(...)` bao quát toàn bộ lệnh, không chỉ phép gán biến.

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

## Ví Dụ Cấu Hình Hoàn Chỉnh / Complete Configuration Example

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

## Chi Tiết Thực Thi Hook / Hook Execution Details

| Khía Cạnh | Hành Vi |
|--------|----------|
| **Timeout** | Mặc định 600 giây cho command/http/mcp_tool (30 cho prompt, 60 cho agent); có thể cấu hình cho từng hook |
| **Song song hóa** | Tất cả hooks khớp đều chạy song song; từ v2.1.312, tối đa 24 prompt hook hoặc agent hook chạy cùng lúc trên mỗi phiên (tính cả subagent), cộng thêm tối đa 12 hook đã chờ lâu hơn timeout của sự kiện của chúng, và số còn lại chờ đến lượt (v2.1.302–v2.1.311: tối đa 12 hook của cùng một sự kiện). |
| **Khử trùng lặp** | Các lệnh hook giống hệt nhau được khử trùng lặp |
| **Môi trường** | Chạy trong thư mục hiện tại với môi trường của Claude Code |

## Xử Lý Sự Cố / Troubleshooting

### Hook Không Thực Thi / Hook Not Executing
- Kiểm tra cú pháp cấu hình JSON có đúng không
- Kiểm tra mẫu matcher có khớp với tên công cụ không
- Đảm bảo script tồn tại và có quyền thực thi: `chmod +x script.sh`
- Chạy `claude --debug` để xem log thực thi hook
- Kiểm tra hook đọc JSON từ stdin (không phải từ tham số lệnh)

### Hook Chặn Ngoài Ý Muốn / Hook Blocks Unexpectedly
- Test hook với JSON mẫu: `echo '{"tool_name": "Write", ...}' | ./hook.py`
- Kiểm tra exit code: phải là 0 để cho phép, 2 để chặn
- Kiểm tra đầu ra stderr (được hiển thị khi exit code là 2)

### Lỗi Phân Tích JSON / JSON Parsing Errors
- Luôn đọc từ stdin, không phải từ tham số lệnh
- Dùng cách phân tích JSON đúng chuẩn (không thao tác chuỗi)
- Xử lý các trường bị thiếu một cách an toàn

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

---

**Cập Nhật Lần Cuối**: Ngày 1 tháng 11 năm 2026
**Phiên Bản Claude Code**: 2.1.316
**Nguồn**:
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
**Các Mô Hình Tương Thích**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
