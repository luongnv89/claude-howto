<!-- i18n-source: 03-skills/refactor/references/refactoring-catalog.md -->
<!-- i18n-source-sha: 245272f -->
<!-- i18n-date: 2026-04-27 -->

# リファクタリングカタログ

Martin Fowler 著『Refactoring』(第 2 版) から厳選したリファクタリング技法のカタログである。各リファクタリングには動機、手順、例を掲載している。

> 「リファクタリングは、その手順、すなわち変更を実施するための正確なステップ列によって定義される。」 — Martin Fowler

---

## このカタログの使い方

1. コードスメルのリファレンスを使って **コードスメルを特定する**
2. このカタログから **対応するリファクタリングを探す**
3. **手順に沿って一段ずつ進める**
4. **各ステップごとにテスト** を実行し、振る舞いが保たれていることを確認する

**鉄則**: ある手順に 10 分以上かかるのであれば、もっと小さなステップに分割すること。

---

## 最も頻出するリファクタリング

### メソッドの抽出 (Extract Method)

**使う場面**: 長いメソッド、重複コード、概念に名前を付けたいとき

**動機**: コード片を、目的を表す名前を持つメソッドに切り出す。

**手順**:
1. やっていること(どうやってではなく)にちなんだ名前で新しいメソッドを作成する
2. コード片を新しいメソッドへコピーする
3. コード片で使われているローカル変数を洗い出す
4. ローカル変数をパラメータとして渡す(あるいはメソッド内で宣言する)
5. 戻り値を適切に処理する
6. 元のコード片を新しいメソッドの呼び出しに置き換える
7. テストする

**Before**:
```javascript
function printOwing(invoice) {
  let outstanding = 0;

  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");

  // 未払額の計算
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // 詳細の出力
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

**After**:
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

### メソッドのインライン化 (Inline Method)

**使う場面**: メソッド本体が名前と同じくらい明快な場合、過度な委譲が見られる場合

**動機**: メソッドが価値を加えていない場合、不要な間接参照を取り除く。

**手順**:
1. メソッドがポリモーフィックでないことを確認する
2. メソッドの呼び出し箇所をすべて見つける
3. 各呼び出しをメソッド本体で置き換える
4. 置き換えるたびにテストする
5. メソッド定義を削除する

**Before**:
```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**After**:
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### 変数の抽出 (Extract Variable)

**使う場面**: 複雑で理解しづらい式があるとき

**動機**: 複雑な式の一部に名前を付ける。

**手順**:
1. 式に副作用がないことを確認する
2. イミュータブルな変数を宣言する
3. 式(または式の一部)の結果をその変数に代入する
4. 元の式を変数で置き換える
5. テストする

**Before**:
```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**After**:
```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### 変数のインライン化 (Inline Variable)

**使う場面**: 変数名が式以上の情報を伝えていないとき

**動機**: 不要な間接参照を取り除く。

**手順**:
1. 右辺に副作用がないことを確認する
2. 変数がイミュータブルでなければイミュータブルにし、テストする
3. 最初の参照箇所を見つけて式で置き換える
4. テストする
5. すべての参照箇所について繰り返す
6. 宣言と代入を削除する
7. テストする

---

### 変数名の変更 (Rename Variable)

**使う場面**: 名前が目的を明確に伝えていないとき

**動機**: クリーンなコードには良い名前が不可欠である。

**手順**:
1. 変数が広く使われている場合は、カプセル化を検討する
2. すべての参照箇所を見つける
3. 各参照箇所を変更する
4. テストする

**Tips**:
- 意図を明らかにする名前を使う
- 略語を避ける
- ドメイン用語を用いる

```javascript
// 悪い例
const d = 30;
const x = users.filter(u => u.a);

// 良い例
const daysSinceLastLogin = 30;
const activeUsers = users.filter(user => user.isActive);
```

---

### 関数宣言の変更 (Change Function Declaration)

**使う場面**: 関数名が目的を表していない、パラメータの変更が必要な場合

**動機**: 良い関数名はコードを自己説明的にする。

**手順 (シンプル版)**:
1. 不要なパラメータを削除する
2. 名前を変更する
3. 必要なパラメータを追加する
4. テストする

