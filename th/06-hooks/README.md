<!-- i18n-source: 06-hooks/README.md -->
<!-- i18n-date: 2026-05-08 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks

Hooks คือสคริปต์อัตโนมัติที่ทำงานตอบสนองต่อ event เฉพาะระหว่าง Claude Code session ช่วยให้สามารถทำ automation การตรวจสอบ การจัดการสิทธิ์ และ workflow แบบกำหนดเองได้

## ภาพรวม

Hooks คือการดำเนินการอัตโนมัติ (คำสั่ง shell, HTTP webhooks, LLM prompts, การเรียกใช้เครื่องมือ MCP หรือการประเมิน subagent) ที่ทำงานโดยอัตโนมัติเมื่อเกิด event เฉพาะใน Claude Code Hooks รับข้อมูล JSON และสื่อสารผลลัพธ์ผ่าน exit codes และ JSON output

**ฟีเจอร์หลัก:**
- Automation ที่ขับเคลื่อนด้วย event
- Input/output แบบ JSON
- รองรับ hook types `command`, `http`, `mcp_tool`, `prompt` และ `agent`
- Pattern matching สำหรับ hook เฉพาะเครื่องมือ

## การกำหนดค่า

Hooks ถูกกำหนดค่าในไฟล์ settings ด้วยโครงสร้างเฉพาะ:

- `~/.claude/settings.json` - การตั้งค่าผู้ใช้ (ทุก project)
- `.claude/settings.json` - การตั้งค่า project (แชร์ได้ committed)
- `.claude/settings.local.json` - การตั้งค่า project แบบ local (ไม่ committed)
- Managed policy - การตั้งค่าทั่วทั้งองค์กร
- Plugin `hooks/hooks.json` - hooks ที่มีขอบเขต plugin
- Skill/Agent frontmatter - hooks ช่วงชีวิตของ component

### โครงสร้างการกำหนดค่าพื้นฐาน

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**ฟิลด์หลัก:**

| ฟิลด์ | คำอธิบาย | ตัวอย่าง |
|-------|-------------|---------|
| `matcher` | รูปแบบเพื่อจับคู่ชื่อเครื่องมือ (case-sensitive) | `"Write"`, `"Edit\|Write"`, `"*"` |
| `hooks` | อาร์เรย์ของนิยาม hook | `[{ "type": "command", ... }]` |
| `type` | ประเภท hook: `"command"` (bash), `"prompt"` (LLM), `"http"` (webhook), `"mcp_tool"` (การเรียกใช้เครื่องมือ MCP, v2.1.118+) หรือ `"agent"` (subagent) | `"command"` |
| `command` | คำสั่ง shell ที่จะรัน | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | timeout ที่กำหนดเองเป็นวินาที (ค่าเริ่มต้น 60) | `30` |
| `once` | ถ้า `true` รัน hook เพียงครั้งเดียวต่อ session | `true` |

### รูปแบบ Matcher

| รูปแบบ | คำอธิบาย | ตัวอย่าง |
|---------|-------------|---------|
| สตริงตรงทั้งหมด | จับคู่เครื่องมือเฉพาะ | `"Write"` |
| รูปแบบ Regex | จับคู่หลายเครื่องมือ | `"Edit\|Write"` |
| Wildcard | จับคู่ทุกเครื่องมือ | `"*"` หรือ `""` |
| เครื่องมือ MCP | รูปแบบ server และเครื่องมือ | `"mcp__memory__.*"` |

**ค่า matcher ของ InstructionsLoaded:**

| ค่า Matcher | คำอธิบาย |
|---------------|-------------|
| `session_start` | คำสั่งที่โหลดเมื่อเริ่ม session |
| `nested_traversal` | คำสั่งที่โหลดระหว่าง nested directory traversal |
| `path_glob_match` | คำสั่งที่โหลดผ่าน path glob pattern matching |

## ประเภท Hook

Claude Code รองรับ hook 5 ประเภท:

### Command Hooks

ประเภท hook เริ่มต้น รันคำสั่ง shell และสื่อสารผ่าน JSON stdin/stdout และ exit codes

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

### HTTP Hooks

> เพิ่มในเวอร์ชัน v2.1.63

Webhook endpoints ระยะไกลที่รับ JSON input เดียวกับ command hooks HTTP hooks ส่ง JSON ไปยัง URL และรับการตอบสนอง JSON HTTP hooks ถูกส่งผ่าน sandbox เมื่อเปิดใช้งาน sandboxing การสอดแทรก environment variable ใน URL ต้องการรายการ `allowedEnvVars` ที่ชัดเจนเพื่อความปลอดภัย

```json
{
  "hooks": {
    "PostToolUse": [{
      "type": "http",
      "url": "https://my-webhook.example.com/hook",
      "matcher": "Write"
    }]
  }
}
```

**คุณสมบัติหลัก:**
- `"type": "http"` -- ระบุว่าเป็น HTTP hook
- `"url"` -- URL ของ webhook endpoint
- ส่งผ่าน sandbox เมื่อเปิดใช้งาน sandbox
- ต้องการรายการ `allowedEnvVars` ที่ชัดเจนสำหรับการสอดแทรก environment variable ใน URL

### Prompt Hooks

Prompts ที่ LLM ประเมิน โดยเนื้อหา hook เป็น prompt ที่ Claude ประเมิน ส่วนใหญ่ใช้กับ event `Stop` และ `SubagentStop` สำหรับการตรวจสอบความสมบูรณ์ของงานอย่างชาญฉลาด

```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude completed all requested tasks.",
  "timeout": 30
}
```

LLM ประเมิน prompt และส่งคืนการตัดสินใจที่มีโครงสร้าง

