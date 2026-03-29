# 程式碼審查發現模板

在程式碼審查中記錄每個發現的問題時使用此模板。

---

## 問題：[標題]

### 嚴重度
- [ ] Critical（阻擋部署）
- [ ] High（合併前應修復）
- [ ] Medium（應盡快修復）
- [ ] Low（改善建議）

### 類別
- [ ] 安全性
- [ ] 效能
- [ ] 程式碼品質
- [ ] 可維護性
- [ ] 測試
- [ ] 設計模式
- [ ] 文件

### 位置
**檔案：** `src/components/UserCard.tsx`

**行號：** 45-52

**函式/方法：** `renderUserDetails()`

### 問題描述

**什麼：** 描述問題是什麼。

**為什麼重要：** 解釋影響以及為什麼需要修復。

**目前行為：** 展示有問題的程式碼或行為。

**預期行為：** 描述應該發生什麼。

### 程式碼範例

#### 目前（有問題的）

```typescript
// Shows the N+1 query problem
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // Query per user!
  renderUserPosts(posts);
});
```

#### 建議修復

```typescript
// Optimized with JOIN query
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### 影響分析

| 面向 | 影響 | 嚴重度 |
|--------|--------|----------|
| 效能 | 20 個使用者需要 100+ 個查詢 | High |
| 使用者體驗 | 頁面載入緩慢 | High |
| 可擴展性 | 在大規模時崩潰 | Critical |
| 可維護性 | 難以除錯 | Medium |

### 相關問題

- `AdminUserList.tsx` 第 120 行有類似問題
- 相關 PR：#456
- 相關 issue：#789

### 額外資源

- [N+1 查詢問題](https://en.wikipedia.org/wiki/N%2B1_problem)
- [資料庫 Join 文件](https://docs.example.com/joins)
- [效能最佳化指南](./docs/performance.md)

### 審查者備註

- 這是此程式碼庫中的常見模式
- 考慮將此加入程式碼風格指南
- 可能值得建立一個輔助函式

### 作者回覆（用於回饋）

*由程式碼作者填寫：*

- [ ] 修復已在提交中實作：`abc123`
- [ ] 修復狀態：完成 / 進行中 / 需要討論
- [ ] 問題或疑慮：（描述）

---

## 發現統計（供審查者）

審查多個發現時，追蹤：

- **發現的問題總數：** X
- **Critical：** X
- **High：** X
- **Medium：** X
- **Low：** X

**建議：** ✅ 核准 / ⚠️ 請求變更 / 🔄 需要討論

**整體程式碼品質：** 1-5 星
