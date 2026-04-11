<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

This folder contains comprehensive documentation and examples for MCP server configurations and usage with Claude Code.

## Overview

MCP (Model Context Protocol) is a standardized way for Claude to access external tools, APIs, and real-time data sources. Unlike Memory, MCP provides live access to changing data.

Key characteristics:
- Real-time access to external services
- Live data synchronization
- Extensible architecture
- Secure authentication
- Tool-based interactions

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

Claude Code supports multiple transport protocols for MCP server connections:

### HTTP Transport (Recommended)

```bash
# Basic HTTP connection
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP with authentication header
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Stdio Transport (Local)

For locally running MCP servers:

```bash
# Local Node.js server
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# With environment variables
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### SSE Transport (Deprecated)

Server-Sent Events transport is deprecated in favor of `http` but still supported:

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### Windows-Specific Note

On native Windows (not WSL), use `cmd /c` for npx commands:

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### OAuth 2.0 Authentication

Claude Code supports OAuth 2.0 for MCP servers that require it. When connecting to an OAuth-enabled server, Claude Code handles the entire authentication flow:

```bash
# Connect to an OAuth-enabled MCP server (interactive flow)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# Pre-configure OAuth credentials for non-interactive setup
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| Feature | Description |
|---------|-------------|
| **Interactive OAuth** | Use `/mcp` to trigger the browser-based OAuth flow |
| **Pre-configured OAuth clients** | Built-in OAuth clients for common services like Notion, Stripe, and others (v2.1.30+) |
| **Pre-configured credentials** | `--client-id`, `--client-secret`, `--callback-port` flags for automated setup |
| **Token storage** | Tokens are stored securely in your system keychain |
| **Step-up auth** | Supports step-up authentication for privileged operations |
| **Discovery caching** | OAuth discovery metadata is cached for faster reconnections |
| **Metadata override** | `oauth.authServerMetadataUrl` in `.mcp.json` to override default OAuth metadata discovery |

#### Overriding OAuth Metadata Discovery

If your MCP server returns errors on the standard OAuth metadata endpoint (`/.well-known/oauth-authorization-server`) but exposes a working OIDC endpoint, you can tell Claude Code to fetch OAuth metadata from a specific URL. Set `authServerMetadataUrl` in the `oauth` object of your server config:

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

The URL must use `https://`. This option requires Claude Code v2.1.64 or later.

### Claude.ai MCP Connectors

MCP servers configured in your Claude.ai account are automatically available in Claude Code. This means any MCP connections you set up through the Claude.ai web interface will be accessible without additional configuration.

Claude.ai MCP connectors are also available in `--print` mode (v2.1.83+), enabling non-interactive and scripted usage.

To disable Claude.ai MCP servers in Claude Code, set the `ENABLE_CLAUDEAI_MCP_SERVERS` environment variable to `false`:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **Note:** This feature is only available for users logged in with Claude.ai accounts.

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

When MCP tool descriptions exceed 10% of the context window, Claude Code automatically enables tool search to efficiently select the right tools without overwhelming the model context.

| Setting | Value | Description |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | `auto` (default) | Automatically enables when tool descriptions exceed 10% of context |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | Automatically enables at a custom threshold of `N` tools |
| `ENABLE_TOOL_SEARCH` | `true` | Always enabled regardless of tool count |
| `ENABLE_TOOL_SEARCH` | `false` | Disabled; all tool descriptions sent in full |

> **Note:** Tool search requires Sonnet 4 or later, or Opus 4 or later. Haiku models are not supported for tool search.

## Dynamic Tool Updates

Claude Code supports MCP `list_changed` notifications. When an MCP server dynamically adds, removes, or modifies its available tools, Claude Code receives the update and adjusts its tool list automatically -- no reconnection or restart required.

## MCP Apps

MCP Apps is the first official MCP extension, enabling MCP tool calls to return interactive UI components that render directly in the chat interface. Instead of plain text responses, MCP servers can deliver rich dashboards, forms, data visualizations, and multi-step workflows -- all displayed inline without leaving the conversation.