### MCP Tool Hooks

> เพิ่มในเวอร์ชัน v2.1.118

ประเภท `mcp_tool` เรียกใช้เครื่องมือ MCP ที่กำหนดค่าไว้โดยตรง การกำหนดค่าอ้างอิง MCP server และชื่อเครื่องมือแทนคำสั่ง shell หรือ URL ซึ่งมีประโยชน์เมื่อตรรกะการตรวจสอบหรือการตอบสนองอยู่ใน MCP server ที่กำหนดค่าไว้แล้ว

```json
{
  "matcher": "Edit",
  "hooks": [{
    "type": "mcp_tool",
    "server": "my-mcp-server",
    "tool": "validate_edit"
  }]
}
```

**คุณสมบัติหลัก:**
- `"type": "mcp_tool"` -- ระบุว่าเป็น MCP tool hook
- `"server"` -- ชื่อของ MCP server ที่กำหนดค่าไว้
- `"tool"` -- ชื่อเครื่องมือบน server นั้นที่จะเรียกใช้

### Agent Hooks

Hook การตรวจสอบแบบ subagent ที่เปิด agent เฉพาะเพื่อประเมินเงื่อนไขหรือทำการตรวจสอบที่ซับซ้อน ต่างจาก prompt hooks (การประเมิน LLM แบบ single-turn) agent hooks สามารถใช้เครื่องมือและทำการใช้เหตุผลหลายขั้นตอนได้

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

**คุณสมบัติหลัก:**
- `"type": "agent"` -- ระบุว่าเป็น agent hook
- `"prompt"` -- คำอธิบายงานสำหรับ subagent
- agent สามารถใช้เครื่องมือ (Read, Grep, Bash ฯลฯ) เพื่อทำการประเมิน
- ส่งคืนการตัดสินใจที่มีโครงสร้างคล้ายกับ prompt hooks

## Hook Events

Claude Code รองรับ **28 hook events**:

| Event | เมื่อเกิดขึ้น | Matcher Input | สามารถบล็อก | การใช้งานทั่วไป |
|-------|---------------|---------------|-----------|------------|
| **SessionStart** | Session เริ่ม/resume/clear/compact | startup/resume/clear/compact | ไม่ | การตั้งค่าสภาพแวดล้อม |
| **InstructionsLoaded** | หลังโหลด CLAUDE.md หรือไฟล์กฎ | (ไม่มี) | ไม่ | แก้ไข/กรองคำสั่ง |
| **UserPromptSubmit** | ผู้ใช้ส่ง prompt | (ไม่มี) | ใช่ | ตรวจสอบ prompts |
| **UserPromptExpansion** | User prompt ถูกขยาย (เช่น `@` mentions, slash commands) | (ไม่มี) | ใช่ | แปลงหรือตรวจสอบ prompt ที่ขยาย |
| **PreToolUse** | ก่อนรันเครื่องมือ | ชื่อเครื่องมือ | ใช่ (allow/deny/ask) | ตรวจสอบ แก้ไข input |
| **PermissionRequest** | แสดง dialog สิทธิ์ | ชื่อเครื่องมือ | ใช่ | อนุมัติ/ปฏิเสธอัตโนมัติ |
| **PermissionDenied** | ผู้ใช้ปฏิเสธ permission prompt | ชื่อเครื่องมือ | ไม่ | การบันทึก analytics การบังคับใช้นโยบาย |
| **PostToolUse** | หลังเครื่องมือสำเร็จ | ชื่อเครื่องมือ | ไม่ | เพิ่ม context feedback |
| **PostToolUseFailure** | การรันเครื่องมือล้มเหลว | ชื่อเครื่องมือ | ไม่ | การจัดการข้อผิดพลาด การบันทึก |
| **PostToolBatch** | หลังชุดการใช้เครื่องมือเสร็จสิ้น | (ไม่มี) | ไม่ | การรายงานรวม การตรวจสอบเป็นชุด |
| **Notification** | ส่งการแจ้งเตือน | ประเภทการแจ้งเตือน | ไม่ | การแจ้งเตือนแบบกำหนดเอง |
| **SubagentStart** | เปิด subagent | ชื่อประเภท agent | ไม่ | การตั้งค่า subagent |
| **SubagentStop** | Subagent เสร็จสิ้น | ชื่อประเภท agent | ใช่ | การตรวจสอบ subagent |
| **Stop** | Claude ตอบสนองเสร็จสิ้น | (ไม่มี) | ใช่ | การตรวจสอบความสมบูรณ์ของงาน |
| **StopFailure** | ข้อผิดพลาด API สิ้นสุด turn | (ไม่มี) | ไม่ | การกู้คืนข้อผิดพลาด การบันทึก |
| **TeammateIdle** | Teammate ของทีม agent ไม่ได้ใช้งาน | (ไม่มี) | ใช่ | การประสานงาน teammate |
| **TaskCompleted** | งานถูกทำเครื่องหมายว่าเสร็จสิ้น | (ไม่มี) | ใช่ | การดำเนินการหลังงาน |
| **TaskCreated** | งานถูกสร้างผ่าน TaskCreate | (ไม่มี) | ไม่ | การติดตามงาน การบันทึก |
| **ConfigChange** | ไฟล์กำหนดค่าเปลี่ยนแปลง | (ไม่มี) | ใช่ (ยกเว้น policy) | ตอบสนองต่อการอัปเดตการกำหนดค่า |
| **CwdChanged** | ไดเรกทอรีการทำงานเปลี่ยนแปลง | (ไม่มี) | ไม่ | การตั้งค่าเฉพาะไดเรกทอรี |
| **FileChanged** | ไฟล์ที่ติดตามเปลี่ยนแปลง | (ไม่มี) | ไม่ | การติดตามไฟล์ การ build ใหม่ |
| **PreCompact** | ก่อน context compaction | manual/auto | ไม่ | การดำเนินการก่อน compact |
| **PostCompact** | หลัง compaction เสร็จสิ้น | (ไม่มี) | ไม่ | การดำเนินการหลัง compact |
| **WorktreeCreate** | กำลังสร้าง Worktree | (ไม่มี) | ใช่ (ส่งคืน path) | การเริ่มต้น worktree |
| **WorktreeRemove** | กำลังลบ Worktree | (ไม่มี) | ไม่ | การล้างข้อมูล worktree |
| **Elicitation** | MCP server ขอข้อมูลจากผู้ใช้ | (ไม่มี) | ใช่ | การตรวจสอบ input |
| **ElicitationResult** | ผู้ใช้ตอบสนองต่อ elicitation | (ไม่มี) | ใช่ | การประมวลผลการตอบสนอง |
| **SessionEnd** | Session สิ้นสุด | (ไม่มี) | ไม่ | การล้างข้อมูล การบันทึกสุดท้าย |

