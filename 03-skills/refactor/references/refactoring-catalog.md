# 重構手法目錄

精選自 Martin Fowler《重構》（第二版）的重構技術目錄。每個重構手法包含動機、逐步操作步驟和範例。

> 「重構由其操作步驟定義 — 你執行變更時遵循的精確步驟序列。」 — Martin Fowler

---

## 如何使用此目錄

1. 使用程式碼壞味道參考**識別壞味道**
2. 在此目錄中**找到對應的重構手法**
3. **遵循操作步驟**逐步執行
4. **每步之後測試**以確保行為保持不變

**黃金法則**：如果任何步驟超過 10 分鐘，將其分解為更小的步驟。

---

## 最常見的重構手法

### 提取方法

**使用時機**：過長方法、重複程式碼、需要命名概念

**動機**：將程式碼片段轉化為方法，方法名稱解釋其目的。

**操作步驟**：
1. 建立新方法，以其功能命名（而非如何做）
2. 將程式碼片段複製到新方法
3. 掃描片段中使用的區域變數
4. 將區域變數作為參數傳入（或在方法中宣告）
5. 適當處理回傳值
6. 將原始片段替換為對新方法的呼叫
7. 測試

**重構前**：
```javascript
function printOwing(invoice) {
  let outstanding = 0;

  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");

  // Calculate outstanding
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // Print details
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

**重構後**：
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

### 內聯方法

**使用時機**：方法本體與其名稱一樣清楚、過多的委派

**動機**：當方法不增加價值時，移除不必要的間接層。

**操作步驟**：
1. 檢查方法不是多型的
2. 找到所有呼叫此方法的地方
3. 將每次呼叫替換為方法本體
4. 每次替換後測試
5. 移除方法定義

**重構前**：
```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**重構後**：
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### 提取變數

**使用時機**：複雜的表達式難以理解

**動機**：為複雜表達式的一部分命名。

**操作步驟**：
1. 確保表達式沒有副作用
2. 宣告一個不可變變數
3. 將其設定為表達式（或部分）的結果
4. 將原始表達式替換為變數
5. 測試

**重構前**：
```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**重構後**：
```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### 內聯變數

**使用時機**：變數名稱不比表達式更能傳達意義

**動機**：移除不必要的間接層。

**操作步驟**：
1. 檢查右側沒有副作用
2. 如果變數不是不可變的，使其不可變並測試
3. 找到第一個引用並替換為表達式
4. 測試
5. 對所有引用重複
6. 移除宣告和賦值
7. 測試

---

### 重新命名變數

**使用時機**：名稱沒有清楚傳達用途

**動機**：好的名稱對乾淨的程式碼至關重要。

**操作步驟**：
1. 如果變數被廣泛使用，考慮封裝
2. 找到所有引用
3. 變更每個引用
4. 測試

**提示**：
- 使用揭示意圖的名稱
- 避免縮寫
- 使用領域術語

```javascript
// Bad
const d = 30;
const x = users.filter(u => u.a);

// Good
const daysSinceLastLogin = 30;
const activeUsers = users.filter(user => user.isActive);
```

---

### 變更函式宣告

**使用時機**：函式名稱無法解釋用途、參數需要變更

**動機**：好的函式名稱使程式碼自我說明。

**操作步驟（簡單）**：
1. 移除不需要的參數
2. 變更名稱
3. 新增需要的參數
4. 測試

**操作步驟（遷移 - 用於複雜變更）**：
1. 如果移除參數，確保它未被使用
2. 建立具有所需宣告的新函式
3. 讓舊函式呼叫新函式
4. 測試
5. 變更呼叫者使用新函式
6. 每次之後測試
7. 移除舊函式

**重構前**：
```javascript
function circum(radius) {
  return 2 * Math.PI * radius;
}
```

**重構後**：
```javascript
function circumference(radius) {
  return 2 * Math.PI * radius;
}
```

---

### 封裝變數

**使用時機**：多處直接存取資料

**動機**：為資料操作提供清晰的存取點。

