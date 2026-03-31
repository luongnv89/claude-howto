# 重构目录

来自 Martin Fowler 的《*重构*》（第2版）的精选重构技术目录。每种重构包括动机、逐步机制和示例。

> "重构由其机制定义——您按照的精确步骤序列来执行变更。" — Martin Fowler

---

## 如何使用本目录

1. **使用代码异味参考识别异味**
2. **在本目录中找到匹配的重构**
3. **逐步遵循机制**
4. **每步后进行测试**以确保行为得以保留

**黄金法则**：如果任何步骤需要超过 10 分钟，将其分解成更小的步骤。

---

## 最常见的重构

### 提取方法

**使用时机**：长方法、重复代码、需要命名一个概念

**动机**：将代码片段转换为一个方法，其名称解释目的。

**机制**：
1. 创建一个以其功能命名的新方法（而非如何实现）
2. 将代码片段复制到新方法中
3. 扫描片段中使用的局部变量
4. 将局部变量作为参数传递（或在方法中声明）
5. 适当处理返回值
6. 用对新方法的调用替换原始片段
7. 测试

**重构前：**
```javascript
function printOwing(invoice) {
  let outstanding = 0;

  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");

  // 计算欠款
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // 打印详情
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

**重构后：**
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

### 内联方法

**使用时机**：方法体与其名称一样清晰，过度委托

**动机**：当方法不增加价值时，移除不必要的间接性。

**机制**：
1. 检查方法不是多态的
2. 找到所有对方法的调用
3. 用方法体替换每个调用
4. 每次替换后测试
5. 删除方法定义

**重构前：**
```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**重构后：**
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### 提取变量

**使用时机**：难以理解的复杂表达式

**动机**：给复杂表达式的一部分命名。

**机制**：
1. 确保表达式没有副作用
2. 声明一个不可变变量
3. 将其设置为表达式（或部分）的结果
4. 用变量替换原始表达式
5. 测试

**重构前：**
```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**重构后：**
```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### 内联变量

**使用时机**：变量名传递的信息不比表达式多

**动机**：移除不必要的间接性。

**机制**：
1. 检查右侧没有副作用
2. 如果变量不是不可变的，使其不可变并测试
3. 找到第一个引用并用表达式替换
4. 测试
5. 对所有引用重复
6. 删除声明和赋值
7. 测试

---

### 重命名变量

**使用时机**：名称没有清晰地传达目的

**动机**：好的名称对于干净的代码至关重要。

**机制**：
1. 如果变量被广泛使用，考虑封装
2. 找到所有引用
3. 更改每个引用
4. 测试

**提示**：
- 使用表达意图的名称
- 避免缩写
- 使用领域术语

```javascript
// 坏
const d = 30;
const x = users.filter(u => u.a);

// 好
const daysSinceLastLogin = 30;
const activeUsers = users.filter(user => user.isActive);
```

---

### 改变函数声明

**使用时机**：函数名没有解释目的，参数需要变更

**动机**：好的函数名使代码自文档化。

**机制（简单）：**
1. 删除不需要的参数
2. 更改名称
3. 添加需要的参数
4. 测试

**机制（迁移——用于复杂变更）：**
1. 如果删除参数，确保它未被使用
2. 创建具有所需声明的新函数
3. 让旧函数调用新函数
4. 测试
5. 更改调用者使用新函数
6. 每次后测试
7. 删除旧函数

**重构前：**
```javascript
function circum(radius) {
  return 2 * Math.PI * radius;
}
```

**重构后：**
```javascript
function circumference(radius) {
  return 2 * Math.PI * radius;
}
```

---

### 封装变量

**使用时机**：来自多个地方的直接数据访问

**动机**：为数据操作提供清晰的访问点。

**机制**：
1. 创建 getter 和 setter 函数
2. 找到所有引用
3. 用 getter 替换读取
4. 用 setter 替换写入
5. 每次变更后测试
6. 限制变量的可见性

**重构前：**
```javascript
let defaultOwner = { firstName: "Martin", lastName: "Fowler" };

// 在许多地方使用
spaceship.owner = defaultOwner;
```

