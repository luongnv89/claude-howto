<!-- i18n-source: INDEX.md -->
<!-- i18n-date: 2026-05-18 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code Examples - ดัชนีรายการสมบูรณ์

เอกสารนี้รวบรวมดัชนีของไฟล์ตัวอย่างทั้งหมด จัดหมวดหมู่ตามประเภทของฟีเจอร์

## สถิติสรุป

- **จำนวนไฟล์ทั้งหมด**: 100+ ไฟล์
- **หมวดหมู่**: 10 หมวดหมู่ฟีเจอร์
- **Plugin**: 3 plugin สมบูรณ์
- **Skill**: 6 skill สมบูรณ์
- **Hook**: 8 hook ตัวอย่าง
- **พร้อมใช้งาน**: ตัวอย่างทั้งหมด

---

## 01. Slash Commands (10 ไฟล์)

ทางลัดที่เรียกใช้โดยผู้ใช้สำหรับ workflow ที่ใช้บ่อย

| ไฟล์ | คำอธิบาย | กรณีใช้งาน |
|------|-------------|----------|
| `optimize.md` | เครื่องมือวิเคราะห์การปรับปรุงโค้ด | ค้นหาปัญหาด้านประสิทธิภาพ |
| `pr.md` | การเตรียม pull request | การทำงานอัตโนมัติสำหรับ PR |
| `generate-api-docs.md` | เครื่องมือสร้างเอกสาร API | สร้างเอกสาร API |
| `commit.md` | ผู้ช่วยเขียน commit message | commit ที่เป็นมาตรฐาน |
| `setup-ci-cd.md` | การตั้งค่า CI/CD pipeline | การทำงานอัตโนมัติสำหรับ DevOps |
| `push-all.md` | push การเปลี่ยนแปลงทั้งหมด | workflow การ push อย่างรวดเร็ว |
| `unit-test-expand.md` | ขยายความครอบคลุมของ unit test | การทดสอบอัตโนมัติ |
| `doc-refactor.md` | การปรับโครงสร้างเอกสาร | การปรับปรุงเอกสาร |
| `pr-slash-command.png` | ตัวอย่างภาพหน้าจอ | อ้างอิงภาพ |
| `README.md` | เอกสารประกอบ | คู่มือการตั้งค่าและใช้งาน |

**เส้นทางการติดตั้ง**: `.claude/commands/`

**การใช้งาน**: `/optimize`, `/pr`, `/generate-api-docs`, `/commit`, `/setup-ci-cd`, `/push-all`, `/unit-test-expand`, `/doc-refactor`

---

## 02. Memory (6 ไฟล์)

บริบทถาวรและมาตรฐานโครงการ

| ไฟล์ | คำอธิบาย | ขอบเขต | ตำแหน่ง |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | มาตรฐานโครงการสำหรับทีม | ระดับโครงการ | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | กฎเฉพาะสำหรับ API | ระดับไดเรกทอรี | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | ความชอบส่วนตัว | ระดับผู้ใช้ | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | ภาพหน้าจอ: memory ที่บันทึก | - | อ้างอิงภาพ |
| `memory-ask-claude.png` | ภาพหน้าจอ: ถาม Claude | - | อ้างอิงภาพ |
| `README.md` | เอกสารประกอบ | - | อ้างอิง |

**การติดตั้ง**: คัดลอกไปยังตำแหน่งที่เหมาะสม

**การใช้งาน**: โหลดโดยอัตโนมัติโดย Claude

---

## 03. Skills (28 ไฟล์)

ความสามารถที่เรียกใช้โดยอัตโนมัติพร้อม script และ template

### Code Review Skill (5 ไฟล์)
```
code-review/
├── SKILL.md                          # คำนิยาม skill
├── scripts/
│   ├── analyze-metrics.py            # เครื่องมือวิเคราะห์ metrics ของโค้ด
│   └── compare-complexity.py         # การเปรียบเทียบความซับซ้อน
└── templates/
    ├── review-checklist.md           # checklist การตรวจสอบ
    └── finding-template.md           # template บันทึกผลการตรวจสอบ
```

