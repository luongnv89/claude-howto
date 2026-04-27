<!-- i18n-source: 03-skills/refactor/references/code-smells.md -->
<!-- i18n-source-sha: 245272f -->
<!-- i18n-date: 2026-04-27 -->
# コードスメルカタログ

Martin Fowler 著『Refactoring』(第 2 版) に基づく、コードスメルの包括的なリファレンスである。コードスメルはより深い問題の症状であり、コード設計に何か問題がある可能性を示す指標となる。

> "A code smell is a surface indication that usually corresponds to a deeper problem in the system." — Martin Fowler

---

## Bloaters（肥満児）

効果的に扱うには大きくなりすぎたものを表すコードスメル群である。

### Long Method（長すぎる関数）

**兆候:**
- メソッドが 30〜50 行を超える
- メソッド全体を見るのにスクロールが必要
- ネストが多重になっている
- セクションごとに何をしているかを説明するコメントがある

**なぜ悪いか:**
- 理解しづらい
- 単独でテストするのが難しい
- 変更が予期しない影響を及ぼす
- 内部に重複ロジックが隠れる

**リファクタリング:**
- メソッドの抽出
- Replace Temp with Query
- パラメータオブジェクトの導入
- Replace Method with Method Object
- 条件記述の分解

**例（Before）:**
```javascript
function processOrder(order) {
  // 注文の検証 (20 行)
  if (!order.items) throw new Error('No items');
  if (order.items.length === 0) throw new Error('Empty order');
  // ... さらに検証

  // 合計金額の計算 (30 行)
  let subtotal = 0;
  for (const item of order.items) {
    subtotal += item.price * item.quantity;
  }
  // ... 税、送料、割引

  // 通知の送信 (20 行)
  // ... メール送信ロジック
}
```

**例（After）:**
```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  sendOrderNotifications(order, totals);
  return { order, totals };
}
```

---

### Large Class（巨大なクラス）

**兆候:**
- クラスのインスタンス変数が多い(7〜10 個超)
- クラスのメソッドが多い(15〜20 個超)
- クラス名が漠然としている(Manager、Handler、Processor)
- 全インスタンス変数を使わないメソッドがある

**なぜ悪いか:**
- 単一責任原則に違反する
- テストが困難
- 変更が無関係な機能にも波及する
- 部分的な再利用が難しい

**リファクタリング:**
- クラスの抽出
- Extract Subclass
- Extract Interface

**検出基準:**
```
コード行数 > 300
メソッド数 > 15
フィールド数 > 10
```

---

### Primitive Obsession（プリミティブ型への執着）

**兆候:**
- ドメイン概念にプリミティブを使う(メールに string、金額に int)
- オブジェクトでなくプリミティブの配列を使う
- タイプコードに文字列定数を使う
- マジックナンバーやマジックストリング

**なぜ悪いか:**
- 型レベルでの検証ができない
- ロジックがコードベース全体に散らばる
- 誤った値を渡しやすい
- ドメイン概念が欠落する

**リファクタリング:**
- Replace Primitive with Object
- Replace Type Code with Class
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**例（Before）:**
```javascript
const user = {
  email: 'john@example.com',     // 単なる文字列
  phone: '1234567890',           // 単なる文字列
  status: 'active',              // マジックストリング
  balance: 10050                 // セント単位の整数
};
```

**例（After）:**
```javascript
const user = {
  email: new Email('john@example.com'),
  phone: new PhoneNumber('1234567890'),
  status: UserStatus.ACTIVE,
  balance: Money.cents(10050)
};
```

---

### Long Parameter List（長すぎるパラメータリスト）

**兆候:**
- パラメータが 4 個以上のメソッド
- 常に一緒に現れるパラメータ
- メソッドの振る舞いを切り替える真偽値フラグ
- null/undefined が頻繁に渡される

**なぜ悪いか:**
- 正しく呼び出すのが難しい
- 引数順序の混乱を招く
- メソッドが多くを抱え込んでいるサイン
- パラメータの追加が難しい

