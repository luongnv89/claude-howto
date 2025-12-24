## MODIFIED Requirements

### Requirement: Memory Hierarchy Documentation
The memory lesson SHALL document the complete 5-level memory hierarchy including Enterprise Policy, Project Memory, Project Rules, User Memory, and Project Local memory types.

#### Scenario: Complete hierarchy explanation
- **WHEN** a reader views the memory hierarchy section
- **THEN** they SHALL see all 5 memory levels with their locations, scopes, and sharing capabilities

#### Scenario: Enterprise Policy Windows path
- **WHEN** a reader views the Enterprise Policy location for Windows
- **THEN** the path SHALL be `C:\Program Files\ClaudeCode\CLAUDE.md`

#### Scenario: Memory type comparison table
- **WHEN** a reader views the memory type comparison table
- **THEN** it SHALL include Project Rules (`.claude/rules/*.md`) and Project Local (`CLAUDE.local.md`) as distinct types

## ADDED Requirements

### Requirement: Modular Rules Documentation
The memory lesson SHALL document the `.claude/rules/` directory for organizing instructions into topic-specific markdown files.

#### Scenario: Rules directory structure
- **WHEN** a reader views the modular rules section
- **THEN** they SHALL see an example directory structure showing `.claude/rules/` with subdirectories

#### Scenario: Benefits explanation
- **WHEN** a reader views the modular rules section
- **THEN** they SHALL understand the benefits of topic-specific rule files for organization

### Requirement: Path-Specific Rules Documentation
The memory lesson SHALL document how to use YAML frontmatter with `paths:` directive to scope rules to specific file patterns.

#### Scenario: YAML frontmatter example
- **WHEN** a reader views the path-specific rules section
- **THEN** they SHALL see an example of YAML frontmatter with `paths:` directive

#### Scenario: Glob pattern table
- **WHEN** a reader views the path-specific rules section
- **THEN** they SHALL see a table of glob pattern examples with explanations

### Requirement: Project Local Memory Documentation
The memory lesson SHALL document `CLAUDE.local.md` files for personal project preferences that are auto-gitignored.

#### Scenario: Local memory explanation
- **WHEN** a reader views the project local memory section
- **THEN** they SHALL understand that `CLAUDE.local.md` is for personal preferences on shared projects

#### Scenario: Auto-gitignore behavior
- **WHEN** a reader views the project local memory section
- **THEN** they SHALL understand that these files are automatically excluded from git

### Requirement: Symlink Support Documentation
The memory lesson SHALL document how to share rules across projects using symbolic links.

#### Scenario: Symlink examples
- **WHEN** a reader views the symlink support section
- **THEN** they SHALL see bash examples for creating symlinks to shared rule files and directories

### Requirement: Memory Lookup Algorithm Documentation
The memory lesson SHALL document how Claude Code discovers and loads memory files recursively.

#### Scenario: Recursive search explanation
- **WHEN** a reader views the memory lookup section
- **THEN** they SHALL understand the recursive upward search from current directory to root

#### Scenario: Subtree discovery
- **WHEN** a reader views the memory lookup section
- **THEN** they SHALL understand that subtree files are discovered when those files are accessed
