# 重构目录

这是 Martin Fowler《Refactoring》（第 2 版）中的一份精选重构目录。每个重构都包含动机、操作步骤和示例。

> “重构由它的操作步骤来定义，也就是你执行这个变化时遵循的精确过程。” — Martin Fowler

---

## 如何使用这个目录

1. **识别异味**：先用代码异味目录定位问题
2. **找到对应重构**：在这里查找匹配的手法
3. **按步骤执行**：一步一步来
4. **每步都测试**：确保行为不变

**黄金法则**：如果某一步超过 10 分钟，就把它拆得更小。

---

## 最常见的重构

### Extract Method

**何时使用**：长函数、重复代码、需要为概念命名

**动机**：把一段代码抽成一个名字能说明意图的方法。

**步骤**：
1. 创建一个新方法，名字应描述“做什么”而不是“怎么做”
2. 把代码片段复制到新方法里
3. 检查片段里用了哪些局部变量
4. 把局部变量作为参数传入，或在方法内声明
5. 正确处理返回值
6. 用新方法调用替换原始片段
7. 测试

**前：**
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

**后：**
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

**何时使用**：方法体和名字一样清楚，或者只是多余转发

**动机**：当方法没有额外价值时，去掉不必要的间接层。

**步骤**：
1. 确认这个方法不是多态方法
2. 找到所有调用点
3. 用方法体替换每个调用
4. 每替换一次就测试一次
5. 删除方法定义

**前：**
```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**后：**
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### Extract Variable

**何时使用**：复杂表达式难以理解

**动机**：给复杂表达式的一部分起名字。

**步骤**：
1. 确保表达式没有副作用
2. 声明一个不可变变量
3. 将表达式结果赋给变量
4. 用变量替换原表达式
5. 测试

**前：**
```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**后：**
```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### Inline Variable

**何时使用**：变量名没有比表达式更清楚

**动机**：移除没必要的间接层。

**步骤**：
1. 检查右侧表达式没有副作用
2. 如果变量不是不可变的，先改成不可变并测试
3. 找到第一次引用并替换成表达式
4. 测试
5. 对所有引用重复
6. 删除变量声明和赋值
7. 测试

---

### Rename Variable

**何时使用**：名字没有清楚表达用途

**动机**：好名字是清晰代码的基础。

**步骤**：
1. 如果变量使用范围很广，先考虑封装
2. 找到所有引用
3. 逐个修改引用
4. 测试

**提示**：
- 使用能体现意图的名字
- 避免缩写
- 使用领域术语

```javascript
// Bad
const d = 30;
const x = users.filter(u => u.a);

// Good
const daysSinceLastLogin = 30;
const activeUsers = users.filter(user => user.isActive);
```

---

### Change Function Declaration

**何时使用**：函数名不能清楚说明用途，参数也需要变化

**动机**：好函数名能让代码自解释。

**步骤（简单情况）**：
1. 删除不需要的参数
2. 修改函数名
3. 添加需要的参数
4. 测试

**步骤（迁移式，适用于复杂改动）**：
1. 如果要删除参数，确保它没有被使用
2. 创建一个新函数，声明符合新设计
3. 让旧函数调用新函数
4. 测试
5. 让调用方逐步改用新函数
6. 每改一个调用点就测试
7. 删除旧函数

**前：**
```javascript
function circum(radius) {
  return 2 * Math.PI * radius;
}
```

**后：**
```javascript
function circumference(radius) {
  return 2 * Math.PI * radius;
}
```

---

### Encapsulate Variable

**何时使用**：多个地方直接访问某个数据

**动机**：为数据访问提供明确入口。

**步骤**：
1. 创建 getter 和 setter
2. 找到所有引用
3. 用 getter 替换读取
4. 用 setter 替换写入
5. 每次改动后测试
6. 降低变量可见性

**前：**
```javascript
let defaultOwner = { firstName: "Martin", lastName: "Fowler" };

// Used in many places
spaceship.owner = defaultOwner;
```

**后：**
```javascript
let defaultOwnerData = { firstName: "Martin", lastName: "Fowler" };

function defaultOwner() { return defaultOwnerData; }
function setDefaultOwner(arg) { defaultOwnerData = arg; }

