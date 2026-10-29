# کاتالوگ ری‌فاکتور

کاتالوگی گزیده از تکنیک‌های ری‌فاکتور بر اساس کتاب *Refactoring* (ویرایش دوم) مارتین فاولر. هر ری‌فاکتور شامل انگیزه، مکانیک گام‌به‌گام و مثال است.

> «یک ری‌فاکتور با مکانیک خود تعریف می‌شود — همان توالی دقیق گام‌هایی که برای انجام تغییر دنبال می‌کنید.» — مارتین فاولر

---

## نحوه استفاده از این کاتالوگ

1. **بوی کد را شناسایی کنید** با استفاده از مرجع بوی کد
2. **ری‌فاکتور مطابق را پیدا کنید** در این کاتالوگ
3. **مکانیک را گام‌به‌گام دنبال کنید**
4. **پس از هر گام تست کنید** تا رفتار حفظ شود

**قاعده طلایی**: اگر هر گامی بیش از ۱۰ دقیقه طول می‌کشد، آن را به گام‌های کوچک‌تر بشکنید.

---

## رایج‌ترین ری‌فاکتورها

### استخراج متد (Extract Method)

**زمان استفاده**: متد طولانی، کد تکراری، نیاز به نام‌گذاری یک مفهوم

**انگیزه**: یک قطعه کد را به متدی تبدیل کنید که نامش هدف را توضیح می‌دهد.

**مکانیک**:
1. متدی جدید بسازید که بر اساس کاری که انجام می‌دهد نام‌گذاری شده باشد (نه نحوه انجام)
2. قطعه کد را به متد جدید کپی کنید
3. متغیرهای محلی استفاده‌شده در قطعه را بررسی کنید
4. متغیرهای محلی را به‌عنوان پارامتر منتقل کنید (یا در متد اعلان کنید)
5. مقادیر بازگشتی را به‌درستی مدیریت کنید
6. قطعه اصلی را با فراخوانی متد جدید جایگزین کنید
7. تست کنید

**قبل**:
```javascript
function printOwing(invoice) {
  let outstanding = 0;

  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");

  // محاسبه بدهی
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // چاپ جزئیات
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

**بعد**:
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

### درون‌خطی کردن متد (Inline Method)

**زمان استفاده**: بدنه متد به‌اندازه نامش شفاف است، واگذاری بیش از حد

**انگیزه**: حذف غیرمستقیم‌سازی غیرضروری وقتی متد ارزشی اضافه نمی‌کند.

**مکانیک**:
1. بررسی کنید که متد چندریختی نباشد
2. همه فراخوانی‌های متد را پیدا کنید
3. هر فراخوانی را با بدنه متد جایگزین کنید
4. پس از هر جایگزینی تست کنید
5. تعریف متد را حذف کنید

**قبل**:
```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**بعد**:
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### استخراج متغیر (Extract Variable)

**زمان استفاده**: عبارت پیچیده‌ای که درک آن دشوار است

**انگیزه**: به بخشی از یک عبارت پیچیده نام بدهید.

**مکانیک**:
1. مطمئن شوید عبارت عوارض جانبی ندارد
2. یک متغیر تغییرناپذیر اعلان کنید
3. آن را به نتیجه عبارت (یا بخشی از آن) مقداردهی کنید
4. عبارت اصلی را با متغیر جایگزین کنید
5. تست کنید

**قبل**:
```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**بعد**:
```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### درون‌خطی کردن متغیر (Inline Variable)

**زمان استفاده**: نام متغیر بیش از خود عبارت چیزی را منتقل نمی‌کند

**انگیزه**: حذف غیرمستقیم‌سازی غیرضروری.

**مکانیک**:
1. بررسی کنید سمت راست عبارت عوارض جانبی ندارد
2. اگر متغیر تغییرناپذیر نیست، آن را تغییرناپذیر کنید و تست کنید
3. نخستین ارجاع را پیدا کنید و با عبارت جایگزین کنید
4. تست کنید
5. برای همه ارجاع‌ها تکرار کنید
6. اعلان و مقداردهی را حذف کنید
7. تست کنید

---

### تغییر نام متغیر (Rename Variable)

**زمان استفاده**: نام به‌روشنی هدف را منتقل نمی‌کند

