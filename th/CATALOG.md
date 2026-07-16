<!-- i18n-source: CATALOG.md -->
<!-- i18n-date: 2026-05-09 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# คู่มืออ้างอิงฟีเจอร์ Claude Code

> คู่มืออ้างอิงฉบับย่อสำหรับฟีเจอร์ทั้งหมดของ Claude Code: คำสั่ง, agents, skills, plugins, และ hooks

**การนำทาง**: [คำสั่ง](#slash-commands) | [โหมดสิทธิ์](#permission-modes) | [Subagents](#subagents) | [Skills](#skills) | [Plugins](#plugins) | [MCP Servers](#mcp-servers) | [Hooks](#hooks) | [Memory](#memory-files) | [ฟีเจอร์ใหม่](#new-features-may-2026)

---

## ภาพรวม

| ฟีเจอร์ | Built-in | ตัวอย่าง | รวม | อ้างอิง |
|---------|----------|----------|-------|-----------|
| **Slash Commands** | 60+ | 8 | 68+ | [01-slash-commands/](../01-slash-commands/) |
| **Subagents** | 6 | 11 | 17 | [04-subagents/](../04-subagents/) |
| **Skills** | 5 bundled | 6 | 11 | [03-skills/](../03-skills/) |
| **Plugins** | - | 3 | 3 | [07-plugins/](../07-plugins/) |
| **MCP Servers** | 1 | 8 | 9 | [05-mcp/](../05-mcp/) |
| **Hooks** | 28 events | 8 | 8 | [06-hooks/](../06-hooks/) |
| **Memory** | 7 ประเภท | 3 | 3 | [02-memory/](../02-memory/) |
| **รวมทั้งหมด** | **99** | **47** | **121** | |

---

## Slash Commands

คำสั่งที่ผู้ใช้เรียกใช้งานเองเพื่อดำเนินการตามที่กำหนด

### คำสั่ง Built-in

| คำสั่ง | คำอธิบาย | เมื่อใดควรใช้ |
|---------|-------------|------------|
| `/help` | แสดงข้อมูลช่วยเหลือ | เริ่มต้นใช้งาน, เรียนรู้คำสั่ง |
| `/btw` | คำถามสั้นนอกบริบทหลัก — ไม่กระทบ context หลัก | คำถามแวบหนึ่ง |
| `/chrome` | กำหนดค่าการเชื่อมต่อ Chrome | การทำงานอัตโนมัติในเบราว์เซอร์ |
| `/clear` | ล้างประวัติการสนทนา | เริ่มต้นใหม่, ลด context |
| `/diff` | ดู diff แบบโต้ตอบ | ตรวจสอบการเปลี่ยนแปลง |
| `/config` | ดู/แก้ไขการกำหนดค่า | ปรับแต่งพฤติกรรม |
| `/status` | แสดงสถานะเซสชัน | ตรวจสอบสถานะปัจจุบัน |
| `/agents` | แสดง agents ที่ใช้งานได้ | ดูตัวเลือกการมอบหมายงาน |
| `/skills` | แสดง skills ที่ใช้งานได้ | ดูความสามารถที่เรียกใช้อัตโนมัติ |
| `/hooks` | แสดง hooks ที่กำหนดค่าไว้ | debug ระบบอัตโนมัติ |
| `/insights` | วิเคราะห์รูปแบบเซสชัน | ปรับปรุงประสิทธิภาพเซสชัน |
| `/install-slack-app` | ติดตั้ง Claude Slack app | การผสานรวม Slack |
| `/keybindings` | ปรับแต่งคีย์ลัด | การปรับแต่งคีย์ |
| `/mcp` | แสดง MCP servers | ตรวจสอบการผสานรวมภายนอก |
| `/memory` | ดูไฟล์ memory ที่โหลดอยู่ | debug การโหลด context |
| `/mobile` | สร้าง QR code สำหรับมือถือ | การเข้าถึงผ่านมือถือ |
| `/passes` | ดู usage passes | ข้อมูลการสมัครสมาชิก |
| `/plugin` | จัดการ plugins | ติดตั้ง/ลบส่วนขยาย |
| `/plan` | เข้าสู่ planning mode | การวางแผนการพัฒนาที่ซับซ้อน |
| `/proactive` | Alias สำหรับ `/loop` (v2.1.105) | เหมือนกับ `/loop` |
| `/recap` | แสดงสรุปเซสชันเมื่อกลับมา | หลังจากไม่ได้ใช้งานนาน |
| `/rewind` | ย้อนกลับไปยัง checkpoint | ยกเลิกการเปลี่ยนแปลง, สำรวจทางเลือก |
| `/checkpoint` | จัดการ checkpoints | บันทึก/กู้คืนสถานะ |
| `/cost` | คำสั่งลัดเปิดแท็บ cost ใน `/usage` (v2.1.118+) | ติดตามค่าใช้จ่าย |
| `/context` | แสดงการใช้งาน context window | จัดการความยาวการสนทนา |
| `/export` | ส่งออกการสนทนา | บันทึกไว้อ้างอิง |
| `/extra-usage` | กำหนดค่าขีดจำกัดการใช้งานพิเศษ | การจัดการ rate limit |
| `/feedback` | ส่ง feedback หรือรายงานปัญหา | รายงานปัญหา |
| `/login` | ยืนยันตัวตนกับ Anthropic | เข้าถึงฟีเจอร์ |
| `/logout` | ออกจากระบบ | สลับบัญชี |
| `/sandbox` | เปิด/ปิด sandbox mode | การดำเนินการคำสั่งที่ปลอดภัย |
| `/doctor` | รันการวินิจฉัย | แก้ไขปัญหา |
| `/reload-plugins` | โหลด plugins ใหม่ | การจัดการ plugin |
| `/release-notes` | แสดง release notes | ตรวจสอบฟีเจอร์ใหม่ |
| `/remote-control` | เปิดใช้งาน remote control | การเข้าถึงระยะไกล |
| `/permissions` | จัดการสิทธิ์ | ควบคุมการเข้าถึง |
| `/session` | จัดการเซสชัน | workflow หลายเซสชัน |
| `/rename` | เปลี่ยนชื่อเซสชันปัจจุบัน | จัดระเบียบเซสชัน |
| `/resume` | กลับไปยังเซสชันก่อนหน้า | ต่อเนื่องงาน |
| `/todo` | ดู/จัดการรายการงาน | ติดตามงาน |
| `/tui` | เปิด/ปิด fullscreen TUI mode | การแสดงผลแบบ flicker-free ใน fullscreen/tmux |
| `/tasks` | ดูงานในพื้นหลัง | ติดตามการดำเนินการแบบ async |
| `/copy` | คัดลอกการตอบสนองล่าสุดไปยัง clipboard | แชร์ผลลัพธ์อย่างรวดเร็ว |
| `/teleport` | ถ่ายโอนเซสชันไปยังเครื่องอื่น | ทำงานต่อเนื่องจากระยะไกล |
| `/desktop` | เปิด Claude Desktop app | สลับไปยัง desktop interface |
| `/theme` | เปลี่ยน color theme | ปรับแต่งรูปลักษณ์ |
| `/usage` | คำสั่งหลักสำหรับ usage/cost/stats (v2.1.118) | ติดตามโควต้าและค่าใช้จ่าย |
| `/focus` | เปิด/ปิด focus view | ลด visual noise ระหว่างงานที่ใช้เวลานาน |
| `/fork` | แยกสาขาการสนทนาปัจจุบัน | สำรวจทางเลือก |
| `/stats` | คำสั่งลัดเปิดแท็บ stats ใน `/usage` (v2.1.118+) | ดูสถิติเซสชัน |
| `/statusline` | กำหนดค่า status line | ปรับแต่งการแสดงสถานะ |
| `/fast` | เปิด/ปิด fast output mode | เพิ่มความเร็วในการตอบสนอง |
| `/terminal-setup` | กำหนดค่าการผสานรวม terminal | ตั้งค่าฟีเจอร์ terminal |
| `/undo` | Alias สำหรับ `/rewind` (v2.1.108) | เหมือนกับ `/rewind` |
| `/upgrade` | ตรวจสอบการอัปเดต | การจัดการเวอร์ชัน |
| `/team-onboarding` | สร้างคู่มือ onboarding สำหรับสมาชิกทีม | onboarding สมาชิกทีมใหม่ (v2.1.101) |
| `/ultraplan` | มอบงานวางแผนให้ Claude Code web session ใน plan mode | วางแผนขนาดใหญ่ (Research Preview, v2.1.91+) |
| `/ultrareview` | รัน cloud multi-agent code review บนการเปลี่ยนแปลงปัจจุบัน | ตรวจสอบโค้ดเชิงลึกก่อน merge (v2.1.112) |
| `/less-permission-prompts` | สแกน transcripts และเสนอ allowlist สำหรับเครื่องมือ read-only | ลดการแจ้งสิทธิ์ซ้ำซ้อนในโปรเจกต์ (v2.1.112) |

### คำสั่งกำหนดเอง (ตัวอย่าง)

| คำสั่ง | คำอธิบาย | เมื่อใดควรใช้ | ขอบเขต | การติดตั้ง |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | วิเคราะห์โค้ดสำหรับการปรับปรุง | ปรับปรุงประสิทธิภาพ | Project | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | เตรียม pull request | ก่อนส่ง PR | Project | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | สร้างเอกสาร API | จัดทำเอกสาร API | Project | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | สร้าง git commit พร้อม context | commit การเปลี่ยนแปลง | User | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | stage, commit, และ push | deployment อย่างรวดเร็ว | User | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | ปรับโครงสร้างเอกสาร | ปรับปรุงเอกสาร | Project | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | ตั้งค่า CI/CD pipeline | โปรเจกต์ใหม่ | Project | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | ขยายการครอบคลุมของ test | ปรับปรุงการทดสอบ | Project | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **ขอบเขต**: `User` = workflow ส่วนตัว (`~/.claude/commands/`), `Project` = ใช้ร่วมกันในทีม (`.claude/commands/`)

**อ้างอิง**: [01-slash-commands/](../01-slash-commands/) | [Official Docs](https://code.claude.com/docs/en/interactive-mode)

**ติดตั้งทั้งหมดด้วยคำสั่งเดียว**:
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## Permission Modes

Claude Code รองรับ 6 permission modes ที่ควบคุมการอนุญาตการใช้เครื่องมือ

| Mode | คำอธิบาย | เมื่อใดควรใช้ |
|------|-------------|------------|
| `default` | แจ้งสำหรับทุกการเรียกใช้เครื่องมือ | การใช้งานแบบโต้ตอบมาตรฐาน |
| `acceptEdits` | ยอมรับการแก้ไขไฟล์อัตโนมัติ แจ้งสำหรับอื่น | workflow การแก้ไขที่เชื่อถือได้ |
| `plan` | เครื่องมือ read-only เท่านั้น ไม่มีการเขียน | การวางแผนและสำรวจ |
| `auto` | ยอมรับเครื่องมือทั้งหมดโดยไม่แจ้ง | การดำเนินการอัตโนมัติเต็มรูปแบบ (Research Preview) |
| `bypassPermissions` | ข้ามการตรวจสอบสิทธิ์ทั้งหมด | CI/CD, headless environments |
| `dontAsk` | ข้ามเครื่องมือที่ต้องการสิทธิ์ | scripting แบบ non-interactive |

> **หมายเหตุ**: `auto` mode เป็น Research Preview (มีนาคม 2026) ใช้ `bypassPermissions` เฉพาะในสภาพแวดล้อมที่เชื่อถือได้

**อ้างอิง**: [Official Docs](https://code.claude.com/docs/en/permissions)

---

## Subagents

ผู้ช่วย AI เฉพาะทางที่มี context แยกสำหรับงานเฉพาะเจาะจง

### Built-in Subagents

| Agent | คำอธิบาย | เครื่องมือ | Model | เมื่อใดควรใช้ |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | งานหลายขั้นตอน, การวิจัย | เครื่องมือทั้งหมด | Inherits model | การวิจัยซับซ้อน, งานหลายไฟล์ |
| **Plan** | การวางแผนการพัฒนา | Read, Glob, Grep, Bash | Inherits model | การออกแบบสถาปัตยกรรม, การวางแผน |
| **Explore** | สำรวจ codebase | Read, Glob, Grep | Haiku 4.5 | ค้นหาอย่างรวดเร็ว, ทำความเข้าใจโค้ด |
| **Bash** | ดำเนินการคำสั่ง | Bash | Inherits model | การดำเนินการ Git, งาน terminal |
| **statusline-setup** | การกำหนดค่า status line | Bash, Read, Write | Sonnet 4.6 | กำหนดค่าการแสดง status line |
| **Claude Code Guide** | ช่วยเหลือและเอกสาร | Read, Glob, Grep | Haiku 4.5 | ขอความช่วยเหลือ, เรียนรู้ฟีเจอร์ |

### ฟิลด์การกำหนดค่า Subagent

| ฟิลด์ | ประเภท | คำอธิบาย |
|-------|------|-------------|
| `name` | string | ตัวระบุ agent |
| `description` | string | สิ่งที่ agent ทำ |
| `model` | string | การกำหนด model (เช่น `haiku-4.5`) |
| `tools` | array | รายการเครื่องมือที่อนุญาต |
| `effort` | string | ระดับความพยายามในการให้เหตุผล (`low`, `medium`, `high`) |
| `initialPrompt` | string | system prompt ที่ inject เมื่อเริ่ม agent |
| `disallowedTools` | array | เครื่องมือที่ปฏิเสธอย่างชัดเจน |

### Subagents กำหนดเอง (ตัวอย่าง)

| Agent | คำอธิบาย | เมื่อใดควรใช้ | ขอบเขต | การติดตั้ง |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | ตรวจสอบคุณภาพโค้ดอย่างครอบคลุม | เซสชันตรวจสอบโค้ด | Project | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | ออกแบบสถาปัตยกรรมฟีเจอร์ | การวางแผนฟีเจอร์ใหม่ | Project | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | วิเคราะห์ codebase เชิงลึก | ทำความเข้าใจฟีเจอร์ที่มีอยู่ | Project | `cp 04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | ตรวจสอบหลักการ Clean Code | การตรวจสอบความสามารถในการบำรุงรักษา | Project | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | กลยุทธ์และความครอบคลุมของ test | การวางแผนทดสอบ | Project | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | เอกสารทางเทคนิค | เอกสาร API, คู่มือ | Project | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | การตรวจสอบด้านความปลอดภัย | การตรวจสอบความปลอดภัย | Project | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | การพัฒนาฟีเจอร์เต็มรูปแบบ | การพัฒนาฟีเจอร์ | Project | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | การวิเคราะห์สาเหตุหลัก | การสืบสวนปัญหา | User | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL queries, การวิเคราะห์ข้อมูล | งานข้อมูล | User | `cp 04-subagents/data-scientist.md .claude/agents/` |
| `performance-optimizer` | การวิเคราะห์และปรับปรุงประสิทธิภาพ | การสืบสวนจุดคอขวด | Project | `cp 04-subagents/performance-optimizer.md .claude/agents/` |

> **ขอบเขต**: `User` = ส่วนตัว (`~/.claude/agents/`), `Project` = ใช้ร่วมกันในทีม (`.claude/agents/`)

**อ้างอิง**: [04-subagents/](../04-subagents/) | [Official Docs](https://code.claude.com/docs/en/sub-agents)

**ติดตั้งทั้งหมด**:
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## Skills

ความสามารถที่เรียกใช้อัตโนมัติพร้อมคำแนะนำ, scripts, และ templates

### ตัวอย่าง Skills

| Skill | คำอธิบาย | เรียกใช้อัตโนมัติเมื่อ | ขอบเขต | การติดตั้ง |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | ตรวจสอบโค้ดอย่างครอบคลุม | "Review this code", "Check quality" | Project | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | ตรวจสอบความสอดคล้องของแบรนด์ | เขียน marketing copy | Project | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | สร้างเอกสาร API | "Generate docs", "Document API" | Project | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | การ refactoring โค้ดอย่างเป็นระบบ | "Refactor this", "Clean up code" | User | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **ขอบเขต**: `User` = ส่วนตัว (`~/.claude/skills/`), `Project` = ใช้ร่วมกันในทีม (`.claude/skills/`)

### โครงสร้าง Skill

```
~/.claude/skills/skill-name/
├── SKILL.md          # คำจำกัดความและคำแนะนำของ skill
├── scripts/          # scripts ช่วยเหลือ
└── templates/        # templates ผลลัพธ์
```

### ฟิลด์ frontmatter ของ Skill

Skills รองรับ YAML frontmatter ใน `SKILL.md` สำหรับการกำหนดค่า:

| ฟิลด์ | ประเภท | คำอธิบาย |
|-------|------|-------------|
| `name` | string | ชื่อแสดงผลของ skill |
| `description` | string | สิ่งที่ skill ทำ |
| `autoInvoke` | array | วลีทริกเกอร์สำหรับการเรียกใช้อัตโนมัติ |
| `effort` | string | ระดับความพยายาม (`low`, `medium`, `high`) |
| `shell` | string | shell สำหรับ scripts (`bash`, `zsh`, `sh`) |

**อ้างอิง**: [03-skills/](../03-skills/) | [Official Docs](https://code.claude.com/docs/en/skills)

**ติดตั้งทั้งหมด**:
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### Bundled Skills

| Skill | คำอธิบาย | เรียกใช้อัตโนมัติเมื่อ |
|-------|-------------|-------------------|
| `/simplify` | ตรวจสอบคุณภาพโค้ด | หลังเขียนโค้ด |
| `/batch` | รัน prompts กับหลายไฟล์ | การดำเนินการแบบ batch |
| `/debug` | debug ข้อผิดพลาดหรือการทดสอบที่ล้มเหลว | เซสชัน debugging |
| `/loop` | รัน prompts ตามช่วงเวลา | งานที่ทำซ้ำ |
| `/claude-api` | สร้างแอปด้วย Claude API | การพัฒนา API |

---

## Plugins

ชุดรวมของคำสั่ง, agents, MCP servers, และ hooks

### ตัวอย่าง Plugins

| Plugin | คำอธิบาย | ส่วนประกอบ | เมื่อใดควรใช้ | ขอบเขต | การติดตั้ง |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | workflow ตรวจสอบ PR | 3 คำสั่ง, 3 agents, GitHub MCP | การตรวจสอบโค้ด | Project | `/plugin install pr-review` |
| `devops-automation` | Deployment และการติดตาม | 4 คำสั่ง, 3 agents, K8s MCP | งาน DevOps | Project | `/plugin install devops-automation` |
| `documentation` | ชุดสร้างเอกสาร | 4 คำสั่ง, 3 agents, templates | เอกสาร | Project | `/plugin install documentation` |

### โครงสร้าง Plugin

```
.claude-plugin/
├── plugin.json       # ไฟล์ manifest
├── commands/         # Slash commands
├── agents/           # Subagents
├── skills/           # Skills
├── mcp/              # การกำหนดค่า MCP
├── hooks/            # Hook scripts
└── scripts/          # Utility scripts
```

**อ้างอิง**: [07-plugins/](../07-plugins/) | [Official Docs](https://code.claude.com/docs/en/plugins)

**คำสั่งจัดการ Plugin**:
```bash
/plugin list              # แสดง plugins ที่ติดตั้ง
/plugin install <name>    # ติดตั้ง plugin
/plugin remove <name>     # ลบ plugin
/plugin update <name>     # อัปเดต plugin
```

---

## MCP Servers

Model Context Protocol servers สำหรับเข้าถึงเครื่องมือและ API ภายนอก

### MCP Servers ทั่วไป

| Server | คำอธิบาย | เมื่อใดควรใช้ | ขอบเขต | การติดตั้ง |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | จัดการ PR, issues, โค้ด | GitHub workflows | Project | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL queries, การเข้าถึงข้อมูล | การดำเนินการฐานข้อมูล | Project | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | การดำเนินการไฟล์ขั้นสูง | งานไฟล์ที่ซับซ้อน | User | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | การสื่อสารในทีม | การแจ้งเตือน, การอัปเดต | Project | กำหนดค่าในการตั้งค่า |
| **Google Docs** | การเข้าถึงเอกสาร | การแก้ไขเอกสาร | Project | กำหนดค่าในการตั้งค่า |
| **Asana** | การจัดการโปรเจกต์ | การติดตามงาน | Project | กำหนดค่าในการตั้งค่า |
| **Stripe** | ข้อมูลการชำระเงิน | การวิเคราะห์ทางการเงิน | Project | กำหนดค่าในการตั้งค่า |
| **Memory** | หน่วยความจำถาวร | การเรียกใช้ข้ามเซสชัน | User | กำหนดค่าในการตั้งค่า |
| **Context7** | เอกสารไลบรารี | การค้นหาเอกสารล่าสุด | Built-in | Built-in |

### ตัวอย่างการกำหนดค่า MCP

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**อ้างอิง**: [05-mcp/](../05-mcp/) | [MCP Protocol Docs](https://modelcontextprotocol.io)

---

## Hooks

ระบบอัตโนมัติที่ขับเคลื่อนด้วยเหตุการณ์ซึ่งดำเนินการคำสั่ง shell ตามเหตุการณ์ของ Claude Code

### Hook Events

| เหตุการณ์ | คำอธิบาย | เมื่อทริกเกอร์ | กรณีการใช้งาน |
|-------|-------------|----------------|-----------|
| `SessionStart` | เซสชันเริ่มต้น/กลับมา | การเริ่มต้นเซสชัน | งานตั้งค่า |
| `InstructionsLoaded` | คำแนะนำโหลดแล้ว | CLAUDE.md หรือไฟล์กฎโหลดแล้ว | การจัดการคำแนะนำกำหนดเอง |
| `UserPromptSubmit` | ก่อนประมวลผล prompt | ผู้ใช้ส่งข้อความ | การตรวจสอบ input |
| `PreToolUse` | ก่อนดำเนินการเครื่องมือ | ก่อนเครื่องมือใดก็ตามทำงาน | การตรวจสอบ, การบันทึก |
| `PermissionRequest` | แสดงกล่องโต้ตอบสิทธิ์ | ก่อนการดำเนินการที่ละเอียดอ่อน | flows การอนุมัติกำหนดเอง |
| `PostToolUse` | หลังเครื่องมือสำเร็จ | หลังเครื่องมือใดก็ตามเสร็จสิ้น | การจัดรูปแบบ, การแจ้งเตือน |
| `PostToolUseFailure` | เครื่องมือดำเนินการล้มเหลว | หลังข้อผิดพลาดของเครื่องมือ | การจัดการข้อผิดพลาด, การบันทึก |
| `Notification` | ส่งการแจ้งเตือน | Claude ส่งการแจ้งเตือน | การแจ้งเตือนภายนอก |
| `SubagentStart` | spawn subagent | งาน subagent เริ่มต้น | กำหนดค่าเริ่มต้น subagent context |
| `SubagentStop` | subagent เสร็จสิ้น | งาน subagent เสร็จสมบูรณ์ | การดำเนินการต่อเนื่อง |
| `Stop` | Claude ตอบสนองเสร็จสิ้น | การตอบสนองเสร็จสมบูรณ์ | การล้างข้อมูล, การรายงาน |
| `StopFailure` | ข้อผิดพลาด API สิ้นสุด turn | เกิดข้อผิดพลาด API | การกู้คืนข้อผิดพลาด, การบันทึก |
| `TeammateIdle` | Teammate agent ไม่ได้ใช้งาน | การประสานงาน agent team | การกระจายงาน |
| `TaskCompleted` | งานทำเครื่องหมายว่าเสร็จสิ้น | งานเสร็จสมบูรณ์ | การประมวลผลหลังงาน |
| `TaskCreated` | สร้างงานผ่าน TaskCreate | สร้างงานใหม่ | การติดตามงาน, การบันทึก |
| `ConfigChange` | อัปเดตการกำหนดค่า | ปรับเปลี่ยนการตั้งค่า | ตอบสนองต่อการเปลี่ยนแปลงการกำหนดค่า |
| `CwdChanged` | เปลี่ยน working directory | เปลี่ยนไดเรกทอรี | การตั้งค่าเฉพาะไดเรกทอรี |
| `FileChanged` | ไฟล์ที่ติดตามเปลี่ยนแปลง | ไฟล์ถูกแก้ไข | การติดตามไฟล์, การ rebuild |
| `PreCompact` | ก่อนการ compact | การบีบอัด context | การรักษาสถานะ |
| `PostCompact` | หลังการ compaction เสร็จสิ้น | การ compaction เสร็จสมบูรณ์ | การดำเนินการหลัง compact |
| `WorktreeCreate` | กำลังสร้าง worktree | สร้าง Git worktree | ตั้งค่าสภาพแวดล้อม worktree |
| `WorktreeRemove` | กำลังลบ worktree | ลบ Git worktree | ล้างทรัพยากร worktree |
| `Elicitation` | MCP server ขอ input | MCP elicitation | การตรวจสอบ input |
| `ElicitationResult` | ผู้ใช้ตอบสนองต่อ elicitation | ผู้ใช้ตอบสนอง | การประมวลผลการตอบสนอง |
| `SessionEnd` | เซสชันสิ้นสุด | การสิ้นสุดเซสชัน | การล้างข้อมูล, บันทึกสถานะ |

### ตัวอย่าง Hooks

| Hook | คำอธิบาย | เหตุการณ์ | ขอบเขต | การติดตั้ง |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | การตรวจสอบคำสั่ง | PreToolUse:Bash | Project | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | การสแกนความปลอดภัย | PostToolUse:Write | Project | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | การจัดรูปแบบอัตโนมัติ | PostToolUse:Write | User | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | การตรวจสอบ prompt | UserPromptSubmit | Project | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | การติดตามการใช้งาน token | Stop | User | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | การตรวจสอบก่อน commit | PreToolUse:Bash | Project | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | การบันทึกคำสั่ง | PostToolUse:Bash | User | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |
| `dependency-check.sh` | การสแกนช่องโหว่เมื่อไฟล์ manifest เปลี่ยนแปลง | PostToolUse:Write | Project | `cp 06-hooks/dependency-check.sh .claude/hooks/` |

> **ขอบเขต**: `Project` = ทีม (`.claude/settings.json`), `User` = ส่วนตัว (`~/.claude/settings.json`)

### การกำหนดค่า Hook

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "~/.claude/hooks/validate-bash.py"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "~/.claude/hooks/format-code.sh"
      }
    ]
  }
}
```

**อ้างอิง**: [06-hooks/](../06-hooks/) | [Official Docs](https://code.claude.com/docs/en/hooks)

**ติดตั้งทั้งหมด**:
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## Memory Files

Context ถาวรที่โหลดอัตโนมัติข้ามเซสชัน

### ประเภท Memory

| ประเภท | ตำแหน่ง | ขอบเขต | เมื่อใดควรใช้ |
|------|----------|-------|------------|
| **Managed Policy** | นโยบายที่จัดการโดยองค์กร | Organization | บังคับใช้มาตรฐานทั่วองค์กร |
| **Project** | `./CLAUDE.md` | Project (ทีม) | มาตรฐานทีม, context โปรเจกต์ |
| **Project Rules** | `.claude/rules/` | Project (ทีม) | กฎโปรเจกต์แบบโมดูลาร์ |
| **User** | `~/.claude/CLAUDE.md` | User (ส่วนตัว) | ความชอบส่วนตัว |
| **User Rules** | `~/.claude/rules/` | User (ส่วนตัว) | กฎส่วนตัวแบบโมดูลาร์ |
| **Local** | `./CLAUDE.local.md` | Local (git-ignored) | การตั้งค่าเฉพาะเครื่อง (gitignored) |
| **Auto Memory** | อัตโนมัติ | Session | ข้อมูลเชิงลึกและการแก้ไขที่บันทึกอัตโนมัติ |

**อ้างอิง**: [02-memory/](../02-memory/) | [Official Docs](https://code.claude.com/docs/en/memory)

**ติดตั้งอย่างรวดเร็ว**:
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## New Features (May 2026)

| ฟีเจอร์ | คำอธิบาย | วิธีใช้งาน |
|---------|-------------|------------|
| **/focus** | เปิด/ปิด focus view สำหรับการแสดงผลแบบ distraction-free (v2.1.110) | รัน `/focus` เพื่อลด visual noise ระหว่างงานที่ใช้เวลานาน |
| **/proactive** | Alias สำหรับ `/loop` (v2.1.105) | ใช้ `/proactive` แทน `/loop` ได้ |
| **/recap** | แสดงสรุปเซสชันเมื่อกลับมา (v2.1.108) | รัน `/recap` หลังจากไม่ได้ใช้งาน |
| **/tui** | เปิด/ปิด fullscreen TUI mode (v2.1.110) | ใช้ `/tui` ใน fullscreen terminals หรือ tmux |
| **/undo** | Alias สำหรับ `/rewind` (v2.1.108) | ใช้ `/undo` แทน `/rewind` ได้ |
| **Monitor Tool** | ดูสตรีม stdout ของคำสั่งพื้นหลัง (v2.1.98+) | ใช้ Monitor tool ผ่าน [Advanced Features](../09-advanced-features/) |
| **/team-onboarding** | สร้างคู่มือ onboarding อัตโนมัติ (v2.1.101) | รัน `/team-onboarding` ในโปรเจกต์ |
| **Auto Mode** | การดำเนินการอัตโนมัติเต็มรูปแบบ (Research Preview) | ใช้ `--mode auto` หรือ `/permissions auto` |
| **Remote Control** | ควบคุมเซสชัน Claude Code จากระยะไกลผ่าน API | ใช้ remote control API ส่ง prompts และรับการตอบสนองแบบ programmatic |
| **Web Sessions** | รัน Claude Code ในสภาพแวดล้อม browser | เข้าถึงผ่าน `claude web` หรือ Anthropic Console |
| **Desktop App** | แอปพลิเคชัน desktop สำหรับ Claude Code | ใช้ `/desktop` หรือดาวน์โหลดจากเว็บไซต์ Anthropic |
| **Agent Teams** | ประสานงาน agents หลายตัวในงานที่เกี่ยวข้องกัน | กำหนดค่า teammate agents ที่ร่วมมือและแชร์ context |
| **Task List** | การจัดการและติดตามงานพื้นหลัง | ใช้ `/tasks` เพื่อดูและจัดการการดำเนินการพื้นหลัง |

---

## ตารางอ้างอิงด่วน

### คู่มือการเลือกฟีเจอร์

| ความต้องการ | ฟีเจอร์ที่แนะนำ | เหตุผล |
|------|---------------------|-----|
| คำสั่งลัด | Slash Command | Manual, ทันที |
| Context ถาวร | Memory | โหลดอัตโนมัติ |
| ระบบอัตโนมัติซับซ้อน | Skill | เรียกใช้อัตโนมัติ |
| งานเฉพาะทาง | Subagent | Context แยกออกมา |
| ข้อมูลภายนอก | MCP Server | การเข้าถึงแบบ real-time |
| ระบบอัตโนมัติตามเหตุการณ์ | Hook | ทริกเกอร์ตามเหตุการณ์ |
| โซลูชันครบวงจร | Plugin | ชุดรวมทั้งหมด |

---

**อัปเดตล่าสุด**: 6 พฤษภาคม 2026
**Claude Code Version**: 2.1.131
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