**วัตถุประสงค์**: การตรวจสอบโค้ดอย่างครอบคลุมด้านความปลอดภัย ประสิทธิภาพ และคุณภาพ

**เรียกใช้โดยอัตโนมัติ**: เมื่อตรวจสอบโค้ด

---

### Brand Voice Skill (4 ไฟล์)
```
brand-voice/
├── SKILL.md                          # คำนิยาม skill
├── templates/
│   ├── email-template.txt            # รูปแบบอีเมล
│   └── social-post-template.txt      # รูปแบบโซเชียลมีเดีย
└── tone-examples.md                  # ตัวอย่างข้อความ
```

**วัตถุประสงค์**: รักษาความสอดคล้องของ brand voice ในการสื่อสาร

**เรียกใช้โดยอัตโนมัติ**: เมื่อสร้างเนื้อหาการตลาด

---

### Documentation Generator Skill (2 ไฟล์)
```
doc-generator/
├── SKILL.md                          # คำนิยาม skill
└── generate-docs.py                  # Python doc extractor
```

**วัตถุประสงค์**: สร้างเอกสาร API ที่ครอบคลุมจากซอร์สโค้ด

**เรียกใช้โดยอัตโนมัติ**: เมื่อสร้างหรืออัปเดตเอกสาร API

---

### Refactor Skill (5 ไฟล์)
```
refactor/
├── SKILL.md                          # คำนิยาม skill
├── scripts/
│   ├── analyze-complexity.py         # เครื่องมือวิเคราะห์ความซับซ้อน
│   └── detect-smells.py              # เครื่องมือตรวจจับ code smells
├── references/
│   ├── code-smells.md                # แคตาล็อก code smells
│   └── refactoring-catalog.md        # รูปแบบการ refactor
└── templates/
    └── refactoring-plan.md           # template แผนการ refactor
```

**วัตถุประสงค์**: การ refactor โค้ดอย่างเป็นระบบพร้อมการวิเคราะห์ความซับซ้อน

**เรียกใช้โดยอัตโนมัติ**: เมื่อทำการ refactor โค้ด

---

### Claude MD Skill (1 ไฟล์)
```
claude-md/
└── SKILL.md                          # คำนิยาม skill
```

**วัตถุประสงค์**: จัดการและปรับปรุงไฟล์ CLAUDE.md

---

### Blog Draft Skill (3 ไฟล์)
```
blog-draft/
├── SKILL.md                          # คำนิยาม skill
└── templates/
    ├── draft-template.md             # template ร่างบล็อก
    └── outline-template.md           # template โครงร่างบล็อก
```

**วัตถุประสงค์**: ร่างบล็อกโพสต์ด้วยโครงสร้างที่สอดคล้องกัน

**รวมถึง**: `README.md` - ภาพรวมและคู่มือการใช้งาน skill

**เส้นทางการติดตั้ง**: `~/.claude/skills/` หรือ `.claude/skills/`

---

## 04. Subagents (9 ไฟล์)

ผู้ช่วย AI เฉพาะทางพร้อมความสามารถที่กำหนดเอง

| ไฟล์ | คำอธิบาย | เครื่องมือ | กรณีใช้งาน |
|------|-------------|-------|----------|
| `code-reviewer.md` | การวิเคราะห์คุณภาพโค้ด | read, grep, diff, lint_runner | การตรวจสอบอย่างครอบคลุม |
| `test-engineer.md` | การวิเคราะห์ความครอบคลุมของการทดสอบ | read, write, bash, grep | การทดสอบอัตโนมัติ |
| `documentation-writer.md` | การสร้างเอกสาร | read, write, grep | การสร้างเอกสาร |
| `secure-reviewer.md` | การตรวจสอบความปลอดภัย (อ่านอย่างเดียว) | read, grep | การตรวจสอบความปลอดภัย |
| `implementation-agent.md` | การพัฒนาฟีเจอร์ครบวงจร | read, write, bash, grep, edit, glob | การพัฒนาฟีเจอร์ |
| `debugger.md` | ผู้เชี่ยวชาญการหาข้อบกพร่อง | read, bash, grep | การสืบสวนข้อบกพร่อง |
| `data-scientist.md` | ผู้เชี่ยวชาญการวิเคราะห์ข้อมูล | read, write, bash | workflow ด้านข้อมูล |
| `clean-code-reviewer.md` | มาตรฐาน clean code | read, grep | คุณภาพโค้ด |
| `README.md` | เอกสารประกอบ | - | คู่มือการตั้งค่าและใช้งาน |

