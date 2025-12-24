# Change: Update Memory Lesson with Latest Documentation

## Why

The current memory lesson (`blog-posts/02-memory.md`) is based on older Claude Code documentation. The official documentation at `https://code.claude.com/docs/en/memory` includes several new features and updates that the lesson doesn't cover, making it incomplete for readers who want to learn about Claude Code's full memory capabilities.

## What Changes

### New Features to Add
- **Project Rules** (`.claude/rules/*.md`) - Modular, topic-specific markdown files for organizing instructions
- **Path-Specific Rules** - YAML frontmatter with `paths:` to scope rules to specific file patterns
- **Glob Pattern Support** - Examples of glob patterns for path-specific rules
- **Project Local Memory** (`CLAUDE.local.md`) - Personal project preferences that are auto-gitignored
- **Symlink Support** - Sharing rules across projects using symbolic links

### Updates to Existing Content
- **Memory Hierarchy Table** - Update to include Project Rules and Project Local as additional memory types
- **Enterprise Policy Windows Path** - Correct to `C:\Program Files\ClaudeCode\CLAUDE.md` (currently shows `C:\ProgramData\ClaudeCode\CLAUDE.md`)
- **Memory Lookup Algorithm** - Add detailed explanation of recursive upward search behavior
- **Best Practices Section** - Add guidelines for `.claude/rules/` organization

### Structure Improvements
- Add new section: "Modular Rules with `.claude/rules/`"
- Add new section: "Path-Specific Rules"
- Update directory structure example to show `.claude/rules/` organization
- Improve organization of content to match official documentation structure

## Impact

- **Affected files**: `blog-posts/02-memory.md`
- **User benefit**: Readers will learn about complete memory capabilities including modular rules and path-specific scoping
- **No breaking changes**: All existing content remains valid; this adds new sections and updates outdated information
