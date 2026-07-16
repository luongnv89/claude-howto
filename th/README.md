<!-- i18n-source: README.md -->
<!-- i18n-date: 2026-07-15 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.131-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

🌐 **ภาษา / Language:** [English](../README.md) | [Tiếng Việt](../vi/README.md) | [中文](../zh/README.md) | [Українська](../uk/README.md) | [日本語](../ja/README.md) | [ภาษาไทย](README.md)

# เรียนรู้ Claude Code ให้เชี่ยวชาญภายในสุดสัปดาห์เดียว

เริ่มต้นจากการพิมพ์ `claude` ไปจนถึงการควบคุม agent, hook, skill และ MCP server — ด้วยบทเรียนแบบภาพ, template ที่คัดลอกนำไปใช้ได้ทันที และเส้นทางการเรียนรู้ที่มีโครงสร้างชัดเจน

**[เริ่มต้นใน 15 นาที](#เริ่มต้นใน-15-นาที)** | **[ค้นหาระดับของคุณ](#ไม่แน่ใจว่าจะเริ่มจากตรงไหน)** | **[เรียกดู Feature Catalog](CATALOG.md)**

---

## สารบัญ

- [ปัญหา](#ปัญหา)
- [Claude How To แก้ปัญหานี้อย่างไร](#claude-how-to-แก้ปัญหานี้อย่างไร)
- [วิธีการทำงาน](#วิธีการทำงาน)
- [ไม่แน่ใจว่าจะเริ่มจากตรงไหน](#ไม่แน่ใจว่าจะเริ่มจากตรงไหน)
- [เริ่มต้นใน 15 นาที](#เริ่มต้นใน-15-นาที)
- [สิ่งที่สร้างได้ด้วย Claude Code](#สิ่งที่สร้างได้ด้วย-claude-code)
- [คำถามที่พบบ่อย](#คำถามที่พบบ่อย)
- [การมีส่วนร่วม](#การมีส่วนร่วม)
- [สัญญาอนุญาต](#สัญญาอนุญาต)

---

## ปัญหา

คุณติดตั้ง Claude Code แล้ว ทดลองพิมพ์ prompt ไปสองสามครั้ง แล้วต่อไปควรทำอะไร?

- **เอกสารทางการอธิบายฟีเจอร์แต่ละอย่าง แต่ไม่แสดงวิธีนำมาใช้ร่วมกัน** คุณรู้ว่า slash command มีอยู่ แต่ไม่รู้วิธีเชื่อมต่อกับ hook, memory และ subagent ให้เป็น workflow ที่ประหยัดเวลาได้จริง
- **ไม่มีเส้นทางการเรียนรู้ที่ชัดเจน** ควรเรียน MCP ก่อน hook หรือเรียน skill ก่อน subagent? จนสุดท้ายอ่านผ่านทุกอย่างแต่ไม่ได้เชี่ยวชาญสักอย่าง
- **ตัวอย่างพื้นฐานเกินไป** slash command แบบ "hello world" ไม่ช่วยให้สร้าง code review pipeline ระดับ production ที่ใช้ memory, มอบหมายงานให้ agent เฉพาะทาง และรัน security scan โดยอัตโนมัติได้

คุณใช้ประโยชน์จาก Claude Code ได้เพียง 10% — และไม่รู้ด้วยซ้ำว่ายังขาดอะไรอีก

---

## Claude How To แก้ปัญหานี้อย่างไร

นี่ไม่ใช่เอกสารอ้างอิงฟีเจอร์อีกฉบับ แต่เป็น **คู่มือเชิงภาพ ตัวอย่างจริง** ที่สอนการใช้ฟีเจอร์ทุกอย่างของ Claude Code พร้อม template ระดับ production ที่คัดลอกใส่โปรเจกต์ได้ทันที

| | เอกสารทางการ | คู่มือนี้ |
|--|---------------|------------|
| **รูปแบบ** | เอกสารอ้างอิง | บทเรียนภาพพร้อม Mermaid diagram |
| **ความลึก** | อธิบายฟีเจอร์ | อธิบายกลไกภายใน |
| **ตัวอย่าง** | โค้ดพื้นฐาน | Template ระดับ production ที่ใช้ได้ทันที |
| **โครงสร้าง** | จัดตามฟีเจอร์ | เส้นทางการเรียนรู้แบบค่อยเป็นค่อยไป (ผู้เริ่มต้นถึงขั้นสูง) |
| **การเริ่มต้น** | เรียนด้วยตัวเอง | Roadmap มีระยะเวลาประมาณ |
| **การประเมินตัวเอง** | ไม่มี | แบบทดสอบเชิงโต้ตอบเพื่อค้นหาจุดอ่อนและสร้างเส้นทางส่วนตัว |

### สิ่งที่ได้รับ:

- **10 โมดูลบทเรียน** ครอบคลุมทุกฟีเจอร์ของ Claude Code — ตั้งแต่ slash command ถึงทีม agent แบบกำหนดเอง
- **การกำหนดค่าแบบคัดลอกนำไปใช้** — slash command, CLAUDE.md template, hook script, MCP config, นิยาม subagent และ plugin bundle ครบชุด
- **Mermaid diagram** แสดงการทำงานภายในของแต่ละฟีเจอร์ เพื่อให้เข้าใจ *ทำไม* ไม่ใช่แค่ *อย่างไร*
- **เส้นทางการเรียนรู้** ที่พาจากผู้เริ่มต้นสู่ผู้ใช้ขั้นสูงใน 11-13 ชั่วโมง
- **การประเมินตัวเองในตัว** — รัน `/self-assessment` หรือ `/lesson-quiz hooks` ใน Claude Code เพื่อระบุจุดที่ต้องพัฒนา

**[เริ่มต้นเส้นทางการเรียนรู้ ->](LEARNING-ROADMAP.md)**

---

## วิธีการทำงาน

### 1. ค้นหาระดับของคุณ

ทำ [แบบทดสอบประเมินตัวเอง](LEARNING-ROADMAP.md#-find-your-level) หรือรัน `/self-assessment` ใน Claude Code รับ roadmap ส่วนตัวตามสิ่งที่รู้อยู่แล้ว

### 2. ทำตาม guided path

ทำ 10 โมดูลตามลำดับ — แต่ละโมดูลต่อยอดจากโมดูลก่อนหน้า คัดลอก template ใส่โปรเจกต์ขณะที่เรียน

### 3. รวมฟีเจอร์เข้าเป็น workflow

พลังที่แท้จริงอยู่ที่การรวมฟีเจอร์เข้าด้วยกัน เรียนรู้การเชื่อม slash command + memory + subagent + hook เข้าเป็น pipeline อัตโนมัติที่จัดการ code review, deployment และการสร้างเอกสาร

### 4. ทดสอบความเข้าใจ

รัน `/lesson-quiz [topic]` หลังแต่ละโมดูล แบบทดสอบระบุสิ่งที่พลาดไปเพื่อเติมช่องว่างได้รวดเร็ว

**[เริ่มต้นใน 15 นาที](#เริ่มต้นใน-15-นาที)**

---

## ที่ใช้งานโดยนักพัฒนาจริง

- **GitHub stars** จากนักพัฒนาที่ใช้ Claude Code ทุกวัน
- **Fork** จากทีมที่นำคู่มือนี้ไปปรับใช้กับ workflow ของตัวเอง
- **ดูแลอย่างต่อเนื่อง** — ซิงก์กับทุก Claude Code release (ล่าสุด: v2.1.131, พฤษภาคม 2026)
- **ขับเคลื่อนโดยชุมชน** — มีส่วนร่วมจากนักพัฒนาที่แชร์การกำหนดค่าจากการใช้งานจริง

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## ไม่แน่ใจว่าจะเริ่มจากตรงไหน?

ทำแบบทดสอบประเมินตัวเองหรือเลือกระดับ:

| ระดับ | ความสามารถ | เริ่มที่นี่ | เวลา |
|-------|-----------|------------|------|
| **ผู้เริ่มต้น** | เริ่ม Claude Code และสนทนาได้ | [Slash Commands](../01-slash-commands/) | ~2.5 ชั่วโมง |
| **ระดับกลาง** | ใช้ CLAUDE.md และคำสั่งกำหนดเองได้ | [Skills](../03-skills/) | ~3.5 ชั่วโมง |
| **ขั้นสูง** | กำหนดค่า MCP server และ hook ได้ | [Advanced Features](../09-advanced-features/) | ~5 ชั่วโมง |

**เส้นทางการเรียนรู้เต็มรูปแบบ 10 โมดูล:**

| ลำดับ | โมดูล | ระดับ | เวลา |
|-------|--------|-------|------|
| 1 | [Slash Commands](../01-slash-commands/) | ผู้เริ่มต้น | 30 นาที |
| 2 | [Memory](../02-memory/) | ผู้เริ่มต้น+ | 45 นาที |
| 3 | [Checkpoints](../08-checkpoints/) | ระดับกลาง | 45 นาที |
| 4 | [CLI Basics](../10-cli/) | ผู้เริ่มต้น+ | 30 นาที |
| 5 | [Skills](../03-skills/) | ระดับกลาง | 1 ชั่วโมง |
| 6 | [Hooks](../06-hooks/) | ระดับกลาง | 1 ชั่วโมง |
| 7 | [MCP](../05-mcp/) | ระดับกลาง+ | 1 ชั่วโมง |
| 8 | [Subagents](../04-subagents/) | ระดับกลาง+ | 1.5 ชั่วโมง |
| 9 | [Advanced Features](../09-advanced-features/) | ขั้นสูง | 2-3 ชั่วโมง |
| 10 | [Plugins](../07-plugins/) | ขั้นสูง | 2 ชั่วโมง |

**[Learning Roadmap ฉบับสมบูรณ์ ->](LEARNING-ROADMAP.md)**

---

## เริ่มต้นใน 15 นาที

> **หมายเหตุการติดตั้ง**: ตั้งแต่ v2.1.113 Claude Code จัดส่งเป็น binary แบบ native ต่อแพลตฟอร์ม (macOS/Linux/Windows) `npm install -g @anthropic-ai/claude-code` ยังใช้งานได้ — native binary จะดาวน์โหลดเป็น optional dep ในการใช้ครั้งแรก ตั้งแต่ v2.1.116 การดาวน์โหลดมาจาก `https://downloads.claude.ai/claude-code-releases` — proxy ขององค์กรต้องอนุญาต host นี้

```bash
# 1. Clone คู่มือ
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. คัดลอก slash command แรกของคุณ
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. ลองใช้งาน — ใน Claude Code พิมพ์:
# /optimize

# 4. พร้อมสำหรับขั้นต่อไป? ตั้งค่า project memory:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. ติดตั้ง skill:
cp -r 03-skills/code-review ~/.claude/skills/
```

ต้องการการตั้งค่าเต็มรูปแบบ? นี่คือ **การตั้งค่าสำคัญใน 1 ชั่วโมง**:

```bash
# Slash commands (15 นาที)
cp 01-slash-commands/*.md .claude/commands/

# Project memory (15 นาที)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# ติดตั้ง skill (15 นาที)
cp -r 03-skills/code-review ~/.claude/skills/

# เป้าหมายสุดสัปดาห์: เพิ่ม hook, subagent, MCP และ plugin
# ติดตาม learning path เพื่อการตั้งค่าที่มีโครงสร้าง
```

**[ดูการอ้างอิงการติดตั้งฉบับเต็ม](#เริ่มต้นใน-15-นาที)**

---

## สิ่งที่สร้างได้ด้วย Claude Code

| กรณีการใช้งาน | ฟีเจอร์ที่ใช้ร่วมกัน |
|----------|------------------------|
| **Code Review อัตโนมัติ** | Slash Commands + Subagents + Memory + MCP |
| **Onboarding ทีมงาน** | Memory + Slash Commands + Plugins |
| **CI/CD Automation** | CLI Reference + Hooks + Background Tasks |
| **การสร้างเอกสาร** | Skills + Subagents + Plugins |
| **Security Audit** | Subagents + Skills + Hooks (read-only mode) |
| **DevOps Pipeline** | Plugins + MCP + Hooks + Background Tasks |
| **Refactoring ซับซ้อน** | Checkpoints + Planning Mode + Hooks |

---

## คำถามที่พบบ่อย

**ใช้งานฟรีหรือไม่?**
ใช่ สัญญาอนุญาต MIT ฟรีตลอดกาล ใช้ในโปรเจกต์ส่วนตัว ที่ทำงาน หรือในทีมได้ — ไม่มีข้อจำกัด นอกจากต้องรวมประกาศสัญญาอนุญาต

**มีการดูแลรักษาหรือไม่?**
ดูแลอย่างต่อเนื่อง คู่มือซิงก์กับทุก Claude Code release เวอร์ชันปัจจุบัน: v2.1.131 (พฤษภาคม 2026) รองรับ Claude Code 2.1+

**แตกต่างจากเอกสารทางการอย่างไร?**
เอกสารทางการเป็นเอกสารอ้างอิงฟีเจอร์ คู่มือนี้เป็นบทเรียนพร้อม diagram, template ระดับ production และเส้นทางการเรียนรู้แบบค่อยเป็นค่อยไป ใช้ร่วมกันได้ดี — เริ่มเรียนที่นี่ ดูเอกสารทางการเมื่อต้องการรายละเอียดเฉพาะ

**ต้องใช้เวลานานแค่ไหนในการผ่านทั้งหมด?**
11-13 ชั่วโมงสำหรับเส้นทางเต็มรูปแบบ แต่จะได้ประโยชน์ทันทีใน 15 นาที — เพียงคัดลอก slash command template แล้วลองใช้

**ใช้กับ Claude Sonnet / Haiku / Opus ได้หรือไม่?**
ได้ template ทั้งหมดใช้งานได้กับ Claude Sonnet 4.6, Claude Opus 4.7 และ Claude Haiku 4.5

**มีส่วนร่วมได้หรือไม่?**
ได้อย่างแน่นอน ดู [CONTRIBUTING.md](CONTRIBUTING.md) สำหรับแนวทาง ยินดีรับตัวอย่างใหม่, การแก้ไขข้อผิดพลาด, การปรับปรุงเอกสาร และ template จากชุมชน

**อ่านแบบออฟไลน์ได้หรือไม่?**
ได้ รัน `uv run scripts/build_epub.py` เพื่อสร้าง EPUB ebook ที่รวมเนื้อหาทั้งหมดพร้อม diagram ที่แสดงผลแล้ว

---

## เริ่มต้นเรียนรู้ Claude Code วันนี้

คุณติดตั้ง Claude Code อยู่แล้ว สิ่งเดียวที่คั่นระหว่างคุณกับประสิทธิภาพที่สูงขึ้น 10 เท่าคือการรู้วิธีใช้ คู่มือนี้ให้เส้นทางที่มีโครงสร้าง คำอธิบายเชิงภาพ และ template ที่คัดลอกนำไปใช้ได้เพื่อบรรลุเป้าหมายนั้น

สัญญาอนุญาต MIT ฟรีตลอดกาล Clone ได้, Fork ได้, ทำให้เป็นของคุณได้

**[เริ่มต้น Learning Path ->](LEARNING-ROADMAP.md)** | **[เรียกดู Feature Catalog](CATALOG.md)** | **[เริ่มต้นใน 15 นาที](#เริ่มต้นใน-15-นาที)**

---

<details>
<summary>การนำทางด่วน — ฟีเจอร์ทั้งหมด</summary>

| ฟีเจอร์ | คำอธิบาย | โฟลเดอร์ |
|---------|-------------|--------|
| **Feature Catalog** | เอกสารอ้างอิงครบถ้วนพร้อมคำสั่งติดตั้ง | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | ทางลัดที่เรียกใช้โดยผู้ใช้ | [01-slash-commands/](../01-slash-commands/) |
| **Memory** | context ถาวร | [02-memory/](../02-memory/) |
| **Skills** | ความสามารถที่นำกลับมาใช้ใหม่ | [03-skills/](../03-skills/) |
| **Subagents** | AI assistant เฉพาะทาง | [04-subagents/](../04-subagents/) |
| **MCP Protocol** | การเข้าถึงเครื่องมือภายนอก | [05-mcp/](../05-mcp/) |
| **Hooks** | automation แบบ event-driven | [06-hooks/](../06-hooks/) |
| **Plugins** | ฟีเจอร์แบบ bundle | [07-plugins/](../07-plugins/) |
| **Checkpoints** | snapshot session และ rewind | [08-checkpoints/](../08-checkpoints/) |
| **Advanced Features** | Planning, thinking, background task | [09-advanced-features/](../09-advanced-features/) |
| **CLI Reference** | คำสั่ง, flag และตัวเลือก | [10-cli/](../10-cli/) |
| **Blog Posts** | ตัวอย่างการใช้งานจริง | [Blog Posts](https://medium.com/@luongnv89) |

</details>

<details>
<summary>การเปรียบเทียบฟีเจอร์</summary>

| ฟีเจอร์ | การเรียกใช้ | ความถาวร | เหมาะสำหรับ |
|---------|-----------|------------|----------|
| **Slash Commands** | Manual (`/cmd`) | เฉพาะ session | ทางลัดด่วน |
| **Memory** | โหลดอัตโนมัติ | ข้าม session | การเรียนรู้ระยะยาว |
| **Skills** | เรียกใช้อัตโนมัติ | Filesystem | Workflow อัตโนมัติ |
| **Subagents** | มอบหมายอัตโนมัติ | context แยกส่วน | กระจายงาน |
| **MCP Protocol** | ค้นหาอัตโนมัติ | Real-time | การเข้าถึงข้อมูลสด |
| **Hooks** | เรียกโดย event | กำหนดค่าแล้ว | Automation และ validation |
| **Plugins** | คำสั่งเดียว | ฟีเจอร์ทั้งหมด | โซลูชันครบชุด |
| **Checkpoints** | Manual/Auto | ตาม session | การทดลองอย่างปลอดภัย |
| **Planning Mode** | Manual/Auto | ช่วง plan | การพัฒนาที่ซับซ้อน |
| **Background Tasks** | Manual | ตลอดระยะเวลางาน | การดำเนินการที่ใช้เวลานาน |
| **CLI Reference** | คำสั่ง terminal | Session/Script | Automation และ scripting |

</details>

<details>
<summary>การอ้างอิงการติดตั้งด่วน</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints (เปิดใช้งานอัตโนมัติ, กำหนดค่าใน settings)
# ดู 08-checkpoints/README.md

# Advanced Features (กำหนดค่าใน settings)
# ดู 09-advanced-features/config-examples.json

# CLI Reference (ไม่ต้องติดตั้ง)
# ดู 10-cli/README.md สำหรับตัวอย่างการใช้งาน
```

</details>

<details>
<summary>01. Slash Commands</summary>

**ตำแหน่ง**: [01-slash-commands/](../01-slash-commands/)

**คืออะไร**: ทางลัดที่เรียกใช้โดยผู้ใช้ จัดเก็บเป็นไฟล์ Markdown

**ตัวอย่าง**:
- `optimize.md` - การวิเคราะห์เพื่อ optimize โค้ด
- `pr.md` - การเตรียม pull request
- `generate-api-docs.md` - ตัวสร้างเอกสาร API

**การติดตั้ง**:
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**การใช้งาน**:
```
/optimize
/pr
/generate-api-docs
```

**เรียนรู้เพิ่มเติม**: [Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. Memory</summary>

**ตำแหน่ง**: [02-memory/](../02-memory/)

**คืออะไร**: context ถาวรข้ามหลาย session

**ตัวอย่าง**:
- `project-CLAUDE.md` - มาตรฐานโปรเจกต์ระดับทีม
- `directory-api-CLAUDE.md` - กฎเฉพาะไดเรกทอรี
- `personal-CLAUDE.md` - ค่ากำหนดส่วนตัว

**การติดตั้ง**:
```bash
# Project memory
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# Directory memory
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# Personal memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**การใช้งาน**: โหลดโดย Claude อัตโนมัติ

</details>

<details>
<summary>03. Skills</summary>

**ตำแหน่ง**: [03-skills/](../03-skills/)

**คืออะไร**: ความสามารถที่นำกลับมาใช้ใหม่และเรียกใช้อัตโนมัติ พร้อมคำสั่งและ script

**ตัวอย่าง**:
- `code-review/` - code review ครบถ้วนพร้อม script
- `brand-voice/` - ตัวตรวจสอบความสม่ำเสมอของ brand voice
- `doc-generator/` - ตัวสร้างเอกสาร API

**การติดตั้ง**:
```bash
# Personal skills
cp -r 03-skills/code-review ~/.claude/skills/

# Project skills
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**การใช้งาน**: เรียกใช้อัตโนมัติเมื่อเกี่ยวข้อง

</details>

<details>
<summary>04. Subagents</summary>

**ตำแหน่ง**: [04-subagents/](../04-subagents/)

**คืออะไร**: AI assistant เฉพาะทางที่มี context แยกส่วนและ prompt กำหนดเอง

**ตัวอย่าง**:
- `code-reviewer.md` - การวิเคราะห์คุณภาพโค้ดอย่างครบถ้วน
- `test-engineer.md` - กลยุทธ์และความครอบคลุมของการทดสอบ
- `documentation-writer.md` - เอกสารทางเทคนิค
- `secure-reviewer.md` - การรีวิวที่เน้นความปลอดภัย (read-only)
- `implementation-agent.md` - การพัฒนาฟีเจอร์แบบเต็มรูปแบบ

**การติดตั้ง**:
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**การใช้งาน**: มอบหมายโดย main agent อัตโนมัติ

</details>

<details>
<summary>05. MCP Protocol</summary>

**ตำแหน่ง**: [05-mcp/](../05-mcp/)

**คืออะไร**: Model Context Protocol สำหรับเข้าถึงเครื่องมือและ API ภายนอก

**ตัวอย่าง**:
- `github-mcp.json` - การเชื่อมต่อ GitHub
- `database-mcp.json` - การ query ฐานข้อมูล
- `filesystem-mcp.json` - การดำเนินการกับไฟล์
- `multi-mcp.json` - MCP server หลายตัว

**การติดตั้ง**:
```bash
# Set environment variables
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Add MCP server via CLI
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Or add to project .mcp.json manually (see 05-mcp/ for examples)
```

**การใช้งาน**: เครื่องมือ MCP พร้อมใช้งานสำหรับ Claude โดยอัตโนมัติเมื่อกำหนดค่าแล้ว

</details>

<details>
<summary>06. Hooks</summary>

**ตำแหน่ง**: [06-hooks/](../06-hooks/)

**คืออะไร**: คำสั่ง shell แบบ event-driven ที่ทำงานอัตโนมัติเพื่อตอบสนองต่อ event ของ Claude Code

**ตัวอย่าง**:
- `format-code.sh` - จัดรูปแบบโค้ดอัตโนมัติก่อนเขียน
- `pre-commit.sh` - รันการทดสอบก่อน commit
- `security-scan.sh` - สแกนหาปัญหาด้านความปลอดภัย
- `log-bash.sh` - บันทึกคำสั่ง bash ทั้งหมด
- `validate-prompt.sh` - ตรวจสอบ prompt ของผู้ใช้
- `notify-team.sh` - ส่งการแจ้งเตือนเมื่อเกิด event

**การติดตั้ง**:
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

กำหนดค่า hook ใน `~/.claude/settings.json`:
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

**การใช้งาน**: hook ทำงานอัตโนมัติเมื่อเกิด event

**ประเภทของ Hook** (5 ประเภท, 28 event):
- **Tool Hooks**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`
- **Session Hooks**: `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **Task Hooks**: `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`
- **Lifecycle Hooks**: `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. Plugins</summary>

**ตำแหน่ง**: [07-plugins/](../07-plugins/)

**คืออะไร**: ชุดรวมของคำสั่ง, agent, MCP และ hook

**ตัวอย่าง**:
- `pr-review/` - workflow การรีวิว PR แบบครบถ้วน
- `devops-automation/` - deployment และการตรวจสอบ
- `documentation/` - การสร้างเอกสาร

**การติดตั้ง**:
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**การใช้งาน**: ใช้ slash command และฟีเจอร์ที่รวมมาในชุด

</details>

<details>
<summary>08. Checkpoints and Rewind</summary>

**ตำแหน่ง**: [08-checkpoints/](../08-checkpoints/)

**คืออะไร**: บันทึกสถานะของบทสนทนาและ rewind กลับไปยังจุดก่อนหน้าเพื่อสำรวจแนวทางที่แตกต่างกัน

**แนวคิดหลัก**:
- **Checkpoint**: snapshot ของสถานะบทสนทนา
- **Rewind**: กลับไปยัง checkpoint ก่อนหน้า
- **Branch Point**: สำรวจหลายแนวทางจาก checkpoint เดียวกัน

**การใช้งาน**:
```
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind

# Then choose from five options:
# 1. Restore code and conversation
# 2. Restore conversation
# 3. Restore code
# 4. Summarize from here
# 5. Never mind
```

**กรณีการใช้งาน**:
- ทดลองแนวทางการพัฒนาที่แตกต่างกัน
- กู้คืนจากความผิดพลาด
- การทดลองอย่างปลอดภัย
- เปรียบเทียบโซลูชันทางเลือก
- A/B testing การออกแบบที่ต่างกัน

</details>

<details>
<summary>09. Advanced Features</summary>

**ตำแหน่ง**: [09-advanced-features/](../09-advanced-features/)

**คืออะไร**: ความสามารถขั้นสูงสำหรับ workflow ที่ซับซ้อนและ automation

**ประกอบด้วย**:
- **Planning Mode** — สร้างแผนการพัฒนาโดยละเอียดก่อนเขียนโค้ด
- **Extended Thinking** — การให้เหตุผลเชิงลึกสำหรับปัญหาที่ซับซ้อน (สลับด้วย `Alt+T` / `Option+T`)
- **Background Tasks** — รันการดำเนินการที่ใช้เวลานานโดยไม่ block
- **Permission Modes** — `default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`
- **Headless Mode** — รัน Claude Code ใน CI/CD: `claude -p "Run tests and generate report"`
- **Session Management** — `/resume`, `/rename`, `/fork`, `claude -c`, `claude -r`
- **Configuration** — ปรับแต่งพฤติกรรมใน `~/.claude/settings.json`

ดู [config-examples.json](../09-advanced-features/config-examples.json) สำหรับการกำหนดค่าแบบครบถ้วน

</details>

<details>
<summary>10. CLI Reference</summary>

**ตำแหน่ง**: [10-cli/](../10-cli/)

**คืออะไร**: เอกสารอ้างอิง command-line interface ของ Claude Code แบบครบถ้วน

**ตัวอย่างด่วน**:
```bash
# Interactive mode
claude "explain this project"

# Print mode (non-interactive)
claude -p "review this code"

# Process file content
cat error.log | claude -p "explain this error"

# JSON output for scripts
claude -p --output-format json "list functions"

# Resume session
claude -r "feature-auth" "continue implementation"
```

**กรณีการใช้งาน**: การเชื่อมต่อ CI/CD pipeline, script automation, batch processing, workflow แบบหลาย session, การกำหนดค่า agent แบบกำหนดเอง

</details>

<details>
<summary>ตัวอย่าง Workflow</summary>

### Workflow การรีวิวโค้ดแบบครบถ้วน

```markdown
# ใช้: Slash Commands + Subagents + Memory + MCP

ผู้ใช้: /review-pr

Claude:
1. โหลด project memory (มาตรฐานการเขียนโค้ด)
2. ดึง PR ผ่าน GitHub MCP
3. มอบหมายให้ code-reviewer subagent
4. มอบหมายให้ test-engineer subagent
5. สังเคราะห์ข้อค้นพบ
6. ให้การรีวิวที่ครบถ้วน
```

### การสร้างเอกสารอัตโนมัติ

```markdown
# ใช้: Skills + Subagents + Memory

ผู้ใช้: "Generate API documentation for the auth module"

Claude:
1. โหลด project memory (มาตรฐานเอกสาร)
2. ตรวจจับคำขอสร้างเอกสาร
3. เรียกใช้ doc-generator skill อัตโนมัติ
4. มอบหมายให้ api-documenter subagent
5. สร้างเอกสารที่ครบถ้วนพร้อมตัวอย่าง
```

### DevOps Deployment

```markdown
# ใช้: Plugins + MCP + Hooks

ผู้ใช้: /deploy production

Claude:
1. รัน pre-deploy hook (ตรวจสอบสภาพแวดล้อม)
2. มอบหมายให้ deployment-specialist subagent
3. ดำเนินการ deployment ผ่าน Kubernetes MCP
4. ติดตามความคืบหน้า
5. รัน post-deploy hook (health check)
6. รายงานสถานะ
```

</details>

<details>
<summary>โครงสร้างไดเรกทอรี</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md (this file)
```

</details>

<details>
<summary>แนวปฏิบัติที่ดี</summary>

### สิ่งที่ควรทำ
- เริ่มต้นอย่างเรียบง่ายด้วย slash command
- เพิ่มฟีเจอร์ทีละขั้น
- ใช้ memory สำหรับมาตรฐานของทีม
- ทดสอบการกำหนดค่าในเครื่องก่อน
- จัดทำเอกสารการใช้งานที่กำหนดเอง
- ควบคุมเวอร์ชันการกำหนดค่าโปรเจกต์
- แชร์ plugin กับทีม

### สิ่งที่ไม่ควรทำ
- อย่าสร้างฟีเจอร์ที่ซ้ำซ้อน
- อย่า hardcode ข้อมูลประจำตัว
- อย่าข้ามการจัดทำเอกสาร
- อย่าทำให้งานง่ายซับซ้อนเกินจำเป็น
- อย่าเพิกเฉยต่อแนวปฏิบัติด้านความปลอดภัย
- อย่า commit ข้อมูลที่ละเอียดอ่อน

</details>

<details>
<summary>การแก้ปัญหา</summary>

### ฟีเจอร์ไม่โหลด
1. ตรวจสอบตำแหน่งและการตั้งชื่อไฟล์
2. ตรวจสอบไวยากรณ์ YAML frontmatter
3. ตรวจสอบสิทธิ์การเข้าถึงไฟล์
4. ตรวจสอบความเข้ากันได้ของเวอร์ชัน Claude Code

### การเชื่อมต่อ MCP ล้มเหลว
1. ตรวจสอบตัวแปรสภาพแวดล้อม
2. ตรวจสอบการติดตั้ง MCP server
3. ทดสอบข้อมูลประจำตัว
4. ตรวจสอบการเชื่อมต่อเครือข่าย

### Subagent ไม่มอบหมายงาน
1. ตรวจสอบสิทธิ์ของเครื่องมือ
2. ตรวจสอบความชัดเจนของคำอธิบาย agent
3. ตรวจสอบความซับซ้อนของงาน
4. ทดสอบ agent อย่างอิสระ

</details>

<details>
<summary>การทดสอบ</summary>

โปรเจกต์นี้มีการทดสอบอัตโนมัติแบบครบถ้วน:

- **Unit Tests**: การทดสอบ Python ด้วย pytest (Python 3.10, 3.11, 3.12)
- **Code Quality**: linting และการจัดรูปแบบด้วย Ruff
- **Security**: การสแกนหาช่องโหว่ด้วย Bandit
- **Type Checking**: การวิเคราะห์ type แบบ static ด้วย mypy
- **Build Verification**: การทดสอบการสร้าง EPUB
- **Coverage Tracking**: การเชื่อมต่อ Codecov

```bash
# Install development dependencies
uv pip install -r requirements-dev.txt

# Run all unit tests
pytest scripts/tests/ -v

# Run tests with coverage report
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run code quality checks
ruff check scripts/
ruff format --check scripts/

# Run security scan
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# Run type checking
mypy scripts/ --ignore-missing-imports
```

การทดสอบทำงานอัตโนมัติทุกครั้งที่ push ไปยัง `main`/`develop` และทุก PR ไปยัง `main` ดู [TESTING.md](../.github/TESTING.md) สำหรับข้อมูลโดยละเอียด

</details>

<details>
<summary>การสร้าง EPUB</summary>

ต้องการอ่านคู่มือนี้แบบออฟไลน์? สร้าง EPUB ebook:

```bash
uv run scripts/build_epub.py
```

คำสั่งนี้สร้าง `claude-howto-guide.epub` พร้อมเนื้อหาทั้งหมด รวมถึง Mermaid diagram ที่แสดงผลแล้ว

ดู [scripts/README.md](../scripts/README.md) สำหรับตัวเลือกเพิ่มเติม

</details>

<details>
<summary>การมีส่วนร่วม</summary>

พบปัญหาหรือต้องการมีส่วนร่วมด้วยตัวอย่าง? เรายินดีรับความช่วยเหลือของคุณ!

**โปรดอ่าน [CONTRIBUTING.md](CONTRIBUTING.md) สำหรับแนวทางโดยละเอียดเกี่ยวกับ:**
- ประเภทของการมีส่วนร่วม (ตัวอย่าง, เอกสาร, ฟีเจอร์, ข้อผิดพลาด, ข้อเสนอแนะ)
- วิธีตั้งค่าสภาพแวดล้อมการพัฒนา
- โครงสร้างไดเรกทอรีและวิธีเพิ่มเนื้อหา
- แนวทางการเขียนและแนวปฏิบัติที่ดี
- กระบวนการ commit และ PR

**มาตรฐานชุมชนของเรา:**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - วิธีที่เราปฏิบัติต่อกัน
- [SECURITY.md](SECURITY.md) - นโยบายความปลอดภัยและการรายงานช่องโหว่

### การรายงานปัญหาด้านความปลอดภัย

หากพบช่องโหว่ด้านความปลอดภัย โปรดรายงานอย่างมีความรับผิดชอบ:

1. **ใช้ GitHub Private Vulnerability Reporting**: https://github.com/luongnv89/claude-howto/security/advisories
2. **หรืออ่าน** [.github/SECURITY_REPORTING.md](../.github/SECURITY_REPORTING.md) สำหรับคำแนะนำโดยละเอียด
3. **อย่า** เปิด public issue สำหรับช่องโหว่ด้านความปลอดภัย

เริ่มต้นอย่างรวดเร็ว:
1. Fork และ clone repository
2. สร้าง branch ที่มีชื่อสื่อความหมาย (`add/feature-name`, `fix/bug`, `docs/improvement`)
3. ทำการเปลี่ยนแปลงตามแนวทาง
4. ส่ง pull request พร้อมคำอธิบายที่ชัดเจน

**ต้องการความช่วยเหลือ?** เปิด issue หรือ discussion แล้วเราจะแนะนำคุณตลอดกระบวนการ

</details>

<details>
<summary>แหล่งข้อมูลเพิ่มเติม</summary>

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - ชุด skill ที่พร้อมใช้งาน
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) - ผู้สร้าง Claude Code แชร์ workflow ที่จัดระบบไว้: agent แบบขนาน, CLAUDE.md ที่ใช้ร่วมกัน, Plan mode, slash command, subagent และ verification hook สำหรับ session ที่ทำงานอัตโนมัติเป็นเวลานาน

</details>

---

## การมีส่วนร่วม

ยินดีรับการมีส่วนร่วม! โปรดดู [คู่มือการมีส่วนร่วม](CONTRIBUTING.md) สำหรับรายละเอียดวิธีเริ่มต้น

---

## สัญญาอนุญาต

สัญญาอนุญาต MIT — ดู [LICENSE](../LICENSE) ใช้, ปรับแต่ง และเผยแพร่ได้อย่างอิสระ ข้อกำหนดเดียวคือต้องรวมประกาศสัญญาอนุญาต

---

**อัปเดตล่าสุด:** 6 พฤษภาคม 2026
**เวอร์ชัน Claude Code:** 2.1.131
**แหล่งข้อมูล:**
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.113
**รองรับ Model:** Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