## MCP Elicitation

MCP servers can request structured input from the user via interactive dialogs (v2.1.49+). This allows an MCP server to ask for additional information mid-workflow -- for example, prompting for a confirmation, selecting from a list of options, or filling in required fields -- adding interactivity to MCP server interactions.

## Tool Description and Instruction Cap

As of v2.1.84, Claude Code enforces a **2 KB cap** on tool descriptions and instructions per MCP server. This prevents individual servers from consuming excessive context with overly verbose tool definitions, reducing context bloat and keeping interactions efficient.

## MCP Prompts as Slash Commands

MCP servers can expose prompts that appear as slash commands in Claude Code. Prompts are accessible using the naming convention:

```
/mcp__<server>__<prompt>
```

For example, if a server named `github` exposes a prompt called `review`, you can invoke it as `/mcp__github__review`.

## Server Deduplication

When the same MCP server is defined at multiple scopes (local, project, user), the local configuration takes precedence. This allows you to override project-level or user-level MCP settings with local customizations without conflicts.

## MCP Resources via @ Mentions

You can reference MCP resources directly in your prompts using the `@` mention syntax:

```
@server-name:protocol://resource/path
```

For example, to reference a specific database resource:

```
@database:postgres://mydb/users
```

This allows Claude to fetch and include MCP resource content inline as part of the conversation context.

## MCP Scopes

MCP configurations can be stored at different scopes with varying levels of sharing:

| Scope | Location | Description | Shared With | Requires Approval |
|-------|----------|-------------|-------------|------------------|
| **Local** (default) | `~/.claude.json` (under project path) | Private to current user, current project only (was called `project` in older versions) | Just you | No |
| **Project** | `.mcp.json` | Checked into git repository | Team members | Yes (first use) |
| **User** | `~/.claude.json` | Available across all projects (was called `global` in older versions) | Just you | No |

### Using Project Scope

Store project-specific MCP configurations in `.mcp.json`:

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

Team members will see an approval prompt on first use of project MCPs.

## MCP Configuration Management

### Adding MCP Servers

```bash
# Add HTTP-based server
claude mcp add --transport http github https://api.github.com/mcp

# Add local stdio server
claude mcp add --transport stdio database -- npx @company/db-server

# List all MCP servers
claude mcp list

# Get details on specific server
claude mcp get github

# Remove an MCP server
claude mcp remove github

# Reset project-specific approval choices
claude mcp reset-project-choices

# Import from Claude Desktop
claude mcp add-from-claude-desktop
```

## Available MCP Servers Table

| MCP Server | Purpose | Common Tools | Auth | Real-time |
|------------|---------|--------------|------|-----------|
| **Filesystem** | File operations | read, write, delete | OS permissions | ✅ Yes |
| **GitHub** | Repository management | list_prs, create_issue, push | OAuth | ✅ Yes |
| **Slack** | Team communication | send_message, list_channels | Token | ✅ Yes |
| **Database** | SQL queries | query, insert, update | Credentials | ✅ Yes |
| **Google Docs** | Document access | read, write, share | OAuth | ✅ Yes |
| **Asana** | Project management | create_task, update_status | API Key | ✅ Yes |
| **Stripe** | Payment data | list_charges, create_invoice | API Key | ✅ Yes |
| **Memory** | Persistent memory | store, retrieve, delete | Local | ❌ No |

## Practical Examples

### Example 1: GitHub MCP Configuration

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

**Available GitHub MCP Tools:**

#### Pull Request Management
- `list_prs` - List all PRs in repository
- `get_pr` - Get PR details including diff
- `create_pr` - Create new PR
- `update_pr` - Update PR description/title
- `merge_pr` - Merge PR to main branch
- `review_pr` - Add review comments

**Example request:**
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### Issue Management
- `list_issues` - List all issues
- `get_issue` - Get issue details
- `create_issue` - Create new issue
- `close_issue` - Close issue
- `add_comment` - Add comment to issue

