# Change: Add CLI Reference Lesson

## Why

The Claude How To repository covers nine major Claude Code features (01-09), but lacks a dedicated lesson for the CLI reference - the command-line interface that users interact with directly. Understanding CLI commands, flags, and options is fundamental to using Claude Code effectively. Users need a comprehensive reference to leverage features like model selection, output formats, permission management, and session handling via CLI.

## What Changes

- **NEW** `10-cli/` directory with comprehensive CLI reference lesson
- **NEW** `10-cli/README.md` - Main lesson content following established structure
- **UPDATE** Root `README.md` - Add CLI lesson to navigation and learning path
- **UPDATE** Root `README.md` - Add CLI to feature comparison and use case matrix
- **UPDATE** `LEARNING-ROADMAP.md` - Include CLI lesson in learning progression

## Key Content Areas

1. **CLI Commands** - Start interactive REPL, query mode, continue/resume sessions, updates
2. **Core Flags** - Print mode, continue, resume, version
3. **Model Configuration** - Model selection, fallback models, agent configuration
4. **System Prompt Customization** - Replace, append, file-based prompts
5. **Tool & Permission Management** - Allowed/disallowed tools, permission modes
6. **Output & Format** - JSON, stream-JSON, text formats
7. **MCP Configuration** - Server loading, strict mode
8. **Session Management** - Session IDs, forking, resumption
9. **Advanced Features** - Chrome integration, IDE connection, debug mode

## High-Value Use Cases

1. **CI/CD Integration** - Headless mode with JSON output for automation pipelines
2. **Script Piping** - Process files, logs, and data through Claude
3. **Multi-Session Workflows** - Resume and fork sessions for complex projects
4. **Custom Agent Configurations** - Define specialized subagents via CLI
5. **Batch Processing** - Process multiple queries with consistent settings
6. **Security-Conscious Development** - Permission modes and tool restrictions
7. **API Integration** - Structured JSON output for programmatic consumption

## Impact

- Affected specs: None (new capability)
- Affected code: Root README.md, LEARNING-ROADMAP.md
- New files: `10-cli/README.md`
