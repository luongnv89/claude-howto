<!-- i18n-source: 03-skills/refactor/references/refactoring-catalog.md -->
<!-- i18n-date: 2026-05-09 -->
# Refactoring Catalog

รายการเทคนิค refactoring ที่คัดสรรมาจาก *Refactoring* (ฉบับที่ 2) ของ Martin Fowler แต่ละ refactoring มีแรงจูงใจ กลไกทีละขั้นตอน และตัวอย่าง

> "A refactoring is defined by its mechanics—the precise sequence of steps that you follow to carry out the change." — Martin Fowler

---

## วิธีการใช้ Catalog นี้

1. **ระบุ smell** โดยใช้ code smells reference
2. **ค้นหา refactoring ที่ตรงกัน** ใน catalog นี้
3. **ปฏิบัติตามกลไก** ทีละขั้นตอน
4. **ทดสอบหลังแต่ละขั้นตอน** เพื่อให้แน่ใจว่าพฤติกรรมยังคงเดิม

**กฎทอง**: หากขั้นตอนใดใช้เวลามากกว่า 10 นาที ให้แบ่งเป็นขั้นตอนเล็กกว่า

---

## Refactoring ที่พบบ่อยที่สุด

### Extract Method

**เมื่อใดที่ควรใช้**: Method ยาว โค้ดซ้ำกัน ต้องการตั้งชื่อ concept

**แรงจูงใจ**: เปลี่ยน code fragment เป็น method ที่มีชื่ออธิบายจุดประสงค์

**กลไก**:
1. สร้าง method ใหม่ตามสิ่งที่ทำ (ไม่ใช่วิธีการทำ)
2. คัดลอก code fragment ไปยัง method ใหม่
3. สแกนหา local variable ที่ใช้ใน fragment
4. ส่ง local variable เป็น parameter (หรือประกาศใน method)
5. จัดการ return value อย่างเหมาะสม
6. แทนที่ fragment เดิมด้วยการเรียก method ใหม่
7. ทดสอบ

**ก่อน**:
```javascript
function printOwing(invoice) {
  let outstanding = 0;

  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");

  // คำนวณยอดค้างชำระ
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // แสดงรายละเอียด
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

**หลัง**:
```javascript
function printOwing(invoice) {
  printBanner();
  const outstanding = calculateOutstanding(invoice);
  printDetails(invoice, outstanding);
}

function printBanner() {
  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");
}

function calculateOutstanding(invoice) {
  return invoice.orders.reduce((sum, order) => sum + order.amount, 0);
}

