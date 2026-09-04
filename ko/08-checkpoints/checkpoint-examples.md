# 체크포인트 예제(Checkpoints and Rewind Examples)

Claude Code에서 체크포인트를 효과적으로 사용하는 실제 예제입니다.

참고: 체크포인트는 모든 사용자 입력마다 자동으로 생성됩니다. 따라서 수동 저장이 필요하지 않습니다. 되돌리려면 `Esc`를 두 번 누르거나(`Esc+Esc`) `/rewind`를 사용하여 체크포인트 브라우저를 열 수 있습니다.

## 예제 1: 데이터베이스 마이그레이션

### 시나리오
MySQL에서 PostgreSQL로 마이그레이션해야 하지만, 직접 마이그레이션 방식과 점진적인 dual-write 방식 두 가지를 모두 실험해보고 싶다.

### 워크플로우

```
User: MySQL에서 PostgreSQL로 직접 마이그레이션을 구현해줘
      [체크포인트 A 자동 생성]

Claude: 직접 마이그레이션을 구현하겠습니다...
[DB 드라이버 변경, 쿼리 수정, 스키마 변경]

User: 테스트 실행
      [체크포인트 B 자동 생성]

Claude: 테스트 실행 중...
❌ 15개 테스트 실패 - 커넥션 풀 문제 발생

User: 이 방식은 문제가 있어. dual-write 방식으로 다시 해보자.
[Esc+Esc로 체크포인트 A 선택 후 "코드와 대화 복원"]

User: 이제 두 데이터베이스에 동시에 쓰는 dual-write 패턴을 구현해줘

Claude: dual-write 마이그레이션을 구현하겠습니다...
[dual-write 레이어 및 점진적 마이그레이션 전략 구현]

User: 테스트 실행

Claude: 테스트 실행 중...
✅ 모든 테스트 통과

User: dual-write 방식이 더 안전하네. 이걸 커밋하자
```

## 예제 2: 성능 최적화

### 시나리오
여러 가지 성능 최적화 전략을 비교해야 하는 상황

### 워크플로우

```
User: API 응답 속도를 최적화해줘. 현재: 450ms
      [체크포인트 "Baseline" 자동 생성]

Claude: DB 쿼리 캐싱을 추가하겠습니다...
[Redis 캐싱 구현]

User: 성능 테스트 실행

Claude: 결과: 평균 280ms (38% 개선)

User: 다른 방법도 시도해보자
[Esc+Esc로 Baseline 복원]

User: DB 쿼리 최적화 방식으로 해보자

Claude: DB 쿼리를 최적화하겠습니다...
[인덱스 추가, N+1 문제 해결]

User: 성능 테스트 실행

Claude: 결과: 평균 180ms (60% 개선)

User: 세 번째 방법도 해보자
[Esc+Esc로 Baseline 복원]

User: 응답 압축 + CDN 적용해보자

Claude: gzip 적용 및 CDN 설정...
[압축 및 CDN 구성]

User: 성능 테스트 실행

Claude: 결과: 평균 320ms (29% 개선)

User: 쿼리 최적화가 가장 좋네. 여기에 캐싱을 결합해보자
[쿼리 최적화 체크포인트로 복원]

User: Redis 캐싱을 추가해보자

Claude: Redis 캐싱 추가...
```

## 예제 3: UI/UX 반복 개선

### 시나리오
대시보드 레이아웃을 여러 방식으로 실험

### 워크플로우

```
User: 사이드바 레이아웃으로 대시보드를 다시 설계해줘
      [체크포인트 "Start" 자동 생성]

Claude: 사이드바 레이아웃 구현

User: 스크린샷 보여줘

Claude: [스크린샷]

User: 너무 답답해. 상단 네비게이션으로 바꿔보자
[Start 체크포인트로 복원]

User: 상단 네비게이션으로 구현해줘

Claude: 상단 네비게이션 구현

User: 스크린샷 보여줘

Claude: [스크린샷]

User: 괜찮긴 한데 카드 그리드 방식도 해보자
[Start로 복원]

User: 카드 기반 그리드로 구현해줘

Claude: 카드 그리드 구현

User: 이건 좋다! 그런데 상단 네비게이션도 같이 넣어볼 수 있나?
[카드 그리드 이후 체크포인트로 복원]

User: 카드 그리드에 상단 네비게이션을 추가해줘

Claude: 상단 네비게이션 + 카드 그리드 결합
```

## 예제 4: 디버깅 세션

### 시나리오
복잡한 메모리 누수 버그 해결

### 워크플로우

```
User: 애플리케이션에 메모리 누수가 있어
      [체크포인트 "디버깅 전" 자동 생성]

Claude: 원인 분석 중...
[코드 분석]

User: 이벤트 리스너 문제인 것 같아. 그걸 고쳐보자

Claude: 이벤트 리스너 정리 수정

User: 메모리 프로파일러 실행

Claude: 여전히 누수 발생 - 이벤트 리스너가 원인이 아님

User: 다른 가설로 돌아가보자
[디버깅 전 체크포인트로 복원]

User: DB 커넥션 문제일 수도 있어

Claude: 커넥션 풀 수정

User: 메모리 프로파일러 실행

Claude: 여전히 누수 - 커넥션 문제 아님

User: 다른 방향으로 가보자
[디버깅 전으로 복원]

User: 순환 참조를 확인해보자

Claude: 캐시 내부 순환 참조 발견 및 수정

User: 메모리 프로파일러 실행

Claude: ✅ 메모리 누수 해결! 캐시 순환 참조가 원인이었음

User: 좋다. 이거 커밋하자
```

