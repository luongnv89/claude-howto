<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Memory Guide

Memory enables Claude to retain context across sessions and conversations. It exists in two forms: automatic synthesis in claude.ai, and filesystem-based CLAUDE.md in Claude Code.

## Overview

Memory in Claude Code provides persistent context that carries across multiple sessions and conversations. Unlike temporary context windows, memory files allow you to:

- Share project standards across your team
- Store personal development preferences
- Maintain directory-specific rules and configurations
- Import external documentation
- Version control memory as part of your project

The memory system operates at multiple levels, from global personal preferences down to specific subdirectories, allowing for fine-grained control over what Claude remembers and how it applies that knowledge.

## Memory Commands Quick Reference

| Command | Purpose | Usage | When to Use |
|---------|---------|-------|-------------|
| `/init` | Initialize project memory | `/init` | Starting new project, first-time CLAUDE.md setup |
| `/memory` | Edit memory files in editor | `/memory` | Extensive updates, reorganization, reviewing content |
| `#` prefix | ~~Quick single-line memory add~~ **Discontinued** | — | Use `/memory` or ask conversationally instead |
| `@path/to/file` | Import external content | `@README.md` or `@docs/api.md` | Referencing existing documentation in CLAUDE.md |

## Quick Start: Initializing Memory

### The `/init` Command

The `/init` command is the fastest way to set up project memory in Claude Code. It initializes a CLAUDE.md file with foundational project documentation.

**Usage:**

```bash
/init
```

**What it does:**

- Creates a new CLAUDE.md file in your project (typically at `./CLAUDE.md` or `./.claude/CLAUDE.md`)
- Establishes project conventions and guidelines
- Sets up the foundation for context persistence across sessions
- Provides a template structure for documenting your project standards

**Enhanced interactive mode:** Set `CLAUDE_CODE_NEW_INIT=1` to enable a multi-phase interactive flow that walks you through project setup step by step:

```bash
CLAUDE_CODE_NEW_INIT=1 claude
/init
```

**When to use `/init`:**

- Starting a new project with Claude Code
- Establishing team coding standards and conventions
- Creating documentation about your codebase structure
- Setting up memory hierarchy for collaborative development

**Example workflow:**

```markdown
# In your project directory
/init

# Claude creates CLAUDE.md with structure like:
# Project Configuration
## Project Overview
- Name: Your Project
- Tech Stack: [Your technologies]
- Team Size: [Number of developers]

## Development Standards
- Code style preferences
- Testing requirements
- Git workflow conventions
```

### Quick Memory Updates

> **Note**: The `#` shortcut for inline memory was discontinued. Use `/memory` to edit memory files directly, or ask Claude conversationally to remember something (e.g., "remember that we always use TypeScript strict mode").

The recommended ways to add information to memory are:

**Option 1: Use `/memory` command**

```bash
/memory
```

Opens your memory files in your system editor for direct editing.

**Option 2: Ask conversationally**

```
Remember that we always use TypeScript strict mode in this project.
Please add to memory: prefer async/await over promise chains.
```

Claude will update the appropriate CLAUDE.md file based on your request.

**Historical reference** (no longer functional):

The `#` prefix shortcut previously allowed adding rules inline:

```markdown
# Always use TypeScript strict mode in this project  ← no longer works
```

If you relied on this pattern, switch to the `/memory` command or conversational requests.

### The `/memory` Command

The `/memory` command provides direct access to edit your CLAUDE.md memory files within Claude Code sessions. It opens your memory files in your system editor for comprehensive editing.

**Usage:**

```bash
/memory
```

**What it does:**

- Opens your memory files in your system's default editor
- Allows you to make extensive additions, modifications, and reorganizations
- Provides direct access to all memory files in the hierarchy
- Enables you to manage persistent context across sessions

**When to use `/memory`:**

- Reviewing existing memory content
- Making extensive updates to project standards
- Reorganizing memory structure
- Adding detailed documentation or guidelines
- Maintaining and updating memory as your project evolves

**Comparison: `/memory` vs `/init`**

| Aspect | `/memory` | `/init` |
|--------|-----------|---------|
| **Purpose** | Edit existing memory files | Initialize new CLAUDE.md |
| **When to use** | Update/modify project context | Begin new projects |
| **Action** | Opens editor for changes | Generates starter template |
| **Workflow** | Ongoing maintenance | One-time setup |

**Example workflow:**

```markdown
# Open memory for editing
/memory

# Claude presents options:
# 1. Managed Policy Memory
# 2. Project Memory (./CLAUDE.md)
# 3. User Memory (~/.claude/CLAUDE.md)
# 4. Local Project Memory

# Choose option 2 (Project Memory)
# Your default editor opens with ./CLAUDE.md content

# Make changes, save, and close editor
# Claude automatically reloads the updated memory
```