function printDetails(invoice, outstanding) {
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

---

### Inline Method

**เมื่อใดที่ควรใช้**: body ของ method ชัดเจนพอ ๆ กับชื่อของมัน มีการ delegate มากเกินไป

**แรงจูงใจ**: ลบ indirection ที่ไม่จำเป็นเมื่อ method ไม่ได้เพิ่มคุณค่า

**กลไก**:
1. ตรวจสอบว่า method ไม่ใช่ polymorphic
2. ค้นหาการเรียก method ทั้งหมด
3. แทนที่แต่ละการเรียกด้วย body ของ method
4. ทดสอบหลังการแทนที่แต่ละครั้ง
5. ลบ definition ของ method

**ก่อน**:
```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**หลัง**:
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### Extract Variable

**เมื่อใดที่ควรใช้**: expression ซับซ้อนที่ยากต่อการเข้าใจ

**แรงจูงใจ**: ตั้งชื่อให้กับส่วนของ expression ที่ซับซ้อน

**กลไก**:
1. ตรวจสอบว่า expression ไม่มี side effect
2. ประกาศ variable ที่ immutable
3. ตั้งค่าให้เท่ากับผลลัพธ์ของ expression (หรือบางส่วน)
4. แทนที่ expression เดิมด้วย variable
5. ทดสอบ

**ก่อน**:
```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**หลัง**:
```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### Inline Variable

**เมื่อใดที่ควรใช้**: ชื่อ variable ไม่ได้สื่อความหมายมากกว่า expression

**แรงจูงใจ**: ลบ indirection ที่ไม่จำเป็น

**กลไก**:
1. ตรวจสอบว่า right-hand side ไม่มี side effect
2. หาก variable ไม่ใช่ immutable ให้ทำให้เป็น immutable และทดสอบ
3. ค้นหาการอ้างอิงแรกและแทนที่ด้วย expression
4. ทดสอบ
5. ทำซ้ำสำหรับการอ้างอิงทั้งหมด
6. ลบการประกาศและการกำหนดค่า
7. ทดสอบ

---

### Rename Variable

**เมื่อใดที่ควรใช้**: ชื่อไม่สื่อจุดประสงค์อย่างชัดเจน

**แรงจูงใจ**: ชื่อที่ดีมีความสำคัญต่อโค้ดที่สะอาด

**กลไก**:
1. หาก variable ถูกใช้งานอย่างกว้างขวาง พิจารณา encapsulating
2. ค้นหาการอ้างอิงทั้งหมด
3. เปลี่ยนแต่ละการอ้างอิง
4. ทดสอบ

**คำแนะนำ**:
- ใช้ชื่อที่สื่อเจตนา
- หลีกเลี่ยงการย่อ
- ใช้คำศัพท์จาก domain

```javascript
// ไม่ดี
const d = 30;
const x = users.filter(u => u.a);

// ดี
const daysSinceLastLogin = 30;
const activeUsers = users.filter(user => user.isActive);
```

---

### Change Function Declaration

**เมื่อใดที่ควรใช้**: ชื่อ function ไม่อธิบายจุดประสงค์ parameter ต้องการการเปลี่ยนแปลง

**แรงจูงใจ**: ชื่อ function ที่ดีทำให้โค้ดอธิบายตัวเองได้

**กลไก (เรียบง่าย)**:
1. ลบ parameter ที่ไม่ต้องการ
2. เปลี่ยนชื่อ
3. เพิ่ม parameter ที่ต้องการ
4. ทดสอบ

**กลไก (Migration — สำหรับการเปลี่ยนแปลงที่ซับซ้อน)**:
1. หากลบ parameter ให้ตรวจสอบว่าไม่ได้ถูกใช้
2. สร้าง function ใหม่ด้วย declaration ที่ต้องการ
3. ให้ function เดิมเรียก function ใหม่
4. ทดสอบ
5. เปลี่ยน caller ให้ใช้ function ใหม่
6. ทดสอบหลังแต่ละครั้ง
7. ลบ function เดิม

**ก่อน**:
```javascript
function circum(radius) {
  return 2 * Math.PI * radius;
}
```

**หลัง**:
```javascript
function circumference(radius) {
  return 2 * Math.PI * radius;
}
```

---

### Encapsulate Variable

**เมื่อใดที่ควรใช้**: การเข้าถึงข้อมูลโดยตรงจากหลายที่

**แรงจูงใจ**: ให้จุดเข้าถึงที่ชัดเจนสำหรับการจัดการข้อมูล

**กลไก**:
1. สร้าง getter และ setter function
2. ค้นหาการอ้างอิงทั้งหมด
3. แทนที่การอ่านด้วย getter
4. แทนที่การเขียนด้วย setter
5. ทดสอบหลังแต่ละการเปลี่ยนแปลง
6. จำกัด visibility ของ variable

**ก่อน**:
```javascript
let defaultOwner = { firstName: "Martin", lastName: "Fowler" };

// ใช้ในหลายที่
spaceship.owner = defaultOwner;
```

**หลัง**:
```javascript
let defaultOwnerData = { firstName: "Martin", lastName: "Fowler" };

function defaultOwner() { return defaultOwnerData; }
function setDefaultOwner(arg) { defaultOwnerData = arg; }

spaceship.owner = defaultOwner();
```

---

### Introduce Parameter Object

**เมื่อใดที่ควรใช้**: หลาย parameter ที่มักปรากฏร่วมกัน

**แรงจูงใจ**: จัดกลุ่มข้อมูลที่อยู่ด้วยกันตามธรรมชาติ

**กลไก**:
1. สร้าง class/structure ใหม่สำหรับ parameter ที่จัดกลุ่ม
2. ทดสอบ
3. ใช้ Change Function Declaration เพื่อเพิ่ม object ใหม่
4. ทดสอบ
5. สำหรับแต่ละ parameter ในกลุ่ม ให้ลบออกจาก function และใช้ object ใหม่แทน
6. ทดสอบหลังแต่ละครั้ง

**ก่อน**:
```javascript
function amountInvoiced(startDate, endDate) { ... }
function amountReceived(startDate, endDate) { ... }
function amountOverdue(startDate, endDate) { ... }
```

**หลัง**:
```javascript
class DateRange {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }
}