#### Repository Information
- `get_repo_info` - Repository details
- `list_files` - File tree structure
- `get_file_content` - Read file contents
- `search_code` - Search across codebase

#### Commit Operations
- `list_commits` - Commit history
- `get_commit` - Specific commit details
- `create_commit` - Create new commit

**Setup**:
```bash
export GITHUB_TOKEN="your_github_token"
# Or use the CLI to add directly:
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### Environment Variable Expansion in Configuration

MCP configurations support environment variable expansion with fallback defaults. The `${VAR}` and `${VAR:-default}` syntax works in the following fields: `command`, `args`, `env`, `url`, and `headers`.

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

Variables are expanded at runtime:
- `${VAR}` - Uses environment variable, error if not set
- `${VAR:-default}` - Uses environment variable, falls back to default if not set

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

**Setup**:
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# Or use the CLI to add directly:
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

**Setup**:
```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
# Add each MCP server via the CLI or configure them in .mcp.json
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
| List files | `ls ~/projects` | Show directory contents |
| Read file | `cat src/main.ts` | Read file contents |
| Write file | `create docs/api.md` | Create new file |
| Edit file | `edit src/app.ts` | Modify file |
| Search | `grep "async function"` | Search in files |
| Delete | `rm old-file.js` | Delete file |

**Setup**:
```bash
# Use the CLI to add directly:
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

Store sensitive credentials in environment variables:

```bash
# ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

Then reference them in MCP config:

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Claude as MCP Server (`claude mcp serve`)

Claude Code itself can act as an MCP server for other applications. This enables external tools, editors, and automation systems to leverage Claude's capabilities through the standard MCP protocol.

```bash
# Start Claude Code as an MCP server on stdio
claude mcp serve
```

Other applications can then connect to this server as they would any stdio-based MCP server. For example, to add Claude Code as an MCP server in another Claude Code instance:

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

This is useful for building multi-agent workflows where one Claude instance orchestrates another.

## Managed MCP Configuration (Enterprise)

For enterprise deployments, IT administrators can enforce MCP server policies through the `managed-mcp.json` configuration file. This file provides exclusive control over which MCP servers are permitted or blocked organization-wide.

**Location:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**Features:**
- `allowedMcpServers` -- whitelist of permitted servers
- `deniedMcpServers` -- blocklist of prohibited servers
- Supports matching by server name, command, and URL patterns
- Organization-wide MCP policies enforced before user configuration
- Prevents unauthorized server connections

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

> **Note:** When both `allowedMcpServers` and `deniedMcpServers` match a server, the deny rule takes precedence.

## Plugin-Provided MCP Servers

Plugins can bundle their own MCP servers, making them available automatically when the plugin is installed. Plugin-provided MCP servers can be defined in two ways:

1. **Standalone `.mcp.json`** -- Place a `.mcp.json` file in the plugin root directory
2. **Inline in `plugin.json`** -- Define MCP servers directly within the plugin manifest

Use the `${CLAUDE_PLUGIN_ROOT}` variable to reference paths relative to the plugin's installation directory:

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

MCP servers can be defined inline within agent frontmatter using the `mcpServers:` key, scoping them to a specific subagent rather than the entire project. This is useful when an agent needs access to a particular MCP server that other agents in the workflow do not require.

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

Subagent-scoped MCP servers are only available within that agent's execution context and are not shared with the parent or sibling agents.

## MCP Output Limits

Claude Code enforces limits on MCP tool output to prevent context overflow:

| Limit | Threshold | Behavior |
|-------|-----------|----------|
| **Warning** | 10,000 tokens | A warning is displayed that the output is large |
| **Default max** | 25,000 tokens | Output is truncated beyond this limit |
| **Disk persistence** | 50,000 characters | Tool results exceeding 50K characters are persisted to disk |

The maximum output limit is configurable via the `MAX_MCP_OUTPUT_TOKENS` environment variable:

