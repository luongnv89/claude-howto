# Change: Add Context Usage Reporting Hook Example

## Why

Users want to monitor their context window usage during Claude Code sessions. The hooks documentation currently lacks a practical example showing how to create a hook that reports context/token usage after each user request. This is valuable for understanding when context is getting full and when auto-compaction might occur.

## What Changes

- Add a detailed example hook that reports context usage after each user prompt
- The hook will read the transcript file and estimate token usage
- Include step-by-step explanation of how the hook works
- Document the limitations (estimation vs exact token counts)

## Impact

- **Affected specs**: hooks-documentation (add new example)
- **Affected code**: `06-hooks/README.md` (add new example section)
- **User impact**: Users gain a practical example for monitoring context usage
