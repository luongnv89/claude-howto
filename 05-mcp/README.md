![Claude How To](../claude-howto-logo.svg)

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
```

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

## Installation

Copy the appropriate configuration to your project's `.claude/` directory:

```bash
cp github-mcp.json /path/to/your/project/.claude/mcp.json
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

**File:** `.claude/mcp.json`

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
cp github-mcp.json ~/.claude/mcp.json
```

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
cp database-mcp.json ~/.claude/mcp.json
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
cp multi-mcp.json ~/.claude/mcp.json
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
cp filesystem-mcp.json ~/.claude/mcp.json
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

    style B fill:#e1f5ff
    style D fill:#fff9c4
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

1. **Version Control**: Keep `.claude/mcp.json` in git but use environment variables for secrets
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

1. **Create MCP configuration file:**
```bash
mkdir -p ~/.claude
touch ~/.claude/mcp.json
```

2. **Add your first MCP server** (example: GitHub):
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

3. **Set environment variables:**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

4. **Test the connection:**
```bash
claude /mcp
```

5. **Use MCP tools:**
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

- [MCP GitHub Repository](https://github.com/modelcontextprotocol/servers)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Claude Code MCP Guide](https://docs.claude.com/en/docs/claude-code/mcp)
- [Available MCP Servers](https://github.com/modelcontextprotocol/servers)
- [Claude API Documentation](https://docs.anthropic.com)
- [Environment Variables Setup Guide](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables)
