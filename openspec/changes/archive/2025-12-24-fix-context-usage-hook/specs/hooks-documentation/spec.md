# hooks-documentation Specification Delta

## MODIFIED Requirements

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