**เส้นทางการติดตั้ง**: `.claude/agents/`

**การใช้งาน**: มอบหมายโดยอัตโนมัติโดย agent หลัก

---

## 05. MCP Protocol (5 ไฟล์)

การเชื่อมต่อกับเครื่องมือและ API ภายนอก

| ไฟล์ | คำอธิบาย | เชื่อมต่อกับ | กรณีใช้งาน |
|------|-------------|-----------------|----------|
| `github-mcp.json` | การเชื่อมต่อ GitHub | GitHub API | จัดการ PR/issue |
| `database-mcp.json` | การสืบค้นฐานข้อมูล | PostgreSQL/MySQL | สืบค้นข้อมูลสด |
| `filesystem-mcp.json` | การดำเนินการไฟล์ | ระบบไฟล์ในเครื่อง | จัดการไฟล์ |
| `multi-mcp.json` | เซิร์ฟเวอร์หลายรายการ | GitHub + DB + Slack | การเชื่อมต่อครบวงจร |
| `README.md` | เอกสารประกอบ | - | คู่มือการตั้งค่าและใช้งาน |

**เส้นทางการติดตั้ง**: `.mcp.json` (ขอบเขตโครงการ) หรือ `~/.claude.json` (ขอบเขตผู้ใช้)

**การใช้งาน**: `/mcp__github__list_prs` เป็นต้น

---

## 06. Hooks (9 ไฟล์)

script อัตโนมัติที่ขับเคลื่อนด้วยเหตุการณ์และทำงานโดยอัตโนมัติ

| ไฟล์ | คำอธิบาย | เหตุการณ์ | กรณีใช้งาน |
|------|-------------|-------|----------|
| `format-code.sh` | จัดรูปแบบโค้ดอัตโนมัติ | PreToolUse:Write | การจัดรูปแบบโค้ด |
| `pre-commit.sh` | รันการทดสอบก่อน commit | PreToolUse:Bash | การทดสอบอัตโนมัติ |
| `security-scan.sh` | การสแกนความปลอดภัย | PostToolUse:Write | การตรวจสอบความปลอดภัย |
| `log-bash.sh` | บันทึก bash commands | PostToolUse:Bash | การบันทึก command |
| `validate-prompt.sh` | ตรวจสอบ prompt | PreToolUse | การตรวจสอบ input |
| `notify-team.sh` | ส่งการแจ้งเตือน | Notification | การแจ้งเตือนทีม |
| `context-tracker.py` | ติดตามการใช้งาน context window | PostToolUse | การตรวจสอบ context |
| `context-tracker-tiktoken.py` | ติดตาม context แบบอิงตาม token | PostToolUse | การนับ token แม่นยำ |
| `README.md` | เอกสารประกอบ | - | คู่มือการตั้งค่าและใช้งาน |

**เส้นทางการติดตั้ง**: กำหนดค่าใน `~/.claude/settings.json`

**การใช้งาน**: กำหนดค่าในการตั้งค่า ทำงานโดยอัตโนมัติ

**ประเภท Hook** (5 ประเภท 28 เหตุการณ์):
- Tool Hooks: PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest
- Session Hooks: SessionStart, SessionEnd, Stop, StopFailure, SubagentStart, SubagentStop
- Task Hooks: UserPromptSubmit, TaskCompleted, TaskCreated, TeammateIdle
- Lifecycle Hooks: ConfigChange, CwdChanged, FileChanged, PreCompact, PostCompact, WorktreeCreate, WorktreeRemove, Notification, InstructionsLoaded, Elicitation, ElicitationResult

---

## 07. Plugins (3 plugin สมบูรณ์ 40 ไฟล์)

คอลเลกชัน feature ที่รวมเป็นชุดเดียวกัน