**重构后：**
```javascript
let defaultOwnerData = { firstName: "Martin", lastName: "Fowler" };

function defaultOwner() { return defaultOwnerData; }
function setDefaultOwner(arg) { defaultOwnerData = arg; }

spaceship.owner = defaultOwner();
```

---

### 引入参数对象

**使用时机**：几个经常一起出现的参数

**动机**：将自然属于一起的数据分组。

**机制**：
1. 为分组参数创建新的类/结构
2. 测试
3. 使用改变函数声明来添加新对象
4. 测试
5. 对于组中的每个参数，将其从函数中删除并使用新对象
6. 每次后测试

**重构前：**
```javascript
function amountInvoiced(startDate, endDate) { ... }
function amountReceived(startDate, endDate) { ... }
function amountOverdue(startDate, endDate) { ... }
```

**重构后：**
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

### 将函数组合成类

**使用时机**：几个函数对相同数据进行操作

**动机**：将函数与它们操作的数据分组。

**机制**：
1. 对公共数据应用封装记录
2. 将每个函数移入类中
3. 每次移动后测试
4. 用类字段使用替换数据参数

**重构前：**
```javascript
function base(reading) { ... }
function taxableCharge(reading) { ... }
function calculateBaseCharge(reading) { ... }
```

**重构后：**
```javascript
class Reading {
  constructor(data) { this._data = data; }

  get base() { ... }
  get taxableCharge() { ... }
  get calculateBaseCharge() { ... }
}
```

---

### 拆分阶段

**使用时机**：代码处理两件不同的事情

**动机**：将代码分离成具有清晰边界的不同阶段。

**机制**：
1. 为第二阶段创建第二个函数
2. 测试
3. 在阶段之间引入中间数据结构
4. 测试
5. 将第一阶段提取到其自己的函数中
6. 测试

**重构前：**
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

**重构后：**
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

## 移动功能

### 移动方法

**使用时机**：方法使用另一个类的功能多于自身

**动机**：将函数放在它们最多使用的数据旁边。

**机制**：
1. 检查方法在其类中使用的所有程序元素
2. 检查方法是否为多态的
3. 将方法复制到目标类
4. 针对新上下文进行调整
5. 使原始方法委托给目标
6. 测试
7. 考虑删除原始方法

---

### 移动字段

**使用时机**：字段被另一个类更多地使用

**动机**：将数据与使用它的函数保持在一起。

**机制**：
1. 如果字段尚未封装，则封装它
2. 测试
3. 在目标中创建字段
4. 更新引用以使用目标字段
5. 测试
6. 删除原始字段

---

### 将语句移入函数

**使用时机**：相同代码总是与函数调用一起出现

**动机**：通过将重复代码移入函数来消除重复。

**机制**：
1. 如果重复代码尚未成为函数，则提取它
2. 将语句移入该函数
3. 测试
4. 如果调用者不再需要独立语句，则删除它们

---

### 将语句移至调用者

**使用时机**：公共行为在调用者之间有所不同

**动机**：当行为需要不同时，将其移出函数。

**机制**：
1. 对要移动的代码使用提取方法
2. 对原始函数使用内联方法
3. 删除现在已内联的调用
4. 将提取的代码移至每个调用者
5. 测试

---

## 组织数据

### 以对象替代基本类型

**使用时机**：数据项需要比简单值更多的行为

**动机**：用其行为封装数据。

**机制**：
1. 应用封装变量
2. 创建简单的值类
3. 更改 setter 以创建新实例
4. 更改 getter 以返回值
5. 测试
6. 为新类添加更丰富的行为

**重构前：**
```javascript
class Order {
  constructor(data) {
    this.priority = data.priority; // 字符串："high"、"rush" 等
  }
}

// 使用
if (order.priority === "high" || order.priority === "rush") { ... }
```

**重构后：**
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

