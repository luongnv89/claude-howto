<!-- i18n-source: 02-memory/personal-CLAUDE.md -->
<!-- i18n-date: 2026-05-09 -->
# ความต้องการด้านการพัฒนาส่วนบุคคล

## เกี่ยวกับฉัน
- **ระดับประสบการณ์**: 8 ปีในการพัฒนา full-stack
- **ภาษาที่ถนัด**: TypeScript, Python
- **รูปแบบการสื่อสาร**: ตรงไปตรงมา พร้อมตัวอย่าง
- **รูปแบบการเรียนรู้**: แผนภาพพร้อมโค้ด

## ความต้องการด้านโค้ด

### การจัดการข้อผิดพลาด (Error Handling)
ต้องการการจัดการข้อผิดพลาดอย่างชัดเจนด้วย try-catch block และข้อความผิดพลาดที่มีความหมาย
หลีกเลี่ยงข้อผิดพลาดทั่วไป บันทึก error ทุกครั้งเพื่อ debugging

### คอมเมนต์
ใช้คอมเมนต์อธิบาย "ทำไม" ไม่ใช่ "ทำอะไร" โค้ดควรอธิบายตัวเองได้
คอมเมนต์ควรอธิบาย business logic หรือการตัดสินใจที่ไม่ชัดเจน

### การทดสอบ (Testing)
ชอบ TDD (test-driven development)
เขียน test ก่อน แล้วค่อยเขียน implementation
มุ่งเน้นที่พฤติกรรม ไม่ใช่รายละเอียดการ implementation

### สถาปัตยกรรม (Architecture)
ชอบการออกแบบแบบ modular ที่มีการ coupling น้อย
ใช้ dependency injection เพื่อให้ทดสอบได้
แยก concerns (Controllers, Services, Repositories)

## ความต้องการด้าน Debugging
- ใช้ console.log พร้อม prefix: `[DEBUG]`
- รวม context: ชื่อ function, ตัวแปรที่เกี่ยวข้อง
- ใช้ stack trace เมื่อมีให้
- รวม timestamp ใน log ทุกครั้ง

## การสื่อสาร
- อธิบายแนวคิดซับซ้อนด้วยแผนภาพ
- แสดงตัวอย่างที่เป็นรูปธรรมก่อนอธิบายทฤษฎี
- รวม code snippet แบบ before/after
- สรุปประเด็นสำคัญท้ายสุด

## การจัดระเบียบโปรเจกต์
ฉันจัดระเบียบโปรเจกต์ดังนี้:
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

## เครื่องมือ (Tooling)
- **IDE**: VS Code with vim keybindings
- **Terminal**: Zsh with Oh-My-Zsh
- **Format**: Prettier (100 char line length)
- **Linter**: ESLint with airbnb config
- **Test Framework**: Jest with React Testing Library

---
**อัปเดตล่าสุด**: 9 เมษายน 2569
