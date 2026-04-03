<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

Thư mục này chứa tài liệu toàn diện và ví dụ cho cấu hình và sử dụng MCP server với Claude Code.

## Tổng Quan / Overview

MCP (Model Context Protocol) là một cách chuẩn hóa để Claude truy cập các công cụ bên ngoài, APIs, và nguồn dữ liệu thời gian thực. Khác với Memory, MCP cung cấp truy cập trực tiếp đến dữ liệu đang thay đổi.

Đặc điểm chính:
- Truy cập thời gian thực đến các dịch vụ bên ngoài
- Đồng bộ hóa dữ liệu trực tiếp
- Kiến trúc có thể mở rộng
- Xác thực bảo mật
- Tương tác dựa trên công cụ

## Kiến Trúc MCP / MCP Architecture

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

## Hệ Sinh Thái MCP / MCP Ecosystem

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

## Phương Thức Cài Đặt MCP / MCP Installation Methods

Claude Code hỗ trợ nhiều giao thức vận chuyển cho kết nối MCP server:

### Giao Thức HTTP (Khuyến Nghị) / HTTP Transport (Recommended)

```bash
# Kết nối HTTP cơ bản
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP với header xác thực
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Giao Thức Stdio (Cục Bộ) / Stdio Transport (Local)

Đối với MCP server chạy cục bộ:

```bash
# Local Node.js server
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# Với biến môi trường
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### Giao Thức SSE (Đã Lỗi Thời) / SSE Transport (Deprecated)

Giao thức Server-Sent Events đã lỗi thời để ủng hộ `http` nhưng vẫn được hỗ trợ:

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### Giao Thức WebSocket / WebSocket Transport

Giao thức WebSocket cho các kết nối hai chiều liên tục:

```bash
claude mcp add --transport ws realtime-server wss://example.com/mcp
```

### Lưu Ý Cụ Thể Cho Windows / Windows-Specific Note

Trên Windows native (không phải WSL), sử dụng `cmd /c` cho các lệnh npx:

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### Xác Thực OAuth 2.0 / OAuth 2.0 Authentication

Claude Code hỗ trợ OAuth 2.0 cho các MCP server yêu cầu. Khi kết nối đến một OAuth-enabled server, Claude Code xử lý toàn bộ quy trình xác thực:

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
| **OAuth Tương Tác** | Sử dụng `/mcp` để kích hoạt flow OAuth dựa trên trình duyệt |
| **OAuth Clients Cấu Hình Trước** | OAuth clients tích hợp sẵn cho các dịch vụ phổ biến như Notion, Stripe, v.v. (v2.1.30+) |
| **Credentials Cấu Hình Trước** | Các cờ `--client-id`, `--client-secret`, `--callback-port` cho thiết lập tự động |
| **Lưu Trữ Token** | Tokens được lưu trữ an toàn trong system keychain của bạn |
| **Xác Thực Bước Nhảy** | Hỗ trợ xác thực step-up cho các thao tác đặc quyền |
| **Caching Discovery** | Metadata discovery OAuth được cache để kết nối lại nhanh hơn |
| **Ghi Đè Metadata** | `oauth.authServerMetadataUrl` trong `.mcp.json` để ghi đè discovery metadata OAuth mặc định |

#### Ghi Đè OAuth Metadata Discovery / Overriding OAuth Metadata Discovery

Nếu MCP server của bạn trả về lỗi trên endpoint metadata OAuth chuẩn (`/.well-known/oauth-authorization-server`) nhưng lộct một endpoint OIDC hoạt động, bạn có thể bảo Claude Code fetch OAuth metadata từ một URL cụ thể. Đặt `authServerMetadataUrl` trong object `oauth` của cấu hình server:

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

### MCP Connectors Claude.ai / Claude.ai MCP Connectors

Các MCP server được cấu hình trong tài khoản Claude.ai của bạn tự động có sẵn trong Claude Code. Điều này có nghĩa là bất kỳ kết nối MCP nào bạn thiết lập qua giao diện web Claude.ai sẽ có thể truy cập mà không cần cấu hình thêm.

MCP connectors Claude.ai cũng có sẵn trong chế độ `--print` (v2.1.83+), cho phép sử dụng không tương tác và theo script.

