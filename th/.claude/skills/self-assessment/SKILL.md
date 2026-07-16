<!-- i18n-source: .claude/skills/self-assessment/SKILL.md -->
<!-- i18n-date: 2026-07-16 -->
---
name: self-assessment
version: 2.3.0
description: Comprehensive Claude Code self-assessment and learning path advisor. Runs a multi-category quiz covering 10 feature areas, produces a detailed skill profile with per-topic scores, identifies specific gaps, and generates a personalized learning path with prioritized next steps. Use when asked to "assess my level", "take the quiz", "find my level", "where should I start", "what should I learn next", "check my skills", "skill check", or "level up".
---

# Self-Assessment & Learning Path Advisor

การประเมินเชิงโต้ตอบแบบครอบคลุมที่ประเมินความเชี่ยวชาญ Claude Code ครอบคลุม 10 ด้านฟีเจอร์ ระบุช่องว่างทักษะเฉพาะ และสร้างเส้นทางการเรียนรู้เฉพาะบุคคลเพื่อยกระดับ

## คำแนะนำ

### ขั้นตอน 1: ต้อนรับและเลือกโหมดการประเมิน

นำเสนอตัวเลือกความลึกของการประเมินให้ผู้ใช้:

ใช้ AskUserQuestion พร้อมตัวเลือกเหล่านี้:
- **Quick Assessment** — "8 questions, ~2 minutes. Determines your overall level (Beginner/Intermediate/Advanced) and gives a learning path."
- **Deep Assessment** — "5 categories with detailed questions, ~5 minutes. Gives per-topic skill scores, identifies specific gaps, and builds a prioritized learning path."

หากผู้ใช้เลือก **Quick Assessment** ให้ไปที่ขั้นตอน 2A
หากผู้ใช้เลือก **Deep Assessment** ให้ไปที่ขั้นตอน 2B

---

### ขั้นตอน 2A: Quick Assessment

นำเสนอคำถามแบบเลือกได้หลายตัวสองข้อ (AskUserQuestion รองรับตัวเลือกสูงสุด 4 ตัวต่อข้อ):

**คำถามที่ 1** (header: "Basics"):
"Part 1/2: Which of these Claude Code skills do you already have?"
ตัวเลือก:
1. "Start Claude Code and chat" — I can run `claude` and interact with it
2. "Created/edited CLAUDE.md" — I have set up project or user memory
3. "Used 3+ slash commands" — e.g., /help, /compact, /model, /clear
4. "Created custom command/skill" — Written a SKILL.md or custom command file

**คำถามที่ 2** (header: "Advanced"):
"Part 2/2: Which of these advanced skills do you have?"
ตัวเลือก:
1. "Configured an MCP server" — e.g., GitHub, database, or other external data source
2. "Set up hooks" — Configured hooks in ~/.claude/settings.json
3. "Created/used subagents" — Used .claude/agents/ for task delegation
4. "Used print mode (claude -p)" — Used `claude -p` for non-interactive or CI/CD use

**การคิดคะแนน:**
- รวม 0-2 = Level 1: Beginner
- รวม 3-5 = Level 2: Intermediate
- รวม 6-8 = Level 3: Advanced

ไปที่ขั้นตอน 3 พร้อมผลระดับ โดยระบุรายการเฉพาะที่ **ไม่ได้** เลือกไว้ให้เป็นช่องว่าง

---

### ขั้นตอน 2B: Deep Assessment

นำเสนอคำถาม 5 รอบ หนึ่งการเรียก AskUserQuestion ต่อรอบ แต่ละรอบครอบคลุม 2 ด้านฟีเจอร์ที่เกี่ยวข้องกัน ใช้แบบเลือกได้หลายตัวสำหรับทุกรอบ

**สำคัญ**: AskUserQuestion รองรับตัวเลือกสูงสุด 4 ตัวต่อคำถาม แต่ละรอบมี 1 คำถามพอดีที่มี 4 ตัวเลือกครอบคลุม 2 หัวข้อ (2 ตัวเลือกต่อหัวข้อ)

