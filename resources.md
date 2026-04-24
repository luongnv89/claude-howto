<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# List of good resources

## Official Documentation

| Resource | Description | Link |
|----------|-------------|------|
| Claude Code Docs | Official Claude Code documentation | [code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview) |
| Anthropic Docs | Full Anthropic documentation | [docs.anthropic.com](https://docs.anthropic.com) |
| MCP Protocol | Model Context Protocol specification | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| MCP Servers | Official MCP server implementations | [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| Anthropic Cookbook | Code examples and tutorials | [github.com/anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) |
| Claude Code Skills | Community skills repository | [github.com/anthropics/skills](https://github.com/anthropics/skills) |
| Agent Teams | Multi-agent coordination and collaboration | [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) |
| Scheduled Tasks | Recurring tasks with /loop and cron | [code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks) |
| Chrome Integration | Browser automation | [code.claude.com/docs/en/chrome](https://code.claude.com/docs/en/chrome) |
| Keybindings | Keyboard shortcut customization | [code.claude.com/docs/en/keybindings](https://code.claude.com/docs/en/keybindings) |
| Desktop App | Native desktop application | [code.claude.com/docs/en/desktop](https://code.claude.com/docs/en/desktop) |
| Remote Control | Remote session control | [code.claude.com/docs/en/remote-control](https://code.claude.com/docs/en/remote-control) |
| Auto Mode | Automatic permission management | [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) |
| Channels | Multi-channel communication | [code.claude.com/docs/en/channels](https://code.claude.com/docs/en/channels) |
| Voice Dictation | Voice input for Claude Code | [code.claude.com/docs/en/voice-dictation](https://code.claude.com/docs/en/voice-dictation) |

## Anthropic Engineering Blog

| Article | Description | Link |
|---------|-------------|------|
| Code Execution with MCP | How to solve MCP context bloat using code execution — 98.7% token reduction | [anthropic.com/engineering/code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp) |

---

## Mastering Claude Code in 30 Minutes

_Video_: https://www.youtube.com/watch?v=6eBSHbLKuN0

_**All Tips**_
- **Explore Advanced Features and Shortcuts**
  - Regularly check Claude's new code editing and context features in their release notes.
  - Learn keyboard shortcuts to switch between chat, file, and editor views quickly.

- **Efficient Setup**
  - Create project-specific sessions with clear names/descriptions for easy retrieval.
  - Pin most-used files or folders so Claude can access them at any time.
  - Set up Claude's integrations (e.g., GitHub, popular IDEs) to streamline your coding process.

- **Effective Codebase Q&A**
  - Ask Claude detailed questions about architecture, design patterns, and specific modules.
  - Use file and line references in your questions (e.g., "What does the logic in `app/models/user.py` accomplish?").
  - For large codebases, provide a summary or manifest to help Claude focus.
  - **Example prompt**: _"Can you explain the authentication flow implemented in src/auth/AuthService.ts:45-120? How does it integrate with the middleware in src/middleware/auth.ts?"_

- **Code Editing & Refactoring**
  - Use inline comments or requests in code blocks to get focused edits ("Refactor this function for clarity").
  - Ask for side-by-side before/after comparisons.
  - Let Claude generate tests or documentation after major edits for quality assurance.
  - **Example prompt**: _"Refactor the getUserData function in api/users.js to use async/await instead of promises. Show me a before/after comparison and generate unit tests for the refactored version."_

- **Context Management**
  - Limit your pasted code/context to only what's relevant for the current task.
  - Use structured prompts ("Here's file A, here's function B, my question is X") for best performance.
  - Remove or collapse large files in the prompt window to avoid exceeding context limits.
  - **Example prompt**: _"Here's the User model from models/User.js and the validateUser function from utils/validation.js. My question is: how can I add email validation while maintaining backward compatibility?"_

- **Integrate Team Tools**
  - Connect Claude sessions to your team's repositories and documentation.
  - Use built-in templates or create custom ones for recurring engineering tasks.
  - Collaborate by sharing session transcripts and prompts with teammates.

- **Boosting Performance**
  - Give Claude clear, goal-oriented instructions (e.g., "Summarize this class in five bullet points").
  - Trim unnecessary comments and boilerplate from context windows.
  - If Claude's output is off track, reset context or rephrase questions for better alignment.
  - **Example prompt**: _"Summarize the DatabaseManager class in src/db/Manager.ts in five bullet points, focusing on its main responsibilities and key methods."_

- **Practical Use Examples**
  - Debugging: Paste errors and stack traces, then ask for possible causes and fixes.
  - Test Generation: Request property-based, unit, or integration tests for complex logic.
  - Code Reviews: Ask Claude to identify risky changes, edge cases, or code smells.
  - **Example prompts**:
    - _"I'm getting this error: 'TypeError: Cannot read property 'map' of undefined at line 42 in components/UserList.jsx'. Here's the stack trace and the relevant code. What's causing this and how can I fix it?"_
    - _"Generate comprehensive unit tests for the PaymentProcessor class, including edge cases for failed transactions, timeouts, and invalid inputs."_
    - _"Review this pull request diff and identify potential security issues, performance bottlenecks, and code smells."_

- **Workflow Automation**
  - Script repetitive tasks (like formatting, clean-ups, and repetitive renaming) using Claude prompts.
  - Use Claude to draft PR descriptions, release notes, or documentation based on code diffs.
  - **Example prompt**: _"Based on the git diff, create a detailed PR description with a summary of changes, list of modified files, testing steps, and potential impacts. Also generate release notes for version 2.3.0."_

**Tip**: For best results, combine several of these practices—start by pinning critical files and summarizing your goals, then use focused prompts and Claude’s refactoring tools to incrementally improve your codebase and automation.


**Recommended workflow with Claude Code**

### Recommended Workflow with Claude Code

#### For a New Repository

1. **Initialize the Repo & Claude Integration**
   - Set up your new repository with essential structure: README, LICENSE, .gitignore, root configs.
   - Create a `CLAUDE.md` file describing the architecture, high-level goals, and coding guidelines.
   - Install Claude Code and link it to your repository for code suggestions, test scaffolding, and workflow automation.

2. **Use Plan Mode and Specs**
   - Use plan mode (`shift-tab` or `/plan`) to draft a detailed specification before implementing features.
   - Ask Claude for architecture suggestions and initial project layout.
   - Keep a clear, goal-oriented prompt sequence—ask for component outlines, major modules, and responsibilities.

3. **Iterative Develop & Review**
   - Implement core features in small chunks, prompting Claude for code generation, refactoring, and documentation.
   - Request unit tests and examples after each increment.
   - Maintain a running task list in CLAUDE.md.

4. **Automate CI/CD and Deployment**
   - Use Claude to scaffold GitHub Actions, npm/yarn scripts, or deployment workflows.
   - Adapt pipelines easily by updating your CLAUDE.md and requesting corresponding commands/scripts.

```mermaid
graph TD
    A[Start New Repository] --> B[Initialize Repository Structure]
    B --> C[Create README, LICENSE, .gitignore]
    C --> D[Create CLAUDE.md]
    D --> E[Document Architecture & Guidelines]
    E --> F[Install & Link Claude Code]

    F --> G[Enter Plan Mode]
    G --> H[Draft Feature Specification]
    H --> I[Get Architecture Suggestions]
    I --> J[Define Components & Modules]

    J --> K[Implement Feature Chunk]
    K --> L[Generate Code with Claude]
    L --> M[Request Unit Tests]
    M --> N[Review & Refactor]
    N --> O{More Features?}
    O -->|Yes| K
    O -->|No| P[Update Task List in CLAUDE.md]

    P --> Q[Setup CI/CD Pipeline]
    Q --> R[Scaffold GitHub Actions]
    R --> S[Create Deployment Scripts]
    S --> T[Test Automation]
    T --> U[Repository Ready]

    style A fill:#e1f5ff
    style G fill:#fff4e1
    style K fill:#f0ffe1
    style Q fill:#ffe1f5
    style U fill:#90EE90
```

#### For an Existing Repository

1. **Repository & Context Setup**
   - Add or update `CLAUDE.md` to document repo structure, coding patterns, and key files. For legacy repos, use `CLAUDE_LEGACY.md` covering frameworks, version maps, instructions, bugs, and upgrade notes.
   - Pin or highlight main files Claude should use for context.

2. **Contextual Code Q&A**
   - Ask Claude for code reviews, bug explanations, refactors, or migration plans referencing specific files/functions.
   - Give Claude explicit boundaries (e.g., "modify only these files" or "no new dependencies").

3. **Branch, Worktree, and Multi-Session Management**
   - Use multiple git worktrees for isolated features or bug fixes and launch separate Claude sessions per worktree.
   - Keep terminal tabs/windows organized by branch or feature for parallel workflows.

4. **Team Tools and Automation**
   - Synchronize custom commands via `.claude/commands/` for cross-team consistency.
   - Automate repetitive tasks, PR creation, and code formatting via Claude's slash commands or hooks.
   - Share sessions and context with team members for collaborative troubleshooting and review.

```mermaid
graph TD
    A[Start with Existing Repository] --> B{Legacy Codebase?}
    B -->|Yes| C[Create CLAUDE_LEGACY.md]
    B -->|No| D[Create/Update CLAUDE.md]
    C --> E[Document Frameworks & Version Maps]
    D --> F[Document Structure & Patterns]
    E --> G[Pin Key Files for Context]
    F --> G

    G --> H[Identify Task Type]
    H --> I{Task Category}
    I -->|Bug Fix| J[Ask Claude for Bug Analysis]
    I -->|Code Review| K[Request Code Review]
    I -->|Refactor| L[Plan Refactoring Strategy]
    I -->|Migration| M[Create Migration Plan]

    J --> N[Set Explicit Boundaries]
    K --> N
    L --> N
    M --> N

    N --> O{Multiple Features?}
    O -->|Yes| P[Create Git Worktrees]
    O -->|No| Q[Work on Main Branch]
    P --> R[Launch Separate Claude Sessions]
    R --> S[Organize Terminal Tabs]
    Q --> S

    S --> T[Setup Team Automation]
    T --> U[Sync .claude/commands/]
    U --> V[Configure Slash Commands]
    V --> W[Setup Hooks for Automation]
    W --> X[Share Session Context with Team]

    X --> Y{More Tasks?}
    Y -->|Yes| H
    Y -->|No| Z[Workflow Complete]

    style A fill:#e1f5ff
    style C fill:#ffecec
    style D fill:#fff4e1
    style P fill:#f0ffe1
    style T fill:#ffe1f5
    style Z fill:#90EE90
```

**Tips**:
- Start each new feature or fix with a spec and plan mode prompt.
- For legacy and complex repos, store detailed guidance in CLAUDE.md/CLAUDE_LEGACY.md.
- Give clear, focused instructions and break down complex work into multi-phase plans.
- Regularly clean up sessions, prune context, and remove completed worktrees to avoid clutter.

These steps capture the core recommendations for smooth workflows with Claude Code in both new and existing codebases.

---

## New Features & Capabilities (March 2026)

### Key Feature Resources

| Feature | Description | Learn More |
|---------|-------------|------------|
| **Auto Memory** | Claude automatically learns and remembers your preferences across sessions | [Memory Guide](02-memory/) |
| **Remote Control** | Programmatically control Claude Code sessions from external tools and scripts | [Advanced Features](09-advanced-features/) |
| **Web Sessions** | Access Claude Code through browser-based interfaces for remote development | [CLI Reference](10-cli/) |
| **Desktop App** | Native desktop application for Claude Code with enhanced UI | [Claude Code Docs](https://code.claude.com/docs/en/desktop) |
| **Extended Thinking** | Deep reasoning toggle via `Alt+T`/`Option+T` or `MAX_THINKING_TOKENS` env var | [Advanced Features](09-advanced-features/) |
| **Permission Modes** | Fine-grained control: default, acceptEdits, plan, auto, dontAsk, bypassPermissions | [Advanced Features](09-advanced-features/) |
| **7-Tier Memory** | Managed Policy, Project, Project Rules, User, User Rules, Local, Auto Memory | [Memory Guide](02-memory/) |
| **Hook Events** | 28 events: PreToolUse, PostToolUse, PostToolUseFailure, Stop, StopFailure, SubagentStart, SubagentStop, Notification, Elicitation, and more | [Hooks Guide](06-hooks/) |
| **Agent Teams** | Coordinate multiple agents working together on complex tasks | [Subagents Guide](04-subagents/) |
| **Scheduled Tasks** | Set up recurring tasks with `/loop` and cron tools | [Advanced Features](09-advanced-features/) |
| **Chrome Integration** | Browser automation with headless Chromium | [Advanced Features](09-advanced-features/) |
| **Keyboard Customization** | Customize keybindings including chord sequences | [Advanced Features](09-advanced-features/) |
| **Monitor Tool** | Watch a background command's stdout stream and react to events instead of polling (v2.1.98+) | [Advanced Features](09-advanced-features/) |

---
**Last Updated**: April 24, 2026
**Claude Code Version**: 2.1.119
**Sources**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
