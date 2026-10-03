# 리팩토링 계획 템플릿

이 템플릿을 사용하여 리팩토링 작업을 문서화하고 추적하세요.


---

## 프로젝트 정보

| Field              | Value                                                  |
| ------------------ | ------------------------------------------------------ |
| **Project/Module** | [프로젝트 이름]                                              |
| **Target Files**   | [리팩토링할 파일 목록]                                          |
| **Date Created**   | [생성 날짜]                                                |
| **Author**         | [작성자]                                                  |
| **Status**         | Draft / In Review / Approved / In Progress / Completed |


---

## 개요

### 목표
- [ ] [주요 목표: 예: 결제 처리 가독성 향상]
- [ ] [부가 목표: 예: 코드 중복 감소]
- [ ] [추가 목표: 예: 테스트 용이성 향상]

### 제약조건
- [ ] [제약 조건 1: 예: 공개 API 변경 불가]
- [ ] [제약 조건 2: 예: 하위 호환성 유지 필수]
- [ ] [제약 조건 3: 예: 데이터베이스 스키마 변경 금지]


### 위험수준
- [ ] Low - 변경 범위가 작고 충분히 테스트된 코드
- [ ] Medium - 중간 수준의 변경, 일부 위험 존재
- [ ] High - 큰 규모의 변경, 신중한 검토 필요

---

## 리팩토링 전 체크리스트

### 테스트 커버리지 평가

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Unit Test Coverage | __%  | ≥80% | |
| Integration Tests | Yes/No | Yes | |
| All Tests Passing | Yes/No | Yes | |

### 시작 전 필수 사항
- [ ] 모든 테스트 통과
- [ ] 코드 검토 및 이해 완료
- [ ] 백업 또는 버전 관리 준비 완료
- [ ] 사용자 승인 획득


---

## 식별된 코드 스멜

### 요약

| # | Smell | Location | Severity | Priority |
|---|-------|----------|----------|----------|
| 1 | [e.g., Long Method] | [file:line] | High | P1 |
| 2 | [e.g., Duplicate Code] | [file:line] | Medium | P2 |
| 3 | [e.g., Feature Envy] | [file:line] | Low | P3 |

### 상세 분석

#### 코드 스멜 #1: [이름]

**위치**: `path/to/file.js:45-120`

**설명**: [문제에 대한 상세 설명]

**영향**:
- [영향 1]
- [영향 2]

**제안된 해결 방안**: [해결 방법에 대한 간략한 설명]

---

## 리팩토링 단계

### Phase A: 빠른 개선 사항 (낮은 위험도)

**목적**: 즉각적인 효과를 얻을 수 있는 간단한 개선

**예상 변경 범위**: [X개 파일, Y개 메서드]

**사용자 승인 필요 여부**: Yes / No

| # | Task | File | Refactoring | Status |
|---|------|------|-------------|--------|
| A1 | 변수 `x`를 `userCount`로 이름 변경 | utils.js:15 | Rename Variable | [ ] |
| A2 | 사용되지 않는 `oldHandler()` 제거 | api.js:89 | Remove Dead Code | [ ] |
| A3 | 중복된 검증 로직 추출  | form.js:23,67 | Extract Method | [ ] |

**롤백 계획**: A1-A3 커밋 되돌리기

---

### Phase B: 구조 개선 (중간 위험도)

**목적**: 코드 구조와 가독성 개선

**예상 변경 범위**: [X개 파일, Y개 메서드]

**사용자 승인 필요 여부**: Yes

**의존성**: Phase A 완료 필수


| #  | Task                               | File           | Refactoring                | Status |
| -- | ---------------------------------- | -------------- | -------------------------- | ------ |
| B1 | 긴 메서드에서 `calculatePrice()` 추출      | order.js:45    | Extract Method             | [ ]    |
| B2 | `OrderDetails` 매개변수 객체 도입          | order.js:12    | Introduce Parameter Object | [ ]    |
| B3 | `formatAddress()`를 Address 클래스로 이동 | customer.js:78 | Move Method                | [ ]    |