Để tắt MCP servers Claude.ai trong Claude Code, đặt biến môi trường `ENABLE_CLAUDEAI_MCP_SERVERS` thành `false`:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **Lưu Ý:** Tính năng này chỉ có sẵn cho người dùng đã đăng nhập bằng tài khoản Claude.ai.

## Quy Trình Thiết Lập MCP / MCP Setup Process

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

## Tìm Kiếm Công Cụ MCP / MCP Tool Search

Khi mô tả công cụ MCP vượt quá 10% cửa sổ ngữ cảnh, Claude Code tự động kích hoạt tìm kiếm công cụ để chọn công cụ phù hợp một cách hiệu quả mà không làm bội ngữ cảnh mô hình.

| Cài Đặt | Giá Trị | Mô Tả |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | `auto` (mặc định) | Tự động kích hoạt khi mô tả công cụ vượt quá 10% ngữ cảnh |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | Tự động kích hoạt tại ngưỡng tùy chỉnh của `N` công cụ |
| `ENABLE_TOOL_SEARCH` | `true` | Luôn được kích hoạt bất kể số lượng công cụ |
| `ENABLE_TOOL_SEARCH` | `false` | Đã tắt; tất cả mô tả công cụ được gửi đầy đủ |

> **Lưu Ý:** Tìm kiếm công cụ yêu cầu Sonnet 4 hoặc mới hơn, hoặc Opus 4 hoặc mới hơn. Các mô hình Haiku không được hỗ trợ cho tìm kiếm công cụ.

## Cập Nhật Công Cụ Động / Dynamic Tool Updates

Claude Code hỗ trợ các thông báo `list_changed` của MCP. Khi một MCP server động thêm, xóa, hoặc sửa đổi các công cụ có sẵn của nó, Claude Code nhận cập nhật và điều chỉnh danh sách công cụ tự động -- không cần kết nối lại hoặc khởi động lại.

## MCP Elicitation

Các MCP server có thể yêu cầu đầu vào có cấu trúc từ người dùng qua các hộp thoại tương tác (v2.1.49+). Điều này cho phép một MCP server yêu cầu thêm thông tin giữa chừng workflow -- ví dụ, yêu cầu xác nhận, chọn từ danh sách tùy chọn, hoặc điền vào các trường bắt buộc -- thêm tính tương tác vào các tương tác MCP server.

## Giới Hạn Mô Tả Và Hướng Dẫn Công Cụ / Tool Description and Instruction Cap

Kể từ v2.1.84, Claude Code thực thi **giới hạn 2 KB** trên mô tả và hướng dẫn công cụ cho mỗi MCP server. Điều này ngăn các server riêng lẻ tiêu thụ quá nhiều ngữ cảnh với các định nghĩa công cụ quá dài dòng, giảm bloat ngữ cảnh và giữ các tương tác hiệu quả.

## MCP Prompts Như Lệnh Slash / MCP Prompts as Slash Commands

Các MCP server có thể lộ các prompts xuất hiện như các lệnh slash trong Claude Code. Prompts có thể truy cập được sử dụng quy ước đặt tên:

```
/mcp__<server>__<prompt>
```

Ví dụ, nếu một server tên là `github` lộ một prompt gọi là `review`, bạn có thể gọi nó là `/mcp__github__review`.

## Khử Trùng Server / Server Deduplication

Khi cùng một MCP server được định nghĩa tại nhiều phạm vi (local, project, user), cấu hình local được ưu tiên. Điều này cho phép bạn ghi đè cài đặt MCP cấp project hoặc user với tùy biến local mà không có xung đột.

## Tài Nguyên MCP Qua @ Mentions / MCP Resources via @ Mentions

Bạn có thể tham khảo tài nguyên MCP trực tiếp trong prompts của bạn sử dụng cú pháp mention `@`:

```
@server-name:protocol://resource/path
```

Ví dụ, để tham khảo một tài nguyên database cụ thể:

```
@database:postgres://mydb/users
```

Điều này cho phép Claude fetch và bao gồm nội dung tài nguyên MCP inline như một phần của ngữ cảnh hội thoại.

## Các Phạm Vi MCP / MCP Scopes

