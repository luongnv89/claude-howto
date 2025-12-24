# Spec: Subagents Lesson Content

## MODIFIED Requirements

### Requirement: Configuration Format

The subagent configuration MUST use YAML frontmatter with all supported fields.

#### Scenario: Complete configuration example
- **Given**: A user wants to create a subagent
- **When**: They view the configuration documentation
- **Then**: The example shows all fields: name, description, tools (optional), model (optional), permissionMode (optional), skills (optional)

#### Scenario: Tools field omission
- **Given**: A subagent configuration omits the tools field
- **When**: The documentation explains this
- **Then**: It states the subagent inherits all tools from the main agent

### Requirement: Built-in Subagents Documentation

The lesson MUST document the three built-in subagents.

#### Scenario: General-Purpose subagent
- **Given**: A user reads about built-in subagents
- **When**: They view the General-Purpose section
- **Then**: They learn it uses Sonnet model, has all tools, and handles complex multi-step tasks

#### Scenario: Plan subagent
- **Given**: A user reads about built-in subagents
- **When**: They view the Plan section
- **Then**: They learn it uses Sonnet model, has Read/Glob/Grep/Bash tools, and is used in plan mode

#### Scenario: Explore subagent
- **Given**: A user reads about built-in subagents
- **When**: They view the Explore section
- **Then**: They learn it uses Haiku model, is read-only, fast, and supports thoroughness levels (quick, medium, very thorough)

### Requirement: /agents Command

The lesson MUST document the interactive /agents command.

#### Scenario: User discovers management interface
- **Given**: A user wants to manage subagents interactively
- **When**: They read the documentation
- **Then**: They learn about `/agents` command to create, edit, delete, and view subagents

### Requirement: Resumable Agents

The lesson MUST document agent continuation with agentId.

#### Scenario: User learns about resuming agents
- **Given**: A user wants to continue a previous agent conversation
- **When**: They read the resumable agents section
- **Then**: They learn agents return an agentId and can be resumed with full context

### Requirement: CLI Configuration

The lesson MUST document session-specific agent configuration via CLI.

#### Scenario: User defines agents via command line
- **Given**: A user wants to define agents for a single session
- **When**: They read the CLI configuration section
- **Then**: They learn to use `--agents` flag with JSON configuration

## ADDED Requirements

### Requirement: Example Subagent - Debugger

The lesson MUST include a debugger subagent example.

#### Scenario: User needs debugging specialist
- **Given**: A user wants a debugging-focused subagent
- **When**: They view the examples
- **Then**: They find a complete debugger.md example with root cause analysis approach

### Requirement: Example Subagent - Data Scientist

The lesson MUST include a data scientist subagent example.

#### Scenario: User needs data analysis specialist
- **Given**: A user wants a data analysis subagent
- **When**: They view the examples
- **Then**: They find a complete data-scientist.md example with SQL/BigQuery focus

### Requirement: File Location Documentation

The lesson MUST document where subagent files can be stored.

#### Scenario: User learns storage locations
- **Given**: A user wants to know where to put subagent files
- **When**: They read the file locations section
- **Then**: They learn about project (.claude/agents/), user (~/.claude/agents/), plugin, and CLI locations with priority order

### Requirement: Proactive Invocation Guidance

The lesson MUST explain how to encourage automatic subagent use.

#### Scenario: User wants subagent used automatically
- **Given**: A user wants Claude to proactively use their subagent
- **When**: They read the usage section
- **Then**: They learn to include "use PROACTIVELY" or "MUST BE USED" in the description field
