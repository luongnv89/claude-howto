<!-- i18n-source: 03-skills/code-review/templates/finding-template.md -->
<!-- i18n-source-sha: 6d1e0ae -->
<!-- i18n-date: 2026-04-27 -->

# コードレビュー指摘事項テンプレート

コードレビュー中に見つけた各問題を文書化する際にこのテンプレートを使用する。

---

## Issue: [TITLE]

### 重要度
- [ ] Critical（デプロイをブロック）
- [ ] High（マージ前に修正すべき）
- [ ] Medium（早期に修正すべき）
- [ ] Low（あれば望ましい）

### カテゴリ
- [ ] Security
- [ ] Performance
- [ ] Code Quality
- [ ] Maintainability
- [ ] Testing
- [ ] Design Pattern
- [ ] Documentation

### 場所
**File:** `src/components/UserCard.tsx`

**Lines:** 45-52

**Function/Method:** `renderUserDetails()`

### 問題の説明

**What:** 問題の内容を記述する。

**Why it matters:** 影響と修正が必要な理由を説明する。

**Current behavior:** 問題のあるコードや挙動を示す。

**Expected behavior:** 代わりに期待される挙動を記述する。

### コード例

#### 現状（問題あり）

```typescript
// N+1 クエリ問題を示す
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // ユーザーごとにクエリ！
  renderUserPosts(posts);
});
```

#### 修正案

```typescript
// JOIN クエリで最適化
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### 影響分析

| Aspect | Impact | Severity |
|--------|--------|----------|
| Performance | 20 ユーザーで 100 件以上のクエリ | High |
| User Experience | ページ読み込みが遅い | High |
| Scalability | 規模拡大で破綻 | Critical |
| Maintainability | デバッグが困難 | Medium |

### 関連する問題

- `AdminUserList.tsx` 120 行目に類似の問題
- 関連 PR: #456
- 関連 issue: #789

### 追加リソース

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)

### レビュアーのメモ

- このコードベースでよく見られるパターンである
- コードスタイルガイドへの追加を検討する
- ヘルパー関数を作成する価値があるかもしれない

### 著者の応答（フィードバック用）

*コード作成者が記入する:*

- [ ] 修正実装コミット: `abc123`
- [ ] 修正状況: Complete / In Progress / Needs Discussion
- [ ] 質問や懸念: （記述）

---

## 指摘統計（レビュアー用）

複数の指摘をレビューする際は、以下を追跡する。

- **Total Issues Found:** X
- **Critical:** X
- **High:** X
- **Medium:** X
- **Low:** X

**Recommendation:** ✅ Approve / ⚠️ Request Changes / 🔄 Needs Discussion

**Overall Code Quality:** 1-5 stars
