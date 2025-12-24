![Claude How To](../claude-howto-logo.svg)

# Hooks

Hooks are automated scripts that execute in response to specific events during Claude Code sessions. They enable automation, validation, permission management, and custom workflows.

## Overview

Hooks are shell commands or LLM prompts that execute automatically when specific events occur in Claude Code. They receive JSON input via stdin and communicate results via exit codes and JSON stdout output.

**Key features:**
- Event-driven automation
- JSON-based input/output
- Support for command and prompt-based hooks
- Pattern matching for tool-specific hooks

## Configuration

Hooks are configured in settings files with a specific structure:

- `~/.claude/settings.json` - User settings (global)
- `.claude/settings.json` - Project settings (committed)
- `.claude/settings.local.json` - Local project settings (not committed)

### Basic Configuration Structure

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**Key fields:**

| Field | Description | Example |
|-------|-------------|---------|
| `matcher` | Pattern to match tool names (case-sensitive) | `"Write"`, `"Edit\|Write"`, `"*"` |
| `hooks` | Array of hook definitions | `[{ "type": "command", ... }]` |
| `type` | Hook type: `"command"` (bash) or `"prompt"` (LLM) | `"command"` |
| `command` | Shell command to execute | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | Optional timeout in seconds (default 60) | `30` |

### Matcher Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| Exact string | Matches specific tool | `"Write"` |
| Regex pattern | Matches multiple tools | `"Edit\|Write"` |
| Wildcard | Matches all tools | `"*"` or `""` |
| MCP tools | Server and tool pattern | `"mcp__memory__.*"` |

## Hook Events

Claude Code supports **9 hook events**:

| Event | When Triggered | Supports Matchers | Can Block | Common Use |
|-------|---------------|-------------------|-----------|------------|
| **PreToolUse** | Before tool execution | Yes (tool names) | Yes | Validate, modify inputs |
| **PermissionRequest** | Permission dialog shown | Yes (tool names) | Yes | Auto-approve/deny |
| **PostToolUse** | After tool completion | Yes (tool names) | Yes (block) | Add context, feedback |
| **Notification** | Notification sent | Yes (notification types) | No | Custom notifications |
| **UserPromptSubmit** | Before prompt processed | No | Yes | Validate prompts |
| **Stop** | Agent finishes responding | No | Yes | Task completion check |
| **SubagentStop** | Subagent finishes | No | Yes | Subagent validation |
| **PreCompact** | Before compact operation | Yes (manual/auto) | No | Pre-compact actions |
| **SessionStart** | Session begins/resumes | Yes (startup/resume/clear/compact) | No | Environment setup |
| **SessionEnd** | Session ends | No | No | Cleanup |

### PreToolUse

Runs after Claude creates tool parameters and before processing. Use this to validate or modify tool inputs.

**Configuration:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py"
          }
        ]
      }
    ]
  }
}
```

**Common matchers:** `Task`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**Output control:**
- `permissionDecision`: `"allow"`, `"deny"`, or `"ask"`
- `permissionDecisionReason`: Explanation for decision
- `updatedInput`: Modified tool input parameters

### PostToolUse

Runs immediately after tool completion. Use for verification, logging, or providing context back to Claude.

**Configuration:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py"
          }
        ]
      }
    ]
  }
}
```

**Output control:**
- `"block"` decision prompts Claude with feedback
- `additionalContext`: Context added for Claude

### UserPromptSubmit

Runs when user submits a prompt, before Claude processes it.

**Configuration:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py"
          }
        ]
      }
    ]
  }
}
```

**Output control:**
- `decision`: `"block"` to prevent processing
- `reason`: Explanation if blocked
- `additionalContext`: Context added to prompt

### Stop and SubagentStop

Run when Claude finishes responding (Stop) or a subagent completes (SubagentStop). Supports prompt-based evaluation for intelligent task completion checking.

**Configuration:**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Evaluate if Claude completed all requested tasks.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### SessionStart

Runs when session starts or resumes. Can persist environment variables.

**Matchers:** `startup`, `resume`, `clear`, `compact`

**Special feature:** Use `CLAUDE_ENV_FILE` to persist environment variables:

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

## Hook Input and Output

### JSON Input (via stdin)

All hooks receive JSON input via stdin:

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.js",
    "content": "..."
  },
  "tool_use_id": "toolu_01ABC123..."
}
```

### Exit Codes

| Exit Code | Meaning | Behavior |
|-----------|---------|----------|
| **0** | Success | Continue, parse JSON stdout |
| **2** | Blocking error | Block operation, stderr shown as error |
| **Other** | Non-blocking error | Continue, stderr shown in verbose mode |

### JSON Output (stdout, exit code 0)

```json
{
  "continue": true,
  "stopReason": "Optional message if stopping",
  "suppressOutput": false,
  "systemMessage": "Optional warning message",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "File is in allowed directory",
    "updatedInput": {
      "file_path": "/modified/path.js"
    }
  }
}
```

## Environment Variables

