<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

🔌 MCP Protocol（Model Context Protocol）
用途: 外部工具和 API 整合
難度: ⭐⭐ 中級 | 時間: 1 小時

此資料夾包含 MCP 伺服器組態與 Claude Code 搭配使用的完整文件與範例。

## 概述

MCP (Model Context Protocol) 是 Claude 存取外部工具、API 和即時資料來源的標準化方式。與 Memory 不同，MCP 提供對變動資料的即時存取。

主要特性：
- 即時存取外部服務
- 即時資料同步
- 可擴展的架構
- 安全認證
- 基於工具的互動

## MCP 架構

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

## MCP 生態系

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

## MCP 安裝方式

Claude Code 支援多種 MCP 伺服器連線的傳輸協定：

### HTTP 傳輸（推薦）

```bash
# 基本 HTTP 連線
claude mcp add --transport http notion https://mcp.notion.com/mcp

# 帶認證標頭的 HTTP
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Stdio 傳輸（本地）

用於本地執行的 MCP 伺服器：

```bash
# 本地 Node.js 伺服器
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# 帶環境變數
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### SSE 傳輸（已棄用）

Server-Sent Events 傳輸已棄用，建議改用 `http`，但仍受支援：

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### WebSocket 傳輸

WebSocket 傳輸用於持久化的雙向連線：

```bash
claude mcp add --transport ws realtime-server wss://example.com/mcp
```

### Windows 特別說明

在原生 Windows（非 WSL）上，npx 命令需使用 `cmd /c`：

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### OAuth 2.0 認證

Claude Code 支援需要 OAuth 2.0 的 MCP 伺服器。連接到啟用 OAuth 的伺服器時，Claude Code 會處理整個認證流程：

```bash
# 連接到啟用 OAuth 的 MCP 伺服器（互動式流程）
claude mcp add --transport http my-service https://my-service.example.com/mcp

# 為非互動式設定預先設定 OAuth 憑證
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| 功能 | 說明 |
|---------|-------------|
| **互動式 OAuth** | 使用 `/mcp` 觸發基於瀏覽器的 OAuth 流程 |
| **預設定 OAuth 用戶端** | 為 Notion、Stripe 等常見服務內建 OAuth 用戶端（v2.1.30+） |
| **預設定憑證** | `--client-id`、`--client-secret`、`--callback-port` 旗標用於自動化設定 |
| **Token 儲存** | Token 安全儲存在您的系統鑰匙圈中 |
| **階段式認證** | 支援特權操作的階段式認證 |
| **探索快取** | OAuth 探索中繼資料已快取以加速重新連線 |
| **中繼資料覆寫** | `.mcp.json` 中的 `oauth.authServerMetadataUrl` 可覆寫預設 OAuth 中繼資料探索 |

#### 覆寫 OAuth 中繼資料探索

如果您的 MCP 伺服器在標準 OAuth 中繼資料端點（`/.well-known/oauth-authorization-server`）回傳錯誤，但公開了可用的 OIDC 端點，您可以告訴 Claude Code 從特定 URL 取得 OAuth 中繼資料。在伺服器組態的 `oauth` 物件中設定 `authServerMetadataUrl`：

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

URL 必須使用 `https://`。此選項需要 Claude Code v2.1.64 或更新版本。

### Claude.ai MCP 連接器

在 Claude.ai 帳戶中設定的 MCP 伺服器會自動在 Claude Code 中可用。這表示您透過 Claude.ai 網頁介面設定的任何 MCP 連線都可以直接使用，無需額外設定。

Claude.ai MCP 連接器在 `--print` 模式中也可用（v2.1.83+），支援非互動式和腳本化使用。

若要在 Claude Code 中停用 Claude.ai MCP 伺服器，請將 `ENABLE_CLAUDEAI_MCP_SERVERS` 環境變數設為 `false`：

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **注意：** 此功能僅適用於使用 Claude.ai 帳戶登入的使用者。

## MCP 設定流程

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

## MCP 工具搜尋

當 MCP 工具描述超過上下文視窗的 10% 時，Claude Code 會自動啟用工具搜尋，以有效率地選擇正確的工具，而不會使模型上下文過載。

| 設定 | 值 | 說明 |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | `auto`（預設） | 當工具描述超過上下文的 10% 時自動啟用 |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | 在自訂閾值 `N` 個工具時自動啟用 |
| `ENABLE_TOOL_SEARCH` | `true` | 無論工具數量多少，總是啟用 |
| `ENABLE_TOOL_SEARCH` | `false` | 停用；所有工具描述完整發送 |

