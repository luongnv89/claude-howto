# 程式碼壞味道目錄

基於 Martin Fowler《重構》（第二版）的程式碼壞味道完整參考。程式碼壞味道是更深層問題的症狀 — 它們表明你的程式碼設計可能有問題。

> 「程式碼壞味道是一種表面指示，通常對應於系統中更深層的問題。」 — Martin Fowler

---

## 膨脹器

代表某些東西已成長到無法有效處理的程式碼壞味道。

### 過長方法

**徵兆：**
- 方法超過 30-50 行
- 需要捲動才能看到整個方法
- 多層巢狀
- 註解解釋各區段的功能

**為什麼不好：**
- 難以理解
- 難以單獨測試
- 變更產生意外後果
- 重複邏輯隱藏其中

**重構手法：**
- 提取方法
- 以查詢取代暫時變數
- 引入參數物件
- 以方法物件取代方法
- 分解條件式

**範例（重構前）：**
```javascript
function processOrder(order) {
  // Validate order (20 lines)
  if (!order.items) throw new Error('No items');
  if (order.items.length === 0) throw new Error('Empty order');
  // ... more validation

  // Calculate totals (30 lines)
  let subtotal = 0;
  for (const item of order.items) {
    subtotal += item.price * item.quantity;
  }
  // ... tax, shipping, discounts

  // Send notifications (20 lines)
  // ... email logic
}
```

**範例（重構後）：**
```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  sendOrderNotifications(order, totals);
  return { order, totals };
}
```

---

### 過大類別

**徵兆：**
- 類別有許多實體變數（>7-10）
- 類別有許多方法（>15-20）
- 類別名稱模糊（Manager、Handler、Processor）
- 方法不使用所有實體變數

**為什麼不好：**
- 違反單一職責原則
- 難以測試
- 變更波及無關的功能
- 難以重用部分功能

**重構手法：**
- 提取類別
- 提取子類別
- 提取介面

**偵測：**
```
Lines of code > 300
Number of methods > 15
Number of fields > 10
```

---

### 基本型別偏執

**徵兆：**
- 對領域概念使用基本型別（string 表示 email，int 表示金額）
- 使用基本型別陣列而非物件
- 用字串常數表示型別代碼
- 魔術數字/字串

**為什麼不好：**
- 型別層級無驗證
- 邏輯散佈在程式碼庫各處
- 容易傳入錯誤的值
- 缺少領域概念

**重構手法：**
- 以物件取代基本型別
- 以類別取代型別代碼
- 以子類別取代型別代碼
- 以狀態/策略取代型別代碼

**範例（重構前）：**
```javascript
const user = {
  email: 'john@example.com',     // Just a string
  phone: '1234567890',           // Just a string
  status: 'active',              // Magic string
  balance: 10050                 // Cents as integer
};
```

**範例（重構後）：**
```javascript
const user = {
  email: new Email('john@example.com'),
  phone: new PhoneNumber('1234567890'),
  status: UserStatus.ACTIVE,
  balance: Money.cents(10050)
};
```

---

### 過長參數列

**徵兆：**
- 方法有 4 個以上參數
- 參數總是一起出現
- 布林旗標改變方法行為
- 經常傳入 null/undefined

**為什麼不好：**
- 難以正確呼叫
- 參數順序混淆
- 表示方法做太多事
- 難以新增參數

**重構手法：**
- 引入參數物件
- 保持整體物件
- 以方法呼叫取代參數
- 移除旗標引數

**範例（重構前）：**
```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy) {
  // ...
}
```

**範例（重構後）：**
```javascript
function createUser(personalInfo, address, options) {
  // personalInfo: { firstName, lastName, email, phone }
  // address: { street, city, state, zip }
  // options: { isAdmin, isActive, createdBy }
}
```

---

### 資料泥團

**徵兆：**
- 相同的 3 個以上欄位反覆一起出現
- 總是一起出現的參數
- 類別中欄位子集屬於同一群組

**為什麼不好：**
- 重複的處理邏輯
- 缺少抽象
- 難以擴展
- 表示隱藏的類別

**重構手法：**
- 提取類別
- 引入參數物件
- 保持整體物件

**範例：**
```javascript
// Data clump: (x, y, z) coordinates
function movePoint(x, y, z, dx, dy, dz) { }
function scalePoint(x, y, z, factor) { }
function distanceBetween(x1, y1, z1, x2, y2, z2) { }

// Extract Point3D class
class Point3D {
  constructor(x, y, z) { }
  move(delta) { }
  scale(factor) { }
  distanceTo(other) { }
}
```

