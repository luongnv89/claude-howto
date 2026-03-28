<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

Thư mục này chứa tài liệu toàn diện và các ví dụ về cấu hình và cách sử dụng MCP server với Claude Code.

## Tổng quan

MCP (Model Context Protocol — Giao thức Ngữ cảnh Mô hình) là một cách tiêu chuẩn hóa để Claude truy cập các công cụ bên ngoài, API và nguồn dữ liệu thời gian thực. Khác với Memory, MCP cung cấp truy cập trực tiếp vào dữ liệu thay đổi liên tục.

Đặc điểm chính:
- Truy cập thời gian thực vào các dịch vụ bên ngoài
- Đồng bộ dữ liệu trực tiếp
- Kiến trúc có thể mở rộng
- Xác thực bảo mật
- Tương tác dựa trên công cụ

## Kiến trúc MCP

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["Dịch vụ bên ngoài"]

    A -->|Yêu cầu: list_issues| B
    B -->|Truy vấn| C
    C -->|Dữ liệu| B
    B -->|Phản hồi| A

    A -->|Yêu cầu: create_issue| B
    B -->|Hành động| C
    C -->|Kết quả| B
    B -->|Phản hồi| A

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
```

## Hệ sinh thái MCP

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["File cục bộ"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Tin nhắn| J["Slack Workspace"]
    F -->|Tài liệu| K["Google Drive"]

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

## Phương thức cài đặt MCP

Claude Code hỗ trợ nhiều giao thức vận chuyển cho kết nối MCP server:

### HTTP Transport (Khuyến nghị)

```bash
# Kết nối HTTP cơ bản
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP với header xác thực
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Stdio Transport (Cục bộ)

Cho các MCP server chạy cục bộ:

```bash
# Server Node.js cục bộ
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# Với biến môi trường
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### SSE Transport (Đã lỗi thời)

Giao thức Server-Sent Events đã lỗi thời, thay bằng `http` nhưng vẫn được hỗ trợ:

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### WebSocket Transport

WebSocket transport cho kết nối hai chiều liên tục:

```bash
claude mcp add --transport ws realtime-server wss://example.com/mcp
```

### Lưu ý cho Windows

Trên Windows gốc (không phải WSL), dùng `cmd /c` cho các lệnh npx:

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### Xác thực OAuth 2.0

Claude Code hỗ trợ OAuth 2.0 cho các MCP server yêu cầu nó. Khi kết nối với server hỗ trợ OAuth, Claude Code xử lý toàn bộ quy trình xác thực:

```bash
# Kết nối với MCP server hỗ trợ OAuth (quy trình tương tác)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# Cấu hình trước OAuth credentials cho thiết lập không tương tác
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| Tính năng | Mô tả |
|-----------|-------|
| **OAuth tương tác** | Dùng `/mcp` để kích hoạt quy trình OAuth dựa trên trình duyệt |
| **OAuth clients có sẵn** | OAuth clients tích hợp sẵn cho các dịch vụ phổ biến như Notion, Stripe và các dịch vụ khác (v2.1.30+) |
| **Credentials được cấu hình trước** | Cờ `--client-id`, `--client-secret`, `--callback-port` để thiết lập tự động |
| **Lưu trữ token** | Token được lưu trữ bảo mật trong keychain hệ thống |
| **Step-up auth** | Hỗ trợ xác thực step-up cho các thao tác đặc quyền |
| **Discovery caching** | Metadata OAuth discovery được cache để kết nối lại nhanh hơn |
| **Ghi đè Metadata** | `oauth.authServerMetadataUrl` trong `.mcp.json` để ghi đè OAuth metadata discovery mặc định |

#### Ghi đè OAuth Metadata Discovery

Nếu MCP server của bạn trả về lỗi tại endpoint OAuth metadata tiêu chuẩn (`/.well-known/oauth-authorization-server`) nhưng có endpoint OIDC hoạt động, bạn có thể yêu cầu Claude Code lấy OAuth metadata từ URL cụ thể. Đặt `authServerMetadataUrl` trong object `oauth` của cấu hình server:

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

URL phải dùng `https://`. Tùy chọn này yêu cầu Claude Code v2.1.64 trở lên.

### Claude.ai MCP Connectors