Cấu hình MCP có thể được lưu trữ tại các phạm vi khác nhau với các mức độ chia sẻ khác nhau:

| Phạm Vi | Vị Trí | Mô Tả | Chia Sẻ Với | Yêu Cầu Chấp Thuận |
|-------|----------|-------------|-------------|------------------|
| **Local** (mặc định) | `~/.claude.json` (dưới đường dẫn project) | Riêng tư cho người dùng hiện tại, project hiện tại chỉ (được gọi là `project` trong các phiên bản cũ hơn) | Chỉ bạn | Không |
| **Project** | `.mcp.json` | Được check vào git repository | Các thành viên nhóm | Có (lần sử dụng đầu) |
| **User** | `~/.claude.json` | Có sẵn trên tất cả các projects (được gọi là `global` trong các phiên bản cũ hơn) | Chỉ bạn | Không |

### Sử Dụng Phạm Vi Project / Using Project Scope

Lưu trữ cấu hình MCP cụ thể project trong `.mcp.json`:

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

Các thành viên nhóm sẽ thấy prompt chấp thuận khi sử dụng project MCPs lần đầu.

## Quản Lý Cấu Hình MCP / MCP Configuration Management

### Thêm MCP Servers / Adding MCP Servers

```bash
# Thêm server dựa trên HTTP
claude mcp add --transport http github https://api.github.com/mcp

# Thêm server stdio cục bộ
claude mcp add --transport stdio database -- npx @company/db-server

# Liệt kê tất cả MCP servers
claude mcp list

# Lấy chi tiết trên server cụ thể
claude mcp get github

# Xóa một MCP server
claude mcp remove github

# Reset các lựa chọn chấp thuận cụ thể project
claude mcp reset-project-choices

# Import từ Claude Desktop
claude mcp add-from-claude-desktop
```

## Bảng MCP Servers Có Sẵn / Available MCP Servers Table

| MCP Server | Mục Đích | Công Thụng Thường Gặp | Auth | Thời Gian Thực |
|------------|---------|--------------|------|-----------|
| **Filesystem** | Thao tác file | read, write, delete | Quyền OS | ✅ Có |
| **GitHub** | Quản lý repository | list_prs, create_issue, push | OAuth | ✅ Có |
| **Slack** | Giao tiếp nhóm | send_message, list_channels | Token | ✅ Có |
| **Database** | Truy vấn SQL | query, insert, update | Credentials | ✅ Có |
| **Google Docs** | Truy cập tài liệu | read, write, share | OAuth | ✅ Có |
| **Asana** | Quản lý dự án | create_task, update_status | API Key | ✅ Có |
| **Stripe** | Dữ liệu thanh toán | list_charges, create_invoice | API Key | ✅ Có |
| **Memory** | Bộ nhớ liên tục | store, retrieve, delete | Local | ❌ Không |

## Ví Dụ Thực Tiễn / Practical Examples

### Ví Dụ 1: Cấu Hình GitHub MCP / Example 1: GitHub MCP Configuration

**File:** `.mcp.json` (project root)

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

**GitHub MCP Tools Có Sẵn:**

#### Quản Lý Pull Request / Pull Request Management
- `list_prs` - Liệt kê tất cả PRs trong repository
- `get_pr` - Lấy chi tiết PR bao gồm diff
- `create_pr` - Tạo PR mới
- `update_pr` - Cập nhật mô tả/tiêu đề PR
- `merge_pr` - Gộp PR vào nhánh chính
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

#### Quản Lý Issue / Issue Management
- `list_issues` - Liệt kê tất cả issues
- `get_issue` - Lấy chi tiết issue
- `create_issue` - Tạo issue mới
- `close_issue` - Đóng issue
- `add_comment` - Thêm bình luận vào issue

#### Thông Tin Repository / Repository Information
- `get_repo_info` - Chi tiết repository
- `list_files` - Cấu trúc cây file
- `get_file_content` - Đọc nội dung file
- `search_code` - Tìm kiếm trên codebase

#### Thao Tác Commit / Commit Operations
- `list_commits` - Lịch sử commit
- `get_commit` - Chi tiết commit cụ thể
- `create_commit` - Tạo commit mới

