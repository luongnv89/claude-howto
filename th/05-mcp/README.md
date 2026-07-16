<!-- i18n-source: 05-mcp/README.md -->
<!-- i18n-date: 2026-05-08 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

โฟลเดอร์นี้ประกอบด้วยเอกสารและตัวอย่างที่ครอบคลุมสำหรับการกำหนดค่า MCP server และการใช้งานร่วมกับ Claude Code

## ภาพรวม

MCP (Model Context Protocol) คือมาตรฐานที่ช่วยให้ Claude เข้าถึงเครื่องมือภายนอก API และแหล่งข้อมูลแบบเรียลไทม์ได้ ต่างจาก Memory ตรงที่ MCP ให้การเข้าถึงข้อมูลที่เปลี่ยนแปลงตลอดเวลาแบบสด

คุณสมบัติหลัก:
- การเข้าถึงบริการภายนอกแบบเรียลไทม์
- การซิงโครไนซ์ข้อมูลสด
- สถาปัตยกรรมที่ขยายได้
- การยืนยันตัวตนที่ปลอดภัย
- การโต้ตอบผ่านเครื่องมือ

## สถาปัตยกรรม MCP

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

## ระบบนิเวศ MCP

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

## วิธีการติดตั้ง MCP

Claude Code รองรับหลาย transport protocol สำหรับการเชื่อมต่อ MCP server:

### HTTP Transport (แนะนำ)

```bash
# เชื่อมต่อ HTTP พื้นฐาน
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP พร้อม authentication header
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Stdio Transport (แบบ Local)

สำหรับ MCP server ที่รันในเครื่องของตนเอง:

```bash
# Local Node.js server
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# พร้อม environment variables
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### SSE Transport (เลิกใช้แล้ว)

Server-Sent Events transport ถูกเลิกใช้แล้ว แนะนำให้ใช้ `http` แทน แต่ยังคงรองรับอยู่:

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### หมายเหตุสำหรับ Windows

บน Windows ดั้งเดิม (ไม่ใช่ WSL) ให้ใช้ `cmd /c` สำหรับคำสั่ง npx:

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### OAuth 2.0 Authentication

Claude Code รองรับ OAuth 2.0 สำหรับ MCP server ที่ต้องการการยืนยันตัวตน เมื่อเชื่อมต่อกับ server ที่เปิดใช้ OAuth Claude Code จะจัดการกระบวนการยืนยันตัวตนทั้งหมด:

```bash
# เชื่อมต่อกับ MCP server ที่ใช้ OAuth (แบบโต้ตอบ)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# กำหนดค่า OAuth credentials ล่วงหน้าสำหรับการตั้งค่าแบบอัตโนมัติ
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| ฟีเจอร์ | คำอธิบาย |
|---------|-------------|
| **Interactive OAuth** | ใช้ `/mcp` เพื่อเริ่ม OAuth flow ผ่านเบราว์เซอร์ |
| **Pre-configured OAuth clients** | OAuth clients ที่ติดตั้งมาพร้อมใช้สำหรับบริการทั่วไป เช่น Notion, Stripe และอื่นๆ (v2.1.30+) |
| **Pre-configured credentials** | flags `--client-id`, `--client-secret`, `--callback-port` สำหรับการตั้งค่าอัตโนมัติ |
| **Token storage** | tokens ถูกเก็บอย่างปลอดภัยใน system keychain |
| **Step-up auth** | รองรับ step-up authentication สำหรับการดำเนินการที่ต้องการสิทธิ์พิเศษ |
| **Discovery caching** | metadata ของ OAuth discovery ถูก cache เพื่อการเชื่อมต่อใหม่ที่รวดเร็วขึ้น |
| **Metadata override** | `oauth.authServerMetadataUrl` ใน `.mcp.json` เพื่อแทนที่การค้นพบ metadata OAuth เริ่มต้น |

#### การแทนที่การค้นพบ OAuth Metadata

หาก MCP server ของคุณส่งข้อผิดพลาดที่ endpoint metadata OAuth มาตรฐาน (`/.well-known/oauth-authorization-server`) แต่มี endpoint OIDC ที่ใช้งานได้ คุณสามารถกำหนดให้ Claude Code ดึง metadata OAuth จาก URL เฉพาะได้ ตั้งค่า `authServerMetadataUrl` ใน object `oauth` ของการกำหนดค่า server:

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

URL ต้องใช้ `https://` ตัวเลือกนี้ต้องใช้ Claude Code v2.1.64 หรือสูงกว่า

### Claude.ai MCP Connectors

MCP server ที่กำหนดค่าในบัญชี Claude.ai ของคุณพร้อมใช้งานใน Claude Code โดยอัตโนมัติ ซึ่งหมายความว่าการเชื่อมต่อ MCP ที่คุณตั้งค่าผ่านเว็บอินเทอร์เฟซ Claude.ai จะสามารถเข้าถึงได้โดยไม่ต้องกำหนดค่าเพิ่มเติม

Claude.ai MCP connectors ยังพร้อมใช้งานในโหมด `--print` (v2.1.83+) ซึ่งเปิดใช้งานการใช้งานแบบไม่โต้ตอบและแบบ scripted

