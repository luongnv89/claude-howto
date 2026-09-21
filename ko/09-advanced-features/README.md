<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 고급 기능

기획 모드, 확장된 사고, 자동 모드, 백그라운드 작업, 권한 모드, 인쇄 모드 (비대화형), 세션 관리, 대화형 기능, 채널, 음성 받아쓰기, 원격 제어, 웹 세션, 데스크톱 앱, 작업 목록, 프롬프트 제안, Git 워크트리, 샌드박싱, 관리형 설정, 구성 등 Claude Code의 고급 기능에 대한 종합 가이드입니다.

## 목차

1. [개요](#개요)
2. [기획 모드](#기획-모드)
3. [울트라플랜 (클라우드 기획 초안 작성)](#울트라플랜-클라우드-기획-초안-작성)
4. [확장된 사고](#확장된-사고)
5. [자동 모드](#자동-모드)
6. [백그라운드 작업](#백그라운드-작업)
7. [모니터 도구 (이벤트 기반 스트림)](#모니터-도구-이벤트-기반-스트림)
8. [동적 워크플로우](#동적-워크플로우)
9. [예약된 작업](#예약된-작업)
10. [권한 모드](#권한-모드)
11. [헤드리스 모드](#헤드리스-모드)
12. [세션 관리](#세션-관리)
13. [대화형 기능](#대화형-기능)
14. [TUI 모드 (전체 화면)](#tui-모드-전체-화면)
15. [음성 받아쓰기](#음성-받아쓰기)
16. [채널](#채널)
17. [Chrome 통합](#chrome-통합)
18. [원격 제어](#원격-제어)
19. [웹 세션](#웹-세션)
20. [데스크톱 앱](#데스크톱-앱)
21. [작업 목록](#작업-목록)
22. [프롬프트 제안](#프롬프트-제안)
23. [Git 워크트리](#git-워크트리)
24. [샌드박싱](#샌드박싱)
25. [관리형 설정 (엔터프라이즈)](#관리형-설정-엔터프라이즈)
26. [구성 및 설정](#구성-및-설정)
27. [에이전트 팀](#에이전트-팀)
28. [모범 사례](#모범-사례)
29. [추가 자료](#추가-자료)

---

## 개요

Claude Code의 고급 기능은 기획, 추론, 자동화 및 제어 메커니즘을 통해 핵심 기능을 확장합니다. 이러한 기능은 복잡한 개발 작업, 코드 검토, 자동화 및 다중 세션 관리를 위한 정교한 워크플로우를 가능하게 합니다.

**주요 고급 기능은 다음과 같습니다:**
- **기획 모드**: 코딩 전에 상세한 구현 계획 생성
- **확장된 사고**: 복잡한 문제에 대한 심층적인 추론
- **자동 모드**: 백그라운드 안전 분류기가 각 작업 실행 전에 검토 (연구 미리보기)
- **백그라운드 작업**: 대화를 차단하지 않고 긴 작업 실행
- **권한 모드**: Claude가 수행할 수 있는 작업 제어 (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`)
- **인쇄 모드**: 자동화 및 CI/CD를 위해 Claude Code를 비대화형으로 실행 (`claude -p`)
- **세션 관리**: 여러 작업 세션 관리
- **대화형 기능**: 키보드 단축키, 여러 줄 입력, 명령 기록
- **음성 받아쓰기**: 20개 언어 STT를 지원하는 푸시투톡 음성 입력
- **채널**: MCP 서버가 실행 중인 세션으로 메시지를 푸시 (연구 미리보기)
- **원격 제어**: Claude.ai 또는 Claude 앱에서 Claude Code 제어
- **웹 세션**: claude.ai/code에서 브라우저 내 Claude Code 실행
- **데스크톱 앱**: 시각적 차이 검토 및 여러 세션을 위한 독립형 앱
- **작업 목록**: 컨텍스트 압축 전반에 걸친 영구적인 작업 추적
- **프롬프트 제안**: 컨텍스트 기반의 스마트 명령 제안
- **Git 워크트리**: 병렬 작업을 위한 격리된 워크트리 브랜치
- **샌드박싱**: OS 수준의 파일 시스템 및 네트워크 격리
- **관리형 설정**: plist, 레지스트리 또는 관리형 파일을 통한 엔터프라이즈 배포
- **구성**: JSON 구성 파일로 동작 사용자 정의

---

## 기획 모드

기획 모드를 사용하면 Claude가 구현 전에 복잡한 작업을 신중하게 고려하여 검토하고 승인할 수 있는 상세한 계획을 만들 수 있습니다.

### 기획 모드란 무엇입니까?

기획 모드는 두 단계로 구성된 접근 방식입니다:
1. **기획 단계**: Claude가 작업을 분석하고 상세한 구현 계획을 생성합니다.
2. **구현 단계**: 승인 후 Claude가 계획을 실행합니다.

### 기획 모드 사용 시점

✅ 기획 모드를 사용하는 경우:
- 복잡한 다중 파일 리팩토링
- 새로운 기능 구현
- 아키텍처 변경
- 데이터베이스 마이그레이션
- 주요 API 재설계

❌ 기획 모드를 사용하지 않는 경우:
- 간단한 버그 수정
- 형식 변경
- 단일 파일 편집
- 빠른 쿼리

### 기획 모드 활성화

**슬래시 명령어**:
```bash
/plan Implement user authentication system
```

**CLI 플래그**:
```bash
claude --permission-mode plan
```

**기본값으로 설정**:
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**키보드 단축키**:
- `Shift + Tab` - 권한 모드 전환 (plan 포함)
- `Alt + M` - 권한 모드 전환 (Windows/Linux)

### 기획 모드의 이점

- **구조화된 구현 접근 방식**: 구현 단계의 상세한 세분화
- **검토 및 승인**: 실행 전에 계획을 승인하거나 조정
- **위험 식별**: 구현 전에 잠재적 문제 식별
- **명확한 단계**: 체계적인 구현 단계 및 마일스톤

### 예시: 기능 구현

```
User: /plan Add a real-time notification system

Claude: 실시간 알림 시스템 구현을 위한 계획을 생성하겠습니다.

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

Estimated time: 3-4 hours
Files to modify: 12
New files to create: 8

Ready to proceed? (yes/no/modify plan)

User: yes

Claude: [계획에 따라 구현을 시작합니다]
```

### 계획 수정

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: 업데이트된 계획:
[큐가 제거된 수정된 계획을 보여줍니다]

User: Looks good, proceed

Claude: [수정된 계획을 구현합니다]
```

### 기획 모드 구성

기획 모드는 CLI 플래그 또는 슬래시 명령어를 통해 활성화됩니다:

```bash
# Activate plan mode via CLI
claude --permission-mode plan

# Or use the /plan slash command inside the REPL
/plan Implement user authentication system
```

**기획용 모델 별칭**: Opus를 기획에, Sonnet을 실행에 사용하려면 `opusplan`을 모델 별칭으로 사용합니다:

```bash
claude --model opusplan "design and implement the new API"
```

**외부에서 계획 편집**: `Ctrl+G`를 눌러 외부 편집기에서 현재 계획을 열고 상세하게 수정할 수 있습니다.

> **v2.1.112 업데이트**: 이제 계획 파일은 무작위 단어 대신 생성된 프롬프트의 이름을 따서 명명되므로, 더 쉽게 찾아보고 재사용할 수 있습니다.

> **v2.1.136 업데이트 — 기획 모드 쓰기 블록은 무조건적입니다**: 기획 모드는 이제 `permissions.allow`에 일치하는 `Edit(...)` 규칙이 있는 경우를 포함하여 모든 파일 쓰기를 차단합니다. 이전에는 관대한 `Edit(...)` 규칙이 기획 모드에서 쓰기를 허용할 수 있었지만, 해당 우회 경로는 폐쇄되었습니다. 워크플로우가 이전 동작에 의존하는 경우, 편집하기 전에 기획 모드를 종료하십시오 (`Shift+Tab`).

---

## 울트라플랜 (클라우드 기획 초안 작성)

> **v2.1.101에 새로 추가**: 울트라플랜은 이제 처음 호출할 때 웹 클라우드 환경에 Claude Code를 자동으로 생성합니다. 수동 설정이 필요 없고, 초안 작성을 시작하기 전에 컨테이너가 준비될 때까지 기다릴 필요가 없습니다.

> **참고**: 울트라플랜은 연구 미리보기 기능이며 Claude Code v2.1.91 이상이 필요합니다.

`/ultraplan`은 로컬 CLI의 기획 작업을 기획 모드로 실행되는 웹 세션의 Claude Code로 넘깁니다. Claude는 클라우드에서 계획 초안을 작성하는 동안 터미널은 다른 작업을 위해 자유롭게 사용할 수 있습니다. 그런 다음 브라우저에서 초안을 검토하고 동일한 클라우드 세션에서 실행하거나 터미널로 다시 전송할지 선택합니다.

### 울트라플랜 사용 시점

- 터미널보다 더 풍부한 검토 화면 (인라인 주석, 이모지 반응, 개요 사이드바, 영구 기록)을 원할 때.
- 로컬에서 코딩을 계속하는 동안 핸즈프리 초안 작성을 원할 때 — 클라우드 세션은 저장소를 조사하고 CLI를 차단하지 않고 계획을 작성합니다.
- 실행 전에 이해 관계자 검토가 필요한 계획 — 공유 가능한 웹 URL이 터미널 스크롤백을 붙여넣는 것보다 낫습니다.

### 요구 사항

- Claude Code on the web 계정.
- GitHub 저장소 (클라우드 세션은 실제 코드에 대해 초안을 작성하기 위해 저장소를 복제합니다).
- Amazon Bedrock, Google Cloud Vertex AI 또는 Microsoft Foundry에서는 **사용할 수 없습니다**.

### 세 가지 실행 방법

- **명령어**: `/ultraplan <prompt>` — 명시적 호출.
- **키워드**: 일반 프롬프트에 `ultraplan` 단어를 포함하면 Claude가 요청을 클라우드로 라우팅합니다.
- **로컬 계획에서**: Claude가 로컬에서 계획을 완료한 후 승인 대화 상자에서 "아니요, Claude Code on the web에서 Ultraplan으로 정교화"를 선택하여 더 심층적인 조사를 위해 초안을 넘깁니다.

### 사용 예시

```bash
/ultraplan migrate the auth service from sessions to JWTs
```

Claude는 승인하고 클라우드 환경을 시작한 다음 (v2.1.101+에서 처음 실행 시 자동 생성), 브라우저에서 열 수 있는 세션 링크를 반환합니다.

### 상태 표시기

| 상태 | 의미 |
|---|---|
| `◇ ultraplan` | Claude가 코드베이스를 조사하고 계획 초안을 작성 중입니다 |
| `◇ ultraplan needs your input` | Claude가 명확한 질문을 가지고 있습니다. 세션 링크를 열어 응답하십시오 |
| `◆ ultraplan ready` | 브라우저에서 계획을 검토할 준비가 되었습니다 |

### 실행 옵션

계획이 준비되면 두 가지 실행 경로가 있습니다. 브라우저에서 계획을 승인하여 동일한 클라우드 세션에서 실행하면 Claude가 원격으로 변경 사항을 구현하고 웹 UI에서 Pull Request를 엽니다. 또는 "계획 승인 및 터미널로 텔레포트"를 선택하여 로컬에서 구현할 수 있습니다. 터미널 텔레포트 대화 상자는 세 가지 선택지를 제공합니다:

- **여기서 구현** — 현재 터미널 세션에서 승인된 계획을 실행합니다.
- **새 세션 시작** — 동일한 작업 디렉토리에서 새 세션을 열고 거기서 구현합니다.
- **취소** — 계획을 파일로 저장하여 나중에 다시 시작할 수 있습니다.

> **경고**: 울트라플랜이 시작되면 원격 제어가 연결 해제됩니다. 두 기능 모두 claude.ai/code 인터페이스를 공유하므로 한 번에 하나만 활성화될 수 있습니다.

---

## 확장된 사고

확장된 사고는 Claude가 솔루션을 제공하기 전에 복잡한 문제에 대해 더 많은 시간을 추론하도록 허용합니다.

### 확장된 사고란 무엇입니까?

확장된 사고는 Claude가 다음을 수행하는 신중한 단계별 추론 프로세스입니다:
- 복잡한 문제를 분해합니다
- 여러 접근 방식을 고려합니다
- 장단점을 평가합니다
- 엣지 케이스를 통해 추론합니다

### 확장된 사고 활성화

**키보드 단축키**:
- `Option + T` (macOS) / `Alt + T` (Windows/Linux) - 확장된 사고 전환

**자동 활성화**:
- 모든 모델 (Opus 4.8, Opus 4.7, Sonnet 4.6, Haiku 4.5)에 기본적으로 활성화되어 있습니다.
- Opus 4.8: 노력 수준이 있는 적응형 추론: `low` (○), `medium` (◐), `high` (●), `xhigh`, `max`. 기본값은 Opus 4.8 (v2.1.154), Opus 4.6, Sonnet 4.6에서는 `high`이고, Opus 4.7에서는 `xhigh`입니다. `xhigh`는 Opus 4.8 및 Opus 4.7에서 사용할 수 있습니다 (Opus 4.6 / Sonnet 4.6에서는 `high`로 대체됩니다). `max`는 Opus 4.8/4.7/4.6 및 Sonnet 4.6에서 작동합니다 (세션 전용). Haiku 4.5에는 노력 수준이 없습니다. Opus 4.8 및 Opus 4.7은 1M 토큰의 기본 컨텍스트 창을 가집니다 (1M 컨텍스트 수정은 v2.1.117에 적용됨 — 이전에는 `/context`가 Opus 4.7을 200K 창에 대해 잘못 계산하여 조기 자동 압축을 트리거했습니다). v2.1.129부터 `/context`는 UI 내에서만 시각화를 표시합니다. ASCII 시각화는 더 이상 대화 컨텍스트로 유출되지 않으므로 (호출당 약 1.6k 토큰 절약), `/context`는 자유롭게 호출해도 안전합니다.
- Opus 4.6 / Sonnet 4.6의 Pro/Max 구독자: v2.1.117에서 기본 노력 수준이 `medium`에서 `high`로 상향 조정되었습니다.
- 다른 모델: 최대 31,999 토큰의 고정 예산

**구성 방법**:
- 전환: `Alt+T` / `Option+T`, 또는 `/config`를 통해
- 추론 보기: `Ctrl+O` (자세한 모드)
- 노력 설정: `/effort` 명령어 또는 `--effort` 플래그

**사용자 지정 예산**:
```bash
export MAX_THINKING_TOKENS=1024
```

**노력 수준** (Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6에서 지원 — Haiku 4.5 제외):
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○), medium (◐), high (●), xhigh (Opus 4.8/4.7), or max — default is high on Opus 4.8
```

**CLI 플래그**:
```bash
claude --effort high "complex architectural review"
```

**슬래시 명령어**:
```
/effort high
```

> **참고:** 프롬프트의 "ultrathink" 키워드는 심층 추론 모드를 활성화합니다. 노력 수준 `low`, `medium`, `high`, `max`는 Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6에서 지원됩니다 (Haiku 4.5는 지원하지 않음). `xhigh`는 Opus 4.8 및 Opus 4.7에서 사용할 수 있습니다. 기본 노력 수준은 Opus 4.8 (및 Opus 4.6 / Sonnet 4.6)에서 `high`이고 Opus 4.7에서 `xhigh`입니다. `/effort` 메뉴는 `ultracode`도 제공하는데, 이는 모델 노력 수준이 **아니며** `xhigh`를 보내고 Claude가 동적 워크플로우를 조율하도록 합니다 (세션 전용).

### 확장된 사고의 이점

- **심층 추론**: 복잡한 문제에 대해 더 많은 시간을 할애하여 생각
- **더 나은 아키텍처 결정**: 포괄적인 평가를 통해 정보에 입각한 선택
- **엣지 케이스 고려**: 잠재적 문제 및 시나리오에 대한 심층적 사고
- **철저한 분석**: 복잡한 문제 해결을 위한 구조화된 접근 방식

### 예시: 아키텍처 결정

```
User: ultrathink Should we use microservices or a monolith for our e-commerce platform?

Claude: 이 아키텍처 결정을 신중하게 고려해 보겠습니다...

<extended_thinking>
## Context Analysis
- Team size: 5 developers
- Expected traffic: 10k daily users initially
- Need to scale to 100k+ users
- Limited DevOps resources
- 6-month timeline to MVP

## Approach 1: Microservices
Pros:
+ Independent scaling
+ Technology flexibility
+ Team independence
+ Fault isolation

Cons:
- Operational complexity
- Network overhead
- Distributed tracing needed
- Requires DevOps expertise
- Slower initial development

## Approach 2: Monolith
Pros:
+ Simpler deployment
+ Faster initial development
+ Easier debugging
+ Lower operational overhead
+ Single codebase

Cons:
- Scaling challenges later
- All-or-nothing deployments
- Technology lock-in
- Potential for tight coupling

## Decision Factors
1. Team size (5 devs) → Favors monolith
2. DevOps resources (limited) → Favors monolith
3. Timeline (6 months) → Favors monolith
4. Future scale (100k users) → Achievable with monolith + caching
5. Complexity budget → Limited

## Recommendation
Start with a **modular monolith**:
- Single deployment unit
- Clear module boundaries
- Clean interfaces between modules
- Prepare for future extraction to microservices if needed

This gives you:
✓ Fast initial development
✓ Low operational complexity
✓ Option to extract services later
✓ Clear architecture

Migration path: When you reach 50k+ users or specific modules need independent scaling, extract those modules into microservices.
</extended_thinking>

**Recommendation**: 깔끔한 모듈 경계를 가진 모듈형 모놀리스를 구현하십시오.

이 접근 방식은 현재 제약 사항(팀 규모, 기한, DevOps 리소스)과 향후 확장성 요구 사항의 균형을 맞춥니다. 명확한 비즈니스 필요성이 있을 때 특정 모듈을 나중에 마이크로 서비스로 마이그레이션할 수 있습니다.
```

### 확장된 사고 구성

확장된 사고는 환경 변수, 키보드 단축키 및 CLI 플래그를 통해 제어됩니다:

```bash
# Set thinking token budget
export MAX_THINKING_TOKENS=16000

# Set effort level (Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6): low (○), medium (◐), high (●), xhigh (Opus 4.8/4.7), or max — default is high on Opus 4.8
export CLAUDE_CODE_EFFORT_LEVEL=high
```

세션 중에 `Alt+T` / `Option+T`로 전환하거나 `/effort`로 노력 수준을 설정하거나 `/config`를 통해 구성할 수 있습니다.

> **간소화된 시스템 프롬프트 (v2.1.154):** 간소화된 시스템 프롬프트는 이제 Haiku, Sonnet, Opus 4.7 및 이전 버전을 제외한 모든 모델의 **기본값**으로, Opus 4.8의 기본 토큰 오버헤드를 줄입니다.

---

## 자동 모드

자동 모드는 배경 안전 분류기를 사용하여 각 작업을 실행하기 전에 검토하는 연구 미리보기 권한 모드입니다 (2026년 3월). Claude가 자율적으로 작업하면서 위험한 작업을 차단할 수 있도록 합니다.

### 요구 사항

- **플랜**: Team, Enterprise 또는 API (Pro 또는 Max 플랜에서는 사용할 수 없음)
- **모델**: Claude Sonnet 4.6 또는 Opus 4.8
- **제공자**: Anthropic API만 해당 (Bedrock, Vertex 또는 Foundry에서는 지원되지 않음)
- **분류기**: Claude Sonnet 4.6에서 실행 (추가 토큰 비용 발생)

### 자동 모드 활성화

```bash
# Unlock auto mode with CLI flag (no longer required for Max subscribers on Opus 4.7 — access it directly)
claude --enable-auto-mode

# Then cycle to it with Shift+Tab in the REPL
```

> **v2.1.112 업데이트**: 자동 모드는 더 이상 `--enable-auto-mode` 플래그를 필요로 하지 않습니다. Max 구독자는 Opus 4.7에서 직접 액세스할 수 있습니다.

> **v2.1.158 업데이트**: 자동 모드는 이제 Opus 4.7/4.8용 Bedrock, Vertex, Foundry에서 사용할 수 있습니다 — `CLAUDE_CODE_ENABLE_AUTO_MODE=1`을 설정하여 **옵트인**하십시오.

또는 기본 권한 모드로 설정:

```bash
claude --permission-mode auto
```

구성으로 설정:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 분류기 작동 방식

배경 분류기는 다음 결정 순서를 사용하여 각 작업을 평가합니다:

1. **허용/거부 규칙** -- 명시적인 권한 규칙이 먼저 확인됩니다.
2. **읽기 전용/편집 자동 승인** -- 파일 읽기 및 편집은 자동으로 통과됩니다.
3. **분류기** -- 배경 분류기가 작업을 검토합니다.
4. **대체** -- 3회 연속 또는 총 20회 차단 후 프롬프트로 대체됩니다.

### 기본 차단 작업

자동 모드는 기본적으로 다음을 차단합니다:

| 차단된 작업 | 예시 |
|----------------|---------|
| 파이프-투-쉘 설치 | `curl \| bash` |
| 민감한 데이터 외부 전송 | API 키, 네트워크를 통한 자격 증명 |
| 프로덕션 배포 | 프로덕션을 대상으로 하는 배포 명령 |
| 대량 삭제 | 대규모 디렉토리에 대한 `rm -rf` |
| IAM 변경 | 권한 및 역할 수정 |
| main으로 강제 푸시 | `git push --force origin main` |

### 기본 허용 작업

| 허용된 작업 | 예시 |
|----------------|---------|
| 로컬 파일 작업 | 프로젝트 파일 읽기, 쓰기, 편집 |
| 선언된 종속성 설치 | 매니페스트에서 `npm install`, `pip install` |
| 읽기 전용 HTTP | 문서 가져오기를 위한 `curl` |
| 현재 브랜치로 푸시 | `git push origin feature-branch` |

### 자동 모드 구성

**기본 규칙을 JSON으로 출력**:
```bash
claude auto-mode defaults
```

엔터프라이즈 배포를 위해 `autoMode.environment` 관리형 설정을 통해 **신뢰할 수 있는 인프라**를 구성합니다. 이를 통해 관리자는 신뢰할 수 있는 CI/CD 환경, 배포 대상 및 인프라 패턴을 정의할 수 있습니다.

#### `"$defaults"`로 기본값 확장 (v2.1.118)

v2.1.118부터 `autoMode.allow`, `autoMode.soft_deny`, `autoMode.environment`는 `"$defaults"` 토큰을 허용하여 기본 제공 목록을 **교체하는 대신** 사용자 규칙을 **추가**합니다. v2.1.118 이전에는 사용자 정의 배열이 기본 제공 목록을 자동으로 덮어썼습니다.

#### `autoMode.hard_deny`를 사용한 무조건적인 차단 (v2.1.136)

`autoMode.hard_deny` (v2.1.136+)는 **추론된 사용자 의도와 관계없이** 특정 유형의 작업을 차단하는 분류기 규칙 배열입니다. 자동 모드에서 절대로 실행되어서는 안 되는 작업에 사용하십시오. 예를 들어, 루트 경로의 `rm -rf` 또는 보호된 브랜치의 `git push --force`가 있습니다. `soft_deny`와 달리 hard-deny 규칙은 분류기에 의해 협상될 수 없습니다.

```json
{
  "autoMode": {
    "hard_deny": ["Bash(rm -rf /:*)", "Bash(git push --force*)"]
  }
}
```

**이전 (기본 제공 항목 대체 — v2.1.118 이전 동작):**

```json
{
  "autoMode": {
    "allow": ["Bash(gh pr list:*)"]
  }
}
```

**이후 (기본 제공 항목 확장 — v2.1.118+):**

```json
{
  "autoMode": {
    "allow": ["$defaults", "Bash(gh pr list:*)"],
    "soft_deny": ["$defaults", "Bash(kubectl delete:*)"],
    "environment": ["$defaults", "trusted-ci.internal"]
  }
}
```

`"$defaults"`를 사용하여 기본 규칙을 유지하면서 조직 또는 프로젝트별 추가 기능을 계층화할 수 있습니다.

#### `autoMode.classifyAllShell`을 사용하여 모든 쉘 명령 분류 (v2.1.193)

`autoMode.classifyAllShell` (부울, v2.1.193+)은 **모든** Bash/PowerShell 명령을 자동 모드 분류기를 통해 라우팅합니다. 분류기가 세션의 모든 쉘 명령을 검사하도록 하려면 이 기능을 활성화하십시오.

```json
{
  "autoMode": {
    "classifyAllShell": true
  }
}
```

같은 릴리스에서 자동 모드가 작업을 차단할 때 **거부 사유**가 표시됩니다 — 트랜스크립트, 거부 토스트, `/permissions` 아래의 최근 거부 목록에서 볼 수 있습니다 (v2.1.193+).

#### 내장된 의도 기반 보호 (v2.1.183)

사용자가 구성하는 `hard_deny`와 별도로, 자동 모드는 다음과 같은 파괴적인 명령을 이 세션에서 명시적으로 요청하지 않는 한 기본적으로 차단합니다:

- `git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`
- `git commit --amend` (커밋이 이 세션에서 에이전트에 의해 만들어지지 않은 경우)
- `terraform destroy`, `pulumi destroy`, `cdk destroy` (특정 스택을 요청하지 않는 한)

이는 추론된 의도에 기반한 내장된 기본 보호 기능입니다. 이러한 항목을 `hard_deny`에 직접 추가할 필요가 없습니다.

### 대체 동작

분류기가 불확실할 때 자동 모드는 사용자에게 프롬프트를 표시하는 것으로 대체됩니다:
- **3회 연속** 분류기 차단 후
- 세션에서 **총 20회** 분류기 차단 후

이는 분류기가 작업을 자신 있게 승인할 수 없을 때 사용자가 항상 제어권을 유지하도록 보장합니다.

### 자동 모드와 동등한 권한 시드 (팀 플랜 불필요)

팀 플랜이 없거나 배경 분류기 없이 더 간단한 접근 방식을 원한다면, `~/.claude/settings.json`에 보수적인 안전 권한 규칙의 기준선을 시드할 수 있습니다. 스크립트는 읽기 전용 및 로컬 검사 규칙으로 시작한 다음, 편집, 테스트, 로컬 Git 쓰기, 패키지 설치 및 GitHub 쓰기 작업은 원할 때만 옵트인할 수 있도록 합니다.

**파일:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Preview what would be added (no changes written)
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Apply the conservative baseline
python3 09-advanced-features/setup-auto-mode-permissions.py

# Add more capability only when you need it
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

스크립트는 다음 범주에 걸쳐 규칙을 추가합니다:

| 범주 | 예시 |
|----------|---------|
| 핵심 읽기 전용 도구 | `Read(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)`, `WebFetch(*)` |
| 로컬 검사 | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)`, `Bash(cat:*)` |
| 선택적 편집 | `Edit(*)`, `Write(*)`, `NotebookEdit(*)` |
| 선택적 테스트/빌드 | `Bash(pytest:*)`, `Bash(python3 -m pytest:*)`, `Bash(cargo test:*)` |
| 선택적 Git 쓰기 | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git stash:*)` |
| Git (로컬 쓰기) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| 패키지 관리자 | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| 빌드 및 테스트 | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| 일반 쉘 | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

위험한 작업 (`rm -rf`, `sudo`, 강제 푸시, `DROP TABLE`, `terraform destroy` 등)은 의도적으로 제외됩니다. 스크립트는 멱등성이 있으므로 두 번 실행해도 규칙이 중복되지 않습니다.

---

## 백그라운드 작업

백그라운드 작업은 장기 실행 작업을 대화를 차단하지 않고 실행할 수 있도록 합니다.

### 백그라운드 작업이란 무엇입니까?

백그라운드 작업은 계속 작업하는 동안 비동기적으로 실행됩니다:
- 긴 테스트 스위트
- 빌드 프로세스
- 데이터베이스 마이그레이션
- 배포 스크립트
- 분석 도구

**기본 사용법:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### 백그라운드 작업 시작

```
User: Run the full test suite in the background

Claude: 백그라운드에서 테스트를 시작합니다 (task-id: bg-1234)
테스트가 실행되는 동안 작업을 계속할 수 있습니다.

[대화를 계속할 수 있습니다]

User: Meanwhile, let's refactor the auth module

Claude: [테스트가 백그라운드에서 실행되는 동안 인증 모듈을 리팩토링합니다]

[나중에, 테스트가 완료되면]

Claude: 📢 백그라운드 작업 bg-1234 완료:
✅ 245 tests passed
❌ 3 tests failed
결과 보기: /task show bg-1234
```

### 백그라운드 작업 관리

**활성 작업 목록**:
```
User: /task list

Active background tasks:
1. [bg-1234] Running tests (50% complete, 2min remaining)
2. [bg-1235] Building Docker image (25% complete, 8min remaining)
3. [bg-1236] Deploying to staging (90% complete, 30sec remaining)
```

**작업 상태 확인**:
```
User: /task status bg-1234

Task bg-1234: Running tests
Status: In progress
Progress: 120/245 tests (49%)
Started: 2025-11-08 10:30:15
Estimated completion: 2025-11-08 10:34:22
```

**작업 출력 보기**:
```
User: /task show bg-1234

[테스트 실행의 실시간 출력을 보여줍니다]
```

**작업 취소**:
```
User: /task cancel bg-1234

Cancelled background task bg-1234
```

### 예시: 병렬 개발

```
User: Run the build in the background

Claude: 빌드를 시작합니다... (task-id: bg-5001)

User: Also run the linter in background

Claude: 린터를 시작합니다... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [빌드 및 린터가 실행되는 동안 API 엔드포인트를 구현합니다]

[10분 후]

Claude: 📢 빌드 성공적으로 완료됨 (bg-5001)
📢 린터에서 12개의 문제 발견됨 (bg-5002)

User: Show me the linter issues

Claude: [bg-5002의 린터 출력을 보여줍니다]
```

### 구성

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## 모니터 도구 (이벤트 기반 스트림)

> **v2.1.98에 새로 추가**: 모니터 도구를 사용하면 Claude가 백그라운드 명령의 stdout을 관찰하고 일치하는 이벤트가 나타나는 즉시 반응할 수 있습니다. 이는 폴링 루프와 `sleep`을 긴 프로세스 대기 대신 대체합니다.

모니터는 stdout에 쓰는 모든 쉘 명령에 연결됩니다. 명령에서 나오는 각 stdout 줄은 세션을 깨우는 알림이 됩니다. Claude가 명령을 지정하면, 하네스가 출력을 스트리밍하고 이벤트가 발생하면 전달합니다. 기본 프로세스 실행에 대해서는 관련 [백그라운드 작업](#백그라운드-작업) 섹션을 참조하십시오.

### 왜 중요한가요?

`/loop` 또는 `sleep`을 사용하는 폴링은 변경 사항이 있는지 여부와 관계없이 매 주기마다 전체 API 왕복을 소모합니다. 모니터는 이벤트가 발생할 때까지 조용히 있다가 명령이 조용할 때는 **토큰을 전혀 소비하지 않습니다**. 이벤트가 발생하면 Claude는 즉시 반응하며, 다음 폴링 주기까지 기다리지 않고 지연 없이 문제를 해결합니다. 몇 분 이상 실행되는 모든 작업에 대해 이는 폴링 루프보다 저렴하고 빠릅니다.

### 두 가지 일반적인 패턴

**스트림 필터**는 장기 실행 소스에서 지속적인 출력을 관찰합니다. 명령은 영원히 실행되며, 일치하는 모든 줄이 이벤트가 됩니다.

```bash
tail -f /var/log/app.log | grep --line-buffered "ERROR"
```

**폴-앤-이밋 필터**는 주기적으로 소스를 확인하고 변경 사항이 있을 때만 이벤트를 발생시킵니다. API, 데이터베이스 또는 기본 스트림이 없는 모든 것에 사용하십시오.

```bash
last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
while true; do
  gh api "repos/owner/repo/issues/123/comments?since=$last" || true
  last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  sleep 30
done
```

### 구체적인 예시

"내 개발 서버를 시작하고 오류를 모니터링해 줘." Claude는 서버를 백그라운드 작업으로 시작하고, 모니터 필터 (`tail -F server.log | grep --line-buffered -E "ERROR|FATAL"`)를 연결하며, 세션은 조용해집니다. 로그에 오류 줄이 나타나는 순간, Claude는 깨어나 오류를 읽고 반응할 수 있습니다. 서버를 재시작하거나 버그를 수정하거나 사용자에게 알릴 수 있으며, 사용자가 직접 확인할 필요가 없습니다.

> **경고**: `grep`으로 파이핑할 때 **항상** `grep --line-buffered`를 사용하십시오. 이를 사용하지 않으면 grep이 stdout을 4KB 청크로 버퍼링하여 트래픽이 적은 스트림에서 이벤트가 몇 분 지연될 수 있습니다. 이는 실제로 모니터가 중단되는 가장 흔한 방법입니다. 필터가 작동해야 할 때 침묵하는 것처럼 보이면 먼저 `--line-buffered` 플래그를 확인하십시오.

---

## 동적 워크플로우

> **v2.1.154에 새로 추가**

동적 워크플로우를 사용하면 Claude가 수십에서 수백 개의 백그라운드 [서브에이전트](../04-subagents/README.md)를 **결정적으로** 조율할 수 있습니다. 즉, 팬아웃, 파이프라인 및 병렬 단계가 모델의 즉흥 연주에 맡겨지는 대신 스크립트에 인코딩됩니다. 단일 에이전트가 하나의 컨텍스트 창을 유지하는 반면, 워크플로우는 많은 에이전트에 걸쳐 작업을 분해하고 그 결과를 재결합합니다.

### 사용 시점

- **포괄적인 범위** — 많은 파일/차원에 걸쳐 병렬로 감사 또는 검토.
- **신뢰성** — 독립적인 관점을 생성한 다음, 커밋하기 전에 발견 사항을 적대적으로 검증.
- **단일 컨텍스트를 넘어서는 확장** — 대규모 마이그레이션, 광범위한 조사 또는 단일 컨텍스트로는 담을 수 없는 연구.

이미 이해하고 있는 일회성 작업의 경우, 단일 에이전트 (또는 직접 편집)가 여전히 올바른 도구입니다. 워크플로우는 작업이 분산될 때 효과를 발휘합니다.

### 실행 및 보기

- **실행**: Claude에게 작업을 위한 워크플로우를 생성하도록 요청합니다 (예: "`src/`의 모든 파일을 검토하는 워크플로우를 실행해 줘"). Claude는 오케스트레이션 스크립트를 작성하고 백그라운드에서 실행합니다.
- **보기**: `/workflows` 명령은 라이브 진행 상황과 함께 실행 중이거나 완료된 워크플로우 실행을 표시합니다.
- **`ultracode`**: `/effort` 메뉴에서 `ultracode`를 선택하면 세션에 대해 이 기능이 켜집니다. 이는 모델에 `xhigh`를 보내고 Claude가 기본적으로 동적 워크플로우를 조율하도록 합니다. 이 기능은 세션 전용이며 설정 파일에서는 허용되지 않습니다. (v2.1.160부터 트리거 키워드는 `ultracode`이며, "workflow" 단어만으로는 더 이상 실행되지 않습니다.)

워크플로우는 서브에이전트 모델을 기반으로 구축됩니다. 개별 에이전트가 정의되고 범위가 지정되는 방법은 [서브에이전트](../04-subagents/README.md)를 참조하십시오.

---

## 예약된 작업

예약된 작업을 사용하면 반복적인 일정 또는 일회성 알림으로 프롬프트를 자동으로 실행할 수 있습니다. 작업은 세션 범위이며, Claude Code가 활성 상태일 때 실행되고 세션이 종료되면 지워집니다. v2.1.72+부터 사용할 수 있습니다.

> **claude.com에서 "Routines"로 마케팅됨 (2026-05-14)**: Anthropic의 제품 블로그는 이 기능을 **Routines**로 소개합니다. CLI 명령은 `/schedule`로 유지되며, 이 가이드는 연속성을 위해 원래의 "예약된 작업" 명칭을 사용합니다. claude.com 문서나 데스크톱 앱에서 "Routines"를 본다면, 동일한 기능을 의미합니다.

### `/loop` 명령어

```bash
# Explicit interval
/loop 5m check if the deployment finished

# Natural language
/loop check build status every 30 minutes
```

정확한 스케줄링을 위해 표준 5필드 크론 표현식도 지원됩니다.

### 일회성 알림

특정 시간에 한 번 발생하는 알림을 설정합니다:

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### 예약된 작업 관리

| 도구 | 설명 |
|------|-------------|
| `CronCreate` | 새 예약 작업 생성 |
| `CronList` | 모든 활성 예약 작업 나열. v2.1.136부터 출력에는 한정자 및 예약된 프롬프트 본문도 포함되어 각 크론이 실행될 내용을 열지 않고도 감사할 수 있습니다. |
| `CronDelete` | 예약 작업 제거 |

**제한 및 동작**:
- 세션당 최대 **50개의 예약된 작업**
- 세션 범위 — 세션이 종료되면 지워집니다
- 반복 작업은 **3일** 후 자동 만료됩니다
- Claude Code가 실행 중일 때만 작업이 발생합니다 — 놓친 작업에 대한 따라잡기는 없습니다

### 동작 세부 정보

| 측면 | 세부 사항 |
|--------|--------|
| **반복 지터** | 간격의 최대 10% (최대 15분) |
| **일회성 지터** | :00/:30 경계에서 최대 90초 |
| **놓친 발동** | 따라잡기 없음 — Claude Code가 실행 중이 아니면 건너뜀 |
| **영속성** | 재시작 시 영속되지 않음 |

### 클라우드 예약 작업

`/schedule`을 사용하여 Anthropic 인프라에서 실행되는 클라우드 예약 작업을 생성합니다:

```
/schedule daily at 9am run the test suite and report failures
```

클라우드 예약 작업은 재시작 시 영속되며 Claude Code가 로컬에서 실행 중일 필요가 없습니다.

### 예약된 작업 비활성화

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

> **`/schedule` API 키 티어에 의해 자동 비활성화됨 (v2.1.139)**: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, 또는 `apiKeyHelper` 중 하나라도 설정되어 있으면 클라우드 `/schedule`은 자동으로 비활성화됩니다. claude.ai로 로그인되어 있는 경우에도 마찬가지입니다. 동일한 조건으로 [원격 제어 비활성화](#원격-제어-비활성화-disableremotecontrol-v21128), claude.ai MCP 커넥터, 알림 설정이 비활성화됩니다. `/schedule`을 사용하려면 API 키를 해제하거나 Pro/Max OAuth 티어에서 실행하십시오. 로컬 `CronCreate`에는 영향을 미치지 않습니다.

### 예시: 배포 모니터링

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **팁**: 예약된 작업은 세션 범위입니다. 재시작 후에도 유지되는 영구적인 자동화를 위해서는 CI/CD 파이프라인, GitHub Actions 또는 데스크톱 앱 예약 작업을 대신 사용하십시오.

---

## 권한 모드

권한 모드는 Claude가 명시적인 승인 없이 수행할 수 있는 작업을 제어합니다.

### 사용 가능한 권한 모드

| 모드 | 동작 |
|---|---|
| `default` | 파일만 읽음; 다른 모든 작업에 대해 프롬프트를 표시 |
| `acceptEdits` | 파일 읽기 및 편집; 명령에 대해 프롬프트를 표시 |
| `plan` | 파일만 읽음 (연구 모드, 편집 불가) |
| `auto` | 배경 안전 분류기 검사를 통한 모든 작업 (연구 미리보기) |
| `bypassPermissions` | 모든 작업, 권한 검사 없음 (위험) |
| `dontAsk` | 미리 승인된 도구만 실행; 다른 모든 것은 거부 |

CLI에서 `Shift+Tab`으로 모드를 순환할 수 있습니다. `--permission-mode` 플래그 또는 `permissions.defaultMode` 설정을 사용하여 기본값을 설정합니다.

v2.1.160 현재, `acceptEdits` 모드에서도 쉘 시작 파일 (`.zshenv`, `.zlogin`, `.bash_login`, `~/.config/git/`) 및 코드 실행 빌드 구성 (`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`, `.pre-commit-config.yaml`, `.devcontainer/`, …)을 작성하기 전에 프롬프트를 표시합니다. 이는 의도치 않은 명령 실행을 방지하기 위함입니다.

> **`--dangerously-skip-permissions` 확장 경로 범위 (v2.1.121, v2.1.126)**: `--dangerously-skip-permissions` CLI 플래그 (및 동등한 `bypassPermissions` 모드)는 이제 훨씬 더 광범위한 허용 목록 (`.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/`, `.git/`, `.vscode/`, 쉘 구성 파일)에 대한 쓰기 프롬프트를 우회합니다. 재앙적인 삭제 명령 (`rm -rf /` 등)은 모드와 관계없이 여전히 프롬프트를 표시합니다. 이 플래그는 이전보다 더 날카로운 도구로 취급하십시오. 일회용 샌드박스에서만 사용하십시오.

> **Windows 쉘 감지 (v2.1.120, v2.1.126)**: Git for Windows / Git Bash는 더 이상 필수가 아닙니다. Git Bash가 없으면 Claude Code는 PowerShell을 쉘 도구로 사용합니다. v2.1.126부터 PowerShell 도구가 활성화되면 PowerShell이 *기본* 쉘이며, Microsoft Store, PATH가 없는 MSI, 또는 `.NET 전역 도구`를 통해 설치된 PowerShell 7도 감지합니다.

> **PowerShell 도구가 Windows용 Bedrock/Vertex/Foundry에서 기본적으로 활성화됨 (v2.1.143)**: v2.1.143부터 PowerShell 도구는 Bedrock, Vertex, Foundry 사용자를 위해 **Windows에서 기본적으로 활성화됩니다**. Claude Code는 `-ExecutionPolicy Bypass`로 PowerShell을 호출하므로 시스템 정책이 `Restricted`인 경우에도 스크립트가 실행됩니다. Claude Code가 시스템 실행 정책을 따르도록 하려면 `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`을 설정하십시오. PowerShell 도구를 완전히 비활성화하려면 `CLAUDE_CODE_USE_POWERSHELL_TOOL=0`을 설정하십시오.

### 활성화 방법

**키보드 단축키**:
```bash
Shift + Tab  # 6가지 모드 모두 순환
```

**슬래시 명령어**:
```bash
/plan                  # 기획 모드 진입
```

**CLI 플래그**:
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**설정**:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 권한 모드 예시

#### 기본 모드
Claude는 중요한 작업에 대해 확인을 요청합니다:

```
User: Fix the bug in auth.ts

Claude: src/auth.ts 파일을 수정하여 버그를 수정해야 합니다.
변경 사항은 비밀번호 유효성 검사 로직을 업데이트할 것입니다.

이 변경 사항을 승인하시겠습니까? (yes/no/show)
```

#### 기획 모드
실행 전에 구현 계획을 검토합니다:

```
User: /plan Implement user authentication system

Claude: 인증 시스템 구현을 위한 계획을 생성하겠습니다.

## Implementation Plan
[단계 및 절차가 포함된 상세 계획]

계속 진행하시겠습니까? (yes/no/modify)
```

#### 편집 승인 모드
파일 수정 사항을 자동으로 승인합니다:

```
User: acceptEdits
User: Fix the bug in auth.ts

Claude: [묻지 않고 변경 사항을 적용합니다]
```

### 사용 사례

**코드 검토**:
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [코드를 읽고 피드백을 제공하지만 수정할 수는 없습니다]
```

**페어 프로그래밍**:
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [각 변경 사항 전에 승인을 요청합니다]
```

**자동화된 작업**:
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [파일 편집을 묻지 않고 자동 승인합니다]
```

---

## 헤드리스 모드

인쇄 모드 (`claude -p`)는 Claude Code를 대화형 입력 없이 실행할 수 있도록 하여 자동화 및 CI/CD에 완벽합니다. 이는 이전의 `--headless` 플래그를 대체하는 비대화형 모드입니다.

### 인쇄 모드에서 실행 (비대화형)

인쇄 모드는 다음을 가능하게 합니다:
- 자동화된 스크립트 실행
- CI/CD 통합
- 배치 처리
- 예약된 작업

### 인쇄 모드에서 실행 (비대화형)

```bash
# 특정 작업 실행
claude -p "Run all tests"

# 파이프된 내용 처리
cat error.log | claude -p "Analyze these errors"

# CI/CD 통합 (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### 추가 인쇄 모드 사용 예시

```bash
# 출력 캡처를 통해 특정 작업 실행
claude -p "Run all tests and generate coverage report"

# 구조화된 출력으로
claude -p --output-format json "Analyze code quality"

# stdin에서 입력받기
echo "Analyze code quality" | claude -p "explain this"
```

### 예시: CI/CD 통합

**GitHub Actions**:
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### 인쇄 모드 구성

인쇄 모드 (`claude -p`)는 자동화를 위한 여러 플래그를 지원합니다:

```bash
# 자율적 턴 제한
claude -p --max-turns 5 "refactor this module"

# 구조화된 JSON 출력
claude -p --output-format json "analyze this codebase"

# 스키마 유효성 검사 포함
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# 세션 영속성 비활성화
claude -p --no-session-persistence "one-off analysis"
```

### 안전 모드 (문제 해결)

`--safe-mode` (및 `CLAUDE_CODE_SAFE_MODE` 환경 변수, 예: `CLAUDE_CODE_SAFE_MODE=1`)는 **모든 사용자 정의를 비활성화**한 상태로 Claude Code를 시작합니다. CLAUDE.md, 플러그인, 스킬, 훅 및 MCP 서버가 모두 꺼집니다.

```bash
# 모든 사용자 정의를 비활성화한 상태로 실행
claude --safe-mode

# 환경 변수를 통한 동등한 방법
CLAUDE_CODE_SAFE_MODE=1 claude
```

이것은 문제 해결 도구입니다. 사용자 정의 구성이 문제를 일으키는 경우, 안전 모드로 시작하여 문제가 사용자 설정에 있는지 Claude Code 자체에 있는지 격리하여 확인할 수 있습니다.

---

## 세션 관리

여러 Claude Code 세션을 효과적으로 관리합니다.

### 세션 관리 명령어

| 명령어 | 설명 |
|---------|-------------|
| `/resume` | ID 또는 이름으로 대화 다시 시작 |
| `/rename` | 현재 세션 이름 지정 |
| `/fork` | 현재 세션을 새 브랜치로 포크 |
| `claude -c` | 가장 최근 대화 계속 |
| `claude -r "session"` | 이름 또는 ID로 세션 다시 시작 |

### 세션 다시 시작

**가장 최근 대화 계속**:
```bash
claude -c
```

**이름 지정된 세션 다시 시작**:
```bash
claude -r "auth-refactor" "finish this PR"
```

**현재 세션 이름 변경** (REPL 내부):
```
/rename auth-refactor
```

### 세션 포크

원본을 잃지 않고 다른 접근 방식을 시도하기 위해 세션을 포크합니다:

```
/fork
```

또는 CLI에서:
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### 세션 영속성

세션은 자동으로 저장되며 다시 시작할 수 있습니다:

```bash
# 가장 최근 대화 계속
claude -c

# 이름 또는 ID로 특정 세션 다시 시작
claude -r "auth-refactor"

# 실험을 위해 세션 다시 시작 및 포크
claude --resume auth-refactor --fork-session "alternative approach"
```

### 세션 요약 (v2.1.108)

오랫동안 떨어져 있던 세션으로 돌아오면 Claude가 수행된 작업에 대한 간략한 요약을 표시할 수 있습니다. 이 기능은 원격 분석이 비활성화된 사용자 (Bedrock, Vertex, Foundry 사용자)에게 기본적으로 활성화되어 있습니다.

> **OTEL 원격 측정 — 피드백 설문조사 재활성화 (v2.1.136+)**: OpenTelemetry 데이터를 캡처하는 조직은 `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL=1`을 설정하여 Anthropic의 세션 품질 설문조사를 다시 활성화할 수 있습니다. 설문조사는 이전에 원격 측정 파이프라인에서 리디렉션되었기 때문에 OTEL 배포에서는 기본적으로 꺼져 있습니다.

> **OTEL 원격 측정 — `assistant_response` 로그 이벤트 (v2.1.193+)**: Claude Code는 모델의 응답 텍스트를 담은 `claude_code.assistant_response` OpenTelemetry 로그 이벤트를 방출하여 OTEL 파이프라인이 기존 도구/이벤트 원격 측정과 함께 Claude가 말한 내용을 캡처할 수 있도록 합니다.

**요약 동작 제어:**

```bash
/recap                                 # 수동으로 요약 트리거
/config                                # 자동 요약 켜기/끄기 전환
```

또는 환경 변수를 통해:
```bash
CLAUDE_CODE_ENABLE_AWAY_SUMMARY=0 claude   # 요약 비활성화
CLAUDE_CODE_ENABLE_AWAY_SUMMARY=1 claude   # 요약 강제 활성화
```

---

## 대화형 기능

### 키보드 단축키

Claude Code는 효율성을 위한 키보드 단축키를 지원합니다. 다음은 공식 문서의 전체 참조입니다:

| 단축키 | 설명 |
|----------|-------------|
| `Ctrl+C` | 현재 입력/생성 취소 |
| `Ctrl+D` | Claude Code 종료 |
| `Ctrl+G` | 외부 편집기에서 계획 편집 |
| `Ctrl+L` | 터미널 화면 지우기 |
| `Ctrl+O` | 자세한 출력 전환 (추론 보기) |
| `Ctrl+R` | 기록 역방향 검색. **모든 프로젝트의 모든 프롬프트**를 기본으로 검색합니다 (v2.1.129+); 선택기 내에서 `Ctrl+S`를 누르면 현재 프로젝트로 범위를 좁힙니다. 이전 버전은 프로젝트 전용이 기본값이었습니다. |
| `Ctrl+T` | 작업 목록 보기 전환 |
| `Ctrl+B` | 백그라운드 작업 |
| `Esc+Esc` | 코드/대화 되감기 |
| `Shift+Tab` / `Alt+M` | 권한 모드 전환 |
| `Option+P` / `Alt+P` | 모델 전환 |
| `Option+T` / `Alt+T` | 확장된 사고 전환 |

**라인 편집 (표준 readline 단축키):**

| 단축키 | 동작 |
|----------|--------|
| `Ctrl + A` | 줄 시작으로 이동 |
| `Ctrl + E` | 줄 끝으로 이동 |
| `Ctrl + K` | 줄 끝까지 잘라내기 |
| `Ctrl + U` | 줄 시작까지 잘라내기 |
| `Ctrl + W` | 단어 뒤로 삭제 |
| `Ctrl + Y` | 붙여넣기 (yank) |
| `Tab` | 자동 완성 |
| `↑ / ↓` | 명령 기록 |

### 키 바인딩 사용자 지정

`/keybindings`를 실행하여 사용자 지정 키보드 단축키를 생성합니다. 이 명령은 `~/.claude/keybindings.json`을 열어 편집할 수 있도록 합니다 (v2.1.18+).

**구성 형식**:

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

기본 단축키를 해제하려면 바인딩을 `null`로 설정합니다.

### 사용 가능한 컨텍스트

키 바인딩은 특정 UI 컨텍스트에 따라 범위가 지정됩니다:

| 컨텍스트 | 주요 동작 |
|---------|-------------|
| **Chat** | `submit`, `cancel`, `cycleMode`, `modelPicker`, `thinkingToggle`, `undo`, `externalEditor`, `stash`, `imagePaste` |
| **Confirmation** | `yes`, `no`, `previous`, `next`, `nextField`, `cycleMode`, `toggleExplanation` |
| **Global** | `interrupt`, `exit`, `toggleTodos`, `toggleTranscript` |
| **Autocomplete** | `accept`, `dismiss`, `next`, `previous` |
| **HistorySearch** | `search`, `previous`, `next` |
| **Settings** | 컨텍스트별 설정 탐색 |
| **Tabs** | 탭 전환 및 관리 |
| **Help** | 도움말 패널 탐색 |

`Transcript`, `Task`, `ThemePicker`, `Attachments`, `Footer`, `MessageSelector`, `DiffDialog`, `ModelPicker`, `Select`를 포함하여 총 18개의 컨텍스트가 있습니다.

### 코드 지원

키 바인딩은 코드 시퀀스 (다중 키 조합)를 지원합니다:

```
"ctrl+k ctrl+s"   → 두 키 시퀀스: ctrl+k를 누른 다음 ctrl+s를 누릅니다
"ctrl+shift+p"    → 동시에 여러 보조 키를 누름
```

**키 입력 구문**:
- **수정자**: `ctrl`, `alt` (또는 `opt`), `shift`, `meta` (또는 `cmd`)
- **대문자는 Shift를 의미**: `K`는 `shift+k`와 동일
- **특수 키**: `escape`, `enter`, `return`, `tab`, `space`, `backspace`, `delete`, 화살표 키

### 예약 및 충돌 키

| 키 | 상태 | 참고 사항 |
|-----|--------|-------|
| `Ctrl+C` | 예약됨 | 재설정 불가 (인터럽트) |
| `Ctrl+D` | 예약됨 | 재설정 불가 (종료) |
| `Ctrl+B` | 터미널 충돌 | tmux 접두사 키 |
| `Ctrl+A` | 터미널 충돌 | GNU Screen 접두사 키 |
| `Ctrl+Z` | 터미널 충돌 | 프로세스 일시 중단 |

> **팁**: 단축키가 작동하지 않으면 터미널 에뮬레이터 또는 멀티플렉서와의 충돌을 확인하십시오.

### 탭 완성

Claude Code는 지능적인 탭 완성을 제공합니다:

```
User: /rew<TAB>
→ /rewind

User: /plu<TAB>
→ /plugin

User: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### 명령 기록

이전 명령에 액세스합니다:

```
User: <↑>  # 이전 명령
User: <↓>  # 다음 명령
User: Ctrl+R  # 기록 검색

(reverse-i-search)`test': run all tests
```

### 여러 줄 입력

복잡한 쿼리에는 여러 줄 모드를 사용하십시오:

```bash
User: \
> 여러 줄에 걸친
> 복잡한 프롬프트
> 입니다.
> \end
```

**예시:**

```
User: \
> 다음 요구 사항을 가진 사용자 인증 시스템을 구현하십시오:
> - JWT 토큰
> - 이메일 인증
> - 비밀번호 재설정
> - 2단계 인증 지원
> \end

Claude: [여러 줄 요청을 처리합니다]
```

### 인라인 편집

전송하기 전에 명령을 편집합니다:

```
User: Deploy to prodcution<Backspace><Backspace>uction

[전송하기 전에 현재 위치에서 편집]
```

### Vim 모드

텍스트 편집을 위한 Vi/Vim 키 바인딩을 활성화합니다:

**활성화**:
- `/config` (토글 "Editor / Vim mode") 또는 `~/.claude/settings.json`에서 `editorMode: "vim"`으로 활성화합니다. 독립형 `/vim` 슬래시 명령은 제거되었습니다 ( [issue #43370](https://github.com/anthropics/claude-code/issues/43370) 참조); 이제 vim 모드는 구성 기반입니다.
- `Esc`로 NORMAL, `i/a/o`로 INSERT, `v`로 VISUAL, `V`로 VISUAL-LINE 모드 전환 (v2.1.118+)

**탐색 키**:
- `h` / `l` - 왼쪽/오른쪽으로 이동
- `j` / `k` - 아래/위로 이동
- `w` / `b` / `e` - 단어 단위 이동
- `0` / `$` - 줄 시작/끝으로 이동
- `gg` / `G` - 텍스트 시작/끝으로 이동

**텍스트 객체**:
- `iw` / `aw` - 단어 내부/주변
- `i"` / `a"` - 인용된 문자열 내부/주변
- `i(` / `a(` - 괄호 내부/주변

**비주얼 모드 (v2.1.118+)**:

| 키 | 모드 | 동작 |
|-----|------|----------|
| `v` | Visual | 시각적 피드백이 있는 문자 단위 선택; 모션 키로 확장 |
| `V` | Visual-line | 줄 단위 선택; 항상 전체 줄 선택 |
| `y` | Yank | 현재 비주얼 선택 복사 |
| `d` / `x` | Delete | 현재 비주얼 선택 삭제 |
| `c` | Change | 선택 삭제 후 INSERT 모드 진입 |
| `Esc` | Exit | NORMAL 모드로 돌아가기 |

비주얼 선택은 입력 필드에 강조 표시되어 연산자를 커밋하기 전에 무엇이 yank되거나, 삭제되거나, 변경될 것인지 정확히 확인할 수 있습니다.

### Bash 모드

`!` 접두사를 사용하여 쉘 명령을 직접 실행합니다:

```bash
! npm test
! git status
! cat src/index.js
```

컨텍스트 전환 없이 빠른 명령 실행에 사용하십시오.

**v2.1.193부터:** bash 모드 (`!`)는 실시간 파일 경로 자동 완성을 제공하므로 프롬프트를 벗어나지 않고 쉘 명령을 입력하는 동안 경로가 완성됩니다.

**v2.1.186부터:** `!` 명령의 출력은 이제 Claude에게 자동으로 전송되어 Claude가 응답합니다. 출력이 응답 없이 컨텍스트에만 추가되는 이전 동작을 유지하려면 `settings.json`에서 `"respondToBashCommands": false`를 설정하십시오.

---

## TUI 모드 (전체 화면)

> **v2.1.110에 새로 추가**

TUI (텍스트 사용자 인터페이스) 모드는 Claude Code를 깜빡임 없는 출력으로 전체 화면으로 렌더링하여 tmux 또는 iTerm2 분할 창과 같은 터미널 멀티플렉서에 이상적입니다.

### TUI 모드 활성화

`/tui` 명령을 사용하거나 `--tui` 플래그를 사용하여 TUI 모드를 전환합니다:

```bash
/tui          # 세션 내에서 전환
claude --tui  # TUI 모드로 직접 시작
```

### 구성

| 설정 | 설명 | 기본값 |
|---------|-------------|---------|
| `autoScrollEnabled` | 최신 메시지로 자동 스크롤 | `true` |

`/config` 또는 `settings.json`을 통해 자동 스크롤을 비활성화합니다:

```json
{
  "autoScrollEnabled": false
}
```

### 포커스 보기

`/focus` 명령은 포커스 보기를 전환합니다. 이는 가장 관련성 높은 출력만 표시하는 집중 모드입니다. `Ctrl+O`는 이제 일반 트랜스크립트와 자세한 트랜스크립트 간에만 전환됩니다 (포커스 보기는 `/focus`입니다).

---

## 음성 받아쓰기

음성 받아쓰기는 Claude Code에 푸시투톡 음성 입력을 제공하여 프롬프트를 입력하는 대신 말할 수 있도록 합니다.

### 음성 받아쓰기 활성화

```
/voice
```

### 기능

| 기능 | 설명 |
|---------|-------------|
| **푸시투톡** | 녹음하려면 키를 누르고, 보내려면 놓습니다 |
| **20개 언어** | 음성-텍스트 변환은 20개 언어를 지원합니다 |
| **사용자 지정 키 바인딩** | `/keybindings`를 통해 푸시투톡 키를 구성합니다 |
| **계정 요구 사항** | STT 처리를 위해 Claude.ai 계정이 필요합니다 |

### 구성

키 바인딩 파일 (`/keybindings`)에서 푸시투톡 키 바인딩을 사용자 지정합니다. 음성 받아쓰기는 음성-텍스트 변환 처리를 위해 Claude.ai 계정을 사용합니다.

---

## 채널

채널은 외부 서비스에서 MCP 서버를 통해 실행 중인 Claude Code 세션으로 이벤트를 푸시하는 연구 미리보기 기능입니다. 소스에는 Telegram, Discord, iMessage 및 임의의 웹훅이 포함되어 Claude가 폴링 없이 실시간 알림에 반응할 수 있도록 합니다.

> **인증 (v2.1.128+)**: `--channels`는 이제 Pro/Max OAuth **및** API 키 (콘솔) 인증 모두에서 작동합니다. 이전 릴리스에서는 OAuth가 필요했습니다.

### 채널 구독

```bash
# 시작 시 채널 플러그인 구독
claude --channels discord,telegram

# 여러 소스 구독
claude --channels discord,telegram,imessage,webhooks
```

### 지원되는 통합

| 통합 | 설명 |
|-------------|-------------|
| **Discord** | 세션에서 Discord 메시지 수신 및 응답 |
| **Telegram** | 세션에서 Telegram 메시지 수신 및 응답 |
| **iMessage** | 세션에서 iMessage 알림 수신 |
| **Webhooks** | 임의의 웹훅 소스에서 이벤트 수신 |

### 구성

시작 시 `--channels` 플래그로 채널을 구성합니다. 엔터프라이즈 배포의 경우, 관리형 설정을 사용하여 허용되는 채널 플러그인을 제어합니다:

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

`allowedChannelPlugins` 관리형 설정은 조직 전체에서 허용되는 채널 플러그인을 제어합니다.

### 작동 방식

1. MCP 서버는 외부 서비스에 연결하는 채널 플러그인 역할을 합니다.
2. 들어오는 메시지 및 이벤트는 활성 Claude Code 세션으로 푸시됩니다.
3. Claude는 세션 컨텍스트 내에서 메시지를 읽고 응답할 수 있습니다.
4. 채널 플러그인은 `allowedChannelPlugins` 관리형 설정을 통해 승인되어야 합니다.
5. 폴링이 필요 없습니다 — 이벤트는 실시간으로 푸시됩니다.

---

## Chrome 통합

Chrome 통합은 Claude Code를 Chrome 또는 Microsoft Edge 브라우저에 연결하여 실시간 웹 자동화 및 디버깅을 지원합니다. 이는 v2.0.73+ (Edge 지원은 v1.0.36+에 추가됨)부터 사용할 수 있는 베타 기능입니다.

### Chrome 통합 활성화

**시작 시**:

```bash
claude --chrome      # Chrome 연결 활성화
claude --no-chrome   # Chrome 연결 비활성화
```

**세션 내에서**:

```
/chrome
```

"기본적으로 활성화"를 선택하여 모든 향후 세션에 대해 Chrome 통합을 활성화합니다. Claude Code는 브라우저의 로그인 상태를 공유하므로 인증된 웹 앱과 상호 작용할 수 있습니다.

### 기능

| 기능 | 설명 |
|------------|-------------|
| **실시간 디버깅** | 콘솔 로그 읽기, DOM 요소 검사, JavaScript 실시간 디버깅 |
| **디자인 검증** | 렌더링된 페이지를 디자인 모형과 비교 |
| **양식 유효성 검사** | 양식 제출, 입력 유효성 검사 및 오류 처리 테스트 |
| **웹 앱 테스트** | 인증된 앱 (Gmail, Google Docs, Notion 등)과 상호 작용 |
| **데이터 추출** | 웹 페이지에서 콘텐츠 스크랩 및 처리 |
| **세션 녹화** | 브라우저 상호 작용을 GIF 파일로 녹화 |

### 사이트별 권한

Chrome 확장 프로그램은 사이트별 액세스를 관리합니다. 확장 프로그램 팝업을 통해 특정 사이트에 대한 액세스를 언제든지 부여하거나 취소할 수 있습니다. Claude Code는 명시적으로 허용한 사이트와만 상호 작용합니다.

### 작동 방식

Claude Code는 보이는 창에서 브라우저를 제어합니다. 사용자는 실시간으로 작업이 발생하는 것을 볼 수 있습니다. 브라우저가 로그인 페이지나 CAPTCHA를 만나면 Claude는 일시 중지하고 사용자가 수동으로 처리할 때까지 기다린 다음 계속 진행합니다.

### 알려진 제한 사항

- **브라우저 지원**: Chrome 및 Edge만 지원 — Brave, Arc 및 기타 Chromium 브라우저는 지원되지 않습니다.
- **WSL**: Windows Sub시스템 for Linux에서는 사용할 수 없습니다.
- **타사 제공자**: Bedrock, Vertex 또는 Foundry API 제공자와는 지원되지 않습니다.
- **서비스 워커 유휴**: Chrome 확장 프로그램 서비스 워커는 확장된 세션 동안 유휴 상태가 될 수 있습니다.

> **팁**: Chrome 통합은 베타 기능입니다. 브라우저 지원은 향후 릴리스에서 확장될 수 있습니다.

---

## 원격 제어

원격 제어를 사용하면 휴대폰, 태블릿 또는 모든 브라우저에서 로컬로 실행 중인 Claude Code 세션을 계속할 수 있습니다. 로컬 세션은 사용자 컴퓨터에서 계속 실행되며, 아무것도 클라우드로 이동하지 않습니다. Pro, Max, Team 및 Enterprise 플랜에서 사용할 수 있습니다 (v2.1.51+).

### 원격 제어 시작

**CLI에서**:

```bash
# 기본 세션 이름으로 시작
claude remote-control

# 사용자 지정 이름으로 시작
claude remote-control --name "Auth Refactor"
```

**세션 내에서**:

```
/remote-control
/remote-control "Auth Refactor"
```

**사용 가능한 플래그**:

| 플래그 | 설명 |
|------|-------------|
| `--name "title"` | 쉬운 식별을 위한 사용자 지정 세션 제목 |
| `--verbose` | 상세 연결 로그 표시 |
| `--sandbox` | 파일 시스템 및 네트워크 격리 활성화 |
| `--no-sandbox` | 샌드박싱 비활성화 (기본값) |

### 세션에 연결

다른 기기에서 연결하는 세 가지 방법:

1. **세션 URL** — 세션이 시작될 때 터미널에 인쇄됩니다. 모든 브라우저에서 엽니다.
2. **QR 코드** — 시작 후 `spacebar`를 눌러 스캔 가능한 QR 코드를 표시합니다.
3. **이름으로 찾기** — claude.ai/code 또는 Claude 모바일 앱 (iOS/Android)에서 세션을 검색합니다.

### 보안

- 컴퓨터에 **인바운드 포트**가 열리지 않습니다.
- **아웃바운드 HTTPS만** TLS를 통해 이루어집니다.
- **범위가 지정된 자격 증명** — 여러 개의 단기적이고 좁은 범위의 토큰.
- **세션 격리** — 각 원격 세션은 독립적입니다.

### 원격 제어 대 웹의 Claude Code

| 측면 | 원격 제어 | 웹의 Claude Code |
|--------|---------------|-------------------|
| **실행** | 사용자 컴퓨터에서 실행 | Anthropic 클라우드에서 실행 |
| **로컬 도구** | 로컬 MCP 서버, 파일 및 CLI에 대한 전체 액세스 | 로컬 종속성 없음 |
| **사용 사례** | 다른 기기에서 로컬 작업 계속 | 모든 브라우저에서 새로 시작 |

### 제한 사항

- Claude Code 인스턴스당 하나의 원격 세션
- 호스트 컴퓨터에서 터미널이 열려 있어야 합니다.
- 네트워크에 연결할 수 없으면 세션이 약 10분 후에 시간 초과됩니다.

### 사용 사례

- 책상에서 떨어져 있는 동안 모바일 기기나 태블릿에서 Claude Code 제어
- 로컬 도구 실행을 유지하면서 풍부한 claude.ai UI 사용
- 전체 로컬 개발 환경으로 이동 중 빠른 코드 검토

### 푸시 알림 (v2.1.110)

원격 제어가 활성 상태이고 `/config`에서 "Claude가 결정할 때 푸시"가 활성화되어 있으면 Claude는 사용자 휴대폰으로 모바일 푸시 알림을 보낼 수 있습니다. 예를 들어, 긴 작업이 완료되거나 사용자 입력이 필요할 때입니다.

활성화 방법:
1. 원격 제어 활성화: `/remote-control` 또는 `claude --rc`
2. `/config`를 열고 **Push when Claude decides**를 활성화합니다.

푸시 알림에는 Claude 구독 및 Claude 모바일 앱이 필요합니다.

### 원격 제어 비활성화 (`disableremotecontrol`, v2.1.128+)

Team 또는 Enterprise 플랜의 관리자는 `disableRemoteControl` 설정을 사용하여 원격 제어를 완전히 차단할 수 있습니다. `true`로 설정되면 `claude remote-control`과 `/remote-control` 모두 시작을 거부합니다.

```json
{
  "disableRemoteControl": true
}
```

이 설정은 **관리/정책** 범위 (예: macOS의 `/Library/Application Support/ClaudeCode/managed-settings.json`)에서 적용되므로 개별 사용자가 재정의할 수 없습니다. 조직 전체에서 로컬 전용 실행을 강제해야 할 때 유용합니다.

> **API 키 티어에 의해 원격 제어가 자동 비활성화되는 경우 (v2.1.139)**: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper` 중 하나라도 설정되어 있으면 원격 제어가 **자동으로 비활성화됩니다**. claude.ai로 동시에 로그인되어 있는 경우에도 마찬가지입니다.
>
> 동일한 조건으로 [`/schedule`](#예약된-작업), claude.ai MCP 커넥터, 알림 설정이 비활성화됩니다. 이 네 가지 claude.ai 연결 기능은 OAuth 로그인이 활성 자격 증명일 때만 작동합니다. 이러한 기능을 사용하려면 API 키를 해제하거나 Pro/Max OAuth 티어에서 실행하십시오.

---

## 웹 세션

웹 세션을 사용하면 claude.ai/code에서 브라우저 내에서 직접 Claude Code를 실행하거나 CLI에서 웹 세션을 생성할 수 있습니다.

### 웹 세션 생성

```bash
# CLI에서 새 웹 세션 생성
claude --remote "implement the new API endpoints"
```

이렇게 하면 claude.ai에서 Claude Code 세션이 시작되며, 모든 브라우저에서 액세스할 수 있습니다.

### 로컬에서 웹 세션 다시 시작

웹에서 세션을 시작하고 로컬에서 계속하려면:

```bash
# 로컬 터미널에서 웹 세션 다시 시작
claude --teleport
```

또는 대화형 REPL 내에서:
```
/teleport
```

### 사용 사례

- 한 컴퓨터에서 작업을 시작하고 다른 컴퓨터에서 계속
- 팀원과 세션 URL 공유
- 시각적 차이 검토를 위해 웹 UI를 사용한 다음 실행을 위해 터미널로 전환

---

## 데스크톱 앱

Claude Code 데스크톱 앱은 시각적 차이 검토, 병렬 세션 및 통합 커넥터를 갖춘 독립형 애플리케이션을 제공합니다. macOS 및 Windows (Pro, Max, Team 및 Enterprise 플랜)에서 사용할 수 있습니다.

### 설치

플랫폼에 맞는 [claude.ai](https://claude.ai)에서 다운로드하십시오:
- **macOS**: 유니버설 빌드 (Apple Silicon 및 Intel)
- **Windows**: x64 및 ARM64 설치 프로그램 사용 가능

설정 지침은 [데스크톱 빠른 시작](https://code.claude.com/docs/en/desktop-quickstart)을 참조하십시오.

### CLI에서 핸드오프

현재 CLI 세션을 데스크톱 앱으로 전송합니다:

```
/desktop
```

### 핵심 기능

| 기능 | 설명 |
|---------|-------------|
| **차이점 보기** | 인라인 주석이 있는 파일별 시각적 검토; Claude는 주석을 읽고 수정 |
| **앱 미리보기** | 라이브 검증을 위해 임베디드 브라우저와 함께 개발 서버 자동 시작 |
| **PR 모니터링** | CI 오류 자동 수정 및 검사가 통과되면 자동 병합되는 GitHub CLI 통합 |
| **병렬 세션** | 자동 Git 워크트리 격리를 통해 사이드바에 여러 세션 표시 |
| **예약된 작업** | 앱이 열려 있는 동안 실행되는 반복 작업 (시간별, 일별, 주중, 주별) |
| **풍부한 렌더링** | 구문 강조 표시가 있는 코드, 마크다운 및 다이어그램 렌더링; GitHub-Flavored-Markdown 작업 목록 확인란 (`- [ ]` / `- [x]`)은 확인란으로 렌더링됩니다 (v2.1.149+) |

### 앱 미리보기 구성

`.claude/launch.json`에서 개발 서버 동작을 구성합니다:

```json
{
  "command": "npm run dev",
  "port": 3000,
  "readyPattern": "ready on",
  "persistCookies": true
}
```

### 커넥터

더 풍부한 컨텍스트를 위해 외부 서비스를 연결합니다:

| 커넥터 | 기능 |
|-----------|------------|
| **GitHub** | PR 모니터링, 이슈 추적, 코드 검토 |
| **Slack** | 알림, 채널 컨텍스트 |
| **Linear** | 이슈 추적, 스프린트 관리 |
| **Notion** | 문서화, 지식 기반 액세스 |
| **Asana** | 작업 관리, 프로젝트 추적 |
| **Calendar** | 일정 인식, 회의 컨텍스트 |

> **참고**: 커넥터는 원격 (클라우드) 세션에서는 사용할 수 없습니다.

### 원격 및 SSH 세션

- **원격 세션**: Anthropic 클라우드 인프라에서 실행; 앱이 닫혀도 계속 실행됩니다. claude.ai/code 또는 Claude 모바일 앱에서 액세스할 수 있습니다.
- **SSH 세션**: SSH를 통해 원격 머신에 연결하여 원격 파일 시스템 및 도구에 완전히 액세스합니다. Claude Code는 원격 머신에 설치되어 있어야 합니다.

### 데스크톱의 권한 모드

데스크톱 앱은 CLI와 동일한 4가지 권한 모드를 지원합니다:

| 모드 | 동작 |
|------|----------|
| **권한 요청** (기본값) | 모든 편집 및 명령 검토 및 승인 |
| **자동 편집 승인** | 파일 편집은 자동 승인; 명령은 수동 승인 필요 |
| **계획 모드** | 변경 사항을 적용하기 전에 접근 방식 검토 |
| **권한 우회** | 자동 실행 (샌드박스 전용, 관리자 제어) |

### 엔터프라이즈 기능

- **관리자 콘솔**: 조직의 코드 탭 액세스 및 권한 설정 제어
- **MDM 배포**: macOS에서는 MDM, Windows에서는 MSIX를 통해 배포
- **SSO 통합**: 조직 구성원에 대한 단일 로그인 필수화
- **관리형 설정**: 팀 구성 및 모델 가용성 중앙 관리

---

## 작업 목록

작업 목록 기능은 컨텍스트 압축 (대화 기록이 컨텍스트 창에 맞게 잘릴 때) 후에도 유지되는 영구적인 작업 추적 기능을 제공합니다.

### 작업 목록 전환

세션 중에 `Ctrl+T`를 눌러 작업 목록 보기를 켜거나 끕니다.

### 영구 작업

작업은 컨텍스트 압축 후에도 유지되므로 대화 컨텍스트가 잘릴 때 장기 실행 작업 항목이 손실되지 않습니다. 이는 복잡한 다단계 구현에 특히 유용합니다.

### 명명된 작업 디렉토리

`CLAUDE_CODE_TASK_LIST_ID` 환경 변수를 사용하여 세션 간에 공유되는 명명된 작업 디렉토리를 생성합니다:

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

이를 통해 여러 세션이 동일한 작업 목록을 공유할 수 있으므로 팀 워크플로우 또는 다중 세션 프로젝트에 유용합니다.

---

## 프롬프트 제안

프롬프트 제안은 Git 기록 및 현재 대화 컨텍스트를 기반으로 회색으로 표시된 예시 명령을 표시합니다.

### 작동 방식

- 입력 프롬프트 아래에 회색 텍스트로 제안이 나타납니다.
- `Tab`을 눌러 제안을 수락합니다.
- `Enter`를 눌러 수락하고 즉시 제출합니다.
- 제안은 Git 기록 및 대화 상태에서 가져온 컨텍스트 인식입니다.

### 프롬프트 제안 비활성화

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git 워크트리

Git 워크트리를 사용하면 Claude Code를 격리된 워크트리에서 시작하여 Stash하거나 전환할 필요 없이 다른 브랜치에서 병렬 작업을 수행할 수 있습니다.

### 워크트리에서 시작

```bash
# 격리된 워크트리에서 Claude Code 시작
claude --worktree
# 또는
claude -w
```

### 워크트리 위치

워크트리는 다음 위치에 생성됩니다:
```
<repo>/.claude/worktrees/<name>
```

### 모노레포를 위한 스파스 체크아웃

`worktree.sparsePaths` 설정을 사용하여 모노레포에서 스파스 체크아웃을 수행하여 디스크 사용량과 클론 시간을 줄입니다:

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### 기본 브랜치 참조 (`worktree.baseRef`)

**`worktree.baseRef`** (v2.1.133 추가) — `claude --worktree`가 `origin/<default>`에서 분기할지 아니면 로컬 `HEAD`에서 분기할지를 제어합니다.

- `"fresh"` (기본값) — `origin/<default-branch>`에서 분기하며, 로컬 푸시되지 않은 커밋을 무시합니다. **이는 v2.1.128에서 도입된 동작을 되돌립니다.** 따라서 v2.1.128 이후 로컬-HEAD 분기에 의존했던 사용자는 다시 옵트인해야 합니다.
- `"head"` — 로컬 `HEAD`에서 분기하며, 푸시되지 않은 커밋을 보존합니다.

`~/.claude/settings.json`에서 설정:

```json
{ "worktree": { "baseRef": "head" } }
```

### 백그라운드 세션 격리 (`worktree.bgIsolation`)

**`worktree.bgIsolation`** (v2.1.143 추가) — 백그라운드 세션 (예: `/bg`, `claude --bg`, 또는 에이전트 보기에서)이 자체 워크트리를 가질지 아니면 포그라운드 작업 복사본을 직접 편집할지를 제어합니다.

- *(기본값)* — 백그라운드 세션은 `--worktree`와 동일한 방식으로 `<repo>/.claude/worktrees/` 아래에 격리된 워크트리를 생성합니다.
- `"none"` — 백그라운드 세션은 현재 작업 복사본을 직접 편집합니다. 워크트리가 비실용적인 경우 (예: 대규모 네이티브 빌드 아티팩트) 또는 백그라운드 에이전트가 포그라운드 세션과 편집을 조율해야 하는 경우에 사용하십시오.

```json
{ "worktree": { "bgIsolation": "none" } }
```

장단점: `"none"`은 워크트리 격리의 안전망을 제거합니다. 백그라운드 및 포그라운드 세션의 동시 편집은 라이브 작업 복사본에서 병합 충돌을 일으킬 수 있습니다.

### 워크트리 도구 및 훅

| 항목 | 설명 |
|------|-------------|
| `EnterWorktree` | 워크트리에 진입하는 도구; v2.1.157부터 세션 중에 Claude 관리 워크트리 간 전환 가능 |
| `ExitWorktree` | 현재 워크트리를 종료하고 정리하는 도구 |
| `WorktreeCreate` | 워크트리가 생성될 때 발생하는 훅 이벤트 |
| `WorktreeRemove` | 워크트리가 제거될 때 발생하는 훅 이벤트 |

v2.1.157부터 Claude가 관리하는 워크트리는 에이전트가 작업을 마친 후 잠금 해제되므로 `git worktree remove`/`prune`으로 정리할 수 있습니다.

### 자동 정리

워크트리에서 변경 사항이 없으면 세션이 종료될 때 자동으로 정리됩니다.

### 사용 사례

- 메인 브랜치를 건드리지 않고 기능 브랜치에서 작업
- 작업 디렉토리에 영향을 미치지 않고 격리된 환경에서 테스트 실행
- 일회용 환경에서 실험적인 변경 시도
- 더 빠른 시작을 위해 모노레포에서 특정 패키지 스파스 체크아웃

---

## 샌드박싱

샌드박싱은 Claude Code에 의해 실행되는 Bash 명령에 OS 수준의 파일 시스템 및 네트워크 격리를 제공합니다. 이는 권한 규칙을 보완하며 추가 보안 계층을 제공합니다.

### 샌드박싱 활성화

**슬래시 명령어**:
```
/sandbox
```

**CLI 플래그**:
```bash
claude --sandbox       # 샌드박싱 활성화
claude --no-sandbox    # 샌드박싱 비활성화
```

### 구성 설정

| 설정 | 설명 |
|---------|-------------|
| `sandbox.enabled` | 샌드박싱 활성화 또는 비활성화 |
| `sandbox.failIfUnavailable` | 샌드박싱을 활성화할 수 없는 경우 실패 |
| `sandbox.filesystem.allowWrite` | 쓰기 액세스 허용 경로 |
| `sandbox.filesystem.allowRead` | 읽기 액세스 허용 경로 |
| `sandbox.filesystem.denyRead` | 읽기 액세스 거부 경로 |
| `sandbox.network.allowedDomains` | Bash로 시작된 프로세스가 도달할 수 있는 도메인 ( `*.` 와일드카드 지원) |
| `sandbox.network.deniedDomains` | `allowedDomains` 와일드카드가 허용하더라도 차단할 도메인 (v2.1.113+) |
| `sandbox.enableWeakerNetworkIsolation` | macOS에서 약한 네트워크 격리 활성화 |
| `sandbox.bwrapPath` | (v2.1.133+, Linux/WSL) `bubblewrap` 바이너리 경로. 기본값: `$PATH` 조회. |
| `sandbox.socatPath` | (v2.1.133+, Linux/WSL) `socat` 바이너리 경로. 기본값: `$PATH` 조회. |
| `sandbox.credentials` | (v2.1.187+) 샌드박스 명령이 자격 증명 파일 및 비밀 환경 변수를 읽는 것을 차단합니다. |
| `sandbox.allowAppleEvents` | (v2.1.181+, macOS) 샌드박스 명령이 Apple Event를 보내도록 옵트인합니다. |

**Linux/WSL 바이너리 경로** (v2.1.133+) — 비표준 설치 위치에서 Claude Code를 가리킵니다:

```json
{
  "sandbox": {
    "bwrapPath": "/opt/bubblewrap/bin/bwrap",
    "socatPath": "/opt/socat/bin/socat"
  }
}
```

광범위한 와일드카드를 재정의하는 `deniedDomains`의 예시 (v2.1.113+):

```json
{
  "sandbox": {
    "network": {
      "allowedDomains": ["*.example.com"],
      "deniedDomains": ["evil.example.com"]
    }
  }
}
```

와일드카드는 `example.com`의 모든 것을 허용하지만, `deniedDomains`는 특정 이름의 호스트를 여전히 차단합니다.

### 예시 구성

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    },
    "enableWeakerNetworkIsolation": true
  }
}
```

### 작동 방식

- Bash 명령은 제한된 파일 시스템 액세스를 가진 샌드박스 환경에서 실행됩니다.
- 의도치 않은 외부 연결을 방지하기 위해 네트워크 액세스를 격리할 수 있습니다.
- 심층 방어를 위해 권한 규칙과 함께 작동합니다.
- macOS에서는 네트워크 제한을 위해 `sandbox.enableWeakerNetworkIsolation`을 사용합니다 (macOS에서는 전체 네트워크 격리가 불가능합니다).

### 사용 사례

- 신뢰할 수 없거나 생성된 코드를 안전하게 실행
- 프로젝트 외부 파일에 대한 우발적인 수정 방지
- 자동화된 작업 중 네트워크 액세스 제한

---

## 관리형 설정 (엔터프라이즈)

관리형 설정은 엔터프라이즈 관리자가 플랫폼 고유의 관리 도구를 사용하여 조직 전체에 Claude Code 구성을 배포할 수 있도록 합니다.

### 배포 방법

| 플랫폼 | 방법 | 이후 버전 |
|----------|--------|-------|
| macOS | 관리형 plist 파일 (MDM) | v2.1.51+ |
| Windows | Windows 레지스트리 | v2.1.51+ |
| 크로스 플랫폼 | 관리형 구성 파일 | v2.1.51+ |
| 크로스 플랫폼 | 관리형 드롭인 (`managed-settings.d/` 디렉토리) | v2.1.83+ |

### 관리형 드롭인

v2.1.83부터 관리자는 `managed-settings.d/` 디렉토리에 여러 관리형 설정 파일을 배포할 수 있습니다. 파일은 알파벳순으로 병합되어 팀 간에 모듈형 구성을 가능하게 합니다:

```
~/.claude/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### 사용 가능한 관리형 설정

| 설정 | 설명 |
|---------|-------------|
| `disableBypassPermissionsMode` | 사용자가 권한 우회 모드를 활성화하지 못하도록 방지 |
| `availableModels` | 사용자가 선택할 수 있는 모델 제한 |
| `enforceAvailableModels` | (v2.1.175) `true`인 경우, `availableModels` 허용 목록은 **기본** 모델도 제한합니다. 구성된 기본값이 목록에 없으면 Claude Code는 허용된 첫 번째 모델로 대체됩니다. 사용자 및 프로젝트 설정은 더 이상 관리되는 `availableModels` 목록을 확장할 수 없습니다. |
| `allowedChannelPlugins` | 허용되는 채널 플러그인 제어 |
| `autoMode.environment` | 자동 모드에 대한 신뢰할 수 있는 인프라 구성 |
| `wslInheritsWindowsSettings` | Windows/WSL 전용 (v2.1.118+): `true`인 경우, WSL 내에서 실행되는 Claude Code는 Windows 호스트의 관리되는 설정을 상속하므로 레지스트리/MDM을 통해 배포된 엔터프라이즈 정책이 Windows 및 WSL 쉘 전체에 균일하게 적용됩니다. |
| `parentSettingsBehavior` | (v2.1.133+, 관리자 계층) SDK의 `managedSettings`가 부모 프로세스 설정과 병합되는 방식을 제어합니다. `"first-wins"`는 기존 우선 순위를 유지하고 (충돌 시 먼저 설정된 것이 승리), `"merge"`는 값을 깊이 병합합니다. |
| 사용자 지정 정책 | 조직별 권한 및 도구 정책 |

### 예시: macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>disableBypassPermissionsMode</key>
  <true/>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## 구성 및 설정

### 구성 파일 위치

1. **전역 구성**: `~/.claude/config.json`
2. **프로젝트 구성**: `./.claude/config.json`
3. **사용자 구성**: `~/.config/claude-code/settings.json`

### 전체 구성 예시

**핵심 고급 기능 구성:**

```json
{
  "permissions": {
    "mode": "default"
  },
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh"
  },
  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    }
  }
}
```

**확장 구성 예시:**

```json
{
  "permissions": {
    "mode": "default",
    "allowedTools": ["Bash(git log:*)", "Read"],
    "disallowedTools": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": ["eslint --fix ${file_path}"] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": ["~/.claude/hooks/security-scan.sh"] }],
    "Stop": [{ "hooks": ["~/.claude/hooks/notify.sh"] }]
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### 대체 모델 (`fallbackModel`)

`fallbackModel` 설정을 사용하면 기본 모델이 과부하되거나 사용할 수 없을 때 순서대로 시도되는 **최대 3개의** 대체 모델을 구성할 수 있습니다.

```json
{
  "fallbackModel": ["claude-opus-4-8", "claude-sonnet-4-6", "claude-haiku-4-5"]
}
```

**v2.1.166부터** `--fallback-model` 플래그는 대화형 세션에도 적용됩니다 (헤드리스뿐만 아니라). 대체 시 Claude Code는 예기치 않은 재시도 불가능한 오류를 한 번 재시도합니다. 인증, 속도 제한, 요청 크기 및 전송 오류는 즉시 실패합니다.

### 환경 변수

환경 변수로 구성을 재정의합니다:

```bash
# Model selection
export ANTHROPIC_MODEL=claude-opus-4-8
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-8
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# API configuration
export ANTHROPIC_API_KEY=sk-ant-...

# Thinking configuration
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high   # low, medium, high, xhigh (Opus 4.8/4.7), or max — default is high on Opus 4.8 (supported on Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6)

# Feature toggles
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # Set by --bare flag

# MCP configuration
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Prompt caching
export ENABLE_PROMPT_CACHING_1H=1      # Use 1-hour prompt cache TTL (default is 5 min)

# Task management
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Agent teams (experimental)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Subagent and plugin configuration
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=1

# Subprocess and streaming
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000

# Output and package manager (v2.1.129+)
export CLAUDE_CODE_FORCE_SYNC_OUTPUT=1                      # Force synchronous output for terminals where auto-detect misses (Emacs eat, etc.)
export CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1            # Enable background upgrades for Homebrew/WinGet installs
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1         # Opt in to /v1/models gateway discovery when ANTHROPIC_BASE_URL is set

# Windows PowerShell tool (v2.1.143+) — default-on for Bedrock/Vertex/Foundry on Windows
export CLAUDE_CODE_USE_POWERSHELL_TOOL=0                    # Disable the PowerShell tool entirely
export CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1    # Honor system ExecutionPolicy instead of `-ExecutionPolicy Bypass`

# Workload identity federation (v2.1.141+)
export ANTHROPIC_WORKSPACE_ID=ws_abc123                     # Scope the federated token to a specific workspace when the rule covers multiple

# Stop hook safety cap (v2.1.143+)
export CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=8                    # Max consecutive Stop-hook blocks before the session ends with a warning. Set 0 to disable the cap.
```

> **v2.1.108**: `ENABLE_PROMPT_CACHING_1H=1` — 기본 5분 TTL 대신 1시간 프롬프트 캐시 TTL을 사용합니다. 길고 안정적인 세션에서 캐시 누락을 줄입니다. (v2.1.129는 1시간 TTL이 자동으로 5분으로 다운그레이드되던 회귀 버그를 수정합니다.)

> **v2.1.129**: `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1`은 자동 감지가 실패하는 터미널 (예: Emacs `eat`)에 대해 동기식 출력을 강제합니다. `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1`은 Homebrew/WinGet 설치에 대한 백그라운드 업그레이드를 활성화하며, 그렇지 않으면 자동 업데이트되지 않습니다.

### 구성 관리 명령어

```
User: /config
[대화형 구성 메뉴 열기]
```

`/config` 명령은 다음과 같은 설정을 전환하는 대화형 메뉴를 제공합니다:
- 확장된 사고 켜기/끄기
- 자세한 출력
- 권한 모드
- 모델 선택

대화형 메뉴에서 Enter 또는 Space를 눌러 선택한 설정을 변경하고, Esc를 눌러 저장하고 닫습니다 (v2.1.183+).

메뉴를 열지 않고도 프롬프트에서 직접 설정을 지정할 수도 있습니다:

```bash
/config thinking=false      # 단일 설정 인라인으로 지정 (v2.1.181+)
/config --help              # 사용 가능한 약식 키 목록 (v2.1.183+)
```

`key=value` 약식은 대화형 세션, `-p` 플래그 사용 시, 그리고 원격 제어에서 작동합니다.

### 프로젝트별 구성

프로젝트에 `.claude/config.json`을 생성합니다:

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": ["npm test && npm run lint"] }]
  },
  "permissions": {
    "mode": "default"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

## 에이전트 팀

에이전트 팀은 여러 Claude Code 인스턴스가 작업에 협력할 수 있도록 하는 실험적인 기능입니다. 기본적으로 비활성화되어 있습니다.

### 에이전트 팀 활성화

환경 변수 또는 설정을 통해 활성화합니다:

```bash
# 환경 변수
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

또는 설정 JSON에 추가합니다:

```json
{
  "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
}
```

### 에이전트 팀 작동 방식

- **팀 리더**는 전체 작업을 조율하고 하위 작업을 팀원에게 위임합니다.
- **팀원**은 각자 자신의 컨텍스트 창을 가지고 독립적으로 작업합니다.
- **공유 작업 목록**은 팀원 간의 자체 조율을 가능하게 합니다.
- 팀원의 역할 및 전문화를 정의하려면 서브에이전트 정의 (`.claude/agents/` 또는 `--agents` 플래그)를 사용합니다.

### 표시 모드

에이전트 팀은 `--teammate-mode` 플래그로 구성되는 두 가지 표시 모드를 지원합니다:

| 모드 | 설명 |
|------|-------------|
| `in-process` (기본값) | 팀원은 동일한 터미널 프로세스 내에서 실행됩니다 |
| `tmux` | 각 팀원은 전용 분할 창을 가집니다 (tmux 또는 iTerm2 필요) |
| `auto` | 최상의 표시 모드를 자동으로 선택합니다 |

```bash
# 팀원 표시를 위해 tmux 분할 창 사용
claude --teammate-mode tmux

# 명시적으로 인프로세스 모드 사용
claude --teammate-mode in-process
```

### 사용 사례

- 다른 팀원이 다른 모듈을 처리하는 대규모 리팩토링 작업
- 병렬 코드 검토 및 구현
- 코드베이스 전체에 걸친 조정된 다중 파일 변경

> **참고**: 에이전트 팀은 실험적인 기능이며 향후 릴리스에서 변경될 수 있습니다. 전체 참조는 [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams)를 참조하십시오.

---

## 모범 사례

### 기획 모드
- ✅ 복잡한 다단계 작업에 사용
- ✅ 승인 전에 계획 검토
- ✅ 필요할 때 계획 수정
- ❌ 간단한 작업에는 사용하지 않음

### 확장된 사고
- ✅ 아키텍처 결정에 사용
- ✅ 복잡한 문제 해결에 사용
- ✅ 사고 과정 검토
- ❌ 간단한 쿼리에는 사용하지 않음

### 백그라운드 작업
- ✅ 장기 실행 작업에 사용
- ✅ 작업 진행 상황 모니터링
- ✅ 작업 실패를 우아하게 처리
- ❌ 너무 많은 동시 작업을 시작하지 않음

### 권한
- ✅ 코드 검토에는 `plan` 사용 (읽기 전용)
- ✅ 대화형 개발에는 `default` 사용
- ✅ 자동화 워크플로우에는 `acceptEdits` 사용
- ✅ 안전 보호 기능이 있는 자율 작업에는 `auto` 사용
- ❌ 절대적으로 필요한 경우가 아니면 `bypassPermissions` 사용하지 않음

### 세션
- ✅ 다른 작업에 대해 별도의 세션 사용
- ✅ 중요한 세션 상태 저장
- ✅ 오래된 세션 정리
- ❌ 관련 없는 작업을 한 세션에 섞지 않음

---

## 추가 자료

Claude Code 및 관련 기능에 대한 자세한 정보는 다음을 참조하십시오:

- [공식 대화형 모드 문서](https://code.claude.com/docs/en/interactive-mode)
- [공식 헤드리스 모드 문서](https://code.claude.com/docs/en/headless)
- [CLI 참조](https://code.claude.com/docs/en/cli-reference)
- [체크포인트 가이드](../08-checkpoints/) - 세션 관리 및 되감기
- [슬래시 명령어](../01-slash-commands/) - 명령어 참조
- [메모리 가이드](../02-memory/) - 영구 컨텍스트
- [스킬 가이드](../03-skills/) - 자율 기능
- [서브에이전트 가이드](../04-subagents/) - 위임된 작업 실행
- [MCP 가이드](../05-mcp/) - 외부 데이터 액세스
- [훅 가이드](../06-hooks/) - 이벤트 기반 자동화
- [플러그인 가이드](../07-plugins/) - 번들 확장
- [공식 예약된 작업 문서](https://code.claude.com/docs/en/scheduled-tasks)
- [공식 Chrome 통합 문서](https://code.claude.com/docs/en/chrome)
- [공식 원격 제어 문서](https://code.claude.com/docs/en/remote-control)
- [공식 키 바인딩 문서](https://code.claude.com/docs/en/keybindings)
- [공식 데스크톱 앱 문서](https://code.claude.com/docs/en/desktop)
- [공식 에이전트 팀 문서](https://code.claude.com/docs/en/agent-teams)

---

**최종 업데이트**: 2026년 6월 28일
**Claude Code 버전**: 2.1.195
**출처**:
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://docs.anthropic.com/en/docs/claude-code/settings
- https://code.claude.com/docs/en/troubleshooting
- https://code.claude.com/docs/en/changelog#2-1-175
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/interactive-mode
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/model-config
- https://www.anthropic.com/news/claude-opus-4-8
- https://claude.com/blog/introducing-routines-in-claude-code
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.139
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/sub-agents
**호환 모델**: Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