### PR Review Plugin (10 ไฟล์)
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # plugin manifest
├── commands/
│   ├── review-pr.md                  # การตรวจสอบอย่างครอบคลุม
│   ├── check-security.md             # การตรวจสอบความปลอดภัย
│   └── check-tests.md                # การตรวจสอบความครอบคลุมของการทดสอบ
├── agents/
│   ├── security-reviewer.md          # ผู้เชี่ยวชาญด้านความปลอดภัย
│   ├── test-checker.md               # ผู้เชี่ยวชาญการทดสอบ
│   └── performance-analyzer.md       # ผู้เชี่ยวชาญด้านประสิทธิภาพ
├── mcp/
│   └── github-config.json            # การเชื่อมต่อ GitHub
├── hooks/
│   └── pre-review.js                 # การตรวจสอบก่อน review
└── README.md                         # เอกสารประกอบ plugin
```

**ฟีเจอร์**: การวิเคราะห์ความปลอดภัย ความครอบคลุมของการทดสอบ ผลกระทบต่อประสิทธิภาพ

**Commands**: `/review-pr`, `/check-security`, `/check-tests`

**การติดตั้ง**: `/plugin install pr-review`

---

### DevOps Automation Plugin (15 ไฟล์)
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # plugin manifest
├── commands/
│   ├── deploy.md                     # การ deploy
│   ├── rollback.md                   # การ rollback
│   ├── status.md                     # สถานะระบบ
│   └── incident.md                   # การตอบสนองต่อ incident
├── agents/
│   ├── deployment-specialist.md      # ผู้เชี่ยวชาญการ deploy
│   ├── incident-commander.md         # ผู้ประสานงาน incident
│   └── alert-analyzer.md             # เครื่องมือวิเคราะห์การแจ้งเตือน
├── mcp/
│   └── kubernetes-config.json        # การเชื่อมต่อ Kubernetes
├── hooks/
│   ├── pre-deploy.js                 # การตรวจสอบก่อน deploy
│   └── post-deploy.js                # งานหลัง deploy
├── scripts/
│   ├── deploy.sh                     # การทำงานอัตโนมัติสำหรับ deploy
│   ├── rollback.sh                   # การทำงานอัตโนมัติสำหรับ rollback
│   └── health-check.sh               # การตรวจสอบสุขภาพระบบ
└── README.md                         # เอกสารประกอบ plugin
```

**ฟีเจอร์**: การ deploy Kubernetes, rollback, การตรวจสอบ, การตอบสนองต่อ incident

**Commands**: `/deploy`, `/rollback`, `/status`, `/incident`

**การติดตั้ง**: `/plugin install devops-automation`

---