> **หมายเหตุการเริ่มต้น (v2.1.117+):** Concurrent connect เป็นค่าเริ่มต้นเมื่อกำหนดค่า MCP server ทั้งแบบ local และ claude.ai ไว้ (เดิมเป็นแบบ serial) ซึ่งลด startup latency เมื่อมีหลาย server ทำงานอยู่

หากต้องการปิดใช้งาน Claude.ai MCP servers ใน Claude Code ให้ตั้งค่าตัวแปรสภาพแวดล้อม `ENABLE_CLAUDEAI_MCP_SERVERS` เป็น `false`:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **หมายเหตุ:** ฟีเจอร์นี้พร้อมใช้งานเฉพาะผู้ใช้ที่ลงชื่อเข้าใช้ด้วยบัญชี Claude.ai เท่านั้น

## กระบวนการตั้งค่า MCP

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

### คำสั่ง `/mcp`

พิมพ์ `/mcp` ภายใน session เพื่อแสดงรายการ server ที่เชื่อมต่อ เริ่ม OAuth flow และตรวจสอบสถานะการเชื่อมต่อ

- ตั้งแต่ **v2.1.121** MCP จะลองเชื่อมต่อใหม่สูงสุด 3 ครั้งเมื่อเกิดข้อผิดพลาดชั่วคราว
- ตั้งแต่ **v2.1.128** `/mcp` แสดง **จำนวนเครื่องมือ** สำหรับแต่ละ server ที่เชื่อมต่อ และแสดงสัญลักษณ์เตือนสำหรับ server ที่รายงาน **0 เครื่องมือ** เพื่อให้ระบุ server ที่กำหนดค่าผิดพลาดได้ทันที

## การค้นหาเครื่องมือ MCP

เมื่อคำอธิบายเครื่องมือ MCP เกิน 10% ของ context window Claude Code จะเปิดใช้งานการค้นหาเครื่องมืออัตโนมัติเพื่อเลือกเครื่องมือที่เหมาะสมโดยไม่ทำให้ context ของโมเดลหนักเกินไป

| การตั้งค่า | ค่า | คำอธิบาย |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | `auto` (ค่าเริ่มต้น) | เปิดใช้งานอัตโนมัติเมื่อคำอธิบายเครื่องมือเกิน 10% ของ context |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | เปิดใช้งานอัตโนมัติที่ threshold `N` เครื่องมือที่กำหนดเอง |
| `ENABLE_TOOL_SEARCH` | `true` | เปิดใช้งานเสมอโดยไม่คำนึงถึงจำนวนเครื่องมือ |
| `ENABLE_TOOL_SEARCH` | `false` | ปิดใช้งาน ส่งคำอธิบายเครื่องมือทั้งหมดแบบเต็ม |

> **หมายเหตุ:** การค้นหาเครื่องมือต้องใช้ Sonnet 4 หรือสูงกว่า หรือ Opus 4 หรือสูงกว่า โมเดล Haiku ไม่รองรับการค้นหาเครื่องมือ

### การข้ามการค้นหาเครื่องมือต่อ Server (v2.1.121+)

หาก MCP server บางตัวต้องการเครื่องมือในทุก turn ให้กำหนดค่า `"alwaysLoad": true` ในการกำหนดค่าเพื่อข้ามการเลื่อนการค้นหาเครื่องมือและทำให้เครื่องมือพร้อมใช้งานเสมอ:

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

ใช้อย่างระมัดระวัง — เครื่องมือที่โหลดเสมอจะใช้ context ที่อาจนำไปใช้สำหรับการค้นหาเครื่องมือที่เกี่ยวข้องมากกว่า

## การอัปเดตเครื่องมือแบบ Dynamic

Claude Code รองรับการแจ้งเตือน `list_changed` ของ MCP เมื่อ MCP server เพิ่ม ลบ หรือแก้ไขเครื่องมือที่พร้อมใช้งานแบบ dynamic Claude Code จะรับการอัปเดตและปรับรายการเครื่องมือโดยอัตโนมัติ โดยไม่ต้องเชื่อมต่อใหม่หรือรีสตาร์ท

## MCP Apps

MCP Apps คือ extension MCP อย่างเป็นทางการแรก ที่ช่วยให้การเรียกใช้เครื่องมือ MCP ส่งคืน UI component แบบโต้ตอบที่แสดงผลในอินเทอร์เฟซแชทโดยตรง แทนที่จะเป็นการตอบสนองข้อความธรรมดา MCP server สามารถส่ง dashboard ที่สมบูรณ์ แบบฟอร์ม การแสดงผลข้อมูล และ workflow หลายขั้นตอน — ทั้งหมดแสดงแบบ inline โดยไม่ต้องออกจากการสนทนา

## MCP Elicitation

MCP server สามารถร้องขอข้อมูลที่มีโครงสร้างจากผู้ใช้ผ่าน dialog แบบโต้ตอบ (v2.1.49+) ซึ่งช่วยให้ MCP server สามารถขอข้อมูลเพิ่มเติมระหว่าง workflow ได้ เช่น การขอการยืนยัน การเลือกจากรายการตัวเลือก หรือการกรอกข้อมูลที่จำเป็น