---

**Round 1 — Slash Commands & Memory** (header: "Commands")

"Which of these have you done? Select all that apply."
ตัวเลือก:
1. "Created a custom slash command or skill" — Written a SKILL.md file with frontmatter, or created .claude/commands/ files
2. "Used dynamic context in commands" — Used `$ARGUMENTS`, `$0`/`$1`, backtick `!command` syntax, or `@file` references in skill/command files
3. "Set up project + personal memory" — Created both a project CLAUDE.md and personal ~/.claude/CLAUDE.md (or CLAUDE.local.md)
4. "Used memory hierarchy features" — Understand the 7-level priority order, used .claude/rules/ directory, path-specific rules, or @import syntax

**การคิดคะแนนสำหรับ Round 1:**
- ตัวเลือก 1-2 จับคู่กับ **Slash Commands** (0-2 คะแนน)
- ตัวเลือก 3-4 จับคู่กับ **Memory** (0-2 คะแนน)

---

**Round 2 — Skills & Hooks** (header: "Automation")

"Which of these have you done? Select all that apply."
ตัวเลือก:
1. "Installed and used an auto-invoked skill" — A skill that triggers automatically based on its description, without manual /command invocation
2. "Controlled skill invocation behavior" — Used `disable-model-invocation`, `user-invocable`, or `context: fork` with agent field in SKILL.md frontmatter
3. "Set up a PreToolUse or PostToolUse hook" — Configured a hook that runs before/after tool execution (e.g., command validator, auto-formatter)
4. "Used advanced hook features" — Configured prompt-type hooks, component-scoped hooks in SKILL.md, HTTP hooks, or hooks with custom JSON output (updatedInput, systemMessage)

**การคิดคะแนนสำหรับ Round 2:**
- ตัวเลือก 1-2 จับคู่กับ **Skills** (0-2 คะแนน)
- ตัวเลือก 3-4 จับคู่กับ **Hooks** (0-2 คะแนน)

---

**Round 3 — MCP & Subagents** (header: "Integration")

"Which of these have you done? Select all that apply."
ตัวเลือก:
1. "Connected an MCP server and used its tools" — e.g., GitHub MCP for PRs/issues, database MCP for queries, or any external data source
2. "Used advanced MCP features" — Project-scope .mcp.json, OAuth authentication, MCP resources with @mentions, Tool Search, or `claude mcp serve`
3. "Created or configured custom subagents" — Defined agents in .claude/agents/ with custom tools, model, or permissions
4. "Used advanced subagent features" — Worktree isolation, persistent agent memory, background tasks with Ctrl+B, agent allowlists with `Task(agent_name)`, or agent teams

**การคิดคะแนนสำหรับ Round 3:**
- ตัวเลือก 1-2 จับคู่กับ **MCP** (0-2 คะแนน)
- ตัวเลือก 3-4 จับคู่กับ **Subagents** (0-2 คะแนน)

---

**Round 4 — Checkpoints & Advanced Features** (header: "Power User")

"Which of these have you done? Select all that apply."
ตัวเลือก:
1. "Used checkpoints for safe experimentation" — Created checkpoints, used Esc+Esc or /rewind, restored code and/or conversation, or used Summarize option
2. "Used planning mode or extended thinking" — Activated planning via /plan, Shift+Tab, or --permission-mode plan; toggled extended thinking with Alt+T/Option+T
3. "Configured permission modes" — Used acceptEdits, plan, dontAsk, or bypassPermissions mode via CLI flags, keyboard shortcuts, or settings
4. "Used remote/desktop/web features" — Used `claude remote-control`, `claude --remote`, `/teleport`, `/desktop`, or worktrees with `claude -w`

**การคิดคะแนนสำหรับ Round 4:**
- ตัวเลือก 1 จับคู่กับ **Checkpoints** (0-1 คะแนน)
- ตัวเลือก 2-4 จับคู่กับ **Advanced Features** (0-3 คะแนน จำกัดที่ 2)