> **注意：** 工具搜尋需要 Sonnet 4 或更新版本，或 Opus 4 或更新版本。Haiku 模型不支援工具搜尋。

## 動態工具更新

Claude Code 支援 MCP `list_changed` 通知。當 MCP 伺服器動態新增、移除或修改其可用工具時，Claude Code 會接收更新並自動調整其工具列表 -- 無需重新連線或重新啟動。

## MCP 引出

MCP 伺服器可以透過互動式對話框向使用者請求結構化輸入（v2.1.49+）。這允許 MCP 伺服器在工作流程中途要求額外資訊 -- 例如，提示確認、從選項列表中選擇，或填寫必填欄位 -- 為 MCP 伺服器互動增添互動性。

## 工具描述與指令上限

自 v2.1.84 起，Claude Code 對每個 MCP 伺服器的工具描述和指令強制執行 **2 KB 上限**。這防止個別伺服器以過於冗長的工具定義消耗過多上下文，減少上下文膨脹並保持互動效率。

## MCP Prompts 作為 Slash Commands

MCP 伺服器可以公開以 slash commands 形式出現在 Claude Code 中的 prompts。Prompts 使用以下命名慣例存取：

```
/mcp__<server>__<prompt>
```

例如，如果名為 `github` 的伺服器公開了名為 `review` 的 prompt，您可以用 `/mcp__github__review` 來呼叫它。

## 伺服器去重

當相同的 MCP 伺服器在多個範圍（local、project、user）定義時，local 組態優先。這讓您可以用本地自訂設定覆寫專案級或使用者級的 MCP 設定，而不會產生衝突。

## MCP 資源透過 @ 提及

您可以使用 `@` 提及語法直接在提示中參照 MCP 資源：

```
@server-name:protocol://resource/path
```

例如，參照特定資料庫資源：

```
@database:postgres://mydb/users
```

這讓 Claude 可以取得並包含 MCP 資源內容作為對話上下文的一部分。

## MCP 範圍

MCP 組態可以儲存在不同範圍，具有不同的共享層級：

| 範圍 | 位置 | 說明 | 共享對象 | 需要核准 |
|-------|----------|-------------|-------------|------------------|
| **Local**（預設） | `~/.claude.json`（專案路徑下） | 僅限目前使用者、目前專案（舊版本稱為 `project`） | 僅您自己 | 否 |
| **Project** | `.mcp.json` | 簽入 git 儲存庫 | 團隊成員 | 是（首次使用） |
| **User** | `~/.claude.json` | 跨所有專案可用（舊版本稱為 `global`） | 僅您自己 | 否 |

### 使用 Project 範圍

在 `.mcp.json` 中儲存專案特定的 MCP 組態：

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

團隊成員在首次使用 project MCPs 時會看到核准提示。

## MCP 組態管理

### 新增 MCP 伺服器

```bash
# 新增基於 HTTP 的伺服器
claude mcp add --transport http github https://api.github.com/mcp

# 新增本地 stdio 伺服器
claude mcp add --transport stdio database -- npx @company/db-server

# 列出所有 MCP 伺服器
claude mcp list

# 取得特定伺服器的詳細資訊
claude mcp get github

# 移除 MCP 伺服器
claude mcp remove github

# 重設專案特定的核准選擇
claude mcp reset-project-choices

# 從 Claude Desktop 匯入
claude mcp add-from-claude-desktop
```

## 可用的 MCP 伺服器一覽

| MCP 伺服器 | 用途 | 常用工具 | 認證 | 即時 |
|------------|---------|--------------|------|-----------|
| **Filesystem** | 檔案操作 | read、write、delete | 作業系統權限 | ✅ 是 |
| **GitHub** | 儲存庫管理 | list_prs、create_issue、push | OAuth | ✅ 是 |
| **Slack** | 團隊通訊 | send_message、list_channels | Token | ✅ 是 |
| **Database** | SQL 查詢 | query、insert、update | 憑證 | ✅ 是 |
| **Google Docs** | 文件存取 | read、write、share | OAuth | ✅ 是 |
| **Asana** | 專案管理 | create_task、update_status | API Key | ✅ 是 |
| **Stripe** | 支付資料 | list_charges、create_invoice | API Key | ✅ 是 |
| **Memory** | 持久記憶 | store、retrieve、delete | 本地 | ❌ 否 |