**انگیزه**: نام‌های خوب برای کد تمیز حیاتی هستند.

**مکانیک**:
1. اگر متغیر به‌طور گسترده استفاده می‌شود، کپسوله‌سازی را در نظر بگیرید
2. همه ارجاع‌ها را پیدا کنید
3. هر ارجاع را تغییر دهید
4. تست کنید

**نکات**:
- از نام‌هایی که نیت را آشکار می‌کنند استفاده کنید
- از اختصارات پرهیز کنید
- از اصطلاحات دامنه استفاده کنید

```javascript
// بد
const d = 30;
const x = users.filter(u => u.a);

// خوب
const daysSinceLastLogin = 30;
const activeUsers = users.filter(user => user.isActive);
```

---

### تغییر اعلان تابع (Change Function Declaration)

**زمان استفاده**: نام تابع هدف را توضیح نمی‌دهد، پارامترها باید تغییر کنند

**انگیزه**: نام‌های خوب تابع، کد را خودمستند می‌کنند.

**مکانیک (ساده)**:
1. پارامترهای غیرلازم را حذف کنید
2. نام را تغییر دهید
3. پارامترهای لازم را اضافه کنید
4. تست کنید

**مکانیک (مهاجرت - برای تغییرات پیچیده)**:
1. اگر پارامتری حذف می‌کنید، مطمئن شوید استفاده نمی‌شود
2. تابع جدید با اعلان مورد نظر بسازید
3. تابع قدیمی تابع جدید را فراخوانی کند
4. تست کنید
5. فراخوانی‌کنندگان را به تابع جدید تغییر دهید
6. پس از هر مورد تست کنید
7. تابع قدیمی را حذف کنید

**قبل**:
```javascript
function circum(radius) {
  return 2 * Math.PI * radius;
}
```

**بعد**:
```javascript
function circumference(radius) {
  return 2 * Math.PI * radius;
}
```

---

### کپسوله‌سازی متغیر (Encapsulate Variable)

**زمان استفاده**: دسترسی مستقیم به داده از چند جا

**انگیزه**: نقطه دسترسی شفافی برای دستکاری داده فراهم کنید.

**مکانیک**:
1. توابع getter و setter بسازید
2. همه ارجاع‌ها را پیدا کنید
3. خواندن‌ها را با getter جایگزین کنید
4. نوشتن‌ها را با setter جایگزین کنید
5. پس از هر تغییر تست کنید
6. دیدپذیری متغیر را محدود کنید

**قبل**:
```javascript
let defaultOwner = { firstName: "Martin", lastName: "Fowler" };

// در جاهای زیادی استفاده می‌شود
spaceship.owner = defaultOwner;
```

**بعد**:
```javascript
let defaultOwnerData = { firstName: "Martin", lastName: "Fowler" };

function defaultOwner() { return defaultOwnerData; }
function setDefaultOwner(arg) { defaultOwnerData = arg; }

spaceship.owner = defaultOwner();
```

---

### معرفی شیء پارامتر (Introduce Parameter Object)

**زمان استفاده**: چند پارامتر که مکرراً با هم می‌آیند

**انگیزه**: داده‌هایی که به‌طور طبیعی به هم تعلق دارند را گروه‌بندی کنید.

**مکانیک**:
1. یک کلاس/ساختار جدید برای پارامترهای گروه‌بندی‌شده بسازید
2. تست کنید
3. از تغییر اعلان تابع برای افزودن شیء جدید استفاده کنید
4. تست کنید
5. برای هر پارامتر در گروه، آن را از تابع حذف کنید و از شیء جدید استفاده کنید
6. پس از هر مورد تست کنید

**قبل**:
```javascript
function amountInvoiced(startDate, endDate) { ... }
function amountReceived(startDate, endDate) { ... }
function amountOverdue(startDate, endDate) { ... }
```

**بعد**:
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

### ترکیب توابع در کلاس (Combine Functions into Class)

**زمان استفاده**: چند تابع روی داده یکسان کار می‌کنند

**انگیزه**: توابع را با داده‌ای که روی آن کار می‌کنند گروه‌بندی کنید.

**مکانیک**:
1. کپسوله‌سازی رکورد را روی داده مشترک اعمال کنید
2. هر تابع را به کلاس منتقل کنید
3. پس از هر انتقال تست کنید
4. آرگومان‌های داده را با استفاده از فیلدهای کلاس جایگزین کنید