> **ระยะเวลา PostToolUse (v2.1.119):** Input ของ hook `PostToolUse` และ `PostToolUseFailure` ตอนนี้รวม `duration_ms` ด้วย

### PreToolUse

รันหลังจาก Claude สร้างพารามิเตอร์เครื่องมือและก่อนการประมวลผล ใช้เพื่อตรวจสอบหรือแก้ไข input ของเครื่องมือ

**การกำหนดค่า:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py"
          }
        ]
      }
    ]
  }
}
```

**matchers ทั่วไป:** `Task`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**การควบคุมผลลัพธ์:**
- `permissionDecision`: `"allow"`, `"deny"` หรือ `"ask"`
- `permissionDecisionReason`: คำอธิบายสำหรับการตัดสินใจ
- `updatedInput`: พารามิเตอร์ input เครื่องมือที่แก้ไขแล้ว

### PostToolUse

รันทันทีหลังจากเครื่องมือเสร็จสิ้น ใช้สำหรับการตรวจสอบ การบันทึก หรือให้ context กลับไปยัง Claude

**การกำหนดค่า:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py"
          }
        ]
      }
    ]
  }
}
```

**การควบคุมผลลัพธ์:**
- การตัดสินใจ `"block"` แจ้ง Claude พร้อม feedback
- `additionalContext`: Context ที่เพิ่มสำหรับ Claude

**ฟิลด์ input เพิ่มเติม (v2.1.119):**

| ฟิลด์ | ประเภท | คำอธิบาย |
|-------|------|-------------|
| `duration_ms` | number | เวลาการรันเครื่องมือเป็นมิลลิวินาที ไม่รวมเวลาที่ใช้ใน permission prompts และการรัน PreToolUse hook |

### UserPromptSubmit

รันเมื่อผู้ใช้ส่ง prompt ก่อนที่ Claude จะประมวลผล

**การกำหนดค่า:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py"
          }
        ]
      }
    ]
  }
}
```

**การควบคุมผลลัพธ์:**
- `decision`: `"block"` เพื่อป้องกันการประมวลผล
- `reason`: คำอธิบายถ้าถูกบล็อก
- `additionalContext`: Context ที่เพิ่มใน prompt

### Stop และ SubagentStop

รันเมื่อ Claude ตอบสนองเสร็จสิ้น (Stop) หรือ subagent เสร็จสิ้น (SubagentStop) รองรับการประเมินแบบ prompt-based สำหรับการตรวจสอบความสมบูรณ์ของงานอย่างชาญฉลาด

**ฟิลด์ input เพิ่มเติม:** Hook ทั้ง `Stop` และ `SubagentStop` รับฟิลด์ `last_assistant_message` ใน JSON input ซึ่งประกอบด้วยข้อความสุดท้ายจาก Claude หรือ subagent ก่อนหยุด ซึ่งมีประโยชน์สำหรับการประเมินความสมบูรณ์ของงาน

**การกำหนดค่า:**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Evaluate if Claude completed all requested tasks.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### SubagentStart

รันเมื่อ subagent เริ่มทำงาน matcher input คือชื่อประเภท agent ซึ่งช่วยให้ hooks สามารถกำหนดเป้าหมายประเภท subagent เฉพาะได้

**การกำหนดค่า:**
```json
{
  "hooks": {
    "SubagentStart": [
      {
        "matcher": "code-review",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/subagent-init.sh"
          }
        ]
      }
    ]
  }
}
```

### SessionStart

รันเมื่อ session เริ่มหรือ resume สามารถเก็บ environment variables แบบถาวรได้

**Matchers:** `startup`, `resume`, `clear`, `compact`

**ฟีเจอร์พิเศษ:** ใช้ `CLAUDE_ENV_FILE` เพื่อเก็บ environment variables แบบถาวร (พร้อมใช้งานใน hook `CwdChanged` และ `FileChanged` ด้วย):

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

รันเมื่อ session สิ้นสุดเพื่อทำการล้างข้อมูลหรือการบันทึกสุดท้าย ไม่สามารถบล็อกการสิ้นสุดได้

**ค่าฟิลด์ Reason:**
- `clear` - ผู้ใช้ล้าง session
- `logout` - ผู้ใช้ออกจากระบบ
- `prompt_input_exit` - ผู้ใช้ออกผ่าน prompt input
- `other` - เหตุผลอื่นๆ

**การกำหนดค่า:**
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-cleanup.sh\""
          }
        ]
      }
    ]
  }
}
```