// 使用
if (order.priority.higherThan(new Priority("normal"))) { ... }
```

---

### 以查询替代临时变量

**使用时机**：临时变量保存表达式的结果

**动机**：通过将表达式提取到函数中使代码更清晰。

**机制**：
1. 检查变量只被赋值一次
2. 将赋值的右侧提取到方法中
3. 用方法调用替换对临时变量的引用
4. 测试
5. 删除临时变量声明和赋值

**重构前：**
```javascript
const basePrice = this._quantity * this._itemPrice;
if (basePrice > 1000) {
  return basePrice * 0.95;
} else {
  return basePrice * 0.98;
}
```

**重构后：**
```javascript
get basePrice() {
  return this._quantity * this._itemPrice;
}

// 在方法中
if (this.basePrice > 1000) {
  return this.basePrice * 0.95;
} else {
  return this.basePrice * 0.98;
}
```

---

## 简化条件逻辑

### 分解条件表达式

**使用时机**：复杂的条件（if-then-else）语句

**动机**：通过提取条件和动作使意图清晰。

**机制**：
1. 对条件应用提取方法
2. 对 then 分支应用提取方法
3. 对 else 分支应用提取方法（如果存在）

**重构前：**
```javascript
if (!aDate.isBefore(plan.summerStart) && !aDate.isAfter(plan.summerEnd)) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}
```

**重构后：**
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

### 合并条件表达式

**使用时机**：多个具有相同结果的条件

**动机**：清楚地表明条件是单个检查。

**机制**：
1. 验证条件中没有副作用
2. 使用 `and` 或 `or` 合并条件
3. 考虑对组合条件使用提取方法

**重构前：**
```javascript
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;
```

**重构后：**
```javascript
if (isNotEligibleForDisability(employee)) return 0;

function isNotEligibleForDisability(employee) {
  return employee.seniority < 2 ||
         employee.monthsDisabled > 12 ||
         employee.isPartTime;
}
```

---

### 以卫语句替换嵌套条件表达式

**使用时机**：深度嵌套的条件使流程难以跟踪

**动机**：对特殊情况使用卫语句，保持正常流程清晰。

**机制**：
1. 找到特殊情况条件
2. 用提前返回的卫语句替换它们
3. 每次变更后测试

**重构前：**
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

**重构后：**
```javascript
function payAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reasonCode: "SEP" };
  if (employee.isRetired) return { amount: 0, reasonCode: "RET" };
  return calculateNormalPay(employee);
}
```

---

### 以多态替代条件表达式

**使用时机**：基于类型的 switch/case，按类型变化的条件逻辑

**动机**：让对象处理自己的行为。

**机制**：
1. 创建类层次结构（如果不存在）
2. 使用工厂函数创建对象
3. 将条件逻辑移入超类方法
4. 为每个 case 创建子类方法
5. 删除原始条件

**重构前：**
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

**重构后：**
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

### 引入特殊情况（空对象）

**使用时机**：对特殊情况的重复 null 检查

**动机**：返回处理特殊情况的特殊对象。

**机制**：
1. 创建具有期望接口的特殊情况类
2. 添加 isSpecialCase 检查
3. 引入工厂方法
4. 用特殊情况对象用法替换 null 检查
5. 测试

**重构前：**
```javascript
const customer = site.customer;
// ... 在许多地方检查
if (customer === "unknown") {
  customerName = "occupant";
} else {
  customerName = customer.name;
}
```

**重构后：**
```javascript
class UnknownCustomer {
  get name() { return "occupant"; }
  get billingPlan() { return registry.defaultPlan; }
}

// 工厂方法
function customer(site) {
  return site.customer === "unknown"
    ? new UnknownCustomer()
    : site.customer;
}

// 使用——不需要 null 检查
const customerName = customer.name;
```

---

## 重构 API

### 分离查询和修改器

**使用时机**：函数既返回值又有副作用

**动机**：明确哪些操作有副作用。

**机制**：
1. 创建新的查询函数
2. 复制原始函数的返回逻辑
3. 修改原始函数以返回 void
4. 替换使用返回值的调用
5. 测试

**重构前：**
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

**重构后：**
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

### 参数化函数

**使用时机**：几个函数用不同的值做类似的事情

**动机**：通过添加参数来消除重复。

**机制**：
1. 选择一个函数
2. 为变化的字面值添加参数
3. 将函数体改为使用参数
4. 测试
5. 更改调用者使用参数化版本
6. 删除现在未使用的函数

**重构前：**
```javascript
function tenPercentRaise(person) {
  person.salary = person.salary * 1.10;
}