**Using Memory Imports:**

CLAUDE.md files support the `@path/to/file` syntax to include external content:

```markdown
# Project Documentation
See @README.md for project overview
See @package.json for available npm commands
See @docs/architecture.md for system design

# Import from home directory using absolute path
@~/.claude/my-project-instructions.md
```

**Import features:**

- Both relative and absolute paths are supported (e.g., `@docs/api.md` or `@~/.claude/my-project-instructions.md`)
- Recursive imports are supported with a maximum depth of 5
- First-time imports from external locations trigger an approval dialog for security
- Import directives are not evaluated inside markdown code spans or code blocks (so documenting them in examples is safe)
- Helps avoid duplication by referencing existing documentation
- Automatically includes referenced content in Claude's context

## Memory Architecture

Memory in Claude Code follows a hierarchical system where different scopes serve different purposes:

```mermaid
graph TB
    A["Claude Session"]
    B["User Input"]
    C["Memory System"]
    D["Memory Storage"]

    B -->|User provides info| C
    C -->|Synthesizes every 24h| D
    D -->|Loads automatically| A
    A -->|Uses context| C
```

## Memory Hierarchy in Claude Code

Claude Code uses a multi-tier hierarchical memory system. Memory files are automatically loaded when Claude Code launches, with higher-level files taking precedence.

**Complete Memory Hierarchy (in order of precedence):**