**操作步驟**：
1. 建立 getter 和 setter 函式
2. 找到所有引用
3. 將讀取替換為 getter
4. 將寫入替換為 setter
5. 每次變更後測試
6. 限制變數的可見性

**重構前**：
```javascript
let defaultOwner = { firstName: "Martin", lastName: "Fowler" };

// Used in many places
spaceship.owner = defaultOwner;
```

**重構後**：
```javascript
let defaultOwnerData = { firstName: "Martin", lastName: "Fowler" };

function defaultOwner() { return defaultOwnerData; }
function setDefaultOwner(arg) { defaultOwnerData = arg; }

spaceship.owner = defaultOwner();
```

---

### 引入參數物件

**使用時機**：多個經常一起出現的參數

**動機**：將自然屬於一起的資料分組。

**操作步驟**：
1. 為分組的參數建立新的類別/結構
2. 測試
3. 使用變更函式宣告新增新物件
4. 測試
5. 對於群組中的每個參數，從函式中移除並使用新物件
6. 每次之後測試

**重構前**：
```javascript
function amountInvoiced(startDate, endDate) { ... }
function amountReceived(startDate, endDate) { ... }
function amountOverdue(startDate, endDate) { ... }
```

**重構後**：
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

### 將函式組合成類別

**使用時機**：多個函式操作相同的資料

**動機**：將函式與其操作的資料分組。

**操作步驟**：
1. 對共同資料套用封裝記錄
2. 將每個函式搬移到類別中
3. 每次搬移後測試
4. 將資料引數替換為類別欄位的使用

**重構前**：
```javascript
function base(reading) { ... }
function taxableCharge(reading) { ... }
function calculateBaseCharge(reading) { ... }
```

**重構後**：
```javascript
class Reading {
  constructor(data) { this._data = data; }

  get base() { ... }
  get taxableCharge() { ... }
  get calculateBaseCharge() { ... }
}
```

---

### 拆分階段

**使用時機**：程式碼處理兩件不同的事情

**動機**：將程式碼分離成具有清晰邊界的不同階段。

**操作步驟**：
1. 為第二階段建立第二個函式
2. 測試
3. 在階段之間引入中間資料結構
4. 測試
5. 將第一階段提取到自己的函式
6. 測試

**重構前**：
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

**重構後**：
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

## 搬移功能

### 搬移方法

**使用時機**：方法使用另一個類別的功能多於自己的

**動機**：將函式與最常使用的資料放在一起。

**操作步驟**：
1. 檢查方法在其類別中使用的所有程式元素
2. 檢查方法是否是多型的
3. 將方法複製到目標類別
4. 針對新上下文調整
5. 讓原始方法委派給目標
6. 測試
7. 考慮移除原始方法

---

### 搬移欄位

**使用時機**：欄位被另一個類別更多地使用

**動機**：將資料與使用它的函式放在一起。

**操作步驟**：
1. 如果欄位尚未封裝，先封裝
2. 測試
3. 在目標中建立欄位
4. 更新引用以使用目標欄位
5. 測試
6. 移除原始欄位

---

### 將語句搬入函式

**使用時機**：相同的程式碼總是與函式呼叫一起出現

**動機**：透過將重複程式碼搬入函式來移除重複。

**操作步驟**：
1. 如果重複程式碼尚未被提取為函式，先提取
2. 將語句搬入該函式
3. 測試
4. 如果呼叫者不再需要獨立的語句，移除它們

---

### 將語句搬到呼叫者

**使用時機**：共同行為在呼叫者之間有差異

**動機**：當行為需要不同時，將其移出函式。

**操作步驟**：
1. 對要搬移的程式碼使用提取方法
2. 對原始函式使用內聯方法
3. 移除現在已內聯的呼叫
4. 將提取的程式碼搬到每個呼叫者
5. 測試

---

## 組織資料

### 以物件取代基本型別

**使用時機**：資料項目需要超出簡單值的行為

**動機**：將資料與其行為封裝在一起。

**操作步驟**：
1. 套用封裝變數
2. 建立簡單的值類別
3. 變更 setter 以建立新實例
4. 變更 getter 以回傳值
5. 測試
6. 為新類別新增更豐富的行為