**手順 (マイグレーション版 — 複雑な変更向け)**:
1. パラメータを削除する場合、それが使われていないことを確認する
2. 望ましい宣言の新しい関数を作成する
3. 古い関数から新しい関数を呼び出すようにする
4. テストする
5. 呼び出し側を新しい関数を使うように変更する
6. 各変更後にテストする
7. 古い関数を削除する

**Before**:
```javascript
function circum(radius) {
  return 2 * Math.PI * radius;
}
```

**After**:
```javascript
function circumference(radius) {
  return 2 * Math.PI * radius;
}
```

---

### 変数のカプセル化 (Encapsulate Variable)

**使う場面**: データに複数箇所から直接アクセスしているとき

**動機**: データ操作のための明確なアクセスポイントを提供する。

**手順**:
1. getter と setter 関数を作成する
2. すべての参照箇所を見つける
3. 読み取りを getter で置き換える
4. 書き込みを setter で置き換える
5. 各変更後にテストする
6. 変数の可視性を制限する

**Before**:
```javascript
let defaultOwner = { firstName: "Martin", lastName: "Fowler" };

// 多くの場所で利用される
spaceship.owner = defaultOwner;
```

**After**:
```javascript
let defaultOwnerData = { firstName: "Martin", lastName: "Fowler" };

function defaultOwner() { return defaultOwnerData; }
function setDefaultOwner(arg) { defaultOwnerData = arg; }

spaceship.owner = defaultOwner();
```

---

### パラメータオブジェクトの導入 (Introduce Parameter Object)

**使う場面**: いくつかのパラメータがしばしばまとまって登場する場合

**動機**: 自然にまとまるべきデータをグループ化する。

**手順**:
1. グループ化したパラメータ用の新しいクラス/構造体を作成する
2. テストする
3. 「関数宣言の変更」で新しいオブジェクトを追加する
4. テストする
5. グループ内の各パラメータについて、関数から取り除き新しいオブジェクトを使うようにする
6. 各変更後にテストする

**Before**:
```javascript
function amountInvoiced(startDate, endDate) { ... }
function amountReceived(startDate, endDate) { ... }
function amountOverdue(startDate, endDate) { ... }
```

**After**:
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

### 関数群のクラス化 (Combine Functions into Class)

**使う場面**: 複数の関数が同じデータを操作している場合

**動機**: 関数を、それらが操作するデータと共にまとめる。

**手順**:
1. 共通データに「レコードのカプセル化 (Encapsulate Record)」を適用する
2. 各関数をクラス内に移動する
3. 移動するたびにテストする
4. データ引数をクラスのフィールド利用に置き換える

**Before**:
```javascript
function base(reading) { ... }
function taxableCharge(reading) { ... }
function calculateBaseCharge(reading) { ... }
```

**After**:
```javascript
class Reading {
  constructor(data) { this._data = data; }

  get base() { ... }
  get taxableCharge() { ... }
  get calculateBaseCharge() { ... }
}
```

---

### 段階の分割 (Split Phase)

**使う場面**: コードが 2 つの異なる事柄を扱っている場合

**動機**: コードを明確な境界を持つ別々のフェーズに分離する。

**手順**:
1. 第 2 フェーズ用の関数を作成する
2. テストする
3. フェーズ間の中間データ構造を導入する
4. テストする
5. 第 1 フェーズを独立した関数として抽出する
6. テストする

**Before**:
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

**After**:
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

## 機能の移動

### メソッドの移動 (Move Method)

**使う場面**: メソッドが自分のクラスより他のクラスの機能を多く使っている場合

**動機**: 関数を、最もよく利用するデータの近くに置く。

**手順**:
1. 自クラス内でメソッドが利用しているプログラム要素をすべて調べる
2. メソッドがポリモーフィックかどうか確認する
3. 移動先クラスにメソッドをコピーする
4. 新しいコンテキストに合わせて調整する
5. 元のメソッドが移動先に委譲するようにする
6. テストする
7. 元のメソッドの削除を検討する

---

### フィールドの移動 (Move Field)

**使う場面**: フィールドが他のクラスでより多く使われている場合