Các MCP server được cấu hình trong tài khoản Claude.ai của bạn tự động có sẵn trong Claude Code. Điều này có nghĩa các kết nối MCP bạn thiết lập qua giao diện web Claude.ai sẽ có thể truy cập mà không cần cấu hình thêm.

Claude.ai MCP connectors cũng có sẵn trong chế độ `--print` (v2.1.83+), cho phép sử dụng không tương tác và theo script.

Để tắt MCP servers của Claude.ai trong Claude Code, đặt biến môi trường `ENABLE_CLAUDEAI_MCP_SERVERS` thành `false`:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **Lưu ý:** Tính năng này chỉ có cho người dùng đăng nhập bằng tài khoản Claude.ai.

## Quy trình thiết lập MCP

```mermaid
sequenceDiagram
    participant User as Người dùng
    participant Claude as Claude Code
    participant Config as File cấu hình
    participant Service as Dịch vụ bên ngoài

    User->>Claude: Gõ /mcp
    Claude->>Claude: Liệt kê các MCP server có sẵn
    Claude->>User: Hiển thị tùy chọn
    User->>Claude: Chọn GitHub MCP
    Claude->>Config: Cập nhật cấu hình
    Config->>Claude: Kích hoạt kết nối
    Claude->>Service: Kiểm tra kết nối
    Service-->>Claude: Xác thực thành công
    Claude->>User: ✅ MCP đã kết nối!
```

## Tìm kiếm Tool MCP

Khi mô tả tool MCP vượt quá 10% cửa sổ ngữ cảnh, Claude Code tự động bật tìm kiếm tool để chọn đúng công cụ mà không làm quá tải ngữ cảnh.

| Cài đặt | Giá trị | Mô tả |
|---------|---------|-------|
| `ENABLE_TOOL_SEARCH` | `auto` (mặc định) | Tự động bật khi mô tả tool vượt quá 10% ngữ cảnh |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | Tự động bật tại ngưỡng `N` tools tùy chỉnh |
| `ENABLE_TOOL_SEARCH` | `true` | Luôn bật bất kể số lượng tool |
| `ENABLE_TOOL_SEARCH` | `false` | Tắt; tất cả mô tả tool được gửi đầy đủ |

> **Lưu ý:** Tìm kiếm tool yêu cầu Sonnet 4 trở lên, hoặc Opus 4 trở lên. Các model Haiku không hỗ trợ tìm kiếm tool.

## Cập nhật Tool động

Claude Code hỗ trợ thông báo `list_changed` của MCP. Khi MCP server tự động thêm, xóa hoặc sửa đổi các tool có sẵn, Claude Code nhận cập nhật và điều chỉnh danh sách tool của mình tự động — không cần kết nối lại hoặc khởi động lại.

## MCP Elicitation (Yêu cầu thông tin)

Các MCP server có thể yêu cầu đầu vào có cấu trúc từ người dùng qua các hộp thoại tương tác (v2.1.49+). Điều này cho phép MCP server yêu cầu thông tin bổ sung trong quá trình làm việc — ví dụ: nhắc xác nhận, chọn từ danh sách tùy chọn, hoặc điền các trường bắt buộc — thêm tính tương tác vào các tương tác MCP server.

## Giới hạn mô tả và hướng dẫn Tool

Từ v2.1.84, Claude Code áp đặt giới hạn **2 KB** cho mô tả tool và hướng dẫn mỗi MCP server. Điều này ngăn các server riêng lẻ tiêu thụ quá nhiều ngữ cảnh với định nghĩa tool quá dài, giảm phình ngữ cảnh và giữ cho các tương tác hiệu quả.

## MCP Prompts dưới dạng Slash Commands

Các MCP server có thể expose prompts xuất hiện dưới dạng slash commands trong Claude Code. Prompts có thể truy cập bằng quy ước đặt tên:

```
/mcp__<server>__<prompt>
```

Ví dụ, nếu server tên `github` expose một prompt tên `review`, bạn có thể gọi nó bằng `/mcp__github__review`.

## Loại trùng lặp Server

Khi cùng một MCP server được định nghĩa ở nhiều phạm vi (local, project, user), cấu hình local được ưu tiên. Điều này cho phép bạn ghi đè cài đặt MCP cấp project hoặc cấp user bằng tùy chỉnh cục bộ mà không xung đột.

## Tài nguyên MCP qua @ Mentions