**قبل**:
```javascript
function base(reading) { ... }
function taxableCharge(reading) { ... }
function calculateBaseCharge(reading) { ... }
```

**بعد**:
```javascript
class Reading {
  constructor(data) { this._data = data; }

  get base() { ... }
  get taxableCharge() { ... }
  get calculateBaseCharge() { ... }
}
```

---

### تقسیم فاز (Split Phase)

**زمان استفاده**: کد با دو چیز متفاوت سروکار دارد

**انگیزه**: کد را به فازهای مجزا با مرزهای شفاف تقسیم کنید.

**مکانیک**:
1. یک تابع دوم برای فاز دوم بسازید
2. تست کنید
3. یک ساختار داده میانی بین فازها معرفی کنید
4. تست کنید
5. فاز اول را به تابع خودش استخراج کنید
6. تست کنید

**قبل**:
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

**بعد**:
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

## جابه‌جایی قابلیت‌ها

### انتقال متد (Move Method)

**زمان استفاده**: متد بیشتر از قابلیت‌های کلاس دیگر استفاده می‌کند تا کلاس خودش

**انگیزه**: توابع را با داده‌ای که بیشتر استفاده می‌کنند قرار دهید.

**مکانیک**:
1. همه عناصر برنامه که متد در کلاس خودش استفاده می‌کند را بررسی کنید
2. بررسی کنید متد چندریختی نباشد
3. متد را به کلاس هدف کپی کنید
4. برای زمینه جدید تنظیم کنید
5. متد اصلی را وادار کنید به هدف واگذار کند
6. تست کنید
7. حذف متد اصلی را در نظر بگیرید

---

### انتقال فیلد (Move Field)

**زمان استفاده**: فیلد بیشتر توسط کلاس دیگری استفاده می‌شود

**انگیزه**: داده را با توابعی که از آن استفاده می‌کنند نگه دارید.

**مکانیک**:
1. اگر فیلد کپسوله نشده، آن را کپسوله کنید
2. تست کنید
3. فیلد را در هدف بسازید
4. ارجاع‌ها را برای استفاده از فیلد هدف به‌روزرسانی کنید
5. تست کنید
6. فیلد اصلی را حذف کنید

---

### انتقال دستورات به تابع (Move Statements into Function)

**زمان استفاده**: همان کد همیشه همراه با فراخوانی یک تابع ظاهر می‌شود

**انگیزه**: با انتقال کد تکراری به تابع، تکرار را حذف کنید.

**مکانیک**:
1. کد تکراری را در تابعی استخراج کنید اگر قبلاً این‌طور نیست
2. دستورات را به آن تابع منتقل کنید
3. تست کنید
4. اگر فراخوانی‌کنندگان دیگر به دستورات مستقل نیاز ندارند، آن‌ها را حذف کنید

---

### انتقال دستورات به فراخوانی‌کنندگان (Move Statements to Callers)

**زمان استفاده**: رفتار مشترک بین فراخوانی‌کنندگان متفاوت است

**انگیزه**: وقتی رفتار باید متفاوت باشد، آن را از تابع بیرون ببرید.

**مکانیک**:
1. استخراج متد را روی کدی که باید منتقل شود اعمال کنید
2. درون‌خطی کردن متد را روی تابع اصلی اعمال کنید
3. فراخوانی درون‌خطی‌شده را حذف کنید
4. کد استخراج‌شده را به هر فراخوانی‌کننده منتقل کنید
5. تست کنید

---

## سازمان‌دهی داده

### جایگزینی نوع ابتدایی با شیء (Replace Primitive with Object)

**زمان استفاده**: آیتم داده به رفتار بیشتری از یک مقدار ساده نیاز دارد

**انگیزه**: داده را همراه با رفتارش کپسوله کنید.

**مکانیک**:
1. کپسوله‌سازی متغیر را اعمال کنید
2. یک کلاس مقدار ساده بسازید
3. setter را تغییر دهید تا نمونه جدید بسازد
4. getter را تغییر دهید تا مقدار را برگرداند
5. تست کنید
6. رفتار غنی‌تر به کلاس جدید اضافه کنید