### Documentation Plugin (14 ไฟล์)
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # plugin manifest
├── commands/
│   ├── generate-api-docs.md          # การสร้างเอกสาร API
│   ├── generate-readme.md            # การสร้าง README
│   ├── sync-docs.md                  # การซิงโครไนซ์เอกสาร
│   └── validate-docs.md              # การตรวจสอบเอกสาร
├── agents/
│   ├── api-documenter.md             # ผู้เชี่ยวชาญเอกสาร API
│   ├── code-commentator.md           # ผู้เชี่ยวชาญ comment โค้ด
│   └── example-generator.md          # ผู้สร้างตัวอย่าง
├── mcp/
│   └── github-docs-config.json       # การเชื่อมต่อ GitHub
├── templates/
│   ├── api-endpoint.md               # template API endpoint
│   ├── function-docs.md              # template เอกสารฟังก์ชัน
│   └── adr-template.md               # template ADR
└── README.md                         # เอกสารประกอบ plugin
```

**ฟีเจอร์**: เอกสาร API, การสร้าง README, การซิงค์เอกสาร, การตรวจสอบ

**Commands**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**การติดตั้ง**: `/plugin install documentation`

**รวมถึง**: `README.md` - ภาพรวมและคู่มือการใช้งาน plugin

---

## 08. Checkpoints และ Rewind (2 ไฟล์)

บันทึกสถานะการสนทนาและสำรวจแนวทางที่แตกต่าง

| ไฟล์ | คำอธิบาย | เนื้อหา |
|------|-------------|---------|
| `README.md` | เอกสารประกอบ | คู่มือ checkpoint ที่ครอบคลุม |
| `checkpoint-examples.md` | ตัวอย่างการใช้งานจริง | การ migrate ฐานข้อมูล, การปรับปรุงประสิทธิภาพ, การวนซ้ำ UI, การหาข้อบกพร่อง |

**แนวคิดหลัก**:
- **Checkpoint**: ภาพรวมของสถานะการสนทนา
- **Rewind**: ย้อนกลับไปยัง checkpoint ก่อนหน้า
- **Branch Point**: สำรวจหลายแนวทาง

**การใช้งาน**:
```
# Checkpoint ถูกสร้างโดยอัตโนมัติพร้อมกับ prompt ของผู้ใช้ทุกครั้ง
# หากต้องการ rewind กด Esc สองครั้งหรือใช้:
/rewind
# จากนั้นเลือก: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, หรือ Never mind
```

**กรณีใช้งาน**:
- ลองใช้การพัฒนาที่แตกต่างกัน
- กู้คืนจากข้อผิดพลาด
- การทดลองที่ปลอดภัย
- เปรียบเทียบวิธีแก้ปัญหา
- การทดสอบ A/B

---

## 09. Advanced Features (3 ไฟล์)

ความสามารถขั้นสูงสำหรับ workflow ที่ซับซ้อน

| ไฟล์ | คำอธิบาย | ฟีเจอร์ |
|------|-------------|---------|
| `README.md` | คู่มือสมบูรณ์ | เอกสารฟีเจอร์ขั้นสูงทั้งหมด |
| `config-examples.json` | ตัวอย่างการกำหนดค่า | 10+ การกำหนดค่าเฉพาะกรณีใช้งาน |
| `planning-mode-examples.md` | ตัวอย่าง planning | REST API, การ migrate ฐานข้อมูล, การ refactor |

**ฟีเจอร์ขั้นสูงที่ครอบคลุม**:

### Planning Mode
- สร้างแผนการพัฒนาโดยละเอียด
- การประมาณเวลาและการประเมินความเสี่ยง
- การแบ่งงานอย่างเป็นระบบ

### Extended Thinking
- การให้เหตุผลเชิงลึกสำหรับปัญหาที่ซับซ้อน
- การวิเคราะห์การตัดสินใจด้านสถาปัตยกรรม
- การประเมิน trade-off

### Background Tasks
- การดำเนินการระยะยาวโดยไม่บล็อก
- workflow การพัฒนาแบบขนาน
- การจัดการและติดตาม task

### Permission Modes
- **default**: ขออนุมัติสำหรับการกระทำที่มีความเสี่ยง
- **acceptEdits**: ยอมรับการแก้ไขไฟล์โดยอัตโนมัติ ขอสำหรับอื่นๆ
- **plan**: การวิเคราะห์แบบอ่านอย่างเดียว ไม่มีการแก้ไข
- **auto**: อนุมัติการกระทำที่ปลอดภัยโดยอัตโนมัติ แจ้งเตือนสำหรับการกระทำที่มีความเสี่ยง
- **dontAsk**: ยอมรับการกระทำทั้งหมดยกเว้นที่มีความเสี่ยงสูง
- **bypassPermissions**: ยอมรับทั้งหมด (ต้องใช้ `--dangerously-skip-permissions`)

### Headless Mode (`claude -p`)
- การเชื่อมต่อ CI/CD
- การดำเนินการงานอัตโนมัติ
- การประมวลผลแบบกลุ่ม

### Session Management
- session การทำงานหลายรายการ
- การสลับและบันทึก session
- ความต่อเนื่องของ session

### Interactive Features
- keyboard shortcuts
- ประวัติ command
- การเติมข้อความอัตโนมัติ
- การป้อนข้อมูลหลายบรรทัด

### Configuration
- การจัดการการตั้งค่าที่ครอบคลุม
- การกำหนดค่าเฉพาะสภาพแวดล้อม
- การปรับแต่งต่อโครงการ

### Scheduled Tasks
- งานที่เกิดซ้ำด้วยคำสั่ง `/loop`
- เครื่องมือ cron: CronCreate, CronList, CronDelete
- workflow ที่เกิดซ้ำโดยอัตโนมัติ

### Chrome Integration
- การทำงานอัตโนมัติบนเบราว์เซอร์ผ่าน headless Chromium
- ความสามารถในการทดสอบและดึงข้อมูลจากเว็บ
- การโต้ตอบกับหน้าเว็บและการดึงข้อมูล

### Remote Control (ขยาย)
- วิธีการเชื่อมต่อและโปรโตคอล
- การพิจารณาด้านความปลอดภัยและแนวทางปฏิบัติที่ดีที่สุด
- ตารางเปรียบเทียบตัวเลือกการเข้าถึงระยะไกล

### Keyboard Customization
- การกำหนดค่า keybinding แบบกำหนดเอง
- การรองรับ chord สำหรับ shortcut หลายปุ่ม
- การเปิดใช้งาน keybinding ตามบริบท

### Desktop App (ขยาย)
- Connector สำหรับการเชื่อมต่อ IDE
- การกำหนดค่า launch.json
- ฟีเจอร์สำหรับองค์กรและการ deploy

---

## 10. CLI Usage (1 ไฟล์)

รูปแบบการใช้งานและอ้างอิง command-line interface

| ไฟล์ | คำอธิบาย | เนื้อหา |
|------|-------------|---------|
| `README.md` | เอกสาร CLI | flags, options และรูปแบบการใช้งาน |

**ฟีเจอร์ CLI หลัก**:
- `claude` - เริ่ม session แบบโต้ตอบ
- `claude -p "prompt"` - โหมด headless/non-interactive
- `claude web` - เปิด session บนเว็บ
- `claude --model` - เลือก model (Sonnet 4.6, Opus 4.7, Haiku 4.5)
- `claude --permission-mode` - กำหนด permission mode
- `claude --remote` - เปิดใช้งาน remote control ผ่าน WebSocket

---

## ไฟล์เอกสาร (13 ไฟล์)

| ไฟล์ | ตำแหน่ง | คำอธิบาย |
|------|----------|-------------|
| `README.md` | `/` | ภาพรวมตัวอย่างหลัก |
| `INDEX.md` | `/` | ดัชนีสมบูรณ์นี้ |
| `QUICK_REFERENCE.md` | `/` | บัตรอ้างอิงด่วน |
| `README.md` | `/01-slash-commands/` | คู่มือ slash commands |
| `README.md` | `/02-memory/` | คู่มือ memory |
| `README.md` | `/03-skills/` | คู่มือ skills |
| `README.md` | `/04-subagents/` | คู่มือ subagents |
| `README.md` | `/05-mcp/` | คู่มือ MCP |
| `README.md` | `/06-hooks/` | คู่มือ hooks |
| `README.md` | `/07-plugins/` | คู่มือ plugins |
| `README.md` | `/08-checkpoints/` | คู่มือ checkpoints |
| `README.md` | `/09-advanced-features/` | คู่มือ advanced features |
| `README.md` | `/10-cli/` | คู่มือ CLI |

---

## แผนผังไฟล์สมบูรณ์

```
claude-howto/
├── README.md                                    # ภาพรวมหลัก
├── INDEX.md                                     # ไฟล์นี้
├── QUICK_REFERENCE.md                           # บัตรอ้างอิงด่วน
├── claude_concepts_guide.md                     # คู่มือต้นฉบับ
│
├── 01-slash-commands/                           # Slash Commands
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # Memory
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # Skills
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # Subagents
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # MCP Protocol
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # Hooks
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # Plugins
│   ├── pr-review/
│   │   └── ...
│   ├── devops-automation/
│   │   └── ...
│   ├── documentation/
│   │   └── ...
│   └── README.md
│
├── 08-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # Advanced Features
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # CLI Usage
    └── README.md