Bạn có thể tham chiếu các tài nguyên MCP trực tiếp trong prompts của mình bằng cú pháp `@`:

```
@tên-server:protocol://resource/path
```

Ví dụ, để tham chiếu tài nguyên database cụ thể:

```
@database:postgres://mydb/users
```

Điều này cho phép Claude lấy và bao gồm nội dung tài nguyên MCP nội tuyến như một phần của ngữ cảnh hội thoại.

## Các phạm vi MCP

Cấu hình MCP có thể lưu trữ ở các phạm vi khác nhau với mức độ chia sẻ khác nhau:

| Phạm vi | Vị trí | Mô tả | Chia sẻ với | Cần phê duyệt |
|---------|--------|-------|------------|--------------|
| **Local** (mặc định) | `~/.claude.json` (theo đường dẫn dự án) | Riêng tư cho người dùng hiện tại, chỉ dự án hiện tại (trước gọi là `project`) | Chỉ bạn | Không |
| **Project** | `.mcp.json` | Được commit vào git repository | Thành viên nhóm | Có (lần đầu dùng) |
| **User** | `~/.claude.json` | Có sẵn qua tất cả dự án (trước gọi là `global`) | Chỉ bạn | Không |

### Dùng phạm vi Project

Lưu cấu hình MCP theo dự án trong `.mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.github.com/mcp"
    }
  }
}
```

Thành viên nhóm sẽ thấy prompt phê duyệt khi lần đầu dùng project MCPs.

## Quản lý cấu hình MCP

### Thêm MCP Servers

```bash
# Thêm server HTTP-based
claude mcp add --transport http github https://api.github.com/mcp

# Thêm server stdio cục bộ
claude mcp add --transport stdio database -- npx @company/db-server

# Liệt kê tất cả MCP server
claude mcp list

# Xem chi tiết server cụ thể
claude mcp get github

# Xóa MCP server
claude mcp remove github

# Đặt lại lựa chọn phê duyệt theo dự án
claude mcp reset-project-choices

# Import từ Claude Desktop
claude mcp add-from-claude-desktop
```

## Bảng các MCP Server có sẵn

| MCP Server | Mục đích | Tools phổ biến | Xác thực | Thời gian thực |
|-----------|---------|---------------|---------|--------------|
| **Filesystem** | Thao tác file | read, write, delete | Quyền OS | ✅ Có |
| **GitHub** | Quản lý repository | list_prs, create_issue, push | OAuth | ✅ Có |
| **Slack** | Giao tiếp nhóm | send_message, list_channels | Token | ✅ Có |
| **Database** | Truy vấn SQL | query, insert, update | Credentials | ✅ Có |
| **Google Docs** | Truy cập tài liệu | read, write, share | OAuth | ✅ Có |
| **Asana** | Quản lý dự án | create_task, update_status | API Key | ✅ Có |
| **Stripe** | Dữ liệu thanh toán | list_charges, create_invoice | API Key | ✅ Có |
| **Memory** | Bộ nhớ liên tục | store, retrieve, delete | Cục bộ | ❌ Không |

## Ví dụ thực tế

### Ví dụ 1: Cấu hình GitHub MCP

**File:** `.mcp.json` (thư mục gốc dự án)

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Các GitHub MCP Tools có sẵn:**

#### Quản lý Pull Request
- `list_prs` - Liệt kê tất cả PRs trong repository
- `get_pr` - Lấy chi tiết PR bao gồm diff
- `create_pr` - Tạo PR mới
- `update_pr` - Cập nhật mô tả/tiêu đề PR
- `merge_pr` - Merge PR vào nhánh main
- `review_pr` - Thêm comment review

**Ví dụ yêu cầu:**
```
/mcp__github__get_pr 456

# Trả về:
Title: Thêm hỗ trợ dark mode
Author: @alice
Description: Triển khai dark theme dùng CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### Quản lý Issue
- `list_issues` - Liệt kê tất cả issues
- `get_issue` - Lấy chi tiết issue
- `create_issue` - Tạo issue mới
- `close_issue` - Đóng issue
- `add_comment` - Thêm comment vào issue

#### Thông tin Repository
- `get_repo_info` - Chi tiết repository
- `list_files` - Cấu trúc cây file
- `get_file_content` - Đọc nội dung file
- `search_code` - Tìm kiếm trong codebase

#### Thao tác Commit
- `list_commits` - Lịch sử commit
- `get_commit` - Chi tiết commit cụ thể
- `create_commit` - Tạo commit mới

**Thiết lập**:
```bash
export GITHUB_TOKEN="your_github_token"
# Hoặc dùng CLI để thêm trực tiếp:
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### Mở rộng biến môi trường trong cấu hình

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

