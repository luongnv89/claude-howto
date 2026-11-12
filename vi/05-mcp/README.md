<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

Thư mục này chứa tài liệu toàn diện và ví dụ cho cấu hình và sử dụng MCP server với Claude Code.

## Tổng Quan

MCP (Model Context Protocol) là một cách chuẩn hóa để Claude truy cập các công cụ bên ngoài, API và nguồn dữ liệu thời gian thực. Khác với bộ nhớ (Memory), MCP cung cấp truy cập trực tiếp đến dữ liệu đang thay đổi.

Đặc điểm chính:
- Truy cập thời gian thực đến các dịch vụ bên ngoài
- Đồng bộ hóa dữ liệu trực tiếp
- Kiến trúc có thể mở rộng
- Xác thực bảo mật
- Tương tác dựa trên công cụ

## Kiến Trúc MCP

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
```

## Hệ Sinh Thái MCP

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#f3e5f5,stroke:#333,color:#333
    style G fill:#e8f5e9,stroke:#333,color:#333
    style H fill:#e8f5e9,stroke:#333,color:#333
    style I fill:#e8f5e9,stroke:#333,color:#333
    style J fill:#e8f5e9,stroke:#333,color:#333
    style K fill:#e8f5e9,stroke:#333,color:#333
```

## Phương Thức Cài Đặt MCP

Claude Code hỗ trợ nhiều giao thức vận chuyển cho kết nối MCP server:

### Giao Thức HTTP (Khuyến Nghị)

```bash
# Kết nối HTTP cơ bản
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP với header xác thực
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Giao Thức Stdio (Cục Bộ)

Đối với MCP server chạy cục bộ:

```bash
# Server Node.js cục bộ
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# Với biến môi trường
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

#### `CLAUDE_PROJECT_DIR` cho stdio server (v2.1.139+)

Mọi MCP stdio server đều được khởi chạy với `CLAUDE_PROJECT_DIR=<đường dẫn tuyệt đối đến thư mục gốc repo>` đã được đặt sẵn trong môi trường của nó — cùng quy ước dùng cho hook. File `.mcp.json` của plugin và project có thể tham chiếu `${CLAUDE_PROJECT_DIR}` trong các giá trị `command`, `args` và `env`, và việc thay thế diễn ra trước `execve()`:

```json
{
  "mcpServers": {
    "repo-tools": {
      "type": "stdio",
      "command": "node",
      "args": ["${CLAUDE_PROJECT_DIR:-.}/.claude/mcp/repo-tools.js"],
      "env": {
        "REPO_ROOT": "${CLAUDE_PROJECT_DIR:-.}"
      }
    }
  }
}
```

> **Lưu ý**: Trong cấu hình project, local và user, hãy viết `${CLAUDE_PROJECT_DIR:-.}` kèm giá trị mặc định: biến này được đặt trong môi trường của server, không phải trong môi trường của chính Claude Code. Chỉ cấu hình MCP của plugin mới thay thế trực tiếp `${CLAUDE_PROJECT_DIR}`.

Dùng cách này khi stdio server của bạn cần đọc file tương đối với thư mục gốc project, bất kể Claude Code được khởi chạy từ đâu.

Các stdio MCP server cũng nhận `CLAUDE_CODE_SESSION_ID` (khớp với giá trị truyền cho hook và Bash), kể cả khi phiên được tiếp tục bằng `--resume` (v2.1.163+).

### Giao Thức SSE (Đã Lỗi Thời)

Giao thức Server-Sent Events đã lỗi thời và được thay bằng `http`, nhưng vẫn được hỗ trợ:

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### Giao Thức WebSocket (`ws`)

Máy chủ WebSocket giữ một kết nối hai chiều liên tục, phù hợp với các máy chủ MCP từ xa cần đẩy sự kiện tới Claude mà không cần được hỏi. Hãy dùng HTTP thay thế nếu máy chủ của bạn chỉ phản hồi các yêu cầu, vì HTTP hỗ trợ OAuth và cờ `claude mcp add --transport`, còn WebSocket thì không hỗ trợ cả hai.

Vì `--transport` không chấp nhận `ws`, hãy cấu hình trong `.mcp.json` hoặc qua `claude mcp add-json`:

```json
{
  "type": "ws",
  "url": "wss://mcp.example.com/socket",
  "headers": {
    "Authorization": "Bearer YOUR_TOKEN"
  }
}
```

Mục `type: "ws"` chấp nhận cùng các trường `url`, `headers`, `headersHelper`, `timeout` và `alwaysLoad` như `http`. Xác thực **chỉ qua header** — không có luồng OAuth cho máy chủ WebSocket.

> **Lưu ý**: Từ v2.1.285, `claude mcp list` liệt kê các máy chủ WebSocket (`ws`) cùng URL và trạng thái sức khỏe của chúng (các phiên bản trước bỏ sót chúng). Bạn cũng có thể kiểm tra chúng bằng `claude mcp get <name>` hoặc bảng `/mcp`.

Giống HTTP và SSE, kết nối WebSocket dùng cửa sổ nhàn rỗi 5 phút; stdio và WebSocket không có bộ đếm thời gian cho từng yêu cầu. Một mục `url` không có `type` sẽ báo lỗi và liệt kê `"http"`, `"sse"`, `"ws"` là các giá trị hợp lệ.

### Thư Mục Làm Việc Của Phiên (roots/list)

MCP server có thể khám phá các thư mục làm việc của phiên: thư mục khởi chạy cùng mọi mục `--add-dir`/`additionalDirectories` được trả về qua request MCP `roots/list`, và một thông báo `notifications/roots/list_changed` được gửi mỗi khi tập hợp này thay đổi (v2.1.203). Thời gian chờ nhàn rỗi giờ cũng áp dụng cho stdio server (30 phút), với `timeout` theo từng server đóng vai trò mức sàn nhàn rỗi (v2.1.203).

### Lưu Ý Riêng Cho Windows

Trên Windows native (không phải WSL), sử dụng `cmd /c` cho các lệnh npx:

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### Xác Thực OAuth 2.0

Claude Code hỗ trợ OAuth 2.0 cho các MCP server yêu cầu nó. Khi kết nối đến một server có OAuth, Claude Code xử lý toàn bộ quy trình xác thực:

```bash
# Kết nối đến một MCP server có OAuth (flow tương tác)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# Cấu hình trước OAuth credentials cho thiết lập không tương tác
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| Tính Năng | Mô Tả |
|---------|-------------|
| **OAuth tương tác** | Sử dụng `/mcp` để kích hoạt flow OAuth dựa trên trình duyệt |
| **OAuth client cấu hình sẵn** | OAuth client tích hợp sẵn cho các dịch vụ phổ biến như Notion, Stripe, v.v. (v2.1.30+) |
| **Credentials cấu hình trước** | Các cờ `--client-id`, `--client-secret`, `--callback-port` cho thiết lập tự động |
| **Lưu trữ token** | Token được lưu trữ an toàn trong system keychain của bạn |
| **Xác thực step-up** | Hỗ trợ xác thực step-up cho các thao tác đặc quyền |
| **Cache discovery** | Metadata discovery OAuth được cache để kết nối lại nhanh hơn |
| **Ghi đè metadata** | `oauth.authServerMetadataUrl` trong `.mcp.json` để ghi đè discovery metadata OAuth mặc định |

#### Ghi Đè OAuth Metadata Discovery

Nếu MCP server của bạn trả về lỗi trên endpoint metadata OAuth chuẩn (`/.well-known/oauth-authorization-server`) nhưng có một endpoint OIDC hoạt động, bạn có thể bảo Claude Code lấy OAuth metadata từ một URL cụ thể. Đặt `authServerMetadataUrl` trong object `oauth` của cấu hình server:

```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

