<!-- i18n-source: 03-skills/refactor/SKILL.md -->
<!-- i18n-date: 2026-05-09 -->
---
name: code-refactor
description: Systematic code refactoring based on Martin Fowler's methodology. Use when users ask to refactor code, improve code structure, reduce technical debt, clean up legacy code, eliminate code smells, or improve code maintainability. This skill guides through a phased approach with research, planning, and safe incremental implementation.
---

# Code Refactoring Skill

แนวทางที่เป็นระบบสำหรับการ refactoring โค้ดตามวิธีการของ Martin Fowler ใน *Refactoring: Improving the Design of Existing Code* (2nd Edition) skill นี้เน้นการเปลี่ยนแปลงที่ปลอดภัยและเพิ่มทีละน้อยโดยมี test เป็นตัวรองรับ

> "Refactoring คือกระบวนการเปลี่ยนแปลงระบบซอฟต์แวร์ในลักษณะที่ไม่เปลี่ยนพฤติกรรมภายนอกของโค้ด แต่ปรับปรุงโครงสร้างภายใน" — Martin Fowler

## หลักการพื้นฐาน

1. **การรักษาพฤติกรรม**: พฤติกรรมภายนอกต้องไม่เปลี่ยนแปลง
2. **ขั้นตอนเล็ก**: เปลี่ยนแปลงทีละน้อยและทดสอบได้
3. **Test-Driven**: test คือตาข่ายความปลอดภัย
4. **ต่อเนื่อง**: refactoring เป็นกระบวนการต่อเนื่อง ไม่ใช่ครั้งเดียว
5. **ร่วมมือกัน**: ต้องได้รับการอนุมัติจากผู้ใช้ในแต่ละขั้นตอน

## ภาพรวม Workflow

```
Phase 1: การวิจัยและวิเคราะห์
    ↓
Phase 2: การประเมินความครอบคลุมของ Test
    ↓
Phase 3: การระบุ Code Smell
    ↓
Phase 4: การสร้างแผน Refactoring
    ↓
Phase 5: การ Implementation ทีละน้อย
    ↓
Phase 6: การตรวจสอบและการทำซ้ำ
```

---

## Phase 1: การวิจัยและวิเคราะห์

### วัตถุประสงค์
- เข้าใจโครงสร้างและวัตถุประสงค์ของ codebase
- ระบุขอบเขตของการ refactoring
- รวบรวม context เกี่ยวกับข้อกำหนดทางธุรกิจ

### คำถามที่ต้องถามผู้ใช้
ก่อนเริ่ม ให้ชัดเจนเกี่ยวกับ:

1. **ขอบเขต**: ไฟล์/โมดูล/function ใดที่ต้องการ refactoring?
2. **เป้าหมาย**: คุณพยายามแก้ปัญหาอะไร? (ความสามารถอ่านได้, ประสิทธิภาพ, ความสามารถในการบำรุงรักษา)
3. **ข้อจำกัด**: มีส่วนใดที่ **ไม่ควร** เปลี่ยนแปลง?
4. **แรงกดดันด้านเวลา**: สิ่งนี้บล็อกงานอื่นอยู่หรือไม่?
5. **สถานะ test**: มี test อยู่หรือไม่? ผ่านอยู่หรือเปล่า?

### การดำเนินการ
- [ ] อ่านและเข้าใจโค้ดเป้าหมาย
- [ ] ระบุ dependency และ integration
- [ ] จัดทำเอกสาร architecture ปัจจุบัน
- [ ] บันทึก technical debt ที่มีอยู่ (TODO, FIXME)

### ผลลัพธ์
นำเสนอการค้นพบต่อผู้ใช้:
- สรุปโครงสร้างโค้ด
- พื้นที่ที่มีปัญหาที่ระบุได้
- คำแนะนำเบื้องต้น
- **ขอการอนุมัติเพื่อดำเนินการต่อ**

---

## Phase 2: การประเมินความครอบคลุมของ Test

### ทำไม Test ถึงสำคัญ
> "Refactoring โดยไม่มี test เหมือนขับรถโดยไม่คาดเข็มขัด" — Martin Fowler

Test เป็น **ตัวเปิดใช้งานหลัก** ของการ refactoring ที่ปลอดภัย หากไม่มี test มีความเสี่ยงในการนำ bug เข้ามา

### ขั้นตอนการประเมิน

1. **ตรวจสอบ test ที่มีอยู่**
   ```bash
   # ค้นหาไฟล์ test
   find . -name "*test*" -o -name "*spec*" | head -20
   ```

2. **รัน test ที่มีอยู่**
   ```bash
   # JavaScript/TypeScript
   npm test

   # Python
   pytest -v

   # Java
   mvn test
   ```

