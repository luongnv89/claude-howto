<!-- i18n-source: QUICK_REFERENCE.md -->
<!-- i18n-date: 2026-07-15 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code Examples - บัตรอ้างอิงด่วน

## คำสั่งติดตั้งอย่างรวดเร็ว

### Slash Commands
```bash
# ติดตั้งทั้งหมด
cp 01-slash-commands/*.md .claude/commands/

# ติดตั้งเฉพาะรายการ
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memory
```bash
# Project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Personal memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills
```bash
# Personal skills
cp -r 03-skills/code-review ~/.claude/skills/

# Project skills
cp -r 03-skills/code-review .claude/skills/
```

### Subagents
```bash
# ติดตั้งทั้งหมด
cp 04-subagents/*.md .claude/agents/

# ติดตั้งเฉพาะรายการ
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# กำหนด credentials
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# ติดตั้งการกำหนดค่า (ขอบเขตโครงการ)
cp 05-mcp/github-mcp.json .mcp.json

# หรือขอบเขตผู้ใช้: เพิ่มใน ~/.claude.json
```

### Hooks
```bash
# ติดตั้ง hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# กำหนดค่าในการตั้งค่า (~/.claude/settings.json)
```

### Plugins
```bash
# ติดตั้งจากตัวอย่าง (หากเผยแพร่แล้ว)
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints
```bash
# Checkpoint ถูกสร้างโดยอัตโนมัติพร้อมกับ prompt ของผู้ใช้ทุกครั้ง
# หากต้องการ rewind กด Esc สองครั้งหรือใช้:
/rewind

# จากนั้นเลือก: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, หรือ Never mind
```

### Advanced Features
```bash
# กำหนดค่าในการตั้งค่า (.claude/settings.json)
# ดู 09-advanced-features/config-examples.json

# Planning mode
/plan Task description

# Permission modes (ใช้ flag --permission-mode)
# default        - ขออนุมัติสำหรับการกระทำที่มีความเสี่ยง
# acceptEdits    - ยอมรับการแก้ไขไฟล์โดยอัตโนมัติ ขอสำหรับอื่นๆ
# plan           - การวิเคราะห์แบบอ่านอย่างเดียว ไม่มีการแก้ไข
# dontAsk        - ยอมรับการกระทำทั้งหมดยกเว้นที่มีความเสี่ยงสูง
# auto           - background classifier ตัดสินใจ permission โดยอัตโนมัติ
# bypassPermissions - ยอมรับการกระทำทั้งหมด (ต้องใช้ --dangerously-skip-permissions)

