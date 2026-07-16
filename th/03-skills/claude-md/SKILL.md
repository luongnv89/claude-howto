<!-- i18n-source: 03-skills/claude-md/SKILL.md -->
<!-- i18n-date: 2026-05-09 -->
---
name: claude-md
description: Create or update CLAUDE.md files following best practices for optimal AI agent onboarding
---

## ข้อมูลจากผู้ใช้

```text
$ARGUMENTS
```

คุณ **ต้อง** พิจารณาข้อมูลจากผู้ใช้ก่อนดำเนินการ (หากไม่ว่างเปล่า) ผู้ใช้อาจระบุ:
- `create` - สร้าง CLAUDE.md ใหม่ตั้งแต่ต้น
- `update` - ปรับปรุง CLAUDE.md ที่มีอยู่
- `audit` - วิเคราะห์และรายงานคุณภาพของ CLAUDE.md ปัจจุบัน
- path ที่ระบุสำหรับสร้าง/อัปเดต (เช่น `src/api/CLAUDE.md` สำหรับคำสั่งเฉพาะ directory)

## หลักการพื้นฐาน

**LLM เป็น stateless**: CLAUDE.md เป็นไฟล์เดียวที่รวมอยู่ใน conversation ทุกครั้งโดยอัตโนมัติ ทำหน้าที่เป็นเอกสาร onboarding หลักสำหรับ AI agent เข้าสู่ codebase ของคุณ

### กฎทอง

1. **น้อยกว่าดีกว่า**: Frontier LLM สามารถปฏิบัติตามคำสั่งประมาณ 150-200 ข้อ system prompt ของ Claude Code ใช้ไปแล้วประมาณ 50 ข้อ ให้ CLAUDE.md มุ่งเน้นและกระชับ

2. **ความสามารถใช้ได้ทั่วไป**: รวมเฉพาะข้อมูลที่เกี่ยวข้องกับทุก session คำสั่งเฉพาะงานควรอยู่ในไฟล์แยกต่างหาก

3. **ห้ามใช้ Claude เป็น linter**: แนวทาง style ทำให้ context บวมและลดประสิทธิภาพในการปฏิบัติตามคำสั่ง ใช้เครื่องมือที่กำหนดได้แน่นอน (prettier, eslint เป็นต้น) แทน

4. **ห้าม auto-generate**: CLAUDE.md เป็นจุดที่มีประสิทธิภาพสูงสุดของ AI harness สร้างด้วยมืออย่างรอบคอบ

## ขั้นตอนการทำงาน

### 1. การวิเคราะห์โปรเจกต์

ขั้นแรก วิเคราะห์สถานะโปรเจกต์ปัจจุบัน:

1. ตรวจสอบไฟล์ CLAUDE.md ที่มีอยู่:
   - ระดับราก: `./CLAUDE.md` หรือ `.claude/CLAUDE.md`
   - เฉพาะ directory: `**/CLAUDE.md`
   - global user config: `~/.claude/CLAUDE.md`

2. ระบุโครงสร้างโปรเจกต์:
   - Technology stack (ภาษา, framework)
   - ประเภทโปรเจกต์ (monorepo, single app, library)
   - เครื่องมือพัฒนา (package manager, build system, test runner)

3. ตรวจสอบเอกสารที่มีอยู่:
   - README.md
   - CONTRIBUTING.md
   - package.json, pyproject.toml, Cargo.toml และอื่นๆ

### 2. กลยุทธ์เนื้อหา (WHAT, WHY, HOW)

จัดโครงสร้าง CLAUDE.md ตาม 3 มิติ:

#### WHAT - เทคโนโลยีและโครงสร้าง
- ภาพรวม technology stack
- การจัดระเบียบโปรเจกต์ (สำคัญเป็นพิเศษสำหรับ monorepo)
- directory หลักและวัตถุประสงค์

#### WHY - วัตถุประสงค์และบริบท
- สิ่งที่โปรเจกต์ทำ
- เหตุผลที่ตัดสินใจด้านสถาปัตยกรรม
- ความรับผิดชอบของแต่ละส่วนประกอบหลัก

#### HOW - Workflow และข้อตกลง
- workflow การพัฒนา (bun vs node, pip vs uv เป็นต้น)
- ขั้นตอนและคำสั่งการทดสอบ
- วิธีการตรวจสอบและ build
- "gotcha" หรือข้อกำหนดที่ไม่ชัดเจน

### 3. กลยุทธ์ Progressive Disclosure

สำหรับโปรเจกต์ขนาดใหญ่ แนะนำให้สร้าง folder `agent_docs/`:

```
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- architecture_decisions.md
```

ใน CLAUDE.md อ้างอิงไฟล์เหล่านี้ด้วยคำสั่งเช่น:
```markdown
For detailed build instructions, refer to `agent_docs/building_the_project.md`
```

**สำคัญ**: ใช้การอ้างอิง `file:line` แทน code snippet เพื่อหลีกเลี่ยง context ที่ล้าสมัย

### 4. ข้อจำกัดด้านคุณภาพ

เมื่อสร้างหรืออัปเดต CLAUDE.md:

1. **เป้าหมายความยาว**: ไม่เกิน 300 บรรทัด (ควรไม่เกิน 100)
2. **ห้ามมีกฎ style**: ลบคำสั่ง linting/formatting ออก
3. **ห้ามมีคำสั่งเฉพาะงาน**: ย้ายไปยังไฟล์แยกต่างหาก
4. **ห้ามมี code snippet**: ใช้การอ้างอิงไฟล์แทน
5. **ห้ามมีข้อมูลซ้ำซ้อน**: ห้ามซ้ำสิ่งที่มีใน package.json หรือ README