```

---

## เริ่มต้นอย่างรวดเร็วตามกรณีใช้งาน

### คุณภาพโค้ดและการตรวจสอบ
```bash
# ติดตั้ง slash command
cp 01-slash-commands/optimize.md .claude/commands/

# ติดตั้ง subagent
cp 04-subagents/code-reviewer.md .claude/agents/

# ติดตั้ง skill
cp -r 03-skills/code-review ~/.claude/skills/

# หรือติดตั้ง plugin ที่ครบวงจร
/plugin install pr-review
```

### DevOps และการ deploy
```bash
# ติดตั้ง plugin (รวมทุกอย่าง)
/plugin install devops-automation
```

### เอกสาร
```bash
# ติดตั้ง slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# ติดตั้ง subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# ติดตั้ง skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# หรือติดตั้ง plugin ที่ครบวงจร
/plugin install documentation
```

### มาตรฐานทีม
```bash
# ตั้งค่า project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# แก้ไขให้ตรงกับมาตรฐานของทีม
```

### การเชื่อมต่อภายนอก
```bash
# กำหนด environment variables
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# ติดตั้งการกำหนดค่า MCP (ขอบเขตโครงการ)
cp 05-mcp/multi-mcp.json .mcp.json
```

### การทำงานอัตโนมัติและการตรวจสอบ
```bash
# ติดตั้ง hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# กำหนดค่า hooks ในการตั้งค่า (~/.claude/settings.json)
# ดู 06-hooks/README.md
```

### การทดลองที่ปลอดภัย
```bash
# Checkpoint ถูกสร้างโดยอัตโนมัติพร้อมกับ prompt ของผู้ใช้ทุกครั้ง
# หากต้องการ rewind: กด Esc+Esc หรือใช้ /rewind
# จากนั้นเลือกสิ่งที่ต้องการกู้คืนจากเมนู rewind