1. **Managed Policy** - Organization-wide instructions
   - macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`
   - Linux/WSL: `/etc/claude-code/CLAUDE.md`
   - Windows: `C:\Program Files\ClaudeCode\CLAUDE.md`

2. **Managed Drop-ins** - Alphabetically merged policy files (v2.1.83+)
   - `managed-settings.d/` directory alongside the managed policy CLAUDE.md
   - Files are merged in alphabetical order for modular policy management

3. **Project Memory** - Team-shared context (version controlled)
   - `./.claude/CLAUDE.md` or `./CLAUDE.md` (in repository root)

4. **Project Rules** - Modular, topic-specific project instructions
   - `./.claude/rules/*.md`

5. **User Memory** - Personal preferences (all projects)
   - `~/.claude/CLAUDE.md`

6. **User-Level Rules** - Personal rules (all projects)
   - `~/.claude/rules/*.md`

7. **Local Project Memory** - Personal project-specific preferences
   - `./CLAUDE.local.md`

> **Note**: `CLAUDE.local.md` is fully supported and documented in the [official documentation](https://code.claude.com/docs/en/memory). It provides personal project-specific preferences that are not committed to version control. Add `CLAUDE.local.md` to your `.gitignore`.

8. **Auto Memory** - Claude's automatic notes and learnings
   - `~/.claude/projects/<project>/memory/`

**Memory Discovery Behavior:**

Claude searches for memory files in this order, with earlier locations taking precedence:

```mermaid
graph TD
    A["Managed Policy<br/>/Library/.../ClaudeCode/CLAUDE.md"] -->|highest priority| A2["Managed Drop-ins<br/>managed-settings.d/"]
    A2 --> B["Project Memory<br/>./CLAUDE.md"]
    B --> C["Project Rules<br/>./.claude/rules/*.md"]
    C --> D["User Memory<br/>~/.claude/CLAUDE.md"]
    D --> E["User Rules<br/>~/.claude/rules/*.md"]
    E --> F["Local Project Memory<br/>./CLAUDE.local.md"]
    F --> G["Auto Memory<br/>~/.claude/projects/.../memory/"]

    B -->|imports| H["@docs/architecture.md"]
    H -->|imports| I["@docs/api-standards.md"]

    style A fill:#fce4ec,stroke:#333,color:#333
    style A2 fill:#fce4ec,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e1f5fe,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
    style G fill:#fff3e0,stroke:#333,color:#333
    style H fill:#e1f5fe,stroke:#333,color:#333
    style I fill:#e1f5fe,stroke:#333,color:#333
```

## Excluding CLAUDE.md Files with `claudeMdExcludes`

In large monorepos, some CLAUDE.md files may be irrelevant to your current work. The `claudeMdExcludes` setting lets you skip specific CLAUDE.md files so they are not loaded into context:

```jsonc
// In ~/.claude/settings.json or .claude/settings.json
{
  "claudeMdExcludes": [
    "packages/legacy-app/CLAUDE.md",
    "vendors/**/CLAUDE.md"
  ]
}
```

Patterns are matched against paths relative to the project root. This is particularly useful for:

- Monorepos with many sub-projects, where only some are relevant
- Repositories that contain vendored or third-party CLAUDE.md files
- Reducing noise in Claude's context window by excluding stale or unrelated instructions

## Settings File Hierarchy

Claude Code settings (including `autoMemoryDirectory`, `claudeMdExcludes`, and other configuration) are resolved from a five-level hierarchy, with higher levels taking precedence:

| Level | Location | Scope |
|-------|----------|-------|
| 1 (Highest) | Managed policy (system-level) | Organization-wide enforcement |
| 2 | `managed-settings.d/` (v2.1.83+) | Modular policy drop-ins, merged alphabetically |
| 3 | `~/.claude/settings.json` | User preferences |
| 4 | `.claude/settings.json` | Project-level (committed to git) |
| 5 (Lowest) | `.claude/settings.local.json` | Local overrides (git-ignored) |

**Platform-specific configuration (v2.1.51+):**

Settings can also be configured via:
- **macOS**: Property list (plist) files
- **Windows**: Windows Registry

These platform-native mechanisms are read alongside JSON settings files and follow the same precedence rules.

> **Note (v2.1.119)**: `/config` changes now persist to `~/.claude/settings.json`. Values written via `/config` participate in the normal project/local/policy precedence chain described above — they are no longer session-only. Use `/config` for interactive edits and edit `settings.json` files directly for scripted or managed configuration.

### Retention and Cleanup Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `cleanupPeriodDays` | integer (days) | 30 | Retention window for on-disk artifacts. **As of v2.1.117**, it applies to all four of: checkpoints (`~/.claude/checkpoints/`), tasks (`~/.claude/tasks/`), shell-snapshots (`~/.claude/shell-snapshots/`), and backups (`~/.claude/backups/`). Files older than the window are pruned at startup. |

```jsonc
// ~/.claude/settings.json
{
  "cleanupPeriodDays": 14
}
```

### Attribution, Voice, and PR URL Settings

| Setting | Type | Description |
|---------|------|-------------|
| `attribution.commit` | boolean | Adds the `Co-Authored-By: Claude` trailer to commits Claude creates. Replaces the deprecated `includeCoAuthoredBy` flag. |
| `attribution.pr` | boolean | Adds Claude attribution to pull request descriptions. Replaces the deprecated `includeCoAuthoredBy` flag for PRs. |
| `voice.enabled` | boolean | Enables push-to-talk voice dictation (`/voice`). Replaces the deprecated `voiceEnabled` flag. |
| `prUrlTemplate` | string | **New in v2.1.119.** Custom URL template for the footer PR badge; useful for GitLab, Bitbucket, or internal code-review platforms. Supports `{{owner}}`, `{{repo}}`, and `{{number}}` placeholders. |

```jsonc
// ~/.claude/settings.json
{
  "attribution": {
    "commit": false,
    "pr": true
  },
  "voice": {
    "enabled": true
  },
  "prUrlTemplate": "https://gitlab.internal/{{owner}}/{{repo}}/-/merge_requests/{{number}}"
}
```

#### Deprecated setting names

The following legacy setting keys still work but are deprecated. Prefer the replacements above.

| Deprecated key | Replacement | Notes |
|----------------|-------------|-------|
| `includeCoAuthoredBy` | `attribution.commit` / `attribution.pr` | The old single flag is split into separate commit and PR switches. Users on older installs can keep the legacy key; new projects should use the nested form. |
| `voiceEnabled` | `voice.enabled` | Grouped under the `voice` namespace alongside future voice-related options. |

## Modular Rules System

Create organized, path-specific rules using the `.claude/rules/` directory structure. Rules can be defined at both the project level and user level:

```
your-project/
├── .claude/
│   ├── CLAUDE.md
│   └── rules/
│       ├── code-style.md
│       ├── testing.md
│       ├── security.md
│       └── api/                  # Subdirectories supported
│           ├── conventions.md
│           └── validation.md

~/.claude/
├── CLAUDE.md
└── rules/                        # User-level rules (all projects)
    ├── personal-style.md
    └── preferred-patterns.md
```

Rules are discovered recursively within the `rules/` directory, including any subdirectories. User-level rules at `~/.claude/rules/` are loaded before project-level rules, allowing personal defaults that projects can override.

### Path-Specific Rules with YAML Frontmatter

Define rules that apply only to specific file paths:

```markdown
---
paths: src/api/**/*.ts
---

# API Development Rules