URL phải sử dụng `https://`. Tùy chọn này yêu cầu Claude Code v2.1.64 hoặc mới hơn.

#### Thông Báo Xác Thực Khi Khởi Động Và Làm Mới Header Động (v2.1.193)

- **Thông báo xác thực khi khởi động (v2.1.193+)**: Khi khởi động, Claude Code hiển thị một thông báo liệt kê các MCP server vẫn cần xác thực, để server cần đăng nhập không bị âm thầm ngừng hoạt động.
- **Tự động làm mới `headersHelper` (v2.1.193+)**: Nếu bạn cung cấp xác thực tùy chỉnh qua `headersHelper`, helper sẽ được gọi lại tự động khi server trả về HTTP 401 hoặc 403. Credentials được làm mới ngay lập tức mà không cần kết nối lại thủ công. Xem [Use dynamic headers for custom authentication](https://code.claude.com/docs/en/mcp).
- **OAuth phía sau proxy xác thực (v2.1.299+)**: truyền header riêng của proxy bằng `--header`, `headers`, hoặc `headersHelper`, không đặt `Authorization` trong các header đó, và đăng nhập bằng `claude mcp login <name>`. Một header `Authorization` đã được cấu hình sẽ được dùng làm credential, không có cơ chế dự phòng sang OAuth.

> **Cảnh báo** (v2.1.238): Một `headersHelper` trong `.mcp.json` của project, và các MCP server inline trong file tác nhân của project hoặc của `--add-dir`, giờ yêu cầu hộp thoại tin cậy (trust dialog) của thư mục đó đã được chấp nhận — kể cả khi chạy `claude -p`. Các helper như vậy cũng chạy **không kế thừa các biến môi trường chứa credentials**; helper ở phạm vi user, managed và claude.ai thì chạy từ thư mục cấu hình Claude. Một cấu hình project từng dựa vào credentials kế thừa hoặc vào việc chạy khi chưa được tin cậy sẽ ngừng hoạt động cho đến khi bạn chấp nhận hộp thoại tin cậy và cung cấp credentials theo cách khác.

### MCP Connector Của Claude.ai

Các MCP server được cấu hình trong tài khoản Claude.ai của bạn tự động có sẵn trong Claude Code. Điều này có nghĩa là bất kỳ kết nối MCP nào bạn thiết lập qua giao diện web Claude.ai đều có thể truy cập mà không cần cấu hình thêm.

MCP connector của Claude.ai cũng có sẵn trong chế độ `--print` (v2.1.83+), cho phép sử dụng không tương tác và theo script.

> **Lưu ý khi khởi động (v2.1.117+):** Kết nối đồng thời là mặc định khi cấu hình cả MCP server cục bộ lẫn của claude.ai (trước đây kết nối tuần tự), giúp giảm độ trễ khởi động khi dùng nhiều server.

Để tắt MCP server của Claude.ai trong Claude Code, đặt biến môi trường `ENABLE_CLAUDEAI_MCP_SERVERS` thành `false`:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **Lưu ý:** Tính năng này chỉ có sẵn cho người dùng đã đăng nhập bằng tài khoản Claude.ai.

## Quy Trình Thiết Lập MCP

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP connected!
```

### Lệnh `/mcp`

Gõ `/mcp` trong phiên để liệt kê các server đã kết nối, kích hoạt flow OAuth và kiểm tra trạng thái kết nối.

- Từ **v2.1.121**, MCP thử lại kết nối ban đầu tối đa 3 lần khi gặp lỗi tạm thời.
- Từ **v2.1.128**, `/mcp` hiển thị **số lượng công cụ** của mỗi server đã kết nối và đánh dấu trực quan các server báo **0 công cụ** để server cấu hình sai dễ nhận ra ngay.

## Tìm Kiếm Công Cụ MCP

Tìm kiếm công cụ được bật theo mặc định: các công cụ MCP được hoãn lại và khám phá khi cần, nên định nghĩa của chúng không lấp đầy ngữ cảnh mô hình. Từ v2.1.304, tính năng này cũng vẫn bật khi đi qua một gateway `ANTHROPIC_BASE_URL` tùy chỉnh, và gateway đó phải chuyển tiếp các trường công cụ `defer_loading` và các khối `tool_reference`; từ v2.1.305, khi gateway từ chối một yêu cầu với mã 400 hoặc 422, Claude Code gửi lại yêu cầu đó mà không dùng tìm kiếm công cụ. Đặt `ENABLE_TOOL_SEARCH=false` để tải mọi công cụ ngay từ đầu và tránh các yêu cầu bị từ chối đó. Trước v2.1.304, tìm kiếm công cụ bị tắt khi đi qua gateway trừ khi `ENABLE_TOOL_SEARCH` là `true`, `auto` hoặc `auto:N`.

| Cài Đặt | Giá Trị | Mô Tả |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | (không đặt — mặc định) | Tất cả công cụ MCP được hoãn lại và tải khi cần |
| `ENABLE_TOOL_SEARCH` | `auto` | Chế độ ngưỡng: công cụ được tải trước cho đến khi định nghĩa của chúng đạt 10% cửa sổ ngữ cảnh, sau đó tất cả được hoãn lại |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | Chế độ ngưỡng với tỷ lệ phần trăm tùy chỉnh (0-100) — ví dụ, `auto:5` cho 5% |
| `ENABLE_TOOL_SEARCH` | `true` | Tất cả công cụ MCP được hoãn lại |
| `ENABLE_TOOL_SEARCH` | `false` | Đã tắt; tất cả mô tả công cụ được gửi đầy đủ |

> **Lưu ý:** Tìm kiếm công cụ yêu cầu một mô hình hỗ trợ các khối `tool_reference`: Claude Opus 4, Claude Sonnet 4, Claude Haiku 4.5, và các mô hình mới hơn (Opus 4.5, Sonnet 4.5, Haiku 4.5 trở lên trên Agent Platform của Google Cloud).

### Bỏ Qua Tìm Kiếm Công Cụ Theo Từng Server (v2.1.121+)

Nếu công cụ của một MCP server cụ thể cần dùng ở mọi lượt, hãy đánh dấu cấu hình
của server đó bằng `"alwaysLoad": true` để bỏ qua việc hoãn qua tìm kiếm công cụ và
giữ các công cụ đó luôn sẵn sàng:

```json
{
  "mcpServers": {
    "always-on-tool": {
      "command": "node",
      "args": ["./tools/always.js"],
      "alwaysLoad": true
    }
  }
}
```

Hãy dùng hạn chế — mỗi công cụ luôn được tải đều tiêu tốn ngữ cảnh mà lẽ ra
tìm kiếm công cụ có thể dùng để đưa ra một công cụ phù hợp hơn.

Để giữ toàn bộ công cụ của một server phía sau tìm kiếm công cụ, đặt
`"alwaysLoad": false` trong mục của server đó (v2.1.287+). Điều này bao gồm cả
các công cụ mà tác giả server đã đánh dấu để tải ngay từ đầu; nếu bạn bỏ qua
`alwaysLoad`, các công cụ được đánh dấu đó sẽ tải ngay từ đầu. Tác giả server đánh
dấu từng công cụ bằng cách đặt `"anthropic/alwaysLoad"` trong object `_meta` của
công cụ đó, và cài đặt `alwaysLoad` cấp server trong cấu hình của bạn có thể ghi đè nó.

Dành cho tác giả server: đánh dấu các công cụ an toàn khi được gọi hai lần bằng annotation `idempotentHint` hoặc `readOnlyHint` trong mục `tools/list` của chúng. Từ v2.1.307, Claude Code chỉ lặp lại một lời gọi đang chờ khi kết nối HTTP hoặc claude.ai connector bị đóng đối với các công cụ đó; các lời gọi khác thất bại với `connection closed before the tool call was answered`.

## Cập Nhật Công Cụ Động

Claude Code hỗ trợ các thông báo `list_changed` của MCP. Khi một MCP server động thêm, xóa hoặc sửa đổi các công cụ có sẵn của nó, Claude Code nhận cập nhật và điều chỉnh danh sách công cụ tự động -- không cần kết nối lại hoặc khởi động lại.

## MCP Apps

MCP Apps là extension MCP chính thức đầu tiên, cho phép các lời gọi công cụ MCP trả về các thành phần UI tương tác được render trực tiếp trong giao diện chat. Thay vì phản hồi văn bản thuần, MCP server có thể cung cấp dashboard phong phú, biểu mẫu, trực quan hóa dữ liệu và workflow nhiều bước -- tất cả hiển thị inline mà không cần rời khỏi cuộc hội thoại.

## MCP Elicitation

Các MCP server có thể yêu cầu đầu vào có cấu trúc từ người dùng qua các hộp thoại tương tác (v2.1.49+). Điều này cho phép một MCP server yêu cầu thêm thông tin giữa chừng workflow -- ví dụ, yêu cầu xác nhận, chọn từ danh sách tùy chọn, hoặc điền vào các trường bắt buộc -- thêm tính tương tác vào các tương tác với MCP server.

Nếu một server xây dựng trên Java MCP SDK 0.17.0 trở về trước từ chối kết nối với lỗi "rejected Claude Code's elicitation capability", hãy nâng cấp nó lên Java MCP SDK 0.17.1+ hoặc thêm `"bareElicitationCapability": true` vào mục cấu hình của nó (stdio, `sse`, `http` và `ws`; v2.1.281+), tùy chọn này giới hạn server ở elicitation dạng form.

## Giới Hạn Mô Tả Và Hướng Dẫn Công Cụ

Claude Code cắt bớt mỗi mô tả công cụ MCP và hướng dẫn của mỗi server để các server dài dòng không làm phình ngữ cảnh. Giới hạn mặc định là **4.096 ký tự** cho hướng dẫn của server và cho mô tả của các công cụ được tải ngay từ đầu (v2.1.296; 2.048 từ v2.1.84 đến trước đó), và **16.384 ký tự** cho các mô tả mà Claude tải qua tìm kiếm công cụ (v2.1.295). Kể từ v2.1.280, `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` ghi đè các giới hạn này: con số bạn đặt thay thế **cả hai** giới hạn (`8192` nâng giới hạn ngắn hơn và hạ giới hạn dài hơn). Kể từ v2.1.299, mô tả và hướng dẫn từ các MCP server first-party của Anthropic tại `api.anthropic.com` đến Claude đầy đủ. Hãy đặt các chi tiết quan trọng ở gần đầu mô tả.

## MCP Prompt Như Lệnh Slash

Các MCP server có thể cung cấp các prompt xuất hiện như lệnh slash trong Claude Code. Prompt được truy cập theo quy ước đặt tên:

```
/mcp__<server>__<prompt>
```

Ví dụ, nếu một server tên là `github` cung cấp một prompt tên là `review`, bạn có thể gọi nó bằng `/mcp__github__review`.

## Khử Trùng Lặp Server

Khi cùng một MCP server được định nghĩa ở nhiều phạm vi (local, project, user), cấu hình local được ưu tiên. Điều này cho phép bạn ghi đè cài đặt MCP cấp project hoặc user bằng tùy biến local mà không gây xung đột.

## Các Bản Sửa Lỗi Vòng Đời Gần Đây (v2.1.136)

Hai lỗi vòng đời MCP tồn tại lâu đã được sửa trong v2.1.136 — đáng để nâng cấp nếu bạn chạy thiết lập nhiều server:

- **MCP server được giữ lại qua `/clear`**: Các server cấu hình qua `.mcp.json`, plugin hoặc claude.ai connector không còn biến mất sau `/clear` trong VS Code, JetBrains hoặc Agent SDK. Các phiên bản trước âm thầm loại bỏ chúng và yêu cầu khởi động lại.
- **Sửa lỗi làm mới đồng thời refresh token OAuth**: Thiết lập OAuth nhiều server không còn mất refresh token khi nhiều server tranh nhau làm mới cùng lúc. Điều này loại bỏ tình trạng "sáng nào cũng phải xác thực lại" từng gặp ở các thiết lập có nhiều MCP server được bảo vệ bằng OAuth.

## Tài Nguyên MCP Qua @ Mention

Bạn có thể tham chiếu tài nguyên MCP trực tiếp trong prompt bằng cú pháp mention `@`:

```
@server-name:protocol://resource/path
```

Ví dụ, để tham chiếu một tài nguyên database cụ thể:

```
@database:postgres://mydb/users
```

Điều này cho phép Claude lấy và đưa nội dung tài nguyên MCP vào inline như một phần ngữ cảnh hội thoại.

## Các Phạm Vi MCP

Cấu hình MCP có thể được lưu trữ ở các phạm vi khác nhau với các mức độ chia sẻ khác nhau:

| Phạm Vi | Cờ | Vị Trí | Mô Tả | Chia Sẻ Với | Yêu Cầu Chấp Thuận |
|-------|------|----------|-------------|-------------|------------------|
| **Local** (mặc định) | `--scope local` | `~/.claude.json` (dưới đường dẫn project) | Riêng tư cho người dùng hiện tại, chỉ trong project hiện tại (được gọi là `project` trong các phiên bản cũ hơn) | Chỉ bạn | Không |
| **Project** | `--scope project` | `.mcp.json` | Được commit vào git repository | Các thành viên nhóm | Có (lần sử dụng đầu) |
| **User** | `--scope user` | `~/.claude.json` | Có sẵn trên tất cả project (được gọi là `global` trong các phiên bản cũ hơn) | Chỉ bạn | Không |

Chọn phạm vi khi thêm server bằng `--scope` (dạng ngắn `-s`). Nếu bỏ qua, Claude
Code sử dụng `local`:

```bash
# Phạm vi project — ghi vào .mcp.json để cả nhóm dùng chung
claude mcp add --scope project --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# Phạm vi user — có sẵn trong mọi project
claude mcp add --scope user --transport stdio memory -- npx @modelcontextprotocol/server-memory
```

### Sử Dụng Phạm Vi Project

Lưu trữ cấu hình MCP riêng cho project trong `.mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

Các thành viên nhóm sẽ thấy prompt chấp thuận khi sử dụng MCP của project lần đầu. Trong một workspace chưa được tin cậy, các server mà repo tự phê duyệt qua file `.claude/settings.json` đã commit sẽ **không** được `claude mcp list`/`get` tự động khởi chạy — chúng hiển thị `⏸ Pending approval` cho đến khi bạn chấp nhận hộp thoại tin cậy, và `enableAllProjectMcpServers` bị bỏ qua trong thư mục chưa được tin cậy (v2.1.196).

## Quản Lý Cấu Hình MCP

### Thêm MCP Server

```bash
# Thêm server dựa trên HTTP
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# Thêm server stdio cục bộ
claude mcp add --transport stdio database -- npx @company/db-server

# Liệt kê tất cả MCP server
claude mcp list

# Lấy chi tiết về một server cụ thể
claude mcp get github

# Xóa một MCP server
claude mcp remove github

# Reset các lựa chọn chấp thuận riêng của project
claude mcp reset-project-choices

# Xác thực một MCP server từ CLI (v2.1.186+)
claude mcp login github

# Đăng xuất khỏi một MCP server (v2.1.186+)
claude mcp logout github

# Import từ Claude Desktop
claude mcp add-from-claude-desktop

# Thêm server từ một chuỗi JSON (hữu ích cho thiết lập bằng script)
claude mcp add-json events-server '{"type":"stdio","command":"npx","args":["@modelcontextprotocol/server-events"]}'
```

> **Lưu ý**: Trong cấu hình JSON — `.mcp.json`, `~/.claude.json` hoặc `claude mcp add-json` — trường `type` chấp nhận `streamable-http` như một bí danh của `http`. Đặc tả MCP dùng tên `streamable-http` cho giao thức này, nên cấu hình sao chép từ tài liệu của chính server vẫn hoạt động mà không cần sửa.

Từ v2.1.238, `claude mcp list` và `claude mcp get` hiển thị các server bị tắt là `⊘ Disabled` mà không kết nối tới chúng để kiểm tra sức khỏe. Một server bị chính sách của tổ chức bạn từ chối hiển thị là `✘ Blocked by enterprise managed policy` trong cả hai lệnh; server bị lọc bởi allowlist, denylist hoặc hạn chế MCP được quản lý khác thì bị ẩn thay vì được liệt kê.

`claude mcp login <name>` / `claude mcp logout <name>` là phiên bản không tương tác của flow OAuth trong menu `/mcp` — xác thực hoặc đăng xuất mà không cần mở menu. Thêm `--no-browser` vào `login` để hoàn tất OAuth qua SSH hoặc trong phiên headless (nó chuyển hướng flow qua stdin). `claude mcp remove` xóa các token OAuth đã lưu nhưng không thu hồi chúng; để thu hồi ở nơi authorization server hỗ trợ, hãy chạy `claude mcp logout <name>` trước `claude mcp remove <name>`.

## Bảng MCP Server Có Sẵn

| MCP Server | Mục Đích | Công Cụ Thường Gặp | Xác Thực | Thời Gian Thực |
|------------|---------|--------------|------|-----------|
| **Filesystem** | Thao tác file | read, write, delete | Quyền hệ điều hành | ✅ Có |
| **GitHub** | Quản lý repository | list_prs, create_issue, push | OAuth | ✅ Có |
| **Slack** | Giao tiếp nhóm | send_message, list_channels | Token | ✅ Có |
| **Database** | Truy vấn SQL | query, insert, update | Credentials | ✅ Có |
| **Google Docs** | Truy cập tài liệu | read, write, share | OAuth | ✅ Có |
| **Asana** | Quản lý dự án | create_task, update_status | API Key | ✅ Có |
| **Stripe** | Dữ liệu thanh toán | list_charges, create_invoice | API Key | ✅ Có |
| **Memory** | Bộ nhớ liên tục | store, retrieve, delete | Cục bộ | ❌ Không |

## Ví Dụ Thực Tiễn

### Ví Dụ 1: Cấu Hình GitHub MCP

**File:** `.mcp.json` (thư mục gốc project)

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

**Các công cụ GitHub MCP có sẵn:**

#### Quản Lý Pull Request
- `list_prs` - Liệt kê tất cả PR trong repository
- `get_pr` - Lấy chi tiết PR bao gồm diff
- `create_pr` - Tạo PR mới
- `update_pr` - Cập nhật mô tả/tiêu đề PR
- `merge_pr` - Merge PR vào branch chính
- `review_pr` - Thêm bình luận review

**Yêu cầu mẫu:**
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### Quản Lý Issue
- `list_issues` - Liệt kê tất cả issue
- `get_issue` - Lấy chi tiết issue
- `create_issue` - Tạo issue mới
- `close_issue` - Đóng issue
- `add_comment` - Thêm bình luận vào issue

#### Thông Tin Repository
- `get_repo_info` - Chi tiết repository
- `list_files` - Cấu trúc cây file
- `get_file_content` - Đọc nội dung file
- `search_code` - Tìm kiếm trên toàn codebase

#### Thao Tác Commit
- `list_commits` - Lịch sử commit
- `get_commit` - Chi tiết một commit cụ thể
- `create_commit` - Tạo commit mới

**Thiết lập**:
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
# Hoặc sử dụng CLI để thêm trực tiếp:
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

### Mở Rộng Biến Môi Trường Trong Cấu Hình

Cấu hình MCP hỗ trợ mở rộng biến môi trường với giá trị mặc định dự phòng. Cú pháp `${VAR}` và `${VAR:-default}` hoạt động trong các trường sau: `command`, `args`, `env`, `url` và `headers`.

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}",
        "X-Custom-Header": "${CUSTOM_HEADER:-default-value}"
      }
    },
    "local-server": {
      "command": "${MCP_BIN_PATH:-npx}",
      "args": ["${MCP_PACKAGE:-@company/mcp-server}"],
      "env": {
        "DB_URL": "${DATABASE_URL:-postgresql://localhost/dev}"
      }
    }
  }
}
```

Các biến được mở rộng lúc runtime:
- `${VAR}` - Sử dụng biến môi trường; nếu biến chưa được đặt (và không có mặc định), server vẫn được tải với chuỗi `${VAR}` nguyên văn, và `claude mcp list` cùng `/mcp` cảnh báo về biến bị thiếu
- `${VAR:-default}` - Sử dụng biến môi trường, dùng giá trị mặc định nếu biến chưa được đặt. Một biến được đặt thành chuỗi rỗng được coi là đã đặt và mở rộng thành rỗng (ví dụ `url` trở thành `/mcp`); hãy unset biến đó để dùng giá trị mặc định

### Ví Dụ 2: Thiết Lập Database MCP

**Cấu hình:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "${DATABASE_URL}"]
    }
  }
}
```