---

## 物件導向濫用者

表示不完整或不正確使用 OOP 原則的壞味道。

### Switch 語句

**徵兆：**
- 冗長的 switch/case 或 if/else 鏈
- 多處有相同的 switch
- 基於型別代碼的 switch
- 新增案例需要到處修改

**為什麼不好：**
- 違反開放/封閉原則
- 變更波及所有 switch 位置
- 難以擴展
- 通常表示缺少多型

**重構手法：**
- 以多型取代條件式
- 以子類別取代型別代碼
- 以狀態/策略取代型別代碼

**範例（重構前）：**
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

**範例（重構後）：**
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

### 暫時欄位

**徵兆：**
- 實體變數僅在某些方法中使用
- 欄位有條件地設定
- 某些情況下的複雜初始化

**為什麼不好：**
- 令人困惑 — 欄位存在但可能為 null
- 難以理解物件狀態
- 表示隱藏的條件邏輯

**重構手法：**
- 提取類別
- 引入 Null 物件
- 以區域變數取代暫時欄位

---

### 被拒絕的遺贈

**徵兆：**
- 子類別不使用繼承的方法/資料
- 子類別覆寫為什麼都不做
- 繼承用於程式碼重用而非 IS-A 關係

**為什麼不好：**
- 錯誤的抽象
- 違反 Liskov 替換原則
- 誤導性的層級

**重構手法：**
- 下推方法/欄位
- 以委派取代子類別
- 以委派取代繼承

---

### 介面不同的替代類別

**徵兆：**
- 兩個類別做類似的事情
- 相同概念使用不同方法名稱
- 可以互換使用

**為什麼不好：**
- 重複的實作
- 沒有共同介面
- 難以切換

**重構手法：**
- 重新命名方法
- 搬移方法
- 提取超類別
- 提取介面

---

## 變更阻礙者

使變更變得困難的壞味道 — 改變一件事需要改變許多其他東西。

### 發散式變更

**徵兆：**
- 一個類別因多個不同原因而被修改
- 不同領域的變更觸發同一類別的編輯
- 類別是「上帝類別」

**為什麼不好：**
- 違反單一職責
- 高變更頻率
- 合併衝突

**重構手法：**
- 提取類別
- 提取超類別
- 提取子類別

**範例：**
一個 `User` 類別因以下原因而變更：
- 認證變更
- 個人資料變更
- 計費變更
- 通知變更

→ 提取：`AuthService`、`ProfileService`、`BillingService`、`NotificationService`

---

### 散彈式修改

**徵兆：**
- 一個變更需要編輯許多類別
- 小功能需要觸及 10 個以上檔案
- 變更分散，難以找到全部

**為什麼不好：**
- 容易遺漏
- 高耦合
- 變更容易出錯

**重構手法：**
- 搬移方法
- 搬移欄位
- 內聯類別

**偵測：**
檢查：新增一個欄位需要在超過 5 個檔案中變更。

---

### 平行繼承層級

**徵兆：**
- 在一個層級中建立子類別需要在另一個層級中也建立子類別
- 類別前綴匹配（例如 `DatabaseOrder`、`DatabaseProduct`）

**為什麼不好：**
- 雙倍維護
- 層級間耦合
- 容易忘記另一邊

**重構手法：**
- 搬移方法
- 搬移欄位
- 消除一個層級

---

## 可省略者

不必要的東西，應該被移除。

### 過多註解

**徵兆：**
- 註解解釋程式碼做什麼
- 被註解掉的程式碼
- 永遠存在的 TODO/FIXME
- 註解中的道歉

**為什麼不好：**
- 註解會說謊（與程式碼不同步）
- 程式碼應該自我說明
- 死碼造成混淆

**重構手法：**
- 提取方法（名稱解釋功能）
- 重新命名（不需註解的清晰度）
- 移除被註解的程式碼
- 引入斷言

**好的 vs 不好的註解：**
```javascript
// BAD: Explaining what
// Loop through users and check if active
for (const user of users) {
  if (user.status === 'active') { }
}

// GOOD: Explaining why
// Active users only - inactive are handled by cleanup job
const activeUsers = users.filter(u => u.isActive);
```

---

### 重複程式碼

**徵兆：**
- 多處有相同的程式碼
- 類似的程式碼有小差異
- 複製貼上的模式

**為什麼不好：**
- 修復 bug 需要在多處修改
- 不一致的風險
- 膨脹的程式碼庫