- All API endpoints must include input validation
- Use Zod for schema validation
- Document all parameters and response types
- Include error handling for all operations
```

**Glob Pattern Examples:**

- `**/*.ts` - All TypeScript files
- `src/**/*` - All files under src/
- `src/**/*.{ts,tsx}` - Multiple extensions
- `{src,lib}/**/*.ts, tests/**/*.test.ts` - Multiple patterns

### Subdirectories and Symlinks

Rules in `.claude/rules/` support two organizational features:

- **Subdirectories**: Rules are discovered recursively, so you can organize them into topic-based folders (e.g., `rules/api/`, `rules/testing/`, `rules/security/`)
- **Symlinks**: Symlinks are supported for sharing rules across multiple projects. For example, you can symlink a shared rule file from a central location into each project's `.claude/rules/` directory

## Memory Locations Table

| Location | Scope | Priority | Shared | Access | Best For |
|----------|-------|----------|--------|--------|----------|
| `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS) | Managed Policy | 1 (Highest) | Organization | System | Company-wide policies |
| `/etc/claude-code/CLAUDE.md` (Linux/WSL) | Managed Policy | 1 (Highest) | Organization | System | Organization standards |
| `C:\Program Files\ClaudeCode\CLAUDE.md` (Windows) | Managed Policy | 1 (Highest) | Organization | System | Corporate guidelines |
| `managed-settings.d/*.md` (alongside policy) | Managed Drop-ins | 1.5 | Organization | System | Modular policy files (v2.1.83+) |
| `./CLAUDE.md` or `./.claude/CLAUDE.md` | Project Memory | 2 | Team | Git | Team standards, shared architecture |
| `./.claude/rules/*.md` | Project Rules | 3 | Team | Git | Path-specific, modular rules |
| `~/.claude/CLAUDE.md` | User Memory | 4 | Individual | Filesystem | Personal preferences (all projects) |
| `~/.claude/rules/*.md` | User Rules | 5 | Individual | Filesystem | Personal rules (all projects) |
| `./CLAUDE.local.md` | Project Local | 6 | Individual | Git (ignored) | Personal project-specific preferences |
| `~/.claude/projects/<project>/memory/` | Auto Memory | 7 (Lowest) | Individual | Filesystem | Claude's automatic notes and learnings |

## Memory Update Lifecycle

Here's how memory updates flow through your Claude Code sessions:

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Editor as File System
    participant Memory as CLAUDE.md

    User->>Claude: "Remember: use async/await"
    Claude->>User: "Which memory file?"
    User->>Claude: "Project memory"
    Claude->>Editor: Open ~/.claude/settings.json
    Claude->>Memory: Write to ./CLAUDE.md
    Memory-->>Claude: File saved
    Claude->>Claude: Load updated memory
    Claude-->>User: "Memory saved!"
```

## Auto Memory

Auto memory is a persistent directory where Claude automatically records learnings, patterns, and insights as it works with your project. Unlike CLAUDE.md files which you write and maintain manually, auto memory is written by Claude itself during sessions.

### How Auto Memory Works

- **Location**: `~/.claude/projects/<project>/memory/`
- **Entrypoint**: `MEMORY.md` serves as the main file in the auto memory directory
- **Topic files**: Optional additional files for specific subjects (e.g., `debugging.md`, `api-conventions.md`)
- **Loading behavior**: The first 200 lines of `MEMORY.md` (or first 25KB, whichever comes first) are loaded into context at session start. Topic files are loaded on demand, not at startup.
- **Read/write**: Claude reads and writes memory files during sessions as it discovers patterns and project-specific knowledge

### Auto Memory Architecture

```mermaid
graph TD
    A["Claude Session Starts"] --> B["Load MEMORY.md<br/>(first 200 lines / 25KB)"]
    B --> C["Session Active"]
    C --> D["Claude discovers<br/>patterns & insights"]
    D --> E{"Write to<br/>auto memory"}
    E -->|General notes| F["MEMORY.md"]
    E -->|Topic-specific| G["debugging.md"]
    E -->|Topic-specific| H["api-conventions.md"]
    C --> I["On-demand load<br/>topic files"]
    I --> C

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#fff3e0,stroke:#333,color:#333
    style F fill:#fce4ec,stroke:#333,color:#333
    style G fill:#fce4ec,stroke:#333,color:#333
    style H fill:#fce4ec,stroke:#333,color:#333
    style I fill:#f3e5f5,stroke:#333,color:#333