**قبل**:
```javascript
class Order {
  constructor(data) {
    this.priority = data.priority; // رشته: "high"، "rush" و غیره
  }
}

// استفاده
if (order.priority === "high" || order.priority === "rush") { ... }
```

**بعد**:
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

// استفاده
if (order.priority.higherThan(new Priority("normal"))) { ... }
```

---

### جایگزینی متغیر موقت با پرس‌وجو (Replace Temp with Query)

**زمان استفاده**: متغیر موقت نتیجه یک عبارت را نگه می‌دارد

**انگیزه**: با استخراج عبارت در یک تابع، کد را شفاف‌تر کنید.

**مکانیک**:
1. بررسی کنید متغیر فقط یک بار مقدار می‌گیرد
2. سمت راست مقداردهی را در متدی استخراج کنید
3. ارجاع‌ها به متغیر موقت را با فراخوانی متد جایگزین کنید
4. تست کنید
5. اعلان و مقداردهی متغیر موقت را حذف کنید

**قبل**:
```javascript
const basePrice = this._quantity * this._itemPrice;
if (basePrice > 1000) {
  return basePrice * 0.95;
} else {
  return basePrice * 0.98;
}
```

**بعد**:
```javascript
get basePrice() {
  return this._quantity * this._itemPrice;
}

// در متد
if (this.basePrice > 1000) {
  return this.basePrice * 0.95;
} else {
  return this.basePrice * 0.98;
}
```

---

## ساده‌سازی منطق شرطی

### تجزیه شرطی (Decompose Conditional)

**زمان استفاده**: دستور شرطی پیچیده (if-then-else)

**انگیزه**: با استخراج شرط‌ها و اقدام‌ها، نیت را شفاف کنید.

**مکانیک**:
1. استخراج متد را روی شرط اعمال کنید
2. استخراج متد را روی شاخه then اعمال کنید
3. استخراج متد را روی شاخه else (در صورت وجود) اعمال کنید

**قبل**:
```javascript
if (!aDate.isBefore(plan.summerStart) && !aDate.isAfter(plan.summerEnd)) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}
```

**بعد**:
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

### یکپارچه‌سازی عبارت شرطی (Consolidate Conditional Expression)

**زمان استفاده**: چند شرط با نتیجه یکسان

**انگیزه**: شفاف کنید که شرط‌ها یک بررسی واحد هستند.

**مکانیک**:
1. بررسی کنید شرط‌ها عوارض جانبی ندارند
2. شرط‌ها را با `and` یا `or` ترکیب کنید
3. استخراج متد را روی شرط ترکیبی در نظر بگیرید

**قبل**:
```javascript
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;
```

**بعد**:
```javascript
if (isNotEligibleForDisability(employee)) return 0;

function isNotEligibleForDisability(employee) {
  return employee.seniority < 2 ||
         employee.monthsDisabled > 12 ||
         employee.isPartTime;
}
```

---

### جایگزینی شرطی تودرتو با بندهای محافظ (Replace Nested Conditional with Guard Clauses)

**زمان استفاده**: شرط‌های عمیقاً تودرتو که جریان را دشوار می‌کنند

**انگیزه**: برای موارد خاص از بندهای محافظ استفاده کنید تا جریان عادی شفاف بماند.

**مکانیک**:
1. شرط‌های مورد خاص را پیدا کنید
2. آن‌ها را با بندهای محافظی که زود بازمی‌گردند جایگزین کنید
3. پس از هر تغییر تست کنید

**قبل**:
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

**بعد**:
```javascript
function payAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reasonCode: "SEP" };
  if (employee.isRetired) return { amount: 0, reasonCode: "RET" };
  return calculateNormalPay(employee);
}
```

---

### جایگزینی شرطی با چندریختی (Replace Conditional with Polymorphism)

**زمان استفاده**: switch/case بر اساس نوع، منطق شرطی که با نوع تغییر می‌کند

**انگیزه**: بگذارید اشیاء رفتار خودشان را مدیریت کنند.

**مکانیک**:
1. سلسله‌مراتب کلاس بسازید (اگر وجود ندارد)
2. برای ساخت شیء از تابع کارخانه استفاده کنید
3. منطق شرطی را به متد ابرکلاس منتقل کنید
4. برای هر حالت متد زیرکلاس بسازید
5. شرطی اصلی را حذف کنید

**قبل**:
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

**بعد**:
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

### معرفی مورد خاص / شیء null (Introduce Special Case)

**زمان استفاده**: بررسی‌های مکرر null برای موارد خاص

**انگیزه**: شیء خاصی برگردانید که مورد خاص را مدیریت می‌کند.

**مکانیک**:
1. کلاس مورد خاص با رابط مورد انتظار بسازید
2. بررسی isSpecialCase را اضافه کنید
3. متد کارخانه معرفی کنید
4. بررسی‌های null را با استفاده از شیء مورد خاص جایگزین کنید
5. تست کنید

**قبل**:
```javascript
const customer = site.customer;
// ... جاهای زیادی بررسی می‌کنند
if (customer === "unknown") {
  customerName = "occupant";
} else {
  customerName = customer.name;
}
```

**بعد**:
```javascript
class UnknownCustomer {
  get name() { return "occupant"; }
  get billingPlan() { return registry.defaultPlan; }
}