**Thiết Lập:**
```bash
export GITHUB_TOKEN="your_github_token"
# Hoặc sử dụng CLI để thêm trực tiếp:
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### Mở Rộng Biến Môi Trường Trong Cấu Hình / Environment Variable Expansion in Configuration

Cấu hình MCP hỗ trợ mở rộng biến môi trường với các mặc định fallback. Cú pháp `${VAR}` và `${VAR:-default}` hoạt động trong các trường sau: `command`, `args`, `env`, `url`, và `headers`.

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

Các biến được mở rộng tại runtime:
- `${VAR}` - Sử dụng biến môi trường, lỗi nếu không được đặt
- `${VAR:-default}` - Sử dụng biến môi trường, fallback thành mặc định nếu không được đặt

### Ví Dụ 2: Thiết Lập Database MCP / Example 2: Database MCP Setup

**Cấu Hình:**

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

**Ví Dụ Sử Dụng:**

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

**Thiết Lập:**
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# Hoặc sử dụng CLI để thêm trực tiếp:
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

### Ví Dụ 3: Workflow Multi-MCP / Example 3: Multi-MCP Workflow

**Kịch Bản: Tạo Báo Cáo Hàng Ngày**

```markdown
# Workflow Báo Cáo Hàng Ngày Sử Dụng Nhiều MCPs

## Thiết Lập
1. GitHub MCP - fetch metrics PR
2. Database MCP - query dữ liệu bán hàng
3. Slack MCP - post báo cáo
4. Filesystem MCP - lưu báo cáo

## Workflow

### Bước 1: Fetch Dữ Liệu GitHub
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Bước 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Bước 3: Tạo Báo Cáo
Kết hợp dữ liệu vào báo cáo HTML

### Bước 4: Lưu Vào Filesystem
Viết report.html vào /reports/

### Bước 5: Post Vào Slack
Gửi tóm tắt vào channel #daily-reports

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

**Thiết Lập:**
```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
# Thêm mỗi MCP server qua CLI hoặc cấu hình chúng trong .mcp.json
```

### Ví Dụ 4: Thao Tác Filesystem MCP / Example 4: Filesystem MCP Operations

**Cấu Hình:**

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

**Thao Tác Có Sẵn:**

| Thao Tác | Lệnh | Mục Đích |
|-----------|---------|---------|
| List files | `ls ~/projects` | Hiển thị nội dung thư mục |
| Read file | `cat src/main.ts` | Đọc nội dung file |
| Write file | `create docs/api.md` | Tạo file mới |
| Edit file | `edit src/app.ts` | Sửa đổi file |
| Search | `grep "async function"` | Tìm kiếm trong files |
| Delete | `rm old-file.js` | Xóa file |