function amountInvoiced(dateRange) { ... }
function amountReceived(dateRange) { ... }
function amountOverdue(dateRange) { ... }
```

---

### Combine Functions into Class

**เมื่อใดที่ควรใช้**: หลาย function ที่ทำงานกับข้อมูลเดียวกัน

**แรงจูงใจ**: จัดกลุ่ม function กับข้อมูลที่ทำงานด้วย

**กลไก**:
1. Apply Encapsulate Record กับข้อมูลร่วม
2. ย้าย function แต่ละตัวเข้าไปใน class
3. ทดสอบหลังการย้ายแต่ละครั้ง
4. แทนที่ argument ของข้อมูลด้วยการใช้ field ของ class

**ก่อน**:
```javascript
function base(reading) { ... }
function taxableCharge(reading) { ... }
function calculateBaseCharge(reading) { ... }
```

**หลัง**:
```javascript
class Reading {
  constructor(data) { this._data = data; }

  get base() { ... }
  get taxableCharge() { ... }
  get calculateBaseCharge() { ... }
}
```

---

### Split Phase

**เมื่อใดที่ควรใช้**: โค้ดจัดการกับสองสิ่งที่แตกต่างกัน

**แรงจูงใจ**: แยกโค้ดออกเป็น phase ที่ชัดเจนพร้อม boundary ที่ชัดเจน

**กลไก**:
1. สร้าง function ที่สองสำหรับ phase ที่สอง
2. ทดสอบ
3. สร้าง intermediate data structure ระหว่าง phase
4. ทดสอบ
5. แยก phase แรกออกเป็น function ของตัวเอง
6. ทดสอบ

**ก่อน**:
```javascript
function priceOrder(product, quantity, shippingMethod) {
  const basePrice = product.basePrice * quantity;
  const discount = Math.max(quantity - product.discountThreshold, 0)
    * product.basePrice * product.discountRate;
  const shippingPerCase = (basePrice > shippingMethod.discountThreshold)
    ? shippingMethod.discountedFee : shippingMethod.feePerCase;
  const shippingCost = quantity * shippingPerCase;
  return basePrice - discount + shippingCost;
}
```

**หลัง**:
```javascript
function priceOrder(product, quantity, shippingMethod) {
  const priceData = calculatePricingData(product, quantity);
  return applyShipping(priceData, shippingMethod);
}

function calculatePricingData(product, quantity) {
  const basePrice = product.basePrice * quantity;
  const discount = Math.max(quantity - product.discountThreshold, 0)
    * product.basePrice * product.discountRate;
  return { basePrice, quantity, discount };
}

function applyShipping(priceData, shippingMethod) {
  const shippingPerCase = (priceData.basePrice > shippingMethod.discountThreshold)
    ? shippingMethod.discountedFee : shippingMethod.feePerCase;
  const shippingCost = priceData.quantity * shippingPerCase;
  return priceData.basePrice - priceData.discount + shippingCost;
}
```

---

## การย้าย Feature

### Move Method

**เมื่อใดที่ควรใช้**: Method ใช้ feature ของ class อื่นมากกว่า class ของตัวเอง

**แรงจูงใจ**: วาง function ไว้กับข้อมูลที่ใช้มากที่สุด

**กลไก**:
1. ตรวจสอบ element ทั้งหมดของโปรแกรมที่ method ใช้ใน class ของตัวเอง
2. ตรวจสอบว่า method เป็น polymorphic หรือไม่
3. คัดลอก method ไปยัง target class
4. ปรับให้เหมาะกับ context ใหม่
5. ให้ method เดิม delegate ไปยัง target
6. ทดสอบ
7. พิจารณาลบ method เดิม

---

### Move Field

**เมื่อใดที่ควรใช้**: Field ถูกใช้มากกว่าโดย class อื่น

**แรงจูงใจ**: เก็บข้อมูลไว้กับ function ที่ใช้มัน

**กลไก**:
1. Encapsulate field หากยังไม่ได้ทำ
2. ทดสอบ
3. สร้าง field ใน target
4. อัปเดตการอ้างอิงให้ใช้ target field
5. ทดสอบ
6. ลบ field เดิม

---

### Move Statements into Function

**เมื่อใดที่ควรใช้**: โค้ดเดิมปรากฏพร้อมการเรียก function เสมอ

**แรงจูงใจ**: ลบ duplication โดยย้ายโค้ดที่ซ้ำกันเข้าไปใน function

**กลไก**:
1. แยกโค้ดที่ซ้ำกันออกเป็น function หากยังไม่ได้ทำ
2. ย้าย statement เข้าไปใน function นั้น
3. ทดสอบ
4. หาก caller ไม่จำเป็นต้องมี statement แยกอีกต่อไป ให้ลบออก

---

### Move Statements to Callers

**เมื่อใดที่ควรใช้**: พฤติกรรมร่วมที่แตกต่างกันระหว่าง caller

**แรงจูงใจ**: เมื่อพฤติกรรมต้องแตกต่างกัน ให้ย้ายออกจาก function

**กลไก**:
1. ใช้ Extract Method กับโค้ดที่จะย้าย
2. ใช้ Inline Method กับ function เดิม
3. ลบการเรียกที่ถูก inline แล้ว
4. ย้ายโค้ดที่แยกออกมาไปยังแต่ละ caller
5. ทดสอบ

---

## การจัดระเบียบข้อมูล

### Replace Primitive with Object

**เมื่อใดที่ควรใช้**: รายการข้อมูลต้องการพฤติกรรมมากกว่าค่าเรียบง่าย

**แรงจูงใจ**: Encapsulate ข้อมูลพร้อมกับพฤติกรรมของมัน

**กลไก**:
1. Apply Encapsulate Variable
2. สร้าง value class อย่างง่าย
3. เปลี่ยน setter ให้สร้าง instance ใหม่
4. เปลี่ยน getter ให้ return ค่า
5. ทดสอบ
6. เพิ่มพฤติกรรมที่หลากหลายกว่าลงใน class ใหม่

**ก่อน**:
```javascript
class Order {
  constructor(data) {
    this.priority = data.priority; // string: "high", "rush", เป็นต้น
  }
}

