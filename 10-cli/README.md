<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# CLI Reference

## Overview

The Claude Code CLI (Command Line Interface) is the primary way to interact with Claude Code. It provides powerful options for running queries, managing sessions, configuring models, and integrating Claude into your development workflows.

## Architecture

```mermaid
graph TD
    A["User Terminal"] -->|"claude [options] [query]"| B["Claude Code CLI"]
    B -->|Interactive| C["REPL Mode"]
    B -->|"--print"| D["Print Mode (SDK)"]
    B -->|"--resume"| E["Session Resume"]
    C -->|Conversation| F["Claude API"]
    D -->|Single Query| F
    E -->|Load Context| F
    F -->|Response| G["Output"]
    G -->|text/json/stream-json| H["Terminal/Pipe"]
```

## Runtime & Packaging

Since **v2.1.113**, the Claude Code CLI launches a **native per-platform binary** (macOS, Linux, Windows) via optional npm dependencies. The binary is matched to your OS and architecture at install time — the older bundled-JavaScript runtime is no longer the default on macOS or Linux.

The **user-facing install is unchanged**: `npm install -g @anthropic-ai/claude-code` still works and remains the recommended path. Behind the scenes npm fetches the correct native binary for your platform.

**Download host** (v2.1.116+): native-binary artifacts are served from `https://downloads.claude.ai/claude-code-releases`.

> **Corporate / proxy users**: If your network requires an explicit allowlist, add `downloads.claude.ai` (and `https://downloads.claude.ai/claude-code-releases`) to your proxy egress rules. Environments that previously allowlisted only `storage.googleapis.com` or the npm registry will need to be updated or `claude update` and the initial install will fail.