**Thiết Lập:**
```bash
# Sử dụng CLI để thêm trực tiếp:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## MCP vs Memory: Ma Trận Quyết Định / MCP vs Memory: Decision Matrix

```mermaid
graph TD
    A["Cần dữ liệu bên ngoài?"]
    A -->|Không| B["Sử Dụng Memory"]
    A -->|Có| C["Nó thay đổi thường xuyên?"]
    C -->|Không/Hiếm Khi| B
    C -->|Có/Thường Xuyên| D["Sử Dụng MCP"]

    B -->|Lưu Trữ| E["Preferences<br/>Context<br/>History"]
    D -->|Truy Cập| F["Live APIs<br/>Databases<br/>Services"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## Mẫu Request/Response / Request/Response Pattern

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

## Biến Môi Trường / Environment Variables

Lưu trữ credentials nhạy cảm trong các biến môi trường:

```bash
# ~/.bashrc hoặc ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

Sau đó tham khảo chúng trong cấu hình MCP:

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Claude Như MCP Server (`claude mcp serve`) / Claude as MCP Server

Claude Code bản thân nó có thể hoạt động như một MCP server cho các ứng dụng khác. Điều này cho phép các công cụ bên ngoài, trình soạn thảo, và hệ thống tự động hóa tận dụng các khả năng của Claude qua giao thức MCP chuẩn.

```bash
# Khởi động Claude Code như một MCP server trên stdio
claude mcp serve
```

Các ứng dụng khác sau đó có thể kết nối đến server này như chúng làm với bất kỳ MCP server dựa trên stdio nào khác. Ví dụ, để thêm Claude Code như một MCP server trong một instance Claude Code khác:

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

Điều này hữu ích để xây dựng workflows multi-agent mà một instance Claude điều phối một instance khác.

## Cấu Hình MCP Được Quản Lý (Enterprise) / Managed MCP Configuration

Đối với các triển khai enterprise, các quản trị viên IT có thể thực thi các chính sách MCP server qua file cấu hình `managed-mcp.json`. File này cung cấp kiểm soát độc quyền về việc MCP servers nào được phép hoặc chặn trên toàn tổ chức.

**Vị Trí:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**Tính Năng:**
- `allowedMcpServers` -- whitelist của các servers được phép
- `deniedMcpServers` -- blocklist của các servers bị cấm
- Hỗ trợ matching theo tên server, lệnh, và mẫu URL
- Chính sách MCP toàn tổ chức được thực thi trước cấu hình người dùng
- Ngăn các kết nối server trái phép

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

> **Lưu Ý:** Khi cả `allowedMcpServers` và `deniedMcpServers` khớp một server, quy tắc deny được ưu tiên.

## MCP Servers Được Cung Cấp Bởi Plugin / Plugin-Provided MCP Servers

Plugins có thể đóng gói MCP servers của riêng chúng, làm cho chúng có sẵn tự động khi plugin được cài đặt. MCP servers được cung cấp bởi plugin có thể được định nghĩa theo hai cách:

1. **`.mcp.json` Standalone** -- Đặt một file `.mcp.json` trong thư mục gốc plugin
2. **Inline trong `plugin.json`** -- Định nghĩa MCP servers trực tiếp trong plugin manifest

Sử dụng biến `${CLAUDE_PLUGIN_ROOT}` để tham khảo các đường dẫn tương đối đến thư mục cài đặt plugin:

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

## MCP Phạm Vi Subagent / Subagent-Scoped MCP

Các MCP server có thể được định nghĩa inline trong frontmatter agent sử dụng key `mcpServers:`, scoping chúng đến một subagent cụ thể thay vì toàn bộ project. Điều này hữu ích khi một agent cần truy cập đến một MCP server cụ thể mà các agent khác trong workflow không yêu cầu.

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

MCP servers scoped-subagent chỉ có sẵn trong bối cảnh thực thi của agent đó và không được chia sẻ với các agent cha hoặc anh em.

## Giới Hạn Đầu Ra MCP / MCP Output Limits

Claude Code thực thi các giới hạn trên đầu ra công cụ MCP để ngăn bội ngữ cảnh:

| Giới Hạn | Ngưỡng | Hành Vi |
|-------|-----------|----------|
| **Cảnh Báo** | 10,000 tokens | Một cảnh báo được hiển thị rằng đầu ra lớn |
| **Max mặc định** | 25,000 tokens | Đầu ra bị cắt ngắn vượt quá giới hạn này |
| **Persist đĩa** | 50,000 ký tự | Kết quả công cụ vượt quá 50K ký tự được persist đến đĩa |

Giới hạn đầu ra tối đa có thể cấu hình qua biến môi trường `MAX_MCP_OUTPUT_TOKENS`:

```bash
# Tăng max đầu ra đến 50,000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## Giải Quyết Context Bloat Với Thực Thi Code / Solving Context Bloat with Code Execution

Khi việc áp dụng MCP mở rộng quy mô, kết nối đến hàng chục servers với hàng trăm hoặc hàng nghìn công cụ tạo ra một thách thức đáng kể: **context bloat**. Đây có lẽ là vấn đề lớn nhất với MCP ở quy mô lớn, và nhóm kỹ thuật của Anthropic đã đề xuất một giải pháp elegantly — sử dụng thực thi code thay vì các cuộc gọi công cụ trực tiếp.

> **Nguồn**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic Engineering Blog

### Vấn Đề: Hai Nguồn Lãng Phí Token / The Problem: Two Sources of Token Waste

**1. Định nghĩa công cụ quá tải cửa sổ ngữ cảnh**

Hầu hết các MCP clients tải tất cả định nghĩa công cụ upfront. Khi kết nối đến hàng nghìn công cụ, mô hình phải xử lý hàng trăm nghìn tokens trước khi nó thậm chí đọc yêu cầu của người dùng.

**2. Kết quả trung gian tiêu thụ thêm tokens**

Mọi kết quả công cụ trung gian đi qua ngữ cảnh của mô hình. Hãy xem xét chuyển một bản ghi chép cuộc họp từ Google Drive đến Salesforce — bản ghi chép đầy đủ đi qua ngữ cảnh **hai lần**: một lần khi đọc nó, và lại khi ghi nó đến đích. Một bản ghi chép cuộc họp 2 giờ có thể có nghĩa là 50,000+ tokens thêm.

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### Giải Pháp: Công Cụ MCP Như APIs Code / The Solution: MCP Tools as Code APIs

Thay vì chuyển định nghĩa công cụ và kết quả qua cửa sổ ngữ cảnh, agent **viết code** gọi các công cụ MCP như APIs. Code chạy trong một môi trường thực thi sandbox, và chỉ kết quả cuối cùng trả về mô hình.

```mermaid
graph LR
    A["Model"] -->|"Viết code"| B["Môi Trường Thực Thi Code"]
    B -->|"Gọi tools trực tiếp"| C["MCP Servers"]
    C -->|"Dữ liệu stays trong<br/>execution env"| B
    B -->|"Chỉ kết quả cuối cùng<br/>(minimal tokens)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

#### Nó Hoạt Động Như Thế Na / How It Works

Các công cụ MCP được trình bày như một cây file của các hàm được gõ:

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

Mỗi file công cụ chứa một wrapper được gõ:

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

Agent sau đó viết code để điều phối các công cụ:

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

**Kết Quả: Sử dụng token giảm từ ~150,000 xuống ~2,000 — giảm 98.7%.**

### Lợi Ích Chính / Key Benefits

| Lợi Ích | Mô Tả |
|---------|-------------|
| **Progressive Disclosure** | Agent duyệt filesystem để chỉ tải các định nghĩa công cụ nó cần, thay vì tất cả công cụ upfront |
| **Kết Quả Hiệu Quả Ngữ Cảnh** | Dữ liệu được filtered/transformed trong môi trường thực thi trước khi trả về mô hình |
| **Điều Khiển Luồng Mạnh Mẽ** | Vòng lặp, điều kiện, và xử lý lỗi chạy trong code mà không cần round-trip qua mô hình |
| **Bảo Vệ Quyền Riêng Tư** | Dữ liệu trung gian (PII, hồ sơ nhạy cảm) stays trong môi trường thực thi; không bao giờ đi vào ngữ cảnh mô hình |
| **Persist Trạng Thái** | Agents có thể lưu kết quả trung gian đến files và xây dựng các hàm kỹ năng có thể tái sử dụng |

#### Ví Dụ: Lọc Datasets Lớn / Example: Filtering Large Datasets

```typescript
// Without code execution — all 10,000 rows flow through context
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> returns 10,000 rows in context

// With code execution — filter in the execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Only 5 rows reach the model
```

#### Ví Dụ: Vòng Lặp Không Round-Trip / Example: Loop Without Round-Tripping

```typescript
// Poll for a deployment notification — runs entirely in code
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

### Trade-offs Cần Xem Xét / Trade-offs to Consider

Thực thi code giới thiệu sự phức tạp riêng của nó. Chạy code được tạo bởi agent yêu cầu:

- Một **môi trường thực thi sandbox an toàn** với các giới hạn tài nguyên phù hợp
- **Monitoring và logging** của code được thực thi
- **Chi phí hạ tầng thêm** so với các cuộc gọi công cụ trực tiếp

Các lợi ích — chi phí token giảm, độ trễ thấp hơn, thành phần công cụ tốt hơn — nên được cân nhắc với các chi phí triển khai này. Đối với các agents chỉ với một vài MCP servers, các cuộc gọi công cụ trực tiếp có thể đơn giản hơn. Đối với các agents ở quy mô (hàng chục servers, hàng trăm công cụ), thực thi code là một cải thiện đáng kể.

### MCPorter: Runtime Cho Thành Phần Công Cụ MCP / MCPorter: A Runtime for MCP Tool Composition

[MCPorter](https://github.com/steipete/mcporter) là một runtime TypeScript và toolkit CLI làm cho việc gọi các MCP servers thực tế mà không cần boilerplate — và giúp giảm context bloat qua lộ có chọn lọc công cụ và wrappers được gõ.

**Nó giải quyết gì:** Thay vì tải tất cả định nghĩa công cụ từ tất cả MCP servers upfront, MCPorter cho phép bạn khám phá, kiểm tra, và gọi các công cụ cụ thể theo yêu cầu — giữ ngữ cảnh của bạn gọn gàng.

**Tính năng chính:**

| Tính Năng | Mô Tả |
|---------|-------------|
| **Discovery zero-config** | Tự động khám phá MCP servers từ Cursor, Claude, Codex, hoặc cấu hình local |
| **Clients công cụ được gõ** | `mcporter emit-ts` tạo interfaces `.d.ts` và wrappers sẵn sàng chạy |
| **API có thể thành phần** | `createServerProxy()` lộ các công cụ như các phương thức camelCase với các helpers `.text()`, `.json()`, `.markdown()` |
| **Generation CLI** | `mcporter generate-cli` chuyển đổi bất kỳ MCP server nào thành một CLI độc lập với filtering `--include-tools` / `--exclude-tools` |
| **Ẩn parameter** | Các parameters tùy chọn stays hidden theo mặc định, giảm verbosity schema |

**Cài Đặt:**

```bash
npx mcporter list          # No install required — discover servers instantly
pnpm add mcporter          # Add to a project
brew install steipete/tap/mcporter  # macOS via Homebrew
```

**Ví dụ — thành phần công cụ trong TypeScript:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Dữ liệu đi giữa các công cụ mà không đi qua ngữ cảnh mô hình
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**Ví dụ — cuộc gọi công cụ CLI:**

```bash
# Gọi một công cụ cụ thể trực tiếp
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# Liệt kê các servers và công cụ có sẵn
npx mcporter list
```

MCPorter bổ sung cho cách tiếp cận thực thi code được mô tả ở trên bằng cách cung cấp hạ tầng runtime để gọi các công cụ MCP như các APIs được gõ — làm cho nó đơn giản để giữ dữ liệu trung gian ra khỏi ngữ cảnh mô hình.

## Thực Hành Tốt Nhất / Best Practices

### Cân Nhắc Bảo Mật / Security Considerations

#### Nên Làm ✅ / Do's ✅
- Sử dụng biến môi trường cho tất cả credentials
- Rotate tokens và API keys thường xuyên (khuyến nghị hàng tháng)
- Sử dụng tokens read-only khi có thể
- Giới hạn phạm vi truy cập MCP server đến tối thiểu cần thiết
- Monitor việc sử dụng MCP server và logs truy cập
- Sử dụng OAuth cho các dịch vụ bên ngoài khi có sẵn
- Triển khai rate limiting trên các yêu cầu MCP
- Test các kết nối MCP trước khi sử dụng production
- Tài liệu hóa tất cả các kết nối MCP hoạt động
- Giữ các gói MCP server được cập nhật

#### Không Nên Làm ❌ / Don'ts ❌
- Đừng hardcode credentials trong các file cấu hình
- Đừng commit tokens hoặc secrets vào git
- Đừng chia sẻ tokens trong các cuộc trò chuyện nhóm hoặc email
- Đừng sử dụng tokens cá nhân cho các dự án nhóm
- Đừng cấp các quyền không cần thiết
- Đừng bỏ qua các lỗi xác thực
- Đừng lộ các endpoint MCP công khai
- Đừng chạy các MCP servers với các đặc quyền root/admin
- Đừng cache dữ liệu nhạy cảm trong logs
- Đừng tắt các cơ chế xác thực

### Thực Hành Tốt Nhất Về Cấu Hình / Configuration Best Practices

1. **Kiểm Soát Phiên Bản**: Giữ `.mcp.json` trong git nhưng sử dụng biến môi trường cho secrets
2. **Đặc Quyền Tối Thiểu**: Cấp các quyền tối thiểu cần thiết cho mỗi MCP server
3. **Cô Lập**: Chạy các MCP servers khác nhau trong các tiến trình riêng biệt khi có thể
4. **Monitoring**: Ghi nhật ký tất cả các yêu cầu và lỗi MCP cho các audit trails
5. **Testing**: Test tất cả các cấu hình MCP trước khi triển khai sang production

### Mẹo Hiệu Suất / Performance Tips

- Cache dữ liệu được truy cập thường xuyên ở cấp ứng dụng
- Sử dụng các truy vấn MCP cụ thể để giảm chuyển dữ liệu
- Monitor các thời gian phản hồi cho các thao tác MCP
- Cân nhắc rate limiting cho các APIs bên ngoài
- Sử dụng batching khi thực hiện nhiều thao tác

## Hướng Dẫn Cài Đặt / Installation Instructions

### Điều Kiện Tiên Quyết / Prerequisites
- Node.js và npm được cài đặt
- Claude Code CLI được cài đặt
- API tokens/credentials cho các dịch vụ bên ngoài

### Thiết Lập Từng Bước / Step-by-Step Setup

1. **Thêm MCP server đầu tiên của bạn** sử dụng CLI (ví dụ: GitHub):
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

   Hoặc tạo một file `.mcp.json` trong thư mục gốc project của bạn:
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

2. **Đặt các biến môi trường:**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3. **Test kết nối:**
```bash
claude /mcp
```

4. **Sử dụng các công cụ MCP:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### Cài Đặt Cho Các Dịch Vụ Cụ Thể / Installation for Specific Services

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

## Xử Lý Sự Cố / Troubleshooting

### MCP Server Not Found
```bash
# Xác minh MCP server được cài đặt
npm list -g @modelcontextprotocol/server-github

# Cài đặt nếu thiếu
npm install -g @modelcontextprotocol/server-github
```

### Authentication Failed
```bash
# Xác minh biến môi trường được đặt
echo $GITHUB_TOKEN

# Re-export nếu cần
export GITHUB_TOKEN="your_token"

# Xác minh token có các quyền đúng
# Check GitHub token scopes tại: https://github.com/settings/tokens
```

### Connection Timeout
- Kiểm tra kết nối mạng: `ping api.github.com`
- Xác minh API endpoint có thể truy cập
- Kiểm tra các giới hạn rate trên API
- Thử tăng timeout trong cấu hình
- Kiểm tra các vấn đề firewall hoặc proxy

### MCP Server Crashes
- Kiểm tra logs MCP server: `~/.claude/logs/`
- Xác minh tất cả các biến môi trường được đặt
- Đảm bảo các quyền file phù hợp
- Thử cài đặt lại gói MCP server
- Kiểm tra các tiến trình xung đột trên cùng một cổng

## Các Khái Niệm Liên Quan / Related Concepts

### Memory vs MCP
- **Memory**: Lưu trữ dữ liệu liên tục, không thay đổi (preferences, context, history)
- **MCP**: Truy cập dữ liệu trực tiếp, thay đổi (APIs, databases, dịch vụ thời gian thực)

### Khi Nào Sử Dụng Mỗi Thứ / When to Use Each
- **Sử Dụng Memory** cho: User preferences, lịch sử hội thoại, ngữ cảnh được học
- **Sử Dụng MCP** cho: Các vấn đề GitHub hiện tại, truy vấn database trực tiếp, dữ liệu thời gian thực

### Tích Hợp Với Các Tính Năng Claude Khác / Integration with Other Claude Features
- Kết hợp MCP với Memory cho ngữ cảnh phong phú
- Sử dụng các công cụ MCP trong prompts để suy luận tốt hơn
- Tận dụng nhiều MCPs cho các workflows phức tạp

## Tài Nguyên Thêm / Additional Resources

- [Tài Liệu MCP Chính Thức](https://code.claude.com/docs/en/mcp)
- [Đặc Tả Giao Thức MCP](https://modelcontextprotocol.io/specification)
- [Kho GitHub MCP](https://github.com/modelcontextprotocol/servers)
- [MCP Servers Có Sẵn](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — Runtime & CLI TypeScript để gọi MCP servers mà không cần boilerplate
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Blog kỹ thuật Anthropic về giải quyết context bloat
- [CLI Reference Claude Code](https://code.claude.com/docs/en/cli-reference)
- [Tài Liệu API Claude](https://docs.anthropic.com)