function fivePercentRaise(person) {
  person.salary = person.salary * 1.05;
}
```

**重构后：**
```javascript
function raise(person, factor) {
  person.salary = person.salary * (1 + factor);
}

// 使用
raise(person, 0.10);
raise(person, 0.05);
```

---

### 移除标志参数

**使用时机**：改变函数行为的布尔参数

**动机**：通过单独的函数使行为明确。

**机制**：
1. 为每个标志值创建显式函数
2. 用适当的新函数替换每个调用
3. 每次变更后测试
4. 删除原始函数

**重构前：**
```javascript
function bookConcert(customer, isPremium) {
  if (isPremium) {
    // 高级预订逻辑
  } else {
    // 常规预订逻辑
  }
}

bookConcert(customer, true);
bookConcert(customer, false);
```

**重构后：**
```javascript
function bookPremiumConcert(customer) {
  // 高级预订逻辑
}

function bookRegularConcert(customer) {
  // 常规预订逻辑
}

bookPremiumConcert(customer);
bookRegularConcert(customer);
```

---

## 处理继承

### 上移方法

**使用时机**：多个子类中存在相同的方法

**动机**：消除类层次结构中的重复。

**机制**：
1. 检查方法是否相同
2. 检查签名是否相同
3. 在超类中创建新方法
4. 从一个子类复制方法体
5. 删除一个子类方法，测试
6. 删除其他子类方法，每次测试

---

### 下移方法

**使用时机**：行为仅与子类的子集相关

**动机**：将方法放在使用它的地方。

**机制**：
1. 将方法复制到需要它的每个子类
2. 从超类中删除方法
3. 测试
4. 从不需要它的子类中删除
5. 测试

---

### 以委托替换子类

**使用时机**：继承使用不正确，需要更多灵活性

**动机**：在适当的情况下，优先使用组合而非继承。

**机制**：
1. 为委托创建空类
2. 在宿主类中添加保存委托的字段
3. 为委托创建构造函数，从宿主调用
4. 将特性移至委托
5. 每次移动后测试
6. 用委托替换继承

---

## 提取类

**使用时机**：具有多个职责的大类

**动机**：分割类以维护单一职责。

**机制**：
1. 决定如何分割职责
2. 创建新类
3. 将字段从原始类移至新类
4. 测试
5. 将方法从原始类移至新类
6. 每次移动后测试
7. 审查并重命名两个类
8. 决定如何暴露新类

**重构前：**
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

**重构后：**
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

## 快速参考：异味到重构

| 代码异味 | 主要重构 | 备选 |
|----------|---------|------|
| 长方法 | 提取方法 | 以查询替代临时变量 |
| 重复代码 | 提取方法 | 上移方法 |
| 大类 | 提取类 | 提取子类 |
| 过长参数列表 | 引入参数对象 | 保持完整对象 |
| 特性依恋 | 移动方法 | 提取方法 + 移动 |
| 数据泥团 | 提取类 | 引入参数对象 |
| 基本类型偏执 | 以对象替代基本类型 | 替换类型码 |
| switch 语句 | 以多态替代条件表达式 | 替换类型码 |
| 临时字段 | 提取类 | 引入空对象 |
| 消息链 | 隐藏委托 | 提取方法 |
| 中间人 | 移除中间人 | 内联方法 |
| 发散式变化 | 提取类 | 拆分阶段 |
| 散弹式修改 | 移动方法 | 内联类 |
| 死代码 | 删除死代码 | - |
| 过度设计 | 折叠继承体系 | 内联类 |

---

## 延伸阅读

- Fowler, M. (2018). *重构：改善既有代码的设计*（第2版）
- 在线目录：https://refactoring.com/catalog/
