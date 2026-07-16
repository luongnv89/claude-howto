<!-- i18n-source: 01-slash-commands/generate-api-docs.md -->
<!-- i18n-date: 2026-05-08 -->
---
description: สร้างเอกสาร API ครอบคลุมจาก source code
---

# ตัวสร้างเอกสาร API

สร้างเอกสาร API โดย:

1. สแกนไฟล์ทั้งหมดใน `/src/api/`
2. ดึง function signatures และ JSDoc comments
3. จัดระเบียบตาม endpoint/โมดูล
4. สร้าง markdown พร้อมตัวอย่าง
5. รวม request/response schemas
6. เพิ่มเอกสาร error

รูปแบบผลลัพธ์:
- ไฟล์ Markdown ใน `/docs/api.md`
- รวมตัวอย่าง curl สำหรับทุก endpoint
- เพิ่ม TypeScript types

---
**อัปเดตล่าสุด**: 9 เมษายน 2026
