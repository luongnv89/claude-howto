---
name: self-assessment
version: 2.4.0
description: Comprehensive Claude Code self-assessment and learning path advisor. Runs a multi-category quiz covering 10 feature areas, produces a detailed skill profile with per-topic scores, identifies specific gaps, and generates a personalized learning path with prioritized next steps. Use when asked to "assess my level", "take the quiz", "find my level", "where should I start", "what should I learn next", "check my skills", "skill check", or "level up".
---

# Self-Assessment & Learning Path Advisor

Comprehensive interactive assessment that evaluates Claude Code proficiency across 10 feature areas, identifies specific skill gaps, and generates a personalized learning path to level up.

## Instructions

### Step 1: Welcome & Choose Assessment Mode

Present the user with a choice of assessment depth:

Use AskUserQuestion with these options:
- **Quick Assessment** — "8 questions, ~2 minutes. Determines your overall level (Beginner/Intermediate/Advanced) and gives a learning path."
- **Deep Assessment** — "5 categories with detailed questions, ~5 minutes. Gives per-topic skill scores, identifies specific gaps, and builds a prioritized learning path."

If user chooses **Quick Assessment**, go to Step 2A.
If user chooses **Deep Assessment**, go to Step 2B.

---

### Step 2A: Quick Assessment

Present TWO multi-select questions (AskUserQuestion supports max 4 options each):

**Question 1** (header: "Basics"):
"Part 1/2: Which of these Claude Code skills do you already have?"
Options:
1. "Start Claude Code and chat" — I can run `claude` and interact with it
2. "Created/edited CLAUDE.md" — I have set up project or user memory
3. "Used 3+ slash commands" — e.g., /help, /compact, /model, /clear
4. "Created custom command/skill" — Written a SKILL.md or custom command file

**Question 2** (header: "Advanced"):
"Part 2/2: Which of these advanced skills do you have?"
Options:
1. "Configured an MCP server" — e.g., GitHub, database, or other external data source
2. "Set up hooks" — Configured hooks in ~/.claude/settings.json
3. "Created/used subagents" — Used .claude/agents/ for task delegation
4. "Used print mode (claude -p)" — Used `claude -p` for non-interactive or CI/CD use

**Scoring:**
- 0-2 total = Level 1: Beginner
- 3-5 total = Level 2: Intermediate
- 6-8 total = Level 3: Advanced

Go to Step 3 with the level result, listing which specific items were NOT checked as gaps.

---

### Step 2B: Deep Assessment

Present 5 rounds of questions, one AskUserQuestion call per round. Each round covers 2 related feature areas. Use multi-select for all rounds.

**IMPORTANT**: AskUserQuestion supports max 4 options per question. Each round has exactly 1 question with 4 options covering 2 topics (2 options per topic).

---

**Round 1 — Slash Commands & Memory** (header: "Commands")

"Which of these have you done? Select all that apply."
Options:
1. "Created a custom slash command or skill" — Written a SKILL.md file with frontmatter, or created .claude/commands/ files
2. "Used dynamic context in commands" — Used `$ARGUMENTS`, `$0`/`$1`, backtick `!command` syntax, or `@file` references in skill/command files
3. "Set up project + personal memory" — Created both a project CLAUDE.md and personal ~/.claude/CLAUDE.md (or CLAUDE.local.md)
4. "Used memory hierarchy features" — Understand how the 7 memory locations are concatenated into context (loaded root-down, CLAUDE.local.md appended after CLAUDE.md at each level, subdirectory files loaded on demand), used .claude/rules/ directory, path-specific rules, or @import syntax

**Scoring for Round 1:**
- Options 1-2 map to **Slash Commands** (0-2 points)
- Options 3-4 map to **Memory** (0-2 points)

---

**Round 2 — Skills & Hooks** (header: "Automation")

"Which of these have you done? Select all that apply."
Options:
1. "Installed and used an auto-invoked skill" — A skill that triggers automatically based on its description, without manual /command invocation
2. "Controlled skill invocation behavior" — Used `disable-model-invocation`, `user-invocable`, or `context: fork` with agent field in SKILL.md frontmatter
3. "Set up a PreToolUse or PostToolUse hook" — Configured a hook that runs before/after tool execution (e.g., command validator, auto-formatter)
4. "Used advanced hook features" — Configured prompt-type hooks, component-scoped hooks in SKILL.md, HTTP hooks, or hooks with custom JSON output (updatedInput, systemMessage)

