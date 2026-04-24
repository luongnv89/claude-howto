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
/plugin install pr-review
```

## What's Included

### Slash Commands
- `/review-pr` - Comprehensive PR review
- `/check-security` - Security-focused review
- `/check-tests` - Test coverage analysis

### Subagents
- `security-reviewer` - Security vulnerability detection
- `test-checker` - Test coverage analysis
- `performance-analyzer` - Performance impact evaluation

### MCP Servers
- GitHub integration for PR data

### Hooks
- `pre-review.js` - Pre-review validation

## Usage

### Basic PR Review
```
/review-pr
```

### Security Check Only
```
/check-security
```

### Test Coverage Check
```
/check-tests
```

## Requirements

- Claude Code 1.0+
- GitHub access
- Git repository

## Configuration

Set up your GitHub token:
```bash
export GITHUB_TOKEN="your_github_token"
```

## Example Workflow

```
User: /review-pr

Claude:
1. Runs pre-review hook (validates git repo)
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

**Last Updated**: April 24, 2026
**Claude Code Version**: 2.1.119
**Sources**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
