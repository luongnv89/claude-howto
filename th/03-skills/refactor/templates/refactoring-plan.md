<!-- i18n-source: 03-skills/refactor/templates/refactoring-plan.md -->
<!-- i18n-date: 2026-05-09 -->
# Refactoring Plan Template

ใช้ template นี้เพื่อบันทึกและติดตามความคืบหน้าของการ refactoring

---

## ข้อมูลโครงการ

| ช่อง | ค่า |
|-------|-------|
| **Project/Module** | [ชื่อโครงการ] |
| **Target Files** | [รายการไฟล์ที่จะ refactor] |
| **Date Created** | [วันที่] |
| **Author** | [ชื่อ] |
| **Status** | Draft / In Review / Approved / In Progress / Completed |

---

## บทสรุปผู้บริหาร

### เป้าหมาย
- [ ] [เป้าหมายหลัก เช่น ปรับปรุงความอ่านง่ายของ payment processing]
- [ ] [เป้าหมายรอง เช่น ลด code duplication]
- [ ] [เป้าหมายเพิ่มเติม เช่น ปรับปรุง testability]

### ข้อจำกัด
- [ ] [ข้อจำกัดที่ 1 เช่น ห้ามเปลี่ยน public API]
- [ ] [ข้อจำกัดที่ 2 เช่น ต้องรักษา backward compatibility]
- [ ] [ข้อจำกัดที่ 3 เช่น ห้ามเปลี่ยน database schema]

### ระดับความเสี่ยง
- [ ] ต่ำ — การเปลี่ยนแปลงเล็กน้อย มีการทดสอบครอบคลุม
- [ ] ปานกลาง — การเปลี่ยนแปลงพอสมควร มีความเสี่ยงบ้าง
- [ ] สูง — การเปลี่ยนแปลงสำคัญ ต้องระมัดระวังเป็นพิเศษ

---

## Checklist ก่อนเริ่ม Refactoring

### การประเมิน Test Coverage

| Metric | ปัจจุบัน | เป้าหมาย | สถานะ |
|--------|---------|--------|--------|
| Unit Test Coverage | __%  | ≥80% | |
| Integration Tests | Yes/No | Yes | |
| All Tests Passing | Yes/No | Yes | |

### สิ่งที่ต้องดำเนินการก่อนเริ่ม
- [ ] test ทั้งหมดผ่าน
- [ ] ตรวจสอบและทำความเข้าใจโค้ด
- [ ] มี backup/version control พร้อมใช้งาน
- [ ] ได้รับการอนุมัติจากผู้ใช้แล้ว

---

## Code Smell ที่ระบุได้

### สรุป

| # | Smell | ตำแหน่ง | ความรุนแรง | ลำดับความสำคัญ |
|---|-------|----------|----------|----------|
| 1 | [เช่น Long Method] | [file:line] | High | P1 |
| 2 | [เช่น Duplicate Code] | [file:line] | Medium | P2 |
| 3 | [เช่น Feature Envy] | [file:line] | Low | P3 |

### การวิเคราะห์รายละเอียด

#### Smell #1: [ชื่อ]

**ตำแหน่ง**: `path/to/file.js:45-120`

**คำอธิบาย**: [คำอธิบายโดยละเอียดของปัญหา]

**ผลกระทบ**:
- [ผลกระทบที่ 1]
- [ผลกระทบที่ 2]

**แนวทางแก้ไขที่เสนอ**: [ภาพรวมสั้น ๆ ของวิธีแก้ไข]

---

## ระยะของ Refactoring

### ระยะ A: Quick Wins (ความเสี่ยงต่ำ)

**วัตถุประสงค์**: การปรับปรุงที่ง่ายและให้ประโยชน์ทันที

**การเปลี่ยนแปลงโดยประมาณ**: [X ไฟล์ Y method]

**ต้องได้รับการอนุมัติจากผู้ใช้**: Yes / No

| # | งาน | ไฟล์ | Refactoring | สถานะ |
|---|------|------|-------------|--------|
| A1 | เปลี่ยนชื่อตัวแปร `x` เป็น `userCount` | utils.js:15 | Rename Variable | [ ] |
| A2 | ลบ `oldHandler()` ที่ไม่ได้ใช้งาน | api.js:89 | Remove Dead Code | [ ] |
| A3 | แยก validation ที่ซ้ำกัน | form.js:23,67 | Extract Method | [ ] |

**แผนการ Rollback**: Revert commits A1-A3

---

### ระยะ B: การปรับปรุงโครงสร้าง (ความเสี่ยงปานกลาง)

**วัตถุประสงค์**: ปรับปรุงการจัดระเบียบและความชัดเจนของโค้ด

**การเปลี่ยนแปลงโดยประมาณ**: [X ไฟล์ Y method]

**ต้องได้รับการอนุมัติจากผู้ใช้**: Yes

**Dependencies**: ต้องเสร็จสิ้นระยะ A ก่อน

| # | งาน | ไฟล์ | Refactoring | สถานะ |
|---|------|------|-------------|--------|
| B1 | แยก `calculatePrice()` จาก method ยาว | order.js:45 | Extract Method | [ ] |
| B2 | สร้าง `OrderDetails` parameter object | order.js:12 | Introduce Parameter Object | [ ] |
| B3 | ย้าย `formatAddress()` ไปยัง Address class | customer.js:78 | Move Method | [ ] |

**แผนการ Rollback**: Revert ไปยัง commit หลังระยะ A

---