**動機**: データを、それを使う関数と共に保持する。

**手順**:
1. まだの場合はフィールドをカプセル化する
2. テストする
3. 移動先にフィールドを作成する
4. 参照箇所を移動先のフィールドを使うように更新する
5. テストする
6. 元のフィールドを削除する

---

### 関数への文の移動 (Move Statements into Function)

**使う場面**: 同じコードが必ずある関数呼び出しと一緒に現れる場合

**動機**: 繰り返しコードを関数内に移動して重複を取り除く。

**手順**:
1. まだの場合は繰り返しコードを関数として抽出する
2. その関数の中に文を移動する
3. テストする
4. 呼び出し側で単独の文が不要になったら削除する

---

### 呼び出し側への文の移動 (Move Statements to Callers)

**使う場面**: 共通の振る舞いが呼び出し側ごとに異なる場合

**動機**: 振る舞いを変える必要があるなら、関数の外に移す。

**手順**:
1. 移動するコードに「メソッドの抽出」を適用する
2. 元の関数に「メソッドのインライン化」を適用する
3. インライン化された呼び出しを削除する
4. 抽出したコードを各呼び出し側に移動する
5. テストする

---

## データの再編成

### プリミティブをオブジェクトで置き換える (Replace Primitive with Object)

**使う場面**: データ項目に単純な値以上の振る舞いが必要な場合

**動機**: データを振る舞いと共にカプセル化する。

**手順**:
1. 「変数のカプセル化」を適用する
2. シンプルな値クラスを作成する
3. setter を新しいインスタンス生成に変更する
4. getter を値の返却に変更する
5. テストする
6. 新しいクラスにより豊かな振る舞いを追加する

**Before**:
```javascript
class Order {
  constructor(data) {
    this.priority = data.priority; // 文字列: "high"、"rush" など
  }
}

// 利用箇所
if (order.priority === "high" || order.priority === "rush") { ... }
```

**After**:
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

// 利用箇所
if (order.priority.higherThan(new Priority("normal"))) { ... }
```

---

### 一時変数を問い合わせで置き換える (Replace Temp with Query)

**使う場面**: 一時変数が式の結果を保持している場合

**動機**: 式を関数として切り出すことでコードを明快にする。

**手順**:
1. 変数が一度だけ代入されていることを確認する
2. 代入の右辺をメソッドとして抽出する
3. 一時変数の参照箇所をメソッド呼び出しで置き換える
4. テストする
5. 一時変数の宣言と代入を削除する

**Before**:
```javascript
const basePrice = this._quantity * this._itemPrice;
if (basePrice > 1000) {
  return basePrice * 0.95;
} else {
  return basePrice * 0.98;
}
```

**After**:
```javascript
get basePrice() {
  return this._quantity * this._itemPrice;
}

// メソッド内
if (this.basePrice > 1000) {
  return this.basePrice * 0.95;
} else {
  return this.basePrice * 0.98;
}
```

---

## 条件記述の単純化

### 条件記述の分解 (Decompose Conditional)

**使う場面**: 複雑な条件分岐 (if-then-else) があるとき

**動機**: 条件と動作を抽出して意図を明確にする。

**手順**:
1. 条件部分に「メソッドの抽出」を適用する
2. then 節に「メソッドの抽出」を適用する
3. else 節 (もしあれば) に「メソッドの抽出」を適用する

**Before**:
```javascript
if (!aDate.isBefore(plan.summerStart) && !aDate.isAfter(plan.summerEnd)) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}
```

**After**:
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

### 条件式の統合 (Consolidate Conditional Expression)

**使う場面**: 同じ結果を返す条件が複数あるとき

**動機**: それらの条件が単一のチェックであることを明らかにする。

**手順**:
1. 条件に副作用がないことを確認する
2. 条件を `and` または `or` で結合する
3. 結合した条件に「メソッドの抽出」を検討する

**Before**:
```javascript
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;
```

**After**:
```javascript
if (isNotEligibleForDisability(employee)) return 0;