**Ví dụ sử dụng:**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Using MCP database tool:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Results:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

**Thiết lập**:
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
claude mcp add --transport stdio database -- npx -y @bytebase/dbhub \
  --dsn "$DATABASE_URL"
```

> **Cảnh báo**: Thiết lập này cho Claude quyền ghi. Công cụ `execute_sql` của DBHub chạy mọi câu SQL nó nhận được, kể cả `UPDATE`, `DELETE` và `DROP`, trừ khi bạn bật chế độ chỉ đọc. Hãy dùng database cục bộ hoặc database dùng thử, không bao giờ dùng production.

**Thiết lập chỉ đọc (khuyến nghị):**

Tạo một user database chỉ được chạy `SELECT` (ví dụ PostgreSQL):

```sql
CREATE ROLE claude_readonly LOGIN PASSWORD 'change-me';
GRANT CONNECT ON DATABASE mydb TO claude_readonly;
GRANT USAGE ON SCHEMA public TO claude_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO claude_readonly;
```

Bật chế độ chỉ đọc trong file `dbhub.toml`. Cờ `--readonly` cũ không còn hoạt động. DBHub lấy `${DATABASE_URL}` từ biến môi trường, nên không cần ghi credentials vào file:

```toml
[[sources]]
id = "default"
dsn = "${DATABASE_URL}"

