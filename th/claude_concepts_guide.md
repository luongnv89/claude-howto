<!-- i18n-source: claude_concepts_guide.md -->
<!-- i18n-date: 2026-07-15 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# คู่มือแนวคิด Claude ฉบับสมบูรณ์

คู่มืออ้างอิงที่ครอบคลุมซึ่งรวม Slash Commands, Subagents, Memory, MCP Protocol และ Agent Skills พร้อมตาราง แผนภาพ และตัวอย่างเชิงปฏิบัติ

---

## สารบัญ

1. [Slash Commands](#slash-commands)
2. [Subagents](#subagents)
3. [Memory](#memory)
4. [MCP Protocol](#mcp-protocol)
5. [Agent Skills](#agent-skills)
6. [Plugins](#claude-code-plugins)
7. [Hooks](#hooks)
8. [Checkpoints และ Rewind](#checkpoints-และ-rewind)
9. [Advanced Features](#advanced-features)
10. [การเปรียบเทียบและการผสานรวม](#การเปรียบเทียบและการผสานรวม)

---

## Slash Commands

### ภาพรวม

Slash commands คือทางลัดที่เรียกใช้โดยผู้ใช้ ซึ่งจัดเก็บเป็นไฟล์ Markdown ที่ Claude Code สามารถดำเนินการได้ ช่วยให้ทีมกำหนดมาตรฐานของ prompt และ workflow ที่ใช้บ่อยได้

### สถาปัตยกรรม

```mermaid
graph TD
    A["อินพุตผู้ใช้: /command-name"] -->|ทริกเกอร์| B["ค้นหาใน .claude/commands/"]
    B -->|พบ| C["command-name.md"]
    C -->|โหลด| D["เนื้อหา Markdown"]
    D -->|ดำเนินการ| E["Claude ประมวลผล Prompt"]
    E -->|ส่งคืน| F["ผลลัพธ์ในบริบท"]
```

### โครงสร้างไฟล์

```mermaid
graph LR
    A["Project Root"] -->|ประกอบด้วย| B[".claude/commands/"]
    B -->|ประกอบด้วย| C["optimize.md"]
    B -->|ประกอบด้วย| D["test.md"]
    B -->|ประกอบด้วย| E["docs/"]
    E -->|ประกอบด้วย| F["generate-api-docs.md"]
    E -->|ประกอบด้วย| G["generate-readme.md"]
```

### ตารางการจัดระเบียบ Command

| ตำแหน่ง | ขอบเขต | ความพร้อมใช้งาน | กรณีการใช้งาน | ติดตามด้วย Git |
|----------|-------|--------------|----------|-------------|
| `.claude/commands/` | เฉพาะโครงการ | สมาชิกในทีม | workflow ของทีม มาตรฐานที่ใช้ร่วมกัน | ✅ ใช่ |
| `~/.claude/commands/` | ส่วนตัว | ผู้ใช้แต่ละคน | ทางลัดส่วนตัวข้ามโครงการ | ❌ ไม่ |
| Subdirectories | มีเนมสเปซ | ตามโฟลเดอร์แม่ | จัดระเบียบตามหมวดหมู่ | ✅ ใช่ |

### ฟีเจอร์และความสามารถ

| ฟีเจอร์ | ตัวอย่าง | รองรับ |
|---------|---------|-----------|
| การดำเนินการ shell script | `bash scripts/deploy.sh` | ✅ ใช่ |
| การอ้างอิงไฟล์ | `@path/to/file.js` | ✅ ใช่ |
| การผสาน Bash | `$(git log --oneline)` | ✅ ใช่ |
| Arguments | `/pr --verbose` | ✅ ใช่ |
| MCP commands | `/mcp__github__list_prs` | ✅ ใช่ |

### ตัวอย่างเชิงปฏิบัติ

#### ตัวอย่างที่ 1: Command สำหรับการปรับปรุงประสิทธิภาพโค้ด

**ไฟล์:** `.claude/commands/optimize.md`

```markdown
---
name: Code Optimization
description: Analyze code for performance issues and suggest optimizations
tags: performance, analysis
---

# การปรับปรุงประสิทธิภาพโค้ด

ตรวจสอบโค้ดที่ให้มาสำหรับปัญหาต่อไปนี้ตามลำดับความสำคัญ:

1. **คอขวดด้านประสิทธิภาพ** - ระบุการดำเนินการ O(n²) ลูปที่ไม่มีประสิทธิภาพ
2. **Memory leaks** - ค้นหาทรัพยากรที่ไม่ได้ปลดปล่อย การอ้างอิงแบบวนซ้ำ
3. **การปรับปรุงอัลกอริทึม** - แนะนำอัลกอริทึมหรือโครงสร้างข้อมูลที่ดีกว่า
4. **โอกาสในการทำ caching** - ระบุการคำนวณที่เกิดซ้ำ
5. **ปัญหา concurrency** - ค้นหา race condition หรือปัญหา threading

จัดรูปแบบคำตอบด้วย:
- ระดับความรุนแรงของปัญหา (Critical/High/Medium/Low)
- ตำแหน่งในโค้ด
- คำอธิบาย
- การแก้ไขที่แนะนำพร้อมตัวอย่างโค้ด
```

**การใช้งาน:**
```bash
# ผู้ใช้พิมพ์ใน Claude Code
/optimize

# Claude โหลด prompt แล้วรอรับอินพุตโค้ด
```

#### ตัวอย่างที่ 2: Command ช่วยเตรียม Pull Request

**ไฟล์:** `.claude/commands/pr.md`

```markdown
---
name: Prepare Pull Request
description: Clean up code, stage changes, and prepare a pull request
tags: git, workflow
---

# รายการตรวจสอบการเตรียม Pull Request

ก่อนสร้าง PR ให้ดำเนินการขั้นตอนเหล่านี้:

1. รัน linting: `prettier --write .`
2. รันการทดสอบ: `npm test`
3. ตรวจสอบ git diff: `git diff HEAD`
4. Stage การเปลี่ยนแปลง: `git add .`
5. สร้าง commit message ตาม conventional commits:
   - `fix:` สำหรับการแก้ไขบั๊ก
   - `feat:` สำหรับฟีเจอร์ใหม่
   - `docs:` สำหรับเอกสาร
   - `refactor:` สำหรับการปรับโครงสร้างโค้ด
   - `test:` สำหรับการเพิ่มการทดสอบ
   - `chore:` สำหรับงานบำรุงรักษา

6. สร้างสรุป PR ที่รวม:
   - สิ่งที่เปลี่ยนแปลง
   - เหตุผลที่เปลี่ยนแปลง
   - การทดสอบที่ดำเนินการ
   - ผลกระทบที่อาจเกิดขึ้น
```

**การใช้งาน:**
```bash
/pr

# Claude ดำเนินการตามรายการตรวจสอบและเตรียม PR
```

#### ตัวอย่างที่ 3: ตัวสร้างเอกสารแบบลำดับชั้น

**ไฟล์:** `.claude/commands/docs/generate-api-docs.md`

```markdown
---
name: Generate API Documentation
description: Create comprehensive API documentation from source code
tags: documentation, api
---

# ตัวสร้างเอกสาร API

สร้างเอกสาร API โดย:

1. สแกนไฟล์ทั้งหมดใน `/src/api/`
2. ดึง function signatures และ JSDoc comments
3. จัดระเบียบตาม endpoint/module
4. สร้าง markdown พร้อมตัวอย่าง
5. รวม schema ของ request/response
6. เพิ่มเอกสารข้อผิดพลาด

รูปแบบผลลัพธ์:
- ไฟล์ Markdown ใน `/docs/api.md`
- รวมตัวอย่าง curl สำหรับทุก endpoint
- เพิ่ม TypeScript types
```

### แผนภาพวงจรชีวิตของ Command

```mermaid
sequenceDiagram
    participant User as ผู้ใช้
    participant Claude as Claude Code
    participant FS as ระบบไฟล์
    participant CLI as Shell/Bash

    User->>Claude: พิมพ์ /optimize
    Claude->>FS: ค้นหาใน .claude/commands/
    FS-->>Claude: ส่งคืน optimize.md
    Claude->>Claude: โหลดเนื้อหา Markdown
    Claude->>User: แสดงบริบทของ prompt
    User->>Claude: ให้โค้ดเพื่อวิเคราะห์
    Claude->>CLI: (อาจดำเนินการ scripts)
    CLI-->>Claude: ผลลัพธ์
    Claude->>User: ส่งคืนการวิเคราะห์
```

### แนวปฏิบัติที่ดี

| ✅ ควรทำ | ❌ ไม่ควรทำ |
|------|---------|
| ใช้ชื่อที่ชัดเจนและมุ่งเน้นการกระทำ | สร้าง command สำหรับงานที่ทำครั้งเดียว |
| บันทึก trigger words ในคำอธิบาย | สร้างตรรกะซับซ้อนใน command |
| รักษา command ให้มุ่งเน้นงานเดียว | สร้าง command ที่ซ้ำซ้อน |
| ควบคุมเวอร์ชันของ command ระดับโครงการ | Hardcode ข้อมูลที่ละเอียดอ่อน |
| จัดระเบียบใน subdirectories | สร้างรายการ command ที่ยาวเกินไป |
| ใช้ prompt ที่เรียบง่ายและอ่านง่าย | ใช้ถ้อยคำแบบย่อหรือกำกวม |

---

## Subagents

### ภาพรวม

Subagents คือผู้ช่วย AI เฉพาะทางที่มี context window แยกต่างหากและ system prompt ที่กำหนดเอง ช่วยให้สามารถมอบหมายงานให้ดำเนินการได้ พร้อมทั้งรักษาการแยกความรับผิดชอบให้ชัดเจน

### แผนภาพสถาปัตยกรรม

```mermaid
graph TB
    User["👤 ผู้ใช้"]
    Main["🎯 Main Agent<br/>(ผู้ประสานงาน)"]
    Reviewer["🔍 Code Reviewer<br/>Subagent"]
    Tester["✅ Test Engineer<br/>Subagent"]
    Docs["📝 Documentation<br/>Subagent"]

    User -->|ถาม| Main
    Main -->|มอบหมาย| Reviewer
    Main -->|มอบหมาย| Tester
    Main -->|มอบหมาย| Docs
    Reviewer -->|ส่งคืนผลลัพธ์| Main
    Tester -->|ส่งคืนผลลัพธ์| Main
    Docs -->|ส่งคืนผลลัพธ์| Main
    Main -->|สังเคราะห์| User
```

### วงจรชีวิตของ Subagent

```mermaid
sequenceDiagram
    participant User as ผู้ใช้
    participant MainAgent as Main Agent
    participant CodeReviewer as Code Reviewer<br/>Subagent
    participant Context as Context Window<br/>แยกต่างหาก

    User->>MainAgent: "สร้างฟีเจอร์ auth ใหม่"
    MainAgent->>MainAgent: วิเคราะห์งาน
    MainAgent->>CodeReviewer: "รีวิวโค้ดนี้"
    CodeReviewer->>Context: เริ่มต้น context ที่สะอาด
    Context->>CodeReviewer: โหลดคำสั่งของ reviewer
    CodeReviewer->>CodeReviewer: ดำเนินการรีวิว
    CodeReviewer-->>MainAgent: ส่งคืนสิ่งที่พบ
    MainAgent->>MainAgent: รวมผลลัพธ์
    MainAgent-->>User: ให้ผลลัพธ์ที่สังเคราะห์แล้ว
```

### ตารางการกำหนดค่า Subagent

| การกำหนดค่า | ประเภท | จุดประสงค์ | ตัวอย่าง |
|---------------|------|---------|---------|
| `name` | String | ตัวระบุ agent | `code-reviewer` |
| `description` | String | จุดประสงค์และคำที่ทริกเกอร์ | `Comprehensive code quality analysis` |
| `tools` | List/String | ความสามารถที่อนุญาต | `read, grep, diff, lint_runner` |
| `system_prompt` | Markdown | คำสั่งด้านพฤติกรรม | แนวทางที่กำหนดเอง |

### ลำดับชั้นการเข้าถึงเครื่องมือ

```mermaid
graph TD
    A["Subagent Configuration"] -->|ตัวเลือก 1| B["สืบทอดเครื่องมือทั้งหมด<br/>จาก Main Thread"]
    A -->|ตัวเลือก 2| C["ระบุเครื่องมือทีละรายการ"]
    B -->|รวมถึง| B1["File Operations"]
    B -->|รวมถึง| B2["Shell Commands"]
    B -->|รวมถึง| B3["MCP Tools"]
    C -->|รายการที่ระบุชัดเจน| C1["read, grep, diff"]
    C -->|รายการที่ระบุชัดเจน| C2["Bash(npm:*), Bash(test:*)"]
```

### ตัวอย่างเชิงปฏิบัติ

#### ตัวอย่างที่ 1: การตั้งค่า Subagent แบบสมบูรณ์

**ไฟล์:** `.claude/agents/code-reviewer.md`

```yaml
---
name: code-reviewer
description: Comprehensive code quality and maintainability analysis
tools: read, grep, diff, lint_runner
---

# Code Reviewer Agent

You are an expert code reviewer specializing in:
- Performance optimization
- Security vulnerabilities
- Code maintainability
- Testing coverage
- Design patterns

## Review Priorities (in order)

1. **Security Issues** - Authentication, authorization, data exposure
2. **Performance Problems** - O(n²) operations, memory leaks, inefficient queries
3. **Code Quality** - Readability, naming, documentation
4. **Test Coverage** - Missing tests, edge cases
5. **Design Patterns** - SOLID principles, architecture

## Review Output Format

For each issue:
- **Severity**: Critical / High / Medium / Low
- **Category**: Security / Performance / Quality / Testing / Design
- **Location**: File path and line number
- **Issue Description**: What's wrong and why
- **Suggested Fix**: Code example
- **Impact**: How this affects the system

## Example Review

### Issue: N+1 Query Problem
- **Severity**: High
- **Category**: Performance
- **Location**: src/user-service.ts:45
- **Issue**: Loop executes database query in each iteration
- **Fix**: Use JOIN or batch query
```

**ไฟล์:** `.claude/agents/test-engineer.md`

```yaml
---
name: test-engineer
description: Test strategy, coverage analysis, and automated testing
tools: read, write, bash, grep
---

# Test Engineer Agent

You are expert at:
- Writing comprehensive test suites
- Ensuring high code coverage (>80%)
- Testing edge cases and error scenarios
- Performance benchmarking
- Integration testing

## Testing Strategy

1. **Unit Tests** - Individual functions/methods
2. **Integration Tests** - Component interactions
3. **End-to-End Tests** - Complete workflows
4. **Edge Cases** - Boundary conditions
5. **Error Scenarios** - Failure handling

## Test Output Requirements

- Use Jest for JavaScript/TypeScript
- Include setup/teardown for each test
- Mock external dependencies
- Document test purpose
- Include performance assertions when relevant

## Coverage Requirements

- Minimum 80% code coverage
- 100% for critical paths
- Report missing coverage areas
```

**ไฟล์:** `.claude/agents/documentation-writer.md`

```yaml
---
name: documentation-writer
description: Technical documentation, API docs, and user guides
tools: read, write, grep
---

# Documentation Writer Agent

You create:
- API documentation with examples
- User guides and tutorials
- Architecture documentation
- Changelog entries
- Code comment improvements

## Documentation Standards

1. **Clarity** - Use simple, clear language
2. **Examples** - Include practical code examples
3. **Completeness** - Cover all parameters and returns
4. **Structure** - Use consistent formatting
5. **Accuracy** - Verify against actual code

## Documentation Sections

### For APIs
- Description
- Parameters (with types)
- Returns (with types)
- Throws (possible errors)
- Examples (curl, JavaScript, Python)
- Related endpoints

### For Features
- Overview
- Prerequisites
- Step-by-step instructions
- Expected outcomes
- Troubleshooting
- Related topics
```

#### ตัวอย่างที่ 2: การมอบหมายงานให้ Subagent ในทางปฏิบัติ

```markdown
# สถานการณ์: การสร้างฟีเจอร์การชำระเงิน

## คำขอของผู้ใช้
"สร้างฟีเจอร์ประมวลผลการชำระเงินที่ปลอดภัยซึ่งผสานรวมกับ Stripe"

## กระแสการทำงานของ Main Agent

1. **ระยะวางแผน**
   - ทำความเข้าใจข้อกำหนด
   - กำหนดงานที่จำเป็น
   - วางแผนสถาปัตยกรรม

2. **มอบหมายให้ Code Reviewer Subagent**
   - งาน: "รีวิวการ implement การประมวลผลการชำระเงินด้านความปลอดภัย"
   - Context: Auth, API keys, การจัดการ token
   - รีวิวสำหรับ: SQL injection, การเปิดเผย key, การบังคับใช้ HTTPS

3. **มอบหมายให้ Test Engineer Subagent**
   - งาน: "สร้างการทดสอบที่ครอบคลุมสำหรับกระแสการชำระเงิน"
   - Context: สถานการณ์สำเร็จ, ล้มเหลว, edge case
   - สร้างการทดสอบสำหรับ: การชำระเงินที่ถูกต้อง, บัตรถูกปฏิเสธ, เครือข่ายล้มเหลว, webhook

4. **มอบหมายให้ Documentation Writer Subagent**
   - งาน: "จัดทำเอกสาร endpoint ของ payment API"
   - Context: schema ของ request/response
   - ผลผลิต: เอกสาร API พร้อมตัวอย่าง curl, error code

5. **การสังเคราะห์**
   - Main agent รวบรวมผลลัพธ์ทั้งหมด
   - ผสานรวมสิ่งที่พบ
   - ส่งคืนโซลูชันที่สมบูรณ์ให้ผู้ใช้
```

#### ตัวอย่างที่ 3: การกำหนดขอบเขตสิทธิ์ของเครื่องมือ

**การตั้งค่าแบบจำกัด - จำกัดเฉพาะคำสั่งบางอย่าง**

```yaml
---
name: secure-reviewer
description: Security-focused code review with minimal permissions
tools: read, grep
---

# Secure Code Reviewer

Reviews code for security vulnerabilities only.

This agent:
- ✅ Reads files to analyze
- ✅ Searches for patterns
- ❌ Cannot execute code
- ❌ Cannot modify files
- ❌ Cannot run tests

This ensures the reviewer doesn't accidentally break anything.
```

**การตั้งค่าแบบขยาย - เครื่องมือทั้งหมดสำหรับการ implement**

```yaml
---
name: implementation-agent
description: Full implementation capabilities for feature development
tools: read, write, bash, grep, edit, glob
---

# Implementation Agent

Builds features from specifications.

This agent:
- ✅ Reads specifications
- ✅ Writes new code files
- ✅ Runs build commands
- ✅ Searches codebase
- ✅ Edits existing files
- ✅ Finds files matching patterns

Full capabilities for independent feature development.
```

### การจัดการ Context ของ Subagent

```mermaid
graph TB
    A["Main Agent Context<br/>50,000 tokens"]
    B["Subagent 1 Context<br/>20,000 tokens"]
    C["Subagent 2 Context<br/>20,000 tokens"]
    D["Subagent 3 Context<br/>20,000 tokens"]

    A -->|เริ่มต้นใหม่| B
    A -->|เริ่มต้นใหม่| C
    A -->|เริ่มต้นใหม่| D

    B -->|เฉพาะผลลัพธ์| A
    C -->|เฉพาะผลลัพธ์| A
    D -->|เฉพาะผลลัพธ์| A

    style A fill:#e1f5ff
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

### เมื่อใดควรใช้ Subagent

| สถานการณ์ | ใช้ Subagent | เหตุผล |
|----------|--------------|-----|
| ฟีเจอร์ซับซ้อนที่มีหลายขั้นตอน | ✅ ใช่ | แยกความรับผิดชอบ ป้องกันการปนเปื้อน context |
| การรีวิวโค้ดอย่างรวดเร็ว | ❌ ไม่ | ไม่จำเป็นและเพิ่ม overhead |
| การดำเนินการงานแบบขนาน | ✅ ใช่ | แต่ละ subagent มี context ของตัวเอง |
| ต้องการความเชี่ยวชาญเฉพาะทาง | ✅ ใช่ | system prompt ที่กำหนดเอง |
| การวิเคราะห์ที่ใช้เวลานาน | ✅ ใช่ | ป้องกันการใช้ context หลักจนหมด |
| งานเดียว | ❌ ไม่ | เพิ่ม latency โดยไม่จำเป็น |

### Agent Teams

Agent Teams ประสานงาน agent หลายตัวที่ทำงานในงานที่เกี่ยวข้องกัน แทนที่จะมอบหมายให้ subagent ทีละตัว Agent Teams ช่วยให้ main agent สามารถควบคุมกลุ่มของ agent ที่ทำงานร่วมกัน แชร์ผลลัพธ์ระหว่างทาง และทำงานไปสู่เป้าหมายร่วมกัน ซึ่งมีประโยชน์สำหรับงานขนาดใหญ่ เช่น การพัฒนาฟีเจอร์แบบ full-stack ที่ frontend agent, backend agent และ testing agent ทำงานแบบขนานกัน

---

## Memory

### ภาพรวม

Memory ช่วยให้ Claude สามารถเก็บ context ข้าม session และการสนทนาต่างๆ ได้ มีอยู่สองรูปแบบ: การสังเคราะห์อัตโนมัติใน claude.ai และ CLAUDE.md ที่อิงกับระบบไฟล์ใน Claude Code

### สถาปัตยกรรมของ Memory

```mermaid
graph TB
    A["Claude Session"]
    B["User Input"]
    C["Memory System"]
    D["Memory Storage"]

    B -->|ผู้ใช้ให้ข้อมูล| C
    C -->|สังเคราะห์ทุก 24 ชม.| D
    D -->|โหลดอัตโนมัติ| A
    A -->|ใช้ context| C
```

### ลำดับชั้นของ Memory ใน Claude Code (7 ระดับ)

Claude Code โหลด memory จาก 7 ระดับ เรียงจากลำดับความสำคัญสูงสุดไปต่ำสุด:

```mermaid
graph TD
    A["1. Managed Policy<br/>นโยบายผู้ดูแลระดับองค์กร"] --> B["2. Project Memory<br/>./CLAUDE.md"]
    B --> C["3. Project Rules<br/>.claude/rules/*.md"]
    C --> D["4. User Memory<br/>~/.claude/CLAUDE.md"]
    D --> E["5. User Rules<br/>~/.claude/rules/*.md"]
    E --> F["6. Local Memory<br/>.claude/local/CLAUDE.md"]
    F --> G["7. Auto Memory<br/>การตั้งค่าที่ถูกจับอัตโนมัติ"]

    style A fill:#fce4ec,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e1f5fe,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
    style G fill:#fff3e0,stroke:#333,color:#333
```

### ตารางตำแหน่งของ Memory

| ระดับ | ตำแหน่ง | ขอบเขต | ลำดับความสำคัญ | แชร์ | เหมาะสำหรับ |
|------|----------|-------|----------|--------|----------|
| 1. Managed Policy | ผู้ดูแลระดับองค์กร | องค์กร | สูงสุด | ผู้ใช้ทั้งองค์กร | การปฏิบัติตามข้อกำหนด, นโยบายความปลอดภัย |
| 2. Project | `./CLAUDE.md` | โปรเจกต์ | สูง | ทีม (Git) | มาตรฐานทีม, สถาปัตยกรรม |
| 3. Project Rules | `.claude/rules/*.md` | โปรเจกต์ | สูง | ทีม (Git) | ข้อตกลงโปรเจกต์แบบโมดูลาร์ |
| 4. User | `~/.claude/CLAUDE.md` | ส่วนตัว | ปานกลาง | รายบุคคล | การตั้งค่าส่วนตัว |
| 5. User Rules | `~/.claude/rules/*.md` | ส่วนตัว | ปานกลาง | รายบุคคล | โมดูลกฎส่วนตัว |
| 6. Local | `.claude/local/CLAUDE.md` | Local | ต่ำ | ไม่แชร์ | การตั้งค่าเฉพาะเครื่อง |
| 7. Auto Memory | อัตโนมัติ | Session | ต่ำสุด | รายบุคคล | การตั้งค่าและรูปแบบที่เรียนรู้ |

### Auto Memory

Auto Memory จับการตั้งค่าและรูปแบบของผู้ใช้ที่สังเกตได้ระหว่าง session โดยอัตโนมัติ Claude เรียนรู้จากการโต้ตอบของคุณและจดจำ:

- การตั้งค่าสไตล์การเขียนโค้ด
- การแก้ไขที่คุณทำบ่อยๆ
- การเลือก framework และเครื่องมือ
- การตั้งค่าสไตล์การสื่อสาร

Auto Memory ทำงานเบื้องหลังและไม่ต้องการการกำหนดค่าด้วยตนเอง

### วงจรชีวิตการอัปเดต Memory

```mermaid
sequenceDiagram
    participant User as ผู้ใช้
    participant Claude as Claude Code
    participant Editor as ระบบไฟล์
    participant Memory as CLAUDE.md

    User->>Claude: "จดจำไว้: ใช้ async/await"
    Claude->>User: "ไฟล์ memory ไหน?"
    User->>Claude: "Project memory"
    Claude->>Editor: เปิด ~/.claude/settings.json
    Claude->>Memory: เขียนลงใน ./CLAUDE.md
    Memory-->>Claude: บันทึกไฟล์แล้ว
    Claude->>Claude: โหลด memory ที่อัปเดต
    Claude-->>User: "บันทึก memory แล้ว!"
```

### ตัวอย่างเชิงปฏิบัติ

#### ตัวอย่างที่ 1: โครงสร้าง Project Memory

**ไฟล์:** `./CLAUDE.md`

```markdown
# Project Configuration

## Project Overview
- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Development Standards

### Code Style
- Use Prettier for formatting
- Use ESLint with airbnb config
- Maximum line length: 100 characters
- Use 2-space indentation

### Naming Conventions
- **Files**: kebab-case (user-controller.js)
- **Classes**: PascalCase (UserService)
- **Functions/Variables**: camelCase (getUserById)
- **Constants**: UPPER_SNAKE_CASE (API_BASE_URL)
- **Database Tables**: snake_case (user_accounts)

### Git Workflow
- Branch names: `feature/description` or `fix/description`
- Commit messages: Follow conventional commits
- PR required before merge
- All CI/CD checks must pass
- Minimum 1 approval required

### Testing Requirements
- Minimum 80% code coverage
- All critical paths must have tests
- Use Jest for unit tests
- Use Cypress for E2E tests
- Test filenames: `*.test.ts` or `*.spec.ts`

### API Standards
- RESTful endpoints only
- JSON request/response
- Use HTTP status codes correctly
- Version API endpoints: `/api/v1/`
- Document all endpoints with examples

### Database
- Use migrations for schema changes
- Never hardcode credentials
- Use connection pooling
- Enable query logging in development
- Regular backups required

### Deployment
- Docker-based deployment
- Kubernetes orchestration
- Blue-green deployment strategy
- Automatic rollback on failure
- Database migrations run before deploy

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start development server |
| `npm test` | Run test suite |
| `npm run lint` | Check code style |
| `npm run build` | Build for production |
| `npm run migrate` | Run database migrations |

## Team Contacts
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Known Issues & Workarounds
- PostgreSQL connection pooling limited to 20 during peak hours
- Workaround: Implement query queuing
- Safari 14 compatibility issues with async generators
- Workaround: Use Babel transpiler

## Related Projects
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
```

#### ตัวอย่างที่ 2: Memory เฉพาะไดเรกทอรี

**ไฟล์:** `./src/api/CLAUDE.md`

~~~~markdown
# API Module Standards

This file overrides root CLAUDE.md for everything in /src/api/

## API-Specific Standards

### Request Validation
- Use Zod for schema validation
- Always validate input
- Return 400 with validation errors
- Include field-level error details

### Authentication
- All endpoints require JWT token
- Token in Authorization header
- Token expires after 24 hours
- Implement refresh token mechanism

### Response Format

All responses must follow this structure:

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

### Error responses:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Pagination
- Use cursor-based pagination (not offset)
- Include `hasMore` boolean
- Limit max page size to 100
- Default page size: 20

### Rate Limiting
- 1000 requests per hour for authenticated users
- 100 requests per hour for public endpoints
- Return 429 when exceeded
- Include retry-after header

### Caching
- Use Redis for session caching
- Cache duration: 5 minutes default
- Invalidate on write operations
- Tag cache keys with resource type
~~~~

#### ตัวอย่างที่ 3: Personal Memory

**ไฟล์:** `~/.claude/CLAUDE.md`

~~~~markdown
# My Development Preferences

## About Me
- **Experience Level**: 8 years full-stack development
- **Preferred Languages**: TypeScript, Python
- **Communication Style**: Direct, with examples
- **Learning Style**: Visual diagrams with code

## Code Preferences

### Error Handling
I prefer explicit error handling with try-catch blocks and meaningful error messages.
Avoid generic errors. Always log errors for debugging.

### Comments
Use comments for WHY, not WHAT. Code should be self-documenting.
Comments should explain business logic or non-obvious decisions.

### Testing
I prefer TDD (test-driven development).
Write tests first, then implementation.
Focus on behavior, not implementation details.

### Architecture
I prefer modular, loosely-coupled design.
Use dependency injection for testability.
Separate concerns (Controllers, Services, Repositories).

## Debugging Preferences
- Use console.log with prefix: `[DEBUG]`
- Include context: function name, relevant variables
- Use stack traces when available
- Always include timestamps in logs

## Communication
- Explain complex concepts with diagrams
- Show concrete examples before explaining theory
- Include before/after code snippets
- Summarize key points at the end

## Project Organization
I organize my projects as:
```
project/
  ├── src/
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  ├── docs/
  └── docker/
```

## Tooling
- **IDE**: VS Code with vim keybindings
- **Terminal**: Zsh with Oh-My-Zsh
- **Format**: Prettier (100 char line length)
- **Linter**: ESLint with airbnb config
- **Test Framework**: Jest with React Testing Library
~~~~

#### ตัวอย่างที่ 4: การอัปเดต Memory ระหว่าง Session

**การโต้ตอบใน Session:**

```markdown
User: Remember that I prefer using React hooks instead of class components
     for all new components.

Claude: I'm adding that to your memory. Which memory file should this go in?
        1. Project memory (./CLAUDE.md)
        2. Personal memory (~/.claude/CLAUDE.md)

User: Project memory

Claude: ✅ Memory saved!

Added to ./CLAUDE.md:
---

### Component Development
- Use functional components with React Hooks
- Prefer hooks over class components
- Custom hooks for reusable logic
- Use useCallback for event handlers
- Use useMemo for expensive computations
```

### Memory ใน Claude Web/Desktop

#### ไทม์ไลน์การสังเคราะห์ Memory

```mermaid
graph LR
    A["วันที่ 1: การสนทนา<br/>ของผู้ใช้"] -->|24 ชั่วโมง| B["วันที่ 2: การสังเคราะห์<br/>Memory"]
    B -->|อัตโนมัติ| C["Memory อัปเดต<br/>สรุปแล้ว"]
    C -->|โหลดใน| D["วันที่ 2-N:<br/>การสนทนาใหม่"]
    D -->|เพิ่มไปยัง| E["Memory"]
    E -->|24 ชั่วโมงต่อมา| F["Memory รีเฟรช"]
```

**ตัวอย่างสรุป Memory:**

```markdown
## Claude's Memory of User

### Professional Background
- Senior full-stack developer with 8 years experience
- Focus on TypeScript/Node.js backends and React frontends
- Active open source contributor
- Interested in AI and machine learning

### Project Context
- Currently building e-commerce platform
- Tech stack: Node.js, PostgreSQL, React 18, Docker
- Working with team of 5 developers
- Using CI/CD and blue-green deployments

### Communication Preferences
- Prefers direct, concise explanations
- Likes visual diagrams and examples
- Appreciates code snippets
- Explains business logic in comments

### Current Goals
- Improve API performance
- Increase test coverage to 90%
- Implement caching strategy
- Document architecture
```

### การเปรียบเทียบฟีเจอร์ Memory

| ฟีเจอร์ | Claude Web/Desktop | Claude Code (CLAUDE.md) |
|---------|-------------------|------------------------|
| การสังเคราะห์อัตโนมัติ | ✅ ทุก 24 ชม. | ❌ ด้วยตนเอง |
| ข้ามโปรเจกต์ | ✅ แชร์ | ❌ เฉพาะโปรเจกต์ |
| การเข้าถึงของทีม | ✅ โปรเจกต์ที่แชร์ | ✅ ติดตามด้วย Git |
| ค้นหาได้ | ✅ ในตัว | ✅ ผ่าน `/memory` |
| แก้ไขได้ | ✅ ในแชท | ✅ แก้ไขไฟล์โดยตรง |
| นำเข้า/ส่งออก | ✅ ใช่ | ✅ คัดลอก/วาง |
| คงอยู่ถาวร | ✅ 24 ชม.+ | ✅ ไม่จำกัด |

---

## MCP Protocol

### ภาพรวม

MCP (Model Context Protocol) คือวิธีมาตรฐานที่ Claude ใช้เข้าถึงเครื่องมือภายนอก, API และแหล่งข้อมูลแบบเรียลไทม์ ต่างจาก Memory ตรงที่ MCP ให้การเข้าถึงข้อมูลที่เปลี่ยนแปลงแบบสด

### สถาปัตยกรรม MCP

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A
```

### ระบบนิเวศ MCP

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]
```

### กระบวนการตั้งค่า MCP

```mermaid
sequenceDiagram
    participant User as ผู้ใช้
    participant Claude as Claude Code
    participant Config as ไฟล์ Config
    participant Service as External Service

    User->>Claude: พิมพ์ /mcp
    Claude->>Claude: แสดงรายการ MCP server ที่มี
    Claude->>User: แสดงตัวเลือก
    User->>Claude: เลือก GitHub MCP
    Claude->>Config: อัปเดตการกำหนดค่า
    Config->>Claude: เปิดใช้งานการเชื่อมต่อ
    Claude->>Service: ทดสอบการเชื่อมต่อ
    Service-->>Claude: ยืนยันตัวตนสำเร็จ
    Claude->>User: ✅ เชื่อมต่อ MCP แล้ว!
```

### ตาราง MCP Server ที่มีให้ใช้

| MCP Server | จุดประสงค์ | เครื่องมือทั่วไป | Auth | เรียลไทม์ |
|------------|---------|--------------|------|-----------|
| **Filesystem** | การดำเนินการกับไฟล์ | read, write, delete | สิทธิ์ OS | ✅ ใช่ |
| **GitHub** | การจัดการ repository | list_prs, create_issue, push | OAuth | ✅ ใช่ |
| **Slack** | การสื่อสารในทีม | send_message, list_channels | Token | ✅ ใช่ |
| **Database** | SQL queries | query, insert, update | Credentials | ✅ ใช่ |
| **Google Docs** | การเข้าถึงเอกสาร | read, write, share | OAuth | ✅ ใช่ |
| **Asana** | การจัดการโปรเจกต์ | create_task, update_status | API Key | ✅ ใช่ |
| **Stripe** | ข้อมูลการชำระเงิน | list_charges, create_invoice | API Key | ✅ ใช่ |
| **Memory** | Memory ถาวร | store, retrieve, delete | Local | ❌ ไม่ |

### ตัวอย่างเชิงปฏิบัติ

#### ตัวอย่างที่ 1: การกำหนดค่า GitHub MCP

**ไฟล์:** `.mcp.json` (ขอบเขตโปรเจกต์) หรือ `~/.claude.json` (ขอบเขตผู้ใช้)

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**เครื่องมือ GitHub MCP ที่มีให้ใช้:**

~~~~markdown
# GitHub MCP Tools

## Pull Request Management
- `list_prs` - List all PRs in repository
- `get_pr` - Get PR details including diff
- `create_pr` - Create new PR
- `update_pr` - Update PR description/title
- `merge_pr` - Merge PR to main branch
- `review_pr` - Add review comments

Example request:
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

## Issue Management
- `list_issues` - List all issues
- `get_issue` - Get issue details
- `create_issue` - Create new issue
- `close_issue` - Close issue
- `add_comment` - Add comment to issue

## Repository Information
- `get_repo_info` - Repository details
- `list_files` - File tree structure
- `get_file_content` - Read file contents
- `search_code` - Search across codebase

## Commit Operations
- `list_commits` - Commit history
- `get_commit` - Specific commit details
- `create_commit` - Create new commit
~~~~

#### ตัวอย่างที่ 2: การตั้งค่า Database MCP

**การกำหนดค่า:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-database"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

**ตัวอย่างการใช้งาน:**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Using MCP database tool:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Results:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

#### ตัวอย่างที่ 3: Workflow แบบหลาย MCP

**สถานการณ์: การสร้างรายงานประจำวัน**

```markdown
# Daily Report Workflow using Multiple MCPs

## Setup
1. GitHub MCP - fetch PR metrics
2. Database MCP - query sales data
3. Slack MCP - post report
4. Filesystem MCP - save report

## Workflow

### Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Step 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Step 3: Generate Report
Combine data into HTML report

### Step 4: Save to Filesystem
Write report.html to /reports/

### Step 5: Post to Slack
Send summary to #daily-reports channel

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

#### ตัวอย่างที่ 4: การดำเนินการ Filesystem MCP

**การกำหนดค่า:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**การดำเนินการที่มีให้ใช้:**

| การดำเนินการ | คำสั่ง | จุดประสงค์ |
|-----------|---------|---------|
| แสดงรายการไฟล์ | `ls ~/projects` | แสดงเนื้อหาไดเรกทอรี |
| อ่านไฟล์ | `cat src/main.ts` | อ่านเนื้อหาไฟล์ |
| เขียนไฟล์ | `create docs/api.md` | สร้างไฟล์ใหม่ |
| แก้ไขไฟล์ | `edit src/app.ts` | แก้ไขไฟล์ |
| ค้นหา | `grep "async function"` | ค้นหาในไฟล์ |
| ลบ | `rm old-file.js` | ลบไฟล์ |

### MCP vs Memory: เมทริกซ์การตัดสินใจ

```mermaid
graph TD
    A["ต้องการข้อมูลภายนอกหรือไม่?"]
    A -->|ไม่| B["ใช้ Memory"]
    A -->|ใช่| C["ข้อมูลเปลี่ยนแปลงบ่อยหรือไม่?"]
    C -->|ไม่/นานๆ ครั้ง| B
    C -->|ใช่/บ่อย| D["ใช้ MCP"]

    B -->|จัดเก็บ| E["Preferences<br/>Context<br/>History"]
    D -->|เข้าถึง| F["Live APIs<br/>Databases<br/>Services"]

    style B fill:#e1f5ff
    style D fill:#fff9c4
```

### รูปแบบ Request/Response

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: ดำเนินการ query
    DB-->>MCP: ชุดผลลัพธ์
    MCP-->>App: ส่งคืนข้อมูลที่ parse แล้ว
    App->>App: ประมวลผลผลลัพธ์
    App->>App: ทำงานต่อ

    Note over MCP,DB: การเข้าถึงแบบเรียลไทม์<br/>ไม่มี caching
```

---

## Agent Skills

### ภาพรวม

Agent Skills คือความสามารถที่นำกลับมาใช้ใหม่ได้และเรียกใช้โดยโมเดล ซึ่งบรรจุเป็นโฟลเดอร์ที่มีคำสั่ง, script และทรัพยากร Claude ตรวจจับและใช้ skill ที่เกี่ยวข้องโดยอัตโนมัติ

### สถาปัตยกรรม Skill

```mermaid
graph TB
    A["Skill Directory"]
    B["SKILL.md"]
    C["YAML Metadata"]
    D["Instructions"]
    E["Scripts"]
    F["Templates"]

    A --> B
    B --> C
    B --> D
    E --> A
    F --> A
```

### กระบวนการโหลด Skill

```mermaid
sequenceDiagram
    participant User as ผู้ใช้
    participant Claude as Claude
    participant System as System
    participant Skill as Skill

    User->>Claude: "สร้างรายงาน Excel"
    Claude->>System: สแกน skill ที่มี
    System->>System: โหลด metadata ของ skill
    Claude->>Claude: จับคู่คำขอของผู้ใช้กับ skill
    Claude->>Skill: โหลด SKILL.md ของ skill xlsx
    Skill-->>Claude: ส่งคืนคำสั่ง + เครื่องมือ
    Claude->>Claude: ดำเนินการ skill
    Claude->>User: สร้างไฟล์ Excel
```

### ตารางประเภทและตำแหน่งของ Skill

| ประเภท | ตำแหน่ง | ขอบเขต | แชร์ | Sync | เหมาะสำหรับ |
|------|----------|-------|--------|------|----------|
| Pre-built | ในตัว | Global | ผู้ใช้ทั้งหมด | อัตโนมัติ | การสร้างเอกสาร |
| Personal | `~/.claude/skills/` | รายบุคคล | ไม่ | ด้วยตนเอง | automation ส่วนตัว |
| Project | `.claude/skills/` | ทีม | ใช่ | Git | มาตรฐานทีม |
| Plugin | ผ่านการติดตั้ง plugin | แตกต่างกัน | ขึ้นอยู่กับ | อัตโนมัติ | ฟีเจอร์ที่ผสานรวม |

### Skill สำเร็จรูป (Pre-built)

```mermaid
graph TB
    A["Pre-built Skills"]
    B["PowerPoint (pptx)"]
    C["Excel (xlsx)"]
    D["Word (docx)"]
    E["PDF"]

    A --> B
    A --> C
    A --> D
    A --> E

    B --> B1["Create presentations"]
    B --> B2["Edit slides"]
    C --> C1["Create spreadsheets"]
    C --> C2["Analyze data"]
    D --> D1["Create documents"]
    D --> D2["Format text"]
    E --> E1["Generate PDFs"]
    E --> E2["Fill forms"]
```

### Skill ที่มาพร้อมกับระบบ (Bundled)

ปัจจุบัน Claude Code มี skill ที่มาพร้อมกับระบบ 5 ตัวที่พร้อมใช้งานทันที:

| Skill | คำสั่ง | จุดประสงค์ |
|-------|---------|---------|
| **Simplify** | `/simplify` | ทำให้โค้ดหรือคำอธิบายที่ซับซ้อนเรียบง่ายขึ้น |
| **Batch** | `/batch` | รันการดำเนินการกับหลายไฟล์หรือหลายรายการ |
| **Debug** | `/debug` | การดีบักปัญหาอย่างเป็นระบบพร้อมการวิเคราะห์สาเหตุที่แท้จริง |
| **Loop** | `/loop` | ตั้งเวลางานที่ทำซ้ำตามตัวจับเวลา |
| **Claude API** | `/claude-api` | โต้ตอบกับ Anthropic API โดยตรง |

Skill ที่มาพร้อมกับระบบเหล่านี้พร้อมใช้งานเสมอและไม่ต้องการการติดตั้งหรือการกำหนดค่า

### ตัวอย่างเชิงปฏิบัติ

#### ตัวอย่างที่ 1: Skill รีวิวโค้ดแบบกำหนดเอง

**โครงสร้างไดเรกทอรี:**

```
~/.claude/skills/code-review/
├── SKILL.md
├── templates/
│   ├── review-checklist.md
│   └── finding-template.md
└── scripts/
    ├── analyze-metrics.py
    └── compare-complexity.py
```

**ไฟล์:** `~/.claude/skills/code-review/SKILL.md`

```yaml
---
name: Code Review Specialist
description: Comprehensive code review with security, performance, and quality analysis
version: "1.0.0"
tags:
  - code-review
  - quality
  - security
when_to_use: When users ask to review code, analyze code quality, or evaluate pull requests
effort: high
shell: bash
---

# Code Review Skill

This skill provides comprehensive code review capabilities focusing on:

1. **Security Analysis**
   - Authentication/authorization issues
   - Data exposure risks
   - Injection vulnerabilities
   - Cryptographic weaknesses
   - Sensitive data logging

2. **Performance Review**
   - Algorithm efficiency (Big O analysis)
   - Memory optimization
   - Database query optimization
   - Caching opportunities
   - Concurrency issues

3. **Code Quality**
   - SOLID principles
   - Design patterns
   - Naming conventions
   - Documentation
   - Test coverage

4. **Maintainability**
   - Code readability
   - Function size (should be < 50 lines)
   - Cyclomatic complexity
   - Dependency management
   - Type safety

## Review Template

For each piece of code reviewed, provide:

### Summary
- Overall quality assessment (1-5)
- Key findings count
- Recommended priority areas

### Critical Issues (if any)
- **Issue**: Clear description
- **Location**: File and line number
- **Impact**: Why this matters
- **Severity**: Critical/High/Medium
- **Fix**: Code example

### Findings by Category

#### Security (if issues found)
List security vulnerabilities with examples

#### Performance (if issues found)
List performance problems with complexity analysis

#### Quality (if issues found)
List code quality issues with refactoring suggestions

#### Maintainability (if issues found)
List maintainability problems with improvements
```
## Python Script: analyze-metrics.py

```python
#!/usr/bin/env python3
import re
import sys

def analyze_code_metrics(code):
    """Analyze code for common metrics."""

    # Count functions
    functions = len(re.findall(r'^def\s+\w+', code, re.MULTILINE))

    # Count classes
    classes = len(re.findall(r'^class\s+\w+', code, re.MULTILINE))

    # Average line length
    lines = code.split('\n')
    avg_length = sum(len(l) for l in lines) / len(lines) if lines else 0

    # Estimate complexity
    complexity = len(re.findall(r'\b(if|elif|else|for|while|and|or)\b', code))

    return {
        'functions': functions,
        'classes': classes,
        'avg_line_length': avg_length,
        'complexity_score': complexity
    }

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    metrics = analyze_code_metrics(code)
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")
```

## Python Script: compare-complexity.py

```python
#!/usr/bin/env python3
"""
Compare cyclomatic complexity of code before and after changes.
Helps identify if refactoring actually simplifies code structure.
"""

import re
import sys
from typing import Dict, Tuple

class ComplexityAnalyzer:
    """Analyze code complexity metrics."""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split('\n')

    def calculate_cyclomatic_complexity(self) -> int:
        """
        Calculate cyclomatic complexity using McCabe's method.
        Count decision points: if, elif, else, for, while, except, and, or
        """
        complexity = 1  # Base complexity

        # Count decision points
        decision_patterns = [
            r'\bif\b',
            r'\belif\b',
            r'\bfor\b',
            r'\bwhile\b',
            r'\bexcept\b',
            r'\band\b(?!$)',
            r'\bor\b(?!$)'
        ]

        for pattern in decision_patterns:
            matches = re.findall(pattern, self.code)
            complexity += len(matches)

        return complexity

    def calculate_cognitive_complexity(self) -> int:
        """
        Calculate cognitive complexity - how hard is it to understand?
        Based on nesting depth and control flow.
        """
        cognitive = 0
        nesting_depth = 0

        for line in self.lines:
            # Track nesting depth
            if re.search(r'^\s*(if|for|while|def|class|try)\b', line):
                nesting_depth += 1
                cognitive += nesting_depth
            elif re.search(r'^\s*(elif|else|except|finally)\b', line):
                cognitive += nesting_depth

            # Reduce nesting when unindenting
            if line and not line[0].isspace():
                nesting_depth = 0

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        Maintainability Index ranges from 0-100.
        > 85: Excellent
        > 65: Good
        > 50: Fair
        < 50: Poor
        """
        lines = len(self.lines)
        cyclomatic = self.calculate_cyclomatic_complexity()
        cognitive = self.calculate_cognitive_complexity()

        # Simplified MI calculation
        mi = 171 - 5.2 * (cyclomatic / lines) - 0.23 * (cognitive) - 16.2 * (lines / 1000)

        return max(0, min(100, mi))

    def get_complexity_report(self) -> Dict:
        """Generate comprehensive complexity report."""
        return {
            'cyclomatic_complexity': self.calculate_cyclomatic_complexity(),
            'cognitive_complexity': self.calculate_cognitive_complexity(),
            'maintainability_index': round(self.calculate_maintainability_index(), 2),
            'lines_of_code': len(self.lines),
            'avg_line_length': round(sum(len(l) for l in self.lines) / len(self.lines), 2) if self.lines else 0
        }


def compare_files(before_file: str, after_file: str) -> None:
    """Compare complexity metrics between two code versions."""

    with open(before_file, 'r') as f:
        before_code = f.read()

    with open(after_file, 'r') as f:
        after_code = f.read()

    before_analyzer = ComplexityAnalyzer(before_code)
    after_analyzer = ComplexityAnalyzer(after_code)

    before_metrics = before_analyzer.get_complexity_report()
    after_metrics = after_analyzer.get_complexity_report()

    print("=" * 60)
    print("CODE COMPLEXITY COMPARISON")
    print("=" * 60)

    print("\nBEFORE:")
    print(f"  Cyclomatic Complexity:    {before_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {before_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {before_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {before_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {before_metrics['avg_line_length']}")

    print("\nAFTER:")
    print(f"  Cyclomatic Complexity:    {after_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {after_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {after_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {after_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {after_metrics['avg_line_length']}")

    print("\nCHANGES:")
    cyclomatic_change = after_metrics['cyclomatic_complexity'] - before_metrics['cyclomatic_complexity']
    cognitive_change = after_metrics['cognitive_complexity'] - before_metrics['cognitive_complexity']
    mi_change = after_metrics['maintainability_index'] - before_metrics['maintainability_index']
    loc_change = after_metrics['lines_of_code'] - before_metrics['lines_of_code']

    print(f"  Cyclomatic Complexity:    {cyclomatic_change:+d}")
    print(f"  Cognitive Complexity:     {cognitive_change:+d}")
    print(f"  Maintainability Index:    {mi_change:+.2f}")
    print(f"  Lines of Code:            {loc_change:+d}")

    print("\nASSESSMENT:")
    if mi_change > 0:
        print("  ✅ Code is MORE maintainable")
    elif mi_change < 0:
        print("  ⚠️  Code is LESS maintainable")
    else:
        print("  ➡️  Maintainability unchanged")

    if cyclomatic_change < 0:
        print("  ✅ Complexity DECREASED")
    elif cyclomatic_change > 0:
        print("  ⚠️  Complexity INCREASED")
    else:
        print("  ➡️  Complexity unchanged")

    print("=" * 60)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare-complexity.py <before_file> <after_file>")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
```

## Template: review-checklist.md

```markdown
# Code Review Checklist

## Security Checklist
- [ ] No hardcoded credentials or secrets
- [ ] Input validation on all user inputs
- [ ] SQL injection prevention (parameterized queries)
- [ ] CSRF protection on state-changing operations
- [ ] XSS prevention with proper escaping
- [ ] Authentication checks on protected endpoints
- [ ] Authorization checks on resources
- [ ] Secure password hashing (bcrypt, argon2)
- [ ] No sensitive data in logs
- [ ] HTTPS enforced

## Performance Checklist
- [ ] No N+1 queries
- [ ] Appropriate use of indexes
- [ ] Caching implemented where beneficial
- [ ] No blocking operations on main thread
- [ ] Async/await used correctly
- [ ] Large datasets paginated
- [ ] Database connections pooled
- [ ] Regular expressions optimized
- [ ] No unnecessary object creation
- [ ] Memory leaks prevented

## Quality Checklist
- [ ] Functions < 50 lines
- [ ] Clear variable naming
- [ ] No duplicate code
- [ ] Proper error handling
- [ ] Comments explain WHY, not WHAT
- [ ] No console.logs in production
- [ ] Type checking (TypeScript/JSDoc)
- [ ] SOLID principles followed
- [ ] Design patterns applied correctly
- [ ] Self-documenting code

## Testing Checklist
- [ ] Unit tests written
- [ ] Edge cases covered
- [ ] Error scenarios tested
- [ ] Integration tests present
- [ ] Coverage > 80%
- [ ] No flaky tests
- [ ] Mock external dependencies
- [ ] Clear test names
```

## Template: finding-template.md

~~~~markdown
# Code Review Finding Template

Use this template when documenting each issue found during code review.

---

## Issue: [TITLE]

### Severity
- [ ] Critical (blocks deployment)
- [ ] High (should fix before merge)
- [ ] Medium (should fix soon)
- [ ] Low (nice to have)

### Category
- [ ] Security
- [ ] Performance
- [ ] Code Quality
- [ ] Maintainability
- [ ] Testing
- [ ] Design Pattern
- [ ] Documentation

### Location
**File:** `src/components/UserCard.tsx`

**Lines:** 45-52

**Function/Method:** `renderUserDetails()`

### Issue Description

**What:** Describe what the issue is.

**Why it matters:** Explain the impact and why this needs to be fixed.

**Current behavior:** Show the problematic code or behavior.

**Expected behavior:** Describe what should happen instead.

### Code Example

#### Current (Problematic)

```typescript
// Shows the N+1 query problem
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // Query per user!
  renderUserPosts(posts);
});
```

#### Suggested Fix

```typescript
// Optimized with JOIN query
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### Impact Analysis

| Aspect | Impact | Severity |
|--------|--------|----------|
| Performance | 100+ queries for 20 users | High |
| User Experience | Slow page load | High |
| Scalability | Breaks at scale | Critical |
| Maintainability | Hard to debug | Medium |

### Related Issues

- Similar issue in `AdminUserList.tsx` line 120
- Related PR: #456
- Related issue: #789

### Additional Resources

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)

### Reviewer Notes

- This is a common pattern in this codebase
- Consider adding this to the code style guide
- Might be worth creating a helper function

### Author Response (for feedback)

*To be filled by the code author:*

- [ ] Fix implemented in commit: `abc123`
- [ ] Fix status: Complete / In Progress / Needs Discussion
- [ ] Questions or concerns: (describe)

---

## Finding Statistics (for Reviewer)

When reviewing multiple findings, track:

- **Total Issues Found:** X
- **Critical:** X
- **High:** X
- **Medium:** X
- **Low:** X

**Recommendation:** ✅ Approve / ⚠️ Request Changes / 🔄 Needs Discussion

**Overall Code Quality:** 1-5 stars
~~~~

## Usage Example

~~~~markdown
User: Review this React component code

Claude: I'll conduct a comprehensive code review using my Code Review Skill.

[Loads SKILL.md]
[Analyzes code against checklist]
[Runs Python metrics script]
[Applies templates]

## Code Review Results

### Summary
Quality Score: 3.5/5
Key Findings: 7 items
Priority Areas: Performance optimization, error handling

### Critical Issues: 1

**Issue**: N+1 Query Problem
**Location**: UserComponent.tsx, lines 45-52
**Impact**: Renders 100+ database queries for list of 20 users
**Severity**: High
**Fix**:
```javascript
// Before: N+1 queries
const users = fetchUsers();
users.forEach(user => fetchUserPosts(user.id)); // 20+ queries

// After: Single query with JOIN
const users = fetchUsersWithPosts(); // 1 query
```

### Performance Findings
- Missing pagination on large lists
- Recommendation: Use React.memo() for items
- Database query: Could be optimized with index

### Quality Findings
- Function in line 20 is 127 lines (max: 50)
- Missing error boundary
- Props should have TypeScript types
~~~~

#### ตัวอย่างที่ 2: Skill สำหรับ Brand Voice

**โครงสร้างไดเรกทอรี:**

```
.claude/skills/brand-voice/
├── SKILL.md
├── brand-guidelines.md
├── tone-examples.md
└── templates/
    ├── email-template.txt
    ├── social-post-template.txt
    └── blog-post-template.md
```

**ไฟล์:** `.claude/skills/brand-voice/SKILL.md`

```yaml
---
name: Brand Voice Consistency
description: Ensure all communication matches brand voice and tone guidelines
tags:
  - brand
  - writing
  - consistency
when_to_use: When creating marketing copy, customer communications, or public-facing content
---

# Brand Voice Skill

## Overview
This skill ensures all communications maintain consistent brand voice, tone, and messaging.

## Brand Identity

### Mission
Help teams automate their development workflows with AI

### Values
- **Simplicity**: Make complex things simple
- **Reliability**: Rock-solid execution
- **Empowerment**: Enable human creativity

### Tone of Voice
- **Friendly but professional** - approachable without being casual
- **Clear and concise** - avoid jargon, explain technical concepts simply
- **Confident** - we know what we're doing
- **Empathetic** - understand user needs and pain points

## Writing Guidelines

### Do's ✅
- Use "you" when addressing readers
- Use active voice: "Claude generates reports" not "Reports are generated by Claude"
- Start with value proposition
- Use concrete examples
- Keep sentences under 20 words
- Use lists for clarity
- Include calls-to-action

### Don'ts ❌
- Don't use corporate jargon
- Don't patronize or oversimplify
- Don't use "we believe" or "we think"
- Don't use ALL CAPS except for emphasis
- Don't create walls of text
- Don't assume technical knowledge

## Vocabulary

### ✅ Preferred Terms
- Claude (not "the Claude AI")
- Code generation (not "auto-coding")
- Agent (not "bot")
- Streamline (not "revolutionize")
- Integrate (not "synergize")

### ❌ Avoid Terms
- "Cutting-edge" (overused)
- "Game-changer" (vague)
- "Leverage" (corporate-speak)
- "Utilize" (use "use")
- "Paradigm shift" (unclear)
```
## Examples

### ✅ Good Example
"Claude automates your code review process. Instead of manually checking each PR, Claude reviews security, performance, and quality—saving your team hours every week."

Why it works: Clear value, specific benefits, action-oriented

### ❌ Bad Example
"Claude leverages cutting-edge AI to provide comprehensive software development solutions."

Why it doesn't work: Vague, corporate jargon, no specific value

## Template: Email

```
Subject: [Clear, benefit-driven subject]

Hi [Name],

[Opening: What's the value for them]

[Body: How it works / What they'll get]

[Specific example or benefit]

[Call to action: Clear next step]

Best regards,
[Name]
```

## Template: Social Media

```
[Hook: Grab attention in first line]
[2-3 lines: Value or interesting fact]
[Call to action: Link, question, or engagement]
[Emoji: 1-2 max for visual interest]
```

## File: tone-examples.md
```
Exciting announcement:
"Save 8 hours per week on code reviews. Claude reviews your PRs automatically."

Empathetic support:
"We know deployments can be stressful. Claude handles testing so you don't have to worry."

Confident product feature:
"Claude doesn't just suggest code. It understands your architecture and maintains consistency."

Educational blog post:
"Let's explore how agents improve code review workflows. Here's what we learned..."
```

#### ตัวอย่างที่ 3: Skill ตัวสร้างเอกสาร

**ไฟล์:** `.claude/skills/doc-generator/SKILL.md`

~~~~yaml
---
name: API Documentation Generator
description: Generate comprehensive, accurate API documentation from source code
version: "1.0.0"
tags:
  - documentation
  - api
  - automation
when_to_use: When creating or updating API documentation
---

# API Documentation Generator Skill

## Generates

- OpenAPI/Swagger specifications
- API endpoint documentation
- SDK usage examples
- Integration guides
- Error code references
- Authentication guides

## Documentation Structure

### For Each Endpoint

```markdown
## GET /api/v1/users/:id

### Description
Brief explanation of what this endpoint does

### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

### Response

**200 Success**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 Not Found**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "User does not exist"
}
```

### Examples

**cURL**
```bash
curl -X GET "https://api.example.com/api/v1/users/usr_123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**JavaScript**
```javascript
const user = await fetch('/api/v1/users/usr_123', {
  headers: { 'Authorization': 'Bearer token' }
}).then(r => r.json());
```

**Python**
```python
response = requests.get(
    'https://api.example.com/api/v1/users/usr_123',
    headers={'Authorization': 'Bearer token'}
)
user = response.json()
```

## Python Script: generate-docs.py

```python
#!/usr/bin/env python3
import ast
import json
from typing import Dict, List

class APIDocExtractor(ast.NodeVisitor):
    """Extract API documentation from Python source code."""

    def __init__(self):
        self.endpoints = []

    def visit_FunctionDef(self, node):
        """Extract function documentation."""
        if node.name.startswith('get_') or node.name.startswith('post_'):
            doc = ast.get_docstring(node)
            endpoint = {
                'name': node.name,
                'docstring': doc,
                'params': [arg.arg for arg in node.args.args],
                'returns': self._extract_return_type(node)
            }
            self.endpoints.append(endpoint)
        self.generic_visit(node)

    def _extract_return_type(self, node):
        """Extract return type from function annotation."""
        if node.returns:
            return ast.unparse(node.returns)
        return "Any"

def generate_markdown_docs(endpoints: List[Dict]) -> str:
    """Generate markdown documentation from endpoints."""
    docs = "# API Documentation\n\n"

    for endpoint in endpoints:
        docs += f"## {endpoint['name']}\n\n"
        docs += f"{endpoint['docstring']}\n\n"
        docs += f"**Parameters**: {', '.join(endpoint['params'])}\n\n"
        docs += f"**Returns**: {endpoint['returns']}\n\n"
        docs += "---\n\n"

    return docs

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        tree = ast.parse(f.read())

    extractor = APIDocExtractor()
    extractor.visit(tree)

    markdown = generate_markdown_docs(extractor.endpoints)
    print(markdown)
~~~~
### การค้นพบและการเรียกใช้ Skill

```mermaid
graph TD
    A["User Request"] --> B["Claude Analyzes"]
    B -->|สแกน| C["Available Skills"]
    C -->|ตรวจสอบ metadata| D["Skill Description Match?"]
    D -->|ใช่| E["Load SKILL.md"]
    D -->|ไม่| F["Try next skill"]
    F -->|มี skill เพิ่มเติม?| D
    F -->|ไม่มีแล้ว| G["Use general knowledge"]
    E --> H["Extract Instructions"]
    H --> I["Execute Skill"]
    I --> J["Return Results"]
```

### Skill vs ฟีเจอร์อื่นๆ

```mermaid
graph TB
    A["Extending Claude"]
    B["Slash Commands"]
    C["Subagents"]
    D["Memory"]
    E["MCP"]
    F["Skills"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F

    B -->|เรียกโดยผู้ใช้| G["Quick shortcuts"]
    C -->|มอบหมายอัตโนมัติ| H["Isolated contexts"]
    D -->|คงอยู่ถาวร| I["Cross-session context"]
    E -->|เรียลไทม์| J["External data access"]
    F -->|เรียกอัตโนมัติ| K["Autonomous execution"]
```

---

## Claude Code Plugins

### ภาพรวม

Claude Code Plugins คือชุดของการปรับแต่งที่รวมเข้าด้วยกัน (slash command, subagent, MCP server และ hook) ซึ่งติดตั้งได้ด้วยคำสั่งเดียว plugin เป็นกลไกการขยายระดับสูงสุด โดยรวมหลายฟีเจอร์เข้าเป็นแพ็กเกจที่เชื่อมโยงกันและแชร์ได้

### สถาปัตยกรรม

```mermaid
graph TB
    A["Plugin"]
    B["Slash Commands"]
    C["Subagents"]
    D["MCP Servers"]
    E["Hooks"]
    F["Configuration"]

    A -->|รวม| B
    A -->|รวม| C
    A -->|รวม| D
    A -->|รวม| E
    A -->|รวม| F
```

### กระบวนการโหลด Plugin

```mermaid
sequenceDiagram
    participant User as ผู้ใช้
    participant Claude as Claude Code
    participant Plugin as Plugin Marketplace
    participant Install as Installation
    participant SlashCmds as Slash Commands
    participant Subagents
    participant MCPServers as MCP Servers
    participant Hooks
    participant Tools as Configured Tools

    User->>Claude: /plugin install pr-review
    Claude->>Plugin: ดาวน์โหลด plugin manifest
    Plugin-->>Claude: ส่งคืนคำนิยาม plugin
    Claude->>Install: แยกส่วนประกอบ
    Install->>SlashCmds: กำหนดค่า
    Install->>Subagents: กำหนดค่า
    Install->>MCPServers: กำหนดค่า
    Install->>Hooks: กำหนดค่า
    SlashCmds-->>Tools: พร้อมใช้งาน
    Subagents-->>Tools: พร้อมใช้งาน
    MCPServers-->>Tools: พร้อมใช้งาน
    Hooks-->>Tools: พร้อมใช้งาน
    Tools-->>Claude: ติดตั้ง plugin แล้ว ✅
```

### ประเภทและการเผยแพร่ Plugin

| ประเภท | ขอบเขต | แชร์ | ผู้รับผิดชอบ | ตัวอย่าง |
|------|-------|--------|-----------|----------|
| Official | Global | ผู้ใช้ทั้งหมด | Anthropic | PR Review, Security Guidance |
| Community | สาธารณะ | ผู้ใช้ทั้งหมด | ชุมชน | DevOps, Data Science |
| Organization | ภายใน | สมาชิกในทีม | บริษัท | มาตรฐานและเครื่องมือภายใน |
| Personal | รายบุคคล | ผู้ใช้คนเดียว | นักพัฒนา | workflow ที่กำหนดเอง |

### โครงสร้างคำนิยาม Plugin

```yaml
---
name: plugin-name
version: "1.0.0"
description: "What this plugin does"
author: "Your Name"
license: MIT

# Plugin metadata
tags:
  - category
  - use-case

# Requirements
requires:
  - claude-code: ">=1.0.0"

# Components bundled
components:
  - type: commands
    path: commands/
  - type: agents
    path: agents/
  - type: mcp
    path: mcp/
  - type: hooks
    path: hooks/

# Configuration
config:
  auto_load: true
  enabled_by_default: true
---
```

### โครงสร้าง Plugin

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── task-1.md
│   ├── task-2.md
│   └── workflows/
├── agents/
│   ├── specialist-1.md
│   ├── specialist-2.md
│   └── configs/
├── skills/
│   ├── skill-1.md
│   └── skill-2.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── .lsp.json
├── settings.json
├── templates/
│   └── issue-template.md
├── scripts/
│   ├── helper-1.sh
│   └── helper-2.py
├── docs/
│   ├── README.md
│   └── USAGE.md
└── tests/
    └── plugin.test.js
```

### ตัวอย่างเชิงปฏิบัติ

#### ตัวอย่างที่ 1: Plugin สำหรับรีวิว PR

**ไฟล์:** `.claude-plugin/plugin.json`

```json
{
  "name": "pr-review",
  "version": "1.0.0",
  "description": "Complete PR review workflow with security, testing, and docs",
  "author": {
    "name": "Anthropic"
  },
  "license": "MIT"
}
```

**ไฟล์:** `commands/review-pr.md`

```markdown
---
name: Review PR
description: Start comprehensive PR review with security and testing checks
---

# PR Review

This command initiates a complete pull request review including:

1. Security analysis
2. Test coverage verification
3. Documentation updates
4. Code quality checks
5. Performance impact assessment
```

**ไฟล์:** `agents/security-reviewer.md`

```yaml
---
name: security-reviewer
description: Security-focused code review
tools: read, grep, diff
---

# Security Reviewer

Specializes in finding security vulnerabilities:
- Authentication/authorization issues
- Data exposure
- Injection attacks
- Secure configuration
```

**การติดตั้ง:**

```bash
/plugin install pr-review

# Result:
# ✅ 3 slash commands installed
# ✅ 3 subagents configured
# ✅ 2 MCP servers connected
# ✅ 4 hooks registered
# ✅ Ready to use!
```

#### ตัวอย่างที่ 2: Plugin สำหรับ DevOps

**ส่วนประกอบ:**

```
devops-automation/
├── commands/
│   ├── deploy.md
│   ├── rollback.md
│   ├── status.md
│   └── incident.md
├── agents/
│   ├── deployment-specialist.md
│   ├── incident-commander.md
│   └── alert-analyzer.md
├── mcp/
│   ├── github-config.json
│   ├── kubernetes-config.json
│   └── prometheus-config.json
├── hooks/
│   ├── pre-deploy.js
│   ├── post-deploy.js
│   └── on-error.js
└── scripts/
    ├── deploy.sh
    ├── rollback.sh
    └── health-check.sh
```

#### ตัวอย่างที่ 3: Plugin สำหรับเอกสาร

**ส่วนประกอบที่รวมมา:**

```
documentation/
├── commands/
│   ├── generate-api-docs.md
│   ├── generate-readme.md
│   ├── sync-docs.md
│   └── validate-docs.md
├── agents/
│   ├── api-documenter.md
│   ├── code-commentator.md
│   └── example-generator.md
├── mcp/
│   ├── github-docs-config.json
│   └── slack-announce-config.json
└── templates/
    ├── api-endpoint.md
    ├── function-docs.md
    └── adr-template.md
```

### Plugin Marketplace

```mermaid
graph TB
    A["Plugin Marketplace"]
    B["Official<br/>Anthropic"]
    C["Community<br/>Marketplace"]
    D["Enterprise<br/>Registry"]

    A --> B
    A --> C
    A --> D

    B -->|หมวดหมู่| B1["Development"]
    B -->|หมวดหมู่| B2["DevOps"]
    B -->|หมวดหมู่| B3["Documentation"]

    C -->|ค้นหา| C1["DevOps Automation"]
    C -->|ค้นหา| C2["Mobile Dev"]
    C -->|ค้นหา| C3["Data Science"]

    D -->|ภายใน| D1["Company Standards"]
    D -->|ภายใน| D2["Legacy Systems"]
    D -->|ภายใน| D3["Compliance"]
```

### การติดตั้งและวงจรชีวิตของ Plugin

```mermaid
graph LR
    A["Discover"] -->|Browse| B["Marketplace"]
    B -->|Select| C["Plugin Page"]
    C -->|View| D["Components"]
    D -->|Install| E["/plugin install"]
    E -->|Extract| F["Configure"]
    F -->|Activate| G["Use"]
    G -->|Check| H["Update"]
    H -->|Available| G
    G -->|Done| I["Disable"]
    I -->|Later| J["Enable"]
    J -->|Back| G
```

### การเปรียบเทียบฟีเจอร์ Plugin

| ฟีเจอร์ | Slash Command | Skill | Subagent | Plugin |
|---------|---------------|-------|----------|--------|
| **การติดตั้ง** | คัดลอกด้วยตนเอง | คัดลอกด้วยตนเอง | กำหนดค่าด้วยตนเอง | คำสั่งเดียว |
| **เวลาตั้งค่า** | 5 นาที | 10 นาที | 15 นาที | 2 นาที |
| **การรวมชุด** | ไฟล์เดียว | ไฟล์เดียว | ไฟล์เดียว | หลายไฟล์ |
| **การจัดเวอร์ชัน** | ด้วยตนเอง | ด้วยตนเอง | ด้วยตนเอง | อัตโนมัติ |
| **การแชร์กับทีม** | คัดลอกไฟล์ | คัดลอกไฟล์ | คัดลอกไฟล์ | Install ID |
| **การอัปเดต** | ด้วยตนเอง | ด้วยตนเอง | ด้วยตนเอง | มีให้อัตโนมัติ |
| **Dependencies** | ไม่มี | ไม่มี | ไม่มี | อาจมี |
| **Marketplace** | ไม่ | ไม่ | ไม่ | ใช่ |
| **การเผยแพร่** | Repository | Repository | Repository | Marketplace |

### กรณีการใช้งาน Plugin

| กรณีการใช้งาน | คำแนะนำ | เหตุผล |
|----------|-----------------|-----|
| **การ Onboarding ทีม** | ✅ ใช้ Plugin | ตั้งค่าทันที มีการกำหนดค่าครบ |
| **การตั้งค่า Framework** | ✅ ใช้ Plugin | รวมคำสั่งเฉพาะ framework |
| **มาตรฐานองค์กร** | ✅ ใช้ Plugin | เผยแพร่จากส่วนกลาง ควบคุมเวอร์ชัน |
| **การ Automate งานเร็วๆ** | ❌ ใช้ Command | ซับซ้อนเกินความจำเป็น |
| **ความเชี่ยวชาญเดี่ยว** | ❌ ใช้ Skill | หนักเกินไป ใช้ skill แทน |
| **การวิเคราะห์เฉพาะทาง** | ❌ ใช้ Subagent | สร้างเองหรือใช้ skill |
| **การเข้าถึงข้อมูลสด** | ❌ ใช้ MCP | ใช้แบบเดี่ยว ไม่ต้องรวมชุด |

### เมื่อใดควรสร้าง Plugin

```mermaid
graph TD
    A["ควรสร้าง plugin หรือไม่?"]
    A -->|ต้องการหลายส่วนประกอบ| B{"มีหลาย command<br/>หรือ subagent<br/>หรือ MCP?"}
    B -->|ใช่| C["✅ สร้าง Plugin"]
    B -->|ไม่| D["ใช้ฟีเจอร์เดี่ยว"]
    A -->|Workflow ของทีม| E{"แชร์กับ<br/>ทีมหรือไม่?"}
    E -->|ใช่| C
    E -->|ไม่| F["เก็บเป็นการตั้งค่าแบบ Local"]
    A -->|การตั้งค่าซับซ้อน| G{"ต้องการการกำหนดค่า<br/>อัตโนมัติหรือไม่?"}
    G -->|ใช่| C
    G -->|ไม่| D
```

### การเผยแพร่ Plugin

**ขั้นตอนการเผยแพร่:**

1. สร้างโครงสร้าง plugin พร้อมส่วนประกอบทั้งหมด
2. เขียน manifest `.claude-plugin/plugin.json`
3. สร้าง `README.md` พร้อมเอกสาร
4. ทดสอบในเครื่องด้วย `/plugin install ./my-plugin`
5. ส่งไปยัง plugin marketplace
6. ผ่านการรีวิวและอนุมัติ
7. เผยแพร่บน marketplace
8. ผู้ใช้ติดตั้งได้ด้วยคำสั่งเดียว

**ตัวอย่างการส่ง:**

~~~~markdown
# PR Review Plugin

## Description
Complete PR review workflow with security, testing, and documentation checks.

## What's Included
- 3 slash commands for different review types
- 3 specialized subagents
- GitHub and CodeQL MCP integration
- Automated security scanning hooks

## Installation
```bash
/plugin install pr-review
```

## Features
✅ Security analysis
✅ Test coverage checking
✅ Documentation verification
✅ Code quality assessment
✅ Performance impact analysis

## Usage
```bash
/review-pr
/check-security
/check-tests
```

## Requirements
- Claude Code 1.0+
- GitHub access
- CodeQL (optional)
~~~~

### Plugin vs การกำหนดค่าด้วยตนเอง

**การตั้งค่าด้วยตนเอง (2+ ชั่วโมง):**
- ติดตั้ง slash command ทีละตัว
- สร้าง subagent ทีละตัว
- กำหนดค่า MCP แยกกัน
- ตั้งค่า hook ด้วยตนเอง
- จัดทำเอกสารทุกอย่าง
- แชร์กับทีม (หวังว่าพวกเขาจะกำหนดค่าถูกต้อง)

**ด้วย Plugin (2 นาที):**
```bash
/plugin install pr-review
# ✅ Everything installed and configured
# ✅ Ready to use immediately
# ✅ Team can reproduce exact setup
```

---

## การเปรียบเทียบและการผสานรวม

### เมทริกซ์เปรียบเทียบฟีเจอร์

| ฟีเจอร์ | การเรียกใช้ | ความคงอยู่ | ขอบเขต | กรณีการใช้งาน |
|---------|-----------|------------|-------|----------|
| **Slash Commands** | ด้วยตนเอง (`/cmd`) | เฉพาะ session | คำสั่งเดียว | ทางลัดด่วน |
| **Subagents** | มอบหมายอัตโนมัติ | context แยกต่างหาก | งานเฉพาะทาง | กระจายงาน |
| **Memory** | โหลดอัตโนมัติ | ข้าม session | context ผู้ใช้/ทีม | การเรียนรู้ระยะยาว |
| **MCP Protocol** | query อัตโนมัติ | ภายนอกแบบเรียลไทม์ | เข้าถึงข้อมูลสด | ข้อมูลแบบ dynamic |
| **Skills** | เรียกอัตโนมัติ | อิงระบบไฟล์ | ความเชี่ยวชาญที่นำกลับมาใช้ | workflow อัตโนมัติ |

### ไทม์ไลน์การโต้ตอบ

```mermaid
graph LR
    A["Session Start"] -->|Load| B["Memory (CLAUDE.md)"]
    B -->|Discover| C["Available Skills"]
    C -->|Register| D["Slash Commands"]
    D -->|Connect| E["MCP Servers"]
    E -->|Ready| F["User Interaction"]

    F -->|Type /cmd| G["Slash Command"]
    F -->|Request| H["Skill Auto-Invoke"]
    F -->|Query| I["MCP Data"]
    F -->|Complex task| J["Delegate to Subagent"]

    G -->|Uses| B
    H -->|Uses| B
    I -->|Uses| B
    J -->|Uses| B
```

### ตัวอย่างการผสานรวมเชิงปฏิบัติ: การ Automate งานสนับสนุนลูกค้า

#### สถาปัตยกรรม

```mermaid
graph TB
    User["Customer Email"] -->|Receives| Router["Support Router"]

    Router -->|Analyze| Memory["Memory<br/>Customer history"]
    Router -->|Lookup| MCP1["MCP: Customer DB<br/>Previous tickets"]
    Router -->|Check| MCP2["MCP: Slack<br/>Team status"]

    Router -->|Route Complex| Sub1["Subagent: Tech Support<br/>Context: Technical issues"]
    Router -->|Route Simple| Sub2["Subagent: Billing<br/>Context: Payment issues"]
    Router -->|Route Urgent| Sub3["Subagent: Escalation<br/>Context: Priority handling"]

    Sub1 -->|Format| Skill1["Skill: Response Generator<br/>Brand voice maintained"]
    Sub2 -->|Format| Skill2["Skill: Response Generator"]
    Sub3 -->|Format| Skill3["Skill: Response Generator"]

    Skill1 -->|Generate| Output["Formatted Response"]
    Skill2 -->|Generate| Output
    Skill3 -->|Generate| Output

    Output -->|Post| MCP3["MCP: Slack<br/>Notify team"]
    Output -->|Send| Reply["Customer Reply"]
```

#### กระแสของคำขอ

```markdown
## Customer Support Request Flow

### 1. Incoming Email
"I'm getting error 500 when trying to upload files. This is blocking my workflow!"

### 2. Memory Lookup
- Loads CLAUDE.md with support standards
- Checks customer history: VIP customer, 3rd incident this month

### 3. MCP Queries
- GitHub MCP: List open issues (finds related bug report)
- Database MCP: Check system status (no outages reported)
- Slack MCP: Check if engineering is aware

### 4. Skill Detection & Loading
- Request matches "Technical Support" skill
- Loads support response template from Skill

### 5. Subagent Delegation
- Routes to Tech Support Subagent
- Provides context: customer history, error details, known issues
- Subagent has full access to: read, bash, grep tools

### 6. Subagent Processing
Tech Support Subagent:
- Searches codebase for 500 error in file upload
- Finds recent change in commit 8f4a2c
- Creates workaround documentation

### 7. Skill Execution
Response Generator Skill:
- Uses Brand Voice guidelines
- Formats response with empathy
- Includes workaround steps
- Links to related documentation

### 8. MCP Output
- Posts update to #support Slack channel
- Tags engineering team
- Updates ticket in Jira MCP

### 9. Response
Customer receives:
- Empathetic acknowledgment
- Explanation of cause
- Immediate workaround
- Timeline for permanent fix
- Link to related issues
```

### การประสานฟีเจอร์แบบสมบูรณ์

```mermaid
sequenceDiagram
    participant User as ผู้ใช้
    participant Claude as Claude Code
    participant Memory as Memory<br/>CLAUDE.md
    participant MCP as MCP Servers
    participant Skills as Skills
    participant SubAgent as Subagents

    User->>Claude: Request: "Build auth system"
    Claude->>Memory: โหลดมาตรฐานโปรเจกต์
    Memory-->>Claude: มาตรฐาน auth, แนวปฏิบัติของทีม
    Claude->>MCP: query GitHub หา implementation ที่คล้ายกัน
    MCP-->>Claude: ตัวอย่างโค้ด, แนวปฏิบัติที่ดี
    Claude->>Skills: ตรวจจับ Skill ที่ตรงกัน
    Skills-->>Claude: Security Review Skill + Testing Skill
    Claude->>SubAgent: มอบหมายการ implement
    SubAgent->>SubAgent: สร้างฟีเจอร์
    Claude->>Skills: ใช้ Security Review Skill
    Skills-->>Claude: ผลลัพธ์ checklist ความปลอดภัย
    Claude->>SubAgent: มอบหมายการทดสอบ
    SubAgent-->>Claude: ผลลัพธ์การทดสอบ
    Claude->>User: ส่งมอบระบบที่สมบูรณ์
```

### เมื่อใดควรใช้แต่ละฟีเจอร์

```mermaid
graph TD
    A["New Task"] --> B{Type of Task?}

    B -->|Repeated workflow| C["Slash Command"]
    B -->|Need real-time data| D["MCP Protocol"]
    B -->|Remember for next time| E["Memory"]
    B -->|Specialized subtask| F["Subagent"]
    B -->|Domain-specific work| G["Skill"]

    C --> C1["✅ Team shortcut"]
    D --> D1["✅ Live API access"]
    E --> E1["✅ Persistent context"]
    F --> F1["✅ Parallel execution"]
    G --> G1["✅ Auto-invoked expertise"]
```

### แผนผังการตัดสินใจในการเลือก

```mermaid
graph TD
    Start["Need to extend Claude?"]

    Start -->|Quick repeated task| A{"Manual or Auto?"}
    A -->|Manual| B["Slash Command"]
    A -->|Auto| C["Skill"]

    Start -->|Need external data| D{"Real-time?"}
    D -->|Yes| E["MCP Protocol"]
    D -->|No/Cross-session| F["Memory"]

    Start -->|Complex project| G{"Multiple roles?"}
    G -->|Yes| H["Subagents"]
    G -->|No| I["Skills + Memory"]

    Start -->|Long-term context| J["Memory"]
    Start -->|Team workflow| K["Slash Command +<br/>Memory"]
    Start -->|Full automation| L["Skills +<br/>Subagents +<br/>MCP"]
```

---

## Summary Table

| ด้าน | Slash Commands | Subagents | Memory | MCP | Skills | Plugins |
|--------|---|---|---|---|---|---|
| **ความยากในการตั้งค่า** | ง่าย | ปานกลาง | ง่าย | ปานกลาง | ปานกลาง | ง่าย |
| **ความชันของการเรียนรู้** | ต่ำ | ปานกลาง | ต่ำ | ปานกลาง | ปานกลาง | ต่ำ |
| **ประโยชน์ต่อทีม** | สูง | สูง | ปานกลาง | สูง | สูง | สูงมาก |
| **ระดับ Automation** | ต่ำ | สูง | ปานกลาง | สูง | สูง | สูงมาก |
| **การจัดการ Context** | Session เดียว | แยกต่างหาก | คงอยู่ถาวร | เรียลไทม์ | คงอยู่ถาวร | ทุกฟีเจอร์ |
| **ภาระการบำรุงรักษา** | ต่ำ | ปานกลาง | ต่ำ | ปานกลาง | ปานกลาง | ต่ำ |
| **ความสามารถในการขยาย** | ดี | ดีเยี่ยม | ดี | ดีเยี่ยม | ดีเยี่ยม | ดีเยี่ยม |
| **ความสามารถในการแชร์** | พอใช้ | พอใช้ | ดี | ดี | ดี | ดีเยี่ยม |
| **การจัดเวอร์ชัน** | ด้วยตนเอง | ด้วยตนเอง | ด้วยตนเอง | ด้วยตนเอง | ด้วยตนเอง | อัตโนมัติ |
| **การติดตั้ง** | คัดลอกด้วยตนเอง | กำหนดค่าด้วยตนเอง | N/A | กำหนดค่าด้วยตนเอง | คัดลอกด้วยตนเอง | คำสั่งเดียว |

---

## Quick Start Guide

### สัปดาห์ที่ 1: เริ่มแบบเรียบง่าย
- สร้าง slash command 2-3 ตัวสำหรับงานที่ทำบ่อย
- เปิดใช้ Memory ใน Settings
- จัดทำเอกสารมาตรฐานของทีมใน CLAUDE.md

### สัปดาห์ที่ 2: เพิ่มการเข้าถึงแบบเรียลไทม์
- ตั้งค่า MCP 1 ตัว (GitHub หรือ Database)
- ใช้ `/mcp` เพื่อกำหนดค่า
- query ข้อมูลสดใน workflow ของคุณ

### สัปดาห์ที่ 3: กระจายงาน
- สร้าง Subagent ตัวแรกสำหรับบทบาทเฉพาะ
- ใช้คำสั่ง `/agents`
- ทดสอบการมอบหมายด้วยงานง่ายๆ

### สัปดาห์ที่ 4: Automate ทุกอย่าง
- สร้าง Skill ตัวแรกสำหรับ automation ที่ทำซ้ำ
- ใช้ Skill marketplace หรือสร้างเอง
- รวมทุกฟีเจอร์เข้าด้วยกันเพื่อ workflow ที่สมบูรณ์

### ทำอย่างต่อเนื่อง
- รีวิวและอัปเดต Memory ทุกเดือน
- เพิ่ม Skill ใหม่เมื่อมีรูปแบบเกิดขึ้น
- ปรับปรุง MCP query ให้เหมาะสม
- ปรับแต่ง prompt ของ Subagent

---

## Hooks

### ภาพรวม

Hooks คือคำสั่ง shell ที่ขับเคลื่อนด้วย event ซึ่งทำงานโดยอัตโนมัติเพื่อตอบสนองต่อ event ของ Claude Code ช่วยให้สามารถทำ automation การตรวจสอบ และ workflow แบบกำหนดเองได้โดยไม่ต้องดำเนินการด้วยตนเอง

### Hook Events

Claude Code รองรับ **28 hook event** ครอบคลุม hook 5 ประเภท (command, http, mcp_tool, prompt, agent):

| Hook Event | ทริกเกอร์ | กรณีการใช้งาน |
|------------|---------|-----------|
| **SessionStart** | Session เริ่ม/resume/clear/compact | ตั้งค่า environment, การเริ่มต้น |
| **InstructionsLoaded** | โหลด CLAUDE.md หรือไฟล์ rules | การตรวจสอบ, การแปลง, การเสริม |
| **UserPromptSubmit** | ผู้ใช้ส่ง prompt | ตรวจสอบ input, กรอง prompt |
| **PreToolUse** | ก่อนที่เครื่องมือใดจะทำงาน | การตรวจสอบ, ด่านอนุมัติ, logging |
| **PermissionRequest** | แสดงกล่องขอสิทธิ์ | กระแสอนุมัติ/ปฏิเสธอัตโนมัติ |
| **PostToolUse** | หลังเครื่องมือทำงานสำเร็จ | จัดรูปแบบอัตโนมัติ, แจ้งเตือน, ล้างข้อมูล |
| **PostToolUseFailure** | การทำงานของเครื่องมือล้มเหลว | จัดการข้อผิดพลาด, logging |
| **Notification** | มีการส่งการแจ้งเตือน | การแจ้งเตือน, การผสานรวมภายนอก |
| **SubagentStart** | Subagent ถูก spawn | ฉีด context, การเริ่มต้น |
| **SubagentStop** | Subagent เสร็จสิ้น | ตรวจสอบผลลัพธ์, logging |
| **Stop** | Claude ตอบเสร็จ | สร้างสรุป, งานล้างข้อมูล |
| **StopFailure** | ข้อผิดพลาด API จบ turn | กู้คืนข้อผิดพลาด, logging |
| **TeammateIdle** | teammate ใน agent team ว่าง | กระจายงาน, การประสานงาน |
| **TaskCompleted** | งานถูกทำเครื่องหมายว่าเสร็จ | การประมวลผลหลังงาน |
| **TaskCreated** | สร้างงานผ่าน TaskCreate | ติดตามงาน, logging |
| **ConfigChange** | ไฟล์ config เปลี่ยนแปลง | การตรวจสอบ, การกระจาย |
| **CwdChanged** | ไดเรกทอรีทำงานเปลี่ยน | ตั้งค่าเฉพาะไดเรกทอรี |
| **FileChanged** | ไฟล์ที่เฝ้าดูเปลี่ยนแปลง | ตรวจสอบไฟล์, ทริกเกอร์ rebuild |
| **PreCompact** | ก่อนการ compact context | รักษาสถานะ |
| **PostCompact** | หลังการ compact เสร็จ | การดำเนินการหลัง compact |
| **WorktreeCreate** | กำลังสร้าง worktree | ตั้งค่า environment, ติดตั้ง dependency |
| **WorktreeRemove** | กำลังลบ worktree | ล้างข้อมูล, คืนทรัพยากร |
| **Elicitation** | MCP server ขอ input จากผู้ใช้ | ตรวจสอบ input |
| **ElicitationResult** | ผู้ใช้ตอบสนองต่อ elicitation | ประมวลผลการตอบสนอง |
| **SessionEnd** | Session สิ้นสุด | ล้างข้อมูล, logging สุดท้าย |

### Hook ทั่วไป

Hook ถูกกำหนดค่าใน `~/.claude/settings.json` (ระดับผู้ใช้) หรือ `.claude/settings.json` (ระดับโปรเจกต์):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $CLAUDE_FILE_PATH"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "eslint $CLAUDE_FILE_PATH"
          }
        ]
      }
    ]
  }
}
```

### Environment Variable ของ Hook

- `$CLAUDE_FILE_PATH` - path ของไฟล์ที่กำลังแก้ไข/เขียน
- `$CLAUDE_TOOL_NAME` - ชื่อของเครื่องมือที่กำลังใช้
- `$CLAUDE_SESSION_ID` - ตัวระบุ session ปัจจุบัน
- `$CLAUDE_PROJECT_DIR` - path ของไดเรกทอรีโปรเจกต์

### แนวปฏิบัติที่ดี

✅ **ควรทำ:**
- ทำให้ hook เร็ว (< 1 วินาที)
- ใช้ hook สำหรับการตรวจสอบและ automation
- จัดการข้อผิดพลาดอย่างเหมาะสม
- ใช้ absolute path

❌ **ไม่ควรทำ:**
- ทำให้ hook เป็นแบบโต้ตอบ
- ใช้ hook สำหรับงานที่ใช้เวลานาน
- Hardcode credentials

**ดู**: [06-hooks/](06-hooks/) สำหรับตัวอย่างโดยละเอียด

---

## Checkpoints และ Rewind

### ภาพรวม

Checkpoints ช่วยให้คุณบันทึกสถานะการสนทนาและ rewind กลับไปยังจุดก่อนหน้าได้ ช่วยให้ทดลองและสำรวจหลายแนวทางได้อย่างปลอดภัย

### แนวคิดหลัก

| แนวคิด | คำอธิบาย |
|---------|-------------|
| **Checkpoint** | Snapshot ของสถานะการสนทนา รวมถึงข้อความ ไฟล์ และ context |
| **Rewind** | กลับไปยัง checkpoint ก่อนหน้า โดยละทิ้งการเปลี่ยนแปลงที่ตามมา |
| **Branch Point** | Checkpoint ที่ใช้สำรวจหลายแนวทางออกไป |

### การเข้าถึง Checkpoints

Checkpoint ถูกสร้างอัตโนมัติทุกครั้งที่ผู้ใช้ป้อน prompt วิธี rewind:

```bash
# กด Esc สองครั้งเพื่อเปิด checkpoint browser
Esc + Esc

# หรือใช้คำสั่ง /rewind
/rewind
```

เมื่อคุณเลือก checkpoint คุณจะเลือกจากห้าตัวเลือก:
1. **Restore code and conversation** -- ย้อนกลับทั้งสองอย่างไปยังจุดนั้น
2. **Restore conversation** -- rewind ข้อความ เก็บโค้ดปัจจุบันไว้
3. **Restore code** -- ย้อนกลับไฟล์ เก็บการสนทนาไว้
4. **Summarize from here** -- บีบอัดการสนทนาเป็นสรุป
5. **Never mind** -- ยกเลิก

### กรณีการใช้งาน

| สถานการณ์ | Workflow |
|----------|----------|
| **การสำรวจแนวทาง** | บันทึก → ลอง A → บันทึก → Rewind → ลอง B → เปรียบเทียบ |
| **การ Refactor อย่างปลอดภัย** | บันทึก → Refactor → ทดสอบ → หากล้มเหลว: Rewind |
| **การทดสอบ A/B** | บันทึก → ออกแบบ A → บันทึก → Rewind → ออกแบบ B → เปรียบเทียบ |
| **การกู้คืนจากข้อผิดพลาด** | สังเกตปัญหา → Rewind ไปยังสถานะที่ดีล่าสุด |

### การกำหนดค่า

```json
{
  "autoCheckpoint": true
}
```

**ดู**: [08-checkpoints/](08-checkpoints/) สำหรับตัวอย่างโดยละเอียด

---

## Advanced Features

### Planning Mode

สร้างแผนการ implement โดยละเอียดก่อนเขียนโค้ด

**การเปิดใช้งาน:**
```bash
/plan Implement user authentication system
```

**ประโยชน์:**
- roadmap ที่ชัดเจนพร้อมประมาณการเวลา
- การประเมินความเสี่ยง
- การแบ่งงานอย่างเป็นระบบ
- โอกาสในการรีวิวและปรับแก้

### Extended Thinking

การให้เหตุผลเชิงลึกสำหรับปัญหาที่ซับซ้อน

**การเปิดใช้งาน:**
- สลับด้วย `Alt+T` (หรือ `Option+T` บน macOS) ระหว่าง session
- ตั้งค่า environment variable `MAX_THINKING_TOKENS` เพื่อควบคุมแบบ programmatic

```bash
# เปิดใช้ extended thinking ผ่าน environment variable
export MAX_THINKING_TOKENS=50000
claude -p "Should we use microservices or monolith?"
```

**ประโยชน์:**
- วิเคราะห์ trade-off อย่างละเอียด
- การตัดสินใจด้านสถาปัตยกรรมที่ดีขึ้น
- พิจารณา edge case
- การประเมินอย่างเป็นระบบ

### Background Tasks

รันการดำเนินการที่ใช้เวลานานโดยไม่บล็อกการสนทนา

**การใช้งาน:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### Permission Modes

ควบคุมสิ่งที่ Claude สามารถทำได้

| โหมด | คำอธิบาย | กรณีการใช้งาน |
|------|-------------|----------|
| **default** | สิทธิ์มาตรฐานพร้อมถามเมื่อมีการกระทำที่ละเอียดอ่อน | การพัฒนาทั่วไป |
| **acceptEdits** | ยอมรับการแก้ไขไฟล์อัตโนมัติโดยไม่ต้องยืนยัน | workflow การแก้ไขที่ไว้ใจได้ |
| **plan** | วิเคราะห์และวางแผนเท่านั้น ไม่แก้ไขไฟล์ | รีวิวโค้ด, วางแผนสถาปัตยกรรม |
| **auto** | อนุมัติการกระทำที่ปลอดภัยอัตโนมัติ ถามเฉพาะที่เสี่ยง | ความอิสระที่สมดุลกับความปลอดภัย |
| **dontAsk** | ดำเนินการทั้งหมดโดยไม่ถามยืนยัน | ผู้ใช้ที่มีประสบการณ์, automation |
| **bypassPermissions** | เข้าถึงเต็มรูปแบบไม่จำกัด ไม่มีการตรวจสอบความปลอดภัย | CI/CD pipeline, script ที่ไว้ใจได้ |

**การใช้งาน:**
```bash
claude --permission-mode plan          # Read-only analysis
claude --permission-mode acceptEdits   # Auto-accept edits
claude --permission-mode auto          # Auto-approve safe actions
claude --permission-mode dontAsk       # No confirmation prompts
```

### Headless Mode (Print Mode)

รัน Claude Code โดยไม่มี input แบบโต้ตอบสำหรับ automation และ CI/CD โดยใช้ flag `-p` (print)

**การใช้งาน:**
```bash
# Run specific task
claude -p "Run all tests"

# Pipe input for analysis
cat error.log | claude -p "explain this error"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR changes and report issues"

# JSON output for scripting
claude -p --output-format json "list all functions in src/"
```

### Scheduled Tasks

รันงานตามตารางเวลาที่ทำซ้ำโดยใช้คำสั่ง `/loop`

**การใช้งาน:**
```bash
/loop every 30m "Run tests and report failures"
/loop every 2h "Check for dependency updates"
/loop every 1d "Generate daily summary of code changes"
```

Scheduled task ทำงานเบื้องหลังและรายงานผลลัพธ์เมื่อเสร็จสิ้น มีประโยชน์สำหรับการติดตามอย่างต่อเนื่อง การตรวจสอบเป็นระยะ และ workflow การบำรุงรักษาแบบอัตโนมัติ

### Chrome Integration

Claude Code สามารถผสานรวมกับเบราว์เซอร์ Chrome สำหรับงาน automation บนเว็บ ช่วยให้มีความสามารถเช่น การนำทางหน้าเว็บ การกรอกฟอร์ม การถ่าย screenshot และการดึงข้อมูลจากเว็บไซต์ได้โดยตรงภายใน workflow การพัฒนาของคุณ

### Session Management

จัดการ session การทำงานหลายรายการ

**คำสั่ง:**
```bash
/resume                # Resume a previous conversation
/rename "Feature"      # Name the current session
/fork                  # Fork into a new session
claude -c              # Continue most recent conversation
claude -r "Feature"    # Resume session by name/ID
```

### ฟีเจอร์แบบโต้ตอบ

**แป้นพิมพ์ลัด:**
- `Ctrl + R` - ค้นหาประวัติคำสั่ง
- `Tab` - เติมข้อความอัตโนมัติ
- `↑ / ↓` - ประวัติคำสั่ง
- `Ctrl + L` - ล้างหน้าจอ

**Input หลายบรรทัด:**
```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

### การกำหนดค่า

ตัวอย่างการกำหนดค่าแบบสมบูรณ์:

```json
{
  "planning": {
    "autoEnter": true,
    "requireApproval": true
  },
  "extendedThinking": {
    "enabled": true,
    "showThinkingProcess": true
  },
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5
  },
  "permissions": {
    "mode": "default"
  }
}
```

**ดู**: [09-advanced-features/](09-advanced-features/) สำหรับคู่มือฉบับสมบูรณ์

---

## Models and Reasoning Effort

Claude Code รองรับสามโมเดลพร้อม reasoning effort แบบปรับตัว:

| โมเดล | Context Window | ระดับ Effort | Effort เริ่มต้น (Claude Code) |
|-------|----------------|---------------|------------------------------|
| Claude Opus 4.7 | 1M tokens (native) | `low`, `medium`, `high`, `xhigh`, `max` | `xhigh` (ตั้งแต่เปิดตัว Opus 4.7, 2026-04-16) |
| Claude Sonnet 4.6 | 1M tokens | `low`, `medium`, `high`, `max` | `high` สำหรับสมาชิก Pro/Max (เพิ่มจาก `medium` ใน v2.1.117) |
| Claude Haiku 4.5 | 200K tokens | `low`, `medium`, `high` | `medium` |

> **หมายเหตุ**: v2.1.117 แก้บั๊กที่ session ของ Opus 4.7 คำนวณ `/context` กับ 200K แทนที่จะเป็น native 1M window — อัปเกรดเป็น v2.1.117 หรือใหม่กว่าเพื่อให้ได้ context 1M บน Opus 4.7 จริงๆ

> **หมายเหตุ**: `/cost` และ `/stats` ถูกรวมเป็น `/usage` ใน v2.1.118 ปัจจุบัน `/usage` เป็นคำสั่งหลักที่มีแท็บสำหรับ cost/stats/ฯลฯ; `/cost` และ `/stats` ยังคงอยู่ในฐานะ alias ทางลัดที่เปิดแท็บที่เกี่ยวข้อง

## Resources

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- [MCP GitHub Servers](https://github.com/modelcontextprotocol/servers)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

---

*อัปเดตล่าสุด: 24 เมษายน 2026*
*สำหรับ Claude Haiku 4.5, Sonnet 4.6 และ Opus 4.7*
*ปัจจุบันรวม: Hooks, Checkpoints, Planning Mode, Extended Thinking, Background Tasks, Permission Modes (6 โหมด), Headless Mode, Session Management, Auto Memory, Agent Teams, Scheduled Tasks, Chrome Integration, Channels, Voice Dictation และ Bundled Skills*

---
**อัปเดตล่าสุด**: 6 พฤษภาคม 2026
**เวอร์ชัน Claude Code**: 2.1.131
**แหล่งที่มา**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://www.anthropic.com/news/claude-opus-4-7
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
**โมเดลที่รองรับ**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