// การใช้งาน
if (order.priority === "high" || order.priority === "rush") { ... }
```

**หลัง**:
```javascript
class Priority {
  constructor(value) {
    if (!Priority.legalValues().includes(value))
      throw new Error(`Invalid priority: ${value}`);
    this._value = value;
  }

  static legalValues() { return ['low', 'normal', 'high', 'rush']; }
  get value() { return this._value; }

  higherThan(other) {
    return Priority.legalValues().indexOf(this._value) >
           Priority.legalValues().indexOf(other._value);
  }
}

// การใช้งาน
if (order.priority.higherThan(new Priority("normal"))) { ... }
```

---

### Replace Temp with Query

**เมื่อใดที่ควรใช้**: Variable ชั่วคราวที่เก็บผลลัพธ์ของ expression

**แรงจูงใจ**: ทำให้โค้ดชัดเจนขึ้นโดยแยก expression ออกเป็น function

**กลไก**:
1. ตรวจสอบว่า variable ถูกกำหนดค่าเพียงครั้งเดียว
2. แยก right-hand side ของการกำหนดค่าออกเป็น method
3. แทนที่การอ้างอิงถึง temp ด้วยการเรียก method
4. ทดสอบ
5. ลบการประกาศและการกำหนดค่า temp

**ก่อน**:
```javascript
const basePrice = this._quantity * this._itemPrice;
if (basePrice > 1000) {
  return basePrice * 0.95;
} else {
  return basePrice * 0.98;
}
```

**หลัง**:
```javascript
get basePrice() {
  return this._quantity * this._itemPrice;
}

// ใน method
if (this.basePrice > 1000) {
  return this.basePrice * 0.95;
} else {
  return this.basePrice * 0.98;
}
```

---

## การทำให้ Conditional Logic เรียบง่าย

### Decompose Conditional

**เมื่อใดที่ควรใช้**: conditional statement ที่ซับซ้อน (if-then-else)

**แรงจูงใจ**: ทำให้เจตนาชัดเจนโดยแยกเงื่อนไขและการดำเนินการออกมา

**กลไก**:
1. Apply Extract Method กับเงื่อนไข
2. Apply Extract Method กับ then-branch
3. Apply Extract Method กับ else-branch (หากมี)

**ก่อน**:
```javascript
if (!aDate.isBefore(plan.summerStart) && !aDate.isAfter(plan.summerEnd)) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}
```

**หลัง**:
```javascript
if (isSummer(aDate, plan)) {
  charge = summerCharge(quantity, plan);
} else {
  charge = regularCharge(quantity, plan);
}

function isSummer(date, plan) {
  return !date.isBefore(plan.summerStart) && !date.isAfter(plan.summerEnd);
}

