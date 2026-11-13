<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Documentation Plugin

Comprehensive documentation generation and maintenance for your project.

## Features

✅ API documentation generation
✅ README creation and updates
✅ Documentation synchronization
✅ Code comment improvements
✅ Example generation

## Installation

```bash
claude --plugin-dir ./07-plugins/documentation
```

Check the plugin before you load it:

```bash
claude plugin validate ./07-plugins/documentation
```

## What's Included

### Slash Commands

Plugin commands are namespaced with the plugin `name` from `plugin.json`:

- `/documentation:generate-api-docs` - Generate API documentation
- `/documentation:generate-readme` - Create or update README
- `/documentation:sync-docs` - Sync docs with code changes
- `/documentation:validate-docs` - Validate documentation

### Subagents
- `api-documenter` - API documentation specialist
- `code-commentator` - Code comment improvements
- `example-generator` - Code example creation

### Templates
- `api-endpoint.md` - API endpoint documentation template
- `function-docs.md` - Function documentation template
- `adr-template.md` - Architecture Decision Record template

### MCP Servers

`.mcp.json` declares one server, `github`: GitHub's official MCP server (`ghcr.io/github/github-mcp-server`), run with Docker in read-only mode. The image is pinned to the [v2.1.0 release](https://github.com/github/github-mcp-server/releases/tag/v2.1.0); change the tag in `.mcp.json` to upgrade. It shows up as `plugin:documentation:github` in `/mcp`.

## Usage

### Generate API Documentation
```text
/documentation:generate-api-docs
```

### Create README
```text
/documentation:generate-readme
```

### Sync Documentation
```text
/documentation:sync-docs
```

### Validate Documentation
```text
/documentation:validate-docs
```

## Requirements

- Claude Code 2.1+
- Docker and a GitHub personal access token (optional, for the GitHub MCP server)

## Example Workflow

```text
User: /documentation:generate-api-docs

Claude:
1. Scans all API endpoints in /src/api/
2. Delegates to api-documenter subagent
3. Extracts function signatures and JSDoc
4. Organizes by module/endpoint
5. Uses api-endpoint.md template
6. Generates comprehensive markdown docs
7. Includes curl, JavaScript, and Python examples

Result:
✅ API documentation generated
📄 Files created:
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 Coverage: 23/23 endpoints documented
```

## Templates Usage

### API Endpoint Template
Use for documenting REST API endpoints with full examples.

### Function Documentation Template
Use for documenting individual functions/methods.

### ADR Template
Use for documenting architectural decisions.

## Configuration

Set up GitHub token for documentation syncing:
```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json` passes it to the server as `GITHUB_PERSONAL_ACCESS_TOKEN`, the variable the server reads. Run `/mcp` to check that `plugin:documentation:github` is connected. Without a token the commands still work on local files.

## Best Practices

- Keep documentation close to code
- Update docs with code changes
- Include practical examples
- Validate regularly
- Use templates for consistency

---

**Last Updated**: October 18, 2026
**Claude Code Version**: 2.1.302
**Sources**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**Compatible Models**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
