<!-- i18n-source: .claude/skills/lesson-quiz/references/question-bank.md -->
<!-- i18n-date: 2026-07-16 -->
# Lesson Quiz — Question Bank

คำถาม 10 ข้อต่อบทเรียน แต่ละคำถามมี: category, ข้อความคำถาม, ตัวเลือก (3-4 ตัว), คำตอบที่ถูกต้อง, คำอธิบาย และหัวข้อที่ควรทบทวน

---

## Lesson 01: Slash Commands

### Q1
- **Category**: conceptual
- **Question**: slash command ใน Claude Code มีสี่ประเภทอะไรบ้าง?
- **Options**: A) Built-in, skills, plugin commands, MCP prompts | B) Built-in, custom, hook commands, API prompts | C) System, user, plugin, terminal commands | D) Core, extension, macro, script commands
- **Correct**: A
- **Explanation**: Claude Code มี built-in commands (เช่น /help, /compact), skills (ไฟล์ SKILL.md), plugin commands (namespaced plugin-name:command) และ MCP prompts (/mcp__server__prompt)
- **Review**: หัวข้อ Types of Slash Commands

### Q2
- **Category**: practical
- **Question**: คุณส่งอาร์กิวเมนต์ทั้งหมดที่ผู้ใช้ระบุไปยัง skill ได้อย่างไร?
- **Options**: A) Use `${args}` | B) Use `$ARGUMENTS` | C) Use `$@` | D) Use `$INPUT`
- **Correct**: B
- **Explanation**: `$ARGUMENTS` จับข้อความทั้งหมดหลังชื่อคำสั่ง สำหรับอาร์กิวเมนต์ตามตำแหน่ง ใช้ `$0`, `$1` เป็นต้น
- **Review**: หัวข้อ Argument handling

### Q3
- **Category**: conceptual
- **Question**: เมื่อ skill (.claude/skills/name/SKILL.md) และ legacy command (.claude/commands/name.md) มีชื่อเดียวกัน อันไหนมีลำดับความสำคัญสูงกว่า?
- **Options**: A) The legacy command | B) The skill | C) Whichever was created first | D) Claude asks the user to choose
- **Correct**: B
- **Explanation**: skill มีลำดับความสำคัญเหนือ legacy command ที่ชื่อเดียวกัน ระบบ skill แทนที่ระบบ command แบบเก่า
- **Review**: หัวข้อ Skill precedence

### Q4
- **Category**: practical
- **Question**: คุณฉีดผลลัพธ์ shell แบบสดเข้าไปใน prompt ของ skill ได้อย่างไร?
- **Options**: A) Use `$(command)` syntax | B) Use `!`command`` (backtick with !) syntax | C) Use `@shell:command` syntax | D) Use `{command}` syntax
- **Correct**: B
- **Explanation**: ไวยากรณ์ `!`command`` รันคำสั่ง shell และฉีดผลลัพธ์เข้าไปใน prompt ของ skill ก่อนที่ Claude จะเห็น
- **Review**: หัวข้อ Dynamic context injection

### Q5
- **Category**: conceptual
- **Question**: `disable-model-invocation: true` ใน frontmatter ของ skill ทำอะไร?
- **Options**: A) Prevents the skill from running entirely | B) Allows only the user to invoke it (Claude cannot auto-invoke) | C) Hides it from the /help menu | D) Disables the skill's AI processing
- **Correct**: B
- **Explanation**: `disable-model-invocation: true` หมายความว่ามีเพียงผู้ใช้เท่านั้นที่เรียกใช้คำสั่งผ่าน `/command-name` ได้ Claude จะไม่เรียกใช้เองโดยอัตโนมัติ มีประโยชน์สำหรับ skill ที่มีผลข้างเคียงเช่นการ deploy
- **Review**: หัวข้อ Controlling invocation

### Q6
- **Category**: practical
- **Question**: คุณต้องการสร้าง skill ที่มีเพียง Claude เท่านั้นที่เรียกใช้อัตโนมัติได้ (ซ่อนจากเมนู / ของผู้ใช้) คุณต้องตั้งค่า frontmatter field ใด?
- **Options**: A) `disable-model-invocation: true` | B) `user-invocable: false` | C) `hidden: true` | D) `auto-only: true`
- **Correct**: B
- **Explanation**: `user-invocable: false` ซ่อน skill จากเมนู slash ของผู้ใช้แต่ให้ Claude เรียกใช้อัตโนมัติตามบริบทได้
- **Review**: Invocation control matrix

### Q7
- **Category**: practical
- **Question**: โครงสร้าง directory ที่ถูกต้องสำหรับ custom skill ใหม่ชื่อ "deploy" คืออะไร?
- **Options**: A) `.claude/commands/deploy.md` | B) `.claude/skills/deploy/SKILL.md` | C) `.claude/skills/deploy.md` | D) `.claude/deploy/SKILL.md`
- **Correct**: B
- **Explanation**: skill อยู่ใน directory ภายใต้ `.claude/skills/` โดยมีไฟล์ `SKILL.md` อยู่ข้างใน ชื่อ directory ตรงกับชื่อคำสั่ง
- **Review**: หัวข้อ Skill types and locations

### Q8
- **Category**: conceptual
- **Question**: plugin command หลีกเลี่ยงการชนกันของชื่อกับ user command ได้อย่างไร?
- **Options**: A) They use a `plugin-name:command-name` namespace | B) They have a special .plugin extension | C) They are prefixed with `p/` | D) They override user commands automatically
- **Correct**: A
- **Explanation**: plugin command ใช้ namespace เช่น `pr-review:check-security` เพื่อหลีกเลี่ยงการชนกับ user command แบบเดี่ยว
- **Review**: หัวข้อ Plugin commands

### Q9
- **Category**: practical
- **Question**: คุณต้องการจำกัดว่า skill ใช้เครื่องมือใดได้บ้าง คุณต้องเพิ่ม frontmatter field ใด?
- **Options**: A) `tools: [Read, Grep]` | B) `allowed-tools: [Read, Grep]` | C) `permissions: [Read, Grep]` | D) `restrict-tools: [Read, Grep]`
- **Correct**: B
- **Explanation**: field `allowed-tools` ใน frontmatter ของ SKILL.md กำหนดขอบเขตว่าคำสั่งเรียกใช้เครื่องมือใดได้บ้าง
- **Review**: Frontmatter fields reference

### Q10
- **Category**: conceptual
- **Question**: ไวยากรณ์ `@file` ใช้ทำอะไรใน skill?
- **Options**: A) Importing another skill | B) Referencing a file to include its content in the prompt | C) Creating a symlink | D) Setting file permissions
- **Correct**: B
- **Explanation**: ไวยากรณ์ `@path/to/file` ใน skill รวมเนื้อหาของไฟล์ที่อ้างอิงเข้าไปใน prompt ทำให้ skill ดึง template หรือไฟล์ context เข้ามาได้
- **Review**: หัวข้อ File references

---

## Lesson 02: Memory

### Q1
- **Category**: conceptual
- **Question**: memory hierarchy ของ Claude Code มีกี่ระดับ และระดับใดมีลำดับความสำคัญสูงสุด?
- **Options**: A) 5 levels, User Memory is highest | B) 7 levels, Managed Policy is highest | C) 3 levels, Project Memory is highest | D) 7 levels, Auto Memory is highest
- **Correct**: B
- **Explanation**: hierarchy มี 7 ระดับ: Managed Policy > Project Memory > Project Rules > User Memory > User Rules > Local Project Memory > Auto Memory โดย Managed Policy (ตั้งค่าโดย admin) มีลำดับความสำคัญสูงสุด
- **Review**: หัวข้อ Memory hierarchy

### Q2
- **Category**: practical
- **Question**: คุณเพิ่มกฎใหม่เข้า memory ระหว่างการสนทนาได้อย่างรวดเร็วอย่างไร?
- **Options**: A) Use the `/memory` slash command or ask conversationally | B) Prefix your message with `#` (e.g., `# always use TypeScript`) | C) Type `/rule "rule text"` | D) Use `@add-memory "rule text"`
- **Correct**: A
- **Explanation**: วิธีที่แนะนำในการเพิ่ม memory คือคำสั่ง `/memory` (เปิดไฟล์ memory ใน editor ของคุณ) หรือการขอ Claude แบบสนทนา (เช่น "remember that we always use TypeScript strict mode") คำนำหน้า `#` ถูกยกเลิกแล้วและไม่ทำงานอีกต่อไป
- **Review**: หัวข้อ Quick memory updates ใน README