function summerCharge(quantity, plan) {
  return quantity * plan.summerRate;
}

function regularCharge(quantity, plan) {
  return quantity * plan.regularRate + plan.regularServiceCharge;
}
```

---

### Consolidate Conditional Expression

**เมื่อใดที่ควรใช้**: หลายเงื่อนไขที่ให้ผลลัพธ์เดียวกัน

**แรงจูงใจ**: ทำให้ชัดเจนว่าเงื่อนไขเป็นการตรวจสอบครั้งเดียว

**กลไก**:
1. ตรวจสอบว่าเงื่อนไขไม่มี side effect
2. รวมเงื่อนไขโดยใช้ `and` หรือ `or`
3. พิจารณา Extract Method กับเงื่อนไขที่รวมแล้ว

**ก่อน**:
```javascript
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;
```

**หลัง**:
```javascript
if (isNotEligibleForDisability(employee)) return 0;

function isNotEligibleForDisability(employee) {
  return employee.seniority < 2 ||
         employee.monthsDisabled > 12 ||
         employee.isPartTime;
}
```

---

### Replace Nested Conditional with Guard Clauses

**เมื่อใดที่ควรใช้**: conditional ที่ซ้อนกันลึกทำให้ flow ยากต่อการติดตาม

**แรงจูงใจ**: ใช้ guard clause สำหรับกรณีพิเศษ เพื่อให้ flow ปกติชัดเจน

**กลไก**:
1. ค้นหาเงื่อนไขกรณีพิเศษ
2. แทนที่ด้วย guard clause ที่ return เร็ว
3. ทดสอบหลังแต่ละการเปลี่ยนแปลง

**ก่อน**:
```javascript
function payAmount(employee) {
  let result;
  if (employee.isSeparated) {
    result = { amount: 0, reasonCode: "SEP" };
  } else {
    if (employee.isRetired) {
      result = { amount: 0, reasonCode: "RET" };
    } else {
      result = calculateNormalPay(employee);
    }
  }
  return result;
}
```

**หลัง**:
```javascript
function payAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reasonCode: "SEP" };
  if (employee.isRetired) return { amount: 0, reasonCode: "RET" };
  return calculateNormalPay(employee);
}
```

---

### Replace Conditional with Polymorphism

**เมื่อใดที่ควรใช้**: Switch/case ตาม type, conditional logic ที่แตกต่างตาม type

**แรงจูงใจ**: ให้ object จัดการพฤติกรรมของตัวเอง

**กลไก**:
1. สร้าง class hierarchy (หากยังไม่มี)
2. ใช้ Factory Function สำหรับการสร้าง object
3. ย้าย conditional logic ไปยัง superclass method
4. สร้าง subclass method สำหรับแต่ละกรณี
5. ลบ conditional เดิม

**ก่อน**:
```javascript
function plumages(birds) {
  return birds.map(b => plumage(b));
}

function plumage(bird) {
  switch (bird.type) {
    case 'EuropeanSwallow':
      return "average";
    case 'AfricanSwallow':
      return (bird.numberOfCoconuts > 2) ? "tired" : "average";
    case 'NorwegianBlueParrot':
      return (bird.voltage > 100) ? "scorched" : "beautiful";
    default:
      return "unknown";
  }
}
```

**หลัง**:
```javascript
class Bird {
  get plumage() { return "unknown"; }
}

class EuropeanSwallow extends Bird {
  get plumage() { return "average"; }
}

class AfricanSwallow extends Bird {
  get plumage() {
    return (this.numberOfCoconuts > 2) ? "tired" : "average";
  }
}

class NorwegianBlueParrot extends Bird {
  get plumage() {
    return (this.voltage > 100) ? "scorched" : "beautiful";
  }
}

function createBird(data) {
  switch (data.type) {
    case 'EuropeanSwallow': return new EuropeanSwallow(data);
    case 'AfricanSwallow': return new AfricanSwallow(data);
    case 'NorwegianBlueParrot': return new NorwegianBlueParrot(data);
    default: return new Bird(data);
  }
}
```

---

### Introduce Special Case (Null Object)

**เมื่อใดที่ควรใช้**: การตรวจสอบ null ซ้ำ ๆ สำหรับกรณีพิเศษ

**แรงจูงใจ**: Return object พิเศษที่จัดการกรณีพิเศษ

**กลไก**:
1. สร้าง special case class ด้วย interface ที่คาดหวัง
2. เพิ่มการตรวจสอบ isSpecialCase
3. สร้าง factory method
4. แทนที่การตรวจสอบ null ด้วยการใช้ special case object
5. ทดสอบ

**ก่อน**:
```javascript
const customer = site.customer;
// ... หลายที่ที่ตรวจสอบ
if (customer === "unknown") {
  customerName = "occupant";
} else {
  customerName = customer.name;
}
```

**หลัง**:
```javascript
class UnknownCustomer {
  get name() { return "occupant"; }
  get billingPlan() { return registry.defaultPlan; }
}

