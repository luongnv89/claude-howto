<!-- i18n-source: 03-skills/refactor/references/code-smells.md -->
<!-- i18n-date: 2026-05-09 -->
# Code Smells Catalog

รายการอ้างอิง code smell อย่างครอบคลุม อ้างอิงจาก *Refactoring* (ฉบับที่ 2) ของ Martin Fowler Code smell คือสัญญาณบ่งบอกปัญหาที่ลึกกว่า — เป็นตัวบ่งชี้ว่าการออกแบบโค้ดอาจมีข้อบกพร่อง

> "A code smell is a surface indication that usually corresponds to a deeper problem in the system." — Martin Fowler

---

## Bloaters

Code smell ที่แสดงถึงสิ่งที่เติบโตใหญ่เกินไปจนยากต่อการจัดการ

### Long Method

**สัญญาณ:**
- Method เกิน 30-50 บรรทัด
- ต้องเลื่อนหน้าจอเพื่อดู method ทั้งหมด
- มีการ nesting หลายระดับ
- มี comment อธิบายว่าส่วนต่าง ๆ ทำอะไร

**เหตุที่เป็นปัญหา:**
- ยากต่อการทำความเข้าใจ
- ยากต่อการทดสอบแบบแยกส่วน
- การเปลี่ยนแปลงมีผลกระทบที่ไม่ตั้งใจ
- logic ที่ซ้ำกันซ่อนอยู่ภายใน

**Refactoring ที่แนะนำ:**
- Extract Method
- Replace Temp with Query
- Introduce Parameter Object
- Replace Method with Method Object
- Decompose Conditional

**ตัวอย่าง (ก่อน):**
```javascript
function processOrder(order) {
  // ตรวจสอบ order (20 บรรทัด)
  if (!order.items) throw new Error('No items');
  if (order.items.length === 0) throw new Error('Empty order');
  // ... การตรวจสอบเพิ่มเติม

  // คำนวณยอดรวม (30 บรรทัด)
  let subtotal = 0;
  for (const item of order.items) {
    subtotal += item.price * item.quantity;
  }
  // ... ภาษี ค่าขนส่ง ส่วนลด

  // ส่งการแจ้งเตือน (20 บรรทัด)
  // ... logic การส่งอีเมล
}
```

**ตัวอย่าง (หลัง):**
```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  sendOrderNotifications(order, totals);
  return { order, totals };
}
```

---

### Large Class

**สัญญาณ:**
- Class มี instance variable จำนวนมาก (>7-10)
- Class มี method จำนวนมาก (>15-20)
- ชื่อ class ไม่ชัดเจน (Manager, Handler, Processor)
- Method ไม่ได้ใช้ instance variable ทั้งหมด

**เหตุที่เป็นปัญหา:**
- ละเมิด Single Responsibility Principle
- ยากต่อการทดสอบ
- การเปลี่ยนแปลงส่งผลกระทบไปยังฟีเจอร์ที่ไม่เกี่ยวข้อง
- ยากต่อการนำกลับมาใช้ซ้ำบางส่วน

**Refactoring ที่แนะนำ:**
- Extract Class
- Extract Subclass
- Extract Interface

**การตรวจจับ:**
```
Lines of code > 300
Number of methods > 15
Number of fields > 10
```

---

### Primitive Obsession

**สัญญาณ:**
- ใช้ primitive สำหรับ domain concept (string สำหรับ email, int สำหรับเงิน)
- Array ของ primitive แทนที่จะเป็น object
- String constant สำหรับ type code
- Magic number/string

**เหตุที่เป็นปัญหา:**
- ไม่มีการตรวจสอบในระดับ type
- logic กระจัดกระจายทั่ว codebase
- ง่ายต่อการส่งค่าผิด
- ขาด domain concept

**Refactoring ที่แนะนำ:**
- Replace Primitive with Object
- Replace Type Code with Class
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**ตัวอย่าง (ก่อน):**
```javascript
const user = {
  email: 'john@example.com',     // เป็นเพียง string
  phone: '1234567890',           // เป็นเพียง string
  status: 'active',              // Magic string
  balance: 10050                 // Cents เป็น integer
};
```

**ตัวอย่าง (หลัง):**
```javascript
const user = {
  email: new Email('john@example.com'),
  phone: new PhoneNumber('1234567890'),
  status: UserStatus.ACTIVE,
  balance: Money.cents(10050)
};
```