## ขีดจำกัดคำอธิบายเครื่องมือและคำสั่ง

ตั้งแต่ v2.1.84 Claude Code บังคับใช้ขีดจำกัด **2 KB** ต่อคำอธิบายเครื่องมือและคำสั่งต่อ MCP server หนึ่งตัว เพื่อป้องกันไม่ให้ server แต่ละตัวใช้ context มากเกินไปด้วยคำอธิบายเครื่องมือที่ยาวเกินไป

## MCP Prompts เป็น Slash Commands

MCP server สามารถเปิดเผย prompts ที่ปรากฏเป็น slash commands ใน Claude Code Prompts สามารถเข้าถึงได้โดยใช้รูปแบบการตั้งชื่อ:

```
/mcp__<server>__<prompt>
```

ตัวอย่างเช่น หาก server ชื่อ `github` เปิดเผย prompt ชื่อ `review` คุณสามารถเรียกใช้ได้ด้วย `/mcp__github__review`

## การกำจัดการซ้ำซ้อนของ Server

เมื่อ MCP server เดียวกันถูกกำหนดในหลาย scope (local, project, user) การกำหนดค่า local จะมีความสำคัญก่อน ซึ่งช่วยให้คุณแทนที่การตั้งค่า MCP ระดับ project หรือ user ด้วยการปรับแต่ง local โดยไม่มีความขัดแย้ง

## MCP Resources ผ่าน @ Mentions

คุณสามารถอ้างอิง MCP resources โดยตรงใน prompt ด้วยรูปแบบ `@` mention:

```
@server-name:protocol://resource/path
```

ตัวอย่างเช่น เพื่ออ้างอิง resource ฐานข้อมูลเฉพาะ:

```
@database:postgres://mydb/users
```

ซึ่งช่วยให้ Claude ดึงและรวมเนื้อหา MCP resource แบบ inline เป็นส่วนหนึ่งของ context การสนทนา

## MCP Scopes

การกำหนดค่า MCP สามารถเก็บไว้ที่ scope ต่างๆ ที่มีระดับการแชร์ที่แตกต่างกัน:

| Scope | ที่เก็บ | คำอธิบาย | แชร์กับ | ต้องอนุมัติ |
|-------|----------|-------------|-------------|------------------|
| **Local** (ค่าเริ่มต้น) | `~/.claude.json` (ใต้ project path) | ส่วนตัวสำหรับผู้ใช้ปัจจุบัน เฉพาะ project ปัจจุบัน | คุณเท่านั้น | ไม่ |
| **Project** | `.mcp.json` | Checked เข้า git repository | สมาชิกทีม | ใช่ (ใช้ครั้งแรก) |
| **User** | `~/.claude.json` | พร้อมใช้งานในทุก project | คุณเท่านั้น | ไม่ |

### การใช้ Project Scope

เก็บการกำหนดค่า MCP เฉพาะ project ใน `.mcp.json`:

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

สมาชิกทีมจะเห็น prompt การอนุมัติเมื่อใช้ project MCPs ครั้งแรก

## การจัดการการกำหนดค่า MCP

### การเพิ่ม MCP Servers

```bash
# เพิ่ม server แบบ HTTP
claude mcp add --transport http github https://api.github.com/mcp

# เพิ่ม local stdio server
claude mcp add --transport stdio database -- npx @company/db-server

# แสดงรายการ MCP server ทั้งหมด
claude mcp list

# ดูรายละเอียด server เฉพาะ
claude mcp get github

# ลบ MCP server
claude mcp remove github

# รีเซ็ตตัวเลือกการอนุมัติเฉพาะ project
claude mcp reset-project-choices

# นำเข้าจาก Claude Desktop
claude mcp add-from-claude-desktop
```

## ตาราง MCP Server ที่พร้อมใช้งาน

| MCP Server | วัตถุประสงค์ | เครื่องมือทั่วไป | Auth | เรียลไทม์ |
|------------|---------|--------------|------|-----------|
| **Filesystem** | การดำเนินการไฟล์ | read, write, delete | สิทธิ์ OS | ✅ ใช่ |
| **GitHub** | การจัดการ repository | list_prs, create_issue, push | OAuth | ✅ ใช่ |
| **Slack** | การสื่อสารในทีม | send_message, list_channels | Token | ✅ ใช่ |
| **Database** | คำสั่ง SQL | query, insert, update | Credentials | ✅ ใช่ |
| **Google Docs** | การเข้าถึงเอกสาร | read, write, share | OAuth | ✅ ใช่ |
| **Asana** | การจัดการโครงการ | create_task, update_status | API Key | ✅ ใช่ |
| **Stripe** | ข้อมูลการชำระเงิน | list_charges, create_invoice | API Key | ✅ ใช่ |
| **Memory** | memory แบบถาวร | store, retrieve, delete | Local | ❌ ไม่ |

## ตัวอย่างเชิงปฏิบัติ

### ตัวอย่างที่ 1: การกำหนดค่า GitHub MCP

**ไฟล์:** `.mcp.json` (รากของ project)

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

**เครื่องมือ GitHub MCP ที่พร้อมใช้งาน:**

