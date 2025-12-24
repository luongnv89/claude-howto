## ADDED Requirements

### Requirement: CLI Reference Lesson

The repository SHALL provide a comprehensive CLI reference lesson at `10-cli/` that documents all command-line interface options, flags, and usage patterns for Claude Code.

#### Scenario: User learns CLI basics
- **WHEN** a user navigates to `10-cli/README.md`
- **THEN** they find an overview of CLI capabilities with architecture diagram
- **AND** a quick reference table of all CLI commands
- **AND** examples demonstrating common usage patterns

#### Scenario: User looks up specific CLI flag
- **WHEN** a user needs to understand a specific CLI flag (e.g., `--output-format`)
- **THEN** they find the flag documented with description, options, and example usage
- **AND** related flags are cross-referenced

#### Scenario: User integrates Claude Code in CI/CD
- **WHEN** a user wants to use Claude Code in automation
- **THEN** they find practical examples for CI/CD integration
- **AND** examples show headless mode, JSON output, and error handling

### Requirement: CLI Commands Documentation

The CLI lesson SHALL document all primary CLI commands with their syntax and use cases.

#### Scenario: Interactive mode commands documented
- **WHEN** a user reads the CLI commands section
- **THEN** they find `claude` for starting interactive REPL
- **AND** `claude "query"` for starting with initial prompt
- **AND** `claude -c` for continuing recent conversation
- **AND** `claude -r` for resuming specific session

#### Scenario: Print mode commands documented
- **WHEN** a user reads the print mode section
- **THEN** they find `claude -p "query"` for non-interactive queries
- **AND** pipe input examples like `cat file | claude -p "query"`
- **AND** output format options (text, json, stream-json)

### Requirement: CLI Flags Documentation

The CLI lesson SHALL document all CLI flags organized by category with examples.

#### Scenario: Core flags documented
- **WHEN** a user reads the core flags section
- **THEN** they find `-p/--print`, `-c/--continue`, `-r/--resume`, `-v/--version`
- **AND** each flag has description and example usage

#### Scenario: Model configuration flags documented
- **WHEN** a user reads the model configuration section
- **THEN** they find `--model`, `--fallback-model`, `--agent`, `--agents`
- **AND** examples show model selection and custom agent definitions

#### Scenario: Permission flags documented
- **WHEN** a user reads the permission section
- **THEN** they find `--tools`, `--allowedTools`, `--disallowedTools`
- **AND** `--dangerously-skip-permissions`, `--permission-mode`
- **AND** examples demonstrate security-conscious configurations

### Requirement: High-Value Use Cases

The CLI lesson SHALL include practical use case examples that demonstrate real-world CLI value.

#### Scenario: CI/CD integration example provided
- **WHEN** a user reads the CI/CD use case
- **THEN** they find a complete GitHub Actions or Jenkins example
- **AND** the example demonstrates headless mode with JSON output
- **AND** error handling and exit codes are explained

#### Scenario: Script piping example provided
- **WHEN** a user reads the script piping use case
- **THEN** they find examples of piping file contents to Claude
- **AND** examples show log analysis, code review via pipe
- **AND** output processing patterns are demonstrated

#### Scenario: Multi-session workflow example provided
- **WHEN** a user reads the session management use case
- **THEN** they find examples of resuming and forking sessions
- **AND** session naming and organization patterns are shown

### Requirement: Navigation Integration

The root documentation SHALL be updated to include the CLI lesson in all navigation elements.

#### Scenario: CLI appears in Quick Navigation
- **WHEN** a user views the README Quick Navigation table
- **THEN** they see CLI Reference listed with link to `10-cli/`

#### Scenario: CLI appears in Learning Path
- **WHEN** a user views the Learning Path table
- **THEN** they see CLI Reference at position 10 with appropriate difficulty and timing

#### Scenario: CLI appears in Feature Comparison
- **WHEN** a user views the Feature Comparison table
- **THEN** CLI Reference is included with invocation, persistence, and use case columns

#### Scenario: CLI appears in Directory Structure
- **WHEN** a user views the Directory Structure tree
- **THEN** `10-cli/` directory is shown with `README.md`
