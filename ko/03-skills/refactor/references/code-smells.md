# 코드 스멜 카탈로그

Martin Fowler의 *Refactoring* (2판)을 기반으로 한 코드 스멜에 대한 포괄적인 참고 자료입니다. 코드 스멜은 더 깊은 문제의 증상이며, 코드 설계에 문제가 있을 수 있음을 나타냅니다.

> "코드 스멜은 일반적으로 시스템의 더 깊은 문제에 해당하는 표면적인 징후입니다." — Martin Fowler

---

## 비대해진 코드 (Bloaters)

너무 커져서 효과적으로 다루기 어려운 것을 나타내는 코드 스멜입니다.

### 긴 메서드 (Long Method)

**징후:**
- 메서드가 30-50줄을 초과
- 전체 메서드를 보려면 스크롤해야 함
- 여러 단계의 중첩
- 섹션이 하는 일을 설명하는 주석

**왜 나쁜가:**
- 이해하기 어려움
- 독립적으로 테스트하기 어려움
- 변경 시 예상치 못한 결과를 초래
- 중복된 로직이 내부에 숨어 있음

**리팩터링:**
- Extract Method (메서드 추출)
- Replace Temp with Query (임시 변수를 쿼리로 전환)
- Introduce Parameter Object (매개변수 객체 도입)
- Replace Method with Method Object (메서드를 메서드 객체로 전환)
- Decompose Conditional (조건문 분해)

**예시 (이전):**
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

**예시 (이후):**
```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  sendOrderNotifications(order, totals);
  return { order, totals };
}
```

---

### 큰 클래스 (Large Class)

**징후:**
- 클래스에 인스턴스 변수가 많음 (>7-10개)
- 클래스에 메서드가 많음 (>15-20개)
- 클래스 이름이 모호함 (Manager, Handler, Processor)
- 메서드가 모든 인스턴스 변수를 사용하지 않음

**왜 나쁜가:**
- 단일 책임 원칙 위반
- 테스트하기 어려움
- 변경 사항이 관련 없는 기능에 파급됨
- 부분적으로 재사용하기 어려움

**리팩터링:**
- Extract Class (클래스 추출)
- Extract Subclass (서브클래스 추출)
- Extract Interface (인터페이스 추출)

**탐지:**
```
Lines of code > 300
Number of methods > 15
Number of fields > 10
```

---

### 원시 타입 집착 (Primitive Obsession)

**징후:**
- 도메인 개념에 원시 타입 사용 (이메일에 string, 돈에 int)
- 객체 대신 원시 타입의 배열
- 타입 코드에 string 상수
- 매직 넘버/스트링

**왜 나쁜가:**
- 타입 레벨에서의 유효성 검사 부재
- 로직이 코드베이스 전체에 흩어져 있음
- 잘못된 값을 전달하기 쉬움
- 도메인 개념 누락

**리팩터링:**
- Replace Primitive with Object (원시 타입을 객체로 전환)
- Replace Type Code with Class (타입 코드를 클래스로 전환)
- Replace Type Code with Subclasses (타입 코드를 서브클래스로 전환)
- Replace Type Code with State/Strategy (타입 코드를 상태/전략 패턴으로 전환)

**예시 (이전):**
```javascript
const user = {
  email: 'john@example.com',     // Just a string
  phone: '1234567890',           // Just a string
  status: 'active',              // Magic string
  balance: 10050                 // Cents as integer
};
```

**예시 (이후):**
```javascript
const user = {
  email: new Email('john@example.com'),
  phone: new PhoneNumber('1234567890'),
  status: UserStatus.ACTIVE,
  balance: Money.cents(10050)
};
```

---

### 긴 매개변수 목록 (Long Parameter List)

**징후:**
- 매개변수가 4개 이상인 메서드
- 항상 함께 나타나는 매개변수
- 메서드 동작을 변경하는 boolean 플래그
- Null/undefined가 자주 전달됨

**왜 나쁜가:**
- 올바르게 호출하기 어려움
- 매개변수 순서 혼란
- 메서드가 너무 많은 일을 하고 있음을 나타냄
- 새로운 매개변수 추가가 어려움

**리팩터링:**
- Introduce Parameter Object (매개변수 객체 도입)
- Preserve Whole Object (객체 전체 유지)
- Replace Parameter with Method Call (매개변수를 메서드 호출로 전환)
- Remove Flag Argument (플래그 매개변수 제거)