# Session management
/resume                # ต่อการสนทนาก่อนหน้า
/rename "name"         # ตั้งชื่อ session ปัจจุบัน
/fork                  # แยก session ปัจจุบัน
claude -c              # ต่อการสนทนาล่าสุด
claude -r "session"    # ต่อ session ตามชื่อ/ID
```

---

## ตาราง Cheat Sheet ฟีเจอร์

| ฟีเจอร์ | เส้นทางติดตั้ง | การใช้งาน |
|---------|-------------|-------|
| **Slash Commands (60+)** | `.claude/commands/*.md` | `/command-name` |
| **Memory** | `./CLAUDE.md` | โหลดอัตโนมัติ |
| **Skills** | `.claude/skills/*/SKILL.md` | เรียกใช้อัตโนมัติ |
| **Subagents** | `.claude/agents/*.md` | มอบหมายอัตโนมัติ |
| **MCP** | `.mcp.json` (โครงการ) หรือ `~/.claude.json` (ผู้ใช้) | `/mcp__server__action` |
| **Hooks (28 events)** | `~/.claude/hooks/*.sh` | ขับเคลื่อนด้วยเหตุการณ์ (5 ประเภท) |
| **Plugins** | ผ่าน `/plugin install` | รวมทุกอย่าง |
| **Checkpoints** | Built-in | `Esc+Esc` หรือ `/rewind` |
| **Planning Mode** | Built-in | `/plan <task>` |
| **Permission Modes (6)** | Built-in | `--allowedTools`, `--permission-mode` |
| **Sessions** | Built-in | `/session <command>` |
| **Background Tasks** | Built-in | รันในพื้นหลัง |
| **Remote Control** | Built-in | WebSocket API |
| **Web Sessions** | Built-in | `claude web` |
| **Git Worktrees** | Built-in | `/worktree` |
| **Auto Memory** | Built-in | บันทึกอัตโนมัติใน CLAUDE.md |
| **Task List** | Built-in | `/task list` |
| **Bundled Skills (5)** | Built-in | `/simplify`, `/loop`, `/claude-api`, `/voice`, `/browse` |

---

## กรณีใช้งานทั่วไป

### การตรวจสอบโค้ด
```bash
# วิธีที่ 1: Slash command
cp 01-slash-commands/optimize.md .claude/commands/
# ใช้: /optimize

# วิธีที่ 2: Subagent
cp 04-subagents/code-reviewer.md .claude/agents/
# ใช้: มอบหมายอัตโนมัติ

# วิธีที่ 3: Skill
cp -r 03-skills/code-review ~/.claude/skills/
# ใช้: เรียกใช้อัตโนมัติ

# วิธีที่ 4: Plugin (ดีที่สุด)
/plugin install pr-review
# ใช้: /review-pr
```

### เอกสาร
```bash
# Slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Plugin (โซลูชันครบวงจร)
/plugin install documentation
```

### DevOps
```bash
# Plugin ที่สมบูรณ์
/plugin install devops-automation

# Commands: /deploy, /rollback, /status, /incident
```

### มาตรฐานทีม
```bash
# Project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# แก้ไขสำหรับทีมของคุณ
vim CLAUDE.md
```

### การทำงานอัตโนมัติและ Hooks
```bash
# ติดตั้ง hooks (28 events, 5 ประเภท: command, http, mcp_tool, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# ตัวอย่าง:
# - การทดสอบก่อน commit: pre-commit.sh
# - จัดรูปแบบโค้ดอัตโนมัติ: format-code.sh
# - การสแกนความปลอดภัย: security-scan.sh

# Auto Mode สำหรับ workflow อัตโนมัติครบวงจร
claude --enable-auto-mode -p "Refactor and test the auth module"
# หรือสลับโหมดแบบโต้ตอบด้วย Shift+Tab
```

### การ Refactor ที่ปลอดภัย
```bash
# Checkpoint ถูกสร้างโดยอัตโนมัติก่อน prompt แต่ละรายการ
# ลอง refactor
# หากได้ผล: ดำเนินต่อไป
# หากล้มเหลว: กด Esc+Esc หรือใช้ /rewind เพื่อย้อนกลับ
```

### การพัฒนาที่ซับซ้อน
```bash
# ใช้ planning mode
/plan Implement user authentication system

# Claude สร้างแผนโดยละเอียด
# ตรวจสอบและอนุมัติ
# Claude พัฒนาอย่างเป็นระบบ
```

### การเชื่อมต่อ CI/CD
```bash
# รันในโหมด headless (non-interactive)
claude -p "Run all tests and generate report"

# ด้วย permission mode สำหรับ CI
claude -p "Run tests" --permission-mode dontAsk

# ด้วย Auto Mode สำหรับงาน CI อัตโนมัติครบวงจร
claude --enable-auto-mode -p "Run tests and fix failures"

# ด้วย hooks สำหรับการทำงานอัตโนมัติ
# ดู 09-advanced-features/README.md
```

### การเรียนรู้และการทดลอง
```bash
# ใช้ plan mode สำหรับการวิเคราะห์ที่ปลอดภัย
claude --permission-mode plan

# ทดลองอย่างปลอดภัย - checkpoint ถูกสร้างโดยอัตโนมัติ
# หากต้องการ rewind: กด Esc+Esc หรือใช้ /rewind
```

### Agent Teams
```bash
# เปิดใช้งาน agent teams
export CLAUDE_AGENT_TEAMS=1

# หรือใน settings.json
{ "agentTeams": { "enabled": true } }

# เริ่มด้วย: "Implement feature X using a team approach"
```

### Scheduled Tasks
```bash
# รัน command ทุก 5 นาที
/loop 5m /check-status

# การแจ้งเตือนครั้งเดียว
/loop 30m "remind me to check the deploy"
```

---

## อ้างอิงตำแหน่งไฟล์

```
Your Project/
├── .claude/
│   ├── commands/              # Slash commands อยู่ที่นี่
│   ├── agents/                # Subagents อยู่ที่นี่
│   ├── skills/                # Project skills อยู่ที่นี่
│   └── settings.json          # การตั้งค่าโครงการ (hooks เป็นต้น)
├── .mcp.json                  # การกำหนดค่า MCP (ขอบเขตโครงการ)
├── CLAUDE.md                  # Project memory
└── src/
    └── api/
        └── CLAUDE.md          # Memory เฉพาะไดเรกทอรี

User Home/
├── .claude/
│   ├── commands/              # Personal commands
│   ├── agents/                # Personal agents
│   ├── skills/                # Personal skills
│   ├── hooks/                 # Hook scripts
│   ├── settings.json          # User settings
│   ├── managed-settings.d/    # Managed settings (enterprise/org)
│   └── CLAUDE.md              # Personal memory
└── .claude.json               # Personal MCP config (ขอบเขตผู้ใช้)
```

---

## ค้นหาตัวอย่าง

### ตามหมวดหมู่
- **Slash Commands**: `01-slash-commands/`
- **Memory**: `02-memory/`
- **Skills**: `03-skills/`
- **Subagents**: `04-subagents/`
- **MCP**: `05-mcp/`
- **Hooks**: `06-hooks/`
- **Plugins**: `07-plugins/`
- **Checkpoints**: `08-checkpoints/`
- **Advanced Features**: `09-advanced-features/`
- **CLI**: `10-cli/`

### ตามกรณีใช้งาน
- **ประสิทธิภาพ**: `01-slash-commands/optimize.md`
- **ความปลอดภัย**: `04-subagents/secure-reviewer.md`
- **การทดสอบ**: `04-subagents/test-engineer.md`
- **เอกสาร**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### ตามความซับซ้อน
- **ง่าย**: Slash commands
- **ปานกลาง**: Subagents, Memory
- **ขั้นสูง**: Skills, Hooks
- **ครบวงจร**: Plugins

---

## เส้นทางการเรียนรู้

### วันที่ 1
```bash
# อ่านภาพรวม
cat README.md

# ติดตั้ง command
cp 01-slash-commands/optimize.md .claude/commands/

# ลองใช้งาน
/optimize
```

### วันที่ 2-3
```bash
# ตั้งค่า memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# ติดตั้ง subagent
cp 04-subagents/code-reviewer.md .claude/agents/
```

### วันที่ 4-5
```bash
# ตั้งค่า MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# ลอง MCP commands
/mcp__github__list_prs
```

### สัปดาห์ที่ 2
```bash
# ติดตั้ง skill
cp -r 03-skills/code-review ~/.claude/skills/

# ให้เรียกใช้อัตโนมัติ
# พูดว่า: "Review this code for issues"
```

### สัปดาห์ที่ 3+
```bash
# ติดตั้ง plugin ที่สมบูรณ์
/plugin install pr-review

# ใช้ฟีเจอร์ที่รวมมา
/review-pr
/check-security
/check-tests
```

---

## ฟีเจอร์ใหม่ (มีนาคม 2569)

| ฟีเจอร์ | คำอธิบาย | การใช้งาน |
|---------|-------------|-------|
| **Auto Mode** | การทำงานอัตโนมัติครบวงจรพร้อม background classifier | flag `--enable-auto-mode`, `Shift+Tab` เพื่อสลับโหมด |
| **Channels** | การเชื่อมต่อ Discord และ Telegram | flag `--channels`, Discord/Telegram bots |
| **Voice Dictation** | พูด commands และบริบทให้ Claude | command `/voice` |
| **Hooks (28 events)** | ระบบ hook ที่ขยายพร้อม 5 ประเภท | ประเภท hook: command, http, mcp_tool, prompt, agent |
| **MCP Elicitation** | MCP servers สามารถร้องขอ input จากผู้ใช้ขณะ runtime | แจ้งเตือนอัตโนมัติเมื่อ server ต้องการการชี้แจง |
| **Plugin LSP** | รองรับ Language Server Protocol สำหรับ plugins | `userConfig`, ตัวแปร `${CLAUDE_PLUGIN_DATA}` |
| **Remote Control** | ควบคุม Claude Code ผ่าน WebSocket API | `claude --remote` สำหรับการเชื่อมต่อภายนอก |
| **Web Sessions** | อินเทอร์เฟส Claude Code บนเบราว์เซอร์ | `claude web` เพื่อเปิด |
| **Desktop App** | แอปพลิเคชัน desktop แบบ native | ดาวน์โหลดจาก claude.ai/download |
| **Task List** | จัดการ background tasks | `/task list`, `/task status <id>` |
| **Auto Memory** | บันทึก memory อัตโนมัติจากการสนทนา | Claude บันทึกบริบทสำคัญใน CLAUDE.md โดยอัตโนมัติ |
| **Git Worktrees** | พื้นที่ทำงานแยกสำหรับการพัฒนาแบบขนาน | `/worktree` เพื่อสร้างพื้นที่ทำงานแยก |
| **Model Selection** | สลับระหว่าง Sonnet 4.6, Opus 4.7, และ Haiku 4.5 | `/model` หรือ flag `--model` |
| **Agent Teams** | ประสานงาน agent หลายตัวในงาน | เปิดใช้ด้วยตัวแปรสภาพแวดล้อม `CLAUDE_AGENT_TEAMS=1` |
| **Scheduled Tasks** | งานที่เกิดซ้ำด้วย `/loop` | `/loop 5m /command` หรือเครื่องมือ CronCreate |
| **Chrome Integration** | การทำงานอัตโนมัติบนเบราว์เซอร์ | flag `--chrome` หรือ command `/chrome` |
| **Keyboard Customization** | keybindings แบบกำหนดเอง | command `/keybindings` |

---

## เคล็ดลับ

### การปรับแต่ง
- เริ่มต้นด้วยตัวอย่างตามที่เป็นอยู่
- แก้ไขให้เหมาะกับความต้องการของคุณ
- ทดสอบก่อนแชร์กับทีม
- ใช้ version control สำหรับการกำหนดค่า

### แนวปฏิบัติที่ดี
- ใช้ memory สำหรับมาตรฐานทีม
- ใช้ plugins สำหรับ workflow ครบวงจร
- ใช้ subagents สำหรับงานที่ซับซ้อน
- ใช้ slash commands สำหรับงานรวดเร็ว

### การแก้ไขปัญหา
```bash
# ตรวจสอบตำแหน่งไฟล์
ls -la .claude/commands/
ls -la .claude/agents/

# ตรวจสอบ YAML syntax
head -20 .claude/agents/code-reviewer.md

# ทดสอบการเชื่อมต่อ MCP
echo $GITHUB_TOKEN
```

---

## เมทริกซ์ฟีเจอร์

| ความต้องการ | ใช้สิ่งนี้ | ตัวอย่าง |
|------|----------|---------|
| ทางลัดด่วน | Slash Command (60+) | `01-slash-commands/optimize.md` |
| มาตรฐานทีม | Memory | `02-memory/project-CLAUDE.md` |
| workflow อัตโนมัติ | Skill | `03-skills/code-review/` |
| งานเฉพาะทาง | Subagent | `04-subagents/code-reviewer.md` |
| ข้อมูลภายนอก | MCP (+ Elicitation) | `05-mcp/github-mcp.json` |
| การทำงานอัตโนมัติตามเหตุการณ์ | Hook (28 events, 5 ประเภท) | `06-hooks/pre-commit.sh` |
| โซลูชันครบวงจร | Plugin (+ รองรับ LSP) | `07-plugins/pr-review/` |
| การทดลองที่ปลอดภัย | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| อัตโนมัติครบวงจร | Auto Mode | `--enable-auto-mode` หรือ `Shift+Tab` |
| การเชื่อมต่อแชท | Channels | `--channels` (Discord, Telegram) |
| CI/CD pipeline | CLI | `10-cli/README.md` |

---

## ลิงก์ด่วน

- **คู่มือหลัก**: `README.md`
- **ดัชนีสมบูรณ์**: `INDEX.md`
- **คู่มือต้นฉบับ**: `claude_concepts_guide.md`

---

## คำถามที่พบบ่อย

**ถ: ควรใช้อะไร?**
ตอบ: เริ่มต้นด้วย slash commands แล้วเพิ่มฟีเจอร์ตามความต้องการ

**ถ: รวมฟีเจอร์ได้หรือไม่?**
ตอบ: ได้ ฟีเจอร์เหล่านี้ทำงานร่วมกัน Memory + Commands + MCP = ทรงพลัง

**ถ: แชร์กับทีมอย่างไร?**
ตอบ: commit ไดเรกทอรี `.claude/` ไปยัง git

**ถ: เกี่ยวกับข้อมูลลับ?**
ตอบ: ใช้ environment variables ไม่ hardcode ข้อมูลลับ

**ถ: สามารถแก้ไขตัวอย่างได้หรือไม่?**
ตอบ: แน่นอน ตัวอย่างเหล่านี้เป็น template สำหรับปรับแต่ง

---

## รายการตรวจสอบ

รายการตรวจสอบสำหรับการเริ่มต้น:

- [ ] อ่าน `README.md`
- [ ] ติดตั้ง slash command 1 รายการ
- [ ] ลองใช้ command
- [ ] สร้าง project `CLAUDE.md`
- [ ] ติดตั้ง subagent 1 รายการ
- [ ] ตั้งค่าการเชื่อมต่อ MCP 1 รายการ
- [ ] ติดตั้ง skill 1 รายการ
- [ ] ลอง plugin ที่สมบูรณ์
- [ ] ปรับแต่งตามความต้องการ
- [ ] แชร์กับทีม

---

**เริ่มต้นด่วน**: `cat README.md`

**ดัชนีสมบูรณ์**: `cat INDEX.md`

**บัตรนี้**: เก็บไว้ใกล้ตัวเพื่อการอ้างอิงด่วน!

---
**อัปเดตล่าสุด**: 6 พฤษภาคม 2569
**Claude Code Version**: 2.1.131
**แหล่งที่มา**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/commands
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
**Model ที่รองรับ**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
