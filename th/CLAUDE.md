<!-- i18n-source: CLAUDE.md -->
<!-- i18n-date: 2026-05-08 -->

# CLAUDE.md

Repository สำหรับบทเรียน ผลลัพธ์เป็น markdown ในโมดูลที่มีหมายเลข `01-` ถึง `10-` ไม่ใช่แอปพลิเคชัน Script ใน `scripts/` มีไว้สำหรับตรวจสอบเอกสารและสร้าง EPUB เท่านั้น

ดูเพิ่มเติมที่ `.claude/CLAUDE.md` สำหรับ stack/คำสั่ง และ `STYLE_GUIDE.md` สำหรับโครงสร้างบทเรียน

## คำสั่งสำคัญ

```bash
# Quality gate (รันอัตโนมัติเมื่อ commit ผ่าน pre-commit hook)
pre-commit run --all-files

# Tests
pytest scripts/tests/ -v

# EPUB build (เรียก Kroki.io API เพื่อ render Mermaid — ต้องใช้เครือข่าย)
uv run scripts/build_epub.py

# Python tooling
ruff check scripts/ && ruff format scripts/
mypy scripts/ --ignore-missing-imports
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/
```

Pre-commit รัน 5 การตรวจสอบ: markdown-lint, cross-references, mermaid-syntax, link-check, build-epub (เมื่อไฟล์ `.md` มีการเปลี่ยนแปลง) ทุกอย่างต้องผ่าน

## แผนที่สถาปัตยกรรม

- `01-` … `10-` — โมดูลบทเรียน **คำนำหน้าหมายเลข = ลำดับการเรียน** ไม่ใช่ตามตัวอักษร ห้ามจัดเรียงใหม่
- แต่ละโมดูล: `README.md` + template แบบคัดลอกได้ (`.md`, `.json`, `.sh`)
- `scripts/` — ยูทิลิตี้ (EPUB builder, link/mermaid/cross-ref validator) ไม่ใช่ผลิตภัณฑ์
- `02-memory/*.md` — CLAUDE.md template สำหรับให้ผู้ใช้คัดลอกไปใช้ในโปรเจกต์ของตัวเอง อย่าสับสนกับไฟล์นี้
- `openspec/` — ข้อเสนอการเปลี่ยนแปลงแบบ spec-driven

## กฎเด็ดขาด

- **ห้าม commit หรือ push โดยไม่ได้รับคำขอจากผู้ใช้อย่างชัดเจน**
- **ห้ามเพิ่ม `Co-Authored-By: Claude`** ใน commit message ใดๆ
- เปิดใช้ `.venv` ก่อนรัน Python script เสมอ (ตรวจสอบ `venv/`, `.venv/`, `env/`)
- Internal link ใช้ **relative path** (เช่น `01-slash-commands/README.md`); anchor ใช้ `#heading-name`
- Code fence **ต้องระบุภาษา** (`bash`, `python`, `json`, …) — การตรวจสอบ cross-reference จะล้มเหลวหากไม่ระบุ
- URL ภายนอกต้องเข้าถึงได้และเสถียร ห้ามใช้ link ที่ไม่ถาวร
- Mermaid diagram ต้อง parse ได้ (ตรวจสอบก่อน commit) การ build EPUB ล้มเหลวส่วนใหญ่เกิดจาก Mermaid ไม่ถูกต้องหรือไม่มีเครือข่ายไปยัง Kroki
- รูปแบบ commit: `type(scope): subject` โดย `scope` ตรงกับโฟลเดอร์โมดูล (เช่น `feat(slash-commands):`, `docs(memory):`, `fix(README):`)
- ห้ามจัดเรียงหมายเลข `01-`–`10-` ใหม่ ลำดับคือ curriculum

## ความต้องการของ workflow

- สำหรับการแก้ไขบทเรียน ทำตาม `STYLE_GUIDE.md` สำหรับโครงสร้าง/การตั้งชื่อ/diagram
- การแก้ไขเล็กน้อย → diff ขั้นต่ำ อย่าเขียนส่วนใหม่ทั้งหมดเพื่อแก้ typo
- เมื่อเพิ่มหน้าโมดูล: README + template ก่อน จากนั้นอัปเดต root `README.md` index และ `LEARNING-ROADMAP.md` หากลำดับ/เวลาเปลี่ยนแปลง
- Tutorial > library: ให้ความสำคัญกับคำอธิบายที่ชัดเจนและตัวอย่างแบบคัดลอกได้มากกว่า abstraction ที่นำกลับมาใช้ใหม่
- หากการตรวจสอบคุณภาพล้มเหลว แก้ไขปัญหาต้นเหตุ อย่าใช้ `--no-verify` เพื่อข้าม

## ประสิทธิภาพด้าน Token
- ไม่อ่านไฟล์ที่เพิ่งเขียนหรือแก้ไขซ้ำ คุณทราบเนื้อหาอยู่แล้ว
- ไม่รันคำสั่งซ้ำเพื่อ "ตรวจสอบ" เว้นแต่ผลลัพธ์ไม่แน่นอน
- ไม่แสดงโค้ดหรือเนื้อหาไฟล์ขนาดใหญ่ซ้ำ เว้นแต่ได้รับการร้องขอ
- รวมการแก้ไขที่เกี่ยวข้องเข้าด้วยกันในการดำเนินการเดียว ไม่แก้ไข 5 ครั้งเมื่อ 1 ครั้งเพียงพอ
- ข้ามการยืนยันเช่น "ฉันจะดำเนินการต่อ..." แค่ทำเลย
- หากงานต้องการ tool call 1 ครั้ง อย่าใช้ 3 ครั้ง วางแผนก่อนลงมือ
- ไม่สรุปสิ่งที่เพิ่งทำ เว้นแต่ผลลัพธ์ไม่ชัดเจนหรือต้องการข้อมูลเพิ่มเติม