**リファクタリング:**
- パラメータオブジェクトの導入
- Preserve Whole Object
- Replace Parameter with Method Call
- Remove Flag Argument

**例（Before）:**
```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy) {
  // ...
}
```

**例（After）:**
```javascript
function createUser(personalInfo, address, options) {
  // personalInfo: { firstName, lastName, email, phone }
  // address: { street, city, state, zip }
  // options: { isAdmin, isActive, createdBy }
}
```

---

### Data Clumps（データの群れ）

**兆候:**
- 同じ 3 個以上のフィールドが繰り返し一緒に現れる
- 常に一緒に渡されるパラメータ群
- 一塊として属するべきフィールド集合を持つクラス

**なぜ悪いか:**
- 取り扱いロジックが重複する
- 抽象化が欠けている
- 拡張しづらい
- 隠れたクラスの存在を示す

**リファクタリング:**
- クラスの抽出
- パラメータオブジェクトの導入
- Preserve Whole Object

**例:**
```javascript
// データの群れ: (x, y, z) 座標
function movePoint(x, y, z, dx, dy, dz) { }
function scalePoint(x, y, z, factor) { }
function distanceBetween(x1, y1, z1, x2, y2, z2) { }

// Point3D クラスを抽出
class Point3D {
  constructor(x, y, z) { }
  move(delta) { }
  scale(factor) { }
  distanceTo(other) { }
}
```

---

## Object-Orientation Abusers（オブジェクト指向の濫用者）

オブジェクト指向の原則を不完全または誤って使っていることを示すスメル群である。

### Switch Statements（スイッチ文）

**兆候:**
- 長い switch/case や if/else の連鎖
- 同じ switch が複数箇所に存在
- タイプコードに対する switch
- 新ケース追加で各所を変更する必要がある

**なぜ悪いか:**
- 開放閉鎖原則に違反する
- 全ての switch 箇所に変更が波及する
- 拡張が困難
- ポリモーフィズム不在のサインであることが多い

**リファクタリング:**
- ポリモーフィズムによる条件記述の置き換え
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**例（Before）:**
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

**例（After）:**
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

### Temporary Field（一時的フィールド）

**兆候:**
- 一部のメソッドでのみ使用されるインスタンス変数
- 条件付きで設定されるフィールド
- 特定ケースのために複雑な初期化を要する

**なぜ悪いか:**
- 紛らわしい - フィールドが存在するが null の場合がある
- オブジェクトの状態が理解しづらい
- 隠れた条件分岐ロジックを示す

**リファクタリング:**
- クラスの抽出
- Introduce Null Object
- Replace Temp Field with Local

---

### Refused Bequest（相続拒否）

**兆候:**
- サブクラスが継承したメソッド/データを使わない
- サブクラスがオーバーライドして何もしない
- IS-A 関係ではなくコード再利用目的の継承

**なぜ悪いか:**
- 抽象化が誤っている
- リスコフの置換原則に違反する
- 階層が誤解を招く

**リファクタリング:**
- Push Down Method/Field
- Replace Subclass with Delegate
- Replace Inheritance with Delegation

---

### Alternative Classes with Different Interfaces（異なるインターフェイスの代替クラス）

**兆候:**
- 似たことをする 2 つのクラス
- 同じ概念に異なるメソッド名を使っている
- 互いに置換可能だが共通インターフェイスがない

**なぜ悪いか:**
- 実装が重複する
- 共通インターフェイスがない
- 切り替えが難しい

**リファクタリング:**
- Rename Method
- Move Method
- Extract Superclass
- Extract Interface

---

## Change Preventers（変更の妨げ）

変更を困難にするスメル群 - ある変更のために他の多くを変える必要が生じる。

### Divergent Change（変更の発散）

**兆候:**
- 1 つのクラスが異なる複数の理由で変更される
- 異なる領域の変更が同じクラスへの編集を引き起こす
- そのクラスは「神クラス」化している