```bash
# Increase the max output to 50,000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## Solving Context Bloat with Code Execution

As MCP adoption scales, connecting to dozens of servers with hundreds or thousands of tools creates a significant challenge: **context bloat**. This is arguably the biggest problem with MCP at scale, and Anthropic's engineering team has proposed an elegant solution — using code execution instead of direct tool calls.

> **Source**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic Engineering Blog

### The Problem: Two Sources of Token Waste

**1. Tool definitions overload the context window**

Most MCP clients load all tool definitions upfront. When connected to thousands of tools, the model must process hundreds of thousands of tokens before it even reads the user's request.

**2. Intermediate results consume additional tokens**

Every intermediate tool result passes through the model's context. Consider transferring a meeting transcript from Google Drive to Salesforce — the full transcript flows through context **twice**: once when reading it, and again when writing it to the destination. A 2-hour meeting transcript could mean 50,000+ extra tokens.

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

Instead of passing tool definitions and results through the context window, the agent **writes code** that calls MCP tools as APIs. The code runs in a sandboxed execution environment, and only the final result returns to the model.

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

MCP tools are presented as a file tree of typed functions:

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

Each tool file contains a typed wrapper:

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

The agent then writes code to orchestrate the tools:

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// Data flows directly between tools — never through the model
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**Result: Token usage drops from ~150,000 to ~2,000 — a 98.7% reduction.**

### Key Benefits

| Benefit | Description |
|---------|-------------|
| **Progressive Disclosure** | Agent browses the filesystem to load only the tool definitions it needs, instead of all tools upfront |
| **Context-Efficient Results** | Data is filtered/transformed in the execution environment before returning to the model |
| **Powerful Control Flow** | Loops, conditionals, and error handling run in code without round-tripping through the model |
| **Privacy Preservation** | Intermediate data (PII, sensitive records) stays in the execution environment; never enters the model context |
| **State Persistence** | Agents can save intermediate results to files and build reusable skill functions |

#### Example: Filtering Large Datasets

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

#### Example: Loop Without Round-Tripping

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

### Trade-offs to Consider

Code execution introduces its own complexity. Running agent-generated code requires:

- A **secure sandboxed execution environment** with appropriate resource limits
- **Monitoring and logging** of executed code
- Additional **infrastructure overhead** compared to direct tool calls

The benefits — reduced token costs, lower latency, improved tool composition — should be weighed against these implementation costs. For agents with only a few MCP servers, direct tool calls may be simpler. For agents at scale (dozens of servers, hundreds of tools), code execution is a significant improvement.

### MCPorter: A Runtime for MCP Tool Composition

[MCPorter](https://github.com/steipete/mcporter) is a TypeScript runtime and CLI toolkit that makes calling MCP servers practical without boilerplate — and helps reduce context bloat through selective tool exposure and typed wrappers.

**What it solves:** Instead of loading all tool definitions from all MCP servers upfront, MCPorter lets you discover, inspect, and call specific tools on demand — keeping your context lean.

**Key features:**

| Feature | Description |
|---------|-------------|
| **Zero-config discovery** | Auto-discovers MCP servers from Cursor, Claude, Codex, or local configs |
| **Typed tool clients** | `mcporter emit-ts` generates `.d.ts` interfaces and ready-to-run wrappers |
| **Composable API** | `createServerProxy()` exposes tools as camelCase methods with `.text()`, `.json()`, `.markdown()` helpers |
| **CLI generation** | `mcporter generate-cli` converts any MCP server into a standalone CLI with `--include-tools` / `--exclude-tools` filtering |
| **Parameter hiding** | Optional parameters stay hidden by default, reducing schema verbosity |

**Installation:**

```bash
npx mcporter list          # No install required — discover servers instantly
pnpm add mcporter          # Add to a project
brew install steipete/tap/mcporter  # macOS via Homebrew
```

**Example — composing tools in TypeScript:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Data flows between tools without passing through the model context
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**Example — CLI tool call:**

```bash
# Call a specific tool directly
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# List available servers and tools
npx mcporter list
```

MCPorter complements the code-execution approach described above by providing the runtime infrastructure for calling MCP tools as typed APIs — making it straightforward to keep intermediate data out of the model context.

## Best Practices

### Security Considerations

#### Do's ✅
- Use environment variables for all credentials
- Rotate tokens and API keys regularly (monthly recommended)
- Use read-only tokens when possible
- Limit MCP server access scope to minimum required
- Monitor MCP server usage and access logs
- Use OAuth for external services when available
- Implement rate limiting on MCP requests
- Test MCP connections before production use
- Document all active MCP connections
- Keep MCP server packages updated

#### Don'ts ❌
- Don't hardcode credentials in config files
- Don't commit tokens or secrets to git
- Don't share tokens in team chats or emails
- Don't use personal tokens for team projects
- Don't grant unnecessary permissions
- Don't ignore authentication errors
- Don't expose MCP endpoints publicly
- Don't run MCP servers with root/admin privileges
- Don't cache sensitive data in logs
- Don't disable authentication mechanisms

### Configuration Best Practices

1. **Version Control**: Keep `.mcp.json` in git but use environment variables for secrets
2. **Least Privilege**: Grant minimum permissions needed for each MCP server
3. **Isolation**: Run different MCP servers in separate processes when possible
4. **Monitoring**: Log all MCP requests and errors for audit trails
5. **Testing**: Test all MCP configurations before deploying to production

### Performance Tips

- Cache frequently accessed data at the application level
- Use MCP queries that are specific to reduce data transfer
- Monitor response times for MCP operations
- Consider rate limiting for external APIs
- Use batching when performing multiple operations

## Installation Instructions

### Prerequisites
- Node.js and npm installed
- Claude Code CLI installed
- API tokens/credentials for external services

### Step-by-Step Setup

1. **Add your first MCP server** using the CLI (example: GitHub):
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

   Or create a `.mcp.json` file in your project root:
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

2. **Set environment variables:**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3. **Test the connection:**
```bash
claude /mcp
```

4. **Use MCP tools:**
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
# Verify MCP server is installed
npm list -g @modelcontextprotocol/server-github

# Install if missing
npm install -g @modelcontextprotocol/server-github
```

