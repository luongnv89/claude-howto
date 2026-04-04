# 代码审查问题记录模板

使用这个模板来记录代码审查中发现的每一个问题。

---

## 问题：[标题]

### 严重性
- [ ] Critical（阻塞发布）
- [ ] High（合并前应修复）
- [ ] Medium（尽快修复）
- [ ] Low（可选优化）

### 类别
- [ ] Security
- [ ] Performance
- [ ] Code Quality
- [ ] Maintainability
- [ ] Testing
- [ ] Design Pattern
- [ ] Documentation

### 位置
**文件：** `src/components/UserCard.tsx`

**行号：** 45-52

**函数 / 方法：** `renderUserDetails()`

### 问题描述

**是什么：** 描述这个问题是什么。

**为什么重要：** 说明影响，以及为什么需要修复。

**当前行为：** 展示有问题的代码或行为。

**期望行为：** 描述理想情况下应该发生什么。

### 代码示例

#### 当前（有问题）

```typescript
// 这里展示了 N+1 查询问题
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // 每个用户都发一次查询！
  renderUserPosts(posts);
});
```

#### 建议修复

```typescript
// 使用 JOIN 查询进行优化
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### 影响分析

| 方面 | 影响 | 严重性 |
|--------|--------|--------|
| 性能 | 20 个用户就会产生 100+ 次查询 | High |
| 用户体验 | 页面加载缓慢 | High |
| 可扩展性 | 规模变大后会失效 | Critical |
| 可维护性 | 难以排查问题 | Medium |

### 相关问题

- `AdminUserList.tsx` 第 120 行有类似问题
- 相关 PR：#456
- 相关 issue：#789

### 额外资源

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)

### 审查者备注

- 这是这个代码库里常见的模式
- 可以考虑把它加入代码风格指南
- 也许值得提取一个辅助函数

### 作者回复（供反馈）

*由代码作者填写：*

- [ ] 已在提交 `abc123` 中修复
- [ ] 修复状态：Complete / In Progress / Needs Discussion
- [ ] 问题或疑虑：（描述）

---

## 统计信息（供审查者使用）

在审查多个问题时，请记录：

- **发现问题总数：** X
- **Critical：** X
- **High：** X
- **Medium：** X
- **Low：** X

**建议：** ✅ Approve / ⚠️ Request Changes / 🔄 Needs Discussion

**整体代码质量：** 1-5 星