spaceship.owner = defaultOwner();
```

---

### Introduce Parameter Object

**何时使用**：一组参数经常一起出现

**动机**：把自然属于一起的数据打包起来。

**步骤**：
1. 为这组参数创建一个新类 / 结构
2. 测试
3. 用 Change Function Declaration 引入新对象
4. 测试
5. 逐个移除参数，改用对象字段
6. 每次移除后测试

**前：**
```javascript
function amountInvoiced(startDate, endDate) { ... }
function amountReceived(startDate, endDate) { ... }
function amountOverdue(startDate, endDate) { ... }
```

**后：**
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

**何时使用**：多个函数操作同一份数据

**动机**：把函数和它操作的数据放到一起。

**步骤**：
1. 对公共数据先做 Encapsulate Record
2. 把每个函数移动到类里
3. 每移动一次就测试
4. 用类字段替代数据参数

**前：**
```javascript
function base(reading) { ... }
function taxableCharge(reading) { ... }
function calculateBaseCharge(reading) { ... }
```

**后：**
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

**何时使用**：代码在处理两件不同的事

**动机**：把代码拆成边界清晰的两个阶段。

**步骤**：
1. 为第二阶段创建新函数
2. 测试
3. 在两个阶段之间引入中间数据结构
4. 测试
5. 把第一阶段提取成独立函数
6. 测试

**前：**
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

**后：**
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

## 移动特性

### Move Method

**何时使用**：方法更依赖另一个类的数据而不是自己类的数据

**动机**：把函数放到它最依赖的数据所在的类里。

**步骤**：
1. 检查方法使用到的所有程序元素
2. 确认方法不是多态的
3. 把方法复制到目标类
4. 调整上下文
5. 让原方法委托给目标方法
6. 测试
7. 视情况删除原方法

---

### Move Field

**何时使用**：字段更多被另一个类使用

**动机**：让数据和使用它的函数靠在一起。

**步骤**：
1. 如果还没有，先封装字段
2. 测试
3. 在目标类中创建字段
4. 把引用改成使用目标字段
5. 测试
6. 删除原字段

---

### Move Statements into Function

**何时使用**：相同代码总是跟着函数调用一起出现

**动机**：把重复语句移入函数，去掉重复。

**步骤**：
1. 如果还没有，先把重复代码提取成函数
2. 把语句移入函数
3. 测试
4. 如果调用方不再需要独立语句，就删除它们

---

### Move Statements to Callers

**何时使用**：不同调用方需要不同的行为

**动机**：当行为需要差异化时，把它从函数里移出去。

**步骤**：
1. 先对要移动的代码做 Extract Method
2. 再对原函数做 Inline Method
3. 删除被内联后的调用
4. 把提取出的代码移到各个调用方
5. 测试

---

## 数据组织

### Replace Primitive with Object

**何时使用**：数据项需要的不只是简单值

**动机**：把数据和行为封装在一起。

**步骤**：
1. 先做 Encapsulate Variable
2. 创建一个简单值对象
3. 修改 setter，让它创建新实例
4. 修改 getter，让它返回值
5. 测试
6. 给新类增加更丰富的行为

**前：**
```javascript
class Order {
  constructor(data) {
    this.priority = data.priority; // string: "high", "rush", etc.
  }
}

// Usage
if (order.priority === "high" || order.priority === "rush") { ... }
```

**后：**
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

### Replace Temp with Query

**何时使用**：临时变量保存的是一个表达式结果

**动机**：把表达式提取成函数，让代码更清晰。

**步骤**：
1. 确保变量只被赋值一次
2. 把赋值右侧提取成一个方法
3. 用方法调用替换临时变量引用
4. 测试
5. 删除临时变量声明和赋值

**前：**
```javascript
const basePrice = this._quantity * this._itemPrice;
if (basePrice > 1000) {
  return basePrice * 0.95;
} else {
  return basePrice * 0.98;
}
```

**后：**
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

## 简化条件逻辑

### Decompose Conditional

**何时使用**：复杂条件语句

**动机**：把条件和分支动作分别提取出来，让意图更清楚。

**步骤**：
1. 对条件做 Extract Method
2. 对 then 分支做 Extract Method
3. 对 else 分支也做 Extract Method（如果有）

**前：**
```javascript
if (!aDate.isBefore(plan.summerStart) && !aDate.isAfter(plan.summerEnd)) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}
```

**后：**
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

**何时使用**：多个条件最后都返回同一个结果

**动机**：让人一眼看出这些条件其实是一道检查。

**步骤**：
1. 确认条件没有副作用
2. 用 and / or 合并条件
3. 视情况对合并后的条件做 Extract Method

**前：**
```javascript
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;
```

**后：**
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

**何时使用**：深层嵌套条件让流程难以追踪

**动机**：用 guard clause 提前返回，让正常流程更清楚。

**步骤**：
1. 找出特殊情况
2. 用提前返回的 guard clause 替换它们
3. 每改一步就测试

**前：**
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

**后：**
```javascript
function payAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reasonCode: "SEP" };
  if (employee.isRetired) return { amount: 0, reasonCode: "RET" };
  return calculateNormalPay(employee);
}
```

---

### Replace Conditional with Polymorphism

**何时使用**：按类型分支的 switch / 条件逻辑

**动机**：让对象自己处理自己的行为。

**步骤**：
1. 创建类层次（如果还没有）
2. 用 Factory Function 创建对象
3. 把条件逻辑移到超类方法里
4. 给每种情况创建子类方法
5. 删除原条件

**前：**
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

**后：**
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

**何时使用**：重复出现 null 检查

**动机**：返回一个特殊对象来处理特殊情况。

**步骤**：
1. 创建一个具备预期接口的特殊情况类
2. 增加 isSpecialCase 检查
3. 引入工厂方法
4. 用特殊对象替换 null 检查
5. 测试

**前：**
```javascript
const customer = site.customer;
// ... many places checking
if (customer === "unknown") {
  customerName = "occupant";
} else {
  customerName = customer.name;
}
```

**后：**
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

## 重构 API

### Separate Query from Modifier

**何时使用**：函数既返回值又有副作用

**动机**：明确哪些操作会产生副作用。

**步骤**：
1. 创建新的查询函数
2. 复制原函数的返回逻辑
3. 修改原函数，让它只负责副作用
4. 替换依赖返回值的调用点
5. 测试

**前：**
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

**后：**
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

**何时使用**：有多个做类似事情但数值不同的函数

**动机**：通过参数化减少重复。

**步骤**：
1. 选择一个函数
2. 为变化的字面值增加参数
3. 修改函数体使用该参数
4. 测试
5. 让调用方改用参数化版本
6. 删除不再使用的旧函数

**前：**
```javascript
function tenPercentRaise(person) {
  person.salary = person.salary * 1.10;
}