# ดู 08-checkpoints/README.md สำหรับตัวอย่าง
```

### Workflow ขั้นสูง
```bash
# กำหนดค่า advanced features
# ดู 09-advanced-features/config-examples.json

# ใช้ planning mode
/plan Implement feature X

# ใช้ permission modes
claude --permission-mode plan          # สำหรับการตรวจสอบโค้ด (อ่านอย่างเดียว)
claude --permission-mode acceptEdits   # ยอมรับการแก้ไขโดยอัตโนมัติ
claude --permission-mode auto          # อนุมัติการกระทำที่ปลอดภัยโดยอัตโนมัติ

# รันในโหมด headless สำหรับ CI/CD
claude -p "Run tests and report results"

# รัน background tasks
Run tests in background

# ดู 09-advanced-features/README.md สำหรับคู่มือสมบูรณ์
```

---

## เมทริกซ์ความครอบคลุมฟีเจอร์

| หมวดหมู่ | Commands | Agents | MCP | Hooks | Scripts | Templates | Docs | Images | รวม |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 Slash Commands** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 Memory** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 Skills** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 Subagents** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 Hooks** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 Checkpoints** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 Advanced** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## เส้นทางการเรียนรู้

### ผู้เริ่มต้น (สัปดาห์ที่ 1)
1. อ่าน `README.md`
2. ติดตั้ง slash command 1-2 รายการ
3. สร้างไฟล์ project memory
4. ลองใช้ command พื้นฐาน

### ระดับกลาง (สัปดาห์ที่ 2-3)
1. ตั้งค่า GitHub MCP
2. ติดตั้ง subagent
3. ลองมอบหมายงาน
4. ติดตั้ง skill

### ขั้นสูง (สัปดาห์ที่ 4+)
1. ติดตั้ง plugin ที่ครบวงจร
2. สร้าง slash command แบบกำหนดเอง
3. สร้าง subagent แบบกำหนดเอง
4. สร้าง skill แบบกำหนดเอง
5. สร้าง plugin ของตนเอง

### ผู้เชี่ยวชาญ (สัปดาห์ที่ 5+)
1. ตั้งค่า hooks สำหรับการทำงานอัตโนมัติ
2. ใช้ checkpoints เพื่อการทดลอง
3. กำหนดค่า planning mode
4. ใช้ permission modes อย่างมีประสิทธิภาพ
5. ตั้งค่า headless mode สำหรับ CI/CD
6. เชี่ยวชาญการจัดการ session

---

**อัปเดตล่าสุด**: 6 พฤษภาคม 2569
**Claude Code Version**: 2.1.131
**Model ที่รองรับ**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
**จำนวนตัวอย่างทั้งหมด**: 100+ ไฟล์
**หมวดหมู่**: 10 ฟีเจอร์
