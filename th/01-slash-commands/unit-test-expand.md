<!-- i18n-source: 01-slash-commands/unit-test-expand.md -->
<!-- i18n-date: 2026-05-08 -->
---
name: Expand Unit Tests
description: เพิ่มความครอบคลุมของ test โดยมุ่งเป้าที่ branch และ edge cases ที่ยังไม่ได้ทดสอบ
tags: testing, coverage, unit-tests
---

# การขยาย Unit Tests

ขยาย unit tests ที่มีอยู่ให้เหมาะสมกับ testing framework ของโครงการ:

1. **วิเคราะห์ความครอบคลุม**: รัน coverage report เพื่อระบุ branch edge cases และพื้นที่ที่มีความครอบคลุมต่ำที่ยังไม่ได้ทดสอบ
2. **ระบุช่องว่าง**: ตรวจสอบโค้ดสำหรับ logical branches, error paths, boundary conditions, null/empty inputs
3. **เขียน tests** โดยใช้ framework ของโครงการ:
   - Jest/Vitest/Mocha (JavaScript/TypeScript)
   - pytest/unittest (Python)
   - Go testing/testify (Go)
   - Rust test framework (Rust)
4. **มุ่งเป้าสถานการณ์เฉพาะ**:
   - การจัดการ error และ exceptions
   - ค่าขอบเขต (min/max, empty, null)
   - Edge cases และ corner cases
   - การเปลี่ยน state และ side effects
5. **ตรวจสอบการปรับปรุง**: รัน coverage อีกครั้ง ยืนยันว่ามีการเพิ่มขึ้นอย่างวัดได้

แสดงเฉพาะบล็อกโค้ด test ใหม่ ปฏิบัติตามรูปแบบ test และ naming conventions ที่มีอยู่

---
**อัปเดตล่าสุด**: 9 เมษายน 2026