**Scoring for Round 2:**
- Options 1-2 map to **Skills** (0-2 points)
- Options 3-4 map to **Hooks** (0-2 points)

---

**Round 3 — MCP & Subagents** (header: "Integration")

"Which of these have you done? Select all that apply."
Options:
1. "Connected an MCP server and used its tools" — e.g., GitHub MCP for PRs/issues, database MCP for queries, or any external data source
2. "Used advanced MCP features" — Project-scope .mcp.json, OAuth authentication, MCP resources with @mentions, Tool Search, or `claude mcp serve`
3. "Created or configured custom subagents" — Defined agents in .claude/agents/ with custom tools, model, or permissions
4. "Used advanced subagent features" — Worktree isolation, persistent agent memory, background tasks with Ctrl+B, agent allowlists with `Agent(agent_type)` (the `Task(...)` form is a back-compat alias), or agent teams

**Scoring for Round 3:**
- Options 1-2 map to **MCP** (0-2 points)
- Options 3-4 map to **Subagents** (0-2 points)

---

**Round 4 — Checkpoints & Advanced Features** (header: "Power User")

"Which of these have you done? Select all that apply."
Options:
1. "Used checkpoints for safe experimentation" — Created checkpoints, used Esc+Esc or /rewind, restored code and/or conversation, or used either Summarize option (summarize from here / summarize up to here)
2. "Used planning mode or extended thinking" — Activated planning via /plan, Shift+Tab, or --permission-mode plan; toggled extended thinking with Alt+T/Option+T
3. "Configured permission modes" — Used any of the six modes — manual (renamed from default in v2.1.200), acceptEdits, plan, auto, dontAsk, or bypassPermissions — via CLI flags, keyboard shortcuts, or settings
4. "Used remote/desktop/web features" — Used `claude remote-control`, `claude --remote`, `/teleport`, `/desktop`, or worktrees with `claude -w`

**Scoring for Round 4:**
- Option 1 maps to **Checkpoints** (0-1 point)
- Options 2-4 map to **Advanced Features** (0-3 points, cap at 2)

---

**Round 5 — Plugins & CLI** (header: "Mastery")

"Which of these have you done? Select all that apply."
Options:
1. "Installed or created a plugin" — Used a bundled plugin from marketplace, or created a .claude-plugin/ directory with plugin.json manifest
2. "Used plugin advanced features" — Plugin skills (`skills/` — the preferred form; namespaced `commands/` is legacy but still works), plugin hooks, plugin MCP servers, LSP configuration, or --plugin-dir flag for testing
3. "Used print mode in scripts or CI/CD" — Used `claude -p` with --output-format json, --max-turns, piped input, or integrated into GitHub Actions / CI pipelines
4. "Used advanced CLI features" — Session resumption (-c/-r), --agents flag, --json-schema for structured output, --fallback-model, --from-pr, or batch processing loops

**Scoring for Round 5:**
- Options 1-2 map to **Plugins** (0-2 points)
- Options 3-4 map to **CLI** (0-2 points)

---

### Step 3: Calculate & Present Results

#### 3A: For Quick Assessment

Count total selections and determine level. Then present:

```markdown
## Claude Code Skill Assessment Results

### Your Level: [Level 1: Beginner / Level 2: Intermediate / Level 3: Advanced]

You checked **N/8** items.

[One-line motivational summary based on level]

### Your Skill Profile

| Area | Status |
|------|--------|
| Basic CLI & Conversations | [Checked/Gap] |
| CLAUDE.md & Memory | [Checked/Gap] |
| Slash Commands (built-in) | [Checked/Gap] |
| Custom Commands & Skills | [Checked/Gap] |
| MCP Servers | [Checked/Gap] |
| Hooks | [Checked/Gap] |
| Subagents | [Checked/Gap] |
| Print Mode & CI/CD | [Checked/Gap] |

### Identified Gaps

[For each unchecked item, provide a 1-line description of what to learn and a link to the tutorial]

### Your Personalized Learning Path

[Output the level-specific learning path — see Step 4]
```