// Factory method
function customer(site) {
  return site.customer === "unknown"
    ? new UnknownCustomer()
    : site.customer;
}

// การใช้งาน — ไม่ต้องตรวจสอบ null
const customerName = customer.name;
```

---

## การ Refactoring API

### Separate Query from Modifier

**เมื่อใดที่ควรใช้**: Function ทั้ง return ค่าและมี side effect

**แรงจูงใจ**: ทำให้ชัดเจนว่า operation ใดมี side effect

**กลไก**:
1. สร้าง query function ใหม่
2. คัดลอก return logic ของ function เดิม
3. แก้ไข function เดิมให้ return void
4. แทนที่การเรียกที่ใช้ return value
5. ทดสอบ

**ก่อน**:
```javascript
function alertForMiscreant(people) {
  for (const p of people) {
    if (p === "Don") {
      setOffAlarms();
      return "Don";
    }
    if (p === "John") {
      setOffAlarms();
      return "John";
    }
  }
  return "";
}
```

**หลัง**:
```javascript
function findMiscreant(people) {
  for (const p of people) {
    if (p === "Don") return "Don";
    if (p === "John") return "John";
  }
  return "";
}

function alertForMiscreant(people) {
  if (findMiscreant(people) !== "") setOffAlarms();
}
```

---

### Parameterize Function

**เมื่อใดที่ควรใช้**: หลาย function ที่ทำสิ่งคล้ายกันด้วยค่าต่างกัน

**แรงจูงใจ**: ลบ duplication โดยเพิ่ม parameter

**กลไก**:
1. เลือก function หนึ่ง
2. เพิ่ม parameter สำหรับ literal ที่แตกต่างกัน
3. เปลี่ยน body ให้ใช้ parameter
4. ทดสอบ
5. เปลี่ยน caller ให้ใช้เวอร์ชันที่ parameterized
6. ลบ function ที่ไม่ได้ใช้แล้ว

**ก่อน**:
```javascript
function tenPercentRaise(person) {
  person.salary = person.salary * 1.10;
}

function fivePercentRaise(person) {
  person.salary = person.salary * 1.05;
}
```

**หลัง**:
```javascript
function raise(person, factor) {
  person.salary = person.salary * (1 + factor);
}

// การใช้งาน
raise(person, 0.10);
raise(person, 0.05);
```

---

### Remove Flag Argument

**เมื่อใดที่ควรใช้**: Boolean parameter ที่เปลี่ยนพฤติกรรมของ function

**แรงจูงใจ**: ทำให้พฤติกรรมชัดเจนผ่าน function แยกกัน

**กลไก**:
1. สร้าง function ที่ชัดเจนสำหรับแต่ละค่า flag
2. แทนที่แต่ละการเรียกด้วย function ใหม่ที่เหมาะสม
3. ทดสอบหลังแต่ละการเปลี่ยนแปลง
4. ลบ function เดิม

**ก่อน**:
```javascript
function bookConcert(customer, isPremium) {
  if (isPremium) {
    // premium booking logic
  } else {
    // regular booking logic
  }
}

bookConcert(customer, true);
bookConcert(customer, false);
```

**หลัง**:
```javascript
function bookPremiumConcert(customer) {
  // premium booking logic
}

function bookRegularConcert(customer) {
  // regular booking logic
}