---

### Long Parameter List

**สัญญาณ:**
- Method มี parameter มากกว่า 4 ตัว
- Parameter ที่ปรากฏร่วมกันเสมอ
- Boolean flag ที่เปลี่ยนพฤติกรรมของ method
- ส่ง null/undefined บ่อยครั้ง

**เหตุที่เป็นปัญหา:**
- ยากต่อการเรียกใช้อย่างถูกต้อง
- สับสนในลำดับ parameter
- บ่งชี้ว่า method ทำงานมากเกินไป
- ยากต่อการเพิ่ม parameter ใหม่

**Refactoring ที่แนะนำ:**
- Introduce Parameter Object
- Preserve Whole Object
- Replace Parameter with Method Call
- Remove Flag Argument

**ตัวอย่าง (ก่อน):**
```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy) {
  // ...
}
```

**ตัวอย่าง (หลัง):**
```javascript
function createUser(personalInfo, address, options) {
  // personalInfo: { firstName, lastName, email, phone }
  // address: { street, city, state, zip }
  // options: { isAdmin, isActive, createdBy }
}
```

---

### Data Clumps

**สัญญาณ:**
- field เดิม 3 ตัวขึ้นไปปรากฏด้วยกันซ้ำ ๆ
- Parameter ที่เดินทางร่วมกันเสมอ
- Class ที่มี field บางส่วนอยู่ด้วยกัน

**เหตุที่เป็นปัญหา:**
- logic การจัดการซ้ำกัน
- ขาด abstraction
- ยากต่อการขยาย
- บ่งชี้ class ที่ซ่อนอยู่

**Refactoring ที่แนะนำ:**
- Extract Class
- Introduce Parameter Object
- Preserve Whole Object

**ตัวอย่าง:**
```javascript
// Data clump: พิกัด (x, y, z)
function movePoint(x, y, z, dx, dy, dz) { }
function scalePoint(x, y, z, factor) { }
function distanceBetween(x1, y1, z1, x2, y2, z2) { }

// แยกเป็น Point3D class
class Point3D {
  constructor(x, y, z) { }
  move(delta) { }
  scale(factor) { }
  distanceTo(other) { }
}
```

---

## Object-Orientation Abusers

Smell ที่บ่งชี้การใช้ OOP principles อย่างไม่สมบูรณ์หรือไม่ถูกต้อง

### Switch Statements

**สัญญาณ:**
- switch/case หรือ if/else chain ยาว
- switch เดิมปรากฏในหลายที่
- Switch บน type code
- การเพิ่ม case ใหม่ต้องเปลี่ยนแปลงทุกที่

**เหตุที่เป็นปัญหา:**
- ละเมิด Open/Closed Principle
- การเปลี่ยนแปลงส่งผลไปยัง switch ทุกจุด
- ยากต่อการขยาย
- มักบ่งชี้ว่าขาด polymorphism

**Refactoring ที่แนะนำ:**
- Replace Conditional with Polymorphism
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**ตัวอย่าง (ก่อน):**
```javascript
function calculatePay(employee) {
  switch (employee.type) {
    case 'hourly':
      return employee.hours * employee.rate;
    case 'salaried':
      return employee.salary / 12;
    case 'commissioned':
      return employee.sales * employee.commission;
  }
}
```

**ตัวอย่าง (หลัง):**
```javascript
class HourlyEmployee {
  calculatePay() {
    return this.hours * this.rate;
  }
}

class SalariedEmployee {
  calculatePay() {
    return this.salary / 12;
  }
}
```

---

### Temporary Field

**สัญญาณ:**
- Instance variable ที่ใช้เฉพาะใน method บางตัว
- Field ที่ตั้งค่าแบบมีเงื่อนไข
- การ initialize ที่ซับซ้อนสำหรับบางกรณี

**เหตุที่เป็นปัญหา:**
- สับสน — field มีอยู่แต่อาจเป็น null
- ยากต่อการทำความเข้าใจสถานะของ object
- บ่งชี้ว่ามี conditional logic ซ่อนอยู่

**Refactoring ที่แนะนำ:**
- Extract Class
- Introduce Null Object
- Replace Temp Field with Local

---

### Refused Bequest