[[tools]]
name = "execute_sql"
source = "default"
readonly = true
```

Sau đó trỏ DBHub tới file này thay vì truyền `--dsn`. Trước tiên hãy xóa server `database` có quyền ghi đã thêm ở trên, vì Claude Code không cho thêm server thứ hai trùng tên:

```bash
# Thay thế server có quyền ghi đã thêm ở trên
claude mcp remove database
export DATABASE_URL="postgresql://claude_readonly:change-me@localhost/mydb"
claude mcp add --transport stdio database -- npx -y @bytebase/dbhub \
  --config "$PWD/dbhub.toml"
```

Chế độ chỉ đọc lọc theo nội dung câu SQL và từng bị vượt qua trong quá khứ (đã sửa trong DBHub 0.22.6), nên user chỉ có quyền `SELECT` mới là lớp thực sự bảo vệ dữ liệu của bạn. Xem [chế độ chỉ đọc của DBHub](https://dbhub.ai/tools/execute-sql#read-only-mode).

### Ví Dụ 3: Workflow Nhiều MCP

**Kịch bản: Tạo báo cáo hàng ngày**

```markdown
# Workflow Báo Cáo Hàng Ngày Sử Dụng Nhiều MCP

## Thiết Lập
1. GitHub MCP - lấy số liệu PR
2. Database MCP - truy vấn dữ liệu bán hàng
3. Slack MCP - đăng báo cáo
4. Filesystem MCP - lưu báo cáo