### 5. ส่วนที่จำเป็น

CLAUDE.md ที่มีโครงสร้างดีควรมี:

```markdown
# ชื่อโปรเจกต์

คำอธิบายสั้นๆ หนึ่งบรรทัด

## Tech Stack
- ภาษาหลักและเวอร์ชัน
- framework/library หลัก
- ฐานข้อมูล/storage (ถ้ามี)

## Project Structure
[เฉพาะ monorepo หรือโครงสร้างที่ซับซ้อน]
- `apps/` - Application entry points
- `packages/` - Shared libraries

## Development Commands
- Install: `command`
- Test: `command`
- Build: `command`

## Critical Conventions
[เฉพาะข้อตกลงที่ไม่ชัดเจนและสำคัญสูง]
- ข้อตกลง 1 พร้อมคำอธิบายสั้นๆ
- ข้อตกลง 2 พร้อมคำอธิบายสั้นๆ

## Known Issues / Gotchas
[สิ่งที่ทำให้นักพัฒนาติดขัดเป็นประจำ]
- ปัญหา 1
- ปัญหา 2
```

### 6. anti-pattern ที่ควรหลีกเลี่ยง

**ห้ามรวม:**
- แนวทาง code style (ใช้ linter แทน)
- เอกสารเกี่ยวกับวิธีใช้ Claude
- คำอธิบายยาวๆ เกี่ยวกับ pattern ที่ชัดเจนอยู่แล้ว
- ตัวอย่างโค้ดที่ copy-paste มา
- แนวปฏิบัติที่ดีทั่วไป ("write clean code")
- คำสั่งสำหรับงานเฉพาะ
- เนื้อหาที่ auto-generate
- รายการ TODO ยาวๆ

### 7. checklist การตรวจสอบ

ก่อนสรุป ตรวจสอบ:

- [ ] ไม่เกิน 300 บรรทัด (ควรไม่เกิน 100)
- [ ] ทุกบรรทัดใช้ได้กับทุก session
- [ ] ไม่มีกฎ style/formatting
- [ ] ไม่มี code snippet (ใช้การอ้างอิงไฟล์)
- [ ] คำสั่งได้รับการตรวจสอบว่าใช้งานได้จริง
- [ ] ใช้ progressive disclosure สำหรับโปรเจกต์ซับซ้อน
- [ ] บันทึก gotcha ที่สำคัญ
- [ ] ไม่มีความซ้ำซ้อนกับ README.md

## รูปแบบผลลัพธ์

### สำหรับ `create` หรือค่าเริ่มต้น:

1. วิเคราะห์โปรเจกต์
2. ร่าง CLAUDE.md ตามโครงสร้างข้างต้น
3. นำเสนอร่างเพื่อตรวจสอบ
4. เขียนไปยังตำแหน่งที่เหมาะสมหลังได้รับการอนุมัติ

### สำหรับ `update`:

1. อ่าน CLAUDE.md ที่มีอยู่
2. ตรวจสอบกับแนวปฏิบัติที่ดี
3. ระบุ:
   - เนื้อหาที่ต้องลบ (กฎ style, code snippet, เฉพาะงาน)
   - เนื้อหาที่ต้องย่อ
   - ข้อมูลสำคัญที่หายไป
4. นำเสนอการเปลี่ยนแปลงเพื่อตรวจสอบ
5. นำไปใช้หลังได้รับการอนุมัติ

### สำหรับ `audit`:

1. อ่าน CLAUDE.md ที่มีอยู่
2. สร้างรายงานพร้อม:
   - จำนวนบรรทัดปัจจุบันเทียบกับเป้าหมาย
   - เปอร์เซ็นต์เนื้อหาที่ใช้ได้กับทุก session
   - รายการ anti-pattern ที่พบ
   - คำแนะนำสำหรับการปรับปรุง
3. ห้ามแก้ไขไฟล์ รายงานเท่านั้น

## การจัดการ AGENTS.md

หากผู้ใช้ขอสร้าง/อัปเดต AGENTS.md:

AGENTS.md ใช้สำหรับกำหนดพฤติกรรมของ agent เฉพาะทาง ไม่เหมือน CLAUDE.md (ที่ใช้สำหรับ context ของโปรเจกต์), AGENTS.md กำหนด:
- บทบาทและความสามารถของ agent เฉพาะ
- คำสั่งและข้อจำกัดเฉพาะ agent
- นิยาม workflow สำหรับ multi-agent scenario

ใช้หลักการเดียวกัน:
- มุ่งเน้นและกระชับ
- ใช้ progressive disclosure
- อ้างอิงเอกสารภายนอกแทนการฝังเนื้อหา

## หมายเหตุ

- ตรวจสอบว่าคำสั่งใช้งานได้จริงก่อนรวมไว้
- เมื่อสงสัย ไม่รวมดีกว่า - น้อยกว่าดีกว่า
- system reminder บอก Claude ว่า CLAUDE.md "อาจหรือไม่อาจเกี่ยวข้อง" - ยิ่งมี noise มาก ยิ่งถูกมองข้าม
- Monorepo ได้ประโยชน์สูงสุดจากโครงสร้าง WHAT/WHY/HOW ที่ชัดเจน
- ไฟล์ CLAUDE.md เฉพาะ directory ควรมุ่งเน้นมากยิ่งขึ้น