```

### Auto Memory Directory Structure

```
~/.claude/projects/<project>/memory/
├── MEMORY.md              # Entrypoint (first 200 lines / 25KB loaded at startup)
├── debugging.md           # Topic file (loaded on demand)
├── api-conventions.md     # Topic file (loaded on demand)
└── testing-patterns.md    # Topic file (loaded on demand)
```

### Version Requirement

Auto memory requires **Claude Code v2.1.59 or later**. If you are on an older version, upgrade first:

```bash
npm install -g @anthropic-ai/claude-code@latest
```

### Custom Auto Memory Directory

By default, auto memory is stored in `~/.claude/projects/<project>/memory/`. You can change this location using the `autoMemoryDirectory` setting (available since **v2.1.74**):

```jsonc
// In ~/.claude/settings.json or .claude/settings.local.json (user/local settings only)
{
  "autoMemoryDirectory": "/path/to/custom/memory/directory"
}
```

> **Note**: `autoMemoryDirectory` can only be set in user-level (`~/.claude/settings.json`) or local settings (`.claude/settings.local.json`), not in project or managed policy settings.

This is useful when you want to:

- Store auto memory in a shared or synced location
- Separate auto memory from the default Claude configuration directory
- Use a project-specific path outside the default hierarchy

### Worktree and Repository Sharing

All worktrees and subdirectories within the same git repository share a single auto memory directory. This means switching between worktrees or working in different subdirectories of the same repo will read and write to the same memory files.

### Subagent Memory

Subagents (spawned via tools like Task or parallel execution) can have their own memory context. Use the `memory` frontmatter field in the subagent definition to specify which memory scopes to load:

```yaml
memory: user      # Load user-level memory only
memory: project   # Load project-level memory only
memory: local     # Load local memory only
```

This allows subagents to operate with focused context rather than inheriting the full memory hierarchy.

> **Note**: Subagents can also maintain their own auto memory. See the [official subagent memory documentation](https://code.claude.com/docs/en/sub-agents#enable-persistent-memory) for details.

### Controlling Auto Memory

Auto memory can be controlled via the `CLAUDE_CODE_DISABLE_AUTO_MEMORY` environment variable:

| Value | Behavior |
|-------|----------|
| `0` | Force auto memory **on** |
| `1` | Force auto memory **off** |
| *(unset)* | Default behavior (auto memory enabled) |

```bash
# Disable auto memory for a session
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 claude

# Force auto memory on explicitly
CLAUDE_CODE_DISABLE_AUTO_MEMORY=0 claude
```

## Additional Directories with `--add-dir`

The `--add-dir` flag allows Claude Code to load CLAUDE.md files from additional directories beyond the current working directory. This is useful for monorepos or multi-project setups where context from other directories is relevant.

To enable this feature, set the environment variable:

```bash
CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1
```

Then launch Claude Code with the flag:

```bash
claude --add-dir /path/to/other/project
```

Claude will load CLAUDE.md from the specified additional directory alongside the memory files from your current working directory.

## Practical Examples

### Example 1: Project Memory Structure

**File:** `./CLAUDE.md`

```markdown
# Project Configuration

## Project Overview
- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Development Standards

### Code Style
- Use Prettier for formatting
- Use ESLint with airbnb config
- Maximum line length: 100 characters
- Use 2-space indentation

### Naming Conventions
- **Files**: kebab-case (user-controller.js)
- **Classes**: PascalCase (UserService)
- **Functions/Variables**: camelCase (getUserById)
- **Constants**: UPPER_SNAKE_CASE (API_BASE_URL)
- **Database Tables**: snake_case (user_accounts)

### Git Workflow
- Branch names: `feature/description` or `fix/description`
- Commit messages: Follow conventional commits
- PR required before merge
- All CI/CD checks must pass
- Minimum 1 approval required

### Testing Requirements
- Minimum 80% code coverage
- All critical paths must have tests
- Use Jest for unit tests
- Use Cypress for E2E tests
- Test filenames: `*.test.ts` or `*.spec.ts`

### API Standards
- RESTful endpoints only
- JSON request/response
- Use HTTP status codes correctly
- Version API endpoints: `/api/v1/`
- Document all endpoints with examples

### Database
- Use migrations for schema changes
- Never hardcode credentials
- Use connection pooling
- Enable query logging in development
- Regular backups required

### Deployment
- Docker-based deployment
- Kubernetes orchestration
- Blue-green deployment strategy
- Automatic rollback on failure
- Database migrations run before deploy

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start development server |
| `npm test` | Run test suite |
| `npm run lint` | Check code style |
| `npm run build` | Build for production |
| `npm run migrate` | Run database migrations |

## Team Contacts
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Known Issues & Workarounds
- PostgreSQL connection pooling limited to 20 during peak hours
- Workaround: Implement query queuing
- Safari 14 compatibility issues with async generators
- Workaround: Use Babel transpiler