### Notification Event

matchers ที่อัปเดตสำหรับ notification events:
- `permission_prompt` - การแจ้งเตือนคำขอสิทธิ์
- `idle_prompt` - การแจ้งเตือนสถานะไม่ได้ใช้งาน
- `auth_success` - การยืนยันตัวตนสำเร็จ
- `elicitation_dialog` - dialog ที่แสดงให้ผู้ใช้

## Hooks ที่มีขอบเขต Component

Hooks สามารถแนบกับ component เฉพาะ (skills, agents, commands) ใน frontmatter ของพวกเขา:

**ใน SKILL.md, agent.md หรือ command.md:**

```yaml
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/check.sh"
          once: true  # รันเพียงครั้งเดียวต่อ session
---
```

**Events ที่รองรับสำหรับ component hooks:** `PreToolUse`, `PostToolUse`, `Stop`

ซึ่งช่วยให้กำหนด hooks โดยตรงใน component ที่ใช้พวกเขา ทำให้โค้ดที่เกี่ยวข้องอยู่ด้วยกัน

### Hooks ใน Subagent Frontmatter

เมื่อกำหนด `Stop` hook ใน frontmatter ของ subagent จะถูกแปลงโดยอัตโนมัติเป็น `SubagentStop` hook ที่มีขอบเขตต่อ subagent นั้น ซึ่งรับประกันว่า stop hook จะเริ่มทำงานเฉพาะเมื่อ subagent นั้นเสร็จสิ้น

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # Stop hook ด้านบนแปลงอัตโนมัติเป็น SubagentStop สำหรับ subagent นี้
---
```

## PermissionRequest Event

จัดการคำขอสิทธิ์ด้วยรูปแบบ output แบบกำหนดเอง:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow|deny",
      "updatedInput": {},
      "message": "Custom message",
      "interrupt": false
    }
  }
}
```

## Hook Input และ Output

### JSON Input (ผ่าน stdin)

Hooks ทั้งหมดรับ JSON input ผ่าน stdin:

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.js",
    "content": "..."
  },
  "tool_use_id": "toolu_01ABC123...",
  "agent_id": "agent-abc123",
  "agent_type": "main",
  "worktree": "/path/to/worktree"
}
```

**ฟิลด์ทั่วไป:**

| ฟิลด์ | คำอธิบาย |
|-------|-------------|
| `session_id` | ตัวระบุ session ที่ไม่ซ้ำกัน |
| `transcript_path` | Path ไปยังไฟล์ transcript การสนทนา |
| `cwd` | ไดเรกทอรีการทำงานปัจจุบัน |
| `hook_event_name` | ชื่อ event ที่เริ่ม hook |
| `agent_id` | ตัวระบุของ agent ที่รัน hook นี้ |
| `agent_type` | ประเภทของ agent (`"main"` ชื่อประเภท subagent ฯลฯ) |
| `worktree` | Path ไปยัง git worktree ถ้า agent รันใน worktree |

### Exit Codes

| Exit Code | ความหมาย | พฤติกรรม |
|-----------|---------|----------|
| **0** | สำเร็จ | ดำเนินต่อ วิเคราะห์ JSON stdout |
| **2** | ข้อผิดพลาดแบบบล็อก | บล็อกการดำเนินการ แสดง stderr เป็นข้อผิดพลาด |
| **อื่นๆ** | ข้อผิดพลาดแบบไม่บล็อก | ดำเนินต่อ แสดง stderr ใน verbose mode |

### JSON Output (stdout, exit code 0)

```json
{
  "continue": true,
  "stopReason": "Optional message if stopping",
  "suppressOutput": false,
  "systemMessage": "Optional warning message",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "File is in allowed directory",
    "updatedInput": {
      "file_path": "/modified/path.js"
    }
  }
}
```

> **ขอบเขต (v2.1.121+):** `hookSpecificOutput.updatedToolOutput` ตอนนี้ใช้ได้กับ **เครื่องมือทั้งหมด** ไม่ใช่เฉพาะเครื่องมือ MCP `PostToolUse` hook บน `Bash`, `Edit`, `Read` ฯลฯ สามารถเขียน output ของเครื่องมือใหม่ก่อนที่ Claude จะเห็นมัน ซึ่งมีประโยชน์สำหรับการแก้ไข secrets การทำให้ diffs เป็นมาตรฐาน หรือการกรอง command output ที่มีเสียงรบกวน ตัวอย่าง (ลบ ANSI color codes จาก `Bash` output):
>
> ```json
> {
>   "hookSpecificOutput": {
>     "hookEventName": "PostToolUse",
>     "updatedToolOutput": "<plain-text output with ANSI escapes removed>"
>   }
> }
> ```

## Environment Variables

| ตัวแปร | ความพร้อมใช้งาน | คำอธิบาย |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | Hooks ทั้งหมด | Path สัมบูรณ์ไปยังรากของ project |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | Path ไฟล์สำหรับเก็บ env vars แบบถาวร |
| `CLAUDE_CODE_REMOTE` | Hooks ทั้งหมด | `"true"` ถ้ารันในสภาพแวดล้อมระยะไกล |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin hooks | Path ไปยังไดเรกทอรี plugin |
| `${CLAUDE_PLUGIN_DATA}` | Plugin hooks | Path ไปยังไดเรกทอรีข้อมูล plugin |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd hooks | timeout ที่กำหนดค่าได้เป็นมิลลิวินาทีสำหรับ SessionEnd hooks |

## Prompt-Based Hooks

สำหรับ event `Stop` และ `SubagentStop` คุณสามารถใช้การประเมินแบบ LLM:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if all tasks are complete. Return your decision.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**Schema การตอบสนองของ LLM:**
```json
{
  "decision": "approve",
  "reason": "All tasks completed successfully",
  "continue": false,
  "stopReason": "Task complete"
}
```

## ตัวอย่าง

### ตัวอย่างที่ 1: Bash Command Validator (PreToolUse)

**ไฟล์:** `.claude/hooks/validate-bash.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"\brm\s+-rf\s+/", "Blocking dangerous rm -rf / command"),
    (r"\bsudo\s+rm", "Blocking sudo rm command"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name != "Bash":
        sys.exit(0)

    command = input_data.get("tool_input", {}).get("command", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, command):
            print(message, file=sys.stderr)
            sys.exit(2)  # Exit 2 = blocking error

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**การกำหนดค่า:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\""
          }
        ]
      }
    ]
  }
}
```

### ตัวอย่างที่ 2: Security Scanner (PostToolUse)

**ไฟล์:** `.claude/hooks/security-scan.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