3. **ตรวจสอบความครอบคลุม (ถ้ามี)**
   ```bash
   # JavaScript
   npm run test:coverage

   # Python
   pytest --cov=.
   ```

### จุดตัดสินใจ: ถามผู้ใช้

**ถ้า test มีอยู่และผ่าน:**
- ดำเนินการต่อไปยัง Phase 3

**ถ้า test ขาดหายหรือไม่ครบถ้วน:**
นำเสนอตัวเลือก:
1. เขียน test ก่อน (แนะนำ)
2. เพิ่ม test ทีละน้อยระหว่าง refactoring
3. ดำเนินการโดยไม่มี test (มีความเสี่ยง - ต้องได้รับการยอมรับจากผู้ใช้)

**ถ้า test ล้มเหลว:**
- หยุด ต้องแก้ไข test ที่ล้มเหลวก่อน refactoring
- ถามผู้ใช้: ควรแก้ไข test ก่อนหรือไม่?

### แนวทางการเขียน Test (ถ้าจำเป็น)

สำหรับแต่ละ function ที่ต้อง refactoring ตรวจสอบให้ test ครอบคลุม:
- Happy path (การทำงานปกติ)
- Edge case (input ว่าง, null, ขอบเขต)
- Error scenario (input ไม่ถูกต้อง, exception)

ใช้วงจร "red-green-refactor":
1. เขียน test ที่ล้มเหลว (red)
2. ทำให้ผ่าน (green)
3. Refactor

---

## Phase 3: การระบุ Code Smell

### Code Smell คืออะไร?
อาการของปัญหาที่ลึกกว่าในโค้ด ไม่ใช่ bug แต่เป็นสัญญาณบ่งบอกว่าโค้ดสามารถปรับปรุงได้

### Code Smell ทั่วไปที่ต้องตรวจสอบ

ดู [references/code-smells.md](references/code-smells.md) สำหรับ catalog ที่ครบถ้วน

#### อ้างอิงด่วน

| Smell | สัญญาณ | ผลกระทบ |
|-------|-------|--------|
| **Long Method** | method มากกว่า 30-50 บรรทัด | เข้าใจยาก, ทดสอบ, บำรุงรักษายาก |
| **Duplicated Code** | logic เดียวกันในหลายที่ | ต้องแก้ bug หลายที่ |
| **Large Class** | class มีความรับผิดชอบมากเกินไป | ละเมิด Single Responsibility |
| **Feature Envy** | method ใช้ข้อมูลของ class อื่นมากกว่า | การห่อข้อมูล (encapsulation) ไม่ดี |
| **Primitive Obsession** | ใช้ primitive มากเกินไปแทน object | ขาด domain concept |
| **Long Parameter List** | method มีมากกว่า 4 parameter | เรียกใช้ยาก |
| **Data Clumps** | ข้อมูลชุดเดียวกันปรากฏซ้ำๆ | ขาด abstraction |
| **Switch Statements** | switch/if-else chain ซับซ้อน | ขยายยาก |
| **Speculative Generality** | โค้ด "เผื่อไว้" | ความซับซ้อนที่ไม่จำเป็น |
| **Dead Code** | โค้ดที่ไม่ได้ใช้งาน | ความสับสน, ภาระการบำรุงรักษา |

### ขั้นตอนการวิเคราะห์

1. **การวิเคราะห์อัตโนมัติ** (ถ้ามี script)
   ```bash
   python scripts/detect-smells.py <file>
   ```

2. **การตรวจสอบด้วยตนเอง**
   - ตรวจสอบโค้ดอย่างเป็นระบบ
   - บันทึก smell แต่ละรายการพร้อมตำแหน่งและความรุนแรง
   - จัดหมวดหมู่ตามผลกระทบ (Critical/High/Medium/Low)

3. **การจัดลำดับความสำคัญ**
   มุ่งเน้น smell ที่:
   - บล็อกการพัฒนาปัจจุบัน
   - ทำให้เกิด bug หรือความสับสน
   - ส่งผลต่อเส้นทางโค้ดที่เปลี่ยนแปลงบ่อยที่สุด

### ผลลัพธ์: รายงาน Smell

นำเสนอต่อผู้ใช้:
- รายการ smell ที่ระบุได้พร้อมตำแหน่ง
- การประเมินความรุนแรงแต่ละรายการ
- ลำดับความสำคัญที่แนะนำ
- **ขอการอนุมัติเกี่ยวกับลำดับความสำคัญ**

---

## Phase 4: การสร้างแผน Refactoring

### การเลือก Refactoring

สำหรับแต่ละ smell ให้เลือก refactoring ที่เหมาะสมจาก catalog

ดู [references/refactoring-catalog.md](references/refactoring-catalog.md) สำหรับรายการที่ครบถ้วน

#### การ Mapping จาก Smell ไปยัง Refactoring