## Related Projects
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
```

### Example 2: Directory-Specific Memory

**File:** `./src/api/CLAUDE.md`

````markdown
# API Module Standards

This file overrides root CLAUDE.md for everything in /src/api/

## API-Specific Standards

### Request Validation
- Use Zod for schema validation
- Always validate input
- Return 400 with validation errors
- Include field-level error details

### Authentication
- All endpoints require JWT token
- Token in Authorization header
- Token expires after 24 hours
- Implement refresh token mechanism

### Response Format

All responses must follow this structure:

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

Error responses:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Pagination
- Use cursor-based pagination (not offset)
- Include `hasMore` boolean
- Limit max page size to 100
- Default page size: 20

### Rate Limiting
- 1000 requests per hour for authenticated users
- 100 requests per hour for public endpoints
- Return 429 when exceeded
- Include retry-after header

### Caching
- Use Redis for session caching
- Cache duration: 5 minutes default
- Invalidate on write operations
- Tag cache keys with resource type
````

### Example 3: Personal Memory

**File:** `~/.claude/CLAUDE.md`

```markdown
# My Development Preferences

## About Me
- **Experience Level**: 8 years full-stack development
- **Preferred Languages**: TypeScript, Python
- **Communication Style**: Direct, with examples
- **Learning Style**: Visual diagrams with code

## Code Preferences

### Error Handling
I prefer explicit error handling with try-catch blocks and meaningful error messages.
Avoid generic errors. Always log errors for debugging.

### Comments
Use comments for WHY, not WHAT. Code should be self-documenting.
Comments should explain business logic or non-obvious decisions.

### Testing
I prefer TDD (test-driven development).
Write tests first, then implementation.
Focus on behavior, not implementation details.

### Architecture
I prefer modular, loosely-coupled design.
Use dependency injection for testability.
Separate concerns (Controllers, Services, Repositories).

## Debugging Preferences
- Use console.log with prefix: `[DEBUG]`
- Include context: function name, relevant variables
- Use stack traces when available
- Always include timestamps in logs

## Communication
- Explain complex concepts with diagrams
- Show concrete examples before explaining theory
- Include before/after code snippets
- Summarize key points at the end

## Project Organization
I organize my projects as:

   project/
   ├── src/
   │   ├── api/
   │   ├── services/
   │   ├── models/
   │   └── utils/
   ├── tests/
   ├── docs/
   └── docker/

## Tooling
- **IDE**: VS Code with vim keybindings
- **Terminal**: Zsh with Oh-My-Zsh
- **Format**: Prettier (100 char line length)
- **Linter**: ESLint with airbnb config
- **Test Framework**: Jest with React Testing Library
```

_My Test_
Ask Claude to save a new rule

![Ask Claude to save a new rule](memory-ask-claude.png)
Claude has not save the rule because I did not have any `Claude.md` file anywhere. Then asked Claude to confirm the location.

![Ask Claude to save a new rule](memory-saved.png)

### Example 4: Memory Update During Session

You can add new rules to memory during an active Claude Code session. There are two ways to do this:

#### Method 1: Direct Request

```markdown
User: Remember that I prefer using React hooks instead of class components
     for all new components.

Claude: I'm adding that to your memory. Which memory file should this go in?
        1. Project memory (./CLAUDE.md)
        2. Personal memory (~/.claude/CLAUDE.md)

User: Project memory

Claude: ✅ Memory saved!

Added to ./CLAUDE.md:
---

### Component Development
- Use functional components with React Hooks
- Prefer hooks over class components
- Custom hooks for reusable logic
- Use useCallback for event handlers
- Use useMemo for expensive computations
```

#### Method 2: Using "# new rule into memory" Pattern

You can also use the explicit pattern "# new rule into memory" to trigger memory updates:

```markdown
User: # new rule into memory
      Always validate user input with Zod schemas before processing.

Claude: I'm saving this rule to memory. Which memory file should I use?
        1. Project memory (./CLAUDE.md)
        2. Personal memory (~/.claude/CLAUDE.md)

User: Project memory

Claude: ✅ Memory saved!

Added to ./CLAUDE.md:
---

