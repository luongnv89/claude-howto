<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP（Model Context Protocol）

本目录包含 Claude Code 中 MCP server 配置与使用的完整文档和示例。

## Overview

MCP（Model Context Protocol）是 Claude 访问外部工具、API 和实时数据源的标准化协议。与 Memory 不同，MCP 提供的是对变化数据的实时访问能力。

核心特性：
- 实时访问外部服务
- 实时数据同步
- 可扩展架构
- 安全认证机制
- 基于工具的交互模式

## MCP Architecture

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

## MCP Ecosystem

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

## MCP Installation Methods

Claude Code 支持多种 MCP server 传输协议：

### HTTP Transport（推荐）

```bash
# 基础 HTTP 连接
claude mcp add --transport http notion https://mcp.notion.com/mcp

# 带认证头的 HTTP
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Stdio Transport（本地）

用于本地运行的 MCP servers：

```bash
# 本地 Node.js server
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# 附带环境变量
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### SSE Transport（已弃用）

SSE 已被 `http` 取代，但仍可使用：

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### WebSocket Transport

用于持久双向连接：

```bash
claude mcp add --transport ws realtime-server wss://example.com/mcp
```

### Windows 注意事项

在原生 Windows（非 WSL）中，`npx` 命令需通过 `cmd /c`：

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### OAuth 2.0 Authentication

Claude Code 支持 OAuth 2.0 MCP server。连接 OAuth server 时，Claude Code 可处理整套认证流程：

```bash
# 连接支持 OAuth 的 MCP server（交互式流程）
claude mcp add --transport http my-service https://my-service.example.com/mcp

# 预配置 OAuth 凭据（非交互式）
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| Feature | Description |
|---------|-------------|
| **Interactive OAuth** | 使用 `/mcp` 触发浏览器 OAuth 流程 |
| **Pre-configured OAuth clients** | 内置常见服务 OAuth client（如 Notion、Stripe，v2.1.30+） |
| **Pre-configured credentials** | 通过 `--client-id`、`--client-secret`、`--callback-port` 自动化配置 |
| **Token storage** | token 安全存储在系统 keychain |
| **Step-up auth** | 支持高权限操作的阶梯认证 |
| **Discovery caching** | OAuth discovery 元数据缓存，加速重连 |
| **Metadata override** | 在 `.mcp.json` 通过 `oauth.authServerMetadataUrl` 覆盖默认发现地址 |

#### Overriding OAuth Metadata Discovery

如果 MCP server 在标准 OAuth metadata 端点（`/.well-known/oauth-authorization-server`）报错，但提供了可用 OIDC 端点，可在 server 配置 `oauth` 中设置 `authServerMetadataUrl`：

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

该 URL 必须使用 `https://`。该能力需要 Claude Code v2.1.64+。

### Claude.ai MCP Connectors

在 Claude.ai 账号中配置的 MCP servers 会自动出现在 Claude Code 中。即你在 Claude.ai Web 端配置的连接，无需额外配置即可在 CLI 使用。

Claude.ai MCP connectors 也支持 `--print` 模式（v2.1.83+），便于非交互和脚本化场景。

若需禁用 Claude.ai MCP servers，可设置环境变量 `ENABLE_CLAUDEAI_MCP_SERVERS=false`：

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **Note:** 此功能仅对使用 Claude.ai 账号登录的用户可用。

## MCP Setup Process

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

## MCP Tool Search

当 MCP 工具描述总量超过上下文窗口 10% 时，Claude Code 会自动启用 tool search，以避免上下文被工具描述淹没。

| Setting | Value | Description |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | `auto`（默认） | 工具描述超过上下文 10% 自动启用 |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | 工具数量达到 `N` 时自动启用 |
| `ENABLE_TOOL_SEARCH` | `true` | 始终启用 |
| `ENABLE_TOOL_SEARCH` | `false` | 关闭；全部工具描述完整注入上下文 |

> **Note:** tool search 需 Sonnet 4+ 或 Opus 4+。Haiku 不支持。

## Dynamic Tool Updates

Claude Code 支持 MCP `list_changed` 通知。MCP server 动态增删改工具时，Claude Code 会自动更新工具列表，无需重连或重启。

