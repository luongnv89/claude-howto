![Claude How To](../claude-howto-logo.svg)

# Advanced Features

Comprehensive guide to Claude Code's advanced capabilities including planning mode, extended thinking, background tasks, permission modes, headless operation, session management, interactive features, and configuration.

## Table of Contents

1. [Overview](#overview)
2. [Planning Mode](#planning-mode)
3. [Extended Thinking](#extended-thinking)
4. [Background Tasks](#background-tasks)
5. [Permission Mode](#permission-mode)
6. [Headless Mode](#headless-mode)
7. [Session Management](#session-management)
8. [Interactive Features](#interactive-features)
9. [Configuration and Settings](#configuration-and-settings)
10. [Best Practices](#best-practices)
11. [Related Concepts](#related-concepts)

---

## Overview

Advanced features in Claude Code extend the core capabilities with planning, reasoning, automation, and control mechanisms. These features enable sophisticated workflows for complex development tasks, code review, automation, and multi-session management.

**Key advanced features include:**
- **Planning Mode**: Create detailed implementation plans before coding
- **Extended Thinking**: Deep reasoning for complex problems
- **Background Tasks**: Run long operations without blocking the conversation
- **Permission Modes**: Control what Claude can do (unrestricted, confirm, read-only, custom)
- **Headless Mode**: Run Claude Code without interactive input for automation and CI/CD
- **Session Management**: Manage multiple work sessions
- **Interactive Features**: Keyboard shortcuts, multi-line input, and command history
- **Configuration**: Customize behavior with JSON configuration files

---

## Planning Mode

Planning mode allows Claude to think through complex tasks before implementing them, creating a detailed plan that you can review and approve.

### What is Planning Mode?

Planning mode is a two-phase approach:
1. **Planning Phase**: Claude analyzes the task and creates a detailed implementation plan
2. **Implementation Phase**: After approval, Claude executes the plan

### When to Use Planning Mode

✅ Use planning mode for:
- Complex multi-file refactoring
- New feature implementations
- Architectural changes
- Database migrations
- Major API redesigns

❌ Don't use planning mode for:
- Simple bug fixes
- Formatting changes
- Single-file edits
- Quick queries

### Activating Planning Mode

**Explicit activation**:
```bash
/plan Implement user authentication system
```

**Automatic activation**:
Claude automatically enters planning mode for complex tasks:
```
User: Refactor the entire API to use microservices architecture

Claude: This is a complex task. Let me create a plan first...
[Enters planning mode]
```

### Benefits of Planning Mode

- **Clear roadmap with time estimates**: Detailed breakdown of implementation steps
- **Risk assessment**: Identify potential issues before implementation
- **Systematic task breakdown**: Organized phases and milestones
- **Opportunity for review and modification**: Approve or adjust the plan before execution

### Example: Feature Implementation

```
User: /plan Add a real-time notification system

Claude: I'll create a plan for implementing real-time notifications.

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

Estimated time: 3-4 hours
Files to modify: 12
New files to create: 8

Ready to proceed? (yes/no/modify plan)

User: yes

Claude: [Begins implementation following the plan]
```

### Plan Modifications

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[Shows modified plan with queue removed]

User: Looks good, proceed

Claude: [Implements modified plan]
```

### Planning Mode Configuration

```json
{
  "planning": {
    "autoEnter": true,
    "complexityThreshold": 3,
    "requireApproval": true,
    "showTimeEstimates": true
  }
}
```

---

## Extended Thinking

Extended thinking allows Claude to spend more time reasoning about complex problems before providing a solution.

### What is Extended Thinking?

Extended thinking is a deliberate, step-by-step reasoning process where Claude:
- Breaks down complex problems
- Considers multiple approaches
- Evaluates trade-offs
- Reasons through edge cases

### Activating Extended Thinking

**Explicit activation**:
```bash
/think Should we use microservices or monolith?
```

**Automatic activation**:
For sufficiently complex queries, Claude automatically uses extended thinking.

### Benefits of Extended Thinking

- **Thorough analysis of trade-offs**: Examine pros and cons systematically
- **Better architectural decisions**: Make informed choices with comprehensive evaluation
- **Consideration of edge cases**: Think through potential issues and scenarios
- **Systematic evaluation**: Structured approach to complex problem-solving

### Example: Architectural Decision

```
User: /think Should we use microservices or a monolith for our e-commerce platform?

Claude: Let me think through this architectural decision carefully...

<extended_thinking>
## Context Analysis
- Team size: 5 developers
- Expected traffic: 10k daily users initially
- Need to scale to 100k+ users
- Limited DevOps resources
- 6-month timeline to MVP

## Approach 1: Microservices
Pros:
+ Independent scaling
+ Technology flexibility
+ Team independence
+ Fault isolation

Cons:
- Operational complexity
- Network overhead
- Distributed tracing needed
- Requires DevOps expertise
- Slower initial development

## Approach 2: Monolith
Pros:
+ Simpler deployment
+ Faster initial development
+ Easier debugging
+ Lower operational overhead
+ Single codebase

Cons:
- Scaling challenges later
- All-or-nothing deployments
- Technology lock-in
- Potential for tight coupling

## Decision Factors
1. Team size (5 devs) → Favors monolith
2. DevOps resources (limited) → Favors monolith
3. Timeline (6 months) → Favors monolith
4. Future scale (100k users) → Achievable with monolith + caching
5. Complexity budget → Limited

## Recommendation
Start with a **modular monolith**:
- Single deployment unit
- Clear module boundaries
- Clean interfaces between modules
- Prepare for future extraction to microservices if needed

This gives you:
✓ Fast initial development
✓ Low operational complexity
✓ Option to extract services later
✓ Clear architecture

Migration path: When you reach 50k+ users or specific modules need independent scaling, extract those modules into microservices.
</extended_thinking>

**Recommendation**: Implement a modular monolith with clean module boundaries.

This approach balances your current constraints (team size, timeline, DevOps resources) with future scalability needs. You can migrate specific modules to microservices later when there's a clear business need.
```

### Extended Thinking Configuration

```json
{
  "extendedThinking": {
    "enabled": true,
    "showThinkingProcess": true,
    "minThinkingTime": 5,
    "maxThinkingTime": 60
  }
}
```

---

## Background Tasks

Background tasks allow long-running operations to execute without blocking your conversation.

### What Are Background Tasks?

Background tasks run asynchronously while you continue working:
- Long test suites
- Build processes
- Database migrations
- Deployment scripts
- Analysis tools

**Basic Usage:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### Starting Background Tasks

```
User: Run the full test suite in the background

Claude: Starting tests in background (task-id: bg-1234)
You can continue working while tests run.

[You can continue the conversation]

User: Meanwhile, let's refactor the auth module

Claude: [Works on auth module while tests run in background]

[Later, when tests complete]

Claude: 📢 Background task bg-1234 completed:
✅ 245 tests passed
❌ 3 tests failed
View results: /task show bg-1234
```

### Managing Background Tasks

**List active tasks**:
```
User: /task list

Active background tasks:
1. [bg-1234] Running tests (50% complete, 2min remaining)
2. [bg-1235] Building Docker image (25% complete, 8min remaining)
3. [bg-1236] Deploying to staging (90% complete, 30sec remaining)
```

**Check task status**:
```
User: /task status bg-1234

Task bg-1234: Running tests
Status: In progress
Progress: 120/245 tests (49%)
Started: 2025-11-08 10:30:15
Estimated completion: 2025-11-08 10:34:22
```

**View task output**:
```
User: /task show bg-1234

[Shows live output from the test run]
```

**Cancel task**:
```
User: /task cancel bg-1234

Cancelled background task bg-1234
```

### Example: Parallel Development

```
User: Run the build in the background

Claude: Starting build... (task-id: bg-5001)

User: Also run the linter in background

Claude: Starting linter... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [Implements API endpoint while build and linter run]

[10 minutes later]

Claude: 📢 Build completed successfully (bg-5001)
📢 Linter found 12 issues (bg-5002)

User: Show me the linter issues

Claude: [Shows linter output from bg-5002]
```

### Configuration

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## Permission Mode

Permission mode controls what actions Claude can take without explicit approval.

### Permission Modes Table

| Mode | Description | Use Case |
|------|-------------|----------|
| **Unrestricted** | Full access (default) | Active development |
| **Confirm** | Ask before actions | Learning, pair programming |
| **Read-only** | Analysis only | Code review |
| **Custom** | Granular permissions | Fine-tuned control |

### Permission Commands

```bash
/permission readonly      # Code review mode
/permission confirm       # Learning mode
/permission unrestricted  # Full automation
```

### Permission Levels

#### 1. Unrestricted Mode (Default)
Claude can use all tools freely.

```
User: /permission unrestricted
```

#### 2. Confirmation Mode
Claude asks before taking actions.

```
User: /permission confirm

User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)

User: show

Claude: [Shows the exact changes]

User: yes

Claude: [Makes the change]
```

#### 3. Read-Only Mode
Claude can only read files, not modify them.

```
User: /permission readonly

User: Fix the bug in auth.ts

Claude: I'm in read-only mode. I can analyze the bug and show you the fix, but I cannot modify files.

Here's the bug and suggested fix:
[Shows analysis and proposed changes]
```

#### 4. Custom Permission Sets

```json
{
  "permissions": {
    "mode": "custom",
    "allowed": ["Read", "Grep", "Glob"],
    "blocked": ["Write", "Edit", "Bash"],
    "requireConfirmation": ["Git"]
  }
}
```

### Use Cases

**Code Review**:
```
User: /permission readonly
User: Review this PR and suggest improvements

Claude: [Reads code, provides feedback, but cannot modify]
```

**Pair Programming**:
```
User: /permission confirm
User: Let's implement the feature together

Claude: [Asks for approval before each change]
```

**Automated Tasks**:
```
User: /permission unrestricted
User: Run the full deployment pipeline

Claude: [Executes all steps without asking]
```

---

## Headless Mode

Headless mode allows Claude Code to run without interactive input, perfect for automation and CI/CD.

### What is Headless Mode?

Headless mode enables:
- Automated script execution
- CI/CD integration
- Batch processing
- Scheduled tasks

### Running in Headless Mode

```bash
# Run specific task
claude-code --headless --task "Run all tests"

# From script file
claude-code --headless --script ./deploy.claude

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude-code --headless --task "Review PR"
```

### Additional Headless Usage Examples

```bash
# Run a specific task with output capture
claude-code --headless --task "Run all tests and generate coverage report"

# Run from a script file
claude-code --headless --script ./tasks/deploy.claude

# With input from stdin
echo "Analyze code quality" | claude-code --headless
```

### Example: CI/CD Integration

**GitHub Actions**:
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Run Claude Code Review
        run: |
          claude-code --headless --task "Review this PR for:
          - Code quality issues
          - Security vulnerabilities
          - Performance concerns
          - Test coverage
          Output results to review-report.md"

      - name: Post Review Comment
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('review-report.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: report
            });
```

### Task Scripts

**deploy.claude**:
```
# Automated deployment script

1. Run full test suite
2. If tests pass, build production bundle
3. Run security scan
4. If scan passes, deploy to staging
5. Run smoke tests on staging
6. If smoke tests pass, deploy to production
7. Send notification to team
```

Run it:
```bash
claude-code --headless --script deploy.claude
```

### Configuration

```json
{
  "headless": {
    "exitOnError": true,
    "verbose": true,
    "timeout": 3600,
    "logFile": "./claude-headless.log"
  }
}
```

---

## Session Management

Manage multiple Claude Code sessions effectively.

### Session Management Commands

```bash
/session list           # Show all sessions
/session new "Feature"  # Create new session
/session switch "Bug"   # Switch sessions
/session save           # Save current state
/session load "name"    # Load saved session
```

### Session Commands Details

**List sessions**:
```
User: /session list

Active sessions:
1. [session-abc] Main development (started 2h ago)
2. [session-def] Bug investigation (started 30m ago)
3. [session-ghi] Refactoring (started 5m ago)
```

**Switch sessions**:
```
User: /session switch session-def

Switched to session "Bug investigation"
```

**Create new session**:
```
User: /session new "Feature: User profiles"

Created new session: session-jkl
```

**Save session**:
```
User: /session save "Before major refactor"

Session saved as checkpoint
```

**Load session**:
```
User: /session load "Before major refactor"

Loaded session from checkpoint
```

### Session Persistence

Sessions are automatically saved and can be resumed:

```bash
# Resume last session
claude-code --resume

# Resume specific session
claude-code --session session-abc

# Start fresh session
claude-code --new
```

### Session Configuration

```json
{
  "sessions": {
    "autoSave": true,
    "autoSaveInterval": 300,
    "maxSessions": 10,
    "persistHistory": true
  }
}
```

---

## Interactive Features

### Keyboard Shortcuts

Claude Code supports keyboard shortcuts for efficiency:

**Basic Navigation and Input:**
- `Ctrl + R` - Search command history
- `Tab` - Autocomplete
- `↑ / ↓` - Command history
- `Ctrl + L` - Clear screen

**Extended Shortcuts:**

| Shortcut | Action |
|----------|--------|
| `Ctrl + C` | Cancel current operation |
| `Ctrl + D` | Exit Claude Code |
| `Ctrl + L` | Clear screen |
| `Ctrl + R` | Search command history |
| `Ctrl + P` | Previous command |
| `Ctrl + N` | Next command |
| `Ctrl + A` | Move to line start |
| `Ctrl + E` | Move to line end |
| `Ctrl + K` | Cut to end of line |
| `Ctrl + U` | Cut to start of line |
| `Ctrl + W` | Delete word backward |
| `Ctrl + Y` | Paste (yank) |
| `Ctrl + Z` | Suspend (background) |
| `Tab` | Autocomplete |
| `↑ / ↓` | Command history |

### Tab Completion

Claude Code provides intelligent tab completion:

```
User: /che<TAB>
→ /checkpoint

User: /checkpoint <TAB>
→ /checkpoint list
→ /checkpoint save
→ /checkpoint rewind
→ /checkpoint delete

User: /checkpoint save<TAB>
→ Shows recent checkpoint names
```

### Command History

Access previous commands:

```
User: <↑>  # Previous command
User: <↓>  # Next command
User: Ctrl+R  # Search history

(reverse-i-search)`test': run all tests
```

### Multi-line Input

For complex queries, use multi-line mode:

```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

**Example:**

```
User: \
> Implement a user authentication system
> with the following requirements:
> - JWT tokens
> - Email verification
> - Password reset
> - 2FA support
> \end

Claude: [Processes the multi-line request]
```

### Inline Editing

Edit commands before sending:

```
User: Deploy to prodcution<Backspace><Backspace>uction

[Edit in-place before sending]
```

---

## Configuration and Settings

### Configuration File Locations

1. **Global config**: `~/.claude/config.json`
2. **Project config**: `./.claude/config.json`
3. **User config**: `~/.config/claude-code/settings.json`

### Complete Configuration Example

**Core advanced features configuration:**

```json
{
  "planning": {
    "autoEnter": true,
    "requireApproval": true
  },
  "extendedThinking": {
    "enabled": true,
    "showThinkingProcess": true
  },
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5
  },
  "permissions": {
    "mode": "unrestricted"
  },
  "headless": {
    "exitOnError": true,
    "verbose": true
  }
}
```

**Extended configuration example:**

```json
{
  "general": {
    "model": "claude-sonnet-4-5",
    "temperature": 0.7,
    "maxTokens": 8000,
    "theme": "dark"
  },

  "planning": {
    "autoEnter": true,
    "complexityThreshold": 3,
    "requireApproval": true,
    "showTimeEstimates": true
  },

  "extendedThinking": {
    "enabled": true,
    "showThinkingProcess": true,
    "minThinkingTime": 5,
    "maxThinkingTime": 60
  },

  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  },

  "permissions": {
    "mode": "unrestricted",
    "requireConfirmationFor": ["Bash:rm", "Git:push --force"],
    "blockedCommands": ["dd", "mkfs", "format"]
  },

  "sessions": {
    "autoSave": true,
    "autoSaveInterval": 300,
    "maxSessions": 10,
    "persistHistory": true
  },

  "checkpoints": {
    "autoCheckpoint": true,
    "autoCheckpointInterval": 30,
    "maxCheckpoints": 20,
    "compressionEnabled": true
  },

  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh",
    "PreCommit": "npm test",
    "UserPromptSubmit": "~/.claude/hooks/validate.sh"
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  },

  "ui": {
    "colorEnabled": true,
    "emojiEnabled": true,
    "showProgress": true,
    "compactMode": false,
    "lineNumbers": true
  },

  "performance": {
    "cacheEnabled": true,
    "cacheTTL": 3600,
    "parallelTasks": true,
    "maxParallelTasks": 3
  },

  "logging": {
    "level": "info",
    "file": "~/.claude/logs/claude-code.log",
    "maxSize": "10MB",
    "maxFiles": 5
  }
}
```

### Environment Variables

Override config with environment variables:

```bash
# Model selection
export CLAUDE_MODEL=claude-opus-4

# API configuration
export ANTHROPIC_API_KEY=sk-ant-...

# Feature toggles
export CLAUDE_PLANNING_MODE=true
export CLAUDE_EXTENDED_THINKING=true

# Permissions
export CLAUDE_PERMISSION_MODE=confirm

# Logging
export CLAUDE_LOG_LEVEL=debug
```

### Configuration Management Commands

```
User: /config show
[Shows current configuration]

User: /config set planning.autoEnter false
[Updates configuration]

User: /config reset
[Resets to defaults]

User: /config export ~/my-claude-config.json
[Exports configuration]

User: /config import ~/my-claude-config.json
[Imports configuration]
```

### Per-Project Configuration

Create `.claude/config.json` in your project:

```json
{
  "hooks": {
    "PreCommit": "npm test && npm run lint"
  },
  "permissions": {
    "mode": "confirm"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

## Best Practices

### Planning Mode
- ✅ Use for complex multi-step tasks
- ✅ Review plans before approving
- ✅ Modify plans when needed
- ❌ Don't use for simple tasks

### Extended Thinking
- ✅ Use for architectural decisions
- ✅ Use for complex problem-solving
- ✅ Review the thinking process
- ❌ Don't use for simple queries

### Background Tasks
- ✅ Use for long-running operations
- ✅ Monitor task progress
- ✅ Handle task failures gracefully
- ❌ Don't start too many concurrent tasks

### Permissions
- ✅ Use read-only for code review
- ✅ Use confirm for learning
- ✅ Use unrestricted for automation
- ❌ Don't stay in restrictive modes unnecessarily

### Sessions
- ✅ Use separate sessions for different tasks
- ✅ Save important session states
- ✅ Clean up old sessions
- ❌ Don't mix unrelated work in one session

---

## Related Concepts

For more information about Claude Code and related features, see:

- [Main Claude Code Guide](../README.md)
- [Slash Commands](../01-slash-commands/)
- [Memory](../02-memory/)
- [Skills](../03-skills/)
- [Subagents](../04-subagents/)
- [MCP](../05-mcp/)
- [Hooks](../06-hooks/)
- [Plugins](../07-plugins/)
- [Checkpoints](../08-checkpoints/)
- [Claude Documentation](https://docs.claude.com)
- [MCP GitHub Servers](https://github.com/modelcontextprotocol/servers)