| Code Smell | Refactoring ที่แนะนำ |
|------------|---------------------------|
| Long Method | Extract Method, Replace Temp with Query |
| Duplicated Code | Extract Method, Pull Up Method, Form Template Method |
| Large Class | Extract Class, Extract Subclass |
| Feature Envy | Move Method, Move Field |
| Primitive Obsession | Replace Primitive with Object, Replace Type Code with Class |
| Long Parameter List | Introduce Parameter Object, Preserve Whole Object |
| Data Clumps | Extract Class, Introduce Parameter Object |
| Switch Statements | Replace Conditional with Polymorphism |
| Speculative Generality | Collapse Hierarchy, Inline Class, Remove Dead Code |
| Dead Code | Remove Dead Code |

### โครงสร้างแผน

ใช้ template ที่ [templates/refactoring-plan.md](templates/refactoring-plan.md)

สำหรับแต่ละ refactoring:
1. **เป้าหมาย**: โค้ดใดที่จะเปลี่ยนแปลง
2. **Smell**: ปัญหาใดที่แก้ไข
3. **Refactoring**: เทคนิคใดที่จะใช้
4. **ขั้นตอน**: micro-step อย่างละเอียด
5. **ความเสี่ยง**: อะไรที่อาจผิดพลาด
6. **Rollback**: วิธียกเลิกถ้าจำเป็น

### แนวทาง Phased

**สำคัญ**: แนะนำ refactoring ทีละน้อยแบบ phase

**Phase A: Quick Wins** (ความเสี่ยงต่ำ, มูลค่าสูง)
- เปลี่ยนชื่อตัวแปรเพื่อความชัดเจน
- Extract โค้ดซ้ำที่ชัดเจน
- ลบ dead code

**Phase B: การปรับปรุงโครงสร้าง** (ความเสี่ยงปานกลาง)
- Extract method จาก function ยาว
- แนะนำ parameter object
- ย้าย method ไปยัง class ที่เหมาะสม

**Phase C: การเปลี่ยนแปลงสถาปัตยกรรม** (ความเสี่ยงสูงกว่า)
- แทนที่ conditional ด้วย polymorphism
- Extract class
- แนะนำ design pattern

### จุดตัดสินใจ: นำเสนอแผนต่อผู้ใช้

ก่อน implementation:
- แสดงแผน refactoring ที่ครบถ้วน
- อธิบายแต่ละ phase และความเสี่ยง
- ได้รับการอนุมัติอย่างชัดเจนสำหรับแต่ละ phase
- **ถาม**: "ควรดำเนินการกับ Phase A ไหม?"

---

## Phase 5: การ Implementation ทีละน้อย

### กฎทอง
> "เปลี่ยนแปลง → ทดสอบ → ผ่าน? → Commit → ขั้นตอนถัดไป"

### จังหวะ Implementation

สำหรับแต่ละขั้นตอน refactoring:

1. **ตรวจสอบก่อน**
   - test ผ่าน (green)
   - โค้ด compile ได้

2. **เปลี่ยนแปลง ONE อย่างเล็กน้อย**
   - ทำตาม mechanics จาก catalog
   - ให้การเปลี่ยนแปลงน้อยที่สุด

3. **ตรวจสอบ**
   - รัน test ทันที
   - ตรวจสอบ compilation error

4. **ถ้า test ผ่าน (green)**
   - Commit พร้อมข้อความที่อธิบาย
   - ไปยังขั้นตอนถัดไป

5. **ถ้า test ล้มเหลว (red)**
   - หยุดทันที
   - ยกเลิกการเปลี่ยนแปลง
   - วิเคราะห์สิ่งที่ผิดพลาด
   - ถามผู้ใช้ถ้าไม่แน่ใจ

### กลยุทธ์ Commit

แต่ละ commit ควร:
- **Atomic**: การเปลี่ยนแปลง logic เดียว
- **Reversible**: ยกเลิกได้ง่าย
- **Descriptive**: ข้อความ commit ชัดเจน

ตัวอย่างข้อความ commit:
```
refactor: Extract calculateTotal() from processOrder()
refactor: Rename 'x' to 'customerCount' for clarity
refactor: Remove unused validateOldFormat() method
```

### การรายงานความคืบหน้า

หลังแต่ละ sub-phase รายงานต่อผู้ใช้:
- การเปลี่ยนแปลงที่ทำ
- test ยังผ่านอยู่หรือไม่?
- ปัญหาที่พบ
- **ถาม**: "ดำเนินการต่อกับชุดถัดไปไหม?"

---

## Phase 6: การตรวจสอบและการทำซ้ำ

### checklist หลัง Refactoring

- [ ] test ทั้งหมดผ่าน
- [ ] ไม่มี warning/error ใหม่
- [ ] โค้ด compile สำเร็จ
- [ ] พฤติกรรมไม่เปลี่ยน (การตรวจสอบด้วยตนเอง)
- [ ] อัปเดตเอกสารถ้าจำเป็น
- [ ] ประวัติ commit สะอาด