### Q3
- **Category**: conceptual
- **Question**: ความลึกสูงสุดสำหรับการ import `@path/to/file` ใน CLAUDE.md คือเท่าใด?
- **Options**: A) 3 levels deep | B) 5 levels deep | C) 10 levels deep | D) Unlimited
- **Correct**: B
- **Explanation**: ไวยากรณ์ `@import` รองรับการ import แบบ recursive ได้สูงสุดที่ความลึก 5 ระดับเพื่อป้องกัน infinite loop
- **Review**: หัวข้อ Import syntax

### Q4
- **Category**: practical
- **Question**: คุณจำกัดขอบเขตไฟล์กฎให้ใช้กับเฉพาะไฟล์ใน `src/api/` ได้อย่างไร?
- **Options**: A) Put the rule in `src/api/CLAUDE.md` | B) Add `paths: src/api/**` YAML frontmatter to a `.claude/rules/*.md` file | C) Name the file `.claude/rules/api.md` | D) Use `@scope: src/api` in the rule file
- **Correct**: B
- **Explanation**: ไฟล์ใน `.claude/rules/` รองรับ frontmatter field `paths:` พร้อม glob pattern เพื่อจำกัดขอบเขตกฎให้กับ directory เฉพาะ
- **Review**: หัวข้อ Path-specific rules

### Q5
- **Category**: conceptual
- **Question**: MEMORY.md ของ Auto Memory ถูกโหลดกี่บรรทัดตอนเริ่ม session?
- **Options**: A) All lines | B) First 100 lines | C) First 200 lines | D) First 500 lines
- **Correct**: C
- **Explanation**: 200 บรรทัดแรกของ MEMORY.md ถูกโหลดเข้า context อัตโนมัติตอนเริ่ม session ไฟล์หัวข้อที่อ้างอิงจาก MEMORY.md จะถูกโหลดตามความต้องการ
- **Review**: หัวข้อ Auto Memory

### Q6
- **Category**: practical
- **Question**: คุณต้องการค่ากำหนดโปรเจกต์ส่วนตัวที่ **ไม่** commit เข้า git คุณควรใช้ไฟล์ใด?
- **Options**: A) `~/.claude/CLAUDE.md` | B) `CLAUDE.local.md` | C) `.claude/rules/personal.md` | D) `.claude/memory/personal.md`
- **Correct**: B
- **Explanation**: `CLAUDE.local.md` ใน root ของโปรเจกต์ใช้สำหรับค่ากำหนดเฉพาะโปรเจกต์ส่วนตัว ควรถูก git-ignore
- **Review**: Memory locations comparison

### Q7
- **Category**: conceptual
- **Question**: คำสั่ง `/init` ทำอะไร?
- **Options**: A) Initializes a new Claude Code project from scratch | B) Generates a template CLAUDE.md based on your project structure | C) Resets all memory to defaults | D) Creates a new session
- **Correct**: B
- **Explanation**: `/init` วิเคราะห์โปรเจกต์ของคุณและสร้าง template CLAUDE.md พร้อมกฎและมาตรฐานที่แนะนำ เป็นเครื่องมือ bootstrap แบบครั้งเดียว
- **Review**: หัวข้อคำสั่ง /init

