![Claude How To](../../claude-howto-logo.svg)

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
/plugin install documentation
```

## What's Included

### Slash Commands
- `/generate-api-docs` - Generate API documentation
- `/generate-readme` - Create or update README
- `/sync-docs` - Sync docs with code changes
- `/validate-docs` - Validate documentation

### Subagents
- `api-documenter` - API documentation specialist
- `code-commentator` - Code comment improvements
- `example-generator` - Code example creation

### Templates
- `api-endpoint.md` - API endpoint documentation template
- `function-docs.md` - Function documentation template
- `adr-template.md` - Architecture Decision Record template

### MCP Servers
- GitHub integration for documentation syncing

## Usage

### Generate API Documentation
```
/generate-api-docs
```

### Create README
```
/generate-readme
```

### Sync Documentation
```
/sync-docs
```

### Validate Documentation
```
/validate-docs
```

## Requirements

- Claude Code 1.0+
- GitHub access (optional)

## Example Workflow

```
User: /generate-api-docs

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

## Best Practices

- Keep documentation close to code
- Update docs with code changes
- Include practical examples
- Validate regularly
- Use templates for consistency