### Input Validation
- Always validate user input with Zod schemas before processing
- Define schemas at the top of each API handler file
- Return 400 status with validation errors
```

#### Tips for Adding Memory

- Be specific and actionable in your rules
- Group related rules together under a section header
- Update existing sections instead of duplicating content
- Choose the appropriate memory scope (project vs. personal)

## Memory Features Comparison

| Feature | Claude Web/Desktop | Claude Code (CLAUDE.md) |
|---------|-------------------|------------------------|
| Auto-synthesis | ✅ Every 24h | ✅ Auto memory |
| Cross-project | ✅ Shared | ❌ Project-specific |
| Team access | ✅ Shared projects | ✅ Git-tracked |
| Searchable | ✅ Built-in | ✅ Through `/memory` |
| Editable | ✅ In-chat | ✅ Direct file edit |
| Import/Export | ✅ Yes | ✅ Copy/paste |
| Persistent | ✅ 24h+ | ✅ Indefinite |

### Memory in Claude Web/Desktop

#### Memory Synthesis Timeline

```mermaid
graph LR
    A["Day 1: User<br/>Conversations"] -->|24 hours| B["Day 2: Memory<br/>Synthesis"]
    B -->|Automatic| C["Memory Updated<br/>Summarized"]
    C -->|Loaded in| D["Day 2-N:<br/>New Conversations"]
    D -->|Add to| E["Memory"]
    E -->|24 hours later| F["Memory Refreshed"]
```

**Example Memory Summary:**

```markdown
## Claude's Memory of User

### Professional Background
- Senior full-stack developer with 8 years experience
- Focus on TypeScript/Node.js backends and React frontends
- Active open source contributor
- Interested in AI and machine learning

### Project Context
- Currently building e-commerce platform
- Tech stack: Node.js, PostgreSQL, React 18, Docker
- Working with team of 5 developers
- Using CI/CD and blue-green deployments

### Communication Preferences
- Prefers direct, concise explanations
- Likes visual diagrams and examples
- Appreciates code snippets
- Explains business logic in comments

### Current Goals
- Improve API performance
- Increase test coverage to 90%
- Implement caching strategy
- Document architecture
```

## Best Practices

### Do's - What To Include

- **Be specific and detailed**: Use clear, detailed instructions rather than vague guidance
  - ✅ Good: "Use 2-space indentation for all JavaScript files"
  - ❌ Avoid: "Follow best practices"

- **Keep organized**: Structure memory files with clear markdown sections and headings

- **Use appropriate hierarchy levels**:
  - **Managed policy**: Company-wide policies, security standards, compliance requirements
  - **Project memory**: Team standards, architecture, coding conventions (commit to git)
  - **User memory**: Personal preferences, communication style, tooling choices
  - **Directory memory**: Module-specific rules and overrides

- **Leverage imports**: Use `@path/to/file` syntax to reference existing documentation
  - Supports up to 5 levels of recursive nesting
  - Avoids duplication across memory files
  - Example: `See @README.md for project overview`

- **Document frequent commands**: Include commands you use repeatedly to save time

- **Version control project memory**: Commit project-level CLAUDE.md files to git for team benefit

- **Review periodically**: Update memory regularly as projects evolve and requirements change

- **Provide concrete examples**: Include code snippets and specific scenarios

### Don'ts - What To Avoid

- **Don't store secrets**: Never include API keys, passwords, tokens, or credentials

- **Don't include sensitive data**: No PII, private information, or proprietary secrets

- **Don't duplicate content**: Use imports (`@path`) to reference existing documentation instead

- **Don't be vague**: Avoid generic statements like "follow best practices" or "write good code"

- **Don't make it too long**: Keep individual memory files focused and under 500 lines

- **Don't over-organize**: Use hierarchy strategically; don't create excessive subdirectory overrides

- **Don't forget to update**: Stale memory can cause confusion and outdated practices

- **Don't exceed nesting limits**: Memory imports support up to 5 levels of nesting

### Memory Management Tips

**Choose the right memory level:**

| Use Case | Memory Level | Rationale |
|----------|-------------|-----------|
| Company security policy | Managed Policy | Applies to all projects organization-wide |
| Team code style guide | Project | Shared with team via git |
| Your preferred editor shortcuts | User | Personal preference, not shared |
| API module standards | Directory | Specific to that module only |

**Quick update workflow:**

1. For single rules: Use `#` prefix in conversation
2. For multiple changes: Use `/memory` to open editor
3. For initial setup: Use `/init` to create template

**Import best practices:**

```markdown
# Good: Reference existing docs
@README.md
@docs/architecture.md
@package.json

# Avoid: Copying content that exists elsewhere
# Instead of copying README content into CLAUDE.md, just import it
```

## Installation Instructions

### Setup Project Memory

#### Method 1: Using `/init` Command (Recommended)

The fastest way to set up project memory:

1. **Navigate to your project directory:**
   ```bash
   cd /path/to/your/project
   ```

2. **Run the init command in Claude Code:**
   ```bash
   /init
   ```

3. **Claude will create and populate CLAUDE.md** with a template structure