### Q8
- **Category**: practical
- **Question**: คุณปิดใช้งาน Auto Memory ทั้งหมดได้อย่างไร?
- **Options**: A) Delete the ~/.claude/projects directory | B) Set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` | C) Add `auto-memory: false` to CLAUDE.md | D) Use `/memory disable auto`
- **Correct**: B
- **Explanation**: การตั้งค่า `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` ปิดใช้งาน auto memory ค่า `0` บังคับเปิด หากไม่ตั้งค่า = เปิดโดยค่าเริ่มต้น
- **Review**: หัวข้อ Auto Memory configuration

### Q9
- **Category**: conceptual
- **Question**: memory tier ที่มีลำดับความสำคัญต่ำกว่าสามารถ override กฎจาก tier ที่มีลำดับความสำคัญสูงกว่าได้หรือไม่?
- **Options**: A) Yes, the most recent rule always wins | B) No, higher tiers always take precedence | C) Yes, if the lower tier uses the `!important` flag | D) It depends on the rule type
- **Correct**: B
- **Explanation**: ลำดับความสำคัญของ memory ไหลลงจาก Managed Policy tier ที่ต่ำกว่า (เช่น Auto Memory) ไม่สามารถ override tier ที่สูงกว่า (เช่น Project Memory) ได้
- **Review**: หัวข้อ Memory hierarchy

### Q10
- **Category**: practical
- **Question**: คุณทำงานข้ามสอง repository และต้องการให้ Claude โหลด CLAUDE.md จากทั้งสอง คุณใช้ flag ใด?
- **Options**: A) `--multi-repo` | B) `--add-dir /path/to/other` | C) `--include /path/to/other` | D) `--merge-context /path/to/other`
- **Correct**: B
- **Explanation**: flag `--add-dir` โหลด CLAUDE.md จาก directory เพิ่มเติม ทำให้มี context แบบ multi-repo ได้
- **Review**: หัวข้อ Additional directories

---

## Lesson 03: Skills

### Q1
- **Category**: conceptual
- **Question**: progressive disclosure ในระบบ skill มี 3 ระดับอะไรบ้าง?
- **Options**: A) Metadata, instructions, resources | B) Name, body, attachments | C) Header, content, scripts | D) Summary, details, data
- **Correct**: A
- **Explanation**: Level 1: Metadata (~100 tokens โหลดเสมอ), Level 2: เนื้อหา SKILL.md (<5k tokens โหลดเมื่อ trigger), Level 3: ทรัพยากรที่รวมมา (scripts/references/assets โหลดตามความต้องการ)
- **Review**: หัวข้อ Progressive disclosure architecture

### Q2
- **Category**: practical
- **Question**: ปัจจัยที่สำคัญที่สุดในการทำให้ skill ถูกเรียกใช้อัตโนมัติโดย Claude คืออะไร?
- **Options**: A) The skill's file name | B) The `description` field in frontmatter with when-to-use keywords | C) The skill's directory location | D) The `auto-invoke: true` frontmatter field
- **Correct**: B
- **Explanation**: Claude ตัดสินใจว่าจะเรียกใช้ skill อัตโนมัติหรือไม่โดยอิงจาก field `description` เพียงอย่างเดียว จึงต้องมีวลี trigger และสถานการณ์ที่เฉพาะเจาะจง
- **Review**: หัวข้อ Auto-invocation

### Q3
- **Category**: conceptual
- **Question**: ความยาวสูงสุดที่แนะนำสำหรับไฟล์ SKILL.md คือเท่าใด?
- **Options**: A) 100 lines | B) 250 lines | C) 500 lines | D) 1000 lines
- **Correct**: C
- **Explanation**: ควรเก็บ SKILL.md ให้ไม่เกิน 500 บรรทัด เอกสารอ้างอิงที่ใหญ่กว่าควรอยู่ในไฟล์ subdirectory `references/`
- **Review**: หัวข้อ Content guidelines

### Q4
- **Category**: practical
- **Question**: คุณทำให้ skill รันใน subagent ที่แยกออกมาพร้อม context ของตัวเองได้อย่างไร?
- **Options**: A) Set `isolation: true` in frontmatter | B) Set `context: fork` with an `agent` field in frontmatter | C) Set `subagent: true` in frontmatter | D) Put the skill in `.claude/agents/`
- **Correct**: B
- **Explanation**: `context: fork` รัน skill ใน context ที่แยกออกมา และ field `agent` ระบุประเภท agent ที่จะใช้ (เช่น `Explore`, `Plan`, custom agent)
- **Review**: หัวข้อ Running skills in subagents

### Q5
- **Category**: conceptual
- **Question**: งบประมาณ context โดยประมาณที่จัดสรรให้ skill metadata (Level 1) คือเท่าใด?
- **Options**: A) 0.5% of context window | B) 1% of context window | C) 5% of context window | D) 10% of context window
- **Correct**: B
- **Explanation**: skill metadata ใช้ประมาณ 1% ของ context window (ค่าสำรอง: 8,000 อักขระ) ปรับได้ด้วย `SLASH_COMMAND_TOOL_CHAR_BUDGET`
- **Review**: หัวข้อ Context budget

### Q6
- **Category**: practical
- **Question**: skill ต้องอ้างอิงข้อกำหนด API ขนาดใหญ่ คุณควรวางไว้ที่ไหน?
- **Options**: A) Inline in SKILL.md | B) In a `references/api-spec.md` file inside the skill directory | C) In the project's CLAUDE.md | D) In a separate `.claude/rules/` file
- **Correct**: B
- **Explanation**: เอกสารอ้างอิงขนาดใหญ่ควรอยู่ใน subdirectory `references/` Claude โหลดทรัพยากร Level 3 ตามความต้องการ ทำให้ SKILL.md กระชับ
- **Review**: หัวข้อ Supporting files structure

### Q7
- **Category**: conceptual
- **Question**: ความแตกต่างระหว่าง Reference Content และ Task Content ใน skill คืออะไร?
- **Options**: A) Reference is read-only, Task is read-write | B) Reference adds knowledge to context, Task provides step-by-step instructions | C) Reference is for documentation, Task is for code | D) There is no difference
- **Correct**: B
- **Explanation**: Reference Content เพิ่มความรู้เฉพาะด้านเข้าไปใน context ของ Claude (เช่น brand guidelines) Task Content ให้คำแนะนำแบบทีละขั้นที่ปฏิบัติได้สำหรับ workflow
- **Review**: หัวข้อ Skill content types

### Q8
- **Category**: practical
- **Question**: อักขระใดที่อนุญาตใน field `name` ของ frontmatter ของ skill?
- **Options**: A) Any characters | B) Lowercase letters, numbers, and hyphens only (max 64 chars) | C) Letters and underscores | D) Alphanumeric only
- **Correct**: B
- **Explanation**: ชื่อต้องเป็น kebab-case (ตัวพิมพ์เล็ก, ขีดกลาง) สูงสุด 64 อักขระ และห้ามมีคำว่า "anthropic" หรือ "claude"
- **Review**: หัวข้อ SKILL.md format

### Q9
- **Category**: conceptual
- **Question**: Claude ค้นหา skill ตามลำดับใด?
- **Options**: A) User > Project > Enterprise | B) Enterprise > Personal > Project (plugin uses namespace) | C) Project > User > Enterprise | D) Alphabetical order
- **Correct**: B
- **Explanation**: ลำดับความสำคัญคือ: Enterprise > Personal > Project ส่วน plugin skill ใช้ namespace (plugin-name:skill) จึงไม่ขัดแย้งกัน
- **Review**: หัวข้อ Skill types and locations

### Q10
- **Category**: practical
- **Question**: คุณป้องกันไม่ให้ Claude เรียกใช้ skill อัตโนมัติในขณะที่ยังให้ผู้ใช้ใช้งานด้วยตนเองได้อย่างไร?
- **Options**: A) Set `user-invocable: false` | B) Set `disable-model-invocation: true` | C) Remove the description field | D) Set `auto-invoke: false`
- **Correct**: B
- **Explanation**: `disable-model-invocation: true` ป้องกันไม่ให้ Claude เรียกใช้อัตโนมัติแต่ยังคง skill ไว้ในเมนู `/` ของผู้ใช้สำหรับการใช้งานด้วยตนเอง
- **Review**: หัวข้อ Controlling invocation

---

## Lesson 04: Subagents

### Q1
- **Category**: conceptual
- **Question**: ข้อได้เปรียบหลักของ subagents เหนือการสนทนาแบบ inline คืออะไร?
- **Options**: A) They are faster | B) They operate in a separate, clean context window preventing context pollution | C) They can use more tools | D) They have better error handling
- **Correct**: B
- **Explanation**: subagents ได้ context window ใหม่ โดยรับเฉพาะสิ่งที่ agent หลักส่งให้ ป้องกันไม่ให้การสนทนาหลักถูกปนเปื้อนด้วยรายละเอียดเฉพาะงาน
- **Review**: หัวข้อ Overview

### Q2
- **Category**: practical
- **Question**: ลำดับความสำคัญสำหรับการนิยาม agent คืออะไร?
- **Options**: A) Project > User > CLI | B) CLI > Project > User | C) User > Project > CLI | D) They all have equal priority
- **Correct**: B
- **Explanation**: agent ที่นิยามผ่าน CLI (flag `--agents`) override ระดับ Project (`.claude/agents/`) ซึ่ง override ระดับ User (`~/.claude/agents/`)
- **Review**: หัวข้อ File locations

### Q3
- **Category**: conceptual
- **Question**: built-in subagent ตัวใดใช้ model Haiku และถูกปรับให้เหมาะกับการสำรวจ codebase แบบอ่านอย่างเดียว?
- **Options**: A) general-purpose | B) Plan | C) Explore | D) Bash
- **Correct**: C
- **Explanation**: subagent Explore ใช้ Haiku สำหรับการสำรวจ codebase แบบอ่านอย่างเดียวที่รวดเร็ว รองรับระดับความละเอียดสามระดับ: quick, medium, very thorough
- **Review**: หัวข้อ Built-in subagents

### Q4
- **Category**: practical
- **Question**: คุณจำกัด subagent ที่ coordinator agent สามารถสร้างได้อย่างไร?
- **Options**: A) Use `allowed-agents:` field | B) Use `Task(agent_name)` syntax in the `tools` field | C) Set `spawn-limit: 2` | D) Use `restrict-agents: [name1, name2]`
- **Correct**: B
- **Explanation**: การเพิ่ม `Task(worker, researcher)` ใน field tools สร้าง allowlist — agent สร้างได้เฉพาะ subagent ชื่อ "worker" หรือ "researcher" เท่านั้น
- **Review**: หัวข้อ Restrict spawnable subagents

### Q5
- **Category**: conceptual
- **Question**: `isolation: worktree` ทำอะไรให้กับ subagent?
- **Options**: A) Runs the agent in a Docker container | B) Gives the agent its own git worktree so changes don't affect the main tree | C) Prevents the agent from reading any files | D) Runs the agent in a sandbox
- **Correct**: B
- **Explanation**: worktree isolation สร้าง git worktree ที่แยกออกมา หาก agent ไม่ทำการเปลี่ยนแปลง จะทำความสะอาดตัวเองอัตโนมัติ หากมีการเปลี่ยนแปลง จะคืน path ของ worktree และ branch
- **Review**: หัวข้อ Worktree isolation

### Q6
- **Category**: practical
- **Question**: คุณทำให้ subagent รันในเบื้องหลังได้อย่างไร?
- **Options**: A) Set `background: true` in the agent config | B) Use `async: true` in the agent config | C) Press Ctrl+D after starting it | D) Use `--background` CLI flag
- **Correct**: A
- **Explanation**: `background: true` ใน agent configuration ทำให้ subagent รันเป็นงานเบื้องหลังเสมอ ผู้ใช้ยังใช้ Ctrl+B เพื่อส่งงานเบื้องหน้าไปเบื้องหลังได้ด้วย
- **Review**: หัวข้อ Background subagents

### Q7
- **Category**: conceptual
- **Question**: field `memory` ที่มี scope `project` ทำอะไรให้กับ subagent?
- **Options**: A) Gives read access to the project CLAUDE.md | B) Creates a persistent memory directory scoped to the current project | C) Shares the main agent's conversation history | D) Loads the project's git history
- **Correct**: B
- **Explanation**: field `memory` สร้าง directory แบบถาวรสำหรับ subagent scope `project` หมายความว่า memory ผูกกับโปรเจกต์ปัจจุบัน 200 บรรทัดแรกของ MEMORY.md ของ agent จะโหลดอัตโนมัติ
- **Review**: หัวข้อ Persistent memory

### Q8
- **Category**: practical
- **Question**: คุณใส่วลีในคำอธิบายของ subagent เพื่อกระตุ้นให้ Claude มอบหมายงานให้อัตโนมัติได้อย่างไร?
- **Options**: A) Add "priority: high" | B) Include "use PROACTIVELY" or "MUST BE USED" in the description | C) Set `auto-delegate: true` | D) Add "trigger: always"
- **Correct**: B
- **Explanation**: การใส่วลีเช่น "use PROACTIVELY" หรือ "MUST BE USED" ในคำอธิบายกระตุ้นให้ Claude มอบหมายงานที่ตรงกันอัตโนมัติอย่างมาก
- **Review**: หัวข้อ Automatic delegation

### Q9
- **Category**: conceptual
- **Question**: ค่า `permissionMode` ที่ถูกต้องสำหรับ subagent มีอะไรบ้าง?
- **Options**: A) read, write, admin | B) default, acceptEdits, bypassPermissions, plan, dontAsk, auto | C) safe, normal, dangerous | D) restricted, standard, elevated
- **Correct**: B
- **Explanation**: subagents รองรับ permission mode หกแบบ: default (ถามทุกอย่าง), acceptEdits (ยอมรับการแก้ไขไฟล์อัตโนมัติ), bypassPermissions (ข้ามทั้งหมด), plan (อ่านอย่างเดียว), dontAsk (ปฏิเสธอัตโนมัติเว้นแต่ได้รับอนุมัติล่วงหน้า), auto (classifier เบื้องหลังตัดสินใจ)
- **Review**: หัวข้อ Configuration fields

### Q10
- **Category**: practical
- **Question**: คุณ resume subagent ที่คืน agentId จากการรันก่อนหน้าได้อย่างไร?
- **Options**: A) Use `/resume agent-id` | B) Pass the `resume` parameter with the agentId when calling Task tool | C) Use `claude -r agent-id` | D) Subagents cannot be resumed
- **Correct**: B
- **Explanation**: subagents สามารถ resume ได้โดยส่ง parameter `resume` พร้อม agentId ที่คืนมาก่อนหน้า เพื่อดำเนินการต่อโดยรักษา context ทั้งหมดไว้
- **Review**: หัวข้อ Resumable agents

---

## Lesson 05: MCP

### Q1
- **Category**: conceptual
- **Question**: MCP transport protocol สามแบบมีอะไรบ้าง และแบบใดที่แนะนำ?
- **Options**: A) HTTP (recommended), Stdio, SSE (deprecated) | B) WebSocket (recommended), REST, gRPC | C) TCP, UDP, HTTP | D) Stdio (recommended), HTTP, SSE
- **Correct**: A
- **Explanation**: HTTP แนะนำสำหรับ server ระยะไกล Stdio สำหรับ process ในเครื่อง (พบมากที่สุดในปัจจุบัน) SSE เลิกใช้แล้วแต่ยังรองรับอยู่
- **Review**: หัวข้อ Transport protocols

### Q2
- **Category**: practical
- **Question**: คุณเพิ่ม GitHub MCP server ผ่าน CLI ได้อย่างไร?
- **Options**: A) `claude mcp install github` | B) `claude mcp add --transport http github https://api.github.com/mcp` | C) `claude plugin add github-mcp` | D) `claude connect github`
- **Correct**: B
- **Explanation**: ใช้ `claude mcp add` พร้อม flag `--transport`, ชื่อ และ URL ของ server สำหรับ stdio: `claude mcp add github -- npx -y @modelcontextprotocol/server-github`
- **Review**: หัวข้อ MCP configuration management

