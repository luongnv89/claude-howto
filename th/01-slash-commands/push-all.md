<!-- i18n-source: 01-slash-commands/push-all.md -->
<!-- i18n-date: 2026-05-08 -->
---
description: จัดระเบียบการเปลี่ยนแปลงทั้งหมด สร้าง commit และ push ไปยัง remote (ใช้ด้วยความระมัดระวัง)
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# Commit และ Push ทั้งหมด

⚠️ **ข้อควรระวัง**: จัดระเบียบการเปลี่ยนแปลงทั้งหมด commit และ push ไปยัง remote ใช้เฉพาะเมื่อมั่นใจว่าการเปลี่ยนแปลงทั้งหมดเป็นชุดเดียวกัน

## Workflow

### 1. วิเคราะห์การเปลี่ยนแปลง
รันพร้อมกัน:
- `git status` - แสดงไฟล์ที่แก้ไข/เพิ่ม/ลบ/ยังไม่ได้ติดตาม
- `git diff --stat` - แสดงสถิติการเปลี่ยนแปลง
- `git log -1 --oneline` - แสดง commit ล่าสุดสำหรับรูปแบบข้อความ

### 2. การตรวจสอบความปลอดภัย

**❌ หยุดและแจ้งเตือนหากตรวจพบ:**
- ความลับ: `.env*`, `*.key`, `*.pem`, `credentials.json`, `secrets.yaml`, `id_rsa`, `*.p12`, `*.pfx`, `*.cer`
- API Keys: ตัวแปร `*_API_KEY`, `*_SECRET`, `*_TOKEN` ที่มีค่าจริง (ไม่ใช่ placeholders เช่น `your-api-key`, `xxx`, `placeholder`)
- ไฟล์ขนาดใหญ่: `>10MB` โดยไม่มี Git LFS
- Build artifacts: `node_modules/`, `dist/`, `build/`, `__pycache__/`, `*.pyc`, `.venv/`
- ไฟล์ชั่วคราว: `.DS_Store`, `thumbs.db`, `*.swp`, `*.tmp`

**การตรวจสอบ API Key:**
ตรวจสอบไฟล์ที่แก้ไขสำหรับรูปแบบเช่น:
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ ตรวจพบ key จริง!
AWS_SECRET_KEY=AKIA...         # ❌ ตรวจพบ key จริง!
STRIPE_API_KEY=sk_live_...    # ❌ ตรวจพบ key จริง!

# ✅ Placeholders ที่ยอมรับได้:
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ ตรวจสอบ:**
- `.gitignore` กำหนดค่าถูกต้อง
- ไม่มี merge conflicts
- branch ถูกต้อง (แจ้งเตือนหาก main/master)
- API keys เป็น placeholders เท่านั้น

### 3. ขอการยืนยัน

แสดงสรุป:
```
📊 สรุปการเปลี่ยนแปลง:
- X ไฟล์ที่แก้ไข, Y เพิ่ม, Z ลบ
- รวม: +AAA insertions, -BBB deletions

🔒 ความปลอดภัย: ✅ ไม่มีความลับ | ✅ ไม่มีไฟล์ขนาดใหญ่ | ⚠️ [คำเตือน]
🌿 Branch: [ชื่อ] → origin/[ชื่อ]

จะดำเนินการ: git add . → commit → push

พิมพ์ 'yes' เพื่อดำเนินการต่อหรือ 'no' เพื่อยกเลิก
```

**รอการยืนยัน "yes" อย่างชัดเจนก่อนดำเนินการ**

### 4. ดำเนินการ (หลังการยืนยัน)

รันตามลำดับ:
```bash
git add .
git status  # ตรวจสอบการจัดระเบียบ
```

### 5. สร้าง Commit Message

วิเคราะห์การเปลี่ยนแปลงและสร้าง conventional commit:

**รูปแบบ:**
```
[type]: สรุปสั้น ๆ (ไม่เกิน 72 ตัวอักษร)

- การเปลี่ยนแปลงหลัก 1
- การเปลี่ยนแปลงหลัก 2
- การเปลี่ยนแปลงหลัก 3
```

**ประเภท:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `build`, `ci`

**ตัวอย่าง:**
```
docs: Update concept README files with comprehensive documentation

- Add architecture diagrams and tables
- Include practical examples
- Expand best practices sections
```

### 6. Commit และ Push

```bash
git commit -m "$(cat <<'EOF'
[Generated commit message]
EOF
)"
git push  # หากล้มเหลว: git pull --rebase && git push
git log -1 --oneline --decorate  # ตรวจสอบ
```

### 7. ยืนยันความสำเร็จ

```
✅ Push ไปยัง remote สำเร็จ!

Commit: [hash] [message]
Branch: [branch] → origin/[branch]
ไฟล์ที่เปลี่ยนแปลง: X (+insertions, -deletions)
```

## การจัดการข้อผิดพลาด

- **git add ล้มเหลว**: ตรวจสอบสิทธิ์ ไฟล์ที่ถูกล็อก ตรวจสอบว่า repository ถูกเริ่มต้นแล้ว
- **git commit ล้มเหลว**: แก้ไข pre-commit hooks ตรวจสอบ git config (user.name/email)
- **git push ล้มเหลว**:
  - Non-fast-forward: `git pull --rebase && git push`
  - ไม่มี remote branch: `git push -u origin [branch]`
  - Protected branch: ใช้ PR workflow แทน

## เมื่อใดควรใช้

✅ **เหมาะสม:**
- การอัปเดตเอกสารหลายไฟล์
- ฟีเจอร์พร้อม tests และ docs
- การแก้ไขข้อผิดพลาดข้ามไฟล์
- การจัดรูปแบบ/refactoring ทั้งโครงการ
- การเปลี่ยนแปลงการกำหนดค่า

❌ **ควรหลีกเลี่ยง:**
- ไม่แน่ใจว่ากำลัง commit อะไร
- มีข้อมูลลับ/ข้อมูลสำคัญ
- Protected branches โดยไม่มีการ review
- มี merge conflicts
- ต้องการประวัติ commit ที่ละเอียด
- pre-commit hooks ล้มเหลว

## ทางเลือกอื่น

หากผู้ใช้ต้องการการควบคุม แนะนำ:
1. **การจัดระเบียบแบบเลือกสรร**: ตรวจสอบ/จัดระเบียบไฟล์เฉพาะ
2. **การจัดระเบียบแบบ interactive**: `git add -p` สำหรับการเลือก patch
3. **PR workflow**: สร้าง branch → push → PR (ใช้คำสั่ง `/pr`)

**⚠️ จำไว้**: ตรวจสอบการเปลี่ยนแปลงเสมอก่อน push เมื่อไม่แน่ใจ ให้ใช้คำสั่ง git แต่ละคำสั่งเพื่อการควบคุมที่มากขึ้น

---
**อัปเดตล่าสุด**: 9 เมษายน 2026
