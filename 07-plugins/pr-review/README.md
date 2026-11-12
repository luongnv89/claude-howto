<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# PR Review Plugin

Complete PR review workflow with security, testing, and documentation checks.

## Features

✅ Security analysis
✅ Test coverage checking
✅ Documentation verification
✅ Code quality assessment
✅ Performance impact analysis

## Installation

```bash
claude --plugin-dir ./07-plugins/pr-review
```

Check the plugin before you load it:

```bash
claude plugin validate ./07-plugins/pr-review
```

## What's Included

```text
pr-review/
├── .claude-plugin/
│   └── plugin.json      # "name": "pr-review" sets the command prefix
├── commands/            # each file becomes /pr-review:<file>
├── agents/
├── hooks/
│   ├── hooks.json       # registers pre-review.js
│   └── pre-review.js
└── .mcp.json            # GitHub MCP server
```

### Slash Commands

Plugin commands are namespaced with the plugin `name` from `plugin.json`:

- `/pr-review:review-pr` - Comprehensive PR review
- `/pr-review:check-security` - Security-focused review
- `/pr-review:check-tests` - Test coverage analysis

### Subagents
- `security-reviewer` - Security vulnerability detection
- `test-checker` - Test coverage analysis
- `performance-analyzer` - Performance impact evaluation

### MCP Servers

`.mcp.json` declares one server, `github`: GitHub's official MCP server (`ghcr.io/github/github-mcp-server`), run with Docker in read-only mode. It shows up as `plugin:pr-review:github` in `/mcp`.

### Hooks

`hooks/hooks.json` registers `pre-review.js` on the `UserPromptExpansion` event, with a matcher for the three commands above. When you type one of them, the hook:

- blocks the command (exit code 2) when the current directory is not a git repository
- otherwise adds the current branch, and a note about uncommitted changes, to Claude's context

## Usage

### Basic PR Review
```text
/pr-review:review-pr
```

### Security Check Only
```text
/pr-review:check-security
```

### Test Coverage Check
```text
/pr-review:check-tests
```

## Requirements

- Claude Code 2.1+
- Node.js (runs the hook script)
- Docker (runs the GitHub MCP server)
- A GitHub personal access token
- Git repository

## Configuration

Set your GitHub token before you start Claude Code:
```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json` passes it to the server as `GITHUB_PERSONAL_ACCESS_TOKEN`, the variable the server reads. Run `/mcp` to check that `plugin:pr-review:github` is connected.

## Example Workflow

```text
User: /pr-review:review-pr

Claude:
1. pre-review hook checks the git repository and adds the branch to context
2. Fetches PR data via GitHub MCP
3. Delegates security review to security-reviewer subagent
4. Delegates testing to test-checker subagent
5. Delegates performance to performance-analyzer subagent
6. Synthesizes all findings
7. Provides comprehensive review report

Result:
✅ Security: No critical issues found
⚠️  Testing: Coverage is 65%, recommend 80%+
✅ Performance: No significant impact
📝 Recommendations: Add tests for edge cases
```

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
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