### Q3
- **Category**: conceptual
- **Question**: เกิดอะไรขึ้นเมื่อคำอธิบายเครื่องมือ MCP เกิน 10% ของ context window?
- **Options**: A) They are truncated | B) Tool Search auto-enables to dynamically select relevant tools | C) Claude shows an error | D) Extra tools are disabled
- **Correct**: B
- **Explanation**: MCP Tool Search เปิดใช้งานอัตโนมัติเมื่อเครื่องมือเกิน 10% ของ context ต้องใช้ Sonnet 4 หรือ Opus 4 เป็นอย่างต่ำ (ไม่รองรับ Haiku)
- **Review**: หัวข้อ MCP Tool Search

### Q4
- **Category**: practical
- **Question**: คุณใช้ค่าสำรองของ environment variable ใน MCP config ได้อย่างไร?
- **Options**: A) `${VAR || "default"}` | B) `${VAR:-default}` | C) `${VAR:default}` | D) `${VAR ? "default"}`
- **Correct**: B
- **Explanation**: `${VAR:-default}` ให้ค่าสำรองหาก environment variable ไม่ได้ถูกตั้งค่า ส่วน `${VAR}` โดยไม่มีค่าสำรองจะ error หากไม่ได้ตั้งค่า
- **Review**: หัวข้อ Environment variable expansion

### Q5
- **Category**: conceptual
- **Question**: ความแตกต่างระหว่าง MCP และ Memory สำหรับการเข้าถึงข้อมูลคืออะไร?
- **Options**: A) MCP is faster, Memory is slower | B) MCP is for live/changing external data, Memory is for persistent/static preferences | C) MCP is for code, Memory is for text | D) They are interchangeable
- **Correct**: B
- **Explanation**: MCP เชื่อมต่อกับแหล่งข้อมูลภายนอกที่มีชีวิตและเปลี่ยนแปลง (API, database) ส่วน Memory เก็บ context และค่ากำหนดโปรเจกต์แบบถาวรและคงที่
- **Review**: หัวข้อ MCP vs Memory

### Q6
- **Category**: practical
- **Question**: เกิดอะไรขึ้นเมื่อสมาชิกทีมพบ `.mcp.json` แบบ project-scoped เป็นครั้งแรก?
- **Options**: A) It loads automatically | B) They get an approval prompt to trust the project's MCP servers | C) It's ignored unless they opt in via settings | D) Claude asks the admin to approve
- **Correct**: B
- **Explanation**: `.mcp.json` แบบ project-scoped กระตุ้น prompt อนุมัติด้านความปลอดภัยในการใช้งานครั้งแรกของสมาชิกทีมแต่ละคน นี่เป็นสิ่งที่ตั้งใจ — ป้องกัน MCP server ที่ไม่น่าเชื่อถือ
- **Review**: หัวข้อ MCP Scopes

### Q7
- **Category**: conceptual
- **Question**: `claude mcp serve` ทำอะไร?
- **Options**: A) Starts an MCP server dashboard | B) Makes Claude Code itself act as an MCP server for other applications | C) Serves MCP documentation | D) Tests MCP server connections
- **Correct**: B
- **Explanation**: `claude mcp serve` ทำให้ Claude Code กลายเป็น MCP server เปิดให้มีการประสานงานแบบ multi-agent ที่ Claude instance หนึ่งถูกควบคุมโดยอีก instance หนึ่งได้
- **Review**: หัวข้อ Claude as MCP Server

### Q8
- **Category**: practical
- **Question**: ขนาด output สูงสุดโดยค่าเริ่มต้นสำหรับเครื่องมือ MCP คือเท่าใด?
- **Options**: A) 5,000 tokens | B) 10,000 tokens | C) 25,000 tokens | D) 50,000 tokens
- **Correct**: C
- **Explanation**: ค่าสูงสุดโดยค่าเริ่มต้นคือ 25,000 tokens (`MAX_MCP_OUTPUT_TOKENS`) คำเตือนปรากฏที่ 10k tokens การเก็บลงดิสก์จำกัดที่ 50k อักขระ
- **Review**: หัวข้อ MCP Output Limits

### Q9
- **Category**: conceptual
- **Question**: เมื่อทั้ง `allowedMcpServers` และ `deniedMcpServers` ตรงกับ server ใน managed config อันไหนชนะ?
- **Options**: A) Allowed wins | B) Denied wins | C) The last one configured wins | D) Both are applied independently
- **Correct**: B
- **Explanation**: ใน managed MCP configuration กฎ deny มีลำดับความสำคัญเหนือกฎ allow เสมอ
- **Review**: หัวข้อ Managed MCP Configuration

### Q10
- **Category**: practical
- **Question**: คุณอ้างอิงทรัพยากร MCP ในการสนทนาได้อย่างไร?
- **Options**: A) Use `/mcp resource-name` | B) Use `@server-name:protocol://resource/path` mention syntax | C) Use `mcp.get("resource")` | D) Resources are auto-loaded
- **Correct**: B
- **Explanation**: ทรัพยากร MCP ถูกเข้าถึงผ่านไวยากรณ์ mention `@server-name:protocol://resource/path` ในการสนทนา
- **Review**: หัวข้อ MCP Resources