Biến được mở rộng lúc chạy:
- `${VAR}` - Dùng biến môi trường, lỗi nếu chưa đặt
- `${VAR:-default}` - Dùng biến môi trường, dùng giá trị mặc định nếu chưa đặt

### Ví dụ 2: Thiết lập Database MCP

**Cấu hình:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-database"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

**Ví dụ sử dụng:**

```markdown
Người dùng: Lấy tất cả users có hơn 10 đơn hàng

Claude: Tôi sẽ truy vấn database để tìm thông tin đó.

# Dùng MCP database tool:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Kết quả:
- Alice: 15 đơn hàng
- Bob: 12 đơn hàng
- Charlie: 11 đơn hàng
```

**Thiết lập**:
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# Hoặc dùng CLI để thêm trực tiếp:
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

### Ví dụ 3: Quy trình đa MCP

**Tình huống: Tạo báo cáo hàng ngày**

```markdown
# Quy trình báo cáo hàng ngày dùng nhiều MCPs

## Thiết lập
1. GitHub MCP - lấy chỉ số PR
2. Database MCP - truy vấn dữ liệu bán hàng
3. Slack MCP - đăng báo cáo
4. Filesystem MCP - lưu báo cáo

## Quy trình

### Bước 1: Lấy dữ liệu GitHub
/mcp__github__list_prs completed:true last:7days

Kết quả:
- Tổng PRs: 42
- Thời gian merge trung bình: 2.3 giờ
- Thời gian review: 1.1 giờ

### Bước 2: Truy vấn Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Kết quả:
- Doanh số: 247
- Doanh thu: $12,450

### Bước 3: Tạo báo cáo
Kết hợp dữ liệu thành báo cáo HTML

### Bước 4: Lưu vào Filesystem
Ghi report.html vào /reports/

### Bước 5: Đăng lên Slack
Gửi tóm tắt vào kênh #daily-reports

Kết quả cuối:
✅ Báo cáo đã tạo và đăng
📊 47 PRs được merge tuần này
💰 $12,450 doanh thu ngày
```

**Thiết lập**:
```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
# Thêm mỗi MCP server qua CLI hoặc cấu hình trong .mcp.json
```

### Ví dụ 4: Filesystem MCP Operations

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

| Thao tác | Lệnh | Mục đích |
|----------|------|---------|
| Liệt kê file | `ls ~/projects` | Hiển thị nội dung thư mục |
| Đọc file | `cat src/main.ts` | Đọc nội dung file |
| Ghi file | `create docs/api.md` | Tạo file mới |
| Sửa file | `edit src/app.ts` | Chỉnh sửa file |
| Tìm kiếm | `grep "async function"` | Tìm trong file |
| Xóa | `rm old-file.js` | Xóa file |