## MCP Elicitation

MCP server 可通过交互对话请求结构化用户输入（v2.1.49+）。例如流程中临时请求确认、让用户选择选项、填写必要字段等。

## Tool Description and Instruction Cap

从 v2.1.84 起，Claude Code 对每个 MCP server 的工具描述与说明施加 **2 KB 上限**，避免单个 server 以冗长定义消耗过多上下文。

## MCP Prompts as Slash Commands

MCP server 可暴露 prompts，并在 Claude Code 中作为 slash commands 使用，命名格式：

```text
/mcp__<server>__<prompt>
```

例如 `github` server 暴露了 `review` prompt，可通过 `/mcp__github__review` 调用。

## Server Deduplication

同一 MCP server 若在 local/project/user 多层重复定义，local 配置优先。可借此用本地配置覆盖团队或全局配置。

## MCP Resources via @ Mentions

可在 prompt 里通过 `@` 直接引用 MCP 资源：

```text
@server-name:protocol://resource/path
```

例如：

```text
@database:postgres://mydb/users
```

Claude 会拉取该资源内容并注入当前上下文。

## MCP Scopes

MCP 配置支持多作用域，分享范围不同：

| Scope | Location | Description | Shared With | Requires Approval |
|-------|----------|-------------|-------------|------------------|
| **Local**（默认） | `~/.claude.json`（按项目路径存储） | 当前用户、当前项目私有（旧版名 `project`） | 仅自己 | No |
| **Project** | `.mcp.json` | 提交到 git 仓库 | 团队成员 | Yes（首次使用） |
| **User** | `~/.claude.json` | 跨项目可用（旧版名 `global`） | 仅自己 | No |

### Using Project Scope

将项目级 MCP 配置写入 `.mcp.json`：

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

团队成员首次使用项目 MCP 时会看到审批提示。

## MCP Configuration Management

### Adding MCP Servers

```bash
# 添加 HTTP server
claude mcp add --transport http github https://api.github.com/mcp

# 添加本地 stdio server
claude mcp add --transport stdio database -- npx @company/db-server

# 列出所有 MCP servers
claude mcp list

# 查看单个 server 详情
claude mcp get github

# 删除 MCP server
claude mcp remove github

# 重置项目级审批选择
claude mcp reset-project-choices

# 从 Claude Desktop 导入
claude mcp add-from-claude-desktop
```

## Available MCP Servers Table

| MCP Server | Purpose | Common Tools | Auth | Real-time |
|------------|---------|--------------|------|-----------|
| **Filesystem** | 文件操作 | read, write, delete | OS permissions | ✅ Yes |
| **GitHub** | 仓库管理 | list_prs, create_issue, push | OAuth | ✅ Yes |
| **Slack** | 团队沟通 | send_message, list_channels | Token | ✅ Yes |
| **Database** | SQL 查询 | query, insert, update | Credentials | ✅ Yes |
| **Google Docs** | 文档访问 | read, write, share | OAuth | ✅ Yes |
| **Asana** | 项目管理 | create_task, update_status | API Key | ✅ Yes |
| **Stripe** | 支付数据 | list_charges, create_invoice | API Key | ✅ Yes |
| **Memory** | 持久记忆 | store, retrieve, delete | Local | ❌ No |

## Practical Examples

### Example 1: GitHub MCP Configuration

**File:** `.mcp.json`（项目根目录）

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

**Available GitHub MCP Tools:**

#### Pull Request Management
- `list_prs` - 列出仓库 PR
- `get_pr` - 获取 PR 详情和 diff
- `create_pr` - 创建 PR
- `update_pr` - 更新 PR 标题/描述
- `merge_pr` - 合并 PR
- `review_pr` - 添加 review 评论

**Example request:**