**สัญญาณ:**
- Subclass ไม่ได้ใช้ method/data ที่รับมาจาก parent
- Subclass override เพื่อไม่ทำอะไร
- ใช้ inheritance เพื่อนำโค้ดกลับมาใช้ซ้ำ ไม่ใช่ความสัมพันธ์แบบ IS-A

**เหตุที่เป็นปัญหา:**
- Abstraction ผิด
- ละเมิด Liskov Substitution Principle
- hierarchy ที่ทำให้เข้าใจผิด

**Refactoring ที่แนะนำ:**
- Push Down Method/Field
- Replace Subclass with Delegate
- Replace Inheritance with Delegation

---

### Alternative Classes with Different Interfaces

**สัญญาณ:**
- สอง class ที่ทำสิ่งเดียวกัน
- ชื่อ method ต่างกันสำหรับ concept เดียวกัน
- สามารถใช้แทนกันได้

**เหตุที่เป็นปัญหา:**
- implementation ที่ซ้ำกัน
- ไม่มี interface ร่วม
- ยากต่อการสลับใช้

**Refactoring ที่แนะนำ:**
- Rename Method
- Move Method
- Extract Superclass
- Extract Interface

---

## Change Preventers

Smell ที่ทำให้การเปลี่ยนแปลงยากขึ้น — การเปลี่ยนสิ่งหนึ่งต้องเปลี่ยนอีกหลายสิ่ง

### Divergent Change

**สัญญาณ:**
- Class หนึ่งถูกเปลี่ยนแปลงด้วยเหตุผลหลายประการที่แตกต่างกัน
- การเปลี่ยนแปลงในพื้นที่ต่าง ๆ ทำให้ต้องแก้ไข class เดิม
- Class เป็น "God class"

**เหตุที่เป็นปัญหา:**
- ละเมิด Single Responsibility
- มีความถี่การเปลี่ยนแปลงสูง
- Merge conflict

**Refactoring ที่แนะนำ:**
- Extract Class
- Extract Superclass
- Extract Subclass

**ตัวอย่าง:**
`User` class ถูกเปลี่ยนแปลงเนื่องจาก:
- การเปลี่ยนแปลง Authentication
- การเปลี่ยนแปลง Profile
- การเปลี่ยนแปลง Billing
- การเปลี่ยนแปลง Notification

→ แยกเป็น: `AuthService`, `ProfileService`, `BillingService`, `NotificationService`

---

### Shotgun Surgery

**สัญญาณ:**
- การเปลี่ยนแปลงหนึ่งต้องแก้ไขหลาย class
- ฟีเจอร์เล็กน้อยต้องแตะไฟล์กว่า 10 ไฟล์
- การเปลี่ยนแปลงกระจัดกระจาย ยากต่อการค้นหาทั้งหมด

**เหตุที่เป็นปัญหา:**
- ง่ายต่อการพลาดจุดที่ต้องแก้
- มี coupling สูง
- การเปลี่ยนแปลงมีโอกาสเกิด error สูง

**Refactoring ที่แนะนำ:**
- Move Method
- Move Field
- Inline Class

**การตรวจจับ:**
ค้นหา: การเพิ่ม field หนึ่งต้องเปลี่ยนแปลงมากกว่า 5 ไฟล์

---

### Parallel Inheritance Hierarchies

**สัญญาณ:**
- การสร้าง subclass ใน hierarchy หนึ่งต้องสร้าง subclass ในอีก hierarchy หนึ่ง
- prefix ของ class ตรงกัน (เช่น `DatabaseOrder`, `DatabaseProduct`)

**เหตุที่เป็นปัญหา:**
- ต้องดูแลรักษาสองเท่า
- มี coupling ระหว่าง hierarchy
- ง่ายต่อการลืมฝั่งหนึ่ง

**Refactoring ที่แนะนำ:**
- Move Method
- Move Field
- ลบ hierarchy หนึ่งออก

---

## Dispensables

สิ่งที่ไม่จำเป็นและควรถูกลบออก

### Comments (Excessive)

**สัญญาณ:**
- Comment ที่อธิบายว่าโค้ดทำอะไร
- โค้ดที่ถูก comment ออก
- TODO/FIXME ที่ค้างนานมาก
- การขอโทษใน comment

**เหตุที่เป็นปัญหา:**
- Comment มักไม่ตรงกับความเป็นจริง (ไม่ได้ update ตามโค้ด)
- โค้ดควรอธิบายตัวเองได้
- โค้ดที่ตายแล้วสร้างความสับสน