**예시 (이전):**
```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy) {
  // ...
}
```

**예시 (이후):**
```javascript
function createUser(personalInfo, address, options) {
  // personalInfo: { firstName, lastName, email, phone }
  // address: { street, city, state, zip }
  // options: { isAdmin, isActive, createdBy }
}
```

---

### 데이터 뭉치 (Data Clumps)

**징후:**
- 동일한 3개 이상의 필드가 반복적으로 함께 나타남
- 항상 함께 전달되는 매개변수
- 함께 속해야 할 필드들의 부분 집합을 가진 클래스

**왜 나쁜가:**
- 중복된 처리 로직
- 추상화 누락
- 확장하기 어려움
- 숨겨진 클래스를 나타냄

**리팩터링:**
- Extract Class (클래스 추출)
- Introduce Parameter Object (매개변수 객체 도입)
- Preserve Whole Object (객체 전체 유지)

**예시:**
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

## 객체 지향 원칙 위반 (Object-Orientation Abusers)

객체 지향 프로그래밍 원칙의 불완전하거나 잘못된 사용을 나타내는 스멜입니다.

### Switch 문 (Switch Statements)

**징후:**
- 긴 switch/case 또는 if/else 체인
- 여러 곳에서 동일한 switch 문 사용
- 타입 코드에 대한 switch 문
- 새로운 case 추가 시 모든 곳에서 변경 필요

**왜 나쁜가:**
- 개방/폐쇄 원칙 위반
- 변경 사항이 모든 switch 위치에 파급됨
- 확장하기 어려움
- 종종 다형성 누락을 나타냄

**리팩터링:**
- Replace Conditional with Polymorphism (조건문을 다형성으로 전환)
- Replace Type Code with Subclasses (타입 코드를 서브클래스로 전환)
- Replace Type Code with State/Strategy (타입 코드를 상태/전략 패턴으로 전환)

**예시 (이전):**
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

**예시 (이후):**
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

### 임시 필드 (Temporary Field)

**징후:**
- 일부 메서드에서만 사용되는 인스턴스 변수
- 조건부로 설정되는 필드
- 특정 경우에 대한 복잡한 초기화

**왜 나쁜가:**
- 혼란스러움—필드가 존재하지만 null일 수 있음
- 객체 상태를 이해하기 어려움
- 조건부 로직이 숨어 있음을 나타냄

**리팩터링:**
- Extract Class (클래스 추출)
- Introduce Null Object (널 객체 도입)
- Replace Temp Field with Local (임시 필드를 지역 변수로 전환)

---

### 상속 거부 (Refused Bequest)

**징후:**
- 서브클래스가 상속된 메서드/데이터를 사용하지 않음
- 서브클래스가 아무것도 하지 않도록 오버라이드함
- 코드 재사용을 위해 상속을 사용하고, IS-A 관계가 아님

**왜 나쁜가:**
- 잘못된 추상화
- 리스코프 치환 원칙 위반
- 오해의 소지가 있는 계층 구조

**리팩터링:**
- Push Down Method/Field (메서드/필드 아래로 푸시다운)
- Replace Subclass with Delegate (서브클래스를 위임으로 전환)
- Replace Inheritance with Delegation (상속을 위임으로 전환)

---

### 다른 인터페이스를 가진 대체 클래스 (Alternative Classes with Different Interfaces)

**징후:**
- 유사한 작업을 수행하는 두 개의 클래스
- 동일한 개념에 대해 다른 메서드 이름
- 상호 교환적으로 사용될 수 있음

**왜 나쁜가:**
- 중복된 구현
- 공통 인터페이스 부재
- 전환하기 어려움

**리팩터링:**
- Rename Method (메서드 이름 변경)
- Move Method (메서드 이동)
- Extract Superclass (슈퍼클래스 추출)
- Extract Interface (인터페이스 추출)

---

## 변경 방해 요소 (Change Preventers)

변경을 어렵게 만드는 스멜—하나를 변경하면 다른 많은 것을 변경해야 합니다.

### 발산적 변경 (Divergent Change)

**징후:**
- 여러 가지 다른 이유로 하나의 클래스가 변경됨
- 다른 영역의 변경이 동일한 클래스 편집을 유발
- 클래스가 "신(神) 클래스"임

**왜 나쁜가:**
- 단일 책임 원칙 위반
- 높은 변경 빈도
- 병합 충돌