## 예제 5: API 설계 진화

### 시나리오
REST API 설계를 여러 방식으로 발전시키는 과정

### 워크플로우

```
User: 블로그 플랫폼용 REST API를 만들어줘
      [API 설계 전 체크포인트 생성]

Claude: 기본 CRUD API 생성

User: 페이지네이션이랑 필터링도 추가해줘

Claude: 페이지네이션 및 필터링 추가

User: 리소스 관계도 개선해야 해

Claude: HATEOAS 링크 구조 적용

User: 잠깐, REST 대신 GraphQL로 해보자
[API 설계 전으로 복원]

User: GraphQL API로 다시 만들어줘

Claude: GraphQL API 구현

User: REST가 더 나은 것 같아
[HATEOAS 이후 체크포인트로 복원]

User: REST API로 최종 확정하자
```

## 예제 6: 설정 관리(Configuration Management)

### 시나리오
여러 가지 설정 방식(config approach)을 실험하는 상황

### 워크플로우

```
User: 설정을 환경 변수로 옮겨줘
      [체크포인트 "Original config" 자동 생성]

Claude: 환경 변수 기반 설정을 적용하겠습니다...
[환경 변수 구성 적용]

User: 개발 환경에서 테스트

Claude: 로컬에서는 정상 동작하지만, 프로덕션 배포에서 문제 발생

User: 다른 방식으로 해보자
[Esc+Esc로 Original config 체크포인트 선택 후 "코드와 대화 복원"]

User: 설정 파일 기반 방식 + 검증 로직으로 바꿔보자

Claude: YAML 설정 + JSON schema 검증 적용

User: 개발 환경 테스트

Claude: ✅ 정상 동작, 검증 에러도 잘 처리됨

User: 민감한 값은 env var도 지원할 수 있어?

Claude: secrets는 env var override 방식 추가

User: 배포 테스트

Claude: ✅ 모든 환경에서 정상 동작

User: 이 방식이 프로덕션에 적합하네
```

## 예제 7: 테스트 전략(Test Strategy)

### 시나리오
포괄적인 테스트 구조를 구축하는 과정

### 워크플로우

```
User: auth 모듈에 유닛 테스트 추가해줘
      [체크포인트 자동 생성]

Claude: Jest 기반 유닛 테스트 추가

User: 테스트 실행

Claude: 45개 테스트 통과, 커버리지 78%

User: 통합 테스트도 추가해줘

Claude: 통합 테스트 추가

User: 테스트 실행

Claude: 89개 통과, 커버리지 92%, 하지만 실행 속도 3분 (느림)

User: 너무 느려. 최적화하자

Claude: 테스트 환경 최적화, 병렬 실행 적용

User: 테스트 실행

Claude: 89개 통과, 커버리지 92%, 35초로 개선됨 ✅

User: 좋다. 이제 E2E 테스트도 추가하자

Claude: Playwright 기반 E2E 테스트 추가

User: 전체 테스트 실행

Claude: 112개 통과, 커버리지 94%, 2분 소요

User: 균형 잘 맞았네
```

## 예제 8: Summarize from Checkpoint 사용

### 시나리오
긴 디버깅 세션 이후 컨텍스트를 압축하면서 핵심만 유지

### 워크플로우

```
User: [20개 이상의 메시지로 디버깅 진행 후]

[Esc+Esc로 초기 체크포인트 선택 후 "여기서부터 요약" 선택]
[선택적으로 지시사항: "무엇을 시도했고 무엇이 해결됐는지 중심으로 요약"]

Claude: [해당 시점 이후 대화 내용을 요약 생성]
[원본 메시지는 transcript에 보존됨]
[요약으로 대화가 압축되어 컨텍스트 사용량 감소]

User: 이제 성공한 접근 방식으로 계속 진행하자
```

## 핵심 정리(Key Takeaways)

1. **체크포인트는 자동 생성됨**: 모든 입력마다 자동 저장 → 수동 저장 불필요
2. **접근 방법은 2가지**: Esc+Esc 또는 /rewind
3. **복원 방식 선택 중요**: 코드 / 대화 / 둘 다 / 요약 중 선택
4. **실험을 두려워하지 말 것**: 체크포인트 덕분에 안전하게 변경 가능
5. **Git과 함께 사용**: 체크포인트는 실험용, Git은 확정용
6. **긴 세션은 요약 활용**: "여기서부터 요약"으로 컨텍스트 관리

---
**Last Updated**: June 2, 2026
**Claude Code Version**: 2.1.160
**Sources**:
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/changelog
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