#### การจัดการ Pull Request
- `list_prs` - แสดงรายการ PR ทั้งหมดใน repository
- `get_pr` - ดูรายละเอียด PR รวมถึง diff
- `create_pr` - สร้าง PR ใหม่
- `update_pr` - อัปเดตคำอธิบาย/ชื่อ PR
- `merge_pr` - Merge PR ไปยัง main branch
- `review_pr` - เพิ่มความคิดเห็นในการตรวจสอบ

**ตัวอย่างคำขอ:**
```
/mcp__github__get_pr 456

# ผลลัพธ์:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### การจัดการ Issue
- `list_issues` - แสดงรายการ issue ทั้งหมด
- `get_issue` - ดูรายละเอียด issue
- `create_issue` - สร้าง issue ใหม่
- `close_issue` - ปิด issue
- `add_comment` - เพิ่มความคิดเห็นใน issue

#### ข้อมูล Repository
- `get_repo_info` - รายละเอียด repository
- `list_files` - โครงสร้าง file tree
- `get_file_content` - อ่านเนื้อหาไฟล์
- `search_code` - ค้นหาทั่ว codebase

#### การดำเนินการ Commit
- `list_commits` - ประวัติ commit
- `get_commit` - รายละเอียด commit เฉพาะ
- `create_commit` - สร้าง commit ใหม่

**การตั้งค่า:**
```bash
export GITHUB_TOKEN="your_github_token"
# หรือใช้ CLI เพื่อเพิ่มโดยตรง:
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### การขยาย Environment Variable ในการกำหนดค่า

การกำหนดค่า MCP รองรับการขยาย environment variable พร้อม fallback เริ่มต้น รูปแบบ `${VAR}` และ `${VAR:-default}` ทำงานในฟิลด์ต่อไปนี้: `command`, `args`, `env`, `url` และ `headers`

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

ตัวแปรจะถูกขยายขณะ runtime:
- `${VAR}` - ใช้ environment variable ข้อผิดพลาดถ้าไม่ได้ตั้งค่า
- `${VAR:-default}` - ใช้ environment variable ใช้ค่า default ถ้าไม่ได้ตั้งค่า

### ตัวอย่างที่ 2: การตั้งค่า Database MCP

**การกำหนดค่า:**

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

**ตัวอย่างการใช้งาน:**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# ใช้เครื่องมือ MCP database:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# ผลลัพธ์:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

**การตั้งค่า:**
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# หรือใช้ CLI เพื่อเพิ่มโดยตรง:
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

### ตัวอย่างที่ 3: Multi-MCP Workflow

**สถานการณ์: การสร้างรายงานรายวัน**

```markdown
# Daily Report Workflow โดยใช้หลาย MCP

## การตั้งค่า
1. GitHub MCP - ดึงตัวชี้วัด PR
2. Database MCP - สืบค้นข้อมูลยอดขาย
3. Slack MCP - โพสต์รายงาน
4. Filesystem MCP - บันทึกรายงาน

## Workflow

### ขั้นตอนที่ 1: ดึงข้อมูล GitHub
/mcp__github__list_prs completed:true last:7days

ผลลัพธ์:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### ขั้นตอนที่ 2: สืบค้นฐานข้อมูล
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

ผลลัพธ์:
- Sales: 247
- Revenue: $12,450

### ขั้นตอนที่ 3: สร้างรายงาน
รวมข้อมูลเป็นรายงาน HTML

### ขั้นตอนที่ 4: บันทึกไปยัง Filesystem
เขียน report.html ไปยัง /reports/

### ขั้นตอนที่ 5: โพสต์ไปยัง Slack
ส่งสรุปไปยัง channel #daily-reports

ผลลัพธ์สุดท้าย:
✅ สร้างและโพสต์รายงานแล้ว
📊 merge 47 PR ในสัปดาห์นี้
💰 ยอดขายรายวัน $12,450
```

**การตั้งค่า:**
```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
# เพิ่ม MCP server แต่ละตัวผ่าน CLI หรือกำหนดค่าใน .mcp.json
```

### ตัวอย่างที่ 4: การดำเนินการ Filesystem MCP

**การกำหนดค่า:**

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

**การดำเนินการที่พร้อมใช้งาน:**

| การดำเนินการ | คำสั่ง | วัตถุประสงค์ |
|-----------|---------|---------|
| แสดงรายการไฟล์ | `ls ~/projects` | แสดงเนื้อหา directory |
| อ่านไฟล์ | `cat src/main.ts` | อ่านเนื้อหาไฟล์ |
| เขียนไฟล์ | `create docs/api.md` | สร้างไฟล์ใหม่ |
| แก้ไขไฟล์ | `edit src/app.ts` | แก้ไขไฟล์ |
| ค้นหา | `grep "async function"` | ค้นหาในไฟล์ |
| ลบ | `rm old-file.js` | ลบไฟล์ |

