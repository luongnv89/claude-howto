# 代码异味目录

基于 Martin Fowler 的《*重构*》（第2版）的代码异味综合参考。代码异味是更深层问题的症状——它们表明代码设计可能存在问题。

> "代码异味是通常对应于系统中更深层问题的表面迹象。" — Martin Fowler

---

## 膨胀者（Bloaters）

表示某些东西已经增长到难以有效处理的代码异味。

### 长方法

**迹象：**
- 方法超过 30-50 行
- 需要滚动才能看到整个方法
- 多层嵌套
- 解释各部分功能的注释

**为什么不好：**
- 难以理解
- 难以独立测试
- 变更会产生意外后果
- 重复逻辑隐藏在内部

**重构方法：**
- 提取方法
- 以查询替代临时变量
- 引入参数对象
- 以方法对象替代方法
- 分解条件表达式

**示例（重构前）：**
```javascript
function processOrder(order) {
  // 验证订单（20 行）
  if (!order.items) throw new Error('No items');
  if (order.items.length === 0) throw new Error('Empty order');
  // ... 更多验证

  // 计算总计（30 行）
  let subtotal = 0;
  for (const item of order.items) {
    subtotal += item.price * item.quantity;
  }
  // ... 税费、运费、折扣

  // 发送通知（20 行）
  // ... 邮件逻辑
}
```

**示例（重构后）：**
```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  sendOrderNotifications(order, totals);
  return { order, totals };
}
```

---

### 大类

**迹象：**
- 类有很多实例变量（> 7-10 个）
- 类有很多方法（> 15-20 个）
- 类名模糊（Manager、Handler、Processor）
- 方法不使用所有实例变量

**为什么不好：**
- 违反单一职责原则
- 难以测试
- 变更会波及不相关的功能
- 难以复用部分功能

**重构方法：**
- 提取类
- 提取子类
- 提取接口

**检测标准：**
```
代码行数 > 300
方法数量 > 15
字段数量 > 10
```

---

### 基本类型偏执

**迹象：**
- 使用基本类型表示领域概念（字符串表示邮件，整数表示金额）
- 基本类型数组代替对象
- 字符串常量表示类型码
- 魔法数字/字符串

**为什么不好：**
- 类型级别无验证
- 逻辑散布在代码库中
- 容易传递错误的值
- 缺失领域概念

**重构方法：**
- 以对象替代基本类型
- 以类替代类型码
- 以子类替代类型码
- 以状态/策略替代类型码

**示例（重构前）：**
```javascript
const user = {
  email: 'john@example.com',     // 只是一个字符串
  phone: '1234567890',           // 只是一个字符串
  status: 'active',              // 魔法字符串
  balance: 10050                 // 分为单位的整数
};
```

**示例（重构后）：**
```javascript
const user = {
  email: new Email('john@example.com'),
  phone: new PhoneNumber('1234567890'),
  status: UserStatus.ACTIVE,
  balance: Money.cents(10050)
};
```

---

### 过长参数列表

**迹象：**
- 方法有 4+ 个参数
- 总是一起出现的参数
- 改变方法行为的布尔标志
- 频繁传递 null/undefined

**为什么不好：**
- 难以正确调用
- 参数顺序容易混淆
- 表明方法做了太多事
- 难以添加新参数

**重构方法：**
- 引入参数对象
- 保持完整对象
- 以方法调用替代参数
- 移除标志参数

**示例（重构前）：**
```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy) {
  // ...
}
```

**示例（重构后）：**
```javascript
function createUser(personalInfo, address, options) {
  // personalInfo: { firstName, lastName, email, phone }
  // address: { street, city, state, zip }
  // options: { isAdmin, isActive, createdBy }
}
```

---

### 数据泥团

**迹象：**
- 同一组 3+ 个字段重复出现
- 总是一起传递的参数
- 字段子集属于一起的类

**为什么不好：**
- 重复处理逻辑
- 缺失抽象
- 难以扩展
- 表明存在隐藏的类

**重构方法：**
- 提取类
- 引入参数对象
- 保持完整对象

**示例：**
```javascript
// 数据泥团：(x, y, z) 坐标
function movePoint(x, y, z, dx, dy, dz) { }
function scalePoint(x, y, z, factor) { }
function distanceBetween(x1, y1, z1, x2, y2, z2) { }

// 提取 Point3D 类
class Point3D {
  constructor(x, y, z) { }
  move(delta) { }
  scale(factor) { }
  distanceTo(other) { }
}
```