#### 3B: For Deep Assessment

Calculate per-topic scores from the 5 rounds. Each topic gets 0-2 points. Then present:

```markdown
## Claude Code Skill Assessment Results

### Overall Level: [Level 1 / Level 2 / Level 3]

**Total Score: N/19 points**

[One-line motivational summary]

### Your Skill Profile

| Feature Area | Score | Mastery | Status |
|-------------|-------|---------|--------|
| Slash Commands | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Memory | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Skills | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Hooks | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| MCP | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Subagents | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Checkpoints | N/1 | [None/Proficient] | [Learn/Mastered] |
| Advanced Features | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Plugins | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| CLI | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |

**Mastery key:** 0 = None, 1 = Basic, 2 = Proficient

### Strength Areas
[List topics with score 2/2 — these are mastered]

### Priority Gaps (Learn Next)
[List topics with score 0 — these need attention first, ordered by dependency]

### Review Areas
[List topics with score 1/2 — basics known but advanced features not yet used]

### Your Personalized Learning Path

[Output gap-specific learning path — see Step 4]
```

**Overall level calculation for Deep Assessment:**
- 0-6 total points = Level 1: Beginner
- 7-13 total points = Level 2: Intermediate
- 14-19 total points = Level 3: Advanced

---

### Step 4: Generate Personalized Learning Path

Based on the assessment results, generate a learning path that is specific to the user's gaps. Do NOT just repeat the generic level path — adapt it.

#### Rules for Path Generation

1. **Skip mastered topics**: If a topic scored 2/2, do not include it in the path.
2. **Prioritize by dependency order**: Slash Commands before Skills, Memory before Subagents, etc. The dependency order is:
   - Slash Commands (no deps) -> Skills (depends on Slash Commands)
   - Memory (no deps) -> Subagents (depends on Memory)
   - CLI Basics (no deps) -> CLI Mastery (depends on all)
   - Checkpoints (no deps)
   - Hooks (depends on Slash Commands)
   - MCP (no deps) -> Plugins (depends on MCP, Skills, Hooks)
   - Advanced Features (depends on all previous)
3. **For score 1/2 topics**: Recommend the "deep dive" — link to the specific advanced section they're missing.
4. **Estimate time**: Sum only the topics they need to learn/review.
5. **Group into phases**: Organize remaining topics into logical phases of 2-3 topics each.

#### Path Output Format

```markdown
### Your Personalized Learning Path

**Estimated time**: ~N hours (adjusted for your current skills)

#### Phase 1: [Phase Name] (~N hours)
[Only if they have gaps in these areas]

**[Topic Name]** — [Learn from scratch / Deep dive into advanced features]
- Tutorial: [link to tutorial directory]
- Focus on: [specific sections/concepts they need]
- Key exercise: [one concrete exercise to do]
- You'll know it's done when: [specific success criterion]

**[Topic Name]** — ...

---

#### Phase 2: [Phase Name] (~N hours)
...

---

### Recommended Practice Projects

Based on your gaps, try these real-world exercises to solidify your learning:

1. **[Project name]**: [1-line description combining 2-3 gap topics]
2. **[Project name]**: [1-line description]
3. **[Project name]**: [1-line description]
```

#### Topic-Specific Recommendations

Use these specific recommendations when a topic is a gap:

**Slash Commands (score 0)**:
- Tutorial: [01-slash-commands/](../../../01-slash-commands/)
- Focus on: Built-in commands reference, creating your first SKILL.md, `$ARGUMENTS` syntax
- Key exercise: Create a `/optimize` command and test it
- Done when: You can create a custom skill with arguments and dynamic context

**Slash Commands (score 1 — review)**:
- Focus on: Dynamic context with `!`backtick`` syntax, `@file` references, `disable-model-invocation` vs `user-invocable` control
- Done when: You can create a skill that injects live command output and controls its own invocation behavior

**Memory (score 0)**:
- Tutorial: [02-memory/](../../../02-memory/)
- Focus on: CLAUDE.md creation, `/init` and `/memory` commands, `#` prefix for quick updates
- Key exercise: Create a project CLAUDE.md with your coding standards
- Done when: Claude remembers your preferences across sessions