**なぜ悪いか:**
- 単一責任原則に違反する
- 変更頻度が高くなる
- マージコンフリクトを招く

**リファクタリング:**
- クラスの抽出
- Extract Superclass
- Extract Subclass

**例:**
`User` クラスが次の理由で変更される:
- 認証の変更
- プロフィールの変更
- 課金の変更
- 通知の変更

→ 抽出: `AuthService`、`ProfileService`、`BillingService`、`NotificationService`

---

### Shotgun Surgery（散弾銃手術）

**兆候:**
- 1 つの変更で多くのクラスへの編集が必要
- 小さな機能でも 10 ファイル以上に手を入れる
- 変更箇所が散在し、すべてを見つけにくい

**なぜ悪いか:**
- 修正漏れが起きやすい
- 結合度が高い
- 変更がエラーを誘発しやすい

**リファクタリング:**
- Move Method
- Move Field
- Inline Class

**検出基準:**
1 フィールドの追加で 5 ファイル以上の変更が必要かを確認する。

---

### Parallel Inheritance Hierarchies（並行継承階層）

**兆候:**
- 一方の階層にサブクラスを作ると、もう一方にも作る必要がある
- クラス名のプレフィックスが揃っている(例: `DatabaseOrder`、`DatabaseProduct`)

**なぜ悪いか:**
- 保守コストが倍になる
- 階層間の結合度が高い
- 片側を忘れやすい

**リファクタリング:**
- Move Method
- Move Field
- 一方の階層を削除する

---

## Dispensables（不要物）

不要であり削除すべきものを表すスメル群である。

### Comments（過剰なコメント）

**兆候:**
- コードが何をしているかを説明するコメント
- コメントアウトされたコード
- 永遠に残る TODO/FIXME
- 言い訳のコメント

**なぜ悪いか:**
- コメントは嘘をつく(コードと乖離する)
- コードは自己文書化されているべき
- 死んだコードは混乱を生む

**リファクタリング:**
- メソッドの抽出(名前で「何」を表す)
- Rename(コメントなしで明確化)
- コメントアウトされたコードの削除
- Introduce Assertion

**良いコメントと悪いコメント:**
```javascript
// 悪い: 「何」を説明している
// users をループしてアクティブかどうか確認
for (const user of users) {
  if (user.status === 'active') { }
}

// 良い: 「なぜ」を説明している
// アクティブなユーザーのみ。非アクティブはクリーンアップジョブで処理される
const activeUsers = users.filter(u => u.isActive);
```

---

### Duplicate Code（重複したコード）

**兆候:**
- 同じコードが複数箇所にある
- わずかな違いだけの似たコード
- コピペのパターン

**なぜ悪いか:**
- バグ修正を複数箇所で行う必要がある
- 不整合のリスク
- コードベースが肥大化する

**リファクタリング:**
- メソッドの抽出
- クラスの抽出
- Pull Up Method(階層内)
- Form Template Method

**検出ルール:**
3 回以上重複するコードは抽出すべきである。

---

### Lazy Class（怠け者のクラス）

**兆候:**
- クラスが存在を正当化できるほど働いていない
- 付加価値のないラッパー
- 過剰設計の結果

**なぜ悪いか:**
- 保守オーバーヘッド
- 不要な間接参照
- メリットなき複雑さ

**リファクタリング:**
- Inline Class
- Collapse Hierarchy

---

### Dead Code（デッドコード）

**兆候:**
- 到達不能なコード
- 使われていない変数/メソッド/クラス
- コメントアウトされたコード
- 起こり得ない条件下にあるコード

**なぜ悪いか:**
- 混乱を招く
- 保守の負担
- 理解の速度を落とす

**リファクタリング:**
- デッドコードの削除
- Safe Delete

**検出基準:**
```bash
# 未使用のエクスポートを探す
# 参照されない関数を探す
# IDE の「未使用」警告を確認
```

---

### Speculative Generality（投機的一般化）