## Workflow

### Bước 1: Lấy Dữ Liệu GitHub
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Bước 2: Truy Vấn Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Bước 3: Tạo Báo Cáo
Kết hợp dữ liệu thành báo cáo HTML

### Bước 4: Lưu Vào Filesystem
Ghi report.html vào /reports/

### Bước 5: Đăng Lên Slack
Gửi tóm tắt vào kênh #daily-reports

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

**Thiết lập**:
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_BOT_TOKEN="your_slack_bot_token"
export SLACK_TEAM_ID="your_slack_team_id"
# Thêm từng MCP server qua CLI hoặc cấu hình chúng trong .mcp.json
```

### Ví Dụ 4: Thao Tác Filesystem MCP

**Cấu hình:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**Các thao tác có sẵn:**

| Thao Tác | Lệnh | Mục Đích |
|-----------|---------|---------|
| Liệt kê file | `ls ~/projects` | Hiển thị nội dung thư mục |
| Đọc file | `cat src/main.ts` | Đọc nội dung file |
| Ghi file | `create docs/api.md` | Tạo file mới |
| Sửa file | `edit src/app.ts` | Sửa đổi file |
| Tìm kiếm | `grep "async function"` | Tìm kiếm trong file |
| Xóa | `rm old-file.js` | Xóa file |

**Thiết lập**:
```bash
# Sử dụng CLI để thêm trực tiếp:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## MCP Và Bộ Nhớ: Ma Trận Quyết Định

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## Mẫu Request/Response

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: Real-time access<br/>No caching
```

## Biến Môi Trường

Lưu trữ credentials nhạy cảm trong biến môi trường:

```bash
# ~/.bashrc hoặc ~/.zshrc
export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_BOT_TOKEN="your-slack-bot-token"
export SLACK_TEAM_ID="T0000000000"
```

Sau đó tham chiếu chúng trong cấu hình MCP:

```json
{
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
  }
}
```

## Claude Như Một MCP Server (`claude mcp serve`)

Bản thân Claude Code có thể hoạt động như một MCP server cho các ứng dụng khác. Điều này cho phép các công cụ bên ngoài, trình soạn thảo và hệ thống tự động hóa tận dụng khả năng của Claude qua giao thức MCP chuẩn.

```bash
# Khởi động Claude Code như một MCP server trên stdio
claude mcp serve
```

Các ứng dụng khác sau đó có thể kết nối đến server này như với bất kỳ MCP server dựa trên stdio nào. Ví dụ, để thêm Claude Code như một MCP server trong một instance Claude Code khác:

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

Điều này hữu ích để xây dựng workflow nhiều tác nhân, trong đó một instance Claude điều phối một instance khác.

## Cấu Hình MCP Được Quản Lý (Enterprise)

Đối với các triển khai enterprise, quản trị viên IT thực thi chính sách MCP server qua hai cơ chế tách biệt: file `managed-mcp.json` triển khai một tập server cố định với quyền kiểm soát độc quyền, và các settings key `allowedMcpServers` / `deniedMcpServers` lọc xem những server đã cấu hình nào được phép tải.

**Vị trí:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux và WSL: `/etc/claude-code/managed-mcp.json`
- Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`

`managed-mcp.json` dùng cùng định dạng với file `.mcp.json` của project — một map `mcpServers` ở cấp cao nhất. Nó triển khai server; nó không lọc server:

```json
{
  "mcpServers": {
    "example-remote": {
      "type": "http",
      "url": "https://mcp.example.com/mcp"
    },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"]
    }
  }
}
```

Mọi người dùng trên máy đều đọc được file này, nên đừng bao giờ đặt credentials trong khối `env`. Hãy dùng mở rộng biến `${VAR}`, OAuth hoặc `headersHelper` thay thế.

> **Lưu ý (v2.1.305):** Server trong `managed-mcp.json` không cần mục `allowedMcpServers`. Allowlist chỉ kiểm tra một server được quản lý khi server đó dùng mở rộng `${VAR}` bên ngoài `env`; trước v2.1.305 nó cũng kiểm tra cả server chỉ dùng `${VAR}` trong `env`. Nếu bạn từng dựa vào `allowedMcpServers` để chặn một server như vậy, giờ nó sẽ được tải khi nâng cấp mà không hỏi; hãy thêm một mục `deniedMcpServers` cho nó.

**Lọc: allowlist và denylist**

`allowedMcpServers`, `deniedMcpServers` và `allowAllClaudeAiMcps` là **settings key, không phải trường của `managed-mcp.json`**. Hãy đặt chúng trong một nguồn settings được quản lý — server-managed settings, `managed-settings.json`, một MDM profile hoặc registry — để chúng có hiệu lực thực thi:

- `allowedMcpServers` -- allowlist các server được phép. Đặt `allowManagedMcpServersOnly: true` cùng với nó, trong cùng nguồn được quản lý, nếu không các allowlist sẽ hợp nhất từ mọi phạm vi và người dùng có thể nới rộng allowlist của bạn.
- `deniedMcpServers` -- denylist các server bị chặn. Luôn hợp nhất từ mọi phạm vi.
- `allowAllClaudeAiMcps` -- tải các cloud connector của claude.ai cùng với một `managed-mcp.json` đã triển khai (v2.1.149+). Chỉ được đọc từ các tầng chính sách do quản trị viên kiểm soát.

Mỗi mục là một object với **duy nhất một** key:

| Key | Khớp với |
|-----|---------|
| `serverUrl` | URL của server từ xa, khớp chính xác hoặc dùng ký tự đại diện `*` |
| `serverCommand` | Chính xác lệnh và các tham số khởi động một stdio server, dưới dạng mảng — mọi tham số, đúng thứ tự |
| `serverName` | Nhãn do người dùng đặt. **Chỉ khớp chính xác; ký tự đại diện không được mở rộng** |

**Ví dụ cấu hình:**

```json
{
  "allowedMcpServers": [
    { "serverUrl": "https://mcp.example.com/*" },
    { "serverCommand": ["/usr/local/bin/company-mcp-server", "--config", "/etc/company/mcp-config.json"] }
  ],
  "deniedMcpServers": [
    { "serverName": "untrusted-server" },
    { "serverUrl": "http://*" }
  ],
  "allowManagedMcpServersOnly": true
}
```

Một setting được quản lý thứ ba, `managedMcpServers` (v2.1.259+), cho phép tổ chức cung cấp MCP server HTTP/SSE cho mọi người dùng. Các mục dùng cùng cấu trúc như `.mcp.json`; các mục chỉ định một lệnh để chạy sẽ bị bỏ qua.

> **Lưu ý:** Khi cả `allowedMcpServers` và `deniedMcpServers` cùng khớp một server, quy tắc deny được ưu tiên.

## MCP Server Do Plugin Cung Cấp

Plugin có thể đóng gói MCP server riêng, giúp chúng tự động có sẵn khi plugin được cài đặt. MCP server do plugin cung cấp có thể được định nghĩa theo hai cách:

1. **`.mcp.json` độc lập** -- Đặt một file `.mcp.json` trong thư mục gốc của plugin
2. **Inline trong `plugin.json`** -- Định nghĩa MCP server trực tiếp trong manifest của plugin

Sử dụng biến `${CLAUDE_PLUGIN_ROOT}` để tham chiếu các đường dẫn tương đối với thư mục cài đặt plugin:

```json
{
  "mcpServers": {
    "plugin-tools": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/dist/mcp-server.js"],
      "env": {
        "CONFIG_PATH": "${CLAUDE_PLUGIN_ROOT}/config.json"
      }
    }
  }
}
```

## MCP Theo Phạm Vi Tác Nhân Con

MCP server có thể được định nghĩa inline trong frontmatter của tác nhân bằng key `mcpServers:`, giới hạn chúng trong một tác nhân con cụ thể thay vì toàn bộ project. Điều này hữu ích khi một tác nhân cần truy cập một MCP server cụ thể mà các tác nhân khác trong workflow không cần.

```yaml
---
name: my-tool-agent
description: Uses my-tool for specialized operations
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

MCP server theo phạm vi tác nhân con chỉ có sẵn trong ngữ cảnh thực thi của tác nhân đó và không được chia sẻ với tác nhân cha hoặc các tác nhân anh em.

## Giới Hạn Đầu Ra MCP

Claude Code áp dụng giới hạn lên đầu ra của công cụ MCP để tránh tràn ngữ cảnh:

| Giới Hạn | Ngưỡng | Hành Vi |
|-------|-----------|----------|
| **Cảnh báo** | 10.000 token | Hiển thị cảnh báo rằng đầu ra lớn |
| **Tối đa mặc định** | 25.000 token | Đầu ra lớn hơn được lưu vào một file, và đường dẫn file được đưa vào cuộc hội thoại thay thế |
| **Lưu xuống đĩa** | 50.000 ký tự | Kết quả công cụ vượt quá 50K ký tự được lưu xuống đĩa |

Giới hạn đầu ra tối đa có thể cấu hình qua biến môi trường `MAX_MCP_OUTPUT_TOKENS`:

```bash
# Tăng giới hạn đầu ra tối đa lên 50.000 token
export MAX_MCP_OUTPUT_TOKENS=50000
```

## Tự Động Chuyển Nền Các Lời Gọi Công Cụ Chạy Lâu (v2.1.212)

Các lời gọi công cụ MCP chạy lâu hơn 2 phút giờ tự động chuyển sang chạy nền, nên phiên vẫn dùng được thay vì bị chặn bởi một công cụ chậm. Ngưỡng này có thể cấu hình, và hành vi có thể tinh chỉnh hoặc tắt, qua `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`:

```bash
# Đổi ngưỡng tự động chuyển nền thành 5 phút (300.000ms)
export CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS=300000
```

Đặt thành `0` để tắt tự động chuyển nền; `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` tắt nó cùng với các lệnh nền và tác nhân con chạy nền. Để giới hạn thời gian một lời gọi được phép chạy, thêm `timeout` theo từng server tính bằng mili giây (giới hạn cứng theo thời gian thực) hoặc đặt `MCP_TOOL_TIMEOUT` cho mọi server (mặc định khoảng 28 giờ).

### MCP Task (public beta, v2.1.304+)

Một server hỗ trợ extension MCP tasks có thể tự chạy một công việc dài: lời gọi công cụ của Claude trả về ngay khi server chấp nhận công việc, footer hiển thị số đếm như `1 MCP task`, và Claude nhận kết quả khi công việc kết thúc. Dừng một task trong `/tasks` bằng `x`. Task trên server từ xa vẫn tiếp tục chạy sau khi bạn thoát; hãy tiếp tục lại cùng phiên để theo dõi nó. Task cần protocol revision 2026-07-28, khả năng lấy feature flag (nên không dùng được với Bedrock, Vertex, Foundry hoặc khi tắt telemetry) và một phiên CLI terminal, Agent SDK hoặc GitHub Actions. Một lần chạy không tương tác chỉ có task từ Agent SDK hoặc `claude -p --input-format stream-json`, và cả hai đều cần `CLAUDE_AUTO_BACKGROUND_TASKS=1` (một lệnh `claude -p "<prompt>"` thông thường không có). VS Code và ứng dụng desktop không có task, và lời gọi từ tác nhân con không bao giờ trở thành task. Để Claude chờ kết quả của task, đặt `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND=1` (hoặc `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS=0` để chờ mọi lời gọi MCP).

## Giải Quyết Phình Ngữ Cảnh Bằng Thực Thi Code

Khi việc áp dụng MCP mở rộng quy mô, kết nối đến hàng chục server với hàng trăm hoặc hàng nghìn công cụ tạo ra một thách thức đáng kể: **phình ngữ cảnh (context bloat)**. Đây có lẽ là vấn đề lớn nhất với MCP ở quy mô lớn, và đội ngũ kỹ thuật của Anthropic đã đề xuất một giải pháp tinh tế — sử dụng thực thi code thay vì gọi công cụ trực tiếp.

> **Nguồn**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic Engineering Blog

### Vấn Đề: Hai Nguồn Lãng Phí Token

**1. Định nghĩa công cụ làm quá tải cửa sổ ngữ cảnh**

Hầu hết MCP client tải tất cả định nghĩa công cụ ngay từ đầu. Khi kết nối đến hàng nghìn công cụ, mô hình phải xử lý hàng trăm nghìn token trước cả khi đọc yêu cầu của người dùng.

**2. Kết quả trung gian tiêu tốn thêm token**

Mọi kết quả công cụ trung gian đều đi qua ngữ cảnh của mô hình. Hãy xem xét việc chuyển bản ghi cuộc họp từ Google Drive sang Salesforce — toàn bộ bản ghi đi qua ngữ cảnh **hai lần**: một lần khi đọc, và một lần nữa khi ghi nó tới đích. Bản ghi một cuộc họp 2 giờ có thể tốn thêm hơn 50.000 token.

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### Giải Pháp: Công Cụ MCP Như API Trong Code

Thay vì chuyển định nghĩa công cụ và kết quả qua cửa sổ ngữ cảnh, tác nhân **viết code** gọi các công cụ MCP như API. Code chạy trong một môi trường thực thi sandbox, và chỉ kết quả cuối cùng được trả về mô hình.

```mermaid
graph LR
    A["Model"] -->|"Writes code"| B["Code Execution<br/>Environment"]
    B -->|"Calls tools directly"| C["MCP Servers"]
    C -->|"Data stays in<br/>execution env"| B
    B -->|"Only final result<br/>(minimal tokens)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

#### Cách Hoạt Động

Các công cụ MCP được trình bày dưới dạng một cây file gồm các hàm có kiểu:

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

Mỗi file công cụ chứa một wrapper có kiểu:

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

export async function getDocument(
  input: GetDocumentInput
): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>(
    'google_drive__get_document', input
  );
}
```

Sau đó tác nhân viết code để điều phối các công cụ:

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// Dữ liệu đi trực tiếp giữa các công cụ — không bao giờ qua mô hình
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**Kết quả: Lượng token sử dụng giảm từ ~150.000 xuống ~2.000 — giảm 98,7%.**

### Lợi Ích Chính

| Lợi Ích | Mô Tả |
|---------|-------------|
| **Tiết lộ dần (progressive disclosure)** | Tác nhân duyệt filesystem để chỉ tải các định nghĩa công cụ cần thiết, thay vì tải tất cả công cụ ngay từ đầu |
| **Kết quả tiết kiệm ngữ cảnh** | Dữ liệu được lọc/biến đổi trong môi trường thực thi trước khi trả về mô hình |
| **Luồng điều khiển mạnh mẽ** | Vòng lặp, điều kiện và xử lý lỗi chạy trong code mà không cần đi vòng qua mô hình |
| **Bảo vệ quyền riêng tư** | Dữ liệu trung gian (PII, hồ sơ nhạy cảm) ở lại trong môi trường thực thi; không bao giờ đi vào ngữ cảnh mô hình |
| **Lưu giữ trạng thái** | Tác nhân có thể lưu kết quả trung gian vào file và xây dựng các hàm skill có thể tái sử dụng |

#### Ví Dụ: Lọc Tập Dữ Liệu Lớn

```typescript
// Không có thực thi code — toàn bộ 10.000 dòng đi qua ngữ cảnh
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> trả về 10.000 dòng trong ngữ cảnh