```text
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### Issue Management
- `list_issues` - 列出 issues
- `get_issue` - 获取 issue 详情
- `create_issue` - 创建 issue
- `close_issue` - 关闭 issue
- `add_comment` - issue 加评论

#### Repository Information
- `get_repo_info` - 仓库详情
- `list_files` - 文件树
- `get_file_content` - 读取文件
- `search_code` - 代码搜索

#### Commit Operations
- `list_commits` - 提交历史
- `get_commit` - 指定提交详情
- `create_commit` - 创建提交

**Setup**：

```bash
export GITHUB_TOKEN="your_github_token"
# 或直接 CLI 添加：
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### Environment Variable Expansion in Configuration

MCP 配置支持环境变量展开与默认值回退。`${VAR}` 与 `${VAR:-default}` 可用于 `command`、`args`、`env`、`url`、`headers`。

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

变量展开规则：
- `${VAR}`：读取环境变量，未设置时报错
- `${VAR:-default}`：未设置时使用默认值

### Example 2: Database MCP Setup

**Configuration:**

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

**Example Usage:**

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

**Setup**：

```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# 或直接 CLI 添加：
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

### Example 3: Multi-MCP Workflow

**Scenario: Daily Report Generation**

```markdown
# Daily Report Workflow using Multiple MCPs

## Setup
1. GitHub MCP - fetch PR metrics
2. Database MCP - query sales data
3. Slack MCP - post report
4. Filesystem MCP - save report

## Workflow

### Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Step 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Step 3: Generate Report
Combine data into HTML report

### Step 4: Save to Filesystem
Write report.html to /reports/

### Step 5: Post to Slack
Send summary to #daily-reports channel

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

**Setup**：

```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
# 通过 CLI 添加对应 MCP server，或写入 .mcp.json
```

### Example 4: Filesystem MCP Operations

**Configuration:**

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

**Available Operations:**

| Operation | Command | Purpose |
|-----------|---------|---------|
| List files | `ls ~/projects` | 查看目录内容 |
| Read file | `cat src/main.ts` | 读取文件 |
| Write file | `create docs/api.md` | 创建文件 |
| Edit file | `edit src/app.ts` | 修改文件 |
| Search | `grep "async function"` | 文件内搜索 |
| Delete | `rm old-file.js` | 删除文件 |

**Setup**：

```bash
# 直接用 CLI 添加：
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## MCP vs Memory: Decision Matrix

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

## Request/Response Pattern

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

将敏感凭据存到环境变量：

```bash
# ~/.bashrc 或 ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

然后在 MCP 配置中引用：

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Claude as MCP Server（`claude mcp serve`）

Claude Code 本身可以作为 MCP server 提供给其他应用使用。外部工具、编辑器和自动化系统可通过标准 MCP 协议调用 Claude 能力。

```bash
# 以 stdio 启动 Claude Code MCP server
claude mcp serve
```

其他应用可像连接普通 stdio MCP server 一样连接它。比如在另一个 Claude Code 实例中接入：

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

适合多 agent 编排：一个 Claude 实例调度另一个 Claude 实例。

## Managed MCP Configuration（Enterprise）

企业场景可通过 `managed-mcp.json` 统一管控 MCP server 策略，集中定义允许/禁止列表。

**Location:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**Features:**
- `allowedMcpServers`：允许名单
- `deniedMcpServers`：禁止名单
- 支持按 server 名、命令、URL 模式匹配
- 在用户配置前先执行组织策略
- 阻止未授权 server 连接

**Example configuration:**

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

> **Note:** 当 `allowedMcpServers` 与 `deniedMcpServers` 同时命中时，deny 优先。

## Plugin-Provided MCP Servers

插件可内置自己的 MCP servers，安装插件后自动可用。定义方式有两种：

1. **独立 `.mcp.json`**：放在插件根目录
2. **`plugin.json` 内联定义**：直接写在插件清单里

可使用 `${CLAUDE_PLUGIN_ROOT}` 引用插件安装目录下路径：

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

## Subagent-Scoped MCP

可在 agent frontmatter 用 `mcpServers:` 内联定义 MCP server，使其仅对该 subagent 生效，而非全项目共享。

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

这种 MCP 只在该 agent 执行上下文可见，不会共享给父 agent 或 sibling agents。

## MCP Output Limits

Claude Code 对 MCP 工具输出设有限制，防止上下文溢出：