### Authentication Failed
```bash
# Verify environment variable is set
echo $GITHUB_TOKEN

# Re-export if needed
export GITHUB_TOKEN="your_token"

# Verify token has correct permissions
# Check GitHub token scopes at: https://github.com/settings/tokens
```

### Connection Timeout
- Check network connectivity: `ping api.github.com`
- Verify API endpoint is accessible
- Check rate limits on API
- Try increasing timeout in config
- Check for firewall or proxy issues

### MCP Server Crashes
- Check MCP server logs: `~/.claude/logs/`
- Verify all environment variables are set
- Ensure proper file permissions
- Try reinstalling the MCP server package
- Check for conflicting processes on the same port

## Related Concepts

### Memory vs MCP
- **Memory**: Stores persistent, unchanging data (preferences, context, history)
- **MCP**: Accesses live, changing data (APIs, databases, real-time services)

### When to Use Each
- **Use Memory** for: User preferences, conversation history, learned context
- **Use MCP** for: Current GitHub issues, live database queries, real-time data

### Integration with Other Claude Features
- Combine MCP with Memory for rich context
- Use MCP tools in prompts for better reasoning
- Leverage multiple MCPs for complex workflows

## Additional Resources

- [Official MCP Documentation](https://code.claude.com/docs/en/mcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io/specification)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol/servers)
- [Available MCP Servers](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — TypeScript runtime & CLI for calling MCP servers without boilerplate
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic's engineering blog on solving context bloat
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Claude API Documentation](https://docs.anthropic.com)

---
**Last Updated**: April 11, 2026
**Claude Code Version**: 2.1.101
**Sources**:
- https://code.claude.com/docs/en/mcp
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