function isNotEligibleForDisability(employee) {
  return employee.seniority < 2 ||
         employee.monthsDisabled > 12 ||
         employee.isPartTime;
}
```

---

### ガード節による入れ子の条件記述の置き換え (Replace Nested Conditional with Guard Clauses)

**使う場面**: 入れ子の条件分岐が深く、流れを追いにくいとき

**動機**: 特殊ケースにガード節を使い、通常フローを明確に保つ。

**手順**:
1. 特殊ケースの条件を見つける
2. それらを早期 return するガード節で置き換える
3. 各変更後にテストする

**Before**:
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

**After**:
```javascript
function payAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reasonCode: "SEP" };
  if (employee.isRetired) return { amount: 0, reasonCode: "RET" };
  return calculateNormalPay(employee);
}
```

---

### ポリモーフィズムによる条件記述の置き換え (Replace Conditional with Polymorphism)

**使う場面**: 型に基づく switch/case、型ごとに変化する条件ロジック

**動機**: オブジェクト自身に振る舞いを担わせる。

**手順**:
1. クラス階層を作成する (なければ)
2. オブジェクト生成にファクトリ関数を使う
3. 条件ロジックをスーパークラスのメソッドに移す
4. ケースごとにサブクラスのメソッドを作成する
5. 元の条件記述を削除する

**Before**:
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

**After**:
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

### 特殊ケースの導入 (Introduce Special Case / Null Object)

**使う場面**: 特殊ケースに対する null チェックが繰り返される場合

**動機**: 特殊ケースを処理する特殊オブジェクトを返す。

**手順**:
1. 期待されるインターフェースを持つ特殊ケースクラスを作成する
2. isSpecialCase チェックを追加する
3. ファクトリメソッドを導入する
4. null チェックを特殊ケースオブジェクトの利用で置き換える
5. テストする

**Before**:
```javascript
const customer = site.customer;
// ... 多数の箇所でチェック
if (customer === "unknown") {
  customerName = "occupant";
} else {
  customerName = customer.name;
}
```

**After**:
```javascript
class UnknownCustomer {
  get name() { return "occupant"; }
  get billingPlan() { return registry.defaultPlan; }
}

// ファクトリメソッド
function customer(site) {
  return site.customer === "unknown"
    ? new UnknownCustomer()
    : site.customer;
}

// 利用箇所 — null チェック不要
const customerName = customer.name;
```

---

## API のリファクタリング

### 問い合わせと変更の分離 (Separate Query from Modifier)

**使う場面**: 関数が値を返すと同時に副作用も持つ場合

**動機**: どの操作に副作用があるのかを明確にする。

**手順**:
1. 新しい問い合わせ関数を作成する
2. 元の関数の戻り値ロジックをコピーする
3. 元の関数を void を返すように変更する
4. 戻り値を使っていた呼び出しを置き換える
5. テストする

**Before**:
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

**After**:
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

### 関数のパラメータ化 (Parameterize Function)

**使う場面**: 似たような処理を異なる値で行う関数が複数あるとき

**動機**: パラメータを追加することで重複を取り除く。

**手順**:
1. 一つの関数を選ぶ
2. 変動するリテラル用のパラメータを追加する
3. 本体をそのパラメータを使うように変更する
4. テストする
5. 呼び出し側をパラメータ化された版を使うように変更する
6. 不要になった関数を削除する

**Before**:
```javascript
function tenPercentRaise(person) {
  person.salary = person.salary * 1.10;
}

function fivePercentRaise(person) {
  person.salary = person.salary * 1.05;
}
```

**After**:
```javascript
function raise(person, factor) {
  person.salary = person.salary * (1 + factor);
}

// 利用箇所
raise(person, 0.10);
raise(person, 0.05);
```

---

### フラグ引数の削除 (Remove Flag Argument)

**使う場面**: 関数の振る舞いを切り替えるブール型パラメータがある場合

**動機**: 別々の関数を通して振る舞いを明示的にする。

**手順**:
1. フラグの値ごとに明示的な関数を作成する
2. 各呼び出しを適切な新しい関数で置き換える
3. 各変更後にテストする
4. 元の関数を削除する

**Before**:
```javascript
function bookConcert(customer, isPremium) {
  if (isPremium) {
    // プレミアム予約のロジック
  } else {
    // 通常予約のロジック
  }
}