---

## Lesson 06: Hooks

### Q1
- **Category**: conceptual
- **Question**: hook ใน Claude Code มีสี่ประเภทอะไรบ้าง?
- **Options**: A) Pre, Post, Error, and Filter hooks | B) Command, HTTP, Prompt, and Agent hooks | C) Before, After, Around, and Through hooks | D) Input, Output, Filter, and Transform hooks
- **Correct**: B
- **Explanation**: Command hooks รัน shell script, HTTP hooks เรียก webhook endpoint, Prompt hooks ใช้การประเมิน LLM แบบ single-turn และ Agent hooks ใช้การตรวจสอบผ่าน subagent
- **Review**: หัวข้อ Hook types

### Q2
- **Category**: practical
- **Question**: hook script ออกด้วย exit code 2 เกิดอะไรขึ้น?
- **Options**: A) Non-blocking warning shown | B) Blocking error — stderr is shown as an error to Claude, tool use is prevented | C) Hook is retried | D) Session ends
- **Correct**: B
- **Explanation**: exit code 0 = สำเร็จ/ดำเนินการต่อ, exit code 2 = blocking error (แสดง stderr เป็น error), non-zero อื่นๆ = non-blocking (stderr ใน verbose เท่านั้น)
- **Review**: หัวข้อ Exit codes

### Q3
- **Category**: conceptual
- **Question**: PreToolUse hook ได้รับ JSON field ใดบ้างทาง stdin?
- **Options**: A) `tool_name` and `tool_output` | B) `session_id`, `tool_name`, `tool_input`, `hook_event_name`, `cwd`, and more | C) Only `tool_name` | D) The full conversation history
- **Correct**: B
- **Explanation**: hook ได้รับ JSON object ทาง stdin ประกอบด้วย: session_id, transcript_path, hook_event_name, tool_name, tool_input, tool_use_id, cwd และ permission_mode
- **Review**: หัวข้อ JSON input structure

### Q4
- **Category**: practical
- **Question**: PreToolUse hook แก้ไข parameter อินพุตของเครื่องมือก่อนการทำงานได้อย่างไร?
- **Options**: A) Return modified JSON on stderr | B) Return JSON with `updatedInput` field on stdout (exit code 0) | C) Write to a temp file | D) Hooks cannot modify inputs
- **Correct**: B
- **Explanation**: PreToolUse hook สามารถ output JSON ที่มี `"updatedInput": {...}` ทาง stdout (พร้อม exit 0) เพื่อแก้ไข parameter ของเครื่องมือก่อนที่ Claude จะใช้
- **Review**: หัวข้อ PreToolUse output

### Q5
- **Category**: conceptual
- **Question**: hook event ใดรองรับ `CLAUDE_ENV_FILE` สำหรับการเก็บ environment variable เข้าไปใน session?
- **Options**: A) PreToolUse | B) UserPromptSubmit | C) SessionStart | D) All events
- **Correct**: C
- **Explanation**: มีเพียง SessionStart hook เท่านั้นที่ใช้ `CLAUDE_ENV_FILE` เพื่อเก็บ environment variable เข้าไปใน session ได้
- **Review**: หัวข้อ SessionStart

### Q6
- **Category**: practical
- **Question**: คุณต้องการ hook ที่รันเพียงครั้งเดียวเมื่อ skill ถูกโหลดครั้งแรก ไม่ใช่ทุกครั้งที่เรียกเครื่องมือ คุณต้องเพิ่ม field ใด?
- **Options**: A) `run-once: true` | B) `once: true` in the component hook definition | C) `single: true` | D) `max-runs: 1`
- **Correct**: B
- **Explanation**: hook แบบ component-scoped (นิยามใน SKILL.md หรือ frontmatter ของ agent) รองรับ `once: true` เพื่อรันเฉพาะตอน activation ครั้งแรก
- **Review**: หัวข้อ Component-scoped hooks

### Q7
- **Category**: conceptual
- **Question**: Stop hook ถูกนิยามไว้ใน frontmatter ของ subagent มันจะแปลงเป็นอะไรโดยอัตโนมัติ?
- **Options**: A) A PostToolUse hook | B) A SubagentStop hook | C) A SessionEnd hook | D) It stays as a Stop hook
- **Correct**: B
- **Explanation**: เมื่อ Stop hook ถูกวางไว้ใน frontmatter ของ subagent มันจะแปลงเป็น SubagentStop อัตโนมัติเพื่อให้รันเมื่อ subagent นั้นทำงานเสร็จ
- **Review**: หัวข้อ Component-scoped hooks

### Q8
- **Category**: practical
- **Question**: คุณจับคู่ hook กับเครื่องมือ MCP ทั้งหมดจาก server หนึ่งได้อย่างไร?
- **Options**: A) `matcher: "mcp_github"` | B) `matcher: "mcp__github__.*"` (regex pattern) | C) `matcher: "mcp:github:*"` | D) `matcher: "github-mcp"`
- **Correct**: B
- **Explanation**: ใช้ regex pattern สำหรับ matcher เครื่องมือ MCP เป็นไปตามรูปแบบการตั้งชื่อ `mcp__server__tool` ดังนั้น `mcp__github__.*` จึงตรงกับเครื่องมือ GitHub MCP ทั้งหมด
- **Review**: หัวข้อ Matcher patterns

### Q9
- **Category**: conceptual
- **Question**: Claude Code รองรับ hook event ทั้งหมดกี่ตัว?
- **Options**: A) 10 | B) 16 | C) 25 | D) 30
- **Correct**: C
- **Explanation**: Claude Code รองรับ hook event 25 ตัว: PreToolUse, PostToolUse, PostToolUseFailure, UserPromptSubmit, Stop, StopFailure, SubagentStop, SubagentStart, PermissionRequest, Notification, PreCompact, PostCompact, SessionStart, SessionEnd, WorktreeCreate, WorktreeRemove, ConfigChange, CwdChanged, FileChanged, TeammateIdle, TaskCompleted, TaskCreated, Elicitation, ElicitationResult, InstructionsLoaded
- **Review**: ตาราง Hook events

### Q10
- **Category**: practical
- **Question**: คุณต้องการ debug ว่าทำไม hook ไม่ทำงาน วิธีที่ดีที่สุดคืออะไร?
- **Options**: A) Add print statements to the hook script | B) Use `--debug` flag and `Ctrl+O` for verbose mode | C) Check the system log | D) Hooks don't have debugging tools
- **Correct**: B
- **Explanation**: flag `--debug` และโหมด verbose `Ctrl+O` แสดงรายละเอียดการทำงานของ hook รวมถึงว่า hook ใดทำงาน อินพุต และเอาต์พุต
- **Review**: หัวข้อ Debugging

---

## Lesson 07: Plugins

### Q1
- **Category**: conceptual
- **Question**: ไฟล์ manifest หลักของ plugin คืออะไร และอยู่ที่ไหน?
- **Options**: A) `plugin.yaml` in the root directory | B) `.claude-plugin/plugin.json` | C) `package.json` with a "claude" key | D) `.claude/plugin.md`
- **Correct**: B
- **Explanation**: manifest ของ plugin อยู่ที่ `.claude-plugin/plugin.json` พร้อม field ที่จำเป็น: name, description, version, author
- **Review**: หัวข้อ Plugin definition structure

### Q2
- **Category**: practical
- **Question**: คุณทดสอบ plugin ในเครื่องก่อนเผยแพร่ได้อย่างไร?
- **Options**: A) Use `/plugin test ./my-plugin` | B) Use `claude --plugin-dir ./my-plugin` | C) Use `claude plugin validate ./my-plugin` | D) Copy it to ~/.claude/plugins/
- **Correct**: B
- **Explanation**: flag `--plugin-dir` โหลด plugin จาก directory ในเครื่องเพื่อทดสอบ ใช้ซ้ำได้เพื่อโหลดหลาย plugin
- **Review**: หัวข้อ Testing