| Limit | Threshold | Behavior |
|-------|-----------|----------|
| **Warning** | 10,000 tokens | 提示输出过大 |
| **Default max** | 25,000 tokens | 超出部分截断 |
| **Disk persistence** | 50,000 characters | 超过 50K 字符会落盘 |

最大输出可通过环境变量 `MAX_MCP_OUTPUT_TOKENS` 调整：

```bash
# 提高上限到 50,000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## Solving Context Bloat with Code Execution

随着 MCP 接入规模扩大（几十个 server、上千工具），会遇到核心问题：**context bloat（上下文膨胀）**。Anthropic 给出的解法是：用代码执行替代直接工具调用。

> **Source**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp)

### The Problem: Two Sources of Token Waste

**1）工具定义占满上下文窗口**

多数 MCP 客户端会一次加载全部工具定义。连接上千工具时，用户请求还没读到，模型上下文已消耗大量 tokens。

**2）中间结果重复消耗 tokens**

每个中间工具结果都要经过模型上下文。比如把 Google Drive 会议纪要转存 Salesforce，完整文本可能在上下文中流过两次。2 小时会议纪要可能额外产生 50,000+ tokens。

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### The Solution: MCP Tools as Code APIs

做法是：不是把工具定义与结果都塞进上下文，而是让 agent **写代码** 调用 MCP 工具 API。代码在沙箱执行环境运行，模型只接收最终结果。

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

#### How It Works

MCP 工具以“带类型函数文件树”的形式暴露：

```text
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

每个工具文件都是类型化包装：

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

然后 agent 写编排代码调用工具：

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// 数据在工具间直接流动，不经过模型上下文
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**结果：token 用量可从约 150,000 降到约 2,000（降低 98.7%）。**

### Key Benefits

| Benefit | Description |
|---------|-------------|
| **Progressive Disclosure** | 仅按需加载必要工具定义，而非全部预加载 |
| **Context-Efficient Results** | 在执行环境先过滤/转换数据，再回传模型 |
| **Powerful Control Flow** | 循环、分支、错误处理在代码中完成，减少模型往返 |
| **Privacy Preservation** | 中间敏感数据留在执行环境，不进入模型上下文 |
| **State Persistence** | 可把中间结果落盘，并复用为技能函数 |

#### Example: Filtering Large Datasets

```typescript
// 不用代码执行：1万行都进上下文
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> returns 10,000 rows in context

// 用代码执行：在执行环境先过滤
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // 只有5行回到模型
```

#### Example: Loop Without Round-Tripping

