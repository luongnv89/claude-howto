# hooks-documentation Specification

## Purpose
TBD - created by archiving change update-hooks-lesson. Update Purpose after archive.
## Requirements
### Requirement: Hook Event Types Documentation
The hooks lesson SHALL document all 9 official hook events with their correct names, matchers, and behavior.

#### Scenario: Complete hook event coverage
- **WHEN** a user reads the hooks lesson
- **THEN** they find documentation for PreToolUse, PermissionRequest, PostToolUse, Notification, UserPromptSubmit, Stop, SubagentStop, PreCompact, SessionStart, and SessionEnd events

#### Scenario: No deprecated hook events
- **WHEN** a user searches for PreCommit, PostCommit, or PrePush hooks
- **THEN** they do not find these as they are not valid Claude Code hook events

### Requirement: Hook Configuration Format
The hooks lesson SHALL document the correct array-based configuration format with matchers and hooks arrays.

#### Scenario: Configuration structure
- **WHEN** a user views hook configuration examples
- **THEN** they see the structure: `{ "hooks": { "EventName": [{ "matcher": "Pattern", "hooks": [{ "type": "command", "command": "..." }] }] } }`

#### Scenario: Matcher patterns
- **WHEN** a user needs to match specific tools
- **THEN** they find documentation for exact string matching, regex patterns, and wildcards

### Requirement: Hook Input Documentation
The hooks lesson SHALL document the JSON stdin input that hooks receive.

#### Scenario: JSON input structure
- **WHEN** a user writes a hook script
- **THEN** they understand the input includes session_id, transcript_path, cwd, permission_mode, hook_event_name, tool_name, tool_input, and tool_use_id

#### Scenario: Event-specific input fields
- **WHEN** a user writes a hook for a specific event
- **THEN** they find documentation for event-specific input fields (e.g., stop_hook_active for Stop event)

### Requirement: Hook Output Documentation
The hooks lesson SHALL document hook output semantics including exit codes and JSON stdout structure.

#### Scenario: Exit code semantics
- **WHEN** a user implements a hook
- **THEN** they understand exit code 0 means success, exit code 2 means blocking error (stderr used as error message), and other codes mean non-blocking error

#### Scenario: JSON output format
- **WHEN** a hook needs to control behavior
- **THEN** the user can output JSON with continue, stopReason, suppressOutput, systemMessage, and hookSpecificOutput fields

#### Scenario: Event-specific output
- **WHEN** a user writes a PreToolUse hook
- **THEN** they can output permissionDecision (allow/deny/ask), permissionDecisionReason, and updatedInput

### Requirement: Prompt-Based Hooks Documentation
The hooks lesson SHALL document type="prompt" hooks for LLM-based evaluation on Stop and SubagentStop events.

#### Scenario: Prompt hook configuration
- **WHEN** a user wants intelligent stop evaluation
- **THEN** they find documentation for configuring type="prompt" hooks with prompt text and timeout

#### Scenario: LLM response schema
- **WHEN** using prompt-based hooks
- **THEN** the user understands the expected response schema with decision (approve/block), reason, continue, stopReason, and systemMessage

### Requirement: Environment Variables Documentation
The hooks lesson SHALL document all environment variables available to hooks.

#### Scenario: Standard environment variables
- **WHEN** a user writes a hook script
- **THEN** they can use CLAUDE_PROJECT_DIR for the absolute project path

#### Scenario: SessionStart environment persistence
- **WHEN** using SessionStart hooks
- **THEN** the user can persist environment variables via CLAUDE_ENV_FILE

#### Scenario: Remote environment detection
- **WHEN** running in web environment
- **THEN** hooks can check CLAUDE_CODE_REMOTE to detect this

### Requirement: Security Documentation
The hooks lesson SHALL include security considerations and best practices from the official documentation.

#### Scenario: Security disclaimer
- **WHEN** a user reads about hooks
- **THEN** they see a clear disclaimer that hooks execute arbitrary shell commands at their own risk

#### Scenario: Security best practices
- **WHEN** a user implements hooks
- **THEN** they find guidance on input validation, shell variable quoting, path traversal prevention, and sensitive file handling

### Requirement: MCP Tool Hook Patterns
The hooks lesson SHALL document how to create hooks for MCP tools.

#### Scenario: MCP tool matching
- **WHEN** a user wants to hook into MCP tool calls
- **THEN** they find documentation for the pattern `mcp__<server>__<tool>` and regex matching

### Requirement: Plugin Hooks Documentation
The hooks lesson SHALL document how plugins can provide hooks.

#### Scenario: Plugin hook configuration
- **WHEN** a plugin needs to provide hooks
- **THEN** documentation covers hooks/hooks.json structure and ${CLAUDE_PLUGIN_ROOT} variable

### Requirement: Debugging Documentation
The hooks lesson SHALL document how to debug hook execution.

#### Scenario: Debug mode
- **WHEN** hooks are not working as expected
- **THEN** users can enable `claude --debug` for detailed hook execution logs

#### Scenario: Verbose mode
- **WHEN** using Claude Code interactively
- **THEN** users can enable verbose mode (ctrl+o) to see hook execution progress

### Requirement: Working Example Scripts
The hooks lesson SHALL provide working example scripts that use JSON stdin input.

#### Scenario: Bash command validator
- **WHEN** a user wants to validate bash commands
- **THEN** they find a working Python script that reads JSON stdin and validates commands

#### Scenario: Intelligent stop hook
- **WHEN** a user wants automatic task completion verification
- **THEN** they find a working prompt-based stop hook example

### Requirement: Context Usage Reporting Hook Example
The hooks lesson SHALL include a correct, working example showing how to create a hook that reports context/token usage after each Claude response.

#### Scenario: Token calculation is correct
- **WHEN** a user copies the context-usage.py example
- **AND** runs it as a Stop hook
- **THEN** the hook correctly calculates estimated tokens from total character count
- **AND** displays a non-zero token count proportional to conversation length

#### Scenario: User learns to create context monitoring hook
- **WHEN** a user reads the context usage reporter example
- **THEN** they find a complete Python script that reads the transcript file
- **AND** they understand how to estimate token usage from conversation history
- **AND** they see the configuration for Stop hooks
- **AND** they understand the limitations of token estimation

#### Scenario: Hook output format is documented
- **WHEN** a user implements the context usage hook
- **THEN** they can generate a one-line report showing used tokens and remaining capacity
- **AND** the output shows realistic token counts based on conversation size