**롤백 계획**: Phase A 완료 후 커밋으로 되돌리기

---

### Phase C: 아키텍처 변경 (높은 위험도)

**목적**: 더 깊은 구조적 문제 해결

**예상 변경 범위**: [X개 파일, Y개 메서드]

**사용자 승인 필요 여부**: Yes

**의존성**: Phase A와 B 완료 필수

| #  | Task                         | File          | Refactoring                           | Status |
| -- | ---------------------------- | ------------- | ------------------------------------- | ------ |
| C1 | 가격 계산 switch 문을 다형성으로 대체     | pricing.js:30 | Replace Conditional with Polymorphism | [ ]    |
| C2 | `NotificationService` 클래스 추출 | user.js:100   | Extract Class                         | [ ]    |


**롤백 계획**: Phase B 완료 후 커밋으로 되돌리기

---

## 상세 리팩토링 절차

### 작업 [ID]: [작업 이름]


**Smell Addressed**: [코드 스멜 이름]

**Refactoring Technique**: [리팩토링 기법 이름]

**Risk Level**: Low / Medium / High


#### 배경

**Before** (현재 상태):
```javascript
// Paste current code here
```

**After** (예상 상태):
```javascript
// Paste expected code here
```

#### 단계별 수행 절차

1. [ ] **Step 1**: [설명]

   - Test: 해당 단계 후 테스트 실행
   - Expected: 모든 테스트 통과

2. [ ] **Step 2**: [설명]

   - Test: 해당 단계 후 테스트 실행
   - Expected: 모든 테스트 통과

3. [ ] **Step 3**: [설명]

   - Test: 해당 단계 후 테스트 실행
   - Expected: 모든 테스트 통과


#### 검증

- [ ] 모든 테스트 통과
- [ ] 동작 변경 없음
- [ ] 코드 컴파일 성공
- [ ] 새로운 경고 없음


#### 커밋 메시지
```
refactor: [Describe the refactoring]
```

---

## 진행 상황 추적

### 단계 상태

| Phase | Status | Started | Completed | Tests Passing |
|-------|--------|---------|-----------|---------------|
| A | Not Started / In Progress / Done | | | |
| B | Not Started / In Progress / Done | | | |
| C | Not Started / In Progress / Done | | | |

### 발생한 이슈

| # | Issue | Resolution | Status          |
| - | ----- | ---------- | --------------- |
| 1 | [설명]  | [해결 방법]    | Open / Resolved |

---

## 지표 비교

### 리팩토링 전


| Metric | File 1 | File 2 | Total |
|--------|--------|--------|-------|
| Lines of Code | | | |
| Cyclomatic Complexity | | | |
| Maintainability Index | | | |
| Number of Methods | | | |
| Avg Method Length | | | |

### After Refactoring

| Metric | File 1 | File 2 | Total | Change |
|--------|--------|--------|-------|--------|
| Lines of Code | | | | |
| Cyclomatic Complexity | | | | |
| Maintainability Index | | | | |
| Number of Methods | | | | |
| Avg Method Length | | | | |

---

## 리팩토링 후 체크리스트

- [ ] 모든 테스트 통과
- [ ] 새로운 경고 또는 오류 없음
- [ ] 코드 컴파일 성공
- [ ] 수동 검증 완료
- [ ] 문서 업데이트 완료 (필요한 경우)
- [ ] 코드 리뷰 완료
- [ ] 지표 개선 확인
- [ ] 사용자 최종 승인 획득

---

## 회고 및 학습 내용

### 잘된 점

- [항목 1]
- [항목 2]

### 개선이 필요한 점

- [항목 1]
- [항목 2]

### 향후 권장 사항

- [항목 1]
- [항목 2]


---

## 승인

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Plan Author | | | |
| Technical Lead | | | |
| Product Owner | | | |

---

## 부록

### A. 관련 문서

- [관련 문서 링크]

### B. 참고 자료

- [코드 스멜 카탈로그 링크]
- [리팩토링 카탈로그 링크]

### C. 사용 도구

- [테스트 프레임워크]
- [린팅 도구]
- [복잡도 분석 도구]