```typescript
// 轮询部署通知：全部在代码环境执行
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

### Trade-offs to Consider

代码执行也带来额外复杂度：
- 需要安全沙箱执行环境与资源限制
- 需要执行代码的监控与日志
- 基础设施开销高于直接工具调用

是否采用需按规模权衡：
- 小规模（少量 MCP servers）→ 直接工具调用更简单
- 大规模（几十 servers、上百工具）→ 代码执行收益显著

### MCPorter: A Runtime for MCP Tool Composition

[MCPorter](https://github.com/steipete/mcporter) 是 TypeScript runtime + CLI，可在几乎无样板代码下调用 MCP servers，并通过按需暴露工具与类型包装减少 context bloat。

**它解决的问题：** 不再一次加载所有工具定义，而是按需发现、检查、调用具体工具，保持上下文精简。

**Key features:**

| Feature | Description |
|---------|-------------|
| **Zero-config discovery** | 自动发现 Cursor、Claude、Codex 或本地配置中的 MCP servers |
| **Typed tool clients** | `mcporter emit-ts` 生成 `.d.ts` 与可运行 wrapper |
| **Composable API** | `createServerProxy()` 以 camelCase 暴露工具，并提供 `.text()` / `.json()` / `.markdown()` |
| **CLI generation** | `mcporter generate-cli` 可把 MCP server 生成独立 CLI，支持 `--include-tools` / `--exclude-tools` |
| **Parameter hiding** | 默认隐藏可选参数，减少 schema 噪声 |

**Installation:**

```bash
npx mcporter list          # 无需安装，直接发现 servers
pnpm add mcporter          # 加入项目依赖
brew install steipete/tap/mcporter  # macOS (Homebrew)
```

**Example — TypeScript 工具编排：**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// 数据在工具间流动，不经过模型上下文
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**Example — CLI 调用工具：**

```bash
# 直接调用指定工具
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# 查看可用 servers 与 tools
npx mcporter list
```

MCPorter 与“代码执行调用 MCP”方案互补：它提供把 MCP 工具当类型 API 调用的运行时基础设施，帮助你把中间数据留在执行环境中。

## Best Practices

### Security Considerations

#### Do's ✅
- 所有凭据都放环境变量
- 定期轮换 token / API key（建议每月）
- 能用只读 token 就不用写权限 token
- MCP server 权限范围最小化
- 监控 MCP 使用与访问日志
- 外部服务优先 OAuth
- 为 MCP 请求做限流
- 上生产前先连通性测试
- 记录所有启用中的 MCP 连接
- 及时更新 MCP server 包版本

#### Don'ts ❌
- 不要在配置文件硬编码凭据
- 不要把 token/secret 提交到 git
- 不要在群聊/邮件分享 token
- 不要用个人 token 跑团队项目
- 不要授予不必要权限
- 不要忽略认证错误
- 不要对公网暴露 MCP endpoint
- 不要用 root/admin 权限运行 MCP server
- 不要在日志缓存敏感数据
- 不要关闭认证机制

### Configuration Best Practices

1. **Version Control**：`.mcp.json` 可入 git，但 secrets 一律用环境变量
2. **Least Privilege**：每个 MCP server 只给最小必要权限
3. **Isolation**：有条件时不同 MCP server 分进程运行
4. **Monitoring**：记录 MCP 请求与错误，便于审计
5. **Testing**：部署前完整测试 MCP 配置

### Performance Tips

- 在应用层缓存高频数据
- MCP 查询尽量具体，减少数据传输
- 监控 MCP 操作响应时间
- 外部 API 注意限流策略
- 多操作场景优先 batch

## Installation Instructions

### Prerequisites
- 已安装 Node.js / npm
- 已安装 Claude Code CLI
- 已准备外部服务 API token / 凭据

### Step-by-Step Setup

1. **先添加一个 MCP server**（例：GitHub）：

```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

或在项目根目录创建 `.mcp.json`：

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

2. **设置环境变量：**

```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3. **测试连接：**

```bash
claude /mcp
```

4. **使用 MCP 工具：**

```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### Installation for Specific Services

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

## Troubleshooting

### MCP Server Not Found

```bash
# 检查是否已安装
npm list -g @modelcontextprotocol/server-github

# 未安装则安装
npm install -g @modelcontextprotocol/server-github
```

### Authentication Failed

```bash
# 检查环境变量
echo $GITHUB_TOKEN

# 重新导出
export GITHUB_TOKEN="your_token"

# 检查 token 权限范围
# GitHub token scopes: https://github.com/settings/tokens
```

### Connection Timeout
- 检查网络：`ping api.github.com`
- 确认 API endpoint 可访问
- 检查 API rate limits
- 必要时增加配置超时
- 排查防火墙或代理

### MCP Server Crashes
- 查看 MCP logs：`~/.claude/logs/`
- 确认环境变量齐全
- 确认文件权限正确
- 尝试重装 MCP server 包
- 检查端口冲突

## Related Concepts

### Memory vs MCP
- **Memory**：存储持久、低变化信息（偏好、上下文、历史）
- **MCP**：访问实时、变化数据（API、数据库、在线服务）

### When to Use Each
- **Use Memory**：用户偏好、会话历史、长期上下文
- **Use MCP**：当前 GitHub issues、实时数据库查询、在线数据

### Integration with Other Claude Features
- MCP + Memory 结合可构建更丰富上下文
- 在 prompts 中调用 MCP 工具可提升推理质量
- 多 MCP 联动可实现复杂自动化流程

## Additional Resources

- [Official MCP Documentation](https://code.claude.com/docs/en/mcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io/specification)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol/servers)
- [Available MCP Servers](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — TypeScript runtime 与 CLI
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic 关于 context bloat 的工程实践
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Claude API Documentation](https://docs.anthropic.com)