### การเปรียบเทียบ Metric

รัน complexity analysis ก่อนและหลัง:
```bash
python scripts/analyze-complexity.py <file>
```

นำเสนอการปรับปรุง:
- การเปลี่ยนแปลงจำนวนบรรทัด
- การเปลี่ยนแปลง cyclomatic complexity
- การเปลี่ยนแปลง maintainability index

### การตรวจสอบของผู้ใช้

นำเสนอผลลัพธ์สุดท้าย:
- สรุปการเปลี่ยนแปลงทั้งหมด
- การเปรียบเทียบโค้ด before/after
- การปรับปรุง metric
- technical debt ที่เหลืออยู่
- **ถาม**: "คุณพอใจกับการเปลี่ยนแปลงเหล่านี้หรือไม่?"

### ขั้นตอนถัดไป

หารือกับผู้ใช้:
- มี smell เพิ่มเติมที่ต้องแก้ไขหรือไม่?
- วางแผน refactoring ติดตามหรือไม่?
- นำการเปลี่ยนแปลงคล้ายกันไปใช้ที่อื่นหรือไม่?

---

## แนวทางสำคัญ

### เมื่อใดที่ต้องหยุดและถาม

หยุดและปรึกษาผู้ใช้เสมอเมื่อ:
- ไม่แน่ใจเกี่ยวกับ business logic
- การเปลี่ยนแปลงอาจส่งผลต่อ API ภายนอก
- ความครอบคลุมของ test ไม่เพียงพอ
- ต้องการการตัดสินใจด้านสถาปัตยกรรมที่สำคัญ
- ระดับความเสี่ยงเพิ่มขึ้น
- พบความซับซ้อนที่ไม่คาดคิด

### กฎความปลอดภัย

1. **ห้าม refactor โดยไม่มี test** (นอกจากผู้ใช้ยอมรับความเสี่ยงอย่างชัดเจน)
2. **ห้ามเปลี่ยนแปลงใหญ่** - แบ่งเป็นขั้นตอนเล็กๆ
3. **ห้ามข้ามการรัน test** หลังแต่ละการเปลี่ยนแปลง
4. **ห้ามดำเนินการต่อถ้า test ล้มเหลว** - แก้ไขหรือ rollback ก่อน
5. **ห้ามสันนิษฐาน** - เมื่อสงสัย ให้ถาม

### สิ่งที่ไม่ควรทำ

- ห้ามรวม refactoring กับการเพิ่มฟีเจอร์
- ห้าม refactoring ในช่วงวิกฤต production
- ห้าม refactor โค้ดที่ไม่เข้าใจ
- ห้าม over-engineer - ให้เรียบง่าย
- ห้าม refactor ทุกอย่างพร้อมกัน

---

## ตัวอย่าง Quick Start

### สถานการณ์: Long Method ที่มีการซ้ำ

**ก่อน:**
```javascript
function processOrder(order) {
  // 150 บรรทัดของโค้ดที่มี:
  // - logic validation ซ้ำ
  // - การคำนวณแบบ inline
  // - ความรับผิดชอบแบบผสม
}
```

**ขั้นตอน Refactoring:**

1. **ตรวจสอบให้มี test** สำหรับ processOrder()
2. **Extract** validation ไปยัง validateOrder()
3. **ทดสอบ** - ควรผ่าน
4. **Extract** การคำนวณไปยัง calculateOrderTotal()
5. **ทดสอบ** - ควรผ่าน
6. **Extract** notification ไปยัง notifyCustomer()
7. **ทดสอบ** - ควรผ่าน
8. **ตรวจสอบ** - processOrder() ตอนนี้ประสาน 3 function ที่ชัดเจน

**หลัง:**
```javascript
function processOrder(order) {
  validateOrder(order);
  const total = calculateOrderTotal(order);
  notifyCustomer(order, total);
  return { order, total };
}
```

---

## เอกสารอ้างอิง

- [Code Smells Catalog](references/code-smells.md) - รายการ code smell ที่ครบถ้วน
- [Refactoring Catalog](references/refactoring-catalog.md) - เทคนิค refactoring
- [Refactoring Plan Template](templates/refactoring-plan.md) - template การวางแผน

## Script

- `scripts/analyze-complexity.py` - วิเคราะห์ metric ความซับซ้อนของโค้ด
- `scripts/detect-smells.py` - การตรวจจับ smell อัตโนมัติ

## ประวัติเวอร์ชัน

- v1.0.0 (2025-01-15): เปิดตัวครั้งแรกพร้อมวิธีการของ Fowler, แนวทาง phased, จุดปรึกษาผู้ใช้