// Có thực thi code — lọc trong môi trường thực thi
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Chỉ 5 dòng đến được mô hình
```

#### Ví Dụ: Vòng Lặp Không Cần Đi Vòng Qua Mô Hình

```typescript
// Chờ thông báo triển khai — chạy hoàn toàn trong code
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({
    channel: 'C123456'
  });
  found = messages.some(
    m => m.text.includes('deployment complete')
  );
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

### Các Đánh Đổi Cần Cân Nhắc

Thực thi code mang theo độ phức tạp riêng. Chạy code do tác nhân tạo ra đòi hỏi:

- Một **môi trường thực thi sandbox an toàn** với giới hạn tài nguyên phù hợp
- **Giám sát và ghi log** code được thực thi
- Thêm **chi phí hạ tầng** so với gọi công cụ trực tiếp

Các lợi ích — giảm chi phí token, độ trễ thấp hơn, kết hợp công cụ tốt hơn — cần được cân nhắc với các chi phí triển khai này. Với các tác nhân chỉ có vài MCP server, gọi công cụ trực tiếp có thể đơn giản hơn. Với các tác nhân ở quy mô lớn (hàng chục server, hàng trăm công cụ), thực thi code là một cải thiện đáng kể.

### MCPorter: Runtime Để Kết Hợp Công Cụ MCP

