<!-- i18n-source: 01-slash-commands/commit.md -->
<!-- i18n-date: 2026-05-08 -->
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: สร้าง git commit พร้อม context จาก repository
---

## Context

- สถานะ git ปัจจุบัน: !`git status`
- git diff ปัจจุบัน: !`git diff HEAD`
- branch ปัจจุบัน: !`git branch --show-current`
- commits ล่าสุด: !`git log --oneline -10`

## งานของคุณ

จากการเปลี่ยนแปลงข้างต้น ให้สร้าง git commit เดียว

หากมีข้อความผ่าน arguments ให้ใช้ข้อความนั้น: $ARGUMENTS

มิฉะนั้น ให้วิเคราะห์การเปลี่ยนแปลงและสร้าง commit message ที่เหมาะสม โดยปฏิบัติตามรูปแบบ conventional commits:
- `feat:` สำหรับฟีเจอร์ใหม่
- `fix:` สำหรับการแก้ไขข้อผิดพลาด
- `docs:` สำหรับการเปลี่ยนแปลงเอกสาร
- `refactor:` สำหรับการปรับโครงสร้างโค้ด
- `test:` สำหรับการเพิ่ม test
- `chore:` สำหรับงานบำรุงรักษา

---
**อัปเดตล่าสุด**: 9 เมษายน 2026