The older JavaScript bundle is still produced for Windows and for environments that pin to it; those installs continue to ship Glob and Grep as first-class tools (see the Glob/Grep footnote under [Tools](#tool--permission-management)).

## CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `claude` | Start interactive REPL | `claude` |
| `claude "query"` | Start REPL with initial prompt | `claude "explain this project"` |
| `claude -p "query"` | Print mode - query then exit | `claude -p "explain this function"` |
| `cat file \| claude -p "query"` | Process piped content | `cat logs.txt \| claude -p "explain"` |
| `claude -c` | Continue most recent conversation | `claude -c` |
| `claude -c -p "query"` | Continue in print mode | `claude -c -p "check for type errors"` |
| `claude -r "<session>" "query"` | Resume session by ID or name | `claude -r "auth-refactor" "finish this PR"` |
| `claude update` | Update to latest version | `claude update` |
| `/doctor` (slash command) | Diagnose installation, config, and plugin health. Since v2.1.116 it can be opened **while Claude is responding**, shows status icons inline, and accepts the `f` keypress to auto-fix detected issues | run `/doctor` inside the REPL |
| `claude mcp` | Configure MCP servers | See [MCP documentation](../05-mcp/) |
| `claude mcp serve` | Run Claude Code as an MCP server | `claude mcp serve` |
| `claude agents` | List all configured subagents | `claude agents` |
| `claude auto-mode defaults` | Print auto mode default rules as JSON | `claude auto-mode defaults` |
| `claude remote-control` | Start Remote Control server | `claude remote-control` |
| `claude plugin` | Manage plugins (install, enable, disable) | `claude plugin install my-plugin` |
| `claude plugin tag <version>` | Create a release git tag for a plugin with version validation (v2.1.118+) | `claude plugin tag v0.3.0` |
| `claude install [version]` | Install a specific native-binary version. Accepts `stable`, `latest`, or an explicit version string | `claude install 2.1.126` |
| `claude project purge [path]` | Delete all local Claude Code state for a project (transcripts, tasks, debug logs, file-edit history, prompt history, and `~/.claude.json` entry). Omit `[path]` for an interactive picker. Flags: `--dry-run` to preview, `-y/--yes` to skip confirmation, `-i/--interactive` to confirm each item, `--all` for every project (v2.1.126+) | `claude project purge ~/work/repo --dry-run` |
| `claude plugin prune` | Remove orphaned auto-installed plugin dependencies (parent plugin gone). `plugin uninstall --prune` does the same cascade after uninstalling a target (v2.1.121+) | `claude plugin prune` |
| `claude ultrareview [target]` | Run `/ultrareview` non-interactively. Prints findings to stdout, exits 0 on success / 1 on failure. Use `--json` for raw payload, `--timeout <minutes>` to override the 30-minute default (v2.1.120+) | `claude ultrareview 1234 --json` |
| `claude auth login` | Log in (supports `--email`, `--sso`). Since v2.1.126, accepts the OAuth code pasted into the terminal as a fallback when the browser callback can't reach localhost (WSL2, SSH, containers) | `claude auth login --email user@example.com` |
| `claude auth logout` | Log out of current account | `claude auth logout` |
| `claude auth status` | Check auth status (exit 0 if logged in, 1 if not) | `claude auth status` |

## Core Flags

| Flag | Description | Example |
|------|-------------|---------|
| `-p, --print` | Print response without interactive mode | `claude -p "query"` |
| `-c, --continue` | Load most recent conversation | `claude --continue` |
| `-r, --resume` | Resume specific session by ID or name | `claude --resume auth-refactor` |
| `-v, --version` | Output version number | `claude -v` |
| `-w, --worktree` | Start in isolated git worktree | `claude -w` |
| `-n, --name` | Session display name | `claude -n "auth-refactor"` |
| `--from-pr <url-or-number>` | Resume sessions linked to a pull/merge request. Accepts GitHub (cloud + Enterprise), GitLab MR, and Bitbucket PR URLs since v2.1.119; previously GitHub.com only | `claude --from-pr 42` or `claude --from-pr https://gitlab.example.com/org/repo/-/merge_requests/17` |
| `--remote "task"` | Create web session on claude.ai | `claude --remote "implement API"` |
| `--remote-control, --rc` | Interactive session with Remote Control | `claude --rc` |
| `--teleport` | Resume web session locally | `claude --teleport` |
| `--teammate-mode` | Agent team display mode | `claude --teammate-mode tmux` |
| `--bare` | Minimal mode (skip hooks, skills, plugins, MCP, auto memory, CLAUDE.md) | `claude --bare` |
| `--enable-auto-mode` | Unlock auto permission mode (no longer required for Max subscribers on Opus 4.7) | `claude --enable-auto-mode` |
| `--channels` | Subscribe to MCP channel plugins | `claude --channels discord,telegram` |
| `--chrome` / `--no-chrome` | Enable/disable Chrome browser integration | `claude --chrome` |
| `--effort` | Set thinking effort level | `claude --effort high` |
| `--init` / `--init-only` | Run initialization hooks | `claude --init` |
| `--maintenance` | Run maintenance hooks and exit | `claude --maintenance` |
| `--disable-slash-commands` | Disable all skills and slash commands | `claude --disable-slash-commands` |
| `--no-session-persistence` | Disable session saving (print mode) | `claude -p --no-session-persistence "query"` |
| `--exclude-dynamic-system-prompt-sections` | Exclude dynamic sections from the system prompt for better prompt cache hit rates | `claude -p --exclude-dynamic-system-prompt-sections "query"` |

### Interactive vs Print Mode

```mermaid
graph LR
    A["claude"] -->|Default| B["Interactive REPL"]
    A -->|"-p flag"| C["Print Mode"]
    B -->|Features| D["Multi-turn conversation<br>Tab completion<br>History<br>Slash commands"]
    C -->|Features| E["Single query<br>Scriptable<br>Pipeable<br>JSON output"]
```

**Interactive Mode** (default):
```bash
# Start interactive session
claude

# Start with initial prompt
claude "explain the authentication flow"
```

**Print Mode** (non-interactive):
```bash
# Single query, then exit
claude -p "what does this function do?"

# Process file content
cat error.log | claude -p "explain this error"

# Chain with other tools
claude -p "list todos" | grep "URGENT"
```

## Model & Configuration

| Flag | Description | Example |
|------|-------------|---------|
| `--model` | Set model (sonnet, opus, haiku, or full name) | `claude --model opus` |
| `--fallback-model` | Automatic model fallback when overloaded | `claude -p --fallback-model sonnet "query"` |
| `--agent` | Specify agent for session | `claude --agent my-custom-agent` |
| `--agents` | Define custom subagents via JSON | See [Agents Configuration](#agents-configuration) |
| `--effort` | Set effort level (low, medium, high, xhigh, max) | `claude --effort xhigh` |

### Model Selection Examples

```bash
# Use Opus 4.7 for complex tasks
claude --model opus "design a caching strategy"

# Use Haiku 4.5 for quick tasks
claude --model haiku -p "format this JSON"

# Full model name
claude --model claude-sonnet-4-6-20250929 "review this code"

# With fallback for reliability
claude -p --model opus --fallback-model sonnet "analyze architecture"

# Use opusplan (Opus plans, Sonnet executes)
claude --model opusplan "design and implement the caching layer"
```

> **Gateway model discovery (v2.1.126+)**: When `ANTHROPIC_BASE_URL` points at an Anthropic-compatible gateway, `/model` populates its picker from the gateway's `/v1/models` endpoint instead of the hard-coded list — useful for self-hosted proxies that expose a different model lineup.

## System Prompt Customization

| Flag | Description | Example |
|------|-------------|---------|
| `--system-prompt` | Replace entire default prompt | `claude --system-prompt "You are a Python expert"` |
| `--system-prompt-file` | Load prompt from file (print mode) | `claude -p --system-prompt-file ./prompt.txt "query"` |
| `--append-system-prompt` | Append to default prompt | `claude --append-system-prompt "Always use TypeScript"` |

### System Prompt Examples

```bash
# Complete custom persona
claude --system-prompt "You are a senior security engineer. Focus on vulnerabilities."

# Append specific instructions
claude --append-system-prompt "Always include unit tests with code examples"

# Load complex prompt from file
claude -p --system-prompt-file ./prompts/code-reviewer.txt "review main.py"
```

### System Prompt Flags Comparison

| Flag | Behavior | Interactive | Print |
|------|----------|-------------|-------|
| `--system-prompt` | Replaces entire default system prompt | ✅ | ✅ |
| `--system-prompt-file` | Replaces with prompt from file | ❌ | ✅ |
| `--append-system-prompt` | Appends to default system prompt | ✅ | ✅ |

**Use `--system-prompt-file` only in print mode. For interactive mode, use `--system-prompt` or `--append-system-prompt`.**

## Tool & Permission Management

| Flag | Description | Example |
|------|-------------|---------|
| `--tools` | Restrict available built-in tools | `claude -p --tools "Bash,Edit,Read" "query"` |
| `--allowedTools` | Tools that execute without prompting | `"Bash(git log:*)" "Read"` |
| `--disallowedTools` | Tools removed from context | `"Bash(rm:*)" "Edit"` |
| `--dangerously-skip-permissions` | Skip all permission prompts | `claude --dangerously-skip-permissions` |
| `--permission-mode` | Begin in specified permission mode | `claude --permission-mode auto` |
| `--permission-prompt-tool` | MCP tool for permission handling | `claude -p --permission-prompt-tool mcp_auth "query"` |
| `--enable-auto-mode` | Unlock auto permission mode | `claude --enable-auto-mode` |

> **Glob / Grep footnote (v2.1.113+)**: On native macOS/Linux builds, `Glob` and `Grep` are provided as the embedded `bfs` and `ugrep` binaries invoked through the Bash tool rather than as separate first-class tools. Windows and npm-bundled (JS) installs still expose them as standalone tools. For subagent `allowedTools` / `disallowedTools` lists the backend substitution is transparent — you can keep referring to `Glob` / `Grep` in your configuration on every platform.

> **PowerShell auto-approve (v2.1.119)**: PowerShell tool commands can be auto-approved in permission mode exactly the same way Bash commands are. Use the same matcher syntax you already use for `Bash(...)` rules to scope PowerShell permissions — for example, `PowerShell(Get-ChildItem:*)`.

### Permission Examples

```bash
# Read-only mode for code review
claude --permission-mode plan "review this codebase"

# Restrict to safe tools only
claude --tools "Read,Grep,Glob" -p "find all TODO comments"

# Allow specific git commands without prompts
claude --allowedTools "Bash(git status:*)" "Bash(git log:*)"

# Block dangerous operations
claude --disallowedTools "Bash(rm -rf:*)" "Bash(git push --force:*)"
```

## Output & Format

| Flag | Description | Options | Example |
|------|-------------|---------|---------|
| `--output-format` | Specify output format (print mode) | `text`, `json`, `stream-json` | `claude -p --output-format json "query"` |
| `--input-format` | Specify input format (print mode) | `text`, `stream-json` | `claude -p --input-format stream-json` |
| `--verbose` | Enable verbose logging | | `claude --verbose` |
| `--include-partial-messages` | Include streaming events | Requires `stream-json` | `claude -p --output-format stream-json --include-partial-messages "query"` |
| `--json-schema` | Get validated JSON matching schema | | `claude -p --json-schema '{"type":"object"}' "query"` |
| `--max-budget-usd` | Maximum spend for print mode | | `claude -p --max-budget-usd 5.00 "query"` |

### Output Format Examples

```bash
# Plain text (default)
claude -p "explain this code"

# JSON for programmatic use
claude -p --output-format json "list all functions in main.py"

# Streaming JSON for real-time processing
claude -p --output-format stream-json "generate a long report"

# Structured output with schema validation
claude -p --json-schema '{"type":"object","properties":{"bugs":{"type":"array"}}}' \
  "find bugs in this code and return as JSON"
```

## Workspace & Directory

| Flag | Description | Example |
|------|-------------|---------|
| `--add-dir` | Add additional working directories | `claude --add-dir ../apps ../lib` |
| `--setting-sources` | Comma-separated setting sources | `claude --setting-sources user,project` |

> **`/config` persistence (v2.1.119)**: Changes made interactively via the `/config` command are now written to `~/.claude/settings.json` and participate in the normal precedence chain (project → local → policy → user). Before v2.1.119, some `/config` changes were session-only. See [Memory & Settings](../02-memory/README.md) for the full precedence order.
| `--settings` | Load settings from file or JSON | `claude --settings ./settings.json` |
| `--plugin-dir` | Load plugins from directory (repeatable) | `claude --plugin-dir ./my-plugin` |

### Multi-Directory Example

```bash
# Work across multiple project directories
claude --add-dir ../frontend ../backend ../shared "find all API endpoints"

# Load custom settings
claude --settings '{"model":"opus","verbose":true}' "complex task"
```

## MCP Configuration

| Flag | Description | Example |
|------|-------------|---------|
| `--mcp-config` | Load MCP servers from JSON | `claude --mcp-config ./mcp.json` |
| `--strict-mcp-config` | Only use specified MCP config | `claude --strict-mcp-config --mcp-config ./mcp.json` |
| `--channels` | Subscribe to MCP channel plugins | `claude --channels discord,telegram` |

### MCP Examples

```bash
# Load GitHub MCP server
claude --mcp-config ./github-mcp.json "list open PRs"

# Strict mode - only specified servers
claude --strict-mcp-config --mcp-config ./production-mcp.json "deploy to staging"
```

## Session Management

| Flag | Description | Example |
|------|-------------|---------|
| `--session-id` | Use specific session ID (UUID) | `claude --session-id "550e8400-..."` |
| `--fork-session` | Create new session when resuming | `claude --resume abc123 --fork-session` |

### Session Examples

```bash
# Continue last conversation
claude -c

# Resume named session
claude -r "feature-auth" "continue implementing login"

# Fork session for experimentation
claude --resume feature-auth --fork-session "try alternative approach"

# Use specific session ID
claude --session-id "550e8400-e29b-41d4-a716-446655440000" "continue"
```

### Session Fork

Create a branch from an existing session for experimentation:

```bash
# Fork a session to try a different approach
claude --resume abc123 --fork-session "try alternative implementation"

# Fork with a custom message
claude -r "feature-auth" --fork-session "test with different architecture"
```

**Use Cases:**
- Try alternative implementations without losing the original session
- Experiment with different approaches in parallel
- Create branches from successful work for variations
- Test breaking changes without affecting the main session

The original session remains unchanged, and the fork becomes a new independent session.

### Project State Cleanup (v2.1.126+)

`claude project purge` deletes all local Claude Code state for a project — transcripts, task lists, debug logs, file-edit history, prompt history lines, and the project's `~/.claude.json` entry. Use `--dry-run` first to preview the deletion; `--all` walks every project on the machine.

```bash
# Preview what would be deleted (safe)
claude project purge ~/work/repo --dry-run

# Delete state for a specific project, no prompts
claude project purge ~/work/repo --yes

# Walk every project interactively
claude project purge --all --interactive
```

## Advanced Features

| Flag | Description | Example |
|------|-------------|---------|
| `--chrome` | Enable Chrome browser integration | `claude --chrome` |
| `--no-chrome` | Disable Chrome browser integration | `claude --no-chrome` |
| `--ide` | Auto-connect to IDE if available | `claude --ide` |
| `--max-turns` | Limit agentic turns (non-interactive) | `claude -p --max-turns 3 "query"` |
| `--debug` | Enable debug mode with filtering | `claude --debug "api,mcp"` |
| `--enable-lsp-logging` | Enable verbose LSP logging | `claude --enable-lsp-logging` |
| `--betas` | Beta headers for API requests | `claude --betas interleaved-thinking` |
| `--plugin-dir` | Load plugins from directory (repeatable) | `claude --plugin-dir ./my-plugin` |
| `--enable-auto-mode` | Unlock auto permission mode | `claude --enable-auto-mode` |
| `--effort` | Set thinking effort level | `claude --effort high` |
| `--bare` | Minimal mode (skip hooks, skills, plugins, MCP, auto memory, CLAUDE.md) | `claude --bare` |
| `--channels` | Subscribe to MCP channel plugins | `claude --channels discord` |
| `--tmux` | Create tmux session for worktree | `claude --tmux` |
| `--fork-session` | Create new session ID when resuming | `claude --resume abc --fork-session` |
| `--max-budget-usd` | Maximum spend (print mode) | `claude -p --max-budget-usd 5.00 "query"` |
| `--json-schema` | Validated JSON output | `claude -p --json-schema '{"type":"object"}' "q"` |

### Platform & Theme Notes (v2.1.112)

- **PowerShell tool on Windows**: A dedicated PowerShell tool is rolling out on Windows and is controllable via environment variable.
- **Auto (match terminal) theme**: The new "Auto (match terminal)" theme syncs Claude Code's light/dark appearance with your terminal.
- **Quieter permission prompts**: Read-only `Bash` invocations and `Glob` patterns no longer trigger permission prompts.

### Advanced Examples

```bash
# Limit autonomous actions
claude -p --max-turns 5 "refactor this module"

# Debug API calls
claude --debug "api" "test query"

# Enable IDE integration
claude --ide "help me with this file"
```

## Agents Configuration

The `--agents` flag accepts a JSON object defining custom subagents for a session.

### Agents JSON Format

```json
{
  "agent-name": {
    "description": "Required: when to invoke this agent",
    "prompt": "Required: system prompt for the agent",
    "tools": ["Optional", "array", "of", "tools"],
    "model": "optional: sonnet|opus|haiku"
  }
}
```

**Required Fields:**
- `description` - Natural language description of when to use this agent
- `prompt` - System prompt that defines the agent's role and behavior

**Optional Fields:**
- `tools` - Array of available tools (inherits all if omitted)
  - Format: `["Read", "Grep", "Glob", "Bash"]`
- `model` - Model to use: `sonnet`, `opus`, or `haiku`

### Complete Agents Example

```json
{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  },
  "debugger": {
    "description": "Debugging specialist for errors and test failures.",
    "prompt": "You are an expert debugger. Analyze errors, identify root causes, and provide fixes.",
    "tools": ["Read", "Edit", "Bash", "Grep"],
    "model": "opus"
  },
  "documenter": {
    "description": "Documentation specialist for generating guides.",
    "prompt": "You are a technical writer. Create clear, comprehensive documentation.",
    "tools": ["Read", "Write"],
    "model": "haiku"
  }
}
```

### Agents Command Examples

```bash
# Define custom agents inline
claude --agents '{
  "security-auditor": {
    "description": "Security specialist for vulnerability analysis",
    "prompt": "You are a security expert. Find vulnerabilities and suggest fixes.",
    "tools": ["Read", "Grep", "Glob"],
    "model": "opus"
  }
}' "audit this codebase for security issues"

# Load agents from file
claude --agents "$(cat ~/.claude/agents.json)" "review the auth module"

# Combine with other flags
claude -p --agents "$(cat agents.json)" --model sonnet "analyze performance"
```

### Agent Priority

When multiple agent definitions exist, they are loaded in this priority order:
1. **CLI-defined** (`--agents` flag) - Session-specific
2. **Project-level** (`.claude/agents/`) - Current project
3. **User-level** (`~/.claude/agents/`) - All projects

CLI-defined agents override both project and user agents for the session. Project-level agents override user-level agents when their names collide. See [Lesson 04 — Subagents](../04-subagents/README.md#file-locations) for the full priority table including plugin-level agents.

---

## High-Value Use Cases

### 1. CI/CD Integration

Use Claude Code in your CI/CD pipelines for automated code review, testing, and documentation.

**GitHub Actions Example:**

```yaml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 1 \
            "Review the changes in this PR for:
            - Security vulnerabilities
            - Performance issues
            - Code quality
            Output as JSON with 'issues' array" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            // Process and post review comments
```

**Jenkins Pipeline:**

```groovy
pipeline {
    agent any
    stages {
        stage('AI Review') {
            steps {
                sh '''
                    claude -p --output-format json \
                      --max-turns 3 \
                      "Analyze test coverage and suggest missing tests" \
                      > coverage-analysis.json
                '''
            }
        }
    }
}
```

**Headless `ultrareview` (v2.1.120+):**

```yaml
# .github/workflows/ultrareview.yml
- name: Claude ultrareview
  run: claude ultrareview ${{ github.event.pull_request.number }} --json > review.json
```

`claude ultrareview` exits 0 on a clean review and 1 when findings are reported, so it's a drop-in PR gate. Use `--timeout <minutes>` to override the 30-minute default.

### 2. Script Piping

Process files, logs, and data through Claude for analysis.

**Log Analysis:**

```bash
# Analyze error logs
tail -1000 /var/log/app/error.log | claude -p "summarize these errors and suggest fixes"

# Find patterns in access logs
cat access.log | claude -p "identify suspicious access patterns"

# Analyze git history
git log --oneline -50 | claude -p "summarize recent development activity"
```

**Code Processing:**

```bash
# Review a specific file
cat src/auth.ts | claude -p "review this authentication code for security issues"

# Generate documentation
cat src/api/*.ts | claude -p "generate API documentation in markdown"

# Find TODOs and prioritize
grep -r "TODO" src/ | claude -p "prioritize these TODOs by importance"
```

### 3. Multi-Session Workflows

Manage complex projects with multiple conversation threads.

```bash
# Start a feature branch session
claude -r "feature-auth" "let's implement user authentication"

# Later, continue the session
claude -r "feature-auth" "add password reset functionality"

# Fork to try an alternative approach
claude --resume feature-auth --fork-session "try OAuth instead"

# Switch between different feature sessions
claude -r "feature-payments" "continue with Stripe integration"
```

### 4. Custom Agent Configuration

Define specialized agents for your team's workflows.

```bash
# Save agents config to file
cat > ~/.claude/agents.json << 'EOF'
{
  "reviewer": {
    "description": "Code reviewer for PR reviews",
    "prompt": "Review code for quality, security, and maintainability.",
    "model": "opus"
  },
  "documenter": {
    "description": "Documentation specialist",
    "prompt": "Generate clear, comprehensive documentation.",
    "model": "sonnet"
  },
  "refactorer": {
    "description": "Code refactoring expert",
    "prompt": "Suggest and implement clean code refactoring.",
    "tools": ["Read", "Edit", "Glob"]
  }
}
EOF

# Use agents in session
claude --agents "$(cat ~/.claude/agents.json)" "review the auth module"
```

### 5. Batch Processing

Process multiple queries with consistent settings.

```bash
# Process multiple files
for file in src/*.ts; do
  echo "Processing $file..."
  claude -p --model haiku "summarize this file: $(cat $file)" >> summaries.md
done

# Batch code review
find src -name "*.py" -exec sh -c '
  echo "## $1" >> review.md
  cat "$1" | claude -p "brief code review" >> review.md
' _ {} \;

# Generate tests for all modules
for module in $(ls src/modules/); do
  claude -p "generate unit tests for src/modules/$module" > "tests/$module.test.ts"
done
```

### 6. Security-Conscious Development

Use permission controls for safe operation.

```bash
# Read-only security audit
claude --permission-mode plan \
  --tools "Read,Grep,Glob" \
  "audit this codebase for security vulnerabilities"

# Block dangerous commands
claude --disallowedTools "Bash(rm:*)" "Bash(curl:*)" "Bash(wget:*)" \
  "help me clean up this project"

# Restricted automation
claude -p --max-turns 2 \
  --allowedTools "Read" "Glob" \
  "find all hardcoded credentials"
```

### 7. JSON API Integration

Use Claude as a programmable API for your tools with `jq` parsing.

```bash
# Get structured analysis
claude -p --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array"},"complexity":{"type":"string"}}}' \
  "analyze main.py and return function list with complexity rating"

# Integrate with jq for processing
claude -p --output-format json "list all API endpoints" | jq '.endpoints[]'

# Use in scripts
RESULT=$(claude -p --output-format json "is this code secure? answer with {secure: boolean, issues: []}" < code.py)
if echo "$RESULT" | jq -e '.secure == false' > /dev/null; then
  echo "Security issues found!"
  echo "$RESULT" | jq '.issues[]'
fi
```

### jq Parsing Examples

Parse and process Claude's JSON output using `jq`:

```bash
# Extract specific fields
claude -p --output-format json "analyze this code" | jq '.result'

# Filter array elements
claude -p --output-format json "list issues" | jq -r '.issues[] | select(.severity=="high")'

# Extract multiple fields
claude -p --output-format json "describe the project" | jq -r '.{name, version, description}'

# Convert to CSV
claude -p --output-format json "list functions" | jq -r '.functions[] | [.name, .lineCount] | @csv'

# Conditional processing
claude -p --output-format json "check security" | jq 'if .vulnerabilities | length > 0 then "UNSAFE" else "SAFE" end'

# Extract nested values
claude -p --output-format json "analyze performance" | jq '.metrics.cpu.usage'

# Process entire array
claude -p --output-format json "find todos" | jq '.todos | length'

# Transform output
claude -p --output-format json "list improvements" | jq 'map({title: .title, priority: .priority})'
```

---

## Models

Claude Code supports multiple models with different capabilities:

| Model | ID | Context Window | Notes |
|-------|-----|----------------|-------|
| Opus 4.7 | `claude-opus-4-7` | 1M tokens (1M context fix landed in v2.1.117) | Most capable, adaptive effort levels; `xhigh` is the default effort on Claude Code since Opus 4.7 launch (2026-04-16) |
| Sonnet 4.6 | `claude-sonnet-4-6` | 1M tokens | Balanced speed and capability; default effort for Pro/Max subscribers raised from `medium` to `high` in v2.1.117 |
| Haiku 4.5 | `claude-haiku-4-5` | 1M tokens | Fastest, best for quick tasks |

### Model Selection

```bash
# Use short names
claude --model opus "complex architectural review"
claude --model sonnet "implement this feature"
claude --model haiku -p "format this JSON"

# Use opusplan alias (Opus plans, Sonnet executes)
claude --model opusplan "design and implement the API"

# Toggle fast mode during session
/fast
```

### Effort Levels (Opus 4.7)

Opus 4.7 supports adaptive reasoning with effort levels, ordered from lightest to heaviest: `low` (○), `medium` (◐), `high` (●), `xhigh` (default on Claude Code since Opus 4.7 launch, 2026-04-16), and `max` (Opus 4.7 only). On Opus 4.6 / Sonnet 4.6, the default effort for Pro/Max subscribers was raised from `medium` to `high` in v2.1.117.

```bash
# Set effort level via CLI flag
claude --effort xhigh "complex review"

# Set effort level via slash command
/effort xhigh

# Set effort level via environment variable
export CLAUDE_CODE_EFFORT_LEVEL=xhigh   # low, medium, high, xhigh (default on Opus 4.7), or max (Opus 4.7 only)
```

The "ultrathink" keyword in prompts activates deep reasoning. The `max` effort level is exclusive to Opus 4.7.

---

## Key Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | API key for authentication |
| `ANTHROPIC_MODEL` | Override default model |
| `ANTHROPIC_CUSTOM_MODEL_OPTION` | Custom model option for API |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | Override default Opus model ID |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | Override default Sonnet model ID |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Override default Haiku model ID |
| `MAX_THINKING_TOKENS` | Set extended thinking token budget |
| `CLAUDE_CODE_EFFORT_LEVEL` | Set effort level (`low`/`medium`/`high`/`xhigh`/`max`) — `xhigh` is the default on Opus 4.7; `max` is Opus 4.7 only |
| `CLAUDE_CODE_SIMPLE` | Minimal mode, set by `--bare` flag |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | Disable automatic CLAUDE.md updates |
| `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` | Disable background task execution |
| `CLAUDE_CODE_DISABLE_CRON` | Disable scheduled/cron tasks |
| `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` | Disable git-related instructions |
| `CLAUDE_CODE_DISABLE_TERMINAL_TITLE` | Disable terminal title updates |
| `CLAUDE_CODE_DISABLE_1M_CONTEXT` | Disable 1M token context window |
| `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK` | Disable non-streaming fallback |
| `CLAUDE_CODE_ENABLE_TASKS` | Enable task list feature |
| `CLAUDE_CODE_TASK_LIST_ID` | Named task directory shared across sessions |
| `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` | Toggle prompt suggestions (`true`/`false`) |
| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | Enable experimental agent teams |
| `CLAUDE_CODE_NEW_INIT` | Use new initialization flow |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Model for subagent execution |
| `CLAUDE_CODE_PLUGIN_SEED_DIR` | Directory for plugin seed files |
| `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` | Env vars to scrub from subprocesses |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | Override auto-compaction percentage |
| `CLAUDE_STREAM_IDLE_TIMEOUT_MS` | Stream idle timeout in milliseconds |
| `SLASH_COMMAND_TOOL_CHAR_BUDGET` | Character budget for slash command tools |
| `ENABLE_TOOL_SEARCH` | Enable tool search capability |
| `MAX_MCP_OUTPUT_TOKENS` | Maximum tokens for MCP tool output |
| `CLAUDE_CODE_PERFORCE_MODE` | Set to `1` to enable Perforce mode — treats files as read-only by default (for Perforce/P4 version control workflows) (added v2.1.98) |
| `DISABLE_UPDATES` | Blocks all update paths including manual `claude update`. Stricter than `DISABLE_AUTOUPDATER`, which only blocks the background autoupdater (v2.1.118+) |
| `CLAUDE_CODE_HIDE_CWD` | When set to `1`, hides the current working directory in the startup logo (privacy / screen-share use) (v2.1.119+) |
| `CLAUDE_CODE_FORK_SUBAGENT` | Set to `1` to enable forked subagents on external builds (Bedrock, Vertex, Foundry). No effect on Anthropic API where forked subagents are GA (v2.1.117+) |
| `OTEL_LOG_TOOL_DETAILS` | Set to `1` to unredact custom and MCP command names in OpenTelemetry events (v2.1.117+). Redaction remains the default. |
| `ANTHROPIC_BEDROCK_SERVICE_TIER` | Selects the Bedrock service tier: `default`, `flex`, or `priority` (v2.1.122+) |
| `AI_AGENT` | Set automatically on subprocesses so external CLIs (e.g., `gh`) can attribute traffic to Claude Code (v2.1.120+) |

> **`ENABLE_TOOL_SEARCH` on Vertex AI (v2.1.119+)**: Tool search is **disabled by default on Google Cloud Vertex AI** deployments. Users who want the tool-search capability on Vertex must explicitly opt in with `export ENABLE_TOOL_SEARCH=true`. On direct Anthropic API it remains enabled by default.

---

## Quick Reference

### Most Common Commands

```bash
# Interactive session
claude

# Quick question
claude -p "how do I..."

# Continue conversation
claude -c

# Process a file
cat file.py | claude -p "review this"

# JSON output for scripts
claude -p --output-format json "query"
```

### Flag Combinations

| Use Case | Command |
|----------|---------|
| Quick code review | `cat file | claude -p "review"` |
| Structured output | `claude -p --output-format json "query"` |
| Safe exploration | `claude --permission-mode plan` |
| Autonomous with safety | `claude --enable-auto-mode --permission-mode auto` |
| CI/CD integration | `claude -p --max-turns 3 --output-format json` |
| Resume work | `claude -r "session-name"` |
| Custom model | `claude --model opus "complex task"` |
| Minimal mode | `claude --bare "quick query"` |
| Budget-capped run | `claude -p --max-budget-usd 2.00 "analyze code"` |

---

## Troubleshooting

### Command Not Found

**Problem:** `claude: command not found`

**Solutions:**
- Install Claude Code: `npm install -g @anthropic-ai/claude-code`
- Check PATH includes npm global bin directory
- Try running with full path: `npx claude`

### API Key Issues

**Problem:** Authentication failed

**Solutions:**
- Set API key: `export ANTHROPIC_API_KEY=your-key`
- Check key is valid and has sufficient credits
- Verify key permissions for the model requested

### Session Not Found

**Problem:** Cannot resume session

**Solutions:**
- List available sessions to find correct name/ID
- Sessions may expire after period of inactivity
- Use `-c` to continue most recent session

### Output Format Issues

**Problem:** JSON output is malformed

**Solutions:**
- Use `--json-schema` to enforce structure
- Add explicit JSON instructions in prompt
- Use `--output-format json` (not just asking for JSON in prompt)

### Permission Denied

**Problem:** Tool execution blocked

**Solutions:**
- Check `--permission-mode` setting
- Review `--allowedTools` and `--disallowedTools` flags
- Use `--dangerously-skip-permissions` for automation (with caution)

---

## Additional Resources

- **[Official CLI Reference](https://code.claude.com/docs/en/cli-reference)** - Complete command reference
- **[Headless Mode Documentation](https://code.claude.com/docs/en/headless)** - Automated execution
- **[Slash Commands](../01-slash-commands/)** - Custom shortcuts within Claude
- **[Memory Guide](../02-memory/)** - Persistent context via CLAUDE.md
- **[MCP Protocol](../05-mcp/)** - External tool integrations
- **[Advanced Features](../09-advanced-features/)** - Planning mode, extended thinking
- **[Subagents Guide](../04-subagents/)** - Delegated task execution

---

*Part of the [Claude How To](../) guide series*

---

**Last Updated**: May 2, 2026
**Claude Code Version**: 2.1.126
**Sources**:
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/changelog
- https://www.anthropic.com/news/claude-opus-4-7
- https://github.com/anthropics/claude-code/releases/tag/v2.1.113
- https://github.com/anthropics/claude-code/releases/tag/v2.1.116
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.118
- https://github.com/anthropics/claude-code/releases/tag/v2.1.126
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