**兆候:**
- サブクラスが 1 つしかない抽象クラス
- 「将来のため」の未使用パラメータ
- 委譲のみのメソッド
- 1 用途しかない「フレームワーク」

**なぜ悪いか:**
- メリットなき複雑さ
- YAGNI(You Ain't Gonna Need It)
- 理解しづらい

**リファクタリング:**
- Collapse Hierarchy
- Inline Class
- Remove Parameter
- Rename Method

---

## Couplers（結合の問題）

クラス間の過剰な結合を表すスメル群である。

### Feature Envy（機能の横恋慕）

**兆候:**
- メソッドが自クラスより他クラスのデータを多く使う
- 他オブジェクトへの getter 呼び出しが多い
- データと振る舞いが分離している

**なぜ悪いか:**
- 振る舞いの置き場所が誤っている
- カプセル化が不十分
- 保守が難しい

**リファクタリング:**
- Move Method
- Move Field
- メソッドの抽出(その後 move)

**例（Before）:**
```javascript
class Order {
  getDiscountedPrice(customer) {
    // customer のデータを多く使っている
    if (customer.loyaltyYears > 5) {
      return this.price * customer.discountRate;
    }
    return this.price;
  }
}
```

**例（After）:**
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

### Inappropriate Intimacy（不適切な親密さ）

**兆候:**
- クラスが互いのプライベート部分にアクセスする
- 双方向の参照
- サブクラスが親について詳しすぎる

**なぜ悪いか:**
- 結合度が高い
- 変更が連鎖する
- 一方を変えると他方も変える必要がある

**リファクタリング:**
- Move Method
- Move Field
- Change Bidirectional to Unidirectional
- クラスの抽出
- Hide Delegate

---

### Message Chains（メッセージの連鎖）

**兆候:**
- メソッド呼び出しの長い連鎖: `a.getB().getC().getD().getValue()`
- クライアントがナビゲーション構造に依存している
- 「列車事故」コード

**なぜ悪いか:**
- 脆弱 - 連鎖中のいずれかが変わると壊れる
- デメテルの法則に違反する
- 構造への結合

**リファクタリング:**
- Hide Delegate
- メソッドの抽出
- Move Method

**例:**
```javascript
// 悪い: メッセージの連鎖
const managerName = employee.getDepartment().getManager().getName();

// 良い: 委譲を隠す
const managerName = employee.getManagerName();
```

---

### Middle Man（仲介人）

**兆候:**
- 他クラスへ委譲するだけのクラス
- メソッドの半数が委譲
- 付加価値がない

**なぜ悪いか:**
- 不要な間接参照
- 保守オーバーヘッド
- アーキテクチャが分かりにくい

**リファクタリング:**
- Remove Middle Man
- メソッドのインライン化

---

## スメル深刻度ガイド

| 深刻度 | 説明 | 対応 |
|----------|-------------|--------|
| **Critical** | 開発をブロックし、バグの原因となる | 直ちに修正 |
| **High** | 保守負担が大きい | 当該スプリント中に修正 |
| **Medium** | 目に付くが許容範囲 | 近い将来に計画 |
| **Low** | 軽微な不便 | 機会があれば修正 |

---

## 簡易検出チェックリスト

コードをスキャンする際に使うチェックリストである。

- [ ] 30 行を超えるメソッドはあるか?
- [ ] 300 行を超えるクラスはあるか?
- [ ] 4 個を超えるパラメータを持つメソッドはあるか?
- [ ] 重複したコードブロックはあるか?
- [ ] タイプコードに対する switch/case はあるか?
- [ ] 使われていないコードはあるか?
- [ ] 他クラスのデータを多く使っているメソッドはあるか?
- [ ] メソッド呼び出しの長い連鎖はあるか?
- [ ] 「なぜ」ではなく「何」を説明しているコメントはあるか?
- [ ] オブジェクト化すべきプリミティブはあるか?

---

## 参考文献

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- Kerievsky, J. (2004). *Refactoring to Patterns*
- Feathers, M. (2004). *Working Effectively with Legacy Code*