SECRET_PATTERNS = [
    (r"password\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded password"),
    (r"api[_-]?key\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded API key"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    file_path = tool_input.get("file_path", "")

    warnings = []
    for pattern, message in SECRET_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            warnings.append(message)

    if warnings:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Security warnings for {file_path}: " + "; ".join(warnings)
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### ตัวอย่างที่ 3: Auto-Format Code (PostToolUse)

**ไฟล์:** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# อ่าน JSON จาก stdin
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# format ตามนามสกุลไฟล์
case "$FILE_PATH" in
    *.js|*.jsx|*.ts|*.tsx|*.json)
        command -v prettier &>/dev/null && prettier --write "$FILE_PATH" 2>/dev/null
        ;;
    *.py)
        command -v black &>/dev/null && black "$FILE_PATH" 2>/dev/null
        ;;
    *.go)
        command -v gofmt &>/dev/null && gofmt -w "$FILE_PATH" 2>/dev/null
        ;;
esac

exit 0
```

### ตัวอย่างที่ 4: Prompt Validator (UserPromptSubmit)

**ไฟล์:** `.claude/hooks/validate-prompt.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"delete\s+(all\s+)?database", "Dangerous: database deletion"),
    (r"rm\s+-rf\s+/", "Dangerous: root deletion"),
]

def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("user_prompt", "") or input_data.get("prompt", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            output = {
                "decision": "block",
                "reason": f"Blocked: {message}"
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### ตัวอย่างที่ 5: Intelligent Stop Hook (Prompt-Based)

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if Claude completed all requested tasks. Check: 1) Were all files created/modified? 2) Were there unresolved errors? If incomplete, explain what's missing.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### ตัวอย่างที่ 6: Context Usage Tracker (Hook Pairs)

ติดตามการใช้ token ต่อคำขอโดยใช้ hook `UserPromptSubmit` (ก่อนข้อความ) และ `Stop` (หลังการตอบสนอง) ร่วมกัน

**ไฟล์:** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
Context Usage Tracker - ติดตามการใช้ token ต่อคำขอ

ใช้ UserPromptSubmit เป็น hook "ก่อนข้อความ" และ Stop เป็น hook "หลังการตอบสนอง"
เพื่อคำนวณ delta ในการใช้ token สำหรับแต่ละคำขอ