bookConcert(customer, true);
bookConcert(customer, false);
```

**After**:
```javascript
function bookPremiumConcert(customer) {
  // プレミアム予約のロジック
}

function bookRegularConcert(customer) {
  // 通常予約のロジック
}

bookPremiumConcert(customer);
bookRegularConcert(customer);
```

---

## 継承の取り扱い

### メソッドの引き上げ (Pull Up Method)

**使う場面**: 同じメソッドが複数のサブクラスにあるとき

**動機**: クラス階層内の重複を取り除く。

**手順**:
1. メソッド同士が同一であることを確認する
2. シグネチャが同じであることを確認する
3. スーパークラスに新しいメソッドを作成する
4. 一つのサブクラスから本体をコピーする
5. 一つのサブクラスからメソッドを削除し、テストする
6. 他のサブクラスのメソッドも順次削除し、その都度テストする

---

### メソッドの押し下げ (Push Down Method)

**使う場面**: サブクラスの一部のみに関係する振る舞いがあるとき

**動機**: メソッドを使われる場所に置く。

**手順**:
1. メソッドを必要とする各サブクラスにコピーする
2. スーパークラスからメソッドを削除する
3. テストする
4. 必要としないサブクラスからは削除する
5. テストする

---

### サブクラスを委譲で置き換える (Replace Subclass with Delegate)

**使う場面**: 継承が誤って使われている、もしくはより柔軟性が必要な場合

**動機**: 適切な場面では継承よりコンポジションを優先する。

**手順**:
1. 委譲先用の空クラスを作成する
2. 委譲先を保持するフィールドをホストクラスに追加する
3. ホストから呼ばれる委譲先のコンストラクタを作成する
4. 機能を委譲先へ移動する
5. 移動するたびにテストする
6. 継承を委譲で置き換える

---

## クラスの抽出 (Extract Class)

**使う場面**: 複数の責務を持つ大きなクラスがあるとき

**動機**: クラスを分割して単一責務を保つ。

**手順**:
1. 責務をどう分けるか決める
2. 新しいクラスを作成する
3. フィールドを元のクラスから新しいクラスへ移動する
4. テストする
5. メソッドを元のクラスから新しいクラスへ移動する
6. 移動するたびにテストする
7. 両クラスを見直して必要なら名前を変更する
8. 新しいクラスをどう公開するかを決める

**Before**:
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

**After**:
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

## クイックリファレンス: スメルからリファクタリングへ

| コードスメル | 主なリファクタリング | 代替 |
|------------|-------------------|-------------|
| 長すぎるメソッド (Long Method) | メソッドの抽出 | 一時変数を問い合わせで置き換える |
| 重複コード (Duplicate Code) | メソッドの抽出 | メソッドの引き上げ |
| 大きすぎるクラス (Large Class) | クラスの抽出 | サブクラスの抽出 |
| 長すぎるパラメータリスト (Long Parameter List) | パラメータオブジェクトの導入 | オブジェクトそのものの受け渡し |
| 機能の横恋慕 (Feature Envy) | メソッドの移動 | メソッドの抽出 + 移動 |
| データのかたまり (Data Clumps) | クラスの抽出 | パラメータオブジェクトの導入 |
| プリミティブ依存症 (Primitive Obsession) | プリミティブをオブジェクトで置き換える | タイプコードの置き換え |
| switch 文 (Switch Statements) | ポリモーフィズムによる条件記述の置き換え | タイプコードの置き換え |
| 一時的属性 (Temporary Field) | クラスの抽出 | Null オブジェクトの導入 |
| メッセージの連鎖 (Message Chains) | 委譲の隠蔽 | メソッドの抽出 |
| 仲介人 (Middle Man) | 中間者の除去 | メソッドのインライン化 |
| 変更の分散 (Divergent Change) | クラスの抽出 | 段階の分割 |
| 散弾銃手術 (Shotgun Surgery) | メソッドの移動 | クラスのインライン化 |
| 死せるコード (Dead Code) | 死せるコードの除去 | - |
| 投機的一般性 (Speculative Generality) | 階層の平坦化 | クラスのインライン化 |

---

## 参考文献

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- オンラインカタログ: https://refactoring.com/catalog/
