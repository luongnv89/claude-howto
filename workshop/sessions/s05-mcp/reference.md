# Session 5 Reference: MCP (Model Context Protocol)

Quick reference for MCP in Claude Code. For the full guide, see [05-mcp/README.md](../../05-mcp/README.md).

## .mcp.json Configuration

Project-scoped MCP configuration at the project root:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@scope/package-name"],
      "env": {
        "TOKEN_VAR": "value"
      }
    }
  }
}
```

| Field | Purpose |
|-------|---------|
| `command` | Executable to run the server |
| `args` | Arguments passed to the command |
| `env` | Environment variables (tokens, URLs) |

## Configuration Scopes

| Scope | File | Applies To |
|-------|------|-----------|
| Project | `.mcp.json` | This project only |
| User | `~/.claude.json` | All projects |

Project scope (`.mcp.json`) is recommended for bootcamp work.

## Adding Servers via CLI

```bash
# Add a server
claude mcp add <name> --command "npx" --args "-y" "@scope/package" --env "KEY=value"

# List configured servers
claude mcp list

# Remove a server
claude mcp remove <name>
```

## GitHub MCP Server

**Package**: `@modelcontextprotocol/server-github`

**Configuration**:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<token>"
      }
    }
  }
}
```

**Required token scopes**: `repo`, `issues` (minimum)

## Atlassian/Jira MCP Server

**Package**: `@aashari/mcp-server-atlassian-jira`

**Configuration**:

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": ["-y", "@aashari/mcp-server-atlassian-jira"],
      "env": {
        "ATLASSIAN_SITE_URL": "https://your-site.atlassian.net",
        "ATLASSIAN_USER_EMAIL": "your@email.com",
        "ATLASSIAN_API_TOKEN": "<token>"
      }
    }
  }
}
```

See [jira-setup-guide.md](jira-setup-guide.md) for account and token setup.

## MCP Transports

| Transport | How It Works | Example |
|-----------|-------------|---------|
| **stdio** | Runs as local subprocess | Most MCP servers |
| **HTTP/SSE** | Connects to remote endpoint | Cloud-hosted servers |

Most bootcamp servers use stdio (local subprocess via npx).

## Environment Variable Security

- Never commit tokens directly in `.mcp.json` if the repo is public
- Consider adding `.mcp.json` to `.gitignore`
- Alternatively, use env vars that reference shell environment: `"$GITHUB_TOKEN"`
- Restart Claude Code after modifying `.mcp.json`

## Troubleshooting

| Issue | Solution |
|-------|---------|
| MCP tools not appearing | Restart Claude Code after editing `.mcp.json` |
| Authentication errors | Verify token scopes and expiration |
| Server not found | Check `npx` can install the package (`npx -y @scope/pkg --help`) |
| Invalid JSON | Validate `.mcp.json` syntax (trailing commas, missing brackets) |

## Tips

- Use `claude mcp add` for initial setup, then edit `.mcp.json` for fine-tuning
- MCP servers are discovered at Claude Code startup -- restart after config changes
- Each MCP server exposes tools that Claude can call directly
- MCP prompts appear as `/mcp__servername__promptname` slash commands