[MCPorter](https://github.com/steipete/mcporter) là một runtime TypeScript và bộ công cụ CLI giúp việc gọi MCP server trở nên thực tế mà không cần boilerplate — và giúp giảm phình ngữ cảnh nhờ chỉ cung cấp công cụ có chọn lọc và các wrapper có kiểu.

**Vấn đề nó giải quyết:** Thay vì tải tất cả định nghĩa công cụ từ mọi MCP server ngay từ đầu, MCPorter cho phép bạn khám phá, kiểm tra và gọi các công cụ cụ thể khi cần — giữ ngữ cảnh của bạn gọn nhẹ.

**Tính năng chính:**

| Tính Năng | Mô Tả |
|---------|-------------|
| **Khám phá không cần cấu hình** | Tự động khám phá MCP server từ Cursor, Claude, Codex hoặc cấu hình cục bộ |
| **Client công cụ có kiểu** | `mcporter emit-ts` tạo interface `.d.ts` và wrapper sẵn sàng chạy |
| **API có thể kết hợp** | `createServerProxy()` cung cấp công cụ dưới dạng phương thức camelCase với các helper `.text()`, `.json()`, `.markdown()` |
| **Tạo CLI** | `mcporter generate-cli` chuyển bất kỳ MCP server nào thành một CLI độc lập với bộ lọc `--include-tools` / `--exclude-tools` |
| **Ẩn tham số** | Tham số tùy chọn được ẩn theo mặc định, giảm độ dài dòng của schema |

**Cài đặt:**

```bash
npx mcporter list          # Không cần cài đặt — khám phá server ngay lập tức
pnpm add mcporter          # Thêm vào project
brew install steipete/tap/mcporter  # macOS qua Homebrew
```

**Ví dụ — kết hợp công cụ trong TypeScript:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Dữ liệu đi giữa các công cụ mà không qua ngữ cảnh mô hình
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**Ví dụ — gọi công cụ qua CLI:**

```bash
# Gọi trực tiếp một công cụ cụ thể
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# Liệt kê các server và công cụ có sẵn
npx mcporter list
```

MCPorter bổ sung cho cách tiếp cận thực thi code ở trên bằng cách cung cấp hạ tầng runtime để gọi công cụ MCP như API có kiểu — giúp việc giữ dữ liệu trung gian ngoài ngữ cảnh mô hình trở nên đơn giản.

## Thực Hành Tốt Nhất

### Cân Nhắc Bảo Mật

#### Nên Làm ✅
- Sử dụng biến môi trường cho mọi credentials
- Xoay vòng token và API key thường xuyên (khuyến nghị hàng tháng)
- Sử dụng token chỉ đọc khi có thể
- Giới hạn phạm vi truy cập của MCP server ở mức tối thiểu cần thiết
- Giám sát việc sử dụng MCP server và log truy cập
- Sử dụng OAuth cho các dịch vụ bên ngoài khi có sẵn
- Áp dụng giới hạn tần suất (rate limiting) cho các request MCP
- Kiểm thử kết nối MCP trước khi dùng cho production
- Ghi lại tài liệu cho mọi kết nối MCP đang hoạt động
- Giữ các gói MCP server luôn được cập nhật

#### Không Nên Làm ❌
- Đừng hardcode credentials trong file cấu hình
- Đừng commit token hoặc secret vào git
- Đừng chia sẻ token trong chat nhóm hoặc email
- Đừng dùng token cá nhân cho project của nhóm
- Đừng cấp các quyền không cần thiết
- Đừng bỏ qua lỗi xác thực
- Đừng công khai endpoint MCP
- Đừng chạy MCP server với quyền root/admin
- Đừng lưu dữ liệu nhạy cảm trong log
- Đừng tắt các cơ chế xác thực

### Thực Hành Tốt Nhất Về Cấu Hình

1. **Quản lý phiên bản**: Giữ `.mcp.json` trong git nhưng dùng biến môi trường cho secret
2. **Đặc quyền tối thiểu**: Chỉ cấp các quyền tối thiểu cần thiết cho mỗi MCP server
3. **Cô lập**: Chạy các MCP server khác nhau trong các tiến trình riêng khi có thể
4. **Giám sát**: Ghi log mọi request và lỗi MCP để phục vụ kiểm toán
5. **Kiểm thử**: Kiểm thử mọi cấu hình MCP trước khi triển khai lên production

### Mẹo Hiệu Suất

- Cache dữ liệu được truy cập thường xuyên ở cấp ứng dụng
- Dùng các truy vấn MCP cụ thể để giảm lượng dữ liệu truyền
- Theo dõi thời gian phản hồi của các thao tác MCP
- Cân nhắc giới hạn tần suất cho các API bên ngoài
- Dùng batching khi thực hiện nhiều thao tác

## Hướng Dẫn Cài Đặt

### Điều Kiện Tiên Quyết
- Đã cài Node.js và npm
- Đã cài Claude Code CLI
- Có API token/credentials cho các dịch vụ bên ngoài

### Thiết Lập Từng Bước

1. **Thêm MCP server đầu tiên của bạn** bằng CLI (ví dụ: GitHub):
```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

   Hoặc tạo file `.mcp.json` trong thư mục gốc project của bạn:
```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

2. **Đặt biến môi trường:**
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_personal_access_token"
```

3. **Kiểm tra kết nối:**
```bash
claude /mcp
```

4. **Sử dụng công cụ MCP:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### Cài Đặt Cho Các Dịch Vụ Cụ Thể

**GitHub MCP:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**Database MCP:**
```bash
npm install -g @bytebase/dbhub
```

**Filesystem MCP:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP (gói đã ngừng hỗ trợ):**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## Xử Lý Sự Cố

### Bắt Đầu Từ Thông Báo Lỗi (v2.1.219+)

Nếu một server không kết nối được, hãy chạy `claude mcp list` (hoặc `/mcp` trong phiên) trước khi thay đổi bất cứ điều gì. Claude Code giờ in ra **mã trạng thái HTTP và nội dung lỗi của server** cạnh server bị lỗi, nên bạn sẽ thấy `401 Unauthorized` hoặc `404 Not Found` thay vì một thông báo chung chung "failed to connect":

```bash
# Hiển thị trạng thái kết nối kèm mã HTTP và nội dung lỗi khi thất bại
claude mcp list
```

Hãy đọc mã trạng thái trước — nó cho bạn biết nên áp dụng cách sửa nào:

- `401` / `403` → credentials sai hoặc đã hết hạn; xác thực lại bằng `claude mcp login <name>`
- `404` → sai URL (nguyên nhân thường gặp là thiếu hậu tố đường dẫn `/mcp` hoặc `/sse`)
- `5xx` / timeout → server từ xa đang gặp sự cố; xem [Hết Thời Gian Kết Nối](#hết-thời-gian-kết-nối)

### Khoảng Trắng Ẩn Trong Giá Trị Cấu Hình (v2.1.219+)

Claude Code cảnh báo khi một giá trị cấu hình MCP có **khoảng trắng ở đầu hoặc cuối**. Đây là nguyên nhân phổ biến và khó phát hiện của lỗi xác thực: một token sao chép từ trình duyệt hoặc tin nhắn chat thường kèm theo dấu cách hoặc ký tự xuống dòng ở cuối, được gửi nguyên văn trong header `Authorization` và bị từ chối như credentials không hợp lệ.

Nếu bạn thấy cảnh báo này, hãy kiểm tra lại giá trị trong `.mcp.json` (hoặc biến môi trường mà nó được mở rộng từ đó) và loại bỏ khoảng trắng:

```bash
# Làm lộ khoảng trắng ẩn ở đầu/cuối giữa hai dấu ngoặc
printf '[%s]\n' "$GITHUB_PERSONAL_ACCESS_TOKEN"
```

### Server Bị Bỏ Qua Khi Chạy Headless (v2.1.219+)

Các server truyền qua `--mcp-config` mà không vượt qua kiểm tra cấu hình sẽ bị **bỏ qua** thay vì làm dừng lần chạy, nên một script headless có thể trông như hoạt động bình thường trong khi thiếu một nửa công cụ. Claude Code giờ báo cáo những server nào đã bị loại bỏ:

- **Lần chạy headless / `-p`**: sự kiện `init` của stream-json chứa trường `mcp_server_errors` liệt kê mọi mục bị bỏ qua. Hãy kiểm tra nó trước khi tin vào kết quả của lần chạy.
- **Lần chạy terminal tương tác**: cùng vấn đề này được in ra thành cảnh báo khi phiên bắt đầu.

```bash
# Kiểm tra các mục --mcp-config bị bỏ qua trong một lần chạy headless
claude -p "list my tools" --mcp-config ./servers.json \
  --output-format stream-json --verbose \
  | jq -r 'select(.type == "system" and .subtype == "init") | .mcp_server_errors'
```

### Không Tìm Thấy MCP Server
```bash
# Xác minh MCP server đã được cài đặt
npm list -g @modelcontextprotocol/server-github

# Cài đặt nếu thiếu
npm install -g @modelcontextprotocol/server-github
```

### Xác Thực Thất Bại
```bash
# Xác minh biến môi trường đã được đặt
echo $GITHUB_PERSONAL_ACCESS_TOKEN

# Export lại nếu cần
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"

# Xác minh token có đúng quyền
# Kiểm tra scope của GitHub token tại: https://github.com/settings/tokens
```

### Hết Thời Gian Kết Nối
- Kiểm tra kết nối mạng: `ping api.github.com`
- Xác minh API endpoint có thể truy cập
- Kiểm tra giới hạn tần suất của API
- Tăng `timeout` (mili giây) trong mục cấu hình của server, hoặc `MCP_TOOL_TIMEOUT` cho mọi server
- Kiểm tra các vấn đề về firewall hoặc proxy

### MCP Server Bị Crash
- Kiểm tra log của MCP server: `~/.claude/logs/`
- Xác minh tất cả biến môi trường đã được đặt
- Đảm bảo quyền file phù hợp
- Thử cài đặt lại gói MCP server
- Kiểm tra các tiến trình xung đột trên cùng một cổng

## Các Khái Niệm Liên Quan

### Bộ Nhớ Và MCP
- **Bộ nhớ (Memory)**: Lưu trữ dữ liệu bền vững, không thay đổi (sở thích, ngữ cảnh, lịch sử)
- **MCP**: Truy cập dữ liệu trực tiếp, thay đổi liên tục (API, database, dịch vụ thời gian thực)

### Khi Nào Dùng Cái Nào
- **Dùng bộ nhớ** cho: Sở thích người dùng, lịch sử hội thoại, ngữ cảnh đã học
- **Dùng MCP** cho: Các issue GitHub hiện tại, truy vấn database trực tiếp, dữ liệu thời gian thực

### Tích Hợp Với Các Tính Năng Khác Của Claude
- Kết hợp MCP với bộ nhớ để có ngữ cảnh phong phú
- Dùng công cụ MCP trong prompt để suy luận tốt hơn
- Tận dụng nhiều MCP cho các workflow phức tạp

## Tài Nguyên Thêm

- [Tài Liệu MCP Chính Thức](https://code.claude.com/docs/en/mcp)
- [Đặc Tả Giao Thức MCP](https://modelcontextprotocol.io/specification)
- [Kho GitHub MCP](https://github.com/modelcontextprotocol/servers)
- [Các MCP Server Có Sẵn](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — Runtime & CLI TypeScript để gọi MCP server mà không cần boilerplate
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Blog kỹ thuật của Anthropic về giải quyết phình ngữ cảnh
- [Tham Chiếu CLI Claude Code](https://code.claude.com/docs/en/cli-reference)
- [Tài Liệu API Claude](https://docs.anthropic.com)

---

**Cập Nhật Lần Cuối**: Ngày 1 tháng 11 năm 2026
**Phiên Bản Claude Code**: 2.1.316
**Nguồn**:
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/managed-mcp
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.139
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/mcp#configure-tool-search
- https://code.claude.com/docs/en/env-vars
- https://github.com/anthropics/claude-code/releases/tag/v2.1.285
- https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- https://code.claude.com/docs/en/mcp#tool-search-for-mcp-server-authors
- https://code.claude.com/docs/en/mcp#environment-variable-expansion-in-mcp-json
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/changelog#2-1-304
- https://code.claude.com/docs/en/changelog#2-1-305
- https://code.claude.com/docs/en/mcp#tool-search-through-an-llm-gateway
- https://code.claude.com/docs/en/managed-mcp#how-allowlists-and-denylists-apply-to-the-managed-set
- https://code.claude.com/docs/en/mcp#mcp-tasks-that-run-on-the-server
- https://code.claude.com/docs/en/mcp#what-a-call-needs-to-become-an-mcp-task
- https://code.claude.com/docs/en/mcp#make-claude-wait-for-the-result-of-an-mcp-task
- https://code.claude.com/docs/en/mcp#automatic-backgrounding-of-long-tool-calls
- https://code.claude.com/docs/en/mcp#time-limits-on-mcp-tool-calls
- https://code.claude.com/docs/en/changelog#2-1-307
- https://code.claude.com/docs/en/mcp#mark-tools-that-are-safe-to-call-twice
- https://code.claude.com/docs/en/mcp#variables-set-to-an-empty-string
- https://code.claude.com/docs/en/mcp#managing-your-servers
- https://code.claude.com/docs/en/mcp#server-status
- https://code.claude.com/docs/en/errors#mcp-server-rejected-the-elicitation-capability
- https://code.claude.com/docs/en/mcp#elicitation-modes-claude-code-declares
- https://code.claude.com/docs/en/mcp#use-oauth-with-a-server-behind-an-authenticating-proxy
**Các Mô Hình Tương Thích**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
