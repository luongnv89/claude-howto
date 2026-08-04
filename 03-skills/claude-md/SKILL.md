---
name: claude-md
description: Create or update CLAUDE.md files following best practices for optimal AI agent onboarding
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty). User may specify:
- `create` - Create new CLAUDE.md from scratch
- `update` - Improve existing CLAUDE.md
- `audit` - Analyze and report on current CLAUDE.md quality
- A specific path to create/update (e.g., `src/api/CLAUDE.md` for directory-specific instructions)

## Core Principles

**LLMs are stateless**: CLAUDE.md is the only file automatically included in every conversation. It serves as the primary onboarding document for AI agents into your codebase.

### The Golden Rules

1. **Less is More**: Frontier LLMs can follow ~150-200 instructions. Claude Code's system prompt already uses ~50. Keep your CLAUDE.md focused and concise.

2. **Universal Applicability**: Only include information relevant to EVERY session. Task-specific instructions belong in separate files.

3. **Don't Use Claude as a Linter**: Style guidelines bloat context and degrade instruction-following. Use deterministic tools (prettier, eslint, etc.) instead.

4. **Never Auto-Generate**: CLAUDE.md is the highest leverage point of the AI harness. Craft it manually with careful consideration.

## Execution Flow

### 1. Project Analysis

First, analyze the current project state:

1. Check for existing CLAUDE.md files:
   - Root level: `./CLAUDE.md` or `.claude/CLAUDE.md`
   - Directory-specific: `**/CLAUDE.md`
   - Global user config: `~/.claude/CLAUDE.md`

2. Identify the project structure:
   - Technology stack (languages, frameworks)
   - Project type (monorepo, single app, library)
   - Development tools (package manager, build system, test runner)

3. Review existing documentation:
   - README.md
   - CONTRIBUTING.md
   - package.json, pyproject.toml, Cargo.toml, etc.

### 2. Content Strategy (WHAT, WHY, HOW)

Structure CLAUDE.md around three dimensions:

#### WHAT - Technology & Structure
- Technology stack overview
- Project organization (especially important for monorepos)
- Key directories and their purposes

#### WHY - Purpose & Context
- What the project does
- Why certain architectural decisions were made
- What each major component is responsible for

#### HOW - Workflow & Conventions
- Development workflow (bun vs node, pip vs uv, etc.)
- Testing procedures and commands
- Verification and build methods
- Critical "gotchas" or non-obvious requirements

### 3. Progressive Disclosure Strategy

For larger projects, recommend creating an `agent_docs/` folder:

```
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- architecture_decisions.md
```

In CLAUDE.md, reference these files with instructions like:
```markdown
For detailed build instructions, refer to `agent_docs/building_the_project.md`
```

**Important**: Use `file:line` references instead of code snippets to avoid outdated context.

### 4. Quality Constraints

When creating or updating CLAUDE.md:

1. **Target Length**: Keep it under a few hundred lines; shorter is better
2. **No Style Rules**: Remove any linting/formatting instructions
3. **No Task-Specific Instructions**: Move to separate files
4. **No Code Snippets**: Use file references instead
5. **No Redundant Information**: Don't repeat what's in package.json or README

### 5. Essential Sections

A well-structured CLAUDE.md should include:

```markdown
# Project Name

Brief one-line description.

## Tech Stack
- Primary language and version
- Key frameworks/libraries
- Database/storage (if any)

## Project Structure
[Only for monorepos or complex structures]
- `apps/` - Application entry points
- `packages/` - Shared libraries

## Development Commands
- Install: `command`
- Test: `command`
- Build: `command`

## Critical Conventions
[Only non-obvious, high-impact conventions]
- Convention 1 with brief explanation
- Convention 2 with brief explanation

## Known Issues / Gotchas
[Things that consistently trip up developers]
- Issue 1
- Issue 2
```

### 6. Anti-Patterns to Avoid

**DO NOT include:**
- Code style guidelines (use linters)
- Documentation on how to use Claude
- Long explanations of obvious patterns
- Copy-pasted code examples
- Generic best practices ("write clean code")
- Instructions for specific tasks
- Auto-generated content
- Extensive TODO lists

### 7. Validation Checklist

Before finalizing, verify:

- [ ] Kept under a few hundred lines; shorter is better
- [ ] Every line applies to ALL sessions
- [ ] No style/formatting rules
- [ ] No code snippets (use file references)
- [ ] Commands are verified to work
- [ ] Progressive disclosure used for complex projects
- [ ] Critical gotchas are documented
- [ ] No redundancy with README.md

## Output Format

### For `create` or default:

1. Analyze the project
2. Draft a CLAUDE.md following the structure above
3. Present the draft for review
4. Write to the appropriate location after approval

### For `update`:

1. Read existing CLAUDE.md
2. Audit against best practices
3. Identify:
   - Content to remove (style rules, code snippets, task-specific)
   - Content to condense
   - Missing essential information
4. Present changes for review
5. Apply changes after approval

### For `audit`:

1. Read existing CLAUDE.md
2. Generate a report with:
   - Current line count vs target
   - Percentage of universally-applicable content
   - List of anti-patterns found
   - Recommendations for improvement
3. Do NOT modify the file, only report

## AGENTS.md Handling

If the user requests AGENTS.md creation/update:

**Claude Code does not read AGENTS.md directly.** To make it take effect, import it from CLAUDE.md with `@AGENTS.md`, or symlink `CLAUDE.md` to it. This is the single most common misunderstanding about the file.

AGENTS.md is a cross-tool project-context file — the same *category* of document as CLAUDE.md, not an agent-definition format. It exists so several coding agents can share one set of project conventions:
- Build, test, and lint commands
- Code style and architectural conventions
- Repository layout and where things live

Subagents are defined separately, in `.claude/agents/*.md` — not in AGENTS.md.

Apply similar principles:
- Keep focused and concise
- Use progressive disclosure
- Reference external docs instead of embedding content

## Notes

- Always verify commands work before including them
- When in doubt, leave it out - less is more
- The system reminder tells Claude that CLAUDE.md "may or may not be relevant" - the more noise, the more it gets ignored
- Monorepos benefit most from clear WHAT/WHY/HOW structure
- Directory-specific CLAUDE.md files should be even more focused

---

**Last Updated**: August 4, 2026
**Claude Code Version**: 2.1.220
**Sources**:
- https://code.claude.com/docs/en/skills
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