**리팩터링:**
- Extract Class (클래스 추출)
- Extract Superclass (슈퍼클래스 추출)
- Extract Subclass (서브클래스 추출)

**예시:**
`User` 클래스가 다음 이유로 변경됩니다:
- 인증 변경
- 프로필 변경
- 결제 변경
- 알림 변경

→ 추출: `AuthService`, `ProfileService`, `BillingService`, `NotificationService`

---

### 산탄총 수술 (Shotgun Surgery)

**징후:**
- 하나의 변경이 많은 클래스에서 편집을 요구함
- 작은 기능이 10개 이상의 파일을 건드려야 함
- 변경 사항이 흩어져 있어 모두 찾기 어려움

**왜 나쁜가:**
- 한 부분을 놓치기 쉬움
- 높은 결합도
- 변경 시 오류 발생 가능성이 높음

**리팩터링:**
- Move Method (메서드 이동)
- Move Field (필드 이동)
- Inline Class (클래스 인라인화)

**탐지:**
다음을 찾습니다: 필드 하나를 추가하는 데 5개 이상의 파일에서 변경이 필요한 경우.

---

### 병렬 상속 계층 (Parallel Inheritance Hierarchies)

**징후:**
- 한 계층에서 서브클래스를 생성하면 다른 계층에서도 서브클래스를 생성해야 함
- 클래스 접두사가 일치함 (예: `DatabaseOrder`, `DatabaseProduct`)

**왜 나쁜가:**
- 두 배의 유지 보수
- 계층 간의 결합
- 한쪽을 잊어버리기 쉬움

**리팩터링:**
- Move Method (메서드 이동)
- Move Field (필드 이동)
- Eliminate one hierarchy (한 계층 제거)

---

## 불필요한 요소 (Dispensables)

제거되어야 할 불필요한 것입니다.

### 주석 (과도한) (Comments (Excessive))

**징후:**
- 코드가 무엇을 하는지 설명하는 주석
- 주석 처리된 코드
- 영원히 남아 있는 TODO/FIXME
- 주석 내의 사과문

**왜 나쁜가:**
- 주석이 거짓말을 함 (동기화되지 않음)
- 코드는 자체적으로 설명되어야 함
- 죽은 코드가 혼란을 야기함

**리팩터링:**
- Extract Method (이름으로 무엇을 하는지 설명)
- Rename (주석 없이 명확성)
- Remove commented code (주석 처리된 코드 제거)
- Introduce Assertion (단언문 도입)

**좋은 주석 vs 나쁜 주석:**
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

### 중복 코드 (Duplicate Code)

**징후:**
- 여러 곳에서 동일한 코드
- 약간의 변형이 있는 유사한 코드
- 복사-붙여넣기 패턴

**왜 나쁜가:**
- 여러 곳에서 버그 수정 필요
- 불일치 위험
- 코드베이스 비대화

**리팩터링:**
- Extract Method (메서드 추출)
- Extract Class (클래스 추출)
- Pull Up Method (계층 구조에서 메서드 위로 올리기)
- Form Template Method (템플릿 메서드 형성)

**탐지 규칙:**
3회 이상 중복된 모든 코드는 추출되어야 합니다.

---

### 게으른 클래스 (Lazy Class)

**징후:**
- 클래스가 존재를 정당화할 만큼 충분히 많은 일을 하지 않음
- 추가된 가치가 없는 래퍼
- 과도한 설계의 결과

**왜 나쁜가:**
- 유지 보수 오버헤드
- 불필요한 간접성
- 이점 없는 복잡성

**리팩터링:**
- Inline Class (클래스 인라인화)
- Collapse Hierarchy (계층 구조 축소)

---

### 죽은 코드 (Dead Code)

**징후:**
- 도달할 수 없는 코드
- 사용되지 않는 변수/메서드/클래스
- 주석 처리된 코드
- 불가능한 조건 뒤에 있는 코드

**왜 나쁜가:**
- 혼란
- 유지 보수 부담
- 이해 속도 저하

**리팩터링:**
- Remove Dead Code (죽은 코드 제거)
- Safe Delete (안전하게 삭제)

**탐지:**
```bash
# Look for unused exports
# Look for unreferenced functions
# IDE "unused" warnings
```

---

### 추측성 일반화 (Speculative Generality)

**징후:**
- 하나의 서브클래스를 가진 추상 클래스
- "미래 사용을 위한" 사용되지 않는 매개변수
- 단순히 위임하는 메서드
- 하나의 사용 사례를 위한 "프레임워크"

