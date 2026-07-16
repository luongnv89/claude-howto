<!-- i18n-source: 09-advanced-features/README.md -->
<!-- i18n-date: 2026-05-09 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Advanced Features

คู่มือครอบคลุมสำหรับความสามารถขั้นสูงของ Claude Code ซึ่งรวมถึง planning mode, extended thinking, auto mode, background task, permission mode, print mode (non-interactive), session management, interactive feature, channel, voice dictation, remote control, web session, desktop app, task list, prompt suggestion, git worktree, sandboxing, managed setting และ configuration

## สารบัญ

1. [ภาพรวม](#ภาพรวม)
2. [Planning Mode](#planning-mode)
3. [Ultraplan (Cloud Plan Drafting)](#ultraplan-cloud-plan-drafting)
4. [Extended Thinking](#extended-thinking)
5. [Auto Mode](#auto-mode)
6. [Background Tasks](#background-tasks)
7. [Monitor Tool (Event-Driven Streams)](#monitor-tool-event-driven-streams)
8. [Scheduled Tasks](#scheduled-tasks)
9. [Permission Modes](#permission-modes)
10. [Headless Mode](#headless-mode)
11. [Session Management](#session-management)
12. [Interactive Features](#interactive-features)
13. [TUI Mode (Fullscreen)](#tui-mode-fullscreen)
14. [Voice Dictation](#voice-dictation)
15. [Channels](#channels)
16. [Chrome Integration](#chrome-integration)
17. [Remote Control](#remote-control)
18. [Web Sessions](#web-sessions)
19. [Desktop App](#desktop-app)
20. [Task List](#task-list)
21. [Prompt Suggestions](#prompt-suggestions)
22. [Git Worktrees](#git-worktrees)
23. [Sandboxing](#sandboxing)
24. [Managed Settings (Enterprise)](#managed-settings-enterprise)
25. [Configuration and Settings](#configuration-and-settings)
26. [Agent Teams](#agent-teams)
27. [Best Practices](#best-practices)
28. [Additional Resources](#additional-resources)

---

## ภาพรวม

Advanced feature ใน Claude Code ขยายความสามารถหลักด้วย planning, reasoning, automation และกลไกการควบคุม feature เหล่านี้เปิดใช้งาน workflow ที่ซับซ้อนสำหรับงานพัฒนาที่ซับซ้อน การตรวจสอบโค้ด automation และการจัดการหลาย session

**Advanced feature หลัก ได้แก่:**
- **Planning Mode**: สร้างแผน implementation โดยละเอียดก่อนเขียนโค้ด
- **Extended Thinking**: การใช้เหตุผลเชิงลึกสำหรับปัญหาที่ซับซ้อน
- **Auto Mode**: background safety classifier ตรวจสอบแต่ละการดำเนินการก่อนการ execute (Research Preview)
- **Background Tasks**: รัน operation ที่ใช้เวลานานโดยไม่บล็อกการสนทนา
- **Permission Modes**: ควบคุมสิ่งที่ Claude ทำได้ (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`)
- **Print Mode**: รัน Claude Code แบบ non-interactive สำหรับ automation และ CI/CD (`claude -p`)
- **Session Management**: จัดการหลาย work session
- **Interactive Features**: keyboard shortcut, multi-line input และ command history
- **Voice Dictation**: push-to-talk voice input พร้อม STT รองรับ 20 ภาษา
- **Channels**: MCP server ส่งข้อความเข้า session ที่กำลังรัน (Research Preview)
- **Remote Control**: ควบคุม Claude Code จาก Claude.ai หรือ Claude app
- **Web Sessions**: รัน Claude Code ในเบราว์เซอร์ที่ claude.ai/code
- **Desktop App**: standalone app สำหรับการตรวจสอบ diff แบบ visual และหลาย session
- **Task List**: การติดตาม task ที่คงทนข้าม context compaction
- **Prompt Suggestions**: คำแนะนำ command อัจฉริยะตาม context
- **Git Worktrees**: isolated worktree branch สำหรับงานแบบ parallel
- **Sandboxing**: การแยก filesystem และ network ระดับ OS
- **Managed Settings**: Enterprise deployment ผ่าน plist, Registry หรือ managed file
- **Configuration**: ปรับแต่งพฤติกรรมด้วยไฟล์ JSON configuration

---

## Planning Mode

Planning mode อนุญาตให้ Claude คิดผ่านงานที่ซับซ้อนก่อน implement สร้างแผนโดยละเอียดที่คุณสามารถตรวจสอบและอนุมัติ

### Planning Mode คืออะไร?

Planning mode เป็นแนวทางสองระยะ:
1. **Planning Phase**: Claude วิเคราะห์งานและสร้างแผน implementation โดยละเอียด
2. **Implementation Phase**: หลังการอนุมัติ Claude ดำเนินการตามแผน

### เมื่อใดที่ควรใช้ Planning Mode

✅ ใช้ planning mode สำหรับ:
- Refactoring หลายไฟล์ที่ซับซ้อน
- การ implement feature ใหม่
- การเปลี่ยนแปลงสถาปัตยกรรม
- Database migration
- การออกแบบ API ใหม่ครั้งใหญ่

❌ ห้ามใช้ planning mode สำหรับ:
- การแก้ bug ธรรมดา
- การเปลี่ยนแปลง formatting
- การแก้ไขไฟล์เดียว
- คำถามด่วน

### การเปิดใช้งาน Planning Mode

**Slash command**:
```bash
/plan Implement user authentication system
```

**CLI flag**:
```bash
claude --permission-mode plan
```

**ตั้งค่าเป็นค่าเริ่มต้น**:
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**Keyboard shortcut**:
- `Shift + Tab` — สลับ permission mode (รวมถึง plan)
- `Alt + M` — สลับ permission mode (Windows/Linux)

### ประโยชน์ของ Planning Mode

- **แนวทาง implementation ที่มีโครงสร้าง**: การแบ่งขั้นตอนการ implement โดยละเอียด
- **ตรวจสอบและอนุมัติ**: อนุมัติหรือปรับแผนก่อนการ execute
- **การระบุความเสี่ยง**: ระบุปัญหาที่อาจเกิดขึ้นก่อนการ implement
- **ระยะที่ชัดเจน**: ระยะการ implement ที่จัดระเบียบและ milestone

### ตัวอย่าง: Feature Implementation

```
User: /plan Add a real-time notification system

Claude: ฉันจะสร้างแผนสำหรับการ implement real-time notification

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

Estimated time: 3-4 hours
Files to modify: 12
New files to create: 8

Ready to proceed? (yes/no/modify plan)

User: yes

Claude: [เริ่ม implement ตามแผน]
```

### การแก้ไขแผน

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[แสดงแผนที่แก้ไขโดยลบ queue ออก]

User: Looks good, proceed

Claude: [Implement แผนที่แก้ไขแล้ว]
```

### Planning Mode Configuration

```bash
# เปิดใช้งาน plan mode ผ่าน CLI
claude --permission-mode plan

# หรือใช้ /plan slash command ใน REPL
/plan Implement user authentication system
```

**Model alias สำหรับ planning**: ใช้ `opusplan` เป็น model alias เพื่อใช้ Opus สำหรับการวางแผนและ Sonnet สำหรับการ execute:

```bash
claude --model opusplan "design and implement the new API"
```

**แก้ไขแผนภายนอก**: กด `Ctrl+G` เพื่อเปิดแผนปัจจุบันใน external editor สำหรับการแก้ไขโดยละเอียด

> **อัปเดต v2.1.112**: ไฟล์แผนตอนนี้ตั้งชื่อตาม prompt ที่สร้างขึ้น (แทนคำสุ่ม) ทำให้ง่ายต่อการเรียกดูและนำกลับมาใช้ซ้ำ

---

## Ultraplan (Cloud Plan Drafting)

> **ใหม่ใน v2.1.101**: Ultraplan ตอนนี้สร้าง Claude Code บน web cloud environment โดยอัตโนมัติในครั้งแรกที่คุณเรียกใช้ — ไม่ต้องตั้งค่าด้วยตนเอง ไม่ต้องรอ container ก่อนเริ่มร่างแผน

> **หมายเหตุ**: Ultraplan เป็น research preview และต้องการ Claude Code v2.1.91 หรือใหม่กว่า

`/ultraplan` ส่งงานวางแผนจาก local CLI ไปยัง Claude Code บน web session ที่รันใน plan mode Claude ร่างแผนในระบบ cloud ขณะที่ terminal ของคุณยังว่างสำหรับงานอื่น จากนั้นคุณตรวจสอบร่างในเบราว์เซอร์และเลือกว่าจะ execute ที่ใด — ใน cloud session เดิมหรือ teleport กลับมาที่ terminal

### สามวิธีในการเปิดใช้งาน

- **Command**: `/ultraplan <prompt>` — การเรียกใช้แบบชัดเจน
- **Keyword**: รวมคำว่า `ultraplan` ใน prompt ปกติและ Claude จะส่งคำขอไปยัง cloud
- **จากแผน local**: หลังจาก Claude เสร็จสิ้นแผน local แล้ว เลือก "No, refine with Ultraplan on Claude Code on the web" ในกล่องโต้ตอบการอนุมัติ

### ตัวอย่างการใช้งาน

```bash
/ultraplan migrate the auth service from sessions to JWTs
```

### ตัวบ่งชี้สถานะ

| สถานะ | ความหมาย |
|---|---|
| `◇ ultraplan` | Claude กำลังวิจัย codebase และร่างแผน |
| `◇ ultraplan needs your input` | Claude มีคำถามขอชี้แจง เปิด session link เพื่อตอบ |
| `◆ ultraplan ready` | แผนพร้อมสำหรับการตรวจสอบในเบราว์เซอร์ |

---

## Extended Thinking

Extended thinking อนุญาตให้ Claude ใช้เวลาคิดเกี่ยวกับปัญหาที่ซับซ้อนมากขึ้นก่อนให้คำตอบ

### การเปิดใช้งาน Extended Thinking

**Keyboard shortcut**:
- `Option + T` (macOS) / `Alt + T` (Windows/Linux) — สลับ extended thinking

**การเปิดใช้งานอัตโนมัติ**:
- เปิดใช้งานโดยค่าเริ่มต้นสำหรับทุก model (Opus 4.7, Sonnet 4.6, Haiku 4.5)
- Opus 4.7: Adaptive reasoning พร้อม effort level: `low` (○), `medium` (◐), `high` (●), `xhigh` (Opus 4.7 เท่านั้น ค่าเริ่มต้นบน Claude Code), `max`

**Custom budget**:
```bash
export MAX_THINKING_TOKENS=1024
```

**Effort level**:
```bash
export CLAUDE_CODE_EFFORT_LEVEL=xhigh   # low, medium, high, xhigh หรือ max
```

**CLI flag**:
```bash
claude --effort high "complex architectural review"
```

**Slash command**:
```
/effort high
```

> **หมายเหตุ:** keyword "ultrathink" ใน prompt เปิดใช้งาน deep reasoning mode

### ประโยชน์ของ Extended Thinking

- **การใช้เหตุผลเชิงลึก**: ใช้เวลาคิดเกี่ยวกับปัญหาที่ซับซ้อนมากขึ้น
- **การตัดสินใจสถาปัตยกรรมที่ดีขึ้น**: ทำการเลือกที่มีข้อมูลครบถ้วนพร้อมการประเมินอย่างครอบคลุม
- **การพิจารณา edge case**: คิดผ่านปัญหาและ scenario ที่อาจเกิดขึ้น
- **การวิเคราะห์อย่างละเอียด**: แนวทางที่มีโครงสร้างสำหรับการแก้ปัญหาที่ซับซ้อน

---

## Auto Mode

Auto Mode เป็น Research Preview permission mode (มีนาคม 2026) ที่ใช้ background safety classifier เพื่อตรวจสอบแต่ละการดำเนินการก่อน execute ช่วยให้ Claude ทำงานแบบ autonomous ขณะบล็อก operation ที่อันตราย

### ข้อกำหนด

- **Plan**: Team, Enterprise หรือ API (ไม่รองรับบน Pro หรือ Max plan)
- **Model**: Claude Sonnet 4.6 หรือ Opus 4.7
- **Provider**: Anthropic API เท่านั้น (ไม่รองรับบน Bedrock, Vertex หรือ Foundry)

### การเปิดใช้งาน Auto Mode

```bash
claude --permission-mode auto
```

หรือตั้งค่าผ่าน config:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### วิธีการทำงานของ Classifier

background classifier ประเมินแต่ละการดำเนินการตามลำดับการตัดสินใจต่อไปนี้:

1. **กฎ Allow/deny** — ตรวจสอบกฎ permission ชัดเจนก่อน
2. **Read-only/edits อนุมัติอัตโนมัติ** — การอ่านและแก้ไขไฟล์ผ่านโดยอัตโนมัติ
3. **Classifier** — background classifier ตรวจสอบการดำเนินการ
4. **Fallback** — ถามผู้ใช้หลังจาก 3 consecutive หรือ 20 total block

### การดำเนินการที่ถูกบล็อกโดยค่าเริ่มต้น

| การดำเนินการที่ถูกบล็อก | ตัวอย่าง |
|----------------|---------|
| Pipe-to-shell install | `curl \| bash` |
| ส่งข้อมูลสำคัญออกภายนอก | API key, credential ผ่าน network |
| Production deploy | Deploy command ที่กำหนดเป้าหมาย production |
| Mass deletion | `rm -rf` บน directory ขนาดใหญ่ |
| IAM change | การแก้ไข permission และ role |
| Force push ไปยัง main | `git push --force origin main` |

---

## Background Tasks

Background task อนุญาตให้ operation ที่ใช้เวลานาน execute โดยไม่บล็อกการสนทนา

### Background Task คืออะไร?

Background task รัน asynchronous ขณะที่คุณทำงานต่อ:
- Test suite ที่ยาว
- Build process
- Database migration
- Deployment script
- Analysis tool

**การใช้งานพื้นฐาน:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # แสดง task ทั้งหมด
/task status bg-1234 # ตรวจสอบความคืบหน้า
/task show bg-1234   # ดู output
/task cancel bg-1234 # ยกเลิก task
```

### การกำหนดค่า

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## Monitor Tool (Event-Driven Streams)

> **ใหม่ใน v2.1.98**: Monitor tool ให้ Claude ดู command background ที่ stdout และตอบสนองทันทีที่ event ที่ match ปรากฏ — แทนที่ polling loop และ `sleep` สำหรับการรอ process ที่ใช้เวลานาน

### สองรูปแบบที่พบบ่อย

**Stream filter** ดู output ต่อเนื่องจาก source ที่รันตลอด:

```bash
tail -f /var/log/app.log | grep --line-buffered "ERROR"
```

**Poll-and-emit filter** ตรวจสอบ source เป็นระยะและ emit เฉพาะเมื่อมีการเปลี่ยนแปลง:

```bash
last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
while true; do
  gh api "repos/owner/repo/issues/123/comments?since=$last" || true
  last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  sleep 30
done
```

> **คำเตือน**: เมื่อ pipe ไปยัง `grep` ให้ใช้ `grep --line-buffered` เสมอ หากไม่มี grep จะ buffer stdout เป็นก้อน 4KB ซึ่งอาจทำให้ event ล่าช้าหลายนาทีบน stream ที่มี traffic ต่ำ

---

## Scheduled Tasks

Scheduled Task ให้คุณรัน prompt โดยอัตโนมัติตามกำหนดการซ้ำหรือเป็น one-time reminder Task ถูก scope ไปที่ session — รันขณะที่ Claude Code active และถูกล้างเมื่อ session สิ้นสุด มีให้ใช้ตั้งแต่ v2.1.72+

### คำสั่ง `/loop`

```bash
# interval ชัดเจน
/loop 5m check if the deployment finished

# ภาษาธรรมชาติ
/loop check build status every 30 minutes
```

### One-time reminder

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### ขีดจำกัดและพฤติกรรม

- สูงสุด **50 scheduled task** ต่อ session
- Session-scoped — ถูกล้างเมื่อ session สิ้นสุด
- Recurring task หมดอายุอัตโนมัติหลัง **3 วัน**
- Task fire เฉพาะขณะที่ Claude Code รัน — ไม่มี catch-up สำหรับ fire ที่พลาด

### Cloud Scheduled Tasks

ใช้ `/schedule` เพื่อสร้าง Cloud scheduled task ที่รันบน Anthropic infrastructure:

```
/schedule daily at 9am run the test suite and report failures
```

### การปิดใช้งาน scheduled task

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

---

## Permission Modes

Permission mode ควบคุมการดำเนินการที่ Claude ทำได้โดยไม่ต้องอนุมัติอย่างชัดเจน

### Permission Mode ที่มี

| Mode | พฤติกรรม |
|---|---|
| `default` | อ่านไฟล์เท่านั้น ถามสำหรับการดำเนินการอื่นทั้งหมด |
| `acceptEdits` | อ่านและแก้ไขไฟล์ ถามสำหรับ command |
| `plan` | อ่านไฟล์เท่านั้น (research mode ไม่มีการแก้ไข) |
| `auto` | การดำเนินการทั้งหมดพร้อม background safety classifier (Research Preview) |
| `bypassPermissions` | การดำเนินการทั้งหมด ไม่มีการตรวจสอบ permission (อันตราย) |
| `dontAsk` | เฉพาะ tool ที่อนุมัติล่วงหน้าเท่านั้นที่ execute ที่เหลือถูกปฏิเสธ |

สลับระหว่าง mode ด้วย `Shift+Tab` ใน CLI ตั้งค่าเริ่มต้นด้วย flag `--permission-mode` หรือการตั้งค่า `permissions.defaultMode`

### วิธีการเปิดใช้งาน

**Keyboard shortcut**:
```bash
Shift + Tab  # สลับผ่าน mode ทั้ง 6
```

**Slash command**:
```bash
/plan                  # เข้า plan mode
```

**CLI flag**:
```bash
claude --permission-mode plan
claude --permission-mode auto
```

---

## Headless Mode

Print mode (`claude -p`) อนุญาตให้ Claude Code รันโดยไม่มี interactive input เหมาะสำหรับ automation และ CI/CD นี่คือ non-interactive mode ที่แทนที่ flag `--headless` เดิม

### การรันใน Print Mode (Non-Interactive)

```bash
# รัน task เฉพาะ
claude -p "Run all tests"

# ประมวลผลเนื้อหาที่ pipe
cat error.log | claude -p "Analyze these errors"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### ตัวอย่าง: CI/CD Integration

**GitHub Actions**:
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for code quality, security vulnerabilities,
            performance concerns, and test coverage.
            Output results as JSON" > review.json
```

### Print Mode Configuration

```bash
# จำกัด autonomous turn
claude -p --max-turns 5 "refactor this module"

# Structured JSON output
claude -p --output-format json "analyze this codebase"

# ปิดใช้งาน session persistence
claude -p --no-session-persistence "one-off analysis"
```

---

## Session Management

จัดการหลาย Claude Code session อย่างมีประสิทธิภาพ

### Session Management Commands

| Command | คำอธิบาย |
|---------|-------------|
| `/resume` | Resume การสนทนาตาม ID หรือชื่อ |
| `/rename` | ตั้งชื่อ session ปัจจุบัน |
| `/fork` | Fork session ปัจจุบันเป็น branch ใหม่ |
| `claude -c` | ต่อ conversation ล่าสุด |
| `claude -r "session"` | Resume session ตามชื่อหรือ ID |

### การ Resume Session

**ต่อ conversation ล่าสุด**:
```bash
claude -c
```

**Resume session ที่ตั้งชื่อ**:
```bash
claude -r "auth-refactor" "finish this PR"
```

### Session Recap (v2.1.108)

เมื่อคุณกลับมาที่ session หลังจากห่างไป Claude สามารถแสดงสรุปสั้น ๆ ของสิ่งที่ดำเนินการไป

```bash
/recap                                 # trigger recap ด้วยตนเอง
/config                                # สลับ auto-recap เปิด/ปิด
```

---

## Interactive Features

### Keyboard Shortcuts

| Shortcut | คำอธิบาย |
|----------|-------------|
| `Ctrl+C` | ยกเลิก input/generation ปัจจุบัน |
| `Ctrl+D` | ออก Claude Code |
| `Ctrl+G` | แก้ไขแผนใน external editor |
| `Ctrl+L` | ล้างหน้าจอ terminal |
| `Ctrl+O` | สลับ verbose output (ดู reasoning) |
| `Ctrl+R` | Reverse search history (ค้นหาทั่วทุกโครงการ v2.1.129+) |
| `Ctrl+T` | สลับ task list view |
| `Ctrl+B` | Background running tasks |
| `Esc+Esc` | Rewind โค้ด/การสนทนา |
| `Shift+Tab` / `Alt+M` | สลับ permission mode |
| `Option+P` / `Alt+P` | สลับ model |
| `Option+T` / `Alt+T` | สลับ extended thinking |

### การปรับแต่ง keybinding

สร้าง keyboard shortcut แบบ custom โดยรัน `/keybindings` ซึ่งเปิด `~/.claude/keybindings.json` สำหรับการแก้ไข (v2.1.18+)

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    }
  ]
}
```

### Vim Mode

เปิดใช้งาน Vi/Vim keybinding สำหรับการแก้ไขข้อความ:

- เปิดใช้งานผ่าน `/config` (สลับ "Editor / Vim mode") หรือใน `~/.claude/settings.json` ภายใต้ `editorMode: "vim"`
- Visual modes (v2.1.118+): `v` สำหรับ Visual, `V` สำหรับ VISUAL-LINE

---

## TUI Mode (Fullscreen)

> **ใหม่ใน v2.1.110**

TUI (Text User Interface) mode แสดง Claude Code แบบ fullscreen พร้อม output แบบ flicker-free — เหมาะสำหรับ terminal multiplexer เช่น tmux หรือ iTerm2 split pane

```bash
/tui          # สลับจากภายใน session
claude --tui  # เริ่มโดยตรงใน TUI mode
```

---

## Voice Dictation

Voice Dictation ให้ push-to-talk voice input สำหรับ Claude Code

```
/voice
```

| Feature | คำอธิบาย |
|---------|-------------|
| **Push-to-talk** | กดค้างเพื่อบันทึก ปล่อยเพื่อส่ง |
| **20 ภาษา** | Speech-to-text รองรับ 20 ภาษา |
| **Custom keybinding** | กำหนดค่า push-to-talk key ผ่าน `/keybindings` |
| **ข้อกำหนด account** | ต้องการ Claude.ai account สำหรับ STT processing |

---

## Channels

Channels เป็น Research Preview feature ที่ส่ง event จาก external service เข้า Claude Code session ที่กำลังรัน ผ่าน MCP server source ได้แก่ Telegram, Discord, iMessage และ arbitrary webhook

```bash
# Subscribe ไปยัง channel plugin เมื่อ startup
claude --channels discord,telegram
```

| Integration | คำอธิบาย |
|-------------|-------------|
| **Discord** | รับและตอบสนองต่อข้อความ Discord ใน session |
| **Telegram** | รับและตอบสนองต่อข้อความ Telegram ใน session |
| **iMessage** | รับการแจ้งเตือน iMessage ใน session |
| **Webhooks** | รับ event จาก webhook source ที่กำหนดเอง |

---

## Chrome Integration

Chrome Integration เชื่อมต่อ Claude Code กับ Chrome หรือ Microsoft Edge browser สำหรับ web automation และ debugging แบบ live

```bash
claude --chrome      # เปิดใช้งาน Chrome connection
claude --no-chrome   # ปิดใช้งาน Chrome connection
```

| ความสามารถ | คำอธิบาย |
|------------|-------------|
| **Live debugging** | อ่าน console log ตรวจสอบ DOM element debug JavaScript แบบ real time |
| **Design verification** | เปรียบเทียบหน้าที่ render กับ design mockup |
| **Form validation** | ทดสอบการส่ง form input validation และการจัดการ error |
| **Web app testing** | Interact กับ app ที่ authenticate แล้ว (Gmail, Google Docs, Notion เป็นต้น) |
| **Data extraction** | Scrape และประมวลผลเนื้อหาจากหน้าเว็บ |
| **Session recording** | บันทึก browser interaction เป็นไฟล์ GIF |

---

## Remote Control

Remote Control ให้คุณต่อ Claude Code session ที่รันบนเครื่อง local จากโทรศัพท์ tablet หรือเบราว์เซอร์ใดก็ได้ Local session ของคุณยังคงรันบนเครื่อง — ไม่มีอะไรย้ายไปยัง cloud รองรับบน Pro, Max, Team และ Enterprise plan (v2.1.51+)

```bash
# เริ่มด้วยชื่อ session เริ่มต้น
claude remote-control

# เริ่มด้วยชื่อ custom
claude remote-control --name "Auth Refactor"
```

### ความปลอดภัย

- **ไม่เปิด inbound port** บนเครื่องของคุณ
- **เฉพาะ outbound HTTPS** ผ่าน TLS
- **Scoped credential** — token ที่มีอายุสั้นและ scope แคบหลาย token
- **Session isolation** — แต่ละ remote session เป็นอิสระ

---

## Web Sessions

Web Session อนุญาตให้คุณรัน Claude Code โดยตรงในเบราว์เซอร์ที่ claude.ai/code หรือสร้าง web session จาก CLI

```bash
# สร้าง web session ใหม่จาก CLI
claude --remote "implement the new API endpoints"
```

**Resume Web Session ใน local**:

```bash
claude --teleport
```

---

## Desktop App

Desktop App ให้ standalone application พร้อม visual diff review, parallel session และ integrated connector รองรับ macOS และ Windows (Pro, Max, Team และ Enterprise plan)

### Core features

| Feature | คำอธิบาย |
|---------|-------------|
| **Diff view** | Visual review ทีละไฟล์พร้อม inline comment; Claude อ่าน comment และแก้ไข |
| **App preview** | Auto-start dev server พร้อม embedded browser สำหรับ live verification |
| **PR monitoring** | GitHub CLI integration พร้อม auto-fix CI failure และ auto-merge เมื่อ check ผ่าน |
| **Parallel sessions** | หลาย session ใน sidebar พร้อม automatic Git worktree isolation |
| **Scheduled tasks** | Recurring task (hourly, daily, weekdays, weekly) ที่รันขณะ app เปิดอยู่ |
| **Rich rendering** | การ render code, markdown และ diagram พร้อม syntax highlighting |

### Connectors

| Connector | ความสามารถ |
|-----------|------------|
| **GitHub** | PR monitoring, issue tracking, code review |
| **Slack** | การแจ้งเตือน, channel context |
| **Linear** | Issue tracking, sprint management |
| **Notion** | Documentation, knowledge base access |
| **Asana** | Task management, project tracking |
| **Calendar** | Schedule awareness, meeting context |

---

## Task List

Task List feature ให้การติดตาม task ที่คงทนซึ่งยังคงอยู่แม้ context compaction (เมื่อ conversation history ถูกตัดเพื่อให้พอดีกับ context window)

กด `Ctrl+T` เพื่อสลับ task list view เปิด/ปิดระหว่าง session

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

---

## Prompt Suggestions

Prompt Suggestion แสดงตัวอย่าง command แบบ grayed-out ตาม git history และ conversation context ปัจจุบัน

- กด `Tab` เพื่อยอมรับ suggestion
- กด `Enter` เพื่อยอมรับและส่งทันที

**ปิดใช้งาน**:
```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git Worktrees

Git Worktree อนุญาตให้คุณเริ่ม Claude Code ใน isolated worktree เปิดใช้งานการทำงานแบบ parallel บน branch ต่างกันโดยไม่ต้อง stash หรือ switch

```bash
# เริ่ม Claude Code ใน isolated worktree
claude --worktree
# หรือ
claude -w
```

Worktree สร้างที่:
```
<repo>/.claude/worktrees/<name>
```

**Sparse Checkout สำหรับ Monorepo**:

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

---

## Sandboxing

Sandboxing ให้การแยก filesystem และ network ระดับ OS สำหรับ Bash command ที่ Claude Code execute เป็น complement ของ permission rule และให้ security layer เพิ่มเติม

```bash
claude --sandbox       # เปิดใช้งาน sandboxing
claude --no-sandbox    # ปิดใช้งาน sandboxing
```

| Setting | คำอธิบาย |
|---------|-------------|
| `sandbox.enabled` | เปิด/ปิด sandboxing |
| `sandbox.filesystem.allowWrite` | Path ที่อนุญาตสำหรับการเขียน |
| `sandbox.filesystem.allowRead` | Path ที่อนุญาตสำหรับการอ่าน |
| `sandbox.network.allowedDomains` | Domain ที่ process ที่เรียกใช้จาก Bash สามารถเข้าถึงได้ |
| `sandbox.network.deniedDomains` | Domain ที่บล็อกแม้ wildcard จะอนุญาต (v2.1.113+) |

---

## Managed Settings (Enterprise)

Managed Setting ช่วยให้ Enterprise administrator deploy Claude Code configuration ทั่วองค์กรโดยใช้เครื่องมือจัดการ platform-native

| Platform | Method | ตั้งแต่ |
|----------|--------|-------|
| macOS | Managed plist files (MDM) | v2.1.51+ |
| Windows | Windows Registry | v2.1.51+ |
| Cross-platform | Managed configuration files | v2.1.51+ |
| Cross-platform | Managed drop-ins (`managed-settings.d/` directory) | v2.1.83+ |

| Setting | คำอธิบาย |
|---------|-------------|
| `disableBypassPermissionsMode` | ป้องกันผู้ใช้จากการเปิดใช้งาน bypass permission |
| `availableModels` | จำกัด model ที่ผู้ใช้สามารถเลือกได้ |
| `allowedChannelPlugins` | ควบคุม channel plugin ที่อนุญาต |
| `autoMode.environment` | กำหนดค่า trusted infrastructure สำหรับ auto mode |

---

## Configuration and Settings

### Environment Variables

```bash
# การเลือก model
export ANTHROPIC_MODEL=claude-opus-4-7

# API configuration
export ANTHROPIC_API_KEY=sk-ant-...

# Thinking configuration
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=xhigh   # low, medium, high, xhigh หรือ max

# Feature toggle
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Agent Teams

Agent Teams เป็น experimental feature ที่เปิดใช้งานให้ Claude Code instance หลายตัว collaborate กันในงาน ปิดใช้งานโดยค่าเริ่มต้น

```bash
# Environment variable
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

### วิธีการทำงานของ Agent Teams

- **team lead** ประสานงานงานโดยรวมและมอบหมายงานย่อยให้ teammate
- **Teammate** ทำงานอิสระ แต่ละตัวมี context window ของตัวเอง
- **shared task list** เปิดใช้งาน self-coordination ระหว่างสมาชิกทีม

| Mode | คำอธิบาย |
|------|-------------|
| `in-process` (default) | Teammate รันภายใน terminal process เดียวกัน |
| `tmux` | Teammate แต่ละตัวได้รับ split pane เฉพาะ (ต้องการ tmux หรือ iTerm2) |
| `auto` | เลือก display mode ที่ดีที่สุดโดยอัตโนมัติ |

---

## Best Practices

### Planning Mode
- ✅ ใช้สำหรับงานหลายขั้นตอนที่ซับซ้อน
- ✅ ตรวจสอบแผนก่อนอนุมัติ
- ✅ แก้ไขแผนเมื่อจำเป็น
- ❌ ห้ามใช้สำหรับงานธรรมดา

### Extended Thinking
- ✅ ใช้สำหรับการตัดสินใจสถาปัตยกรรม
- ✅ ใช้สำหรับการแก้ปัญหาที่ซับซ้อน
- ✅ ตรวจสอบ thinking process
- ❌ ห้ามใช้สำหรับคำถามธรรมดา

### Background Tasks
- ✅ ใช้สำหรับ operation ที่ใช้เวลานาน
- ✅ ติดตามความคืบหน้าของ task
- ✅ จัดการ task failure อย่างเหมาะสม
- ❌ ห้ามเริ่ม concurrent task มากเกินไป

### Permissions
- ✅ ใช้ `plan` สำหรับ code review (read-only)
- ✅ ใช้ `default` สำหรับการพัฒนาแบบ interactive
- ✅ ใช้ `acceptEdits` สำหรับ automation workflow
- ✅ ใช้ `auto` สำหรับการทำงาน autonomous พร้อม safety guardrail
- ❌ ห้ามใช้ `bypassPermissions` เว้นแต่จำเป็นอย่างยิ่ง

---

## Additional Resources

- [Official Interactive Mode Documentation](https://code.claude.com/docs/en/interactive-mode)
- [Official Headless Mode Documentation](https://code.claude.com/docs/en/headless)
- [CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Checkpoints Guide](../08-checkpoints/) — Session management และการ rewind
- [Slash Commands](../01-slash-commands/) — Command reference
- [Memory Guide](../02-memory/) — Persistent context
- [Skills Guide](../03-skills/) — Autonomous capability
- [Subagents Guide](../04-subagents/) — Delegated task execution
- [MCP Guide](../05-mcp/) — External data access
- [Hooks Guide](../06-hooks/) — Event-driven automation
- [Plugins Guide](../07-plugins/) — Bundled extension

---

**Last Updated**: May 6, 2026
**Claude Code Version**: 2.1.131
**Sources**:
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/interactive-mode
- https://code.claude.com/docs/en/settings
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