// متد کارخانه
function customer(site) {
  return site.customer === "unknown"
    ? new UnknownCustomer()
    : site.customer;
}

// استفاده - نیازی به بررسی null نیست
const customerName = customer.name;
```

---

## ری‌فاکتور APIها

### جداسازی پرس‌وجو از تغییردهنده (Separate Query from Modifier)

**زمان استفاده**: تابع هم مقدار برمی‌گرداند و هم عوارض جانبی دارد

**انگیزه**: شفاف کنید کدام عملیات عوارض جانبی دارند.

**مکانیک**:
1. یک تابع پرس‌وجوی جدید بسازید
2. منطق بازگشتی تابع اصلی را کپی کنید
3. تابع اصلی را تغییر دهید تا void برگرداند
4. فراخوانی‌هایی که از مقدار بازگشتی استفاده می‌کنند را جایگزین کنید
5. تست کنید

**قبل**:
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

**بعد**:
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

### پارامتری کردن تابع (Parameterize Function)

**زمان استفاده**: چند تابع که کارهای مشابه با مقادیر متفاوت انجام می‌دهند

**انگیزه**: با افزودن یک پارامتر، تکرار را حذف کنید.

**مکانیک**:
1. یک تابع انتخاب کنید
2. برای مقدار متغیر، پارامتر اضافه کنید
3. بدنه را تغییر دهید تا از پارامتر استفاده کند
4. تست کنید
5. فراخوانی‌کنندگان را به نسخه پارامتری تغییر دهید
6. توابع استفاده‌نشده را حذف کنید

**قبل**:
```javascript
function tenPercentRaise(person) {
  person.salary = person.salary * 1.10;
}

function fivePercentRaise(person) {
  person.salary = person.salary * 1.05;
}
```

**بعد**:
```javascript
function raise(person, factor) {
  person.salary = person.salary * (1 + factor);
}

// استفاده
raise(person, 0.10);
raise(person, 0.05);
```

---

### حذف آرگومان پرچم (Remove Flag Argument)

**زمان استفاده**: پارامتر بولی که رفتار تابع را تغییر می‌دهد

**انگیزه**: رفتار را از طریق توابع مجزا صریح کنید.

**مکانیک**:
1. برای هر مقدار پرچم تابع صریح بسازید
2. هر فراخوانی را با تابع جدید مناسب جایگزین کنید
3. پس از هر تغییر تست کنید
4. تابع اصلی را حذف کنید

**قبل**:
```javascript
function bookConcert(customer, isPremium) {
  if (isPremium) {
    // منطق رزرو ویژه
  } else {
    // منطق رزرو عادی
  }
}

bookConcert(customer, true);
bookConcert(customer, false);
```

**بعد**:
```javascript
function bookPremiumConcert(customer) {
  // منطق رزرو ویژه
}

function bookRegularConcert(customer) {
  // منطق رزرو عادی
}