| Variable | Availability | Description |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | All hooks | Absolute path to project root |
| `CLAUDE_ENV_FILE` | SessionStart only | File path for persisting env vars |
| `CLAUDE_CODE_REMOTE` | All hooks | `"true"` if running in web environment |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin hooks | Path to plugin directory |

## Prompt-Based Hooks

For `Stop` and `SubagentStop` events, you can use LLM-based evaluation:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if all tasks are complete. Return your decision.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**LLM Response Schema:**
```json
{
  "decision": "approve",
  "reason": "All tasks completed successfully",
  "continue": false,
  "stopReason": "Task complete"
}
```

## Examples

### Example 1: Bash Command Validator (PreToolUse)

**File:** `.claude/hooks/validate-bash.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"\brm\s+-rf\s+/", "Blocking dangerous rm -rf / command"),
    (r"\bsudo\s+rm", "Blocking sudo rm command"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name != "Bash":
        sys.exit(0)

    command = input_data.get("tool_input", {}).get("command", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, command):
            print(message, file=sys.stderr)
            sys.exit(2)  # Exit 2 = blocking error

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**Configuration:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\""
          }
        ]
      }
    ]
  }
}
```

### Example 2: Security Scanner (PostToolUse)

**File:** `.claude/hooks/security-scan.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

SECRET_PATTERNS = [
    (r"password\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded password"),
    (r"api[_-]?key\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded API key"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    file_path = tool_input.get("file_path", "")

    warnings = []
    for pattern, message in SECRET_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            warnings.append(message)

    if warnings:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Security warnings for {file_path}: " + "; ".join(warnings)
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Example 3: Auto-Format Code (PostToolUse)

**File:** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# Read JSON from stdin
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# Format based on file extension
case "$FILE_PATH" in
    *.js|*.jsx|*.ts|*.tsx|*.json)
        command -v prettier &>/dev/null && prettier --write "$FILE_PATH" 2>/dev/null
        ;;
    *.py)
        command -v black &>/dev/null && black "$FILE_PATH" 2>/dev/null
        ;;
    *.go)
        command -v gofmt &>/dev/null && gofmt -w "$FILE_PATH" 2>/dev/null
        ;;
esac

exit 0
```

### Example 4: Prompt Validator (UserPromptSubmit)

**File:** `.claude/hooks/validate-prompt.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"delete\s+(all\s+)?database", "Dangerous: database deletion"),
    (r"rm\s+-rf\s+/", "Dangerous: root deletion"),
]

def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("user_prompt", "") or input_data.get("prompt", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            output = {
                "decision": "block",
                "reason": f"Blocked: {message}"
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Example 5: Intelligent Stop Hook (Prompt-Based)

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if Claude completed all requested tasks. Check: 1) Were all files created/modified? 2) Were there unresolved errors? If incomplete, explain what's missing.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### Example 6: Context Usage Reporter (Stop Hook)

This example shows how to create a hook that reports context/token usage after each Claude response. It reads the conversation transcript and estimates token usage.

**How it works:**

1. The hook receives `transcript_path` in the JSON input - this points to a JSONL file containing all conversation messages
2. The script reads the transcript file and calculates total character count
3. It estimates tokens using a simple heuristic (~4 characters per token)
4. Outputs a one-line report showing estimated usage vs model capacity

**File:** `.claude/hooks/context-usage.py`

```python
#!/usr/bin/env python3
"""
Context Usage Reporter Hook

Reports estimated context/token usage after each Claude response.
Uses the transcript_path field to read conversation history and estimate tokens.

Limitations:
- Token count is an ESTIMATE (~4 chars/token average)
- Actual token usage depends on the tokenizer and includes system prompts
- Use /context command for accurate real-time usage
"""
import json
import sys
import os

# Model context limits (adjust based on your model)
MODEL_LIMITS = {
    "default": 200000,  # Claude Opus 4.5 / Sonnet
    "haiku": 200000,
}

def read_transcript(transcript_path: str) -> list:
    """Read JSONL transcript file and return list of messages."""
    messages = []
    if not os.path.exists(transcript_path):
        return messages

    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    messages.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return messages

def calculate_usage(messages: list) -> tuple[int, int]:
    """Calculate total characters and estimated tokens from messages."""
    total_chars = 0

    for msg in messages:
        # Handle different message formats in transcript
        if isinstance(msg, dict):
            # Check common content fields
            content = msg.get('content', '')
            if isinstance(content, str):
                total_chars += len(content)
            elif isinstance(content, list):
                # Handle content blocks (text, tool_use, etc.)
                for block in content:
                    if isinstance(block, dict):
                        text = block.get('text', '') or block.get('content', '')
                        total_chars += len(str(text))
                    elif isinstance(block, str):
                        total_chars += len(block)

            # Also count tool inputs/outputs
            tool_input = msg.get('tool_input', {})
            if tool_input:
                total_chars += len(json.dumps(tool_input))

    estimated_tokens = total_chars // 4  # ~4 characters per token
    return total_chars, estimated_tokens