---

## 面向对象滥用者（Object-Orientation Abusers）

表明面向对象原则使用不完整或不正确的异味。

### switch 语句

**迹象：**
- 长的 switch/case 或 if/else 链
- 相同的 switch 出现在多个地方
- 对类型码进行 switch
- 添加新 case 需要在所有地方做变更

**为什么不好：**
- 违反开闭原则
- 变更波及所有 switch 位置
- 难以扩展
- 通常表明缺失多态性

**重构方法：**
- 以多态替代条件表达式
- 以子类替代类型码
- 以状态/策略替代类型码

**示例（重构前）：**
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

**示例（重构后）：**
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

### 临时字段

**迹象：**
- 实例变量只在某些方法中使用
- 字段被条件性地设置
- 某些情况下的复杂初始化

**为什么不好：**
- 令人困惑——字段存在但可能为 null
- 难以理解对象状态
- 表明存在隐藏的条件逻辑

**重构方法：**
- 提取类
- 引入空对象
- 以局部变量替代临时字段

---

### 被拒绝的遗赠

**迹象：**
- 子类不使用继承的方法/数据
- 子类覆盖以什么都不做
- 继承用于代码复用，而非 IS-A 关系

**为什么不好：**
- 错误的抽象
- 违反里氏替换原则
- 误导性的层次结构

**重构方法：**
- 下移方法/字段
- 以委托替代子类
- 以委托替代继承

---

### 接口不同的替代类

**迹象：**
- 两个类做相似的事情
- 相同概念的不同方法名
- 可以互换使用

**为什么不好：**
- 重复实现
- 没有公共接口
- 难以在两者之间切换

**重构方法：**
- 重命名方法
- 移动方法
- 提取超类
- 提取接口

---

## 变更阻碍者（Change Preventers）

使变更变得困难的异味——改变一件事需要改变许多其他事情。

### 发散式变化

**迹象：**
- 一个类因多种不同原因而变更
- 不同领域的变更触发对同一类的编辑
- 该类是"神类"

**为什么不好：**
- 违反单一职责
- 变更频率高
- 合并冲突

**重构方法：**
- 提取类
- 提取超类
- 提取子类

**示例：**
`User` 类因以下原因变更：
- 认证变更
- 资料变更
- 账单变更
- 通知变更

→ 提取：`AuthService`、`ProfileService`、`BillingService`、`NotificationService`

---

### 散弹式修改

**迹象：**
- 一次变更需要在许多类中进行编辑
- 小功能需要修改 10+ 个文件
- 变更是分散的，难以找到所有位置

**为什么不好：**
- 容易遗漏某个位置
- 高耦合
- 变更容易出错

**重构方法：**
- 移动方法
- 移动字段
- 内联类

**检测标准：**
查找：添加一个字段需要在 > 5 个文件中变更。

---

### 平行继承体系

**迹象：**
- 在一个层次结构中创建子类需要在另一个中创建子类
- 类前缀匹配（例如，`DatabaseOrder`、`DatabaseProduct`）

**为什么不好：**
- 双倍维护
- 层次结构之间的耦合
- 容易忘记一侧

**重构方法：**
- 移动方法
- 移动字段
- 消除一个层次结构

---

## 可去除物（Dispensables）

不必要的、应该删除的东西。

### 注释（过度的）

**迹象：**
- 解释代码做什么的注释
- 被注释掉的代码
- 永远存在的 TODO/FIXME
- 注释中的道歉

**为什么不好：**
- 注释会说谎（与代码不同步）
- 代码应该自文档化
- 死代码造成混乱

**重构方法：**
- 提取方法（名称解释做什么）
- 重命名（无需注释即可清晰）
- 删除注释掉的代码
- 引入断言

**好注释与坏注释：**
```javascript
// 坏：解释什么
// 遍历用户并检查是否活跃
for (const user of users) {
  if (user.status === 'active') { }
}

// 好：解释为什么
// 仅活跃用户——非活跃用户由清理任务处理
const activeUsers = users.filter(u => u.isActive);
```

---

### 重复代码

**迹象：**
- 多处相同的代码
- 有小变化的类似代码
- 复制粘贴模式

**为什么不好：**
- bug 修复需要在多处进行
- 不一致风险
- 代码库膨胀