4. **Customize the generated file** to match your project needs

5. **Commit to git:**
   ```bash
   git add CLAUDE.md
   git commit -m "Initialize project memory with /init"
   ```

#### Method 2: Manual Creation

If you prefer manual setup:

1. **Create a CLAUDE.md in your project root:**
   ```bash
   cd /path/to/your/project
   touch CLAUDE.md
   ```

2. **Add project standards:**
   ```bash
   cat > CLAUDE.md << 'EOF'
   # Project Configuration

   ## Project Overview
   - **Name**: Your Project Name
   - **Tech Stack**: List your technologies
   - **Team Size**: Number of developers

   ## Development Standards
   - Your coding standards
   - Naming conventions
   - Testing requirements
   EOF
   ```

3. **Commit to git:**
   ```bash
   git add CLAUDE.md
   git commit -m "Add project memory configuration"
   ```

#### Method 3: Quick Updates with `#`

Once CLAUDE.md exists, add rules quickly during conversations:

```markdown
# Use semantic versioning for all releases

# Always run tests before committing

# Prefer composition over inheritance
```

Claude will prompt you to choose which memory file to update.

### Setup Personal Memory

1. **Create ~/.claude directory:**
   ```bash
   mkdir -p ~/.claude
   ```

2. **Create personal CLAUDE.md:**
   ```bash
   touch ~/.claude/CLAUDE.md
   ```

3. **Add your preferences:**
   ```bash
   cat > ~/.claude/CLAUDE.md << 'EOF'
   # My Development Preferences

   ## About Me
   - Experience Level: [Your level]
   - Preferred Languages: [Your languages]
   - Communication Style: [Your style]

   ## Code Preferences
   - [Your preferences]
   EOF
   ```

### Setup Directory-Specific Memory

1. **Create memory for specific directories:**
   ```bash
   mkdir -p /path/to/directory/.claude
   touch /path/to/directory/CLAUDE.md
   ```

2. **Add directory-specific rules:**
   ```bash
   cat > /path/to/directory/CLAUDE.md << 'EOF'
   # [Directory Name] Standards

   This file overrides root CLAUDE.md for this directory.

   ## [Specific Standards]
   EOF
   ```

3. **Commit to version control:**
   ```bash
   git add /path/to/directory/CLAUDE.md
   git commit -m "Add [directory] memory configuration"
   ```

### Verify Setup

1. **Check memory locations:**
   ```bash
   # Project root memory
   ls -la ./CLAUDE.md

   # Personal memory
   ls -la ~/.claude/CLAUDE.md
   ```

2. **Claude Code will automatically load** these files when starting a session

3. **Test with Claude Code** by starting a new session in your project

## Official Documentation

For the most up-to-date information, refer to the official Claude Code documentation:

- **[Memory Documentation](https://code.claude.com/docs/en/memory)** - Complete memory system reference
- **[Slash Commands Reference](https://code.claude.com/docs/en/interactive-mode)** - All built-in commands including `/init` and `/memory`
- **[CLI Reference](https://code.claude.com/docs/en/cli-reference)** - Command-line interface documentation

### Key Technical Details from Official Docs

**Memory Loading:**

- All memory files are automatically loaded when Claude Code launches
- Claude traverses upward from the current working directory to discover CLAUDE.md files
- Subtree files are discovered and loaded contextually when accessing those directories

**Import Syntax:**

- Use `@path/to/file` to include external content (e.g., `@~/.claude/my-project-instructions.md`)
- Supports both relative and absolute paths
- Recursive imports supported with a maximum depth of 5
- First-time external imports trigger an approval dialog
- Not evaluated inside markdown code spans or code blocks
- Automatically includes referenced content in Claude's context

**Memory Hierarchy Precedence:**

1. Managed Policy (highest precedence)
2. Managed Drop-ins (`managed-settings.d/`, v2.1.83+)
3. Project Memory
4. Project Rules (`.claude/rules/`)
5. User Memory
6. User-Level Rules (`~/.claude/rules/`)
7. Local Project Memory
8. Auto Memory (lowest precedence)

## Related Concepts Links

### Integration Points
- [MCP Protocol](../05-mcp/) - Live data access alongside memory
- [Slash Commands](../01-slash-commands/) - Session-specific shortcuts
- [Skills](../03-skills/) - Automated workflows with memory context

### Related Claude Features
- [Claude Web Memory](https://claude.ai) - Automatic synthesis
- [Official Memory Docs](https://code.claude.com/docs/en/memory) - Anthropic documentation

---
**Last Updated**: April 24, 2026
**Claude Code Version**: 2.1.119
**Sources**:
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/settings
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