**重構手法：**
- 提取方法
- 提取類別
- 提升方法（在層級中）
- 形成模板方法

**偵測規則：**
任何重複 3 次以上的程式碼應該被提取。

---

### 冗贅類別

**徵兆：**
- 類別做的事不足以證明其存在
- 無附加值的包裝器
- 過度工程化的結果

**為什麼不好：**
- 維護開銷
- 不必要的間接層
- 無益的複雜性

**重構手法：**
- 內聯類別
- 摺疊層級

---

### 死碼

**徵兆：**
- 不可達的程式碼
- 未使用的變數/方法/類別
- 被註解掉的程式碼
- 不可能條件後的程式碼

**為什麼不好：**
- 混淆
- 維護負擔
- 減慢理解速度

**重構手法：**
- 移除死碼
- 安全刪除

**偵測：**
```bash
# Look for unused exports
# Look for unreferenced functions
# IDE "unused" warnings
```

---

### 投機性通用化

**徵兆：**
- 只有一個子類別的抽象類別
- 「為未來使用」的未使用參數
- 僅委派的方法
- 只有一個使用案例的「框架」

**為什麼不好：**
- 無益的複雜性
- YAGNI（You Ain't Gonna Need It — 你不會需要它）
- 更難理解

**重構手法：**
- 摺疊層級
- 內聯類別
- 移除參數
- 重新命名方法

---

## 耦合器

代表類別間過度耦合的壞味道。

### 依戀情結

**徵兆：**
- 方法使用另一個類別的資料多於自己的
- 對另一個物件有許多 getter 呼叫
- 資料和行為被分離

**為什麼不好：**
- 行為放在錯誤的位置
- 封裝不佳
- 難以維護

**重構手法：**
- 搬移方法
- 搬移欄位
- 提取方法（然後搬移）

**範例（重構前）：**
```javascript
class Order {
  getDiscountedPrice(customer) {
    // Uses customer data heavily
    if (customer.loyaltyYears > 5) {
      return this.price * customer.discountRate;
    }
    return this.price;
  }
}
```

**範例（重構後）：**
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

### 不當親密關係

**徵兆：**
- 類別存取彼此的私有部分
- 雙向引用
- 子類別對父類別知道太多

**為什麼不好：**
- 高耦合
- 變更會串聯
- 難以單獨修改

**重構手法：**
- 搬移方法
- 搬移欄位
- 將雙向改為單向
- 提取類別
- 隱藏委派

---

### 訊息鏈

**徵兆：**
- 長串的方法呼叫鏈：`a.getB().getC().getD().getValue()`
- 客戶端依賴導航結構
- 「火車事故」程式碼

**為什麼不好：**
- 脆弱 — 任何變更都會破壞鏈
- 違反迪米特法則
- 與結構耦合

**重構手法：**
- 隱藏委派
- 提取方法
- 搬移方法

**範例：**
```javascript
// Bad: Message chain
const managerName = employee.getDepartment().getManager().getName();

// Better: Hide delegation
const managerName = employee.getManagerName();
```

---

### 中間人

**徵兆：**
- 類別僅委派給另一個類別
- 一半的方法是委派
- 無附加值

**為什麼不好：**
- 不必要的間接層
- 維護開銷
- 令人困惑的架構

**重構手法：**
- 移除中間人
- 內聯方法

---

## 壞味道嚴重度指南

| 嚴重度 | 描述 | 動作 |
|----------|-------------|--------|
| **Critical** | 阻擋開發、導致 bug | 立即修復 |
| **High** | 顯著的維護負擔 | 在目前 sprint 修復 |
| **Medium** | 明顯但可管理 | 計畫在近期修復 |
| **Low** | 輕微不便 | 有機會時修復 |

---

## 快速偵測清單

掃描程式碼時使用此清單：

- [ ] 有方法超過 30 行嗎？
- [ ] 有類別超過 300 行嗎？
- [ ] 有方法超過 4 個參數嗎？
- [ ] 有重複的程式碼區塊嗎？
- [ ] 有基於型別代碼的 switch/case 嗎？
- [ ] 有未使用的程式碼嗎？
- [ ] 有方法大量使用另一個類別的資料嗎？
- [ ] 有長串的方法呼叫鏈嗎？
- [ ] 有解釋「什麼」而非「為什麼」的註解嗎？
- [ ] 有應該是物件的基本型別嗎？

---

## 延伸閱讀

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- Kerievsky, J. (2004). *Refactoring to Patterns*
- Feathers, M. (2004). *Working Effectively with Legacy Code*
