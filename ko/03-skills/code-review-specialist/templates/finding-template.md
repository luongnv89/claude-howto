# Code Review Finding Template

코드 리뷰 중 발견된 각 문제를 기록할 때 이 템플릿을 사용하세요.

---

## Issue: [TITLE]

### Severity
- [ ] Critical (배포 차단)
- [ ] High (머지 전 수정 필요)
- [ ] Medium (조만간 수정 필요)
- [ ] Low (수정하면 좋음)
### Category
- [ ] Security
- [ ] Performance
- [ ] Code Quality
- [ ] Maintainability
- [ ] Testing
- [ ] Design Pattern
- [ ] Documentation

### 위치
**File:** `src/components/UserCard.tsx`

**Lines:** 45-52

**Function/Method:** `renderUserDetails()`

### 문제 설명

**What:** 문제가 무엇인지 설명합니다.

**Why it matters:** 영향도와 이 문제를 왜 수정해야 하는지 설명합니다.

**Current behavior:** 문제가 되는 코드나 동작을 보여줍니다.

**Expected behavior:** 대신 어떤 동작이 일어나야 하는지 설명합니다.

### 코드 예시

#### 현재 (문제가 되는 코드)

```typescript
// Shows the N+1 query problem
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // Query per user!
  renderUserPosts(posts);
});
```

#### 제안된 해결 방법

```typescript
// Optimized with JOIN query
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### 영향도 분석


| 측면 | 영향 | 심각성 |
|--------|--------|----------|
| 성능 | 유저 20명당 100개 이상의 쿼리 발생 | 높음 |
| 사용자 경험 | 느린 페이지 로드 | 높음 |
| 확장성 | 대규모 환경에서 시스템 중단 발생 | 치명적 |
| 유지보수성 | 디버깅이 어려움 | 중간 |

### 관련 이슈

- `AdminUserList.tsx` 120번 줄의 유사한 문제
- 관련 PR: #456
- 관련 이슈: #789

### 추가 자료

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)

### 리뷰어 노트
- 이 코드베이스에서 흔히 발생하는 패턴입니다.
- 이를 코드 스타일 가이드에 추가하는 것을 고려해 보세요.
- 헬퍼 함수를 만들 가치가 있을 수 있습니다.

### 작성자 답변 (피드백용)

*코드 작성자가 작성할 부분:*
- [ ] 다음 커밋에서 수정 반영됨: `abc123`
- [ ] 수정 상태: 완료 / 진행 중 / 논의 필요
- [ ] 질문 및 우려 사항: (설명)


---

## 발견 통계 (리뷰어용)

여러 개의 발견 사항을 리뷰할 때 다음을 추적하세요:

- **총 발견된 문제 수:** X
- **치명적:** X
- **높음:** X
- **중간:** X
- **낮음:** X

**권장 사항**: ✅ 승인 / ⚠️ 변경 요청 / 🔄 논의 필요

**전반적인 코드 품질**: 별 1-5개