**การตั้งค่า:**
```bash
# ใช้ CLI เพื่อเพิ่มโดยตรง:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## เมทริกซ์การตัดสินใจ MCP vs Memory

```mermaid
graph TD
    A["ต้องการข้อมูลภายนอก?"]
    A -->|ไม่| B["ใช้ Memory"]
    A -->|ใช่| C["ข้อมูลเปลี่ยนบ่อยหรือไม่?"]
    C -->|ไม่/นานๆ ครั้ง| B
    C -->|ใช่/บ่อยครั้ง| D["ใช้ MCP"]

    B -->|เก็บ| E["การตั้งค่า<br/>Context<br/>ประวัติ"]
    D -->|เข้าถึง| F["Live APIs<br/>ฐานข้อมูล<br/>บริการ"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## รูปแบบ Request/Response

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

## Environment Variables

เก็บ credentials ที่ละเอียดอ่อนใน environment variables:

```bash
# ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

จากนั้นอ้างอิงในการกำหนดค่า MCP:

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Claude เป็น MCP Server (`claude mcp serve`)

Claude Code เองสามารถทำหน้าที่เป็น MCP server สำหรับแอปพลิเคชันอื่นๆ ได้ ซึ่งช่วยให้เครื่องมือภายนอก editor และระบบอัตโนมัติสามารถใช้ประโยชน์จากความสามารถของ Claude ผ่าน protocol MCP มาตรฐาน

```bash
# เริ่ม Claude Code เป็น MCP server บน stdio
claude mcp serve
```

แอปพลิเคชันอื่นๆ สามารถเชื่อมต่อกับ server นี้ได้เหมือน stdio-based MCP server ทั่วไป ตัวอย่างเช่น เพื่อเพิ่ม Claude Code เป็น MCP server ใน Claude Code อีกตัวหนึ่ง:

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

ซึ่งมีประโยชน์สำหรับการสร้าง multi-agent workflow ที่ Claude ตัวหนึ่งประสานงาน Claude ตัวอื่น

## การกำหนดค่า MCP แบบ Managed (Enterprise)

สำหรับการ deployment ระดับองค์กร ผู้ดูแลระบบ IT สามารถบังคับใช้นโยบาย MCP server ผ่านไฟล์กำหนดค่า `managed-mcp.json` ไฟล์นี้ให้การควบคุมเฉพาะว่า MCP server ใดได้รับอนุญาตหรือถูกบล็อกทั่วทั้งองค์กร

**ที่เก็บ:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**ฟีเจอร์:**
- `allowedMcpServers` -- whitelist ของ server ที่ได้รับอนุญาต
- `deniedMcpServers` -- blocklist ของ server ที่ถูกห้าม
- รองรับการจับคู่ด้วยชื่อ server คำสั่ง และรูปแบบ URL
- นโยบาย MCP ทั่วทั้งองค์กรถูกบังคับใช้ก่อนการกำหนดค่าของผู้ใช้
- ป้องกันการเชื่อมต่อ server ที่ไม่ได้รับอนุญาต

**ตัวอย่างการกำหนดค่า:**

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

> **หมายเหตุ:** เมื่อทั้ง `allowedMcpServers` และ `deniedMcpServers` ตรงกับ server กฎ deny จะมีความสำคัญก่อน

## MCP Servers ที่ Plugin จัดหาให้

Plugin สามารถรวม MCP server ของตนเองได้ ทำให้พร้อมใช้งานโดยอัตโนมัติเมื่อติดตั้ง plugin MCP server ที่ plugin จัดหาสามารถกำหนดได้สองวิธี:

1. **Standalone `.mcp.json`** -- วาง `.mcp.json` ในไดเรกทอรีรากของ plugin
2. **Inline ใน `plugin.json`** -- กำหนด MCP server โดยตรงในไฟล์ manifest ของ plugin

ใช้ตัวแปร `${CLAUDE_PLUGIN_ROOT}` เพื่ออ้างอิง path ที่สัมพัทธ์กับไดเรกทอรีติดตั้งของ plugin:

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

## MCP ที่มีขอบเขตต่อ Subagent

MCP server สามารถกำหนดแบบ inline ภายใน frontmatter ของ agent โดยใช้คีย์ `mcpServers:` ซึ่งกำหนดขอบเขตให้กับ subagent เฉพาะแทนที่จะเป็นทั้ง project ซึ่งมีประโยชน์เมื่อ agent ต้องการเข้าถึง MCP server เฉพาะที่ agent อื่นใน workflow ไม่ต้องการ

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

MCP server ที่มีขอบเขตต่อ subagent พร้อมใช้งานเฉพาะใน context การทำงานของ agent นั้น และไม่แชร์กับ agent หลักหรือ agent พี่น้อง

## ขีดจำกัดผลลัพธ์ MCP

Claude Code บังคับใช้ขีดจำกัดผลลัพธ์เครื่องมือ MCP เพื่อป้องกัน context overflow:

| ขีดจำกัด | เกณฑ์ | พฤติกรรม |
|-------|-----------|----------|
| **คำเตือน** | 10,000 tokens | แสดงคำเตือนว่าผลลัพธ์มีขนาดใหญ่ |
| **สูงสุดเริ่มต้น** | 25,000 tokens | ผลลัพธ์ถูกตัดทอนเกินขีดจำกัดนี้ |
| **Disk persistence** | 50,000 อักขระ | ผลลัพธ์เครื่องมือที่เกิน 50K อักขระจะถูกเก็บไว้ในดิสก์ |

ขีดจำกัดผลลัพธ์สูงสุดสามารถกำหนดค่าได้ผ่าน environment variable `MAX_MCP_OUTPUT_TOKENS`:

```bash
# เพิ่มผลลัพธ์สูงสุดเป็น 50,000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## การแก้ปัญหา Context Bloat ด้วย Code Execution

เมื่อการนำ MCP ไปใช้ขยายตัว การเชื่อมต่อกับ server หลายสิบตัวที่มีเครื่องมือหลายร้อยหรือหลายพันตัวสร้างความท้าทายที่สำคัญ: **context bloat** นี่คือปัญหาที่ใหญ่ที่สุดกับ MCP ในระดับขนาดใหญ่ และทีมวิศวกรรมของ Anthropic ได้เสนอวิธีแก้ปัญหาที่ชาญฉลาด — การใช้ code execution แทนการเรียกใช้เครื่องมือโดยตรง

> **แหล่งที่มา**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic Engineering Blog

### ปัญหา: สองแหล่งของการสูญเสีย Token

**1. คำจำกัดความเครื่องมือทำให้ context window เต็ม**

MCP client ส่วนใหญ่โหลดคำจำกัดความเครื่องมือทั้งหมดล่วงหน้า เมื่อเชื่อมต่อกับเครื่องมือหลายพันตัว โมเดลต้องประมวลผล token หลายแสนตัวก่อนอ่านคำขอของผู้ใช้

**2. ผลลัพธ์ระหว่างกลางใช้ token เพิ่มเติม**

ผลลัพธ์เครื่องมือระหว่างกลางทุกตัวผ่าน context ของโมเดล พิจารณาการถ่ายโอน transcript การประชุมจาก Google Drive ไปยัง Salesforce — transcript ทั้งหมดไหลผ่าน context **สองครั้ง**: ครั้งหนึ่งเมื่ออ่าน และอีกครั้งเมื่อเขียนไปยังปลายทาง transcript การประชุม 2 ชั่วโมงอาจหมายถึง token เพิ่มเติมกว่า 50,000 ตัว

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### วิธีแก้ปัญหา: เครื่องมือ MCP เป็น Code APIs

แทนที่จะส่งคำจำกัดความเครื่องมือและผลลัพธ์ผ่าน context window agent **เขียนโค้ด** ที่เรียกใช้เครื่องมือ MCP เป็น API โค้ดรันใน execution environment แบบ sandbox และมีเพียงผลลัพธ์สุดท้ายที่ส่งกลับไปยังโมเดล

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

#### วิธีการทำงาน

เครื่องมือ MCP ถูกนำเสนอเป็น file tree ของฟังก์ชันที่มี type:

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

ไฟล์เครื่องมือแต่ละไฟล์ประกอบด้วย wrapper ที่มี type:

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

จากนั้น agent เขียนโค้ดเพื่อประสานงานเครื่องมือ:

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// ข้อมูลไหลโดยตรงระหว่างเครื่องมือ — ไม่ผ่านโมเดล
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**ผลลัพธ์: การใช้ token ลดลงจาก ~150,000 เป็น ~2,000 — ลดลง 98.7%**

### ประโยชน์หลัก

| ประโยชน์ | คำอธิบาย |
|---------|-------------|
| **Progressive Disclosure** | Agent เรียกดู filesystem เพื่อโหลดเฉพาะคำจำกัดความเครื่องมือที่ต้องการ แทนที่จะโหลดทั้งหมดล่วงหน้า |
| **ผลลัพธ์ที่ประหยัด Context** | ข้อมูลถูกกรอง/แปลงใน execution environment ก่อนส่งกลับไปยังโมเดล |
| **การควบคุมการไหลที่มีประสิทธิภาพ** | Loops เงื่อนไข และการจัดการข้อผิดพลาดรันในโค้ดโดยไม่ต้องส่งกลับผ่านโมเดล |
| **การรักษาความเป็นส่วนตัว** | ข้อมูลระหว่างกลาง (PII ระเบียนที่ละเอียดอ่อน) อยู่ใน execution environment ไม่เข้า context ของโมเดล |
| **State Persistence** | Agent สามารถบันทึกผลลัพธ์ระหว่างกลางลงในไฟล์และสร้างฟังก์ชัน skill ที่นำมาใช้ซ้ำได้ |

#### ตัวอย่าง: การกรอง Dataset ขนาดใหญ่

```typescript
// ไม่มี code execution — แถวทั้งหมด 10,000 แถวไหลผ่าน context
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> returns 10,000 rows in context

// มี code execution — กรองใน execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // มีเพียง 5 แถวที่ส่งถึงโมเดล
```

#### ตัวอย่าง: Loop โดยไม่ต้องส่งกลับผ่านโมเดล

```typescript
// รอการแจ้งเตือน deployment — รันทั้งหมดในโค้ด
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

### ข้อแลกเปลี่ยนที่ต้องพิจารณา

Code execution มีความซับซ้อนของตัวเอง การรันโค้ดที่ agent สร้างต้องการ:

- **execution environment แบบ sandbox ที่ปลอดภัย** พร้อมขีดจำกัดทรัพยากรที่เหมาะสม
- **การติดตามและการบันทึก** ของโค้ดที่รัน
- **ค่าใช้จ่ายโครงสร้างพื้นฐานเพิ่มเติม** เมื่อเทียบกับการเรียกใช้เครื่องมือโดยตรง

ประโยชน์ — ต้นทุน token ที่ลดลง latency ที่ต่ำกว่า การผสมผสานเครื่องมือที่ดีขึ้น — ควรชั่งน้ำหนักกับต้นทุนการดำเนินการเหล่านี้

### MCPorter: Runtime สำหรับการผสมผสาน MCP Tool

[MCPorter](https://github.com/steipete/mcporter) คือ TypeScript runtime และ CLI toolkit ที่ทำให้การเรียกใช้ MCP server เป็นเรื่องง่ายโดยไม่มี boilerplate — และช่วยลด context bloat ผ่านการเปิดเผยเครื่องมือแบบ selective และ wrapper ที่มี type

**สิ่งที่แก้ปัญหา:** แทนที่จะโหลดคำจำกัดความเครื่องมือทั้งหมดจาก MCP server ทั้งหมดล่วงหน้า MCPorter ช่วยให้คุณค้นพบ ตรวจสอบ และเรียกใช้เครื่องมือเฉพาะตามต้องการ — ทำให้ context ของคุณกระชับ

**ฟีเจอร์หลัก:**

| ฟีเจอร์ | คำอธิบาย |
|---------|-------------|
| **Zero-config discovery** | ค้นพบ MCP server โดยอัตโนมัติจาก Cursor, Claude, Codex หรือ local configs |
| **Typed tool clients** | `mcporter emit-ts` สร้าง `.d.ts` interfaces และ wrapper ที่พร้อมรัน |
| **Composable API** | `createServerProxy()` เปิดเผยเครื่องมือเป็นวิธี camelCase พร้อม helper `.text()`, `.json()`, `.markdown()` |
| **CLI generation** | `mcporter generate-cli` แปลง MCP server ใดๆ เป็น CLI standalone พร้อมตัวกรอง `--include-tools` / `--exclude-tools` |
| **Parameter hiding** | พารามิเตอร์ optional ถูกซ่อนไว้เริ่มต้น ลดความยาวของ schema |

**การติดตั้ง:**

```bash
npx mcporter list          # ไม่ต้องติดตั้ง — ค้นพบ server ทันที
pnpm add mcporter          # เพิ่มในโครงการ
brew install steipete/tap/mcporter  # macOS ผ่าน Homebrew
```

**ตัวอย่าง — การผสมผสานเครื่องมือใน TypeScript:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// ข้อมูลไหลระหว่างเครื่องมือโดยไม่ผ่าน context ของโมเดล
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**ตัวอย่าง — การเรียกใช้เครื่องมือ CLI:**

```bash
# เรียกใช้เครื่องมือเฉพาะโดยตรง
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# แสดงรายการ server และเครื่องมือที่พร้อมใช้งาน
npx mcporter list
```

## แนวปฏิบัติที่ดี

### ข้อพิจารณาด้านความปลอดภัย

#### สิ่งที่ควรทำ ✅
- ใช้ environment variables สำหรับ credentials ทั้งหมด
- หมุนเวียน tokens และ API keys เป็นประจำ (แนะนำรายเดือน)
- ใช้ tokens แบบอ่านอย่างเดียวเมื่อเป็นไปได้
- จำกัดขอบเขตการเข้าถึง MCP server ให้น้อยที่สุดที่จำเป็น
- ติดตาม logs การใช้งานและการเข้าถึง MCP server
- ใช้ OAuth สำหรับบริการภายนอกเมื่อพร้อมใช้งาน
- ดำเนินการ rate limiting สำหรับคำขอ MCP
- ทดสอบการเชื่อมต่อ MCP ก่อนการใช้งานจริง
- จัดทำเอกสารการเชื่อมต่อ MCP ที่ใช้งานอยู่ทั้งหมด
- อัปเดต MCP server packages ให้ทันสมัย

#### สิ่งที่ไม่ควรทำ ❌
- อย่า hardcode credentials ในไฟล์กำหนดค่า
- อย่า commit tokens หรือ secrets ไปยัง git
- อย่าแชร์ tokens ในแชทหรืออีเมลของทีม
- อย่าใช้ tokens ส่วนตัวสำหรับโครงการของทีม
- อย่าให้สิทธิ์ที่ไม่จำเป็น
- อย่าละเว้นข้อผิดพลาดการยืนยันตัวตน
- อย่าเปิดเผย MCP endpoints สาธารณะ
- อย่ารัน MCP server ด้วยสิทธิ์ root/admin
- อย่า cache ข้อมูลที่ละเอียดอ่อนใน logs
- อย่าปิดใช้งานกลไกการยืนยันตัวตน

### แนวปฏิบัติที่ดีในการกำหนดค่า

1. **Version Control**: เก็บ `.mcp.json` ใน git แต่ใช้ environment variables สำหรับ secrets
2. **Least Privilege**: ให้สิทธิ์น้อยที่สุดที่จำเป็นสำหรับ MCP server แต่ละตัว
3. **Isolation**: รัน MCP server ต่างๆ ในกระบวนการแยกกันเมื่อเป็นไปได้
4. **Monitoring**: บันทึกคำขอและข้อผิดพลาด MCP ทั้งหมดสำหรับ audit
5. **Testing**: ทดสอบการกำหนดค่า MCP ทั้งหมดก่อน deployment จริง

### เคล็ดลับด้านประสิทธิภาพ

- Cache ข้อมูลที่เข้าถึงบ่อยครั้งในระดับแอปพลิเคชัน
- ใช้คำสืบค้น MCP ที่เจาะจงเพื่อลดการถ่ายโอนข้อมูล
- ติดตามเวลาตอบสนองสำหรับการดำเนินการ MCP
- พิจารณา rate limiting สำหรับ API ภายนอก
- ใช้ batching เมื่อทำหลายการดำเนินการ

## คำแนะนำการติดตั้ง

### ข้อกำหนดเบื้องต้น
- ติดตั้ง Node.js และ npm
- ติดตั้ง Claude Code CLI
- มี API tokens/credentials สำหรับบริการภายนอก

### การตั้งค่าทีละขั้นตอน

1. **เพิ่ม MCP server ตัวแรก** ด้วย CLI (ตัวอย่าง: GitHub):
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

   หรือสร้างไฟล์ `.mcp.json` ในรากของ project:
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

2. **ตั้งค่า environment variables:**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3. **ทดสอบการเชื่อมต่อ:**
```bash
claude /mcp
```

4. **ใช้เครื่องมือ MCP:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### การติดตั้งสำหรับบริการเฉพาะ

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

## การแก้ไขปัญหา

### ไม่พบ MCP Server
```bash
# ตรวจสอบว่าติดตั้ง MCP server แล้ว
npm list -g @modelcontextprotocol/server-github

# ติดตั้งถ้าขาดหายไป
npm install -g @modelcontextprotocol/server-github
```

### การยืนยันตัวตนล้มเหลว
```bash
# ตรวจสอบว่าตั้งค่า environment variable แล้ว
echo $GITHUB_TOKEN

# ส่งออกใหม่ถ้าจำเป็น
export GITHUB_TOKEN="your_token"

# ตรวจสอบว่า token มีสิทธิ์ที่ถูกต้อง
# ตรวจสอบขอบเขต GitHub token ที่: https://github.com/settings/tokens
```

### Connection Timeout
- ตรวจสอบการเชื่อมต่อเครือข่าย: `ping api.github.com`
- ตรวจสอบว่า API endpoint เข้าถึงได้
- ตรวจสอบขีดจำกัด rate ของ API
- ลองเพิ่ม timeout ในการกำหนดค่า
- ตรวจสอบปัญหา firewall หรือ proxy

### MCP Server Crash
- ตรวจสอบ logs ของ MCP server: `~/.claude/logs/`
- ตรวจสอบว่าตั้งค่า environment variables ทั้งหมดแล้ว
- ตรวจสอบสิทธิ์ไฟล์ที่ถูกต้อง
- ลองติดตั้ง MCP server package ใหม่
- ตรวจสอบกระบวนการที่ขัดแย้งบน port เดียวกัน

## แนวคิดที่เกี่ยวข้อง

### Memory vs MCP
- **Memory**: เก็บข้อมูลถาวรที่ไม่เปลี่ยนแปลง (การตั้งค่า context ประวัติ)
- **MCP**: เข้าถึงข้อมูลสดที่เปลี่ยนแปลง (APIs ฐานข้อมูล บริการเรียลไทม์)

### เมื่อควรใช้แต่ละอย่าง
- **ใช้ Memory** สำหรับ: การตั้งค่าผู้ใช้ ประวัติการสนทนา context ที่เรียนรู้
- **ใช้ MCP** สำหรับ: GitHub issues ปัจจุบัน คำสืบค้นฐานข้อมูลสด ข้อมูลเรียลไทม์

### การรวมกับฟีเจอร์ Claude อื่นๆ
- รวม MCP กับ Memory เพื่อ context ที่สมบูรณ์
- ใช้เครื่องมือ MCP ใน prompts เพื่อการใช้เหตุผลที่ดีขึ้น
- ใช้ประโยชน์จาก MCP หลายตัวสำหรับ workflow ที่ซับซ้อน

## แหล่งข้อมูลเพิ่มเติม

- [เอกสาร MCP อย่างเป็นทางการ](https://code.claude.com/docs/en/mcp)
- [ข้อกำหนด MCP Protocol](https://modelcontextprotocol.io/specification)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol/servers)
- [MCP Servers ที่พร้อมใช้งาน](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — TypeScript runtime และ CLI สำหรับการเรียกใช้ MCP server
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — บล็อกวิศวกรรมของ Anthropic เกี่ยวกับการแก้ปัญหา context bloat
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Claude API Documentation](https://docs.anthropic.com)

---

**อัปเดตล่าสุด**: May 6, 2026
**Claude Code Version**: 2.1.131
**แหล่งที่มา**:
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
**โมเดลที่รองรับ**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