function fivePercentRaise(person) {
  person.salary = person.salary * 1.05;
}
```

**后：**
```javascript
function raise(person, factor) {
  person.salary = person.salary * (1 + factor);
}

// Usage
raise(person, 0.10);
raise(person, 0.05);
```

---

### Remove Flag Argument

**何时使用**：布尔参数改变函数行为

**动机**：通过拆分成明确函数，让行为更清楚。

**步骤**：
1. 针对不同旗标值创建显式函数
2. 替换每个调用点
3. 每次改动后测试
4. 删除原函数

**前：**
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

**后：**
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

## 继承相关

### Pull Up Method

**何时使用**：多个子类里有相同方法

**动机**：去掉类层次中的重复。

**步骤**：
1. 检查方法是否完全相同
2. 确认签名一致
3. 在超类中新建方法
4. 从一个子类复制实现
5. 删除一个子类中的方法并测试
6. 删除其他子类中的方法并测试

---

### Push Down Method

**何时使用**：某个行为只适用于部分子类

**动机**：把方法放到真正使用它的地方。

**步骤**：
1. 把方法复制到需要它的子类
2. 从超类删除方法
3. 测试
4. 删除不需要该方法的子类副本
5. 测试

---

### Replace Subclass with Delegate

**何时使用**：继承用得不对，需要更灵活

**动机**：在合适的地方更偏向组合而不是继承。

**步骤**：
1. 创建一个空的委托类
2. 在宿主类中加一个持有委托的字段
3. 在宿主类构造委托
4. 把功能迁移到委托类
5. 每次迁移后测试
6. 用委托替代继承

---

## Extract Class

**何时使用**：大类里有多个职责

**动机**：拆分类以维持单一职责。

**步骤**：
1. 决定如何拆分职责
2. 创建新类
3. 把字段从原类移到新类
4. 测试
5. 把方法从原类移到新类
6. 每次移动后测试
7. 重新检查并命名两个类
8. 决定如何暴露新类

**前：**
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

**后：**
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

| 代码异味 | 主要重构 | 备选方案 |
|----------|---------|---------|
| 长函数 | Extract Method | Replace Temp with Query |
| 重复代码 | Extract Method | Pull Up Method |
| 大类 | Extract Class | Extract Subclass |
| 长参数列表 | Introduce Parameter Object | Preserve Whole Object |
| Feature Envy | Move Method | Extract Method + Move |
| 数据泥团 | Extract Class | Introduce Parameter Object |
| 基础类型沉迷 | Replace Primitive with Object | Replace Type Code |
| switch 语句 | Replace Conditional with Polymorphism | Replace Type Code |
| 临时字段 | Extract Class | Introduce Null Object |
| 消息链 | Hide Delegate | Extract Method |
| 中间人 | Remove Middle Man | Inline Method |
| 发散式变化 | Extract Class | Split Phase |
| 散弹式修改 | Move Method | Inline Class |
| 死代码 | Remove Dead Code | - |
| 臆想泛化 | Collapse Hierarchy | Inline Class |

---

## 延伸阅读

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (第 2 版)
- 在线目录：https://refactoring.com/catalog/
