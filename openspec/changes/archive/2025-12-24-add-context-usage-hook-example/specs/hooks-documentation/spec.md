# Hooks Documentation Specification

## ADDED Requirements

### Requirement: Context Usage Reporting Hook Example
The hooks lesson SHALL include a detailed example showing how to create a hook that reports context/token usage after each user request.

#### Scenario: User learns to create context monitoring hook
- **WHEN** a user reads the context usage reporter example
- **THEN** they find a complete Python script that reads the transcript file
- **AND** they understand how to estimate token usage from conversation history
- **AND** they see the configuration for UserPromptSubmit or Stop hooks
- **AND** they understand the limitations of token estimation

#### Scenario: Hook output format is documented
- **WHEN** a user implements the context usage hook
- **THEN** they can generate a one-line report showing used tokens and remaining capacity
- **AND** they understand the report is an estimate based on transcript analysis