**왜 나쁜가:**
- 이점 없는 복잡성
- YAGNI (You Ain't Gonna Need It - 필요 없을 거야) 원칙 위반
- 이해하기 어려움

**리팩터링:**
- Collapse Hierarchy (계층 구조 축소)
- Inline Class (클래스 인라인화)
- Remove Parameter (매개변수 제거)
- Rename Method (메서드 이름 변경)

---

## 결합자 (Couplers)

클래스 간의 과도한 결합을 나타내는 스멜입니다.

### 기능 선망 (Feature Envy)

**징후:**
- 메서드가 자신의 클래스보다 다른 클래스의 데이터를 더 많이 사용함
- 다른 객체에 대한 많은 getter 호출
- 데이터와 행동이 분리되어 있음

**왜 나쁜가:**
- 행동이 잘못된 위치에 있음
- 캡슐화 불량
- 유지 보수하기 어려움

**리팩터링:**
- Move Method (메서드 이동)
- Move Field (필드 이동)
- Extract Method (메서드 추출 후 이동)

**예시 (이전):**
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

**예시 (이후):**
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

### 부적절한 친밀함 (Inappropriate Intimacy)

**징후:**
- 클래스들이 서로의 비공개 부분에 접근함
- 양방향 참조
- 서브클래스가 부모에 대해 너무 많이 알고 있음

**왜 나쁜가:**
- 높은 결합도
- 변경 사항이 연쇄적으로 발생
- 하나를 다른 것 없이 수정하기 어려움

**리팩터링:**
- Move Method (메서드 이동)
- Move Field (필드 이동)
- Change Bidirectional to Unidirectional (양방향 참조를 단방향으로 변경)
- Extract Class (클래스 추출)
- Hide Delegate (위임 숨기기)

---

### 메시지 체인 (Message Chains)

**징후:**
- 긴 메서드 호출 체인: `a.getB().getC().getD().getValue()`
- 클라이언트가 탐색 구조에 의존함
- "기차 탈선" 코드

**왜 나쁜가:**
- 취약함—어떤 변경이든 체인을 깨뜨림
- 데메테르의 법칙 위반
- 구조에 대한 결합

**리팩터링:**
- Hide Delegate (위임 숨기기)
- Extract Method (메서드 추출)
- Move Method (메서드 이동)

**예시:**
```javascript
// Bad: Message chain
const managerName = employee.getDepartment().getManager().getName();

// Better: Hide delegation
const managerName = employee.getManagerName();
```

---

### 중개인 (Middle Man)

**징후:**
- 다른 클래스에 단순히 위임하는 클래스
- 메서드의 절반이 위임임
- 추가된 가치가 없음

**왜 나쁜가:**
- 불필요한 간접성
- 유지 보수 오버헤드
- 혼란스러운 아키텍처

**리팩터링:**
- Remove Middle Man (중개인 제거)
- Inline Method (메서드 인라인화)

---

## 코드 스멜 심각도 가이드

| 심각도 | 설명 | 조치 |
|----------|-------------|--------|
| **Critical** | 개발을 막고, 버그를 유발 | 즉시 수정 |
| **High** | 상당한 유지 보수 부담 | 현재 스프린트에서 수정 |
| **Medium** | 눈에 띄지만 관리 가능 | 가까운 미래를 위해 계획 |
| **Low** | 사소한 불편함 | 기회가 있을 때 수정 |

---

## 빠른 탐지 체크리스트

코드를 스캔할 때 이 체크리스트를 사용하십시오:

- [ ] 30줄을 초과하는 메서드가 있습니까?
- [ ] 300줄을 초과하는 클래스가 있습니까?
- [ ] 4개 이상의 매개변수를 가진 메서드가 있습니까?
- [ ] 중복된 코드 블록이 있습니까?
- [ ] 타입 코드에 대한 switch/case 문이 있습니까?
- [ ] 사용되지 않는 코드가 있습니까?
- [ ] 다른 클래스의 데이터를 과도하게 사용하는 메서드가 있습니까?
- [ ] 긴 메서드 호출 체인이 있습니까?
- [ ] "왜"가 아닌 "무엇"을 설명하는 주석이 있습니까?
- [ ] 객체여야 할 원시 타입이 있습니까?

---

## 추가 자료

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- Kerievsky, J. (2004). *Refactoring to Patterns*
- Feathers, M. (2004). *Working Effectively with Legacy Code*
