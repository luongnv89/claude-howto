# Proposal: update-subagents-lesson

## Summary

Update the `04-subagents` lesson to align with the official Claude Code documentation at https://code.claude.com/docs/en/sub-agents. The current lesson is missing several key features and uses outdated configuration formats.

## Motivation

The existing subagents lesson lacks critical features documented in the official docs:

1. **Missing `/agents` command** - The interactive management interface
2. **Incomplete configuration fields** - Missing `model`, `permissionMode`, `skills` fields
3. **No built-in subagents section** - General-Purpose, Plan, and Explore agents not documented
4. **Missing resumable agents feature** - Agent continuation with `agentId`
5. **No CLI-based configuration** - `--agents` flag for session-specific agents
6. **Outdated file format** - Uses `system_prompt` instead of YAML frontmatter with markdown body
7. **Missing thoroughness levels** - Quick, Medium, Very thorough for Explore agent
8. **No proactive invocation guidance** - "use PROACTIVELY" description patterns

## Scope

### In Scope
- Update `04-subagents/README.md` with all official documentation features
- Update example subagent files to use correct YAML frontmatter format
- Add new example subagents (debugger, data-scientist) from official docs
- Document built-in subagents (General-Purpose, Plan, Explore)
- Add `/agents` command documentation
- Add CLI-based configuration section
- Document resumable agents feature
- Update installation and usage instructions

### Out of Scope
- Plugin subagents in `07-plugins/` (separate concern)
- Creating new advanced tutorials
- Video or interactive content

## Key Changes

### 1. Configuration Format Update

**Current** (incorrect):
```yaml
---
name: agent-name
description: Brief description
tools: read, grep, diff
---
```

**Updated** (per official docs):
```yaml
---
name: agent-name
description: Description of when this subagent should be invoked
tools: tool1, tool2, tool3  # Optional - inherits all tools if omitted
model: sonnet  # Optional - specify model alias or 'inherit'
permissionMode: default  # Optional - permission mode
skills: skill1, skill2  # Optional - skills to auto-load
---

Your subagent's system prompt goes here in markdown.
```

### 2. Built-in Subagents Documentation

Add new section documenting:
- **General-Purpose** - Sonnet model, all tools, complex tasks
- **Plan** - Sonnet model, research tools, plan mode
- **Explore** - Haiku model, read-only, fast codebase searching with thoroughness levels

### 3. Management Features

- `/agents` command for interactive management
- CLI `--agents` flag for session-specific configuration
- Resumable agents with `agentId`

### 4. Example Updates

Update existing examples and add:
- Debugger subagent (from official docs)
- Data Scientist subagent (from official docs)

## Success Criteria

- [ ] README covers all features from official documentation
- [ ] Configuration examples use correct YAML frontmatter format
- [ ] All 5 existing example agents updated to new format
- [ ] 2 new example agents added (debugger, data-scientist)
- [ ] Built-in subagents documented
- [ ] `/agents` command documented
- [ ] Resumable agents feature documented
- [ ] Installation instructions updated
