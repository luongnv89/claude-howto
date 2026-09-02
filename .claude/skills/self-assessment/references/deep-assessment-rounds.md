# Deep Assessment — Round Questions

The 5 rounds for Deep Assessment. Present one AskUserQuestion call per round (multi-select, max 4 options). Each round covers 2 feature areas with 2 options each. The scoring map for each round is duplicated in SKILL.md Step 2B so results can be computed without re-reading this file.

---

**Round 1 — Slash Commands & Memory** (header: "Commands")

"Which of these have you done? Select all that apply."
Options:
1. "Created a custom slash command or skill" — Written a SKILL.md file with frontmatter, or created .claude/commands/ files
2. "Used dynamic context in commands" — Used `$ARGUMENTS`, `$0`/`$1`, backtick `!command` syntax, or `@file` references in skill/command files
3. "Set up project + personal memory" — Created both a project CLAUDE.md and personal ~/.claude/CLAUDE.md (or CLAUDE.local.md)
4. "Used memory hierarchy features" — Understand how the 7 memory locations are concatenated into context (loaded root-down, CLAUDE.local.md appended after CLAUDE.md at each level, subdirectory files loaded on demand), used .claude/rules/ directory, path-specific rules, or @import syntax

**Scoring:** Options 1-2 → **Slash Commands** (0-2); Options 3-4 → **Memory** (0-2)

---

**Round 2 — Skills & Hooks** (header: "Automation")

"Which of these have you done? Select all that apply."
Options:
1. "Installed and used an auto-invoked skill" — A skill that triggers automatically based on its description, without manual /command invocation
2. "Controlled skill invocation behavior" — Used `disable-model-invocation`, `user-invocable`, or `context: fork` with agent field in SKILL.md frontmatter
3. "Set up a PreToolUse or PostToolUse hook" — Configured a hook that runs before/after tool execution (e.g., command validator, auto-formatter)
4. "Used advanced hook features" — Configured prompt-type hooks, component-scoped hooks in SKILL.md, HTTP hooks, or hooks with custom JSON output (updatedInput, systemMessage)

**Scoring:** Options 1-2 → **Skills** (0-2); Options 3-4 → **Hooks** (0-2)

---

**Round 3 — MCP & Subagents** (header: "Integration")

"Which of these have you done? Select all that apply."
Options:
1. "Connected an MCP server and used its tools" — e.g., GitHub MCP for PRs/issues, database MCP for queries, or any external data source
2. "Used advanced MCP features" — Project-scope .mcp.json, OAuth authentication, MCP resources with @mentions, Tool Search, or `claude mcp serve`
3. "Created or configured custom subagents" — Defined agents in .claude/agents/ with custom tools, model, or permissions
4. "Used advanced subagent features" — Worktree isolation, persistent agent memory, background tasks with Ctrl+B, agent allowlists with `Agent(agent_type)` (the `Task(...)` form is a back-compat alias), or agent teams

**Scoring:** Options 1-2 → **MCP** (0-2); Options 3-4 → **Subagents** (0-2)

---

**Round 4 — Checkpoints & Advanced Features** (header: "Power User")

"Which of these have you done? Select all that apply."
Options:
1. "Used checkpoints for safe experimentation" — Created checkpoints, used Esc+Esc or /rewind, restored code and/or conversation, or used either Summarize option (summarize from here / summarize up to here)
2. "Used planning mode or extended thinking" — Activated planning via /plan, Shift+Tab, or --permission-mode plan; toggled extended thinking with Alt+T/Option+T
3. "Configured permission modes" — Used any of the six modes — manual (renamed from default in v2.1.200), acceptEdits, plan, auto, dontAsk, or bypassPermissions — via CLI flags, keyboard shortcuts, or settings
4. "Used remote/desktop/web features" — Used `claude --remote-control`, `claude --cloud`, `/teleport`, `/desktop`, or worktrees with `claude -w`

**Scoring:** Option 1 → **Checkpoints** (0-1); Options 2-4 → **Advanced Features** (0-3)

---

**Round 5 — Plugins & CLI** (header: "Mastery")

"Which of these have you done? Select all that apply."
Options:
1. "Installed or created a plugin" — Used a bundled plugin from marketplace, or created a .claude-plugin/ directory with plugin.json manifest
2. "Used plugin advanced features" — Plugin skills (`skills/` — the preferred form; namespaced `commands/` is legacy but still works), plugin hooks, plugin MCP servers, LSP configuration, or --plugin-dir flag for testing
3. "Used print mode in scripts or CI/CD" — Used `claude -p` with --output-format json, --max-turns, piped input, or integrated into GitHub Actions / CI pipelines
4. "Used advanced CLI features" — Session resumption (-c/-r), --agents flag, --json-schema for structured output, --fallback-model, --from-pr, or batch processing loops

**Scoring:** Options 1-2 → **Plugins** (0-2); Options 3-4 → **CLI** (0-2)

---

**Last Updated**: September 2, 2026
**Claude Code Version**: 2.1.257
**Sources**:
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/plugins-reference