**Refactoring ที่แนะนำ:**
- Extract Method (ชื่ออธิบายว่าทำอะไร)
- Rename (ความชัดเจนโดยไม่ต้องมี comment)
- ลบโค้ดที่ถูก comment ออก
- Introduce Assertion

**Comment ที่ดี vs ไม่ดี:**
```javascript
// ไม่ดี: อธิบายว่าทำอะไร
// วนซ้ำผ่าน user และตรวจสอบว่า active
for (const user of users) {
  if (user.status === 'active') { }
}

// ดี: อธิบายว่าทำไม
// เฉพาะ active user — inactive จัดการโดย cleanup job
const activeUsers = users.filter(u => u.isActive);
```

---

### Duplicate Code

**สัญญาณ:**
- โค้ดเดิมปรากฏในหลายที่
- โค้ดที่คล้ายกันพร้อมการเปลี่ยนแปลงเล็กน้อย
- รูปแบบการ copy-paste

**เหตุที่เป็นปัญหา:**
- การแก้ไข bug ต้องทำในหลายที่
- ความเสี่ยงจากความไม่สอดคล้องกัน
- Codebase บวมโต

**Refactoring ที่แนะนำ:**
- Extract Method
- Extract Class
- Pull Up Method (ใน hierarchy)
- Form Template Method

**กฎการตรวจจับ:**
โค้ดที่ซ้ำกัน 3 ครั้งขึ้นไปควรถูกแยกออก

---

### Lazy Class

**สัญญาณ:**
- Class ทำงานไม่พอที่จะสมเหตุสมผลในการมีอยู่
- Wrapper ที่ไม่มีคุณค่าเพิ่มเติม
- ผลจากการ over-engineering

**เหตุที่เป็นปัญหา:**
- ภาระการดูแลรักษา
- Indirection ที่ไม่จำเป็น
- ความซับซ้อนโดยไม่มีประโยชน์

**Refactoring ที่แนะนำ:**
- Inline Class
- Collapse Hierarchy

---

### Dead Code

**สัญญาณ:**
- โค้ดที่ไม่สามารถเข้าถึงได้
- Variable/method/class ที่ไม่ได้ใช้งาน
- โค้ดที่ถูก comment ออก
- โค้ดหลังเงื่อนไขที่เป็นไปไม่ได้

**เหตุที่เป็นปัญหา:**
- ความสับสน
- ภาระการดูแลรักษา
- ชะลอความเข้าใจ

**Refactoring ที่แนะนำ:**
- Remove Dead Code
- Safe Delete

**การตรวจจับ:**
```bash
# ค้นหา export ที่ไม่ได้ใช้
# ค้นหา function ที่ไม่มีการอ้างอิง
# คำเตือน "unused" ใน IDE
```

---

### Speculative Generality

**สัญญาณ:**
- Abstract class ที่มี subclass เพียงตัวเดียว
- Parameter ที่ไม่ได้ใช้ "สำหรับอนาคต"
- Method ที่ทำหน้าที่เพียงแค่ delegate
- "Framework" สำหรับ use case เดียว