**Memory (score 1 — review)**:
- Focus on: the 7 memory locations and how they are concatenated into context (loaded root-down, not overridden), .claude/rules/ directory with path-specific rules, `@import` syntax (max depth 4), Auto Memory MEMORY.md (Claude loads its first 200 lines or 25 KB, whichever comes first — a load cap, not a file-size limit)
- Done when: You have modular rules for different directories and understand how every memory file is concatenated into context

**Skills (score 0)**:
- Tutorial: [03-skills/](../../../03-skills/)
- Focus on: SKILL.md format, auto-invocation via description field, progressive disclosure (3 loading levels)
- Key exercise: Install the code-review skill and verify it auto-triggers
- Done when: A skill automatically activates based on conversation context

**Skills (score 1 — review)**:
- Focus on: `context: fork` with `agent` field for subagent execution, `disable-model-invocation` vs `user-invocable`, the skill-listing budget (1% of the context window, fallback 8,000 characters, 250 characters per entry), bundled resources (scripts/, references/, assets/)
- Done when: You can create a skill that runs in a subagent with forked context

**Hooks (score 0)**:
- Tutorial: [06-hooks/](../../../06-hooks/)
- Focus on: Configuration structure (matcher + hooks array), PreToolUse/PostToolUse events, exit codes (0=success, 2=block), JSON input/output format
- Key exercise: Create a PreToolUse hook that validates Bash commands
- Done when: A hook blocks dangerous commands before execution

**Hooks (score 1 — review)**:
- Focus on: All 31 hook events (including PostToolUseFailure, StopFailure, TaskCreated, CwdChanged, FileChanged, PostCompact, Elicitation, ElicitationResult, Setup, UserPromptExpansion, MessageDisplay), 5 hook types (command, http, mcp_tool, prompt, agent — agent hooks are experimental and may change), component-scoped hooks in SKILL.md frontmatter, HTTP hooks with allowedEnvVars, `CLAUDE_ENV_FILE` for SessionStart/CwdChanged/FileChanged
- Done when: You can create a prompt-based Stop hook and a component-scoped hook in a skill

**MCP (score 0)**:
- Tutorial: [05-mcp/](../../../05-mcp/)
- Focus on: `claude mcp add` command, transport types (`http` recommended, `stdio`, `ws` for push-style servers, and the deprecated `sse` — note `--transport` does not accept `ws`, so add WebSocket servers with `claude mcp add-json`), GitHub MCP setup, environment variable expansion
- Key exercise: Add GitHub MCP server and query PRs
- Done when: You can query live data from an external service via MCP

**MCP (score 1 — review)**:
- Focus on: Project-scope .mcp.json (requires team approval), OAuth 2.0 auth, MCP resources with `@server:resource` mentions, Tool Search (ENABLE_TOOL_SEARCH), `claude mcp serve`, output limits (10,000 tokens warning; 25,000 tokens default max via `MAX_MCP_OUTPUT_TOKENS`; 50,000 characters disk-persistence threshold)
- Done when: You have a project .mcp.json and understand Tool Search auto mode