## 實用範例

### 範例 1：GitHub MCP 組態

**檔案：** `.mcp.json`（專案根目錄）

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

**可用的 GitHub MCP 工具：**

#### Pull Request 管理
- `list_prs` - 列出儲存庫中的所有 PR
- `get_pr` - 取得 PR 詳情，包含 diff
- `create_pr` - 建立新 PR
- `update_pr` - 更新 PR 說明/標題
- `merge_pr` - 合併 PR 至主分支
- `review_pr` - 新增審查評論

**請求範例：**
```
/mcp__github__get_pr 456

# 回傳：
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### Issue 管理
- `list_issues` - 列出所有 issues
- `get_issue` - 取得 issue 詳情
- `create_issue` - 建立新 issue
- `close_issue` - 關閉 issue
- `add_comment` - 新增 issue 評論

#### 儲存庫資訊
- `get_repo_info` - 儲存庫詳情
- `list_files` - 檔案樹狀結構
- `get_file_content` - 讀取檔案內容
- `search_code` - 搜尋整個程式碼庫

#### Commit 操作
- `list_commits` - Commit 歷史
- `get_commit` - 特定 commit 詳情
- `create_commit` - 建立新 commit

**設定**：
```bash
export GITHUB_TOKEN="your_github_token"
# 或使用 CLI 直接新增：
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### 組態中的環境變數擴展

MCP 組態支援帶備用預設值的環境變數擴展。`${VAR}` 和 `${VAR:-default}` 語法適用於以下欄位：`command`、`args`、`env`、`url` 和 `headers`。

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

變數在執行時擴展：
- `${VAR}` - 使用環境變數，若未設定則報錯
- `${VAR:-default}` - 使用環境變數，若未設定則退回預設值

### 範例 2：Database MCP 設定

**組態：**

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

**使用範例：**

```markdown
使用者：找出訂單超過 10 筆的所有使用者

Claude：我將查詢您的資料庫來找出該資訊。

# 使用 MCP 資料庫工具：
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# 結果：
- Alice：15 筆訂單
- Bob：12 筆訂單
- Charlie：11 筆訂單
```

**設定**：
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# 或使用 CLI 直接新增：
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

### 範例 3：多 MCP 工作流程

**情境：每日報表產生**

```markdown
# 使用多個 MCPs 的每日報表工作流程

## 設定
1. GitHub MCP - 取得 PR 指標
2. Database MCP - 查詢銷售資料
3. Slack MCP - 發布報表
4. Filesystem MCP - 儲存報表

## 工作流程

### 步驟 1：取得 GitHub 資料
/mcp__github__list_prs completed:true last:7days

輸出：
- PR 總數：42
- 平均合併時間：2.3 小時
- 審查週轉時間：1.1 小時

### 步驟 2：查詢資料庫
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

輸出：
- 銷售：247
- 營收：$12,450

### 步驟 3：產生報表
將資料合併為 HTML 報表

### 步驟 4：儲存至檔案系統
將 report.html 寫入 /reports/

### 步驟 5：發布至 Slack
將摘要發送到 #daily-reports 頻道

最終輸出：
✅ 報表已產生並發布
📊 本週合併 47 個 PR
💰 每日銷售 $12,450
```

**設定**：
```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
# 透過 CLI 新增每個 MCP 伺服器或在 .mcp.json 中設定
```

### 範例 4：Filesystem MCP 操作

**組態：**

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

**可用操作：**

| 操作 | 命令 | 用途 |
|-----------|---------|---------|
| 列出檔案 | `ls ~/projects` | 顯示目錄內容 |
| 讀取檔案 | `cat src/main.ts` | 讀取檔案內容 |
| 寫入檔案 | `create docs/api.md` | 建立新檔案 |
| 編輯檔案 | `edit src/app.ts` | 修改檔案 |
| 搜尋 | `grep "async function"` | 在檔案中搜尋 |
| 刪除 | `rm old-file.js` | 刪除檔案 |

**設定**：
```bash
# 使用 CLI 直接新增：
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## MCP 與 Memory：決策矩陣

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

## 請求/回應模式

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

## 環境變數

將敏感憑證儲存在環境變數中：

```bash
# ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

然後在 MCP 組態中參照它們：

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Claude 作為 MCP 伺服器（`claude mcp serve`）