**เหตุที่เป็นปัญหา:**
- ความซับซ้อนโดยไม่มีประโยชน์
- YAGNI (You Ain't Gonna Need It)
- ยากต่อความเข้าใจ

**Refactoring ที่แนะนำ:**
- Collapse Hierarchy
- Inline Class
- Remove Parameter
- Rename Method

---

## Couplers

Smell ที่แสดงถึง coupling ที่มากเกินไประหว่าง class

### Feature Envy

**สัญญาณ:**
- Method ใช้ข้อมูลจาก class อื่นมากกว่า class ของตัวเอง
- การเรียก getter หลายครั้งไปยัง object อื่น
- ข้อมูลและพฤติกรรมถูกแยกออกจากกัน

**เหตุที่เป็นปัญหา:**
- ตำแหน่งของ behavior ไม่ถูกต้อง
- Encapsulation ไม่ดี
- ยากต่อการดูแลรักษา

**Refactoring ที่แนะนำ:**
- Move Method
- Move Field
- Extract Method (จากนั้น move)

**ตัวอย่าง (ก่อน):**
```javascript
class Order {
  getDiscountedPrice(customer) {
    // ใช้ข้อมูลของ customer เป็นหลัก
    if (customer.loyaltyYears > 5) {
      return this.price * customer.discountRate;
    }
    return this.price;
  }
}
```

**ตัวอย่าง (หลัง):**
```javascript
class Customer {
  getDiscountedPriceFor(price) {
    if (this.loyaltyYears > 5) {
      return price * this.discountRate;
    }
    return price;
  }
}
```

---

### Inappropriate Intimacy

**สัญญาณ:**
- Class เข้าถึง private ของกันและกัน
- การอ้างอิงแบบสองทิศทาง
- Subclass รู้มากเกินไปเกี่ยวกับ parent

**เหตุที่เป็นปัญหา:**
- Coupling สูง
- การเปลี่ยนแปลงส่งผลกระทบเป็นลูกโซ่
- ยากต่อการแก้ไขสิ่งหนึ่งโดยไม่กระทบอีกสิ่ง

**Refactoring ที่แนะนำ:**
- Move Method
- Move Field
- Change Bidirectional to Unidirectional
- Extract Class
- Hide Delegate

---

### Message Chains

**สัญญาณ:**
- การเรียก method เป็นลูกโซ่ยาว: `a.getB().getC().getD().getValue()`
- Client ขึ้นอยู่กับโครงสร้างการนำทาง
- โค้ดแบบ "Train wreck"

**เหตุที่เป็นปัญหา:**
- เปราะบาง — การเปลี่ยนแปลงใดก็ทำให้ลูกโซ่พัง
- ละเมิด Law of Demeter
- มี coupling กับโครงสร้าง

**Refactoring ที่แนะนำ:**
- Hide Delegate
- Extract Method
- Move Method

**ตัวอย่าง:**
```javascript
// ไม่ดี: Message chain
const managerName = employee.getDepartment().getManager().getName();

// ดีกว่า: ซ่อน delegation
const managerName = employee.getManagerName();
```

---

### Middle Man

**สัญญาณ:**
- Class ที่ทำหน้าที่เพียงแค่ delegate ไปยังอีก class
- Method ครึ่งหนึ่งเป็น delegation
- ไม่มีคุณค่าเพิ่มเติม

**เหตุที่เป็นปัญหา:**
- Indirection ที่ไม่จำเป็น
- ภาระการดูแลรักษา
- สถาปัตยกรรมที่สับสน

**Refactoring ที่แนะนำ:**
- Remove Middle Man
- Inline Method

---

## คู่มือระดับความรุนแรงของ Smell

| ระดับความรุนแรง | คำอธิบาย | การดำเนินการ |
|----------|-------------|--------|
| **Critical** | ขัดขวางการพัฒนา ก่อให้เกิด bug | แก้ไขทันที |
| **High** | ภาระการดูแลรักษาอย่างมีนัยสำคัญ | แก้ไขใน sprint ปัจจุบัน |
| **Medium** | สังเกตเห็นได้แต่จัดการได้ | วางแผนสำหรับอนาคตอันใกล้ |
| **Low** | ความไม่สะดวกเล็กน้อย | แก้ไขตามโอกาส |

---

## Checklist การตรวจจับอย่างรวดเร็ว

ใช้ checklist นี้เมื่อสแกนโค้ด:

- [ ] มี method ที่เกิน 30 บรรทัดหรือไม่?
- [ ] มี class ที่เกิน 300 บรรทัดหรือไม่?
- [ ] มี method ที่มี parameter มากกว่า 4 ตัวหรือไม่?
- [ ] มีบล็อกโค้ดที่ซ้ำกันหรือไม่?
- [ ] มี switch/case บน type code หรือไม่?
- [ ] มีโค้ดที่ไม่ได้ใช้งานหรือไม่?
- [ ] มี method ที่ใช้ข้อมูลของ class อื่นเป็นหลักหรือไม่?
- [ ] มีการเรียก method เป็นลูกโซ่ยาวหรือไม่?
- [ ] มี comment ที่อธิบาย "อะไร" ไม่ใช่ "ทำไม" หรือไม่?
- [ ] มี primitive ที่ควรเป็น object หรือไม่?

---

## เอกสารอ่านเพิ่มเติม

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- Kerievsky, J. (2004). *Refactoring to Patterns*
- Feathers, M. (2004). *Working Effectively with Legacy Code*