**Thiết lập**:
```bash
# Dùng CLI để thêm trực tiếp:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## Ma trận quyết định MCP vs Memory

```mermaid
graph TD
    A["Cần dữ liệu bên ngoài?"]
    A -->|Không| B["Dùng Memory"]
    A -->|Có| C["Dữ liệu có thay đổi thường xuyên không?"]
    C -->|Không/Hiếm| B
    C -->|Có/Thường| D["Dùng MCP"]

    B -->|Lưu trữ| E["Tùy chọn<br/>Ngữ cảnh<br/>Lịch sử"]
    D -->|Truy cập| F["APIs trực tiếp<br/>Database<br/>Dịch vụ"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## Pattern Yêu cầu/Phản hồi

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Yêu cầu: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Thực thi truy vấn
    DB-->>MCP: Tập kết quả
    MCP-->>App: Trả về dữ liệu đã phân tích
    App->>App: Xử lý kết quả
    App->>App: Tiếp tục tác vụ

    Note over MCP,DB: Truy cập thời gian thực<br/>Không cache
```

## Biến môi trường

Lưu thông tin xác thực nhạy cảm trong biến môi trường:

```bash
# ~/.bashrc hoặc ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

Sau đó tham chiếu trong cấu hình MCP:

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Claude làm MCP Server (`claude mcp serve`)

Bản thân Claude Code có thể hoạt động như một MCP server cho các ứng dụng khác. Điều này cho phép các công cụ bên ngoài, editor và hệ thống tự động tận dụng khả năng của Claude qua giao thức MCP tiêu chuẩn.

```bash
# Khởi động Claude Code làm MCP server trên stdio
claude mcp serve
```

Các ứng dụng khác có thể kết nối với server này như với bất kỳ MCP server dựa trên stdio nào. Ví dụ, để thêm Claude Code làm MCP server trong một instance Claude Code khác:

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

Hữu ích khi xây dựng quy trình đa agent trong đó một instance Claude điều phối instance khác.

## Cấu hình MCP Quản lý (Enterprise)

Cho các triển khai doanh nghiệp, quản trị viên IT có thể áp đặt chính sách MCP server qua file cấu hình `managed-mcp.json`. File này cung cấp quyền kiểm soát duy nhất về các MCP server nào được phép hoặc bị chặn trên toàn tổ chức.

**Vị trí:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**Tính năng:**
- `allowedMcpServers` -- danh sách trắng các server được phép
- `deniedMcpServers` -- danh sách đen các server bị cấm
- Hỗ trợ khớp theo tên server, lệnh và URL patterns
- Chính sách MCP toàn tổ chức được áp dụng trước cấu hình người dùng
- Ngăn kết nối server trái phép

**Ví dụ cấu hình:**

```json
{
  "allowedMcpServers": [
    {
      "serverName": "github",
      "serverUrl": "https://api.github.com/mcp"
    },
    {
      "serverName": "company-internal",
      "serverCommand": "company-mcp-server"
    }
  ],
  "deniedMcpServers": [
    {
      "serverName": "untrusted-*"
    },
    {
      "serverUrl": "http://*"
    }
  ]
}
```

> **Lưu ý:** Khi cả `allowedMcpServers` và `deniedMcpServers` khớp một server, quy tắc deny được ưu tiên.

## MCP Servers do Plugin cung cấp

Plugins có thể đi kèm các MCP server riêng, tự động có sẵn khi plugin được cài đặt. MCP servers do plugin cung cấp có thể được định nghĩa theo hai cách:

1. **`.mcp.json` độc lập** -- Đặt file `.mcp.json` trong thư mục gốc plugin
2. **Nội tuyến trong `plugin.json`** -- Định nghĩa MCP servers trực tiếp trong manifest plugin

Dùng biến `${CLAUDE_PLUGIN_ROOT}` để tham chiếu đường dẫn tương đối với thư mục cài đặt plugin:

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

## MCP theo phạm vi Subagent

Các MCP server có thể được định nghĩa nội tuyến trong frontmatter agent bằng khóa `mcpServers:`, giới hạn phạm vi cho subagent cụ thể thay vì toàn bộ dự án. Hữu ích khi một agent cần truy cập MCP server cụ thể mà các agent khác trong quy trình không cần.

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

Bạn là agent có quyền truy cập my-tool cho các thao tác chuyên biệt.
```

Các MCP server theo phạm vi subagent chỉ có sẵn trong ngữ cảnh thực thi của agent đó và không được chia sẻ với agent cha hoặc agent anh em.

## Giới hạn đầu ra MCP

Claude Code áp đặt giới hạn đầu ra tool MCP để ngăn tràn ngữ cảnh:

| Giới hạn | Ngưỡng | Hành vi |
|---------|--------|---------|
| **Cảnh báo** | 10.000 tokens | Hiển thị cảnh báo rằng đầu ra lớn |
| **Tối đa mặc định** | 25.000 tokens | Đầu ra bị cắt ngắn sau giới hạn này |
| **Lưu vào đĩa** | 50.000 ký tự | Kết quả tool vượt quá 50K ký tự được lưu xuống đĩa |

Giới hạn đầu ra tối đa có thể cấu hình qua biến môi trường `MAX_MCP_OUTPUT_TOKENS`:

```bash
# Tăng đầu ra tối đa lên 50.000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## Giải quyết phình ngữ cảnh bằng thực thi code

Khi MCP được áp dụng rộng rãi, kết nối hàng chục server với hàng trăm hoặc hàng nghìn tools tạo ra thách thức lớn: **phình ngữ cảnh** (context bloat). Đây là vấn đề lớn nhất với MCP ở quy mô, và nhóm kỹ thuật Anthropic đề xuất giải pháp tinh tế — dùng thực thi code thay vì gọi tool trực tiếp.

> **Nguồn**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Blog Kỹ thuật Anthropic

### Vấn đề: Hai nguồn lãng phí token

**1. Định nghĩa tool làm quá tải cửa sổ ngữ cảnh**

Hầu hết MCP client tải tất cả định nghĩa tool ngay từ đầu. Khi kết nối với hàng nghìn tool, model phải xử lý hàng trăm nghìn token trước khi đọc yêu cầu người dùng.

**2. Kết quả trung gian tiêu thụ thêm token**

Mọi kết quả tool trung gian đều đi qua ngữ cảnh của model. Hãy xem xét việc chuyển một transcript cuộc họp từ Google Drive sang Salesforce — transcript đầy đủ chạy qua ngữ cảnh **hai lần**: một lần khi đọc, và một lần nữa khi ghi vào đích. Một transcript cuộc họp 2 giờ có thể tốn hơn 50.000 token thêm.

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Toàn bộ transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(gửi lại toàn bộ transcript)"| B
    B -->|"Xác nhận"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### Giải pháp: MCP Tools dưới dạng Code APIs

Thay vì đưa định nghĩa tool và kết quả qua cửa sổ ngữ cảnh, agent **viết code** gọi MCP tools như APIs. Code chạy trong môi trường thực thi được sandbox, và chỉ kết quả cuối cùng trả về model.

```mermaid
graph LR
    A["Model"] -->|"Viết code"| B["Môi trường<br/>thực thi code"]
    B -->|"Gọi tools trực tiếp"| C["MCP Servers"]
    C -->|"Dữ liệu ở trong<br/>môi trường thực thi"| B
    B -->|"Chỉ kết quả cuối<br/>(tối thiểu tokens)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

#### Cách hoạt động

Các MCP tool được trình bày như cây file của các hàm có kiểu:

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

Mỗi file tool chứa một wrapper có kiểu:

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

Agent sau đó viết code để điều phối các tool:

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// Dữ liệu chạy trực tiếp giữa các tool — không qua model
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**Kết quả: Sử dụng token giảm từ ~150.000 xuống ~2.000 — giảm 98,7%.**

### Lợi ích chính

| Lợi ích | Mô tả |
|---------|-------|
| **Tiết lộ dần dần** | Agent duyệt filesystem để chỉ tải định nghĩa tool cần thiết, thay vì tất cả tools ngay từ đầu |
| **Kết quả tiết kiệm ngữ cảnh** | Dữ liệu được lọc/biến đổi trong môi trường thực thi trước khi trả về model |
| **Luồng điều khiển mạnh mẽ** | Vòng lặp, điều kiện và xử lý lỗi chạy trong code mà không cần round-trip qua model |
| **Bảo vệ quyền riêng tư** | Dữ liệu trung gian (PII, hồ sơ nhạy cảm) ở trong môi trường thực thi; không bao giờ vào ngữ cảnh model |
| **Lưu trữ trạng thái** | Agent có thể lưu kết quả trung gian vào file và xây dựng các hàm skill tái sử dụng |

#### Ví dụ: Lọc tập dữ liệu lớn

```typescript
// Không có code execution — tất cả 10.000 hàng qua ngữ cảnh
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> trả về 10.000 hàng trong ngữ cảnh

// Với code execution — lọc trong môi trường thực thi
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Tìm thấy ${pendingOrders.length} đơn hàng pending`);
console.log(pendingOrders.slice(0, 5)); // Chỉ 5 hàng đến model
```

#### Ví dụ: Vòng lặp không cần round-trip

```typescript
// Poll thông báo deployment — chạy hoàn toàn trong code
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
console.log('Đã nhận thông báo deployment');
```

### Đánh đổi cần xem xét

Thực thi code tạo ra sự phức tạp riêng. Chạy code do agent tạo ra yêu cầu:

- **Môi trường thực thi sandbox an toàn** với giới hạn tài nguyên phù hợp
- **Giám sát và ghi log** code được thực thi
- **Chi phí hạ tầng** cao hơn so với gọi tool trực tiếp

Lợi ích — giảm chi phí token, độ trễ thấp hơn, kết hợp tool tốt hơn — cần được đánh giá so với chi phí triển khai. Với các agent chỉ có vài MCP server, gọi tool trực tiếp có thể đơn giản hơn. Với các agent ở quy mô (hàng chục server, hàng trăm tool), thực thi code là cải thiện đáng kể.

### MCPorter: Runtime cho MCP Tool Composition

[MCPorter](https://github.com/steipete/mcporter) là runtime TypeScript và bộ CLI giúp gọi MCP server thực tế mà không cần boilerplate — và giảm phình ngữ cảnh qua việc expose tool có chọn lọc và các wrapper có kiểu.

**Vấn đề nó giải quyết:** Thay vì tải tất cả định nghĩa tool từ tất cả MCP server ngay từ đầu, MCPorter cho phép bạn khám phá, kiểm tra và gọi các tool cụ thể theo nhu cầu — giữ cho ngữ cảnh gọn gàng.

**Tính năng chính:**

| Tính năng | Mô tả |
|-----------|-------|
| **Khám phá không cần cấu hình** | Tự động khám phá MCP server từ Cursor, Claude, Codex hoặc cấu hình cục bộ |
| **Tool clients có kiểu** | `mcporter emit-ts` tạo interfaces `.d.ts` và wrappers sẵn chạy |
| **API có thể kết hợp** | `createServerProxy()` expose tools như các phương thức camelCase với helpers `.text()`, `.json()`, `.markdown()` |
| **Tạo CLI** | `mcporter generate-cli` chuyển đổi bất kỳ MCP server nào thành CLI độc lập với lọc `--include-tools` / `--exclude-tools` |
| **Ẩn tham số** | Tham số tùy chọn bị ẩn mặc định, giảm độ dài schema |

**Cài đặt:**

```bash
npx mcporter list          # Không cần cài — khám phá server ngay
pnpm add mcporter          # Thêm vào dự án
brew install steipete/tap/mcporter  # macOS qua Homebrew
```

**Ví dụ — kết hợp tools trong TypeScript:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Dữ liệu chạy giữa các tool mà không đi qua ngữ cảnh model
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**Ví dụ — gọi tool qua CLI:**

```bash
# Gọi tool cụ thể trực tiếp
npx mcporter call linear.create_comment issueId:ENG-123 body:'Trông ổn!'

# Liệt kê các server và tool có sẵn
npx mcporter list
```

MCPorter bổ trợ cho cách tiếp cận thực thi code được mô tả ở trên bằng cách cung cấp runtime infrastructure để gọi MCP tools như typed APIs — giúp dễ dàng giữ dữ liệu trung gian ra khỏi ngữ cảnh model.

## Thực hành tốt nhất

### Cân nhắc bảo mật

#### Nên làm ✅
- Dùng biến môi trường cho tất cả thông tin xác thực
- Xoay vòng tokens và API keys thường xuyên (khuyến nghị hàng tháng)
- Dùng tokens chỉ đọc khi có thể
- Giới hạn phạm vi truy cập MCP server ở mức tối thiểu cần thiết
- Giám sát sử dụng và log truy cập MCP server
- Dùng OAuth cho dịch vụ bên ngoài khi có thể
- Triển khai rate limiting cho MCP requests
- Kiểm tra kết nối MCP trước khi dùng production
- Ghi lại tất cả kết nối MCP đang hoạt động
- Cập nhật các gói MCP server

#### Không nên làm ❌
- Đừng hardcode thông tin xác thực trong file cấu hình
- Đừng commit tokens hoặc secrets lên git
- Đừng chia sẻ tokens trong chat nhóm hoặc email
- Đừng dùng tokens cá nhân cho dự án nhóm
- Đừng cấp quyền không cần thiết
- Đừng bỏ qua lỗi xác thực
- Đừng expose MCP endpoints công khai
- Đừng chạy MCP server với quyền root/admin
- Đừng cache dữ liệu nhạy cảm trong logs
- Đừng tắt cơ chế xác thực

### Thực hành tốt nhất về cấu hình

1. **Kiểm soát phiên bản**: Giữ `.mcp.json` trong git nhưng dùng biến môi trường cho secrets
2. **Quyền tối thiểu**: Cấp quyền tối thiểu cần thiết cho mỗi MCP server
3. **Cô lập**: Chạy các MCP server khác nhau trong tiến trình riêng khi có thể
4. **Giám sát**: Ghi log tất cả MCP requests và lỗi để kiểm tra
5. **Kiểm tra**: Kiểm tra tất cả cấu hình MCP trước khi deploy production

### Mẹo hiệu năng

- Cache dữ liệu truy cập thường xuyên ở tầng ứng dụng
- Dùng MCP queries cụ thể để giảm truyền dữ liệu
- Giám sát thời gian phản hồi của các thao tác MCP
- Xem xét rate limiting cho các API bên ngoài
- Dùng batching khi thực hiện nhiều thao tác

## Hướng dẫn cài đặt

### Yêu cầu tiên quyết
- Node.js và npm đã cài đặt
- Claude Code CLI đã cài đặt
- API tokens/credentials cho các dịch vụ bên ngoài

### Thiết lập từng bước

1. **Thêm MCP server đầu tiên** qua CLI (ví dụ: GitHub):
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

Hoặc tạo file `.mcp.json` trong thư mục gốc dự án:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

2. **Đặt biến môi trường:**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3. **Kiểm tra kết nối:**
```bash
claude /mcp
```

4. **Dùng MCP tools:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Tiêu đề" "Mô tả"
```

### Cài đặt cho các dịch vụ cụ thể

**GitHub MCP:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**Database MCP:**
```bash
npm install -g @modelcontextprotocol/server-database
```

**Filesystem MCP:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP:**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## Xử lý sự cố

### MCP Server không tìm thấy
```bash
# Kiểm tra MCP server đã cài đặt chưa
npm list -g @modelcontextprotocol/server-github

# Cài đặt nếu thiếu
npm install -g @modelcontextprotocol/server-github
```

### Xác thực thất bại
```bash
# Kiểm tra biến môi trường đã đặt chưa
echo $GITHUB_TOKEN

# Re-export nếu cần
export GITHUB_TOKEN="your_token"

# Kiểm tra token có đúng quyền không
# Xem GitHub token scopes tại: https://github.com/settings/tokens
```

### Kết nối timeout
- Kiểm tra kết nối mạng: `ping api.github.com`
- Xác minh API endpoint có thể truy cập
- Kiểm tra rate limits trên API
- Thử tăng timeout trong cấu hình
- Kiểm tra firewall hoặc proxy

### MCP Server bị crash
- Kiểm tra log MCP server: `~/.claude/logs/`
- Xác minh tất cả biến môi trường đã đặt
- Đảm bảo quyền file đúng
- Thử cài lại gói MCP server
- Kiểm tra các tiến trình xung đột trên cùng port

## Khái niệm liên quan

### Memory vs MCP
- **Memory**: Lưu trữ dữ liệu liên tục, không thay đổi (tùy chọn, ngữ cảnh, lịch sử)
- **MCP**: Truy cập dữ liệu trực tiếp, thay đổi (APIs, databases, dịch vụ thời gian thực)

### Khi nào dùng cái nào
- **Dùng Memory** cho: Tùy chọn người dùng, lịch sử hội thoại, ngữ cảnh đã học
- **Dùng MCP** cho: GitHub issues hiện tại, truy vấn database trực tiếp, dữ liệu thời gian thực

### Tích hợp với các tính năng Claude khác
- Kết hợp MCP với Memory để có ngữ cảnh phong phú
- Dùng MCP tools trong prompts để lý luận tốt hơn
- Tận dụng nhiều MCPs cho các quy trình phức tạp

## Tài nguyên bổ sung

- [Tài liệu MCP chính thức](https://code.claude.com/docs/en/mcp)
- [Đặc tả giao thức MCP](https://modelcontextprotocol.io/specification)
- [GitHub Repository MCP](https://github.com/modelcontextprotocol/servers)
- [Các MCP Server có sẵn](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — Runtime TypeScript & CLI để gọi MCP server không cần boilerplate
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Blog kỹ thuật Anthropic về giải quyết phình ngữ cảnh
- [Tài liệu tham chiếu Claude Code CLI](https://code.claude.com/docs/en/cli-reference)
- [Tài liệu Claude API](https://docs.anthropic.com)