Claude Code 本身可以作為其他應用程式的 MCP 伺服器。這讓外部工具、編輯器和自動化系統可以透過標準 MCP 協定利用 Claude 的能力。

```bash
# 在 stdio 上啟動 Claude Code 作為 MCP 伺服器
claude mcp serve
```

其他應用程式可以像連接任何基於 stdio 的 MCP 伺服器一樣連接到此伺服器。例如，在另一個 Claude Code 實例中將 Claude Code 新增為 MCP 伺服器：

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

這對於建構一個 Claude 實例協調另一個的多代理工作流程很有用。

## 受管 MCP 組態（企業版）

對於企業部署，IT 管理員可以透過 `managed-mcp.json` 組態檔案強制執行 MCP 伺服器策略。此檔案提供對整個組織允許或阻擋哪些 MCP 伺服器的獨佔控制。

**位置：**
- macOS：`/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux：`~/.config/ClaudeCode/managed-mcp.json`
- Windows：`%APPDATA%\ClaudeCode\managed-mcp.json`

**功能：**
- `allowedMcpServers` -- 允許的伺服器白名單
- `deniedMcpServers` -- 禁止的伺服器黑名單
- 支援按伺服器名稱、命令和 URL 模式比對
- 在使用者組態之前強制執行全組織 MCP 策略
- 防止未授權的伺服器連線

**組態範例：**

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

> **注意：** 當 `allowedMcpServers` 和 `deniedMcpServers` 同時匹配一個伺服器時，拒絕規則優先。

## Plugin 提供的 MCP 伺服器

Plugins 可以打包自己的 MCP 伺服器，使其在安裝 plugin 時自動可用。Plugin 提供的 MCP 伺服器可以用兩種方式定義：

1. **獨立 `.mcp.json`** -- 在 plugin 根目錄放置 `.mcp.json` 檔案
2. **內嵌在 `plugin.json`** -- 直接在 plugin 清單中定義 MCP 伺服器

使用 `${CLAUDE_PLUGIN_ROOT}` 變數來參照相對於 plugin 安裝目錄的路徑：

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

## Subagent 範圍的 MCP

MCP 伺服器可以在 agent frontmatter 中使用 `mcpServers:` 鍵內嵌定義，將其範圍限定在特定 subagent 而非整個專案。當某個 agent 需要存取工作流程中其他 agent 不需要的特定 MCP 伺服器時，這很有用。

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

Subagent 範圍的 MCP 伺服器僅在該 agent 的執行上下文中可用，不會與父代或同級 agent 共享。

## MCP 輸出限制

Claude Code 對 MCP 工具輸出強制執行限制以防止上下文溢出：

| 限制 | 閾值 | 行為 |
|-------|-----------|----------|
| **警告** | 10,000 tokens | 顯示輸出很大的警告 |
| **預設最大值** | 25,000 tokens | 超過此限制的輸出會被截斷 |
| **磁碟持久化** | 50,000 字元 | 超過 50K 字元的工具結果會持久化到磁碟 |

最大輸出限制可透過 `MAX_MCP_OUTPUT_TOKENS` 環境變數設定：

```bash
# 將最大輸出增加到 50,000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## 用程式碼執行解決上下文膨脹

隨著 MCP 採用規模擴大，連接數十個伺服器及數百或數千個工具會產生一個重大挑戰：**上下文膨脹**。這可以說是大規模 MCP 面臨的最大問題，而 Anthropic 的工程團隊提出了一個優雅的解決方案 — 使用程式碼執行取代直接工具呼叫。