### Q3
- **Category**: conceptual
- **Question**: environment variable ใดที่มีอยู่ภายใน plugin hook และ MCP config เพื่ออ้างอิง directory ที่ติดตั้ง plugin?
- **Options**: A) `$PLUGIN_HOME` | B) `${CLAUDE_PLUGIN_ROOT}` | C) `$PLUGIN_DIR` | D) `${CLAUDE_PLUGIN_PATH}`
- **Correct**: B
- **Explanation**: `${CLAUDE_PLUGIN_ROOT}` แปลงเป็น directory ที่ติดตั้ง plugin ทำให้อ้างอิง path แบบพกพาได้ใน hook และ MCP config
- **Review**: หัวข้อ Plugin directory structure

### Q4
- **Category**: practical
- **Question**: plugin มีคำสั่งชื่อ "check-security" ใน plugin "pr-review" ผู้ใช้เรียกใช้ได้อย่างไร?
- **Options**: A) `/check-security` | B) `/pr-review:check-security` | C) `/plugin pr-review check-security` | D) `/pr-review/check-security`
- **Correct**: B
- **Explanation**: plugin command ใช้ namespace `plugin-name:command-name` เพื่อหลีกเลี่ยงการชนกับ user command และ plugin อื่น
- **Review**: หัวข้อ Plugin commands

### Q5
- **Category**: conceptual
- **Question**: plugin สามารถรวมส่วนประกอบใดได้บ้าง?
- **Options**: A) Only commands and settings | B) Commands, agents, skills, hooks, MCP servers, LSP config, settings, templates, scripts | C) Only commands, hooks, and MCP servers | D) Only skills and agents
- **Correct**: B
- **Explanation**: plugin สามารถรวม: commands/, agents/, skills/, hooks/hooks.json, .mcp.json, .lsp.json, settings.json, templates/, scripts/, docs/, tests/
- **Review**: หัวข้อ Plugin directory structure

### Q6
- **Category**: practical
- **Question**: คุณติดตั้ง plugin จาก GitHub ได้อย่างไร?
- **Options**: A) `claude plugin add github:username/repo` | B) `/plugin install github:username/repo` | C) `npm install @claude/username-repo` | D) `git clone` then `claude plugin register`
- **Correct**: B
- **Explanation**: ใช้ `/plugin install github:username/repo` เพื่อติดตั้งโดยตรงจาก GitHub repository
- **Review**: หัวข้อ Installation methods

### Q7
- **Category**: conceptual
- **Question**: key `agent` ใน `settings.json` ของ plugin ทำอะไร?
- **Options**: A) Specifies authentication credentials | B) Sets the main thread agent for the plugin | C) Lists available subagents | D) Configures agent permissions
- **Correct**: B
- **Explanation**: key `agent` ใน settings.json ของ plugin ระบุการนิยาม agent ที่จะใช้เป็น main thread agent เมื่อ plugin ทำงานอยู่
- **Review**: หัวข้อ Plugin Settings

### Q8
- **Category**: practical
- **Question**: คุณจัดการวงจรชีวิตของ plugin (enable/disable/update) ได้อย่างไร?
- **Options**: A) Edit a config file manually | B) Use `/plugin enable`, `/plugin disable`, `/plugin update plugin-name` | C) Use `claude plugin-manager` | D) Reinstall the plugin
- **Correct**: B
- **Explanation**: Claude Code มี slash command สำหรับการจัดการวงจรชีวิตแบบเต็ม: enable, disable, update, uninstall
- **Review**: หัวข้อ Installation methods

### Q9
- **Category**: conceptual
- **Question**: ข้อได้เปรียบหลักของ plugin เหนือ skills/hooks/MCP แบบเดี่ยวคืออะไร?
- **Options**: A) Plugins are faster | B) Single-command install, versioned, marketplace distribution, bundles everything together | C) Plugins have more permissions | D) Plugins work offline
- **Correct**: B
- **Explanation**: plugin รวมส่วนประกอบหลายอย่างไว้ในหน่วยติดตั้งเดียวพร้อมการกำหนดเวอร์ชัน การเผยแพร่ผ่าน marketplace และการอัปเดตอัตโนมัติ — เทียบกับการตั้งค่าส่วนประกอบเดี่ยวด้วยตนเอง
- **Review**: หัวข้อ Standalone vs Plugin comparison

### Q10
- **Category**: practical
- **Question**: การกำหนดค่า plugin hook อยู่ที่ไหนภายใน directory ของ plugin?
- **Options**: A) `.claude-plugin/hooks.json` | B) `hooks/hooks.json` | C) `plugin.json` hooks section | D) `.claude/settings.json`
- **Correct**: B
- **Explanation**: plugin hook ถูกกำหนดค่าใน `hooks/hooks.json` ภายในโครงสร้าง directory ของ plugin
- **Review**: หัวข้อ Plugin hooks

---

## Lesson 08: Checkpoints

### Q1
- **Category**: conceptual
- **Question**: checkpoint จับสี่สิ่งใด?
- **Options**: A) Git commits, branches, tags, stashes | B) Messages, file modifications, tool usage history, session context | C) Code, tests, logs, configs | D) Inputs, outputs, errors, timing
- **Correct**: B
- **Explanation**: checkpoint จับข้อความสนทนา การแก้ไขไฟล์ที่ทำโดยเครื่องมือของ Claude ประวัติการใช้เครื่องมือ และ session context
- **Review**: หัวข้อ Overview

### Q2
- **Category**: practical
- **Question**: คุณเข้าถึง checkpoint browser ได้อย่างไร?
- **Options**: A) Use `/checkpoints` command | B) Press `Esc + Esc` (double-escape) or use `/rewind` | C) Use `/history` command | D) Press `Ctrl+Z`
- **Correct**: B
- **Explanation**: double-escape (Esc+Esc) หรือคำสั่ง `/rewind` เปิด checkpoint browser เพื่อเลือกจุดที่จะ restore
- **Review**: หัวข้อ Accessing checkpoints

### Q3
- **Category**: conceptual
- **Question**: ตัวเลือกการ rewind มีกี่ตัว และมีอะไรบ้าง?
- **Options**: A) 3: Undo, Redo, Reset | B) 5: Restore code+conversation, Restore conversation, Restore code, Summarize from here, Never mind | C) 2: Full restore, Partial restore | D) 4: Code, Messages, Both, Cancel
- **Correct**: B
- **Explanation**: 5 ตัวเลือกคือ: Restore code and conversation (rollback เต็ม), Restore conversation only, Restore code only, Summarize from here (บีบอัด), Never mind (ยกเลิก)
- **Review**: หัวข้อ Rewind options

### Q4
- **Category**: practical
- **Question**: คุณใช้ `rm -rf temp/` ผ่าน Bash ใน Claude Code จากนั้นต้องการ rewind checkpoint จะ restore ไฟล์เหล่านั้นหรือไม่?
- **Options**: A) Yes, checkpoints capture everything | B) No, Bash filesystem operations (rm, mv, cp) are not tracked by checkpoints | C) Only if you used the Edit tool instead | D) Only if autoCheckpoint was enabled
- **Correct**: B
- **Explanation**: checkpoint ติดตามเฉพาะการเปลี่ยนแปลงไฟล์ที่ทำโดยเครื่องมือของ Claude (Write, Edit) คำสั่ง Bash เช่น rm, mv, cp ทำงานนอกการติดตามของ checkpoint
- **Review**: หัวข้อ Limitations

### Q5
- **Category**: conceptual
- **Question**: checkpoint ถูกเก็บไว้นานเท่าใด?
- **Options**: A) Until session ends | B) 7 days | C) 30 days | D) Indefinitely
- **Correct**: C
- **Explanation**: checkpoint คงอยู่ข้าม session ได้นานสูงสุด 30 วัน หลังจากนั้นจะถูกทำความสะอาดอัตโนมัติ
- **Review**: หัวข้อ Checkpoint persistence

### Q6
- **Category**: practical
- **Question**: "Summarize from here" ทำอะไรเมื่อ rewind?
- **Options**: A) Deletes the conversation from that point | B) Compresses the conversation into an AI-generated summary while preserving the original in the transcript | C) Creates a bullet-point list of changes | D) Exports the conversation to a file
- **Correct**: B
- **Explanation**: Summarize บีบอัดการสนทนาให้เป็นสรุปที่สร้างโดย AI ที่สั้นลง ข้อความเต็มต้นฉบับถูกเก็บไว้ในไฟล์ transcript
- **Review**: หัวข้อ Summarize option