---

**Round 5 — Plugins & CLI** (header: "Mastery")

"Which of these have you done? Select all that apply."
ตัวเลือก:
1. "Installed or created a plugin" — Used a bundled plugin from marketplace, or created a .claude-plugin/ directory with plugin.json manifest
2. "Used plugin advanced features" — Plugin hooks, plugin MCP servers, LSP configuration, plugin namespaced commands, or --plugin-dir flag for testing
3. "Used print mode in scripts or CI/CD" — Used `claude -p` with --output-format json, --max-turns, piped input, or integrated into GitHub Actions / CI pipelines
4. "Used advanced CLI features" — Session resumption (-c/-r), --agents flag, --json-schema for structured output, --fallback-model, --from-pr, or batch processing loops

**การคิดคะแนนสำหรับ Round 5:**
- ตัวเลือก 1-2 จับคู่กับ **Plugins** (0-2 คะแนน)
- ตัวเลือก 3-4 จับคู่กับ **CLI** (0-2 คะแนน)

---

### ขั้นตอน 3: คำนวณและนำเสนอผลลัพธ์

#### 3A: สำหรับ Quick Assessment

นับจำนวนการเลือกทั้งหมดและกำหนดระดับ จากนั้นนำเสนอ:

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

#### 3B: สำหรับ Deep Assessment

คำนวณคะแนนรายหัวข้อจากทั้ง 5 รอบ แต่ละหัวข้อได้ 0-2 คะแนน จากนั้นนำเสนอ:

```markdown
## Claude Code Skill Assessment Results

### Overall Level: [Level 1 / Level 2 / Level 3]

**Total Score: N/20 points**

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

**การคำนวณระดับโดยรวมสำหรับ Deep Assessment:**
- คะแนนรวม 0-6 = Level 1: Beginner
- คะแนนรวม 7-13 = Level 2: Intermediate
- คะแนนรวม 14-20 = Level 3: Advanced

---

### ขั้นตอน 4: สร้างเส้นทางการเรียนรู้เฉพาะบุคคล

จากผลการประเมิน ให้สร้างเส้นทางการเรียนรู้ที่เจาะจงต่อช่องว่างของผู้ใช้ อย่าเพียงแค่ทำซ้ำเส้นทางระดับแบบทั่วไป — ให้ปรับให้เหมาะสม

#### กฎสำหรับการสร้างเส้นทาง

1. **ข้ามหัวข้อที่เชี่ยวชาญแล้ว**: หากหัวข้อได้คะแนน 2/2 อย่ารวมไว้ในเส้นทาง
2. **จัดลำดับความสำคัญตามลำดับ dependency**: Slash Commands ก่อน Skills, Memory ก่อน Subagents ฯลฯ ลำดับ dependency คือ:
   - Slash Commands (ไม่มี deps) -> Skills (ขึ้นกับ Slash Commands)
   - Memory (ไม่มี deps) -> Subagents (ขึ้นกับ Memory)
   - CLI Basics (ไม่มี deps) -> CLI Mastery (ขึ้นกับทั้งหมด)
   - Checkpoints (ไม่มี deps)
   - Hooks (ขึ้นกับ Slash Commands)
   - MCP (ไม่มี deps) -> Plugins (ขึ้นกับ MCP, Skills, Hooks)
   - Advanced Features (ขึ้นกับทั้งหมดก่อนหน้า)
3. **สำหรับหัวข้อคะแนน 1/2**: แนะนำ "deep dive" — ลิงก์ไปยังหัวข้อขั้นสูงเฉพาะที่พวกเขายังขาด
4. **ประมาณเวลา**: รวมเฉพาะหัวข้อที่พวกเขาต้องเรียน/ทบทวน
5. **จัดกลุ่มเป็นเฟส**: จัดระเบียบหัวข้อที่เหลือเป็นเฟสเชิงตรรกะ เฟสละ 2-3 หัวข้อ

#### รูปแบบผลลัพธ์ของเส้นทาง

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

#### คำแนะนำเฉพาะหัวข้อ

ใช้คำแนะนำเฉพาะเหล่านี้เมื่อหัวข้อใดเป็นช่องว่าง:

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
- Focus on: 7-level hierarchy and priority order, .claude/rules/ directory with path-specific rules, `@import` syntax (max depth 5), Auto Memory MEMORY.md (200-line limit)
- Done when: You have modular rules for different directories and understand the full hierarchy

**Skills (score 0)**:
- Tutorial: [03-skills/](../../../03-skills/)
- Focus on: SKILL.md format, auto-invocation via description field, progressive disclosure (3 loading levels)
- Key exercise: Install the code-review skill and verify it auto-triggers
- Done when: A skill automatically activates based on conversation context

**Skills (score 1 — review)**:
- Focus on: `context: fork` with `agent` field for subagent execution, `disable-model-invocation` vs `user-invocable`, 2% context budget, bundled resources (scripts/, references/, assets/)
- Done when: You can create a skill that runs in a subagent with forked context

**Hooks (score 0)**:
- Tutorial: [06-hooks/](../../../06-hooks/)
- Focus on: Configuration structure (matcher + hooks array), PreToolUse/PostToolUse events, exit codes (0=success, 2=block), JSON input/output format
- Key exercise: Create a PreToolUse hook that validates Bash commands
- Done when: A hook blocks dangerous commands before execution

**Hooks (score 1 — review)**:
- Focus on: All 25 hook events (including PostToolUseFailure, StopFailure, TaskCreated, CwdChanged, FileChanged, PostCompact, Elicitation, ElicitationResult), 4 hook types (command, http, prompt, agent), component-scoped hooks in SKILL.md frontmatter, HTTP hooks with allowedEnvVars, `CLAUDE_ENV_FILE` for SessionStart/CwdChanged/FileChanged
- Done when: You can create a prompt-based Stop hook and a component-scoped hook in a skill

**MCP (score 0)**:
- Tutorial: [05-mcp/](../../../05-mcp/)
- Focus on: `claude mcp add` command, transport types (HTTP recommended), GitHub MCP setup, environment variable expansion
- Key exercise: Add GitHub MCP server and query PRs
- Done when: You can query live data from an external service via MCP

**MCP (score 1 — review)**:
- Focus on: Project-scope .mcp.json (requires team approval), OAuth 2.0 auth, MCP resources with `@server:resource` mentions, Tool Search (ENABLE_TOOL_SEARCH), `claude mcp serve`, output limits (10k/25k/50k)
- Done when: You have a project .mcp.json and understand Tool Search auto mode

**Subagents (score 0)**:
- Tutorial: [04-subagents/](../../../04-subagents/)
- Focus on: Agent file format (.claude/agents/*.md), built-in agents (general-purpose, Plan, Explore), tools/model/permissionMode config
- Key exercise: Create a code-reviewer subagent and test delegation
- Done when: Claude delegates code review to your custom agent

**Subagents (score 1 — review)**:
- Focus on: Worktree isolation (`isolation: worktree`), persistent agent memory (`memory` field with scopes), background agents (Ctrl+B/Ctrl+F), agent allowlists with `Task(agent_name)`, agent teams (`--teammate-mode`)
- Done when: You have a subagent with persistent memory running in worktree isolation

**Checkpoints (score 0)**:
- Tutorial: [08-checkpoints/](../../../08-checkpoints/)
- Focus on: Esc+Esc and /rewind access, 5 rewind options (restore code+conversation, restore conversation, restore code, summarize, cancel), limitations (bash filesystem ops not tracked)
- Key exercise: Make experimental changes, then rewind to restore
- Done when: You can confidently experiment knowing you can rewind

**Advanced Features (score 0)**:
- Tutorial: [09-advanced-features/](../../../09-advanced-features/)
- Focus on: Planning mode (/plan or Shift+Tab), permission modes (5 types), extended thinking (Alt+T toggle)
- Key exercise: Use planning mode to design a feature, then implement it
- Done when: You can switch between planning and implementation modes fluently

**Advanced Features (score 1 — review)**:
- Focus on: Remote control (`claude remote-control`), web sessions (`claude --remote`), desktop handoff (`/desktop`), worktrees (`claude -w`), task lists (Ctrl+T), managed settings for enterprise
- Done when: You can hand off sessions between CLI, web, and desktop

**Plugins (score 0)**:
- Tutorial: [07-plugins/](../../../07-plugins/)
- Focus on: Plugin structure (.claude-plugin/plugin.json), what plugins bundle (commands, agents, MCP, hooks, settings), installation from marketplace
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

### ขั้นตอน 5: เสนอการดำเนินการต่อ

หลังจากนำเสนอผลลัพธ์ ให้ถามผู้ใช้ว่าต้องการทำอะไรต่อไป:

ใช้ AskUserQuestion พร้อมตัวเลือกเหล่านี้:
- **Start learning** — "Help me begin the first topic in my learning path right now"
- **Deep dive on a gap** — "Explain one of my gap areas in detail so I can learn it here"
- **Practice project** — "Set up a practice project that covers my gap areas"
- **Retake assessment** — "I want to retake the quiz (maybe the other mode)"

หากเลือก **Start learning**: อ่าน README.md ของบทเรียนช่องว่างแรกและพาผู้ใช้ทำแบบฝึกหัดแรก
หากเลือก **Deep dive on a gap**: ถามว่าหัวข้อช่องว่างใด จากนั้นอ่าน README.md ของบทเรียนที่เกี่ยวข้องและอธิบายแนวคิดสำคัญพร้อมตัวอย่าง
หากเลือก **Practice project**: ออกแบบโปรเจกต์เล็กๆ ที่รวม 2-3 หัวข้อช่องว่างของพวกเขาพร้อมขั้นตอนที่เป็นรูปธรรม
หากเลือก **Retake assessment**: กลับไปที่ขั้นตอน 1

## การจัดการข้อผิดพลาด

### ผู้ใช้ไม่เลือกรายการใดในรอบหนึ่ง
ถือเป็น 0 คะแนนสำหรับหัวข้อของรอบนั้น ดำเนินการต่อไปยังรอบถัดไป

### ผู้ใช้ไม่เลือกรายการใดในทุกรอบ
กำหนดเป็น Level 1: Beginner สนับสนุนให้เริ่มต้นจากต้น แสดงเส้นทาง Level 1 แบบเต็ม

### ผู้ใช้ต้องการทำแบบประเมินใหม่
รันใหม่จากขั้นตอน 1 ด้วยการประเมินใหม่

### ผู้ใช้ไม่เห็นด้วยกับระดับของตน
รับทราบความต้องการของพวกเขา ถามว่าพวกเขาระบุตัวเองที่ระดับใด นำเสนอเส้นทางสำหรับระดับที่พวกเขาเลือกพร้อมการตรวจสอบข้อกำหนดเบื้องต้นสำหรับหัวข้อที่พวกเขาอาจพลาดไป

### ผู้ใช้ถามเกี่ยวกับหัวข้อเฉพาะ
หากผู้ใช้พูดบางอย่างเช่น "tell me about hooks" หรือ "I want to learn MCP" ระหว่างการประเมิน ให้จดบันทึกไว้ หลังจากนำเสนอผลลัพธ์ ให้เน้นหัวข้อนั้นในเส้นทางการเรียนรู้ของพวกเขาโดยไม่คำนึงถึงคะแนน

## การตรวจสอบความถูกต้อง

### ชุดทดสอบการ trigger

**ควร trigger:**
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

**ไม่ควร trigger:**
- "review my code"
- "create a skill"
- "help me with MCP"
- "explain slash commands"
- "what is a checkpoint"