bookPremiumConcert(customer);
bookRegularConcert(customer);
```

---

## کار با ارث‌بری

### کشیدن متد به بالا (Pull Up Method)

**زمان استفاده**: متد یکسان در چند زیرکلاس

**انگیزه**: حذف تکرار در سلسله‌مراتب کلاس.

**مکانیک**:
1. متدها را بررسی کنید تا مطمئن شوید یکسان‌اند
2. بررسی کنید امضاها یکسان‌اند
3. متد جدید در ابرکلاس بسازید
4. بدنه را از یک زیرکلاس کپی کنید
5. متد یک زیرکلاس را حذف کنید، تست کنید
6. متدهای زیرکلاس‌های دیگر را حذف کنید، هر یک را تست کنید

---

### هل دادن متد به پایین (Push Down Method)

**زمان استفاده**: رفتاری که فقط به زیرمجموعه‌ای از زیرکلاس‌ها مربوط است

**انگیزه**: متد را جایی بگذارید که استفاده می‌شود.

**مکانیک**:
1. متد را به هر زیرکلاسی که به آن نیاز دارد کپی کنید
2. متد را از ابرکلاس حذف کنید
3. تست کنید
4. از زیرکلاس‌هایی که نیاز ندارند حذف کنید
5. تست کنید

---

### جایگزینی زیرکلاس با واگذاری (Replace Subclass with Delegate)

**زمان استفاده**: ارث‌بری نادرست استفاده می‌شود، نیاز به انعطاف بیشتر

**انگیزه**: در جای مناسب، ترکیب را به ارث‌بری ترجیح دهید.

**مکانیک**:
1. کلاس خالی برای واگذار بسازید
2. فیلدی به کلاس میزبان اضافه کنید که واگذار را نگه دارد
3. سازنده‌ای برای واگذار بسازید که از میزبان فراخوانی شود
4. قابلیت‌ها را به واگذار منتقل کنید
5. پس از هر انتقال تست کنید
6. ارث‌بری را با واگذاری جایگزین کنید

---

## استخراج کلاس (Extract Class)

**زمان استفاده**: کلاس بزرگ با چند مسئولیت

**انگیزه**: کلاس را برای حفظ مسئولیت واحد تقسیم کنید.

**مکانیک**:
1. تصمیم بگیرید مسئولیت‌ها را چگونه تقسیم کنید
2. کلاس جدید بسازید
3. فیلد را از کلاس اصلی به کلاس جدید منتقل کنید
4. تست کنید
5. متدها را از کلاس اصلی به کلاس جدید منتقل کنید
6. پس از هر انتقال تست کنید
7. هر دو کلاس را بازبینی و تغییر نام دهید
8. تصمیم بگیرید کلاس جدید چگونه افشا شود

**قبل**:
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

**بعد**:
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

## مرجع سریع: از بوی کد تا ری‌فاکتور

| بوی کد | ری‌فاکتور اصلی | جایگزین |
|------------|-------------------|-------------|
| متد طولانی | استخراج متد | جایگزینی متغیر موقت با پرس‌وجو |
| کد تکراری | استخراج متد | کشیدن متد به بالا |
| کلاس بزرگ | استخراج کلاس | استخراج زیرکلاس |
| فهرست پارامتر طولانی | معرفی شیء پارامتر | حفظ شیء کامل |
| حسادت به ویژگی | انتقال متد | استخراج متد + انتقال |
| خوشه‌های داده | استخراج کلاس | معرفی شیء پارامتر |
| وسواس به انواع ابتدایی | جایگزینی نوع ابتدایی با شیء | جایگزینی کد نوع |
| دستورات switch | جایگزینی شرطی با چندریختی | جایگزینی کد نوع |
| فیلد موقت | استخراج کلاس | معرفی شیء null |
| زنجیره‌های پیام | پنهان‌سازی واگذار | استخراج متد |
| واسطه | حذف واسطه | درون‌خطی کردن متد |
| تغییر واگرا | استخراج کلاس | تقسیم فاز |
| جراحی با شاتگان | انتقال متد | درون‌خطی کردن کلاس |
| کد مرده | حذف کد مرده | - |
| کلیت حدسی | فروپاشی سلسله‌مراتب | درون‌خطی کردن کلاس |

---

## مطالعه بیشتر

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- کاتالوگ آنلاین: https://refactoring.com/catalog/

---

**آخرین به‌روزرسانی**: ۴ اوت ۲۰۲۶
**نسخه Claude Code**: 2.1.220
**منابع**:
- https://code.claude.com/docs/en/skills
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