**Subagents (score 0)**:
- Tutorial: [04-subagents/](../../../04-subagents/)
- Focus on: Agent file format (.claude/agents/*.md), built-in agents (Explore, Plan, general-purpose, claude, statusline-setup, claude-code-guide), tools/model/permissionMode config, spawn limits (depth default 3 since v2.1.219, concurrency default 20, and the 200-per-session spawn cap removed in v2.1.224)
- Key exercise: Create a code-reviewer subagent and test delegation
- Done when: Claude delegates code review to your custom agent

**Subagents (score 1 — review)**:
- Focus on: Worktree isolation (`isolation: worktree`), persistent agent memory (`memory` field with scopes), background agents (Ctrl+B/Ctrl+F), agent allowlists with `Agent(agent_type)` (`Task(...)` remains a back-compat alias), agent teams (`--teammate-mode`)
- Done when: You have a subagent with persistent memory running in worktree isolation

**Checkpoints (score 0)**:
- Tutorial: [08-checkpoints/](../../../08-checkpoints/)
- Focus on: Esc+Esc and /rewind access, 6 rewind options (restore code and conversation, restore conversation, restore code, summarize from here, summarize up to here, never mind), limitations (bash filesystem ops not tracked)
- Key exercise: Make experimental changes, then rewind to restore
- Done when: You can confidently experiment knowing you can rewind

**Advanced Features (score 0)**:
- Tutorial: [09-advanced-features/](../../../09-advanced-features/)
- Focus on: Planning mode (/plan or Shift+Tab), permission modes (6 types: manual — renamed from default in v2.1.200 — acceptEdits, plan, auto, dontAsk, bypassPermissions), extended thinking (Alt+T toggle)
- Key exercise: Use planning mode to design a feature, then implement it
- Done when: You can switch between planning and implementation modes fluently

**Advanced Features (score 1 — review)**:
- Focus on: Remote control (`claude remote-control`), web sessions (`claude --remote`), desktop handoff (`/desktop`), worktrees (`claude -w`), task lists (Ctrl+T), managed settings for enterprise
- Done when: You can hand off sessions between CLI, web, and desktop

**Plugins (score 0)**:
- Tutorial: [07-plugins/](../../../07-plugins/)
- Focus on: Plugin structure (.claude-plugin/plugin.json), what plugins bundle (skills, agents, MCP, hooks, settings — plus the legacy `commands/` directory, which still works but `skills/` is preferred for new plugins), installation from marketplace
- Key exercise: Install a plugin and explore its components
- Done when: You understand when to use a plugin vs standalone components

**Plugins (score 1 — review)**:
- Focus on: Creating plugin.json manifest, plugin hooks (hooks/hooks.json), LSP configuration (.lsp.json), `${CLAUDE_PLUGIN_ROOT}` variable, --plugin-dir for testing, marketplace publishing
- Done when: You can create and test a plugin for your team

**CLI (score 0)**:
- Tutorial: [10-cli/](../../../10-cli/)
- Focus on: Interactive vs print mode, `claude -p` with piping, `--output-format json`, session management (-c/-r)
- Key exercise: Pipe a file to `claude -p` and get JSON output
- Done when: You can use Claude non-interactively in a script

**CLI (score 1 — review)**:
- Focus on: --agents flag with JSON config, --json-schema for structured output, --fallback-model, --from-pr, --strict-mcp-config, batch processing with for loops, `claude mcp serve`
- Done when: You have a CI/CD script that uses Claude with structured JSON output

---

### Step 5: Offer Follow-up Actions

After presenting results, ask the user what they'd like to do next:

Use AskUserQuestion with these options:
- **Start learning** — "Help me begin the first topic in my learning path right now"
- **Deep dive on a gap** — "Explain one of my gap areas in detail so I can learn it here"
- **Practice project** — "Set up a practice project that covers my gap areas"
- **Retake assessment** — "I want to retake the quiz (maybe the other mode)"

If **Start learning**: Read the README.md of the first gap tutorial and walk the user through the first exercise.
If **Deep dive on a gap**: Ask which gap topic, then read the relevant tutorial README.md and explain the key concepts with examples.
If **Practice project**: Design a small project that combines 2-3 of their gap topics with concrete steps.
If **Retake assessment**: Go back to Step 1.

## Error Handling

### User selects no items in a round
Treat as 0 points for that round's topics. Continue to next round.

### User selects no items in any round
Assign Level 1: Beginner. Encourage starting from the beginning. Output the full Level 1 path.

### User wants to retake
Re-run from Step 1 with a fresh assessment.

### User disagrees with their level
Acknowledge their preference. Ask which level they identify with. Present the path for their chosen level with a prerequisites check for topics they may have missed.

### User asks about a specific topic
If the user says something like "tell me about hooks" or "I want to learn MCP" during the assessment, note it. After presenting results, highlight that topic in their learning path regardless of score.

## Validation

### Triggering test suite

**Should trigger:**
- "assess my level"
- "take the quiz"
- "find my level"
- "where should I start"
- "what level am I"
- "learning path quiz"
- "self-assessment"
- "what should I learn next"
- "check my skills"
- "skill check"
- "level up"
- "how good am I at Claude Code"
- "evaluate my Claude Code knowledge"

**Should NOT trigger:**
- "review my code"
- "create a skill"
- "help me with MCP"
- "explain slash commands"
- "what is a checkpoint"