### ระยะ C: การเปลี่ยนแปลงสถาปัตยกรรม (ความเสี่ยงสูงกว่า)

**วัตถุประสงค์**: แก้ไขปัญหาเชิงโครงสร้างที่ลึกกว่า

**การเปลี่ยนแปลงโดยประมาณ**: [X ไฟล์ Y method]

**ต้องได้รับการอนุมัติจากผู้ใช้**: Yes

**Dependencies**: ต้องเสร็จสิ้นระยะ A และ B ก่อน

| # | งาน | ไฟล์ | Refactoring | สถานะ |
|---|------|------|-------------|--------|
| C1 | แทนที่ price switch ด้วย polymorphism | pricing.js:30 | Replace Conditional with Polymorphism | [ ] |
| C2 | แยก `NotificationService` class | user.js:100 | Extract Class | [ ] |

**แผนการ Rollback**: Revert ไปยัง commit หลังระยะ B

---

## ขั้นตอน Refactoring รายละเอียด

### งาน [ID]: [ชื่องาน]

**Smell ที่แก้ไข**: [ชื่อ smell]

**เทคนิค Refactoring**: [ชื่อเทคนิค]

**ระดับความเสี่ยง**: Low / Medium / High

#### บริบท

**ก่อน** (สถานะปัจจุบัน):
```javascript
// วางโค้ดปัจจุบันที่นี่
```

**หลัง** (สถานะที่คาดหวัง):
```javascript
// วางโค้ดที่คาดหวังที่นี่
```

#### กลไกทีละขั้นตอน

1. [ ] **ขั้นตอนที่ 1**: [คำอธิบาย]
   - ทดสอบ: รัน test หลังขั้นตอนนี้
   - ที่คาดหวัง: test ทั้งหมดผ่าน

2. [ ] **ขั้นตอนที่ 2**: [คำอธิบาย]
   - ทดสอบ: รัน test หลังขั้นตอนนี้
   - ที่คาดหวัง: test ทั้งหมดผ่าน

3. [ ] **ขั้นตอนที่ 3**: [คำอธิบาย]
   - ทดสอบ: รัน test หลังขั้นตอนนี้
   - ที่คาดหวัง: test ทั้งหมดผ่าน

#### การตรวจสอบ

- [ ] test ทั้งหมดผ่าน
- [ ] พฤติกรรมไม่เปลี่ยนแปลง
- [ ] โค้ด compile ได้
- [ ] ไม่มี warning ใหม่

#### Commit Message
```
refactor: [อธิบายการ refactoring]
```

---

## การติดตามความคืบหน้า

### สถานะของแต่ละระยะ

| ระยะ | สถานะ | เริ่มต้น | เสร็จสิ้น | Tests Passing |
|-------|--------|---------|-----------|---------------|
| A | Not Started / In Progress / Done | | | |
| B | Not Started / In Progress / Done | | | |
| C | Not Started / In Progress / Done | | | |

### ปัญหาที่พบ

| # | ปัญหา | การแก้ไข | สถานะ |
|---|-------|------------|--------|
| 1 | [คำอธิบาย] | [วิธีแก้ไข] | Open / Resolved |

---

## การเปรียบเทียบ Metrics

### ก่อน Refactoring

| Metric | ไฟล์ที่ 1 | ไฟล์ที่ 2 | รวม |
|--------|--------|--------|-------|
| Lines of Code | | | |
| Cyclomatic Complexity | | | |
| Maintainability Index | | | |
| Number of Methods | | | |
| Avg Method Length | | | |

### หลัง Refactoring

| Metric | ไฟล์ที่ 1 | ไฟล์ที่ 2 | รวม | การเปลี่ยนแปลง |
|--------|--------|--------|-------|--------|
| Lines of Code | | | | |
| Cyclomatic Complexity | | | | |
| Maintainability Index | | | | |
| Number of Methods | | | | |
| Avg Method Length | | | | |

---

## Checklist หลัง Refactoring

- [ ] test ทั้งหมดผ่าน
- [ ] ไม่มี warning หรือ error ใหม่
- [ ] โค้ด compile ได้สำเร็จ
- [ ] การตรวจสอบด้วยตนเองเสร็จสิ้น
- [ ] อัปเดตเอกสาร (หากจำเป็น)
- [ ] ตรวจสอบโค้ดแล้ว
- [ ] Metrics ดีขึ้น
- [ ] ได้รับการอนุมัติจากผู้ใช้แล้ว

---

## บทเรียนที่ได้รับ

### สิ่งที่ดำเนินการได้ดี
- [รายการที่ 1]
- [รายการที่ 2]

### สิ่งที่สามารถปรับปรุงได้
- [รายการที่ 1]
- [รายการที่ 2]

### คำแนะนำสำหรับอนาคต
- [รายการที่ 1]
- [รายการที่ 2]

---

## การอนุมัติ

| บทบาท | ชื่อ | วันที่ | ลายเซ็น |
|------|------|------|-----------|
| Plan Author | | | |
| Technical Lead | | | |
| Product Owner | | | |

---

## ภาคผนวก

### A. เอกสารที่เกี่ยวข้อง
- [ลิงก์ไปยังเอกสารที่เกี่ยวข้อง]

### B. เอกสารอ้างอิง
- [ลิงก์ไปยัง code smells catalog]
- [ลิงก์ไปยัง refactoring catalog]

### C. เครื่องมือที่ใช้
- [Testing framework]
- [Linting tools]
- [Complexity analysis tools]