**重构方法：**
- 提取方法
- 提取类
- 上移方法（在层次结构中）
- 形成模板方法

**检测规则：**
重复 3+ 次的任何代码都应该被提取。

---

### 懒类

**迹象：**
- 类做的事情不足以证明其存在的合理性
- 无附加价值的包装器
- 过度设计的结果

**为什么不好：**
- 维护开销
- 不必要的间接性
- 无益处的复杂性

**重构方法：**
- 内联类
- 折叠继承体系

---

### 死代码

**迹象：**
- 不可达的代码
- 未使用的变量/方法/类
- 被注释掉的代码
- 不可能条件后面的代码

**为什么不好：**
- 造成混乱
- 维护负担
- 减慢理解速度

**重构方法：**
- 删除死代码
- 安全删除

**检测：**
```bash
# 查找未使用的导出
# 查找未引用的函数
# IDE "unused" 警告
```

---

### 过度设计

**迹象：**
- 只有一个子类的抽象类
- "将来使用"的未使用参数
- 只委托的方法
- 只有一个用例的"框架"

**为什么不好：**
- 无益处的复杂性
- YAGNI（你不会需要它）
- 更难理解

**重构方法：**
- 折叠继承体系
- 内联类
- 删除参数
- 重命名方法

---

## 耦合者（Couplers）

表示类之间过度耦合的异味。

### 特性依恋

**迹象：**
- 方法使用另一个类的数据多于自身的数据
- 对另一个对象的许多 getter 调用
- 数据和行为被分离

**为什么不好：**
- 行为的位置错误
- 封装性差
- 难以维护

**重构方法：**
- 移动方法
- 移动字段
- 提取方法（然后移动）

**示例（重构前）：**
```javascript
class Order {
  getDiscountedPrice(customer) {
    // 大量使用 customer 数据
    if (customer.loyaltyYears > 5) {
      return this.price * customer.discountRate;
    }
    return this.price;
  }
}
```

**示例（重构后）：**
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

### 不恰当的亲密关系

**迹象：**
- 类访问彼此的私有部分
- 双向引用
- 子类对父类了解太多

**为什么不好：**
- 高耦合
- 变更会级联
- 难以在不影响另一个的情况下修改一个

**重构方法：**
- 移动方法
- 移动字段
- 将双向改为单向
- 提取类
- 隐藏委托

---

### 消息链

**迹象：**
- 长的方法调用链：`a.getB().getC().getD().getValue()`
- 客户端依赖于导航结构
- "火车事故"代码

**为什么不好：**
- 脆弱——任何变更都会破坏链
- 违反得墨忒耳定律
- 耦合于结构

**重构方法：**
- 隐藏委托
- 提取方法
- 移动方法

**示例：**
```javascript
// 坏：消息链
const managerName = employee.getDepartment().getManager().getName();

// 好：隐藏委托
const managerName = employee.getManagerName();
```

---

### 中间人

**迹象：**
- 只委托给另一个类的类
- 一半的方法是委托
- 没有附加价值

**为什么不好：**
- 不必要的间接性
- 维护开销
- 令人困惑的架构

**重构方法：**
- 移除中间人
- 内联方法

---

## 异味严重性指南

| 严重性 | 描述 | 行动 |
|--------|------|------|
| **严重** | 阻碍开发，导致 bug | 立即修复 |
| **高** | 重大维护负担 | 在当前迭代中修复 |
| **中** | 明显但可控 | 计划在近期修复 |
| **低** | 轻微不便 | 机会性修复 |

---

## 快速检测清单

扫描代码时使用此清单：

- [ ] 有方法 > 30 行吗？
- [ ] 有类 > 300 行吗？
- [ ] 有方法带 > 4 个参数吗？
- [ ] 有重复的代码块吗？
- [ ] 有对类型码进行 switch/case 吗？
- [ ] 有未使用的代码吗？
- [ ] 有方法大量使用另一个类的数据吗？
- [ ] 有长的方法调用链吗？
- [ ] 有解释"什么"而非"为什么"的注释吗？
- [ ] 有应该是对象的基本类型吗？

---

## 延伸阅读

- Fowler, M. (2018). *重构：改善既有代码的设计*（第2版）
- Kerievsky, J. (2004). *重构与模式*
- Feathers, M. (2004). *修改代码的艺术*
