<!-- i18n-source: 01-slash-commands/pr.md -->
<!-- i18n-date: 2026-05-08 -->
---
description: ทำความสะอาดโค้ด จัดระเบียบการเปลี่ยนแปลง และเตรียม pull request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# รายการตรวจสอบการเตรียม Pull Request

ก่อนสร้าง PR ให้ดำเนินการตามขั้นตอนเหล่านี้:

1. รัน linting: `prettier --write .`
2. รัน tests: `npm test`
3. ตรวจสอบ git diff: `git diff HEAD`
4. จัดระเบียบการเปลี่ยนแปลง: `git add .`
5. สร้าง commit message ตามรูปแบบ conventional commits:
   - `fix:` สำหรับการแก้ไขข้อผิดพลาด
   - `feat:` สำหรับฟีเจอร์ใหม่
   - `docs:` สำหรับเอกสาร
   - `refactor:` สำหรับการปรับโครงสร้างโค้ด
   - `test:` สำหรับการเพิ่ม test
   - `chore:` สำหรับงานบำรุงรักษา

6. สร้างสรุป PR ที่ประกอบด้วย:
   - สิ่งที่เปลี่ยนแปลง
   - เหตุผลที่เปลี่ยนแปลง
   - การทดสอบที่ดำเนินการ
   - ผลกระทบที่อาจเกิดขึ้น

---
**อัปเดตล่าสุด**: 9 เมษายน 2026