bookPremiumConcert(customer);
bookRegularConcert(customer);
```

---

## การจัดการกับ Inheritance

### Pull Up Method

**เมื่อใดที่ควรใช้**: method เดิมปรากฏใน subclass หลายตัว

**แรงจูงใจ**: ลบ duplication ใน class hierarchy

**กลไก**:
1. ตรวจสอบว่า method เหมือนกัน
2. ตรวจสอบว่า signature เหมือนกัน
3. สร้าง method ใหม่ใน superclass
4. คัดลอก body จาก subclass หนึ่ง
5. ลบ method ของ subclass หนึ่ง แล้วทดสอบ
6. ลบ method ของ subclass อื่น ๆ แล้วทดสอบแต่ละครั้ง

---

### Push Down Method

**เมื่อใดที่ควรใช้**: พฤติกรรมที่เกี่ยวข้องกับเฉพาะ subclass บางตัว

**แรงจูงใจ**: วาง method ไว้ที่ที่มีการใช้งาน

**กลไก**:
1. คัดลอก method ไปยังแต่ละ subclass ที่ต้องการ
2. ลบ method จาก superclass
3. ทดสอบ
4. ลบจาก subclass ที่ไม่ต้องการ
5. ทดสอบ

---

### Replace Subclass with Delegate

**เมื่อใดที่ควรใช้**: ใช้ inheritance อย่างไม่ถูกต้อง ต้องการความยืดหยุ่นมากขึ้น

**แรงจูงใจ**: ใช้ composition แทน inheritance เมื่อเหมาะสม

**กลไก**:
1. สร้าง class ว่างสำหรับ delegate
2. เพิ่ม field ใน host class สำหรับเก็บ delegate
3. สร้าง constructor สำหรับ delegate เรียกจาก host
4. ย้าย feature ไปยัง delegate
5. ทดสอบหลังการย้ายแต่ละครั้ง
6. แทนที่ inheritance ด้วย delegation

---

## Extract Class

**เมื่อใดที่ควรใช้**: Large class ที่มีหลาย responsibility

**แรงจูงใจ**: แยก class เพื่อรักษา single responsibility

**กลไก**:
1. ตัดสินใจว่าจะแยก responsibility อย่างไร
2. สร้าง class ใหม่
3. ย้าย field จาก class เดิมไปยัง class ใหม่
4. ทดสอบ
5. ย้าย method จาก class เดิมไปยัง class ใหม่
6. ทดสอบหลังการย้ายแต่ละครั้ง
7. ตรวจสอบและตั้งชื่อ class ทั้งสองใหม่
8. ตัดสินใจว่าจะเปิดเผย class ใหม่อย่างไร

**ก่อน**:
```javascript
class Person {
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get officeAreaCode() { return this._officeAreaCode; }
  set officeAreaCode(arg) { this._officeAreaCode = arg; }
  get officeNumber() { return this._officeNumber; }
  set officeNumber(arg) { this._officeNumber = arg; }

  get telephoneNumber() {
    return `(${this._officeAreaCode}) ${this._officeNumber}`;
  }
}
```

**หลัง**:
```javascript
class Person {
  constructor() {
    this._telephoneNumber = new TelephoneNumber();
  }
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get telephoneNumber() { return this._telephoneNumber.toString(); }
  get officeAreaCode() { return this._telephoneNumber.areaCode; }
  set officeAreaCode(arg) { this._telephoneNumber.areaCode = arg; }
}

class TelephoneNumber {
  get areaCode() { return this._areaCode; }
  set areaCode(arg) { this._areaCode = arg; }
  get number() { return this._number; }
  set number(arg) { this._number = arg; }
  toString() { return `(${this._areaCode}) ${this._number}`; }
}
```

---

## Quick Reference: Smell กับ Refactoring

| Code Smell | Refactoring หลัก | ทางเลือก |
|------------|-------------------|-------------|
| Long Method | Extract Method | Replace Temp with Query |
| Duplicate Code | Extract Method | Pull Up Method |
| Large Class | Extract Class | Extract Subclass |
| Long Parameter List | Introduce Parameter Object | Preserve Whole Object |
| Feature Envy | Move Method | Extract Method + Move |
| Data Clumps | Extract Class | Introduce Parameter Object |
| Primitive Obsession | Replace Primitive with Object | Replace Type Code |
| Switch Statements | Replace Conditional with Polymorphism | Replace Type Code |
| Temporary Field | Extract Class | Introduce Null Object |
| Message Chains | Hide Delegate | Extract Method |
| Middle Man | Remove Middle Man | Inline Method |
| Divergent Change | Extract Class | Split Phase |
| Shotgun Surgery | Move Method | Inline Class |
| Dead Code | Remove Dead Code | — |
| Speculative Generality | Collapse Hierarchy | Inline Class |

---

## เอกสารอ่านเพิ่มเติม

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- Online catalog: https://refactoring.com/catalog/