**重構前**：
```javascript
class Order {
  constructor(data) {
    this.priority = data.priority; // string: "high", "rush", etc.
  }
}

// Usage
if (order.priority === "high" || order.priority === "rush") { ... }
```

**重構後**：
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

// Usage
if (order.priority.higherThan(new Priority("normal"))) { ... }
```

---

### 以查詢取代暫時變數

**使用時機**：暫時變數持有表達式的結果

**動機**：透過將表達式提取到函式使程式碼更清晰。

**操作步驟**：
1. 檢查變數只被賦值一次
2. 將賦值的右側提取到方法
3. 將對暫時變數的引用替換為方法呼叫
4. 測試
5. 移除暫時變數的宣告和賦值

**重構前**：
```javascript
const basePrice = this._quantity * this._itemPrice;
if (basePrice > 1000) {
  return basePrice * 0.95;
} else {
  return basePrice * 0.98;
}
```

**重構後**：
```javascript
get basePrice() {
  return this._quantity * this._itemPrice;
}

// In the method
if (this.basePrice > 1000) {
  return this.basePrice * 0.95;
} else {
  return this.basePrice * 0.98;
}
```

---

## 簡化條件邏輯

### 分解條件式

**使用時機**：複雜的條件（if-then-else）語句

**動機**：透過提取條件和動作使意圖清晰。

**操作步驟**：
1. 對條件套用提取方法
2. 對 then 分支套用提取方法
3. 對 else 分支套用提取方法（如果存在）

**重構前**：
```javascript
if (!aDate.isBefore(plan.summerStart) && !aDate.isAfter(plan.summerEnd)) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}
```

**重構後**：
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

### 合併條件表達式

**使用時機**：多個條件有相同的結果

**動機**：明確表達條件是單一檢查。

**操作步驟**：
1. 驗證條件中沒有副作用
2. 使用 `and` 或 `or` 合併條件
3. 考慮對合併的條件使用提取方法

**重構前**：
```javascript
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;
```

**重構後**：
```javascript
if (isNotEligibleForDisability(employee)) return 0;

function isNotEligibleForDisability(employee) {
  return employee.seniority < 2 ||
         employee.monthsDisabled > 12 ||
         employee.isPartTime;
}
```

---

### 以衛語句取代巢狀條件式

**使用時機**：深層巢狀的條件式使流程難以追蹤

**動機**：使用衛語句處理特殊案例，保持正常流程清晰。

**操作步驟**：
1. 找到特殊案例條件
2. 將它們替換為提前回傳的衛語句
3. 每次變更後測試

**重構前**：
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

**重構後**：
```javascript
function payAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reasonCode: "SEP" };
  if (employee.isRetired) return { amount: 0, reasonCode: "RET" };
  return calculateNormalPay(employee);
}
```

---

### 以多型取代條件式

**使用時機**：基於型別的 switch/case、依型別變化的條件邏輯

**動機**：讓物件處理自己的行為。

**操作步驟**：
1. 建立類別層級（如果不存在）
2. 使用工廠函式建立物件
3. 將條件邏輯搬到超類別方法
4. 為每個案例建立子類別方法
5. 移除原始條件式

**重構前**：
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

**重構後**：
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

### 引入特殊案例（Null 物件）

**使用時機**：重複的 null 檢查處理特殊案例

**動機**：回傳處理特殊案例的特殊物件。

**操作步驟**：
1. 建立具有預期介面的特殊案例類別
2. 新增 isSpecialCase 檢查
3. 引入工廠方法
4. 將 null 檢查替換為特殊案例物件的使用
5. 測試

**重構前**：
```javascript
const customer = site.customer;
// ... many places checking
if (customer === "unknown") {
  customerName = "occupant";
} else {
  customerName = customer.name;
}
```

**重構後**：
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

// Usage - no null checks needed
const customerName = customer.name;
```

---

## 重構 API

### 將查詢與修改分離

**使用時機**：函式同時回傳值並有副作用

**動機**：明確哪些操作有副作用。