### Q7
- **Category**: conceptual
- **Question**: checkpoint ถูกสร้างอัตโนมัติเมื่อใด?
- **Options**: A) Every 5 minutes | B) On every user prompt | C) Only when you manually save | D) After every tool use
- **Correct**: B
- **Explanation**: checkpoint อัตโนมัติถูกสร้างขึ้นทุก user prompt โดยจับสถานะก่อนที่ Claude จะประมวลผลคำร้องขอ
- **Review**: หัวข้อ Automatic checkpoints

### Q8
- **Category**: practical
- **Question**: คุณปิดการสร้าง checkpoint อัตโนมัติได้อย่างไร?
- **Options**: A) Use `--no-checkpoints` flag | B) Set `autoCheckpoint: false` in settings | C) Delete the checkpoints directory | D) Checkpoints cannot be disabled
- **Correct**: B
- **Explanation**: ตั้งค่า `autoCheckpoint: false` ในการกำหนดค่าของคุณเพื่อปิดการสร้าง checkpoint อัตโนมัติ (ค่าเริ่มต้นคือ true)
- **Review**: หัวข้อ Configuration

### Q9
- **Category**: conceptual
- **Question**: checkpoint เป็นตัวแทนของ git commit หรือไม่?
- **Options**: A) Yes, they're more powerful | B) No, they are complementary — checkpoints are session-scoped and expire, git is permanent and shareable | C) Yes, for small projects | D) Only in solo development
- **Correct**: B
- **Explanation**: checkpoint เป็นแบบชั่วคราว (เก็บ 30 วัน), scope ที่ session และแบ่งปันไม่ได้ ส่วน git commit เป็นแบบถาวร ตรวจสอบได้ และแบ่งปันได้ ใช้ทั้งสองร่วมกัน
- **Review**: หัวข้อ Integration with git

### Q10
- **Category**: practical
- **Question**: คุณต้องการเปรียบเทียบสองแนวทางที่ต่างกัน workflow ของ checkpoint ที่แนะนำคืออะไร?
- **Options**: A) Create two separate sessions | B) Checkpoint before approach A, try it, rewind to checkpoint, try approach B, compare results | C) Use git branches instead | D) There's no good way to compare approaches
- **Correct**: B
- **Explanation**: กลยุทธ์การแตกกิ่ง: checkpoint ที่สถานะสะอาด ลองแนวทาง A จดผลลัพธ์ rewind กลับไปยัง checkpoint เดิม ลองแนวทาง B เปรียบเทียบผลลัพธ์ทั้งสอง
- **Review**: หัวข้อ Workflow patterns

---

## Lesson 09: Advanced Features

### Q1
- **Category**: conceptual
- **Question**: permission mode หกแบบใน Claude Code มีอะไรบ้าง?
- **Options**: A) read, write, execute, admin, root, sudo | B) default, acceptEdits, plan, auto, dontAsk, bypassPermissions | C) safe, normal, elevated, admin, unrestricted, god | D) view, edit, run, deploy, full, bypass
- **Correct**: B
- **Explanation**: หกโหมดคือ: default (ถามทุกอย่าง), acceptEdits (ยอมรับการแก้ไขไฟล์อัตโนมัติ), plan (วิเคราะห์แบบอ่านอย่างเดียว), auto (classifier เบื้องหลังตัดสินใจ), dontAsk (ปฏิเสธอัตโนมัติเว้นแต่ได้รับอนุมัติล่วงหน้า), bypassPermissions (ข้ามการตรวจสอบทั้งหมด)
- **Review**: หัวข้อ Permission Modes

### Q2
- **Category**: practical
- **Question**: คุณเปิดใช้งาน planning mode ได้อย่างไร?
- **Options**: A) Only via `/plan` command | B) Via `/plan`, `Shift+Tab`/`Alt+M`, `--permission-mode plan` flag, or default config | C) Via `--planning` flag only | D) Planning is always on
- **Correct**: B
- **Explanation**: planning mode เปิดใช้งานได้หลายวิธี: คำสั่ง /plan, คีย์ลัด Shift+Tab/Alt+M, flag --permission-mode plan ของ CLI หรือเป็นค่าเริ่มต้นใน config
- **Review**: หัวข้อ Planning Mode

### Q3
- **Category**: conceptual
- **Question**: model alias `opusplan` ทำอะไร?
- **Options**: A) Uses only Opus for everything | B) Uses Opus for planning phase and Sonnet for implementation | C) Uses a special planning-optimized model | D) Enables plan mode automatically
- **Correct**: B
- **Explanation**: `opusplan` เป็น model alias ที่ใช้ Opus สำหรับเฟสการวางแผน (การวิเคราะห์คุณภาพสูงกว่า) และ Sonnet สำหรับเฟสการดำเนินการ (implement เร็วกว่า)
- **Review**: หัวข้อ Planning Mode

### Q4
- **Category**: practical
- **Question**: คุณสลับเปิด/ปิด extended thinking ระหว่าง session ได้อย่างไร?
- **Options**: A) Type `/effort max` | B) Press `Option+T` (macOS) or `Alt+T` | C) Include "ultrathink" in prompt | D) It's always enabled and cannot be toggled
- **Correct**: B
- **Explanation**: Option+T (macOS) หรือ Alt+T สลับเปิด/ปิด extended thinking สำหรับ session (`Ctrl+O` สลับโหมด verbose เพื่อแสดง/ซ่อนข้อความการให้เหตุผล) สำหรับการให้เหตุผลเชิงลึกครั้งเดียว ให้ใส่ "ultrathink" ใน prompt; สำหรับการควบคุมระดับ session ใช้คำสั่ง `/effort`
- **Review**: หัวข้อ Extended Thinking

### Q5
- **Category**: conceptual
- **Question**: คีย์เวิร์ด "ultrathink" กระตุ้นการให้เหตุผลเชิงลึกหรือไม่?
- **Options**: A) Yes, it triggers deep reasoning for one response without changing session settings | B) No, it's treated as regular prompt text | C) Yes, but only on Opus 4.6 | D) Yes, and it permanently changes the effort level
- **Correct**: A
- **Explanation**: การใส่ "ultrathink" ใน prompt เพิ่มคำสั่งใน context ให้ model ให้เหตุผลมากขึ้นในเทิร์นนั้น ไม่ได้เปลี่ยนระดับ effort ที่ส่งไปยัง API — ใช้ `/effort max` สำหรับการให้เหตุผลเชิงลึกระดับ session
- **Review**: หัวข้อ Extended Thinking

### Q6
- **Category**: practical
- **Question**: คุณรัน Claude ใน pipeline CI/CD พร้อม output JSON แบบมีโครงสร้างและจำกัดจำนวนเทิร์นได้อย่างไร?
- **Options**: A) `claude --ci --json --limit 3` | B) `claude -p --output-format json --max-turns 3 "review code"` | C) `claude --pipeline --format json` | D) `claude run --json --turns 3`
- **Correct**: B
- **Explanation**: Print mode (`-p`) พร้อม `--output-format json` และ `--max-turns` เป็นรูปแบบมาตรฐานของการผสานรวม CI/CD
- **Review**: หัวข้อ Headless/Print Mode

### Q7
- **Category**: conceptual
- **Question**: ฟีเจอร์ Task List (Ctrl+T) ให้อะไร?
- **Options**: A) A list of running background processes | B) A persistent to-do list that survives context compaction, shareable via `CLAUDE_CODE_TASK_LIST_ID` | C) A history of past sessions | D) A queue of pending tool calls
- **Correct**: B
- **Explanation**: Task List (Ctrl+T) คงอยู่ข้ามการ compact context และแบ่งปันข้าม session ได้ผ่าน directory งานที่ตั้งชื่อโดยใช้ `CLAUDE_CODE_TASK_LIST_ID`
- **Review**: หัวข้อ Task List