> **來源**：[Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic 工程部落格

### 問題：兩個 Token 浪費來源

**1. 工具定義使上下文視窗過載**

大多數 MCP 用戶端會預先載入所有工具定義。當連接到數千個工具時，模型在讀取使用者請求之前必須處理數十萬個 tokens。

**2. 中間結果消耗額外的 tokens**

每個中間工具結果都會通過模型的上下文。考慮將會議紀錄從 Google Drive 傳輸到 Salesforce — 完整的紀錄會通過上下文**兩次**：一次讀取，一次寫入目標。一個 2 小時的會議紀錄可能意味著 50,000+ 額外的 tokens。

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### 解決方案：MCP 工具作為程式碼 API

不再將工具定義和結果通過上下文視窗傳遞，agent **撰寫程式碼**將 MCP 工具當作 API 呼叫。程式碼在沙箱執行環境中執行，只有最終結果返回模型。

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

#### 運作原理

MCP 工具呈現為類型化函式的檔案樹：

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

每個工具檔案包含一個類型化的包裝器：

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

然後 agent 撰寫程式碼來協調工具：

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// 資料直接在工具之間流動 — 絕不通過模型
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**結果：Token 使用從約 150,000 降至約 2,000 — 減少 98.7%。**

### 主要優勢

| 優勢 | 說明 |
|---------|-------------|
| **漸進式揭露** | Agent 瀏覽檔案系統以僅載入需要的工具定義，而非預先載入所有工具 |
| **上下文高效的結果** | 資料在返回模型前在執行環境中被篩選/轉換 |
| **強大的控制流程** | 迴圈、條件判斷和錯誤處理在程式碼中執行，無需通過模型往返 |
| **隱私保護** | 中間資料（個人識別資訊、敏感記錄）留在執行環境中；永不進入模型上下文 |
| **狀態持久化** | Agent 可以將中間結果儲存至檔案並建構可重用的技能函式 |

#### 範例：篩選大型資料集

```typescript
// 不使用程式碼執行 — 所有 10,000 行都通過上下文
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> 在上下文中返回 10,000 行

// 使用程式碼執行 — 在執行環境中篩選
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // 僅 5 行到達模型
```

#### 範例：無需往返的迴圈

```typescript
// 輪詢部署通知 — 完全在程式碼中執行
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

### 需要考量的取捨

程式碼執行引入了自身的複雜性。執行 agent 產生的程式碼需要：

- 具有適當資源限制的**安全沙箱執行環境**
- 已執行程式碼的**監控與日誌**
- 相較於直接工具呼叫的額外**基礎設施開銷**

這些優勢 — 降低 token 成本、降低延遲、改善工具組合 — 應與這些實作成本權衡。對於只有少數 MCP 伺服器的 agent，直接工具呼叫可能更簡單。對於大規模的 agent（數十個伺服器、數百個工具），程式碼執行是一個顯著的改善。

### MCPorter：MCP 工具組合的執行時

[MCPorter](https://github.com/steipete/mcporter) 是一個 TypeScript 執行時和 CLI 工具套件，讓呼叫 MCP 伺服器無需樣板程式碼變得實用 — 並透過選擇性工具曝露和類型化包裝器幫助減少上下文膨脹。

**它解決什麼問題：** MCPorter 讓您可以按需發現、檢查和呼叫特定工具，而不是預先從所有 MCP 伺服器載入所有工具定義 — 保持您的上下文精簡。

**主要功能：**

| 功能 | 說明 |
|---------|-------------|
| **零設定探索** | 從 Cursor、Claude、Codex 或本地組態自動發現 MCP 伺服器 |
| **類型化工具用戶端** | `mcporter emit-ts` 產生 `.d.ts` 介面和即用的包裝器 |
| **可組合 API** | `createServerProxy()` 將工具公開為駝峰式命名方法，帶有 `.text()`、`.json()`、`.markdown()` 輔助方法 |
| **CLI 產生** | `mcporter generate-cli` 將任何 MCP 伺服器轉換為獨立 CLI，帶有 `--include-tools` / `--exclude-tools` 篩選 |
| **參數隱藏** | 預設隱藏可選參數，減少結構描述的冗長度 |

**安裝：**

```bash
npx mcporter list          # 無需安裝 — 即時發現伺服器
pnpm add mcporter          # 新增至專案
brew install steipete/tap/mcporter  # macOS 透過 Homebrew
```

**範例 — 在 TypeScript 中組合工具：**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// 資料在工具之間流動而不通過模型上下文
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**範例 — CLI 工具呼叫：**

```bash
# 直接呼叫特定工具
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# 列出可用的伺服器和工具
npx mcporter list
```

MCPorter 透過提供呼叫 MCP 工具作為類型化 API 的執行時基礎設施，補充了上述程式碼執行方法 — 讓中間資料不進入模型上下文變得簡單明瞭。

## 最佳實踐

### 安全考量

#### 建議做法 ✅
- 所有憑證使用環境變數
- 定期輪換 token 和 API 金鑰（建議每月）
- 盡可能使用唯讀 token
- 將 MCP 伺服器存取範圍限制在最低所需
- 監控 MCP 伺服器使用和存取日誌
- 可用時使用 OAuth 進行外部服務認證
- 對 MCP 請求實施速率限制
- 生產使用前測試 MCP 連線
- 記錄所有活躍的 MCP 連線
- 保持 MCP 伺服器套件更新

#### 不建議做法 ❌
- 不要在組態檔案中硬編碼憑證
- 不要將 token 或機密提交至 git
- 不要在團隊聊天或電子郵件中分享 token
- 不要對團隊專案使用個人 token
- 不要授予不必要的權限
- 不要忽略認證錯誤
- 不要公開曝露 MCP 端點
- 不要以 root/管理員權限執行 MCP 伺服器
- 不要在日誌中快取敏感資料
- 不要停用認證機制

### 組態最佳實踐

1. **版本控制**：將 `.mcp.json` 保留在 git 中，但對機密使用環境變數
2. **最小權限**：為每個 MCP 伺服器授予最低所需權限
3. **隔離**：盡可能在不同程序中執行不同的 MCP 伺服器
4. **監控**：記錄所有 MCP 請求和錯誤以供稽核
5. **測試**：在部署至生產環境前測試所有 MCP 組態

### 效能提示

- 在應用程式層級快取頻繁存取的資料
- 使用具體的 MCP 查詢以減少資料傳輸
- 監控 MCP 操作的回應時間
- 考慮外部 API 的速率限制
- 執行多個操作時使用批次處理

## 安裝指引

### 先決條件
- 已安裝 Node.js 和 npm
- 已安裝 Claude Code CLI
- 外部服務的 API token/憑證

### 逐步設定

1. **使用 CLI 新增您的第一個 MCP 伺服器**（範例：GitHub）：
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

   或在專案根目錄建立 `.mcp.json` 檔案：
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

2. **設定環境變數：**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3. **測試連線：**
```bash
claude /mcp
```

4. **使用 MCP 工具：**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### 特定服務的安裝

**GitHub MCP：**
```bash
npm install -g @modelcontextprotocol/server-github
```

**Database MCP：**
```bash
npm install -g @modelcontextprotocol/server-database
```

**Filesystem MCP：**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP：**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## 疑難排解

### MCP 伺服器未找到
```bash
# 驗證 MCP 伺服器已安裝
npm list -g @modelcontextprotocol/server-github

# 若未安裝則安裝
npm install -g @modelcontextprotocol/server-github
```

### 認證失敗
```bash
# 驗證環境變數已設定
echo $GITHUB_TOKEN

# 若需要則重新匯出
export GITHUB_TOKEN="your_token"

# 驗證 token 有正確的權限
# 在此檢查 GitHub token 範圍：https://github.com/settings/tokens
```

### 連線逾時
- 檢查網路連線：`ping api.github.com`
- 驗證 API 端點可存取
- 檢查 API 的速率限制
- 嘗試在組態中增加逾時
- 檢查防火牆或代理問題

### MCP 伺服器當機
- 檢查 MCP 伺服器日誌：`~/.claude/logs/`
- 驗證所有環境變數已設定
- 確保正確的檔案權限
- 嘗試重新安裝 MCP 伺服器套件
- 檢查同一連接埠上是否有衝突的程序

## 相關概念

### Memory 與 MCP
- **Memory**：儲存持久的、不變的資料（偏好設定、上下文、歷史）
- **MCP**：存取即時的、變動的資料（API、資料庫、即時服務）

### 何時使用哪個
- **使用 Memory**：使用者偏好設定、對話歷史、已學習的上下文
- **使用 MCP**：目前的 GitHub issues、即時資料庫查詢、即時資料

### 與其他 Claude 功能的整合
- 將 MCP 與 Memory 結合以獲得豐富的上下文
- 在提示中使用 MCP 工具以改善推理
- 利用多個 MCPs 進行複雜的工作流程

## 額外資源

- [官方 MCP 文件](https://code.claude.com/docs/en/mcp)
- [MCP 協定規範](https://modelcontextprotocol.io/specification)
- [MCP GitHub 儲存庫](https://github.com/modelcontextprotocol/servers)
- [可用的 MCP 伺服器](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — 用於呼叫 MCP 伺服器無需樣板程式碼的 TypeScript 執行時和 CLI
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic 工程部落格關於解決上下文膨脹的文章
- [Claude Code CLI 參考](https://code.claude.com/docs/en/cli-reference)
- [Claude API 文件](https://docs.anthropic.com)