**操作步驟**：
1. 建立新的查詢函式
2. 複製原始函式的回傳邏輯
3. 修改原始函式回傳 void
4. 替換使用回傳值的呼叫
5. 測試

**重構前**：
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

**重構後**：
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

### 參數化函式

**使用時機**：多個函式做類似的事情但使用不同的值

**動機**：透過新增參數來移除重複。

**操作步驟**：
1. 選擇一個函式
2. 為變化的字面值新增參數
3. 變更本體使用參數
4. 測試
5. 變更呼叫者使用參數化版本
6. 移除現在未使用的函式

**重構前**：
```javascript
function tenPercentRaise(person) {
  person.salary = person.salary * 1.10;
}

function fivePercentRaise(person) {
  person.salary = person.salary * 1.05;
}
```

**重構後**：
```javascript
function raise(person, factor) {
  person.salary = person.salary * (1 + factor);
}

// Usage
raise(person, 0.10);
raise(person, 0.05);
```

---

### 移除旗標引數

**使用時機**：布林參數改變函式行為

**動機**：透過分開的函式使行為明確。

**操作步驟**：
1. 為每個旗標值建立明確的函式
2. 將每次呼叫替換為適當的新函式
3. 每次變更後測試
4. 移除原始函式

**重構前**：
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

**重構後**：
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

## 處理繼承

### 提升方法

**使用時機**：多個子類別有相同的方法

**動機**：移除類別層級中的重複。

**操作步驟**：
1. 檢查方法確實相同
2. 檢查簽名一致
3. 在超類別中建立新方法
4. 從一個子類別複製本體
5. 刪除一個子類別方法，測試
6. 刪除其他子類別方法，每次測試

---

### 下推方法

**使用時機**：行為僅與部分子類別相關

**動機**：將方法放在使用它的地方。

**操作步驟**：
1. 將方法複製到每個需要它的子類別
2. 從超類別移除方法
3. 測試
4. 從不需要它的子類別移除
5. 測試

---

### 以委派取代子類別

**使用時機**：繼承使用不正確、需要更多靈活性

**動機**：在適當時偏好組合而非繼承。

**操作步驟**：
1. 為委派建立空類別
2. 在宿主類別中新增持有委派的欄位
3. 為委派建立建構函式，從宿主呼叫
4. 將功能搬到委派
5. 每次搬移後測試
6. 以委派取代繼承

---

## 提取類別

**使用時機**：大型類別有多個職責

**動機**：拆分類別以維護單一職責。

**操作步驟**：
1. 決定如何拆分職責
2. 建立新類別
3. 將欄位從原始類別搬到新類別
4. 測試
5. 將方法從原始類別搬到新類別
6. 每次搬移後測試
7. 審查並重新命名兩個類別
8. 決定如何公開新類別

**重構前**：
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

**重構後**：
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

## 快速參考：壞味道到重構手法

| 程式碼壞味道 | 主要重構手法 | 替代方案 |
|------------|-------------------|-------------|
| 過長方法 | 提取方法 | 以查詢取代暫時變數 |
| 重複程式碼 | 提取方法 | 提升方法 |
| 過大類別 | 提取類別 | 提取子類別 |
| 過長參數列 | 引入參數物件 | 保持整體物件 |
| 依戀情結 | 搬移方法 | 提取方法 + 搬移 |
| 資料泥團 | 提取類別 | 引入參數物件 |
| 基本型別偏執 | 以物件取代基本型別 | 以類別取代型別代碼 |
| Switch 語句 | 以多型取代條件式 | 以類別取代型別代碼 |
| 暫時欄位 | 提取類別 | 引入 Null 物件 |
| 訊息鏈 | 隱藏委派 | 提取方法 |
| 中間人 | 移除中間人 | 內聯方法 |
| 發散式變更 | 提取類別 | 拆分階段 |
| 散彈式修改 | 搬移方法 | 內聯類別 |
| 死碼 | 移除死碼 | - |
| 投機性通用化 | 摺疊層級 | 內聯類別 |

---

## 延伸閱讀

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- 線上目錄：https://refactoring.com/catalog/