def main():
    # Read hook input from stdin
    input_data = json.load(sys.stdin)

    # Get transcript path from hook input
    transcript_path = input_data.get('transcript_path', '')

    if not transcript_path:
        # No transcript available, exit silently
        sys.exit(0)

    # Read and analyze transcript
    messages = read_transcript(transcript_path)
    total_chars, estimated_tokens = calculate_usage(messages)

    # Get model limit (default to 200k)
    max_tokens = MODEL_LIMITS.get("default", 200000)

    # Calculate percentages
    used_percent = (estimated_tokens / max_tokens) * 100
    remaining_tokens = max_tokens - estimated_tokens
    remaining_percent = 100 - used_percent

    # Format the report (output as systemMessage so it appears in UI)
    report = f"Context: ~{estimated_tokens:,}/{max_tokens:,} tokens ({remaining_percent:.1f}% remaining)"

    # Output JSON with systemMessage to show in Claude Code UI
    output = {
        "systemMessage": report
    }
    print(json.dumps(output))
    sys.exit(0)

if __name__ == "__main__":
    main()
```

**Configuration:**

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-usage.py\"",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

**Sample Output:**

After each Claude response, you'll see a message like:
```
Context: ~45,230/200,000 tokens (77.4% remaining)
```

**Key Points:**

| Aspect | Details |
|--------|---------|
| **Event** | `Stop` - runs after Claude finishes responding |
| **Input** | Uses `transcript_path` field to access conversation history |
| **Estimation** | ~4 characters per token (rough heuristic) |
| **Output** | `systemMessage` field displays in Claude Code UI |
| **Accuracy** | Estimate only - use `/context` for exact counts |

**Why use Stop hook instead of UserPromptSubmit?**

- `Stop` runs after Claude responds, giving a more complete picture
- `UserPromptSubmit` runs before Claude processes, missing the response
- Both work, but `Stop` shows total usage including Claude's response

**Alternative: UserPromptSubmit for Pre-Response Check**

If you want to check context BEFORE Claude processes your prompt:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-usage.py\""
          }
        ]
      }
    ]
  }
}
```

## MCP Tool Hooks

MCP tools follow the pattern `mcp__<server>__<tool>`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"systemMessage\": \"Memory operation logged\"}'"
          }
        ]
      }
    ]
  }
}
```

## Security Considerations

### Disclaimer

**USE AT YOUR OWN RISK**: Hooks execute arbitrary shell commands. You are solely responsible for:
- Commands you configure
- File access/modification permissions
- Potential data loss or system damage
- Testing hooks in safe environments before production use

### Best Practices

| Do | Don't |
|-----|-------|
| Validate and sanitize all inputs | Trust input data blindly |
| Quote shell variables: `"$VAR"` | Use unquoted: `$VAR` |
| Block path traversal (`..`) | Allow arbitrary paths |
| Use absolute paths with `$CLAUDE_PROJECT_DIR` | Hardcode paths |
| Skip sensitive files (`.env`, `.git/`, keys) | Process all files |
| Test hooks in isolation first | Deploy untested hooks |

## Debugging

### Enable Debug Mode

Run Claude with debug flag for detailed hook logs:

```bash
claude --debug
```

### Verbose Mode

Use `Ctrl+O` in Claude Code to enable verbose mode and see hook execution progress.

### Test Hooks Independently

```bash
# Test with sample JSON input
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# Check exit code
echo $?
```

## Complete Configuration Example

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/format-code.sh\"",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py\""
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-init.sh\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Verify all tasks are complete before stopping.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Hook Execution Details

| Aspect | Behavior |
|--------|----------|
| **Timeout** | 60 seconds default, configurable per command |
| **Parallelization** | All matching hooks run in parallel |
| **Deduplication** | Identical hook commands deduplicated |
| **Environment** | Runs in current directory with Claude Code's environment |

## Troubleshooting

### Hook Not Executing
- Verify JSON configuration syntax is correct
- Check matcher pattern matches the tool name
- Ensure script exists and is executable: `chmod +x script.sh`
- Run `claude --debug` to see hook execution logs
- Verify hook reads JSON from stdin (not command args)

### Hook Blocks Unexpectedly
- Test hook with sample JSON: `echo '{"tool_name": "Write", ...}' | ./hook.py`
- Check exit code: should be 0 for allow, 2 for block
- Check stderr output (shown on exit code 2)

### JSON Parsing Errors
- Always read from stdin, not command arguments
- Use proper JSON parsing (not string manipulation)
- Handle missing fields gracefully

## Installation

### Step 1: Create Hooks Directory
```bash
mkdir -p ~/.claude/hooks
```

### Step 2: Copy Example Hooks
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### Step 3: Configure in Settings
Edit `~/.claude/settings.json` or `.claude/settings.json` with the hook configuration shown above.

## Related Concepts

- **[Checkpoints and Rewind](../08-checkpoints/)** - Save and restore conversation state
- **[Slash Commands](../01-slash-commands/)** - Create custom slash commands
- **[Plugins](../07-plugins/)** - Bundled extension packages
- **[Advanced Features](../09-advanced-features/)** - Explore advanced Claude Code capabilities

## Resources

- **Official Documentation**: [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks)