### Q8
- **Category**: practical
- **Question**: คุณแก้ไข plan จากภายนอก (ใน editor ที่คุณชอบ) ระหว่าง planning mode ได้อย่างไร?
- **Options**: A) Copy-paste from the terminal | B) Press `Ctrl+G` to open the plan in an external editor | C) Use `/export-plan` command | D) Plans can't be edited externally
- **Correct**: B
- **Explanation**: Ctrl+G เปิด plan ปัจจุบันใน external editor ที่กำหนดค่าไว้เพื่อแก้ไข
- **Review**: หัวข้อ Planning Mode

### Q9
- **Category**: conceptual
- **Question**: ความแตกต่างระหว่างโหมด `dontAsk` และ `bypassPermissions` คืออะไร?
- **Options**: A) They are the same | B) `dontAsk` auto-denies unless pre-approved; `bypassPermissions` skips all checks entirely | C) `dontAsk` is for files; `bypassPermissions` is for commands | D) `bypassPermissions` is safer
- **Correct**: B
- **Explanation**: dontAsk ปฏิเสธคำขอสิทธิ์อัตโนมัติเว้นแต่จะตรงกับ pattern ที่อนุมัติล่วงหน้า ส่วน bypassPermissions ข้ามการตรวจสอบความปลอดภัยทั้งหมด — อันตรายสำหรับการใช้งานประจำ
- **Review**: หัวข้อ Permission Modes

### Q10
- **Category**: practical
- **Question**: คุณส่งต่อ session CLI ไปยัง desktop app ได้อย่างไร?
- **Options**: A) Use `/export` command | B) Use `/desktop` command | C) Copy the session ID and paste in the app | D) Sessions can't transfer between CLI and desktop
- **Correct**: B
- **Explanation**: คำสั่ง `/desktop` ส่งต่อ session CLI ปัจจุบันไปยังแอปพลิเคชัน desktop แบบเนทีฟสำหรับการตรวจสอบ diff แบบภาพและการจัดการหลาย session
- **Review**: หัวข้อ Desktop App

---

## Lesson 10: CLI Reference

### Q1
- **Category**: conceptual
- **Question**: โหมดหลักสองแบบของ Claude CLI คืออะไร?
- **Options**: A) Online and offline mode | B) Interactive REPL (`claude`) and Print mode (`claude -p`) | C) GUI and terminal mode | D) Single and batch mode
- **Correct**: B
- **Explanation**: Interactive REPL เป็นโหมดสนทนาโดยค่าเริ่มต้น Print mode (-p) เป็นแบบไม่โต้ตอบ เขียน script ได้ pipe ได้ — ออกหลังจากตอบหนึ่งครั้ง
- **Review**: หัวข้อ CLI architecture

### Q2
- **Category**: practical
- **Question**: คุณ pipe ไฟล์เข้า Claude และรับ output JSON ได้อย่างไร?
- **Options**: A) `claude --file error.log --json` | B) `cat error.log | claude -p --output-format json "explain this"` | C) `claude < error.log --format json` | D) `claude -p --input error.log --json`
- **Correct**: B
- **Explanation**: pipe เนื้อหาผ่าน stdin ไปยัง print mode (-p) และใช้ --output-format json สำหรับ output แบบมีโครงสร้าง
- **Review**: หัวข้อ Interactive vs Print Mode

### Q3
- **Category**: conceptual
- **Question**: ความแตกต่างระหว่าง flag `-c` และ `-r` คืออะไร?
- **Options**: A) Both do the same thing | B) `-c` continues the most recent session; `-r` resumes by name or ID | C) `-c` creates a new session; `-r` resumes | D) `-c` is for code; `-r` is for review
- **Correct**: B
- **Explanation**: `-c/--continue` ดำเนินการต่อการสนทนาล่าสุด `-r/--resume "name"` resume session เฉพาะด้วยชื่อหรือ session ID
- **Review**: หัวข้อ Session management

### Q4
- **Category**: practical
- **Question**: คุณรับประกัน output JSON ที่ถูกต้องตาม schema จาก Claude ได้อย่างไร?
- **Options**: A) Just use `--output-format json` | B) Use `--output-format json --json-schema '{"type":"object",...}'` | C) Use `--strict-json` flag | D) JSON output is always schema-valid
- **Correct**: B
- **Explanation**: `--output-format json` เพียงอย่างเดียวสร้าง JSON แบบ best-effort การเพิ่ม `--json-schema` พร้อมการนิยาม JSON Schema รับประกันว่า output ตรงกับ schema
- **Review**: หัวข้อ Output and format

### Q5
- **Category**: conceptual
- **Question**: flag ใดทำงานเฉพาะใน print mode (-p) และไม่มีผลในโหมดโต้ตอบ?
- **Options**: A) `--model` | B) `--system-prompt-file` | C) `--verbose` | D) `--max-turns`
- **Correct**: B
- **Explanation**: `--system-prompt-file` โหลด system prompt จากไฟล์แต่ทำงานเฉพาะใน print mode ใช้ `--system-prompt` (สตริง inline) สำหรับ session แบบโต้ตอบ
- **Review**: ตารางเปรียบเทียบ System prompt flags

### Q6
- **Category**: practical
- **Question**: คุณจำกัด Claude ให้ใช้เฉพาะเครื่องมือแบบอ่านอย่างเดียวสำหรับการตรวจสอบความปลอดภัยได้อย่างไร?
- **Options**: A) `claude --read-only "audit code"` | B) `claude --permission-mode plan --tools "Read,Grep,Glob" "audit code"` | C) `claude --safe-mode "audit code"` | D) `claude --no-write "audit code"`
- **Correct**: B
- **Explanation**: รวม `--permission-mode plan` (วิเคราะห์แบบอ่านอย่างเดียว) กับ `--tools` (allowlist ของเครื่องมือเฉพาะ) เพื่อจำกัด Claude ให้ทำเฉพาะการอ่าน
- **Review**: หัวข้อ Tool and permission management

### Q7
- **Category**: conceptual
- **Question**: ลำดับความสำคัญของการนิยาม agent คืออะไร?
- **Options**: A) Project > User > CLI | B) CLI > Project > User | C) User > CLI > Project | D) All are equal priority
- **Correct**: B
- **Explanation**: agent ที่นิยามผ่าน CLI (flag --agents) มีลำดับความสำคัญสูงสุด จากนั้นระดับ Project (.claude/agents/) แล้วจึงระดับ User (~/.claude/agents/)
- **Review**: หัวข้อ Agents configuration

### Q8
- **Category**: practical
- **Question**: คุณ fork session ที่มีอยู่เพื่อลองแนวทางอื่นโดยไม่สูญเสียต้นฉบับได้อย่างไร?
- **Options**: A) Use `/fork` command | B) Use `--resume session-name --fork-session "branch name"` | C) Use `--clone session-name` | D) Use `/branch session-name`
- **Correct**: B
- **Explanation**: `--resume` พร้อม `--fork-session` สร้าง branch อิสระใหม่จาก session ที่ resume โดยรักษาการสนทนาต้นฉบับไว้
- **Review**: หัวข้อ Session management

### Q9
- **Category**: conceptual
- **Question**: `claude auth status` คืน exit code ใดเมื่อผู้ใช้ล็อกอินอยู่?
- **Options**: A) 1 | B) 0 | C) 200 | D) It doesn't return an exit code
- **Correct**: B
- **Explanation**: `claude auth status` ออกด้วย code 0 เมื่อล็อกอินอยู่ และ 1 เมื่อไม่ได้ล็อกอิน ทำให้เขียน script สำหรับการตรวจสอบ authentication ใน CI/CD ได้
- **Review**: ตาราง CLI commands

### Q10
- **Category**: practical
- **Question**: คุณประมวลผลหลายไฟล์เป็น batch ด้วย Claude ได้อย่างไร?
- **Options**: A) `claude --batch *.md` | B) Use a for loop: `for file in *.md; do claude -p "summarize: $(cat $file)" > ${file%.md}.json; done` | C) `claude -p --files *.md "summarize all"` | D) Batch processing is not supported
- **Correct**: B
- **Explanation**: ใช้ for-loop ของ shell กับ print mode เพื่อประมวลผลไฟล์ทีละไฟล์ แต่ละการเรียกใช้เป็นอิสระต่อกันและสร้าง output แบบมีโครงสร้างได้
- **Review**: หัวข้อ Batch processing