วิธีการนับ Token:
1. การประมาณอักขระ (ค่าเริ่มต้น): ~4 อักขระต่อ token ไม่มี dependencies
2. tiktoken (ทางเลือก): แม่นยำกว่า (~90-95%) ต้องการ: pip install tiktoken
"""
import json
import os
import sys
import tempfile

# การกำหนดค่า
CONTEXT_LIMIT = 128000  # context window ของ Claude (ปรับตามโมเดล)
USE_TIKTOKEN = False    # ตั้งเป็น True ถ้าติดตั้ง tiktoken


def get_state_file(session_id: str) -> str:
    """ดู path ไฟล์ชั่วคราวสำหรับเก็บจำนวน token ก่อนข้อความ แยกตาม session"""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    นับ tokens ในข้อความ

    ใช้ tiktoken กับ encoding p50k_base ถ้าพร้อมใช้งาน (~90-95% แม่นยำ)
    มิฉะนั้น fallback เป็นการประมาณอักขระ (~80-90% แม่นยำ)
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # Fallback เป็นการประมาณ

    # การประมาณตามอักขระ: ~4 อักขระต่อ token สำหรับภาษาอังกฤษ
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """อ่านและต่อเนื้อหาทั้งหมดจากไฟล์ transcript"""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # ดึงเนื้อหาข้อความจากรูปแบบข้อความต่างๆ
                if "message" in entry:
                    msg = entry["message"]
                    if isinstance(msg.get("content"), str):
                        content.append(msg["content"])
                    elif isinstance(msg.get("content"), list):
                        for block in msg["content"]:
                            if isinstance(block, dict) and block.get("type") == "text":
                                content.append(block.get("text", ""))
            except json.JSONDecodeError:
                continue

    return "\n".join(content)


def handle_user_prompt_submit(data: dict) -> None:
    """Hook ก่อนข้อความ: บันทึกจำนวน token ปัจจุบันก่อนคำขอ"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # บันทึกลงไฟล์ชั่วคราวเพื่อเปรียบเทียบในภายหลัง
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """Hook หลังการตอบสนอง: คำนวณและรายงาน delta ของ token"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # โหลดจำนวน token ก่อนข้อความ
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # คำนวณ delta
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # รายงานการใช้งาน
    method = "tiktoken" if USE_TIKTOKEN else "estimated"
    print(f"Context ({method}): ~{current_tokens:,} tokens ({percentage:.1f}% used, ~{remaining:,} remaining)", file=sys.stderr)
    if delta_tokens > 0:
        print(f"This request: ~{delta_tokens:,} tokens", file=sys.stderr)


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")

    if event == "UserPromptSubmit":
        handle_user_prompt_submit(data)
    elif event == "Stop":
        handle_stop(data)

    sys.exit(0)


if __name__ == "__main__":
    main()
```

**การกำหนดค่า:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ]
  }
}
```

**วิธีการทำงาน:**
1. `UserPromptSubmit` เริ่มก่อนที่ prompt จะถูกประมวลผล — บันทึกจำนวน token ปัจจุบัน
2. `Stop` เริ่มหลัง Claude ตอบสนอง — คำนวณ delta และรายงานการใช้งาน
3. แต่ละ session ถูกแยกผ่าน `session_id` ในชื่อไฟล์ชั่วคราว

**วิธีการนับ Token:**

| วิธีการ | ความแม่นยำ | Dependencies | ความเร็ว |
|--------|----------|--------------|-------|
| การประมาณอักขระ | ~80-90% | ไม่มี | <1ms |
| tiktoken (p50k_base) | ~90-95% | `pip install tiktoken` | <10ms |

### ตัวอย่างที่ 7: Seed Auto-Mode Permissions (สคริปต์ตั้งค่าครั้งเดียว)

สคริปต์ตั้งค่าครั้งเดียวที่เพิ่มกฎสิทธิ์ที่ปลอดภัยประมาณ 67 รายการใน `~/.claude/settings.json` ซึ่งเทียบเท่ากับ baseline auto-mode ของ Claude Code — โดยไม่มี hook และไม่จดจำตัวเลือกในอนาคต รันครั้งเดียว ปลอดภัยที่จะรันซ้ำ (ข้ามกฎที่มีอยู่แล้ว)

**ไฟล์:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# ดูตัวอย่างสิ่งที่จะเพิ่ม
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# ใช้งาน
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**สิ่งที่จะเพิ่ม:**

| หมวดหมู่ | ตัวอย่าง |
|----------|---------|
| เครื่องมือในตัว | `Read(*)`, `Edit(*)`, `Write(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)` |
| Git read | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)` |
| Git write (local) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Package managers | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| Build & test | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Shell ทั่วไป | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

**สิ่งที่ตั้งใจไม่รวม** (ไม่เพิ่มโดยสคริปต์นี้เด็ดขาด):
- `rm -rf`, `sudo`, force push, `git reset --hard`
- `DROP TABLE`, `kubectl delete`, `terraform destroy`
- `npm publish`, `curl | bash`, production deploys

### ตัวอย่างที่ 8: Learning Progress Logger (SessionEnd)

บันทึกว่าคุณศึกษาโมดูลใดเมื่อสิ้นสุด Claude Code session แต่ละครั้ง ความคืบหน้าถูกเก็บไว้ใน `~/.claude-howto-progress.json` — ภายนอก repository ดังนั้นจึงรอดพ้นจาก `git pull` โดยไม่ถูกเขียนทับ

**เหตุใดจึงใช้ `SessionEnd` ไม่ใช่ `Stop`?**
`Stop` เริ่มหลังการตอบสนองของ Claude *ทุกครั้ง* `SessionEnd` เริ่มทำงานครั้งเดียวเมื่อ session สิ้นสุด — ซึ่งเหมาะสำหรับรายการบันทึกสิ้นสุด session

**เหตุใดจึงใช้ `/dev/tty` สำหรับ input?**
สคริปต์ hook รับ JSON payload ของ hook ผ่าน `stdin` ดังนั้น `read` แบบโต้ตอบต้องใช้ `/dev/tty` โดยตรงเพื่อเข้าถึง terminal

**ไฟล์:** `06-hooks/session-end.sh`

```bash
#!/usr/bin/env bash
# SessionEnd hook: แจ้งให้ระบุโมดูลที่ทำงาน จากนั้นเพิ่มระเบียน session
# ลงใน ~/.claude-howto-progress.json สำหรับการติดตามความคืบหน้าการเรียนรู้แบบถาวร

PROGRESS_FILE="$HOME/.claude-howto-progress.json"

# Guard: รันเฉพาะใน repository นี้
if [[ "$CLAUDE_PROJECT_DIR" != *"claude-howto"* ]] && [[ "$PWD" != *"claude-howto"* ]]; then
  exit 0
fi

if [ ! -f "$PROGRESS_FILE" ]; then
  echo '{"sessions":[]}' > "$PROGRESS_FILE"
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H:%M")

echo ""
echo " คุณทำงานกับโมดูลใด? (เช่น 06,07 หรือกด Enter เพื่อข้าม)"
echo " 01=Slash  02=Memory  03=Skills  04=Subagents  05=MCP"
echo " 06=Hooks  07=Plugins 08=Checkpoints 09=Advanced 10=CLI"
printf " > "
read -r INPUT </dev/tty

if [ -z "$INPUT" ] || [ "$INPUT" = "skip" ]; then
  exit 0
fi

MODULES_JSON=$(echo "$INPUT" | tr ',' '\n' | tr -d ' ' | while read -r m; do
  case "$m" in
    01) echo '"01-slash-commands"' ;;
    02) echo '"02-memory"' ;;
    03) echo '"03-skills"' ;;
    04) echo '"04-subagents"' ;;
    05) echo '"05-mcp"' ;;
    06) echo '"06-hooks"' ;;
    07) echo '"07-plugins"' ;;
    08) echo '"08-checkpoints"' ;;
    09) echo '"09-advanced-features"' ;;
    10) echo '"10-cli"' ;;
    *)  echo "\"$m\"" ;;
  esac
done | paste -sd ',' -)

printf " หมายเหตุ? (ทางเลือก กด Enter เพื่อข้าม): "
read -r NOTES </dev/tty

# ส่ง NOTES เป็น argument แยกเพื่อให้ Python จัดการ JSON escaping —
# หลีกเลี่ยง JSON ที่เสียหายเมื่อ notes มีเครื่องหมายคำพูดหรือ backslash
python3 - "$PROGRESS_FILE" "$DATE" "$TIME" "$MODULES_JSON" "$NOTES" <<'PYEOF'
import sys, json

path, date, time_str, modules_raw, notes = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]

new_session = {
    "date": date,
    "time": time_str,
    "modules": json.loads(f"[{modules_raw}]") if modules_raw else [],
    "notes": notes,
}

with open(path, 'r') as f:
    data = json.load(f)

data.setdefault('sessions', []).append(new_session)

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

echo " บันทึกไปยัง $PROGRESS_FILE แล้ว"
```

**ติดตั้ง** — คัดลอกสคริปต์ไปยัง hook directory ของ project เพื่อให้ path ใน `settings.json` ทำงานได้:

```bash
mkdir -p .claude/hooks
cp 06-hooks/session-end.sh .claude/hooks/
chmod +x .claude/hooks/session-end.sh
```

**การกำหนดค่า** (ใน `.claude/settings.json`):

```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-end.sh\""
          }
        ]
      }
    ]
  }
}
```

**ผลลัพธ์ — `~/.claude-howto-progress.json`:**

```json
{
  "sessions": [
    {
      "date": "2026-04-18",
      "time": "14:32",
      "modules": ["06-hooks", "07-plugins"],
      "notes": "Installed first hook, tried pre-commit example"
    }
  ]
}
```

**รูปแบบหลักที่แสดง:**

| รูปแบบ | เหตุผลที่สำคัญ |
|---------|----------------|
| `SessionEnd` event | เริ่มทำงานครั้งเดียวเมื่อออก — ไม่ใช่หลังทุกการตอบสนองเหมือน `Stop` |
| `read -r INPUT </dev/tty` | Hooks มี `stdin` (JSON payload) ใช้ `/dev/tty` สำหรับ input ผู้ใช้ |
| `$CLAUDE_PROJECT_DIR` | Path ที่พกพาได้ — ไม่ hardcode `/Users/yourname/...` เด็ดขาด |
| Guard clause ด้านบน | ป้องกัน hook รันใน project ที่ไม่เกี่ยวข้องถ้าติดตั้งแบบ global |
| เก็บภายนอก repository | `~/` path รอดพ้นจาก `git pull` โดยไม่เขียนทับข้อมูลของคุณ |

## Plugin Hooks

Plugin สามารถรวม hooks ในไฟล์ `hooks/hooks.json` ของพวกเขา:

**ไฟล์:** `plugins/hooks/hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"
          }
        ]
      }
    ]
  }
}
```

**Environment Variables ใน Plugin Hooks:**
- `${CLAUDE_PLUGIN_ROOT}` - Path ไปยังไดเรกทอรี plugin
- `${CLAUDE_PLUGIN_DATA}` - Path ไปยังไดเรกทอรีข้อมูล plugin

ซึ่งช่วยให้ plugin สามารถรวม validation และ automation hooks แบบกำหนดเองได้

## MCP Tool Hooks

เครื่องมือ MCP ใช้รูปแบบ `mcp__<server>__<tool>`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"systemMessage\": \"Memory operation logged\"}'"
          }
        ]
      }
    ]
  }
}
```

## ข้อพิจารณาด้านความปลอดภัย

### ข้อจำกัดความรับผิดชอบ

**ใช้งานด้วยความเสี่ยงของตนเอง**: Hooks รันคำสั่ง shell ตามอำเภอใจ คุณรับผิดชอบแต่เพียงผู้เดียวสำหรับ:
- คำสั่งที่คุณกำหนดค่า
- สิทธิ์การเข้าถึง/การแก้ไขไฟล์
- การสูญหายของข้อมูลหรือความเสียหายของระบบที่อาจเกิดขึ้น
- การทดสอบ hooks ในสภาพแวดล้อมที่ปลอดภัยก่อนใช้งานจริง

### หมายเหตุความปลอดภัย

- **ต้องการความน่าเชื่อถือของ workspace:** คำสั่ง hook output `statusLine` และ `fileSuggestion` ตอนนี้ต้องการการยอมรับความน่าเชื่อถือของ workspace ก่อนที่จะมีผล
- **HTTP hooks และ environment variables:** HTTP hooks ต้องการรายการ `allowedEnvVars` ที่ชัดเจนเพื่อใช้การสอดแทรก environment variable ใน URL ซึ่งป้องกันการรั่วไหลโดยไม่ตั้งใจของ environment variables ที่ละเอียดอ่อนไปยัง remote endpoints
- **ลำดับชั้นการตั้งค่าที่จัดการ:** การตั้งค่า `disableAllHooks` ตอนนี้เคารพลำดับชั้นการตั้งค่าที่จัดการ ซึ่งหมายความว่าการตั้งค่าระดับองค์กรสามารถบังคับใช้การปิดใช้งาน hook ที่ผู้ใช้แต่ละคนไม่สามารถแทนที่ได้
- **PowerShell auto-approve (v2.1.119):** คำสั่งเครื่องมือ PowerShell สามารถอนุมัติอัตโนมัติในโหมดสิทธิ์ได้ เทียบเท่ากับ Bash ซึ่งช่วยให้ Windows ผู้ใช้ Claude Code ที่มีเครื่องมือ shell แบบ PowerShell ทำงานได้เท่าเทียมกัน

### แนวปฏิบัติที่ดี

| ควรทำ | ไม่ควรทำ |
|-----|-------|
| ตรวจสอบและ sanitize input ทั้งหมด | เชื่อถือข้อมูล input โดยไม่ตรวจสอบ |
| อ้างอิงตัวแปร shell: `"$VAR"` | ใช้โดยไม่อ้างอิง: `$VAR` |
| บล็อก path traversal (`..`) | อนุญาต paths ตามอำเภอใจ |
| ใช้ absolute paths กับ `$CLAUDE_PROJECT_DIR` | Hardcode paths |
| ข้ามไฟล์ที่ละเอียดอ่อน (`.env`, `.git/`, keys) | ประมวลผลทุกไฟล์ |
| ทดสอบ hooks แบบ isolation ก่อน | Deploy hooks ที่ยังไม่ทดสอบ |
| ใช้ `allowedEnvVars` ที่ชัดเจนสำหรับ HTTP hooks | เปิดเผย env vars ทั้งหมดให้ webhooks |

## การ debugging

### เปิดใช้งาน Debug Mode

รัน Claude ด้วย debug flag เพื่อดู logs การรัน hook โดยละเอียด:

```bash
claude --debug
```

### Verbose Mode

ใช้ `Ctrl+O` ใน Claude Code เพื่อเปิดใช้งาน verbose mode และดูความคืบหน้าการรัน hook

### ทดสอบ Hooks อย่างอิสระ

```bash
# ทดสอบด้วย JSON input ตัวอย่าง
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# ตรวจสอบ exit code
echo $?
```

## ตัวอย่างการกำหนดค่าที่สมบูรณ์

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/format-code.sh\"",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py\""
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-init.sh\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Verify all tasks are complete before stopping.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## รายละเอียดการรัน Hook

| ด้าน | พฤติกรรม |
|--------|----------|
| **Timeout** | ค่าเริ่มต้น 60 วินาที กำหนดค่าได้ต่อคำสั่ง |
| **Parallelization** | hooks ที่ตรงกันทั้งหมดรันพร้อมกัน |
| **Deduplication** | คำสั่ง hook ที่เหมือนกันถูกกำจัดซ้ำ |
| **Environment** | รันในไดเรกทอรีปัจจุบันพร้อมสภาพแวดล้อมของ Claude Code |

## การแก้ไขปัญหา

### Hook ไม่รัน
- ตรวจสอบว่า JSON configuration syntax ถูกต้อง
- ตรวจสอบว่า matcher pattern ตรงกับชื่อเครื่องมือ
- ตรวจสอบว่าสคริปต์มีอยู่และสามารถรันได้: `chmod +x script.sh`
- รัน `claude --debug` เพื่อดู logs การรัน hook
- ตรวจสอบว่า hook อ่าน JSON จาก stdin (ไม่ใช่ command args)

### Hook บล็อกโดยไม่คาดคิด
- ทดสอบ hook ด้วย JSON ตัวอย่าง: `echo '{"tool_name": "Write", ...}' | ./hook.py`
- ตรวจสอบ exit code: ควรเป็น 0 สำหรับ allow, 2 สำหรับ block
- ตรวจสอบ stderr output (แสดงเมื่อ exit code 2)

### ข้อผิดพลาดการวิเคราะห์ JSON
- อ่านจาก stdin เสมอ ไม่ใช่ command arguments
- ใช้การวิเคราะห์ JSON ที่ถูกต้อง (ไม่ใช่การจัดการสตริง)
- จัดการฟิลด์ที่ขาดหายอย่างสง่างาม

## การติดตั้ง

### ขั้นตอนที่ 1: สร้าง Hooks Directory
```bash
mkdir -p ~/.claude/hooks
```

### ขั้นตอนที่ 2: คัดลอก Hooks ตัวอย่าง
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### ขั้นตอนที่ 3: กำหนดค่าใน Settings
แก้ไข `~/.claude/settings.json` หรือ `.claude/settings.json` ด้วยการกำหนดค่า hook ที่แสดงด้านบน

## แนวคิดที่เกี่ยวข้อง

- **[Checkpoints and Rewind](../08-checkpoints/)** - บันทึกและกู้คืนสถานะการสนทนา
- **[Slash Commands](../01-slash-commands/)** - สร้าง slash commands แบบกำหนดเอง
- **[Skills](../03-skills/)** - ความสามารถอัตโนมัติที่นำมาใช้ซ้ำได้
- **[Subagents](../04-subagents/)** - การมอบหมายการทำงาน
- **[Plugins](../07-plugins/)** - แพ็คเกจ extension ที่รวมกัน
- **[Advanced Features](../09-advanced-features/)** - สำรวจฟีเจอร์ขั้นสูงของ Claude Code

## แหล่งข้อมูลเพิ่มเติม

- **[เอกสาร Hooks อย่างเป็นทางการ](https://code.claude.com/docs/en/hooks)** - ข้อมูลอ้างอิง hooks ที่สมบูรณ์
- **[CLI Reference](https://code.claude.com/docs/en/cli-reference)** - เอกสาร command-line interface
- **[Memory Guide](../02-memory/)** - การกำหนดค่า context แบบถาวร

---

**อัปเดตล่าสุด**: May 6, 2026
**Claude Code Version**: 2.1.131
**แหล่งที่มา**:
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.118
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
**โมเดลที่รองรับ**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
