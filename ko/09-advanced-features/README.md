<!-- i18n-source: 09-advanced-features/README.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 고급 기능

계획 모드, 확장 사고, 자동 모드, 백그라운드 작업, 권한 모드, 인쇄 모드 (비대화형), 세션 관리, 대화형 기능, 채널, 음성 받아쓰기, 원격 제어, 웹 세션, 데스크톱 앱, 작업 목록, 프롬프트 제안, Git 워크트리, 샌드박싱, 관리형 설정, 구성 등 Claude Code의 고급 기능에 대한 종합 가이드입니다.

## 목차

1. [개요](#개요)
2. [계획 모드](#계획-모드)
3. [확장 사고](#확장-사고)
4. [자동 모드](#자동-모드)
5. [백그라운드 작업](#백그라운드-작업)
6. [모니터 도구 (이벤트 기반 스트림)](#모니터-도구-이벤트-기반-스트림)
7. [동적 워크플로](#동적-워크플로)
8. [예약된 작업](#예약된-작업)
9. [권한 모드](#권한-모드)
10. [헤드리스 모드](#헤드리스-모드)
11. [세션 관리](#세션-관리)
12. [세션 간 메시징](#세션-간-메시징)
13. [대화형 기능](#대화형-기능)
14. [출력 스타일](#출력-스타일)
15. [상태 표시줄](#상태-표시줄)
16. [TUI 모드 (전체 화면)](#tui-모드-전체-화면)
17. [음성 받아쓰기](#음성-받아쓰기)
18. [채널](#채널)
19. [Chrome 통합](#chrome-통합)
20. [원격 제어](#원격-제어)
21. [웹 세션](#웹-세션)
22. [데스크톱 앱](#데스크톱-앱)
23. [작업 목록](#작업-목록)
24. [프롬프트 제안](#프롬프트-제안)
25. [Git 워크트리](#git-워크트리)
26. [샌드박싱](#샌드박싱)
27. [관리형 설정 (엔터프라이즈)](#관리형-설정-엔터프라이즈)
28. [구성 및 설정](#구성-및-설정)
29. [신뢰 및 권한 범위 지정](#신뢰-및-권한-범위-지정)
30. [에이전트 팀](#에이전트-팀)
31. [모범 사례](#모범-사례)
32. [추가 자료](#추가-자료)

---

## 개요

Claude Code의 고급 기능은 계획, 추론, 자동화 및 제어 메커니즘을 통해 핵심 기능을 확장합니다. 이러한 기능은 복잡한 개발 작업, 코드 검토, 자동화 및 다중 세션 관리를 위한 정교한 워크플로를 가능하게 합니다.

**주요 고급 기능은 다음과 같습니다:**
- **계획 모드**: 코딩 전에 상세한 구현 계획 생성
- **확장 사고**: 복잡한 문제에 대한 심층적인 추론
- **자동 모드**: 백그라운드 안전 분류기가 각 작업 실행 전에 검토
- **백그라운드 작업**: 대화를 차단하지 않고 긴 작업 실행
- **권한 모드**: Claude가 수행할 수 있는 작업 제어 (`manual` — 이전 명칭 `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`)
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

## 계획 모드

계획 모드를 사용하면 Claude가 구현 전에 복잡한 작업을 신중하게 고려하여 검토하고 승인할 수 있는 상세한 계획을 만들 수 있습니다.

### 계획 모드란 무엇입니까?

계획 모드는 두 단계로 구성된 접근 방식입니다:
1. **계획 단계**: Claude가 작업을 분석하고 상세한 구현 계획을 생성합니다.
2. **구현 단계**: 승인 후 Claude가 계획을 실행합니다.

### 계획 모드 사용 시점

✅ 계획 모드를 사용하는 경우:
- 복잡한 다중 파일 리팩터링
- 새로운 기능 구현
- 아키텍처 변경
- 데이터베이스 마이그레이션
- 주요 API 재설계

❌ 계획 모드를 사용하지 않는 경우:
- 간단한 버그 수정
- 형식 변경
- 단일 파일 편집
- 빠른 쿼리

### 계획 모드 활성화

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
- `Alt + M` - 권한 모드 전환 (Windows 전용, 런타임이 VT 입력 모드를 활성화하지 않는 경우)

### 계획 모드의 이점

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

### 계획 모드 구성

계획 모드는 CLI 플래그 또는 슬래시 명령어를 통해 활성화됩니다:

```bash
# Activate plan mode via CLI
claude --permission-mode plan

# Or use the /plan slash command inside the REPL
/plan Implement user authentication system
```

**계획용 모델 별칭**: Opus를 계획에, Sonnet을 실행에 사용하려면 `opusplan`을 모델 별칭으로 사용합니다:

```bash
claude --model opusplan "design and implement the new API"
```

**외부에서 계획 편집**: `Ctrl+G`를 눌러 외부 편집기에서 현재 계획을 열고 상세하게 수정할 수 있습니다.

> **v2.1.112 업데이트**: 이제 계획 파일은 무작위 단어 대신 생성된 프롬프트의 이름을 따서 명명되므로, 더 쉽게 찾아보고 재사용할 수 있습니다.

> **v2.1.136 업데이트 — 계획 모드 쓰기 블록은 무조건적입니다**: 계획 모드는 이제 `permissions.allow`에 일치하는 `Edit(...)` 규칙이 있는 경우를 포함하여 모든 파일 쓰기를 차단합니다. 이전에는 관대한 `Edit(...)` 규칙이 계획 모드에서 쓰기를 허용할 수 있었지만, 해당 우회 경로는 폐쇄되었습니다. 워크플로가 이전 동작에 의존하는 경우, 편집하기 전에 계획 모드를 종료하십시오 (`Shift+Tab`).

---

## 확장 사고

확장 사고는 Claude가 솔루션을 제공하기 전에 복잡한 문제에 대해 더 많은 시간을 추론하도록 허용합니다.

### 확장 사고란 무엇입니까?

확장 사고는 Claude가 다음을 수행하는 신중한 단계별 추론 프로세스입니다:
- 복잡한 문제를 분해합니다
- 여러 접근 방식을 고려합니다
- 장단점을 평가합니다
- 엣지 케이스를 통해 추론합니다

### 확장 사고 활성화

**키보드 단축키**:
- `Option + T` (macOS) / `Alt + T` (Windows/Linux) - 확장 사고 전환. Opus 5.5(v2.1.280부터 기본 모델), Sonnet 5.5, Haiku 5.5 및 Fable 모델에서는 사고를 끌 수 없습니다. 이 모델들에서는 전환 키, `alwaysThinkingEnabled`, `MAX_THINKING_TOKENS=0`이 아무 효과가 없습니다.

**자동 활성화**:
- 모든 모델 (Opus 5, Opus 4.8, Opus 4.7, Sonnet 4.6, Haiku 4.5)에 기본적으로 활성화되어 있습니다.
- Opus 5 / Opus 4.8: 노력 수준이 있는 적응형 추론: `low` (○), `medium` (◐), `high` (●), `xhigh`, `max`. 기본값은 Opus 5.5(v2.1.280부터 기본 모델), Sonnet 5.5, Haiku 5.5에서 `medium`이고, Opus 5 (v2.1.219), Sonnet 5, Opus 4.8 (v2.1.154), Opus 4.6, Sonnet 4.6에서 `high`이며, Opus 4.7에서 `xhigh`입니다. `xhigh`는 Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7에서 사용할 수 있습니다 (Opus 4.6 / Sonnet 4.6에서는 `high`로 대체됩니다). `max`는 Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7/4.6 및 Sonnet 4.6에서 작동합니다 (세션 전용). Haiku 4.5에는 노력 수준이 없습니다. Opus 5, Opus 4.8, Opus 4.7은 1M 토큰의 기본 컨텍스트 창을 가집니다 (1M 컨텍스트 수정은 v2.1.117에 적용됨 — 이전에는 `/context`가 Opus 4.7을 200K 창에 대해 잘못 계산하여 조기 자동 압축을 트리거했습니다). v2.1.129부터 `/context`는 UI 내에서만 시각화를 표시합니다. ASCII 시각화는 더 이상 대화 컨텍스트로 유출되지 않으므로 (호출당 약 1.6k 토큰 절약), `/context`는 자유롭게 호출해도 안전합니다.
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

**노력 수준** (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6에서 지원 — Haiku 4.5 제외):
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○), medium (◐), high (●), xhigh (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7), or max — default is high on Opus 5 and Opus 4.8
```

**CLI 플래그**:
```bash
claude --effort high "complex architectural review"
```

**슬래시 명령어**:
```
/effort high
```

> **참고:** 프롬프트의 "ultrathink" 키워드는 심층 추론 모드를 활성화합니다. 노력 수준 `low`, `medium`, `high`, `max`는 Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6에서 지원됩니다 (Haiku 4.5는 지원하지 않음). `xhigh`는 Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7에서 사용할 수 있습니다. 기본 노력 수준은 Opus 5.5, Sonnet 5.5, Haiku 5.5에서 `medium`이고, Opus 5, Sonnet 5, Opus 4.8 (및 Opus 4.6 / Sonnet 4.6)에서 `high`이며, Opus 4.7에서 `xhigh`입니다. 첫 실행 시 기본 노력 수준을 고정하는 Opus 4.8 및 Opus 4.7과 달리 Opus 5에는 그런 고정이 없으므로, 이전에 설정한 수준이 그대로 유지됩니다. `/effort` 슬라이더에는 **Ultracode** 토글(Tab 또는 `/effort ultracode [on|off]`)도 있는데, 이는 모델 노력 수준이 **아니며** 세션이 실행 중인 노력 수준에서 Claude가 동적 워크플로를 조율하도록 합니다. v2.1.284부터는 더 이상 `xhigh`를 강제하지 않고 수준을 바꿔도 켜진 상태로 유지됩니다. `--effort ultracode`와 Agent SDK의 `effortLevel: "ultracode"`는 여전히 `xhigh`를 설정합니다.

### Opus 5의 안전 분류기 대체 동작

[`fallbackModel` 설정](#대체-모델-fallbackmodel)(과부하 및 사용 불가 상황 처리)과는 별개로, Claude Code는 안전 분류기가 요청을 플래그 처리하면 **카테고리 기반 대체**를 적용합니다. Claude Code v2.1.219 이상이 필요합니다.

- **Opus 5**: 사이버 보안으로 플래그된 요청은 Opus 4.8에서 다시 실행됩니다. 생물학으로 플래그된 요청은 대신 거부로 끝납니다. Opus 5는 대체 모델 없이 자체 생물학 분류기를 실행하기 때문입니다. 이러한 거부는 첫 번째 플래그된 요청부터 발생합니다.
- 공격 보안 또는 생물학 분야의 작업 — 침투 테스트, CTF(Capture the Flag) 실습, 생물학 관련 코드베이스 — 은 대체를 자주 트리거하며, 첫 요청에서 트리거되는 경우도 많습니다.

여기서 이것이 중요한 이유: Opus 5에서 [보안 검토 서브에이전트](../04-subagents/README.md)나 CTF/침투 테스트 작업을 실행한다면, 사이버 보안 프롬프트는 Opus 4.8(노력 상한과 컨텍스트 창이 다름)에서 조용히 재실행되고, 생물학 관련 프롬프트는 즉시 거부될 수 있다고 예상하십시오. 이 동작이 방해된다면 다른 모델을 명시적으로 고정하십시오.

**전환 제어** — `switchModelsOnFlag` 설정(v2.1.170+, 기본값 `true`)은 대체가 조용히 일어날지 결정합니다. `false`로 설정하면 Claude Code가 대신 일시 중지하여 모델 전환과 프롬프트 수정 중 하나를 선택할 수 있게 합니다. `/config`에서 **Switch models when a message is flagged**로 표시됩니다.

```json
{
  "switchModelsOnFlag": false
}
```

### 확장 사고의 이점

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

### 확장 사고 구성

확장 사고는 환경 변수, 키보드 단축키 및 CLI 플래그를 통해 제어됩니다:

```bash
# Set thinking token budget
export MAX_THINKING_TOKENS=16000

# Set effort level (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6): low (○), medium (◐), high (●), xhigh (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7), or max — default is high on Opus 5 and Opus 4.8
export CLAUDE_CODE_EFFORT_LEVEL=high
```

세션 중에 `Alt+T` / `Option+T`로 전환하거나 `/effort`로 노력 수준을 설정하거나 `/config`를 통해 구성할 수 있습니다.

> **간소화된 시스템 프롬프트 (v2.1.154):** 간소화된 시스템 프롬프트는 이제 Haiku 4.5, Sonnet 5, Opus 4.7 및 해당 계열의 이전 모델을 제외한 모든 모델의 **기본값**이며(Haiku 5.5와 Sonnet 5.5도 사용), Opus 5와 Opus 4.8의 기본 토큰 오버헤드를 줄입니다.

---

## 자동 모드

자동 모드는 백그라운드 안전 분류기를 사용하여 각 작업을 실행하기 전에 검토하는 권한 모드입니다. Claude가 자율적으로 작업하면서 위험한 작업을 차단할 수 있도록 합니다. 모든 플랜에서 사용할 수 있지만 적격한 모델이 필요합니다(Anthropic API 및 Claude Platform on AWS에서는 Claude Opus 4.6 이상, Sonnet 4.6 이상, Haiku 5.5 또는 Fable 모델, Bedrock, Vertex, Foundry 및 로그인된 Claude apps gateway 세션에서는 Sonnet 5 이상, Opus 4.7 이상, Haiku 5.5 또는 Fable 모델). Team 및 Enterprise에서는 기본적으로 켜져 있으며, 관리자는 관리형 설정에서 조직 전체에 대해 끌 수 있습니다.

### 요구 사항

자동 모드는 계정이 다음 요구 사항을 모두 충족할 때만 사용할 수 있습니다:

- **플랜**: 모든 플랜.
- **조직**: Team 및 Enterprise에서는 자동 모드를 기본적으로 사용할 수 있습니다. 관리자는 관리형 설정에서 `permissions.disableAutoMode`를 `"disable"`로 설정하여 조직 전체에 대해 끌 수 있습니다.
- **모델**: Anthropic API 및 Claude Platform on AWS에서는 Claude Opus 4.6 이상, Sonnet 4.6 이상, Haiku 5.5 또는 Fable 모델. Amazon Bedrock, Google Cloud's Agent Platform(Vertex AI), Microsoft Foundry 및 로그인된 Claude apps gateway 세션에서는 Claude Sonnet 5 이상, Opus 4.7 이상, Haiku 5.5(v2.1.293+), Fable 모델만 해당합니다. 이전 모델 — Sonnet 4.5, Opus 4.5, Haiku 4.5 및 claude-3 모델 — 은 어떤 제공자에서도 지원되지 않습니다.
- **제공자**: Anthropic API, Claude Platform on AWS, Amazon Bedrock, Google Cloud's Agent Platform(Vertex AI), Microsoft Foundry 및 로그인된 Claude apps gateway 세션에서 기본적으로 사용할 수 있습니다. v2.1.158부터 v2.1.206까지는 Anthropic API와 Claude Platform on AWS를 제외한 모든 제공자에서 `CLAUDE_CODE_ENABLE_AUTO_MODE=1`을 설정하기 전까지 자동 모드가 꺼져 있었으며, v2.1.207에서 이 요구 사항이 제거되었습니다. 이 변수는 호환성을 위해 여전히 허용되지만 v2.1.207부터는 효과가 없습니다.
- **분류기**: 추가 토큰 비용이 발생합니다. 단, Enterprise 플랜과 Claude API 계정에서는 v2.1.278+부터 검사를 서버 측에서 무료로 실행합니다

### 자동 모드 활성화

```bash
# 권한 모드가 구성되지 않은 경우 대화형 세션은 자동 모드로 시작합니다 (v2.1.284+)
# 명시적으로 선택하려면(예: 설정의 기본값이 다른 모드인 경우):
claude --permission-mode auto

# 또는 REPL에서 Shift+Tab으로 순환하여 선택합니다
```

> **v2.1.112 업데이트**: 자동 모드는 더 이상 `--enable-auto-mode` 플래그를 필요로 하지 않습니다. Max 구독자는 Opus 4.7에서 직접 액세스할 수 있습니다.

> **v2.1.158 업데이트**: Opus 4.7/4.8용 Bedrock, Vertex, Foundry에서 자동 모드를 사용할 수 있게 되었으며, `CLAUDE_CODE_ENABLE_AUTO_MODE=1`로 활성화해야 했습니다.
>
> **v2.1.207 업데이트**: 이 옵트인 요구 사항이 제거되었습니다. 이제 Bedrock, Vertex AI, Microsoft Foundry 및 로그인된 Claude apps gateway 세션에서 Claude Sonnet 5, Opus 4.7, Opus 4.8, Fable 5(v2.1.219부터는 Opus 5 포함)에 대해 자동 모드를 기본적으로 사용할 수 있으며, 플래그나 환경 변수가 필요하지 않습니다. 관리자는 관리형 설정의 `disableAutoMode`로 비활성화할 수 있습니다. `CLAUDE_CODE_ENABLE_AUTO_MODE`는 호환성을 위해 여전히 허용되지만 v2.1.207부터는 효과가 없습니다.

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

백그라운드 분류기는 다음 결정 순서를 사용하여 각 작업을 평가합니다:

1. **허용/거부 규칙** -- 명시적인 권한 규칙이 먼저 확인됩니다.
2. **읽기 전용/편집 자동 승인** -- 파일 읽기 및 편집은 자동으로 통과됩니다.
3. **분류기** -- 백그라운드 분류기가 작업을 검토합니다.
4. **대체** -- 3회 연속 또는 총 20회 차단 후 프롬프트로 대체됩니다.

### 기본 차단 작업

자동 모드는 기본적으로 다음을 차단합니다:

| 차단된 작업 | 예시 |
|----------------|---------|
| 파이프-투-셸 설치 | `curl \| bash` |
| 민감한 데이터 외부 전송 | API 키, 네트워크를 통한 자격 증명 |
| 프로덕션 배포 | 프로덕션을 대상으로 하는 배포 명령어 |
| 대량 삭제 | 대규모 디렉터리에 대한 `rm -rf` |
| IAM 변경 | 권한 및 역할 수정 |
| main으로 강제 푸시 | `git push --force origin main` |

> **분류기로 이동한 결정 확대 (v2.1.218)**: 분류기는 `rm -rf /`, `rm -rf ~`처럼 파일 시스템 루트나 홈 디렉터리를 대상으로 하는 삭제도 판단하며, 삭제가 명령어 치환이나 프로세스 치환 안에 있는 경우도 포함합니다. v2.1.218 이전에는 일반 형태는 대신 승인을 요청했고, 치환 형태는 v2.1.208부터 v2.1.217까지 승인을 요청했습니다. 백그라운드 `&` 검사와 의심스러운 Windows 경로 검사도 더 이상 권한 대화 상자를 열지 않으며, 분류기가 판단합니다. v2.1.281부터 이와 같이 인식된 중요 경로 삭제는 자동 모드에서 다시 승인을 요청하며, 터미널에서는 2분 카운트다운이 표시되고 그 외 환경에서는 즉시 거부됩니다. 분류기는 `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1`이 설정된 경우에만 이를 판단합니다.

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

**기본 자동 모드 구성 복원** (v2.1.212), 확인 프롬프트 포함(`--yes`로 건너뛰기):
```bash
claude auto-mode reset
claude auto-mode reset --yes
```

엔터프라이즈 배포를 위해 `autoMode.environment` 관리형 설정을 통해 **신뢰할 수 있는 인프라를 구성**합니다. 이를 통해 관리자는 신뢰할 수 있는 CI/CD 환경, 배포 대상 및 인프라 패턴을 정의할 수 있습니다.

**`/auto-mode-setup`으로 환경 항목 초안 작성**: 이 안내형 명령어는 프로젝트와 최근 세션을 읽고 `autoMode.environment` 항목(때로는 규칙 항목)을 제안하며, 수락하면 `~/.claude/settings.json`에 기록합니다. Pro, Max, Team은 v2.1.228+(네이티브 Windows에서는 v2.1.233+)가 필요하고, Enterprise와 Claude Console API 키는 v2.1.283+가 필요합니다. v2.1.304부터는 Bedrock, Vertex, Foundry 및 텔레메트리가 꺼진 환경에서도 작동합니다.

#### `"$defaults"`로 기본값 확장 (v2.1.118)

v2.1.118부터 `autoMode.allow`, `autoMode.soft_deny`, `autoMode.environment`는 `"$defaults"` 토큰을 허용하여 기본 제공 목록을 교체하는 대신 사용자 규칙을 **추가**합니다. v2.1.118 이전에는 사용자 정의 배열이 기본 제공 목록을 조용히 덮어썼습니다.

#### `autoMode.hard_deny`를 사용한 무조건 차단 (v2.1.136)

`autoMode.hard_deny` (v2.1.136+)는 **추론된 사용자 의도와 관계없이** 특정 유형의 작업을 차단하는 분류기 규칙 배열입니다. 자동 모드에서 절대로 실행되어서는 안 되는 작업에 사용하십시오. 예를 들어, 루트 경로의 `rm -rf` 또는 보호된 브랜치의 `git push --force`가 있습니다. `soft_deny`와 달리 hard-deny 규칙은 분류기가 재량으로 바꿀 수 없습니다.

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

`"$defaults"`를 사용하면 기본 규칙을 유지하면서 그 위에 조직 또는 프로젝트별 규칙을 추가할 수 있습니다.

#### `autoMode.classifyAllShell`로 모든 셸 명령어 분류 (v2.1.193)

`autoMode.classifyAllShell` (부울, v2.1.193+)은 **모든** Bash/PowerShell 명령어를 자동 모드 분류기로 라우팅합니다. 분류기가 세션의 모든 셸 명령어를 검사하도록 하려면 이 기능을 활성화하십시오.

```json
{
  "autoMode": {
    "classifyAllShell": true
  }
}
```

같은 릴리스에서 자동 모드가 작업을 차단할 때 **거부 사유**가 표시됩니다 — 트랜스크립트, 거부 토스트, `/permissions` 아래의 최근 거부 목록에서 볼 수 있습니다 (v2.1.193+).

#### 내장된 의도 기반 보호 (v2.1.183)

사용자가 구성하는 `hard_deny`와 별도로, 자동 모드는 다음과 같은 파괴적인 명령어를 이 세션에서 명시적으로 요청하지 않는 한 기본적으로 차단합니다:

- `git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`
- `git commit --amend` (커밋이 이 세션에서 에이전트에 의해 만들어지지 않은 경우)
- `terraform destroy`, `pulumi destroy`, `cdk destroy` (특정 스택을 요청하지 않는 한)

이는 추론된 의도에 기반한 내장 기본 보호 기능입니다. 이러한 항목을 `hard_deny`에 직접 추가할 필요가 없습니다.

### 대체 동작

분류기가 확신하지 못할 때 자동 모드는 사용자에게 프롬프트를 표시하는 것으로 대체됩니다:
- **3회 연속** 분류기 차단 후
- 세션에서 **총 20회** 분류기 차단 후

이를 통해 분류기가 작업을 확신을 갖고 승인할 수 없을 때 사용자가 항상 제어권을 유지합니다.

### 자동 모드에 준하는 권한 시드

백그라운드 분류기 없이 더 간단한 접근 방식을 원한다면, `~/.claude/settings.json`에 보수적인 안전 권한 규칙의 기준선을 시드할 수 있습니다. 스크립트는 읽기 전용 및 로컬 검사 규칙으로 시작한 다음, 편집, 테스트, 로컬 Git 쓰기, 패키지 설치 및 GitHub 쓰기 작업은 원할 때만 옵트인할 수 있도록 합니다.

**파일:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# 추가될 내용 미리 보기 (변경 사항은 기록되지 않음)
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# 보수적인 기준선 적용
python3 09-advanced-features/setup-auto-mode-permissions.py

# 필요할 때만 기능 추가
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

스크립트는 다음 범주에 걸쳐 규칙을 추가합니다:

| 범주 | 예시 |
|----------|---------|
| 핵심 읽기 전용 도구 | `Read(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)`, `WebFetch(*)` |
| 로컬 검사 | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)`, `Bash(cat:*)` |
| 선택적 편집 | `Edit(*)` |
| 선택적 테스트/빌드 | `Bash(pytest:*)`, `Bash(python3 -m pytest:*)`, `Bash(cargo test:*)` |
| 선택적 Git 쓰기 | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)`, `Bash(git switch:*)`, `Bash(git stash:*)`, `Bash(git tag:*)` |
| 패키지 관리자 | `Bash(npm ci:*)`, `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(pip3 install:*)` |
| 빌드 및 테스트 | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| 일반 셸 | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)` |
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

/tasks    # 백그라운드 작업(셸 및 서브에이전트) 보기 및 관리, 여기서 작업 중지 가능
Ctrl+B    # 실행 중인 Bash 명령어나 에이전트를 백그라운드로 이동
```

### 백그라운드 작업 시작

```
User: Run the full test suite in the background

Claude: 백그라운드에서 테스트를 시작합니다 (task-id: bg-1234)
테스트가 실행되는 동안 작업을 계속할 수 있습니다.

[대화를 계속할 수 있습니다]

User: Meanwhile, let's refactor the auth module

Claude: [테스트가 백그라운드에서 실행되는 동안 인증 모듈을 리팩터링합니다]

[나중에, 테스트가 완료되면]

Claude: 📢 백그라운드 작업 bg-1234 완료:
✅ 245 tests passed
❌ 3 tests failed
결과 보기: /tasks
```

### 백그라운드 작업 관리

`/tasks`(별칭 `/bashes`)를 실행하면 실행 중인 셸과 서브에이전트를 나열하고, 하나를 열어 출력을 보거나 중지할 수 있습니다. `/task` 하위 명령어는 없습니다.

```text
User: /tasks

[백그라운드 작업 보기가 열립니다: 실행 중인 셸과 서브에이전트,
 완료된 서브에이전트도 포함됩니다. 하나를 선택해 출력을 보거나
 여기서 중지할 수 있습니다.]
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

백그라운드 작업을 위한 `settings.json` 블록은 없습니다. 이 기능은 환경 변수로 제어합니다:

```bash
# 백그라운드 Bash/서브에이전트 실행과 Ctrl+B 끄기 (MCP 작업과 Monitor 도구는 여전히 백그라운드에서 실행됨)
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1
```

동시 실행 수도 백그라운드 작업 설정이 아닙니다. 한 번에 실행되는 에이전트 수는 `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`(기본값 `20`)가 결정합니다.

백그라운드 Bash 및 PowerShell 명령어는 무인 세션에서만 시간 제한이 있습니다(v2.1.288). `-p` 실행, Agent SDK 세션, CI 또는 클라우드 세션에서 `run_in_background`로 시작한 명령어는 `timeout`(기본 30분, 최대 2시간) 후 중지되며, 중지되면 Claude에 알림이 갑니다. 터미널, 데스크톱 앱 또는 VS Code 세션의 백그라운드 명령어에는 시간 제한이 없습니다(v2.1.285–v2.1.287에서는 모든 세션에 제한이 적용되었습니다).

---

## 모니터 도구 (이벤트 기반 스트림)

> **v2.1.98에 새로 추가**: 모니터 도구를 사용하면 Claude가 백그라운드 명령어의 stdout을 관찰하고 일치하는 이벤트가 나타나는 즉시 반응할 수 있습니다. 장기 실행 프로세스를 기다리기 위한 폴링 루프와 `sleep`을 대체합니다.

모니터는 stdout에 쓰는 모든 셸 명령어에 연결됩니다. 명령어에서 나오는 각 stdout 줄은 세션을 깨우는 알림이 됩니다. Claude가 명령어를 지정하면, 하네스가 출력을 스트리밍하고 이벤트가 발생하면 전달합니다. 기반 프로세스 실행에 대해서는 관련 [백그라운드 작업](#백그라운드-작업) 섹션을 참조하십시오.

> **기한 (v2.1.271)**: 이제 모든 모니터 감시에는 기한이 있습니다. 최대 30분이며, 단일 프롬프트 `-p` 실행에서는 10분입니다. 기한이 지나면 Claude에 알림이 가서 감시를 다시 설정할 수 있습니다. 시간 제한이 없는 감시를 설정하는 방법은 더 이상 없습니다.

> **사용 가능 여부 (v2.1.310)**: Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform 또는 Microsoft Foundry에서, 또는 `DISABLE_TELEMETRY`나 `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`가 설정된 경우 모니터를 사용하려면 Claude Code v2.1.310 이상이 필요합니다. Windows에서는 Git Bash가 필요합니다.

### 왜 중요한가요?

`/loop` 또는 `sleep`을 사용하는 폴링은 변경 사항이 있는지 여부와 관계없이 매 주기마다 전체 API 왕복을 소모합니다. 모니터는 이벤트가 발생할 때까지 조용히 있으며, 명령어가 조용한 동안에는 **토큰을 전혀 소비하지 않습니다**. 이벤트가 발생하면 Claude는 즉시 반응하므로, 다음 폴링 주기까지 기다리느라 발견이 늦어지지 않습니다. 몇 분 이상 실행되는 모든 작업에 대해 이는 폴링 루프보다 저렴하고 빠릅니다.

### 두 가지 일반적인 패턴

**스트림 필터**는 장기 실행 소스에서 지속적인 출력을 관찰합니다. 명령어는 계속 실행되며, 일치하는 모든 줄이 이벤트가 됩니다.

```bash
tail -f /var/log/app.log | grep --line-buffered "ERROR"
```

**폴-앤-이밋 필터**는 주기적으로 소스를 확인하고 변경 사항이 있을 때만 이벤트를 발생시킵니다. API, 데이터베이스 또는 네이티브 스트림이 없는 모든 것에 사용하십시오.

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

> **경고**: `grep`으로 파이핑할 때 **항상** `grep --line-buffered`를 사용하십시오. 이를 사용하지 않으면 grep이 stdout을 4KB 청크로 버퍼링하여 트래픽이 적은 스트림에서 이벤트가 몇 분 지연될 수 있습니다. 이는 실제로 모니터가 고장 나는 가장 흔한 원인입니다. 필터가 작동해야 할 때 침묵하는 것처럼 보이면 먼저 `--line-buffered` 플래그를 확인하십시오.

---

## 동적 워크플로

> **v2.1.154에 새로 추가**

동적 워크플로를 사용하면 Claude가 수십에서 수백 개의 백그라운드 [서브에이전트](../04-subagents/README.md)를 **결정적으로** 조율할 수 있습니다. 즉, 팬아웃, 파이프라인 및 병렬 단계가 모델의 즉흥에 맡겨지는 대신 스크립트에 인코딩됩니다. 단일 에이전트가 하나의 컨텍스트 창을 유지하는 반면, 워크플로는 많은 에이전트에 걸쳐 작업을 분해하고 그 결과를 재결합합니다.

v2.1.219부터 동적 워크플로의 기본값은 **중간 크기 지침(에이전트 10개 미만 목표)**이며, v2.1.271부터 Pro 플랜으로 로그인한 경우에는 **small**입니다. 다른 크기(또는 제한 없음)는 `/config`의 **Dynamic workflow size**에서 선택하거나 설정 파일에 `workflowSizeGuideline` 키를 설정하면 됩니다. 실행 중인 워크플로의 상태 표시줄에는 활성 크기가 표시되며, 변경하려면 `/config`를 안내합니다.

### 사용 시점

- **포괄적인 범위** — 많은 파일/차원에 걸쳐 병렬로 감사 또는 검토.
- **신뢰성** — 독립적인 관점을 생성한 다음, 커밋하기 전에 발견 사항을 적대적으로 검증.
- **단일 컨텍스트를 넘어서는 확장** — 대규모 마이그레이션, 광범위한 조사 또는 단일 컨텍스트로는 담을 수 없는 연구.

이미 이해하고 있는 일회성 작업의 경우, 단일 에이전트 (또는 직접 편집)가 여전히 올바른 도구입니다. 워크플로는 작업이 분산될 때 효과를 발휘합니다.

### 실행 및 보기

- **실행**: Claude에게 작업을 위한 워크플로를 생성하도록 요청합니다 (예: "`src/`의 모든 파일을 검토하는 워크플로를 실행해 줘"). Claude는 오케스트레이션 스크립트를 작성하고 백그라운드에서 실행합니다.
- **보기**: `/workflows` 명령어는 라이브 진행 상황과 함께 실행 중이거나 완료된 워크플로 실행을 표시합니다.
- **`ultracode`**: `/effort` 슬라이더의 Ultracode 토글(Tab) 또는 `/effort ultracode [on|off]`로 켭니다. 그러면 Claude가 세션이 실행 중인 노력 수준에서 기본적으로 동적 워크플로를 조율합니다. v2.1.284부터 이 토글은 노력 수준을 바꾸지 않습니다(이전에는 `xhigh`를 강제했습니다). `--effort ultracode`와 Agent SDK의 `effortLevel: "ultracode"`는 여전히 `xhigh`를 설정합니다. `/effort ultracode`는 세션 동안 유지되며, 모든 세션을 이 기능과 함께 시작하려면 설정에서 `ultracode` 키를 설정하십시오(`effortLevel`과 `CLAUDE_CODE_EFFORT_LEVEL`은 `ultracode`를 허용하지 않습니다). (v2.1.160부터 트리거 키워드는 `ultracode`이며, "workflow" 단어만으로는 더 이상 실행되지 않습니다.)

워크플로는 서브에이전트 모델을 기반으로 구축됩니다. 개별 에이전트가 정의되고 범위가 지정되는 방법은 [서브에이전트](../04-subagents/README.md)를 참조하십시오.

---

## 예약된 작업

예약된 작업을 사용하면 반복적인 일정 또는 일회성 알림으로 프롬프트를 자동으로 실행할 수 있습니다. 작업은 세션 범위이며, Claude Code가 활성 상태일 때 실행되고 세션이 종료되면 지워집니다. v2.1.72+부터 사용할 수 있습니다.

> **"Routines"는 이제 "클라우드 예약 작업"입니다 (2026년 10월)**: Anthropic 문서는 `/schedule`(별칭 `/routines`, 아래 참조)로 만드는 클라우드 작업인 Routines의 이름을 **클라우드 예약 작업(이전 명칭 routines)**으로 바꾸었고, 이 페이지의 `/loop` 및 크론 작업은 **세션 범위 예약 작업**이라고 부릅니다. 이전 이름은 `claude.ai/code/routines` URL, `/fire` API, 관리자 토글 **Scheduled tasks (Was Routines)**에 남아 있습니다.

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

클라우드 예약 작업은 재시작 후에도 유지되며 Claude Code가 로컬에서 실행 중일 필요가 없습니다. 자동 모드를 사용할 수 없는 경우가 아니면 각 실행은 자동 모드로 시작하므로 분류기가 작업을 승인하거나 차단합니다. 다만 ask 규칙이 일치하거나 차단 횟수가 자동 모드의 반복 차단 임계값에 도달하면 실행은 여전히 중지되고 세션에서 응답을 기다립니다. 사용자 지정 역할을 사용하는 Enterprise 플랜에서는 예약 작업 권한이 있는 역할도 필요합니다.

### 예약된 작업 비활성화

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

> **`/schedule` API 키 티어에 의해 자동 비활성화됨 (v2.1.139)**: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, 또는 `apiKeyHelper` 중 하나라도 설정되어 있으면 클라우드 `/schedule`은 자동으로 비활성화됩니다. claude.ai로 로그인되어 있는 경우에도 마찬가지입니다. 동일한 조건으로 [원격 제어](#원격-제어-비활성화-disableremotecontrol-v21128), claude.ai MCP 커넥터, 알림 설정이 비활성화됩니다. `/schedule`을 사용하려면 API 키를 해제하거나 Pro/Max OAuth 티어에서 실행하십시오. 로컬 `CronCreate`에는 영향을 미치지 않습니다.

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
| `manual` | 파일만 읽음; 다른 모든 작업에 대해 프롬프트를 표시. v2.1.200에서 `default`에서 이름이 바뀌었으며, `default`는 여전히 별칭으로 허용됩니다 |
| `acceptEdits` | 파일 읽기 및 편집; 명령어에 대해 프롬프트를 표시 |
| `plan` | 파일만 읽음 (연구 모드, 편집 불가) |
| `auto` | 백그라운드 안전 분류기 검사를 거쳐 모든 작업 수행. 적격한 모델(모든 제공자에서 Sonnet 5 이상, Opus 4.7 이상, Haiku 5.5 또는 Fable 모델. Anthropic API 및 Claude Platform on AWS에서는 Opus 4.6과 Sonnet 4.6도 해당)과 제공자가 필요합니다. 모든 플랜에서 사용 가능하며, [자동 모드](#자동-모드)를 참조하십시오 |
| `bypassPermissions` | 모든 작업, 권한 검사 없음 (위험) |
| `dontAsk` | 미리 승인된 도구만 실행; 다른 모든 것은 거부 |

> **참고**: `default` 권한 모드는 v2.1.200에서 **Manual**로 이름이 바뀌었으며(CLI, `--help`, VS Code, JetBrains 전반), 이 모드가 활성화된 동안에는 하단에 회색 ⏸ 배지가 표시됩니다(v2.1.203). `--permission-mode manual`과 `--permission-mode default` 모두 작동하며, 설정의 `"defaultMode": "manual"`과 `"defaultMode": "default"`도 마찬가지입니다. 설정 키는 `permissions.defaultMode`이며 `permissions.mode` 키는 없으므로, 아래 예시는 정식 철자를 사용합니다.

CLI에서 `Shift+Tab`으로 모드를 순환할 수 있습니다. `--permission-mode` 플래그 또는 `permissions.defaultMode` 설정으로 기본값을 설정합니다. 권한 모드가 구성되지 않은 경우, v2.1.284부터 모든 플랜과 제공자에서 대화형 터미널 및 VS Code 세션은 자동 모드로 시작합니다(v2.1.283에서는 Bedrock, Google Cloud's Agent Platform, Foundry 같은 서드파티 제공자나 텔레메트리가 꺼진 경우에만 그랬습니다). `permissions.defaultMode`가 여전히 이를 재정의하며, 자동 모드를 사용할 수 없는 세션은 대신 Manual로 시작합니다. v2.1.302부터 권한 모드가 설정되지 않은 `claude -p` 또는 Agent SDK 실행은 Manual 모드(구성 값 `default`)로 시작하며 승인이 필요한 도구 호출을 거부합니다. `--permission-mode`(예: `auto` 또는 `acceptEdits`)나 `--allowedTools`를 전달하십시오.

> **계획 모드는 셸 명령어를 분류기에 맡깁니다 (v2.1.218)**: [자동 모드](#자동-모드)를 사용할 수 있고 `useAutoModeDuringPlan` 설정이 켜져 있으면(기본값), 계획 중에 분류기가 프롬프트 대신 셸 명령어를 검토합니다. 승인된 명령어는 실행되고 거부된 명령어는 차단됩니다. 계획 모드는 여전히 파일 쓰기를 무조건 차단합니다.

v2.1.160부터 `acceptEdits` 모드에서도 셸 시작 파일 (`.zshenv`, `.zlogin`, `.bash_login`, `~/.config/git/`) 및 코드 실행 빌드 구성 (`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`, `.pre-commit-config.yaml`, `.devcontainer/`, …)을 작성하기 전에 프롬프트를 표시합니다. 그렇지 않으면 의도치 않은 명령어 실행으로 이어질 수 있기 때문입니다.

> **`--dangerously-skip-permissions` 확장 경로 범위 (v2.1.121, v2.1.126)**: `--dangerously-skip-permissions` CLI 플래그 (및 동등한 `bypassPermissions` 모드)는 이제 훨씬 더 광범위한 허용 목록 (`.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/`, `.git/`, `.vscode/`, 셸 구성 파일)에 대한 쓰기 프롬프트를 우회합니다. 재앙적인 삭제 명령어 (`rm -rf /` 등)는 이 모드에서도 여전히 프롬프트를 표시합니다. v2.1.281부터 터미널 프롬프트는 2분간 기다린 후 재작성 힌트와 함께 명령어를 거부하여 무인 세션이 계속 진행되도록 하며, v2.1.309부터 데스크톱 앱과 VS Code는 같은 힌트와 함께 즉시 거부합니다(`CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1`로 타임아웃을 끌 수 있습니다). 자동 모드도 이러한 중요 경로 삭제를 같은 방식으로 처리하며(터미널에서는 2분 프롬프트, 그 외에서는 즉시 거부), 해당 변수가 설정된 경우에만 분류기로 보냅니다. v2.1.304부터 `/Volumes/USB`나 WSL의 `/mnt/c/Users` 같은 마운트된 드라이브 경로에 대한 재귀 `rm`은 `rm` 허용 규칙이 있더라도 같은 처리를 받습니다. 이 프롬프트를 끄려면 `CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT=1`로 Claude Code를 시작하십시오(설정의 `env` 블록은 무시됩니다). 이 플래그는 이전보다 더 날카로운 도구로 취급하십시오. 일회용 샌드박스에서만 사용하십시오.

> **Windows 셸 감지 (v2.1.120, v2.1.126)**: Git for Windows / Git Bash는 더 이상 필수가 아닙니다. Git Bash가 없으면 Claude Code는 PowerShell을 셸 도구로 사용합니다. v2.1.126부터 PowerShell 도구가 활성화되면 PowerShell이 *기본* 셸이며, Microsoft Store, PATH가 없는 MSI, 또는 `.NET 전역 도구`를 통해 설치된 PowerShell 7도 감지합니다.

> **PowerShell 도구가 Windows용 Bedrock/Vertex/Foundry에서 기본적으로 활성화됨 (v2.1.143)**: v2.1.143부터 PowerShell 도구는 Bedrock, Vertex, Foundry 사용자를 위해 **Windows에서 기본적으로 활성화됩니다**. Claude Code는 `-ExecutionPolicy Bypass`로 PowerShell을 호출하므로 시스템 정책이 `Restricted`인 경우에도 스크립트가 실행됩니다. Claude Code가 시스템 실행 정책을 따르도록 하려면 `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`을 설정하십시오. PowerShell 도구를 완전히 비활성화하려면 `CLAUDE_CODE_USE_POWERSHELL_TOOL=0`을 설정하십시오.

### 활성화 방법

**키보드 단축키**:
```bash
Shift + Tab  # default → acceptEdits → plan 순으로 순환하며, 사용 가능하면 bypassPermissions/auto로 이어짐 (dontAsk는 순환에 나타나지 않음)
```

**슬래시 명령어**:
```bash
/plan                  # 계획 모드 진입
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

#### 계획 모드
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

### 인쇄 모드란 무엇입니까?

인쇄 모드는 다음을 가능하게 합니다:
- 자동화된 스크립트 실행
- CI/CD 통합
- 배치 처리
- 예약된 작업

### 인쇄 모드에서 실행 (비대화형)

```bash
# 특정 작업 실행
claude -p "Run all tests" --permission-mode auto

# 파이프된 내용 처리
cat error.log | claude -p "Analyze these errors"

# CI/CD 통합 (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### 추가 인쇄 모드 사용 예시

```bash
# 출력 캡처를 통해 특정 작업 실행
claude -p "Run all tests and generate coverage report" --permission-mode auto

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
| `/fork [prompt]` | 대화를 새로운 독립 백그라운드 세션으로 복사하고 여기서는 계속 작업 (v2.1.212+) |
| `/subtask <task>` | 전체 대화를 상속하는 포크된 서브에이전트를 생성하고 결과를 여기로 보고받음 (v2.1.212+) |
| `/branch [name]` | 이 시점의 대화 사본으로 전환하며 원본은 보존 |
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

> **v2.1.212 업데이트**: 이제 에이전트 보기에서 인수 없이 `/resume`을 입력하면 지난 세션 선택기(표시 목록에서 제거된 세션 포함)가 열리고, 선택한 세션을 백그라운드 세션으로 다시 시작합니다.

> **v2.1.304 업데이트**: Pro 및 Max 플랜에서 오래 비활성 상태였던 대화를 다시 시작할 때 5시간 사용 한도의 상당 부분을 사용하게 되면 **Resume this conversation?** 대화 상자가 표시됩니다. 그래도 다시 시작하거나 새 대화를 시작할 수 있습니다(이전 대화를 언급하면 Claude가 여전히 찾아볼 수 있습니다).

### 세션 포크 및 브랜치

대화 사본을 만드는 명령어는 세 가지이며, *사본이 실행되는 위치*가 다릅니다:

`/subtask <task>`는 전체 대화를 상속하는 포크된 서브에이전트를 생성하여, 사용자가 계속 작업하는 동안 해당 작업을 처리합니다. `claude agents`에 자체 행이 생기며, 완료되면 결과가 대화로 반환됩니다:

```
/subtask Investigate why the auth tests are flaky
```

`/fork [prompt]`는 대신 대화를 새로운 **백그라운드 세션**으로 복사합니다. 사본은 지금까지의 모든 내용으로 시작해 독립적으로 실행되며, 이 대화로는 아무것도 돌아오지 않습니다:

```
/fork Try the OAuth approach end to end
```

위임하지 않고 직접 사본으로 전환하려면 `/branch [name]`을 사용합니다. 원본이 보존되며 `/resume`으로 원본에 돌아갈 수 있습니다:

```
/branch try-oauth-instead
```

> **참고**: `/fork`와 `/subtask`는 **v2.1.212**에서 역할이 바뀌었습니다. v2.1.161 이전에는 `/fork`가 `/branch`의 별칭이었고, v2.1.161부터 v2.1.211까지는 포크된 서브에이전트를 시작했습니다(현재 `/subtask`가 담당하는 동작). 에이전트 보기가 꺼져 있으면 `/subtask`를 사용할 수 없으며 `/fork`가 포크된 서브에이전트 동작을 유지합니다.

또는 CLI에서 포크:
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

### 사용 한도 자동 계속 (v2.1.234)

**v2.1.234**부터 claude.ai 사용 한도에 막힌 세션은 한도가 재설정되면 자동으로 계속됩니다. 수동으로 다시 프롬프트할 필요가 없습니다. `/config`의 "Continue automatically at usage limit"에서 전환할 수 있습니다.

### 세션 요약 (v2.1.108)

자리를 비웠다가 세션으로 돌아오면 Claude가 수행된 작업에 대한 간략한 요약을 표시할 수 있습니다. 이 기능은 모든 플랜과 제공자에서 기본적으로 켜져 있으며, `/config` → **Session recap**에서 끌 수 있습니다.

> **OTEL 텔레메트리 — 피드백 설문조사 재활성화 (v2.1.136+)**: OpenTelemetry 데이터를 캡처하는 조직은 `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL=1`을 설정하여 Anthropic의 세션 품질 설문조사를 다시 활성화할 수 있습니다. 설문조사는 이전에 텔레메트리 파이프라인에서 우회되었기 때문에 OTEL 배포에서는 기본적으로 꺼져 있습니다.

> **OTEL 텔레메트리 — `assistant_response` 로그 이벤트 (v2.1.193+)**: Claude Code는 모델의 응답 텍스트를 담은 `claude_code.assistant_response` OpenTelemetry 로그 이벤트를 내보내므로, OTEL 파이프라인이 기존 도구/이벤트 텔레메트리와 함께 Claude가 말한 내용을 캡처할 수 있습니다.

> **OTEL 텔레메트리 — 캐시 및 GenAI 속성 (v2.1.300)**: `api_request` 이벤트에 `cache_creation_5m_tokens`/`cache_creation_1h_tokens`가 추가되고, span에는 `gen_ai.provider.name` 같은 GenAI 시맨틱 규약 속성이 포함됩니다.

> **OTEL 텔레메트리 — `tool_decision` 속성 (v2.1.301)**: `tool_decision` 이벤트에 `classifier_verdict`와 `permission_mode`가 추가됩니다.

> **OTEL 텔레메트리 — `safety_event` (v2.1.307)**: 권한 규칙, 자동 모드, 안전 검사, 훅 또는 샌드박스가 거부하거나, 승인을 요청하거나, 되돌려 보낸 각 도구 호출에 대해 새로운 `claude_code.safety_event` 로그 이벤트가 발생하며, `category`, `decision`(`accept`/`reject`/`sent_back`), `decision_source` 속성을 포함합니다. 명령어 텍스트, 파일 경로, 호스트 이름은 포함하지 않습니다.

> **OTEL 텔레메트리 — 조인 속성 (v2.1.310)**: `tool_decision` 및 `tool_result` 이벤트에 호출을 API 응답과 조인하기 위한 `request_id`가 추가되고, 서브에이전트 이벤트에는 `parent_agent_id`가 포함됩니다.

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

## 세션 간 메시징

> **v2.1.224에서 추가**되었으며 v2.1.239까지 확장되었습니다. **macOS, Linux 및 (v2.1.239부터) Windows**에서 사용할 수 있습니다.

예전에는 세션이 서로 고립되어 있었습니다. 세션 간 메시징을 사용하면 한 Claude Code 세션이 다른 세션(다른 머신의 세션과 클라우드 세션 포함)과 대화할 수 있으므로, 다시 설명하는 대신 이미 적절한 컨텍스트가 로드된 세션에 질문을 넘길 수 있습니다.

### 세션 검색

`ListAgents`는 메시지를 보낼 수 있는 모든 대상을 나열합니다. 직접 생성한 서브에이전트, 이 머신의 다른 로컬 세션, 클라우드 세션, 그리고 (원격 제어가 연결된 경우) 다른 머신의 세션이 포함됩니다. 각 행에는 종류가 표시되며, v2.1.229부터는 `offline` 및 `cloud` 레이블도 붙어 연결 가능한 세션과 휴면 세션을 구분할 수 있습니다.

**각 행의 이름이 주소**이며, 이것으로 메시지를 보냅니다.

### 메시지 보내기

`SendMessage`는 대상과 메시지를 받습니다:

```text
SendMessage({ to: "<session name>", message: "What did you conclude about the retry logic?" })
```

v2.1.232부터는 이름만으로 충분합니다. 두 행이 실제로 같은 이름을 갖는 경우가 아니면 구분용 참조를 덧붙일 필요가 없습니다.

### 세션이 유휴 상태가 될 때까지 대기 (`notify_when_idle`, v2.1.236)

메시지를 보내는 세션이 작업 중이라면, 보통 폴링하기보다는 작업이 끝나는 시점을 알고 싶을 것입니다. `SendMessage`는 바로 이를 위한 `notify_when_idle` 입력을 받습니다:

```text
SendMessage({
  to: "auth-refactor",
  message: "ping me when the migration finishes",
  notify_when_idle: true
})
```

이는 **옵트인 방식이며 일회성**입니다. 대상 세션은 다음에 유휴 상태가 될 때 알림을 한 번 보내고, 구독은 그것으로 끝납니다. 폴링 루프가 없으며, 세션이 다시 바빠졌다가 유휴 상태가 되어도 알림이 반복되지 않습니다.

관련된 v2.1.239 변경 사항 두 가지: 이제 `ListAgents`는 활성 팀원과 함께 **세션 자신의 이름**도 보고하며(세션이 다른 세션에 자신의 주소를 알려줄 수 있도록), 세션 간 메시징을 **Windows**에서도 사용할 수 있게 되었습니다.

### `@`-멘션 축약 (v2.1.232)

도구를 명시적으로 호출하는 대신, 프롬프트에서 세션을 직접 `@`-멘션하여 메시지를 보낼 수 있습니다:

```text
@auth-refactor did the migration tests pass?
```

### 수신 메시지 제어: `crossSessionInbound`

수신 메시지는 `crossSessionInbound` 설정(v2.1.224+)으로 제어됩니다:

| 값 | 동작 |
|---|---|
| `"accept"` | 수신 메시지가 이 세션의 Claude에게 전달됩니다 |
| `"hold"` | 메시지가 도착했다는 알림만 표시되고 전달되지 않습니다 |
| `"refuse"` | 수신 메시지가 삭제됩니다 |

값은 `accept < hold < refuse` 순서의 단계를 이루며, **프로젝트 및 로컬 설정은 사용자 범위 값보다 더 엄격할 때만 적용됩니다**. 프로젝트는 수신 전달을 강화할 수만 있고 완화할 수는 없습니다. v2.1.232부터 이 설정은 `/config`에도 "Messages from your other sessions" 행으로 표시됩니다.

### 도달 범위 및 제한

- 같은 머신의 로컬 세션과 클라우드 세션.
- 다른 머신의 원격 제어 세션(이름으로 지정 가능, v2.1.225).
- 클라우드 세션은 메시지를 **수신**하지만 아직 로컬 세션에 답장을 보낼 수 없습니다. 답변은 해당 세션의 트랜스크립트에서 확인하십시오.
- macOS 및 Linux는 v2.1.224부터, Windows는 v2.1.239부터 지원됩니다.

---

## 대화형 기능

### 키보드 단축키

Claude Code는 효율성을 위한 키보드 단축키를 지원합니다. 다음은 공식 문서의 전체 참조입니다:

| 단축키 | 설명 |
|----------|-------------|
| `Ctrl+C` | 현재 입력/생성 취소 |
| `Ctrl+D` | Claude Code 종료 |
| `Ctrl+G` | 외부 편집기에서 계획 편집 |
| `Ctrl+L` | 화면 다시 그리기 (다시 그리기만 수행 — 두 번 눌러 `/clear`하는 단축키는 v2.1.238에서 제거됨) |
| `Ctrl+O` | 자세한 출력 전환 (추론 보기) |
| `Ctrl+R` | 기록 역방향 검색. **모든 프로젝트의 모든 프롬프트**를 기본으로 검색합니다 (v2.1.129+); 선택기 내에서 `Ctrl+S`를 누르면 현재 프로젝트로 범위를 좁힙니다. 이전 버전은 프로젝트 전용이 기본값이었습니다. |
| `Ctrl+T` | 작업 목록 보기 전환 |
| `Ctrl+B` | 실행 중인 작업을 백그라운드로 보내기 |
| `Esc+Esc` | 코드/대화 되감기 |
| `Shift+Tab` / `Alt+M` | 권한 모드 전환 |
| `Option+P` / `Alt+P` | 모델 전환 |
| `Option+T` / `Alt+T` | 확장 사고 전환 |
| `Option+O` / `Alt+O` | 빠른 모드 전환 (`/fast`) |
| `Ctrl+X` `Ctrl+K` | 모든 백그라운드 서브에이전트 중지 |
| `Ctrl+Enter` (또는 `Ctrl+X` `Ctrl+S`) | 지금 보내기 — 대기 중인 모든 메시지를 한 번에 보냅니다. v2.1.281부터 턴이 취소되는 대신 실행 중인 도구와 서브에이전트가 백그라운드로 이동합니다. 보낸 메시지와 대기 중인 메시지는 모델이 받을 때까지 회색으로 표시됩니다 (v2.1.275) |
| `Ctrl+S` | 현재 프롬프트 임시 보관; 다시 누르면 복원 |
| `Ctrl+_` | 프롬프트 입력의 마지막 편집 실행 취소 |
| `:` | 단어 시작에 `:`를 입력하면 이모지 단축 코드 자동 완성이 열립니다. 예: `:heart:` (v2.1.217+) |

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
| `↑ / ↓` | 명령어 기록 |

### 접근성

화면 낭독기 모드(v2.1.208+)는 CLI를 화면 낭독기용으로 설계된 일반 텍스트 렌더링 모드로 전환합니다. CLI 플래그, 환경 변수 또는 사용자 설정(`~/.claude/settings.json`), 관리형 설정, `--settings`로 전달한 파일의 `axScreenReader` 키로 활성화합니다. v2.1.305부터 Claude Code는 프로젝트 및 로컬 설정에 있는 이 키와 `env` 블록의 `CLAUDE_AX_*` 변수를 무시합니다:

```bash
claude --ax-screen-reader
```

```bash
export CLAUDE_AX_SCREEN_READER=1
```

```json
{
  "axScreenReader": true
}
```

### 키 바인딩 사용자 지정

`/keybindings`를 실행하여 사용자 지정 키보드 단축키를 생성합니다. 이 명령어는 `~/.claude/keybindings.json`을 열어 편집할 수 있도록 합니다 (v2.1.18+).

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

키 바인딩은 코드(chord) 시퀀스 (다중 키 조합)를 지원합니다:

```
"ctrl+k ctrl+s"   → 두 키 시퀀스: ctrl+k를 누른 다음 ctrl+s를 누릅니다
"ctrl+shift+p"    → 동시에 여러 보조 키를 누름
```

**키 입력 구문**:
- **수정자**: `ctrl` (또는 `control`), `alt` (또는 `opt`, `option`, `meta`), `shift`, `cmd` (또는 `command`, `super`, `win`) — `cmd`는 `meta`의 별칭이 아닌 별도의 수정자이며, Super 키를 보고하는 터미널에서만 감지됩니다
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

### 명령어 기록

이전 명령어에 액세스합니다:

```
User: <↑>  # 이전 명령어
User: <↓>  # 다음 명령어
User: Ctrl+R  # 기록 검색

(reverse-i-search)`test': run all tests
```

### 여러 줄 입력

복잡한 쿼리의 경우 `\` + Enter, Option+Enter(macOS), Shift+Enter 또는 Ctrl+J로 새 줄을 시작합니다. `\end` 종료자는 없으며, Enter를 누르면 전송됩니다:

```bash
User: Long complex prompt \
spanning multiple lines
```

**예시:**

```
User: Implement a user authentication system \
with the following requirements: \
- JWT tokens \
- Email verification \
- Password reset \
- 2FA support

Claude: [여러 줄 요청을 처리합니다]
```

### 인라인 편집

전송하기 전에 명령어를 편집합니다:

```
User: Deploy to prodcution<Backspace><Backspace>uction

[전송하기 전에 현재 위치에서 편집]
```

### Vim 모드

텍스트 편집을 위한 Vi/Vim 키 바인딩을 활성화합니다:

**활성화**:
- `/config` (토글 "Editor / Vim mode") 또는 `~/.claude/settings.json`에서 `editorMode: "vim"`으로 활성화합니다. 독립형 `/vim` 슬래시 명령어는 제거되었습니다 ([issue #43370](https://github.com/anthropics/claude-code/issues/43370) 참조). 이제 vim 모드는 구성 기반입니다.
- `Esc`로 NORMAL, `i/a/o`로 INSERT, `v`로 VISUAL, `V`로 VISUAL-LINE 모드 전환 (v2.1.118+)

**탐색 키**:
- `h` / `l` - 왼쪽/오른쪽으로 이동
- `j` / `k` - 아래/위로 이동
- `w` / `b` / `e` - 단어 단위 이동
- `0` / `$` - 줄 시작/끝으로 이동
- `gg` / `G` - 텍스트 시작/끝으로 이동
- `%` - 짝이 맞는 괄호로 이동; `d`, `c`, `y`와 조합 가능 (v2.1.301)

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

비주얼 선택은 입력 필드에 강조 표시되어 연산자를 실행하기 전에 무엇이 yank되거나, 삭제되거나, 변경될 것인지 정확히 확인할 수 있습니다.

### Bash 모드

`!` 접두사를 사용하여 셸 명령어를 직접 실행합니다:

```bash
! npm test
! git status
! cat src/index.js
```

컨텍스트 전환 없이 빠른 명령어 실행에 사용하십시오.

**v2.1.193부터:** bash 모드 (`!`)는 실시간 파일 경로 자동 완성을 제공하므로 프롬프트를 벗어나지 않고 셸 명령어를 입력하는 동안 경로가 완성됩니다.

**v2.1.186부터:** `!` 명령어의 출력은 이제 Claude에게 자동으로 전송되어 Claude가 응답합니다. 출력이 응답 없이 컨텍스트에만 추가되는 이전 동작을 유지하려면 `settings.json`에서 `"respondToBashCommands": false`를 설정하십시오.

---

## 출력 스타일

출력 스타일은 Claude가 알고 있는 내용이 아니라 **응답하는 방식**을 바꿉니다. 시스템 프롬프트를 수정하여 역할, 어조, 기본 응답 형식을 설정합니다. 매 턴마다 같은 말투를 다시 요청하고 있거나, Claude가 소프트웨어 엔지니어가 아닌 다른 역할을 하기를 원할 때 사용하십시오.

프로젝트나 코드베이스에 대한 지침은 대신 [CLAUDE.md](../02-memory/)를 사용하십시오. 이는 장단점이 다른 별개의 메커니즘입니다.

### 기본 제공 스타일

| 스타일 | 동작 |
|-------|----------|
| **Default** | 소프트웨어 엔지니어링 작업을 효율적으로 완료하도록 조정된 표준 시스템 프롬프트 |
| **Proactive** | Claude가 일상적인 결정을 위해 멈추지 않고 합리적인 가정을 하며 즉시 실행합니다. 자동 모드보다 더 강한 자율 실행 지침이지만 권한 모드는 **바꾸지 않으므로** 권한 프롬프트는 계속 표시됩니다 |
| **Explanatory** | 단계 사이에 교육용 "Insights"를 추가하여 구현 선택과 코드베이스 패턴을 설명합니다 |
| **Learning** | 직접 해 보며 배우는 협업 방식. Claude가 인사이트를 공유하고 *또한* 작고 전략적인 부분을 사용자가 직접 구현하도록 `TODO(human)` 마커를 남깁니다 |
| **Concise** (v2.1.237) | Claude가 결과부터 제시하고 서두와 서술을 생략합니다. 철저함은 그대로이며, 답변을 둘러싼 표현만 빠집니다. `/config` → Output style에서 선택하거나 `"outputStyle": "Concise"`를 설정하십시오 |

### 스타일 선택

`/config`를 실행하고 **Output style**을 선택하거나, `/output-style <style>`을 실행하여 바로 전환합니다. 인수 없이 실행하면 사용 가능한 스타일을 나열하고 현재 스타일을 표시합니다. 어느 방법이든 선택은 `.claude/settings.local.json`에 저장됩니다. 메뉴 없이 설정하려면 설정을 직접 편집합니다:

```json
{
  "outputStyle": "Explanatory"
}
```

> **참고**: 독립형 `/output-style` 명령어는 v2.1.73에서 지원 중단(deprecated)되고 v2.1.91에서 제거되었지만, **v2.1.269에서 다시 도입되었으며** v2.1.278에서 사용할 수 있습니다. 헤드리스 및 원격 제어 세션에서 작동합니다. `/config`와 `outputStyle` 설정도 여전히 작동합니다.

출력 스타일은 Claude Code가 세션 시작 시 한 번 읽는 시스템 프롬프트의 일부이므로, 변경 사항은 `/clear` 후 또는 새 세션에서 적용됩니다.

### 사용자 지정 출력 스타일

사용자 지정 스타일은 프런트매터가 있는 Markdown 파일이며, 세 가지 수준 중 하나에 저장합니다:

- 사용자: `~/.claude/output-styles/`
- 프로젝트: `.claude/output-styles/`
- 관리형 정책: 관리형 설정 디렉터리 내부의 `.claude/output-styles/`

프로젝트 스타일은 작업 디렉터리와 저장소 루트 사이의 모든 `.claude/output-styles/`에서 로드됩니다. v2.1.178부터 중첩된 디렉터리에서 같은 스타일 이름을 정의하면 작업 디렉터리에 가장 가까운 것이 우선합니다.

```markdown
---
name: Diagrams first
description: 모든 설명을 다이어그램으로 시작합니다
keep-coding-instructions: true
---

코드, 아키텍처 또는 데이터 흐름을 설명할 때는 구조를 보여 주는 Mermaid 다이어그램으로
시작한 다음 산문으로 설명합니다.
```

| 프런트매터 | 용도 | 기본값 |
|-------------|---------|---------|
| `name` | 파일 이름과 다를 경우의 스타일 이름 | 파일 이름을 상속 |
| `description` | `/config` 선택기에 표시됨 | 없음 |
| `keep-coding-instructions` | Claude Code의 기본 제공 소프트웨어 엔지니어링 지침 유지 | `false` |
| `force-for-plugin` | 플러그인 스타일 전용: 플러그인이 활성화될 때마다 자동 적용되어 사용자의 `outputStyle`을 재정의 | `false` |

Claude의 소통 방식은 바꾸되 코딩 방식은 그대로 유지하려면 **`keep-coding-instructions: true`를 설정**하십시오. 글쓰기 도우미나 데이터 분석가처럼 Claude가 소프트웨어 엔지니어링을 전혀 하지 않는 경우에는 생략하십시오.

### 범위 및 비용

출력 스타일은 **메인 대화에만** 적용됩니다. 서브에이전트는 자체 시스템 프롬프트로 실행되므로 스타일이 서브에이전트의 응답 방식을 바꾸지 않습니다. 단, 포크는 부모의 전체 시스템 프롬프트를 상속하므로 예외입니다.

지침을 추가하면 입력 토큰이 늘어나지만, 첫 요청 이후에는 프롬프트 캐싱이 대부분을 흡수합니다. Explanatory와 Learning은 설계상 더 긴 응답을 생성하므로 출력 토큰이 늘어납니다.

### 비교

| 기능 | 작동 방식 | 사용 시점 |
|---------|--------------|-------------|
| 출력 스타일 | 시스템 프롬프트를 수정 | 매 턴마다 다른 역할, 어조, 형식을 원할 때 |
| [CLAUDE.md](../02-memory/) | 시스템 프롬프트 뒤에 사용자 메시지를 추가 | Claude가 항상 프로젝트 규칙을 알아야 할 때 |
| `--append-system-prompt` | 아무것도 제거하지 않고 시스템 프롬프트에 덧붙임 | 단일 호출에 대한 일회성 추가 |
| [서브에이전트](../04-subagents/) | 자체 시스템 프롬프트, 모델, 도구로 실행 | 별도 범위의 도우미를 원할 때 |
| [스킬](../03-skills/) | 호출될 때 작업별 지침을 로드 | 재사용 가능한 워크플로가 있을 때 |

---

## 상태 표시줄

상태 표시줄은 출력이 세션 하단에 렌더링되는 사용자 지정 명령어입니다. `/statusline`으로 구성하거나 직접 설정합니다:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "padding": 0
  }
}
```

`padding`의 기본값은 `0`입니다. Claude Code는 stdin으로 명령어에 JSON 객체를 전달하므로, 무엇을 표시할지는 스크립트가 결정합니다.

### 사용 가능한 입력 필드

| 그룹 | 필드 |
|-------|--------|
| 세션 | `session_id`, `session_name`, `prompt_id`, `transcript_path`, `cwd`, `version` |
| 모델 | `model.id`, `output_style.name`, `effort.level`, `fast_mode`, `thinking.enabled` |
| 에이전트 | `agent.name`, `vim.mode` |
| 비용 | `cost.total_cost_usd`, `cost.total_duration_ms`, `cost.total_api_duration_ms`, `cost.total_lines_added` |
| 컨텍스트 | `context_window.context_window_size`, `.current_usage`, `.remaining_percentage`, `.total_input_tokens`, `.used_percentage` |
| 한도 | `rate_limits.five_hour.used_percentage`, `.resets_at` |
| 저장소 | `pr.number`, `pr.review_state`, `workspace.project_dir`, `workspace.added_dirs`, `workspace.git_worktree`, `workspace.repo.host` |
| 워크트리 | `worktree.name`, `.branch`, `.path`, `.original_branch`, `.original_cwd` |

### 예시

```bash
#!/bin/bash
# ~/.claude/statusline.sh — 모델, 컨텍스트 사용량, 비용
input=$(cat)
model=$(echo "$input" | jq -r '.model.id')
used=$(echo "$input" | jq -r '.context_window.used_percentage')
cost=$(echo "$input" | jq -r '.cost.total_cost_usd')
printf '%s | ctx %.0f%% | $%.2f' "$model" "$used" "$cost"
```

> **참고**: `statusLine`은 작업 공간 신뢰가 필요합니다. 상태 표시줄 스크립트는 환경에서 `COLUMNS`와 `LINES`도 받으므로(v2.1.153+) 출력 크기를 터미널에 맞출 수 있습니다.

---

## TUI 모드 (전체 화면)

> **v2.1.110에 새로 추가**

TUI (텍스트 사용자 인터페이스) 모드는 Claude Code를 깜빡임 없는 출력으로 전체 화면으로 렌더링하여 tmux 또는 iTerm2 분할 창과 같은 터미널 멀티플렉서에 이상적입니다.

### TUI 모드 활성화

`/tui` 명령어로 렌더러를 전환하거나, 실행 전에 `CLAUDE_CODE_NO_FLICKER=1`을 설정합니다:

```bash
/tui fullscreen               # 세션 내에서 전체 화면으로 전환
/tui default                  # 기존 렌더러로 되돌리기
CLAUDE_CODE_NO_FLICKER=1 claude  # 전체 화면으로 직접 시작
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

`/focus` 명령어는 포커스 보기를 전환합니다. 이는 가장 관련성 높은 출력만 표시하는 집중 모드입니다. `Ctrl+O`는 이제 일반 트랜스크립트와 자세한 트랜스크립트 간에만 전환됩니다 (포커스 보기는 `/focus`입니다).

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
claude --channels plugin:telegram@claude-plugins-official

# 여러 소스 구독 (공백으로 구분)
claude --channels plugin:discord@claude-plugins-official plugin:telegram@claude-plugins-official
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
  "channelsEnabled": true,
  "allowedChannelPlugins": [
    { "marketplace": "claude-plugins-official", "plugin": "discord" },
    { "marketplace": "claude-plugins-official", "plugin": "telegram" }
  ]
}
```

`allowedChannelPlugins` 관리형 설정은 조직 전체에서 허용되는 채널 플러그인을 제어합니다. 이 설정은 Anthropic이 관리하는 허용 목록을 대체하며 `channelsEnabled: true`가 필요합니다.

### 작동 방식

1. MCP 서버는 외부 서비스에 연결하는 채널 플러그인 역할을 합니다.
2. 들어오는 메시지 및 이벤트는 활성 Claude Code 세션으로 푸시됩니다.
3. Claude는 세션 컨텍스트 내에서 메시지를 읽고 응답할 수 있습니다.
4. 채널 플러그인은 Anthropic이 관리하는 허용 목록에 있거나, 관리자가 설정한 경우 조직의 `allowedChannelPlugins` 목록에 있어야 합니다.
5. 폴링이 필요 없습니다 — 이벤트는 실시간으로 푸시됩니다.

---

## Chrome 통합

Chrome 통합은 Claude Code를 Chrome 또는 Microsoft Edge 브라우저에 연결하여 실시간 웹 자동화 및 디버깅을 지원합니다. 이는 v2.0.73+부터 사용할 수 있는 베타 기능입니다 (Claude in Chrome 확장 프로그램 v1.0.36+ 필요).

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

> **참고**: v2.1.290부터 프로젝트의 설정 파일로는 Chrome 통합을 켤 수 없습니다. `--chrome`, `/chrome` 또는 사용자 설정을 사용하십시오.

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

- **브라우저 지원**: Chrome 및 Edge. Claude Code는 Brave, Arc, Vivaldi, Opera 같은 다른 Chromium 기반 브라우저에서도 연결됩니다
- **WSL**: Windows Subsystem for Linux에서는 사용할 수 없습니다.
- **타사 제공자**: Bedrock, Vertex 또는 Foundry API 제공자와는 지원되지 않습니다.
- **서비스 워커 유휴**: Chrome 확장 프로그램 서비스 워커는 확장된 세션 동안 유휴 상태가 될 수 있습니다.

> **팁**: Chrome 통합은 베타 기능입니다. 브라우저 지원은 향후 릴리스에서 확장될 수 있습니다.

---

## 원격 제어

원격 제어를 사용하면 휴대폰, 태블릿 또는 모든 브라우저에서 로컬로 실행 중인 Claude Code 세션을 계속할 수 있습니다. 로컬 세션은 사용자 컴퓨터에서 계속 실행되며, 아무것도 클라우드로 이동하지 않습니다. Pro, Max, Team 및 Enterprise 플랜에서 사용할 수 있습니다 (v2.1.51+). Enterprise 사용자 지정 역할로 액세스가 관리되는 경우, 클라우드 세션 권한과 **Claude Code remote control** 권한을 모두 가진 역할이 필요합니다.

원격 제어는 **더 이상 연구 미리보기가 아닙니다**. 이 레이블은 2026년 34주차에 제거되었습니다. 이제 `claude remote-control`을 실행 중인 모든 머신은 Claude 앱의 Code 탭에 **기기 카드**로 표시되므로, 먼저 해당 머신에서 세션을 시작한 뒤 연결할 필요 없이 휴대폰에서 바로 그 머신의 세션을 시작할 수 있습니다.

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

> **참고 (v2.1.300)**: `claude remote-control`은 더 이상 `--sandbox`나 `--no-sandbox`를 허용하지 않습니다(원래 아무 효과가 없었으며, 이제 둘 중 하나를 전달하면 오류와 함께 종료됩니다). 원격 제어 세션을 샌드박싱하려면 설정 파일에서 `sandbox.enabled`를 설정하십시오.

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

- 대화형 Claude Code 프로세스당 하나의 원격 세션 — 서버 모드(`claude remote-control`)는 여러 세션을 동시에 제공합니다(`--capacity`, 기본값 32)
- 호스트 컴퓨터에서 터미널이 열려 있어야 합니다
- 네트워크에 연결할 수 없으면 서버 모드는 약 10분 후 종료되며, 대화형 세션은 계속 재시도하다가 네트워크가 복구되면 다시 연결됩니다

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

### 원격 제어 비활성화 (`disableRemoteControl`, v2.1.128+)

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
claude --cloud "implement the new API endpoints"   # --remote는 지원 중단된 별칭
```

이렇게 하면 claude.ai에서 Claude Code 세션이 시작되며, 모든 브라우저에서 액세스할 수 있습니다.

### 로컬에서 웹 세션 다시 시작

웹에서 세션을 시작하고 로컬에서 계속하려면:

```bash
# 로컬 터미널에서 웹 세션 다시 시작 — 웹 세션 선택기가 열림
claude --teleport
```

또는 대화형 REPL 내에서:

```text
/teleport
```

`/tp`는 `/teleport`의 별칭입니다. 둘 다 claude.ai 구독이 필요합니다. 클라우드 세션에는 로컬에서 계속하는 방법을 설명하는 `/teleport` 힌트가 표시됩니다 (v2.1.223).

> **변경 로그 기반**: v2.1.223 변경 로그에는 알려진 세션으로 바로 이동하는 인수 형식
> `claude --teleport <session id>`가 나와 있습니다. CLI 참조 문서는 인수 없는 선택기 형식만
> 설명하므로, 이미 세션 ID가 있는 경우가 아니면 `claude --teleport`를 사용하십시오.

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
| **PR 모니터링** | **Auto-fix**는 Claude가 실패한 CI 검사와 리뷰 댓글을 수정하게 하고, **Merge when ready**는 GitHub 자동 병합을 켭니다(기본 브랜치가 병합 큐를 사용하지 않으면 로컬 세션에서는 squash). 둘 다 세션의 **Changes** 카드에 있는 풀 리퀘스트의 **⋮** 메뉴에 있습니다 |
| **병렬 세션** | 자동 Git 워크트리 격리를 통해 사이드바에 여러 세션 표시 |
| **예약된 작업** | 앱이 열려 있는 동안 실행되는 반복 작업 (시간별, 일별, 주중, 주별) |
| **풍부한 렌더링** | 구문 강조 표시가 있는 코드, 마크다운 및 다이어그램 렌더링; GitHub-Flavored-Markdown 작업 목록 확인란 (`- [ ]` / `- [x]`)은 확인란으로 렌더링됩니다 (v2.1.149+) |

### 앱 미리보기 구성

`.claude/launch.json`에서 개발 서버 동작을 구성합니다:

```json
{
  "version": "0.0.1",
  "configurations": [
    {
      "name": "my-app",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "dev"],
      "port": 3000
    }
  ]
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

데스크톱 앱은 CLI와 동일한 권한 모드를 지원합니다:

| 모드 | 동작 |
|------|----------|
| **Manual** (기본값) | 모든 편집 및 명령어 검토 및 승인 |
| **Accept edits** | 파일 편집은 자동 승인; 명령어는 수동 승인 필요 |
| **Plan** | 변경 사항을 적용하기 전에 접근 방식 검토 |
| **Auto** | 일상적인 프롬프트 없이 실행; 백그라운드 분류기가 먼저 작업을 검사 |
| **Bypass permissions** | 자동 실행 (샌드박스 전용, 관리자 제어) |

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

### 명명된 작업 디렉터리

`CLAUDE_CODE_TASK_LIST_ID` 환경 변수를 사용하여 세션 간에 공유되는 명명된 작업 디렉터리를 생성합니다:

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

이를 통해 여러 세션이 동일한 작업 목록을 공유할 수 있으므로 팀 워크플로 또는 다중 세션 프로젝트에 유용합니다.

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

대화형 워크트리 세션을 종료할 때 워크트리에 변경 사항이 없으면 Claude가 워크트리와 해당 브랜치를 자동으로 제거합니다(이름이 지정된 세션은 먼저 묻습니다). 변경 사항이나 새 커밋이 있거나, 새 커밋이 있는 다른 브랜치가 체크아웃되어 있으면(v2.1.304부터) Claude가 유지할지 제거할지 묻습니다. 비대화형 `-p` 실행은 워크트리를 그대로 남겨 둡니다.

### 사용 사례

- 메인 브랜치를 건드리지 않고 기능 브랜치에서 작업
- 작업 디렉터리에 영향을 미치지 않고 격리된 환경에서 테스트 실행
- 일회용 환경에서 실험적인 변경 시도
- 더 빠른 시작을 위해 모노레포에서 특정 패키지 스파스 체크아웃

---

## 샌드박싱

샌드박싱은 Claude Code가 실행하는 Bash 명령어에 OS 수준의 파일 시스템 및 네트워크 격리를 제공합니다. 이는 권한 규칙을 보완하며 추가 보안 계층을 제공합니다.

### 샌드박싱 활성화

**슬래시 명령어** (이 프로젝트의 `.claude/settings.local.json`에 선택 사항 저장):
```text
/sandbox
```

**설정 파일** (모든 프로젝트): `~/.claude/settings.json`에 `"sandbox": { "enabled": true }`를 설정합니다.

**세션별**로, 설정 파일을 작성하지 않고:
```bash
claude --settings '{"sandbox": {"enabled": true}}'
```

> `claude --sandbox` / `--no-sandbox` 플래그는 없습니다. v2.1.300부터 `claude remote-control`에 이 플래그를 전달하면 오류와 함께 종료됩니다.

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
| `sandbox.network.strictAllowlist` | (v2.1.219) 샌드박스 명령어에 대해 허용 목록에 없는 호스트를 프롬프트 없이 거부 |
| `sandbox.enableWeakerNetworkIsolation` | macOS에서 약한 네트워크 격리 활성화 |
| `sandbox.bwrapPath` | (v2.1.133+, Linux/WSL) `bubblewrap` 바이너리 경로. 기본값: `$PATH` 조회. |
| `sandbox.socatPath` | (v2.1.133+, Linux/WSL) `socat` 바이너리 경로. 기본값: `$PATH` 조회. |
| `sandbox.credentials` | (v2.1.187+) 샌드박스 명령어가 자격 증명 파일 및 비밀 환경 변수를 읽는 것을 차단합니다. |
| `sandbox.allowAppleEvents` | (v2.1.181+, macOS) 샌드박스 명령어가 Apple Event를 보내도록 옵트인합니다. |
| `sandbox.filesystem.disabled` | (v2.1.216+) 네트워크 격리는 유지하면서 파일 시스템 격리를 완전히 건너뜁니다. 파일 샌드박싱이 도구를 망가뜨리지만 네트워크 이그레스 제어는 계속 활성화해야 할 때 유용합니다. 사용자 설정, 관리형 설정 또는 `--settings`에서만 적용되며, 프로젝트 설정으로는 설정할 수 없습니다. |
| `sandbox.excludedCommands` | `"docker compose *"`처럼 `Bash(...)` 규칙 구문으로 쓴 명령어 패턴으로, 샌드박스 밖에서 실행되며 일반 권한 흐름을 거칩니다. v2.1.309부터 샌드박스가 활성화되어 있지만 실행할 수 없는 동안에는 샌드박스 쓰기 목록 경로에 쓰기 전에 묻습니다 |
| `sandbox.allowNestedUserNamespaces` | (v2.1.305+, Linux/WSL2) 샌드박스 명령어가 사용자 네임스페이스(Chromium/Electron 샌드박스, 중첩 bubblewrap, `unshare`)를 만들 수 있게 합니다. 이는 보안 경계를 끄는 것이며, 사용자 또는 관리형 설정이나 `--settings`에서만 적용됩니다. rootless Podman에는 대신 `excludedCommands`를 사용하십시오 |

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

> **참고** (v2.1.243): 샌드박스 Bash 도구의 권한 프롬프트는 **더 이상 허용된 네트워크 호스트를 나열하지 않습니다**. Claude는 그냥 요청을 시도하고, 새 호스트가 나타날 때마다 사용자가 승인합니다. 따라서 프롬프트가 허용 목록을 미리 보여 줄 것이라고 기대하지 마십시오. 같은 릴리스에서 차단된 명령어가 `0`으로 종료되는 경우에도 네트워크 위반 세부 정보가 더 이상 누락되지 않으므로, 조용해 보이는 성공도 무엇이 차단되었는지 보고합니다.

### 자격 증명 마스킹 (v2.1.221, v2.1.224)

> **변경 로그 기반**: 이 `sandbox.credentials` 옵션은 v2.1.221 및 v2.1.224 변경 로그 항목에서
> 가져온 것이며, 설정 참조 문서에는 아직 자세히 나와 있지 않습니다.

v2.1.221 이전에는 `sandbox.credentials`가 자격 증명 파일을 `deny`할 수만 있었으므로, 자격 증명이
필요한 샌드박스 명령어는 그냥 실패했습니다. `mode: "mask"`를 사용하면 비밀을 노출하지 않고도
명령어가 계속 작동합니다. 샌드박스 프로세스는 파일의 **센티널** 사본을 읽고, 샌드박스 프록시가
네트워크로 나가는 길에 실제 값으로 바꿉니다.

```json
{
  "sandbox": {
    "network": { "tlsTerminate": true },
    "credentials": {
      "files": [
        { "path": "~/.aws/credentials", "mode": "mask" }
      ]
    }
  }
}
```

| 기능 | 도입 버전 | 동작 |
|---|---|---|
| 자격 증명 **파일**용 `mode: "mask"` | v2.1.221 | 샌드박스 명령어는 센티널을 읽고, 프록시가 이그레스 시 실제 값으로 교체합니다. **Linux 및 WSL 전용** — macOS에서는 파일 마스킹이 `deny`로 대체됩니다. |
| `extract` / `onExtractNoMatch` | v2.1.224 | 변수 전체가 아니라 구조화된 환경 값 안의 한 필드만 마스킹하고, 패턴이 일치하지 않을 때의 동작을 결정합니다. |
| `maskClaims`와 함께 `decode: "jwt"` | v2.1.224 | JWT를 디코딩하여 지정된 클레임만 마스킹하고 나머지는 읽을 수 있게 둡니다. |
| `awsPairs` / `sigv4` | v2.1.224 | 실제 액세스 키로 치환한 뒤 프록시에서 AWS SigV4 요청을 다시 서명합니다. |

**놓치기 쉬운 두 가지 제약:**

- 모든 마스킹에는 `network.tlsTerminate`가 필요합니다. 프록시가 값을 치환하려면 요청 내부를
  볼 수 있어야 합니다.
- 이 옵션은 사용자 설정, 관리형 설정 또는 `--settings`에서**만** 적용됩니다.
  프로젝트 설정으로는 마스킹을 켜거나 마스킹 대상을 바꿀 수 없습니다.

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
    }
  }
}
```

### 작동 방식

- Bash 명령어는 제한된 파일 시스템 액세스를 가진 샌드박스 환경에서 실행됩니다.
- 의도치 않은 외부 연결을 방지하기 위해 네트워크 액세스를 격리할 수 있습니다.
- 심층 방어를 위해 권한 규칙과 함께 작동합니다.
- macOS에서는 Seatbelt가 샌드박스 프록시로 가는 연결을 제외한 모든 네트워크 연결을 차단합니다. `sandbox.enableWeakerNetworkIsolation`은 이 격리를 **약화**하며, MITM `httpProxyPort` 프록시 뒤의 Go CLI 같은 도구에만 사용합니다

### 사용 사례

- 신뢰할 수 없거나 생성된 코드를 안전하게 실행
- 프로젝트 외부 파일에 대한 우발적인 수정 방지
- 자동화된 작업 중 네트워크 액세스 제한

---

## 관리형 설정 (엔터프라이즈)

관리형 설정은 엔터프라이즈 관리자가 플랫폼 고유의 관리 도구를 사용하여 조직 전체에 Claude Code 구성을 배포할 수 있도록 합니다.

### 배포 방법

| 플랫폼 | 방법 | 도입 버전 |
|----------|--------|-------|
| macOS | 관리형 plist 파일 (MDM) | v2.1.51+ |
| Windows | Windows 레지스트리 | v2.1.51+ |
| 크로스 플랫폼 | 관리형 구성 파일 | v2.1.51+ |
| 크로스 플랫폼 | 관리형 드롭인 (`managed-settings.d/` 디렉터리) | v2.1.83+ |

### 관리형 드롭인

v2.1.83부터 관리자는 `managed-settings.d/` 디렉터리에 여러 관리형 설정 파일을 배포할 수 있습니다. 파일은 알파벳순으로 병합되어 팀 간에 모듈형 구성을 가능하게 합니다. 이 디렉터리는 시스템 디렉터리(macOS는 `/Library/Application Support/ClaudeCode/`, Linux는 `/etc/claude-code/`, Windows는 `C:\Program Files\ClaudeCode\`)의 `managed-settings.json` 옆에 위치합니다:

```
/etc/claude-code/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### 사용 가능한 관리형 설정

| 설정 | 설명 |
|---------|-------------|
| `permissions.disableBypassPermissionsMode` | `"disable"`로 설정하면 사용자가 권한 우회 모드를 활성화하지 못하도록 방지 |
| `availableModels` | 사용자가 선택할 수 있는 모델 제한 |
| `enforceAvailableModels` | (v2.1.175) `true`인 경우, `availableModels` 허용 목록은 **기본** 모델*도* 제한합니다. 구성된 기본값이 목록에 없으면 Claude Code는 허용된 첫 번째 모델로 대체됩니다. 사용자 및 프로젝트 설정은 더 이상 관리되는 `availableModels` 목록을 확장할 수 없습니다. |
| `allowedChannelPlugins` | 허용되는 채널 플러그인 제어 |
| `autoMode.environment` | 자동 모드에 대한 신뢰할 수 있는 인프라 구성 |
| `workflowSizeGuideline` | (v2.1.219) 권고용 [동적 워크플로 크기 지침](#동적-워크플로)을 설정합니다. 관리형 설정뿐 아니라 모든 설정 파일에서 읽을 수 있으며, 설정 파일에서 이를 지정하면 `/config`에서 **Dynamic workflow size** 행이 숨겨집니다 |
| `wslInheritsWindowsSettings` | Windows/WSL 전용 (v2.1.118+): `true`인 경우, WSL 내에서 실행되는 Claude Code는 Windows 호스트의 관리형 설정을 상속하므로 레지스트리/MDM을 통해 배포된 엔터프라이즈 정책이 Windows 및 WSL 셸 전체에 균일하게 적용됩니다 |
| `parentSettingsBehavior` | (v2.1.133+, 관리자 계층) SDK의 `managedSettings`가 부모 프로세스 설정과 병합되는 방식을 제어합니다. `"first-wins"`는 기존 우선순위를 유지하고 (충돌 시 먼저 설정된 것이 우선), `"merge"`는 값을 깊이 병합합니다. |
| 사용자 지정 정책 | 조직별 권한 및 도구 정책 |

### 예시: macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>permissions</key>
  <dict>
    <key>disableBypassPermissionsMode</key>
    <string>disable</string>
  </dict>
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

1. **사용자 설정**: `~/.claude/settings.json`
2. **프로젝트 설정**: `.claude/settings.json` (저장소에 커밋)
3. **로컬 프로젝트 설정**: `.claude/settings.local.json` (커밋하지 않음)
4. **관리형 설정**: 시스템 디렉터리의 `managed-settings.json` ([관리형 설정](#관리형-설정-엔터프라이즈) 참조)

### 전체 구성 예시

**핵심 고급 기능 구성** (`.claude/settings.json`):

```json
{
  "permissions": {
    "defaultMode": "manual"
  },
  "hooks": {
    "PreToolUse": [
      { "matcher": "Edit", "hooks": [{ "type": "command", "command": "~/.claude/hooks/eslint-fix.sh" }] }
    ],
    "PostToolUse": [
      { "matcher": "Write", "hooks": [{ "type": "command", "command": "~/.claude/hooks/security-scan.sh" }] }
    ]
  }
}
```

훅 스크립트는 stdin으로 도구 입력을 JSON으로 받습니다(예: `tool_input.file_path`). `${file_path}` 치환은 없습니다. MCP 서버는 설정 키가 아니므로 프로젝트 루트의 `.mcp.json`에 정의합니다:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": { "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}" }
    }
  }
}
```

**확장 구성 예시:**

```json
{
  "permissions": {
    "defaultMode": "manual",
    "allow": ["Bash(git log:*)", "Read"],
    "deny": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": [{ "type": "command", "command": "~/.claude/hooks/eslint-fix.sh" }] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": [{ "type": "command", "command": "~/.claude/hooks/security-scan.sh" }] }],
    "Stop": [{ "hooks": [{ "type": "command", "command": "~/.claude/hooks/notify.sh" }] }]
  }
}
```

이 구성의 GitHub MCP 서버는 위에서 보인 것처럼 `.mcp.json`에 넣습니다.

### 추가 사용자별 설정

이 키들은 `~/.claude/settings.json`(또는 프로젝트의 `.claude/settings.json`)에 넣으며, 개별 사용자의 대화형 동작을 제어합니다:

| 설정 | 설명 |
|---------|-------------|
| `askUserQuestionTimeout` | 응답하지 않은 `AskUserQuestion` 대화 상자를 유휴 시간 후 자동으로 계속합니다. **v2.1.200**부터 대화 상자는 기본적으로 자동 계속되지 않으므로, 시간 제한 자동 계속을 다시 사용하려면 이 값을 설정하십시오. |
| `enableArtifact` | 사용자별 Artifact 도구 활성화/비활성화 (v2.1.196). |
| `crossSessionInbound` | (v2.1.224) 수신 [세션 간 메시지](#세션-간-메시징)의 처리 방식 — `"accept"`, `"hold"`, `"refuse"`. 프로젝트 및 로컬 값은 `accept < hold < refuse` 단계에서 *더 엄격*할 때만 적용됩니다. v2.1.232부터 `/config`에 "Messages from your other sessions"로 표시됩니다. |
| `dialogExpiry` | (v2.1.224) 응답하지 않은 대화 상자가 열려 있는 시간. 기본값 `"5m"`; `"60s"`, `"5m"`, `"10m"`, `"never"`를 허용합니다. `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS`가 재정의합니다. v2.1.232부터 `/config`에 "Dialog expiry"로 표시됩니다. |
| `modelPicker` | (v2.1.243) `/model` 선택기에 나열할 모델을 원하는 순서와 레이블로 선택합니다. 설정 계층 간에 **병합되지 않고 대체되는** 몇 안 되는 설정 중 하나로, 가장 가까운 범위의 값이 그대로 우선합니다. |
| `promptCacheTtl` | (v2.1.243) 메인 대화의 프롬프트 캐시 수명을 선택합니다. |
| `subagentPromptCacheTtl` | (v2.1.243) 서브에이전트 및 메인 대화 외부의 기타 요청에 대한 같은 선택입니다. |
| `modelPricing` | (v2.1.243) **관리형 설정.** 조직의 계약 요율을 제공하여 `/cost`, 상태 표시줄, 텔레메트리가 정가 대신 해당 요율로 보고하게 합니다. |
| `keybindingFlavor` | **v2.1.261부터 지원 중단되었으며 효과가 없습니다.** 프롬프트의 단어 편집 키는 Bash처럼 항상 readline 규칙을 따릅니다. `Ctrl+W`는 공백까지 뒤로 삭제하고, `Alt+F`와 `Alt+D`는 단어 끝에서 멈추며, 구두점은 단어를 구분합니다. Claude Code는 여전히 이 키를 허용하므로 이를 설정한 설정 파일도 유효합니다. (v2.1.238–v2.1.260에서는 `"classic"`과 `"readline"` 중에서 선택했습니다.) |
| `spellcheck` | (v2.1.235) `PATH`에 있는 `aspell`, `hunspell`, `ispell` 중 하나(이 순서로 시도)를 사용하여 프롬프트 입력의 철자가 틀린 단어에 밑줄을 표시합니다. 객체 값(`{"enabled": true, "language": "en_GB"}`)이며 기본적으로 꺼져 있습니다. **사용자 설정, `--settings` 플래그, 관리형 설정에서만 읽습니다**. 프로젝트의 `.claude/settings.json`이나 `.claude/settings.local.json`에 있는 `spellcheck` 블록은 무시됩니다. |
| `bashOutputMaxChars` | (v2.1.261) **성공한** Bash 또는 PowerShell 명령어 출력 중 Claude가 인라인으로 받는 문자 수(최대 128K). 한도를 넘으면 Claude Code가 출력을 파일에 저장하고 Claude는 짧은 미리보기와 경로를 받습니다. 이를 설정하면 Claude Code는 `BASH_MAX_OUTPUT_LENGTH`를 무시합니다. |
| `taskOutputMaxChars` | (v2.1.261) **v2.1.278에서 대체되었으며 효과가 없습니다.** 이전에는 `TaskOutput` 도구로 **백그라운드 작업** 출력을 읽을 때 Claude가 인라인으로 받는 문자 수를 제한했습니다. v2.1.278에서 `TaskOutput` 도구가 제거되어 이제 Claude는 백그라운드 작업의 출력 파일을 `Read`로 읽으므로, 이 키와 `TASK_MAX_OUTPUT_LENGTH`는 모두 효과가 없습니다. Claude Code는 여전히 이 키를 허용하므로 이를 설정한 설정 파일도 유효합니다. |
| `maxEffortLevel` | (v2.1.267) Bedrock, Vertex, Foundry를 포함한 모든 제공자에서 Claude Code가 사용할 수 있는 노력 수준의 상한을 정합니다. 최상위 또는 `modelSettings` 아래 모델별로 설정합니다. 사용자는 여전히 더 낮은 수준을 선택할 수 있습니다. |
| `bashEditDiffEnabled` | (v2.1.269) Bash 도구 결과에 명령어가 변경한 파일의 diff를 포함합니다. |
| `syncClaudeAiSkills` / `syncClaudeAiPlugins` | (v2.1.275) 둘 중 하나를 `false`로 설정하면 claude.ai 계정에서 활성화한 스킬이나 플러그인을 터미널 세션으로 동기화하지 않습니다. |

### 대체 모델 (`fallbackModel`)

`fallbackModel` 설정을 사용하면 기본 모델이 과부하되거나 사용할 수 없을 때 순서대로 시도되는 **최대 3개의** 대체 모델을 구성할 수 있습니다.

```json
{
  "fallbackModel": ["claude-opus-4-8", "claude-sonnet-4-6", "claude-haiku-4-5"]
}
```

**v2.1.166부터** `--fallback-model` 플래그는 대화형 세션에도 적용됩니다 (헤드리스뿐만 아니라). 대체 시 Claude Code는 예기치 않은 재시도 불가능한 오류를 한 번 재시도합니다. 인증, 속도 제한, 요청 크기 및 전송 오류는 여전히 즉시 실패합니다.

### 환경 변수

환경 변수로 구성을 재정의합니다:

```bash
# 모델 선택
export ANTHROPIC_MODEL=claude-opus-4-8
export ANTHROPIC_DEFAULT_MODEL=claude-opus-4-8   # (v2.1.236) 새 세션이 시작할 모델. ANTHROPIC_MODEL과 달리 /model 선택이 여전히 이를 재정의하며, 그 선택은 재시작 후에도 유지됨
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-8
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# API 구성
export ANTHROPIC_API_KEY=sk-ant-...

# 사고 구성
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high   # low, medium, high, xhigh (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7), or max — default is high on Opus 5 and Opus 4.8 (supported on Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6)

# 기능 토글
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1    # 자동 메모리 비활성화 (자동 메모리 파일을 만들거나 로드하지 않음)
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=0          # 작업 도구가 기본값이며, 0이면 레거시 TodoWrite 도구로 되돌림
export CLAUDE_CODE_SIMPLE=true              # --bare 플래그가 설정함

# MCP 구성
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# 프롬프트 캐싱
export ENABLE_PROMPT_CACHING_1H=1      # 모든 요청에 1시간 캐시 TTL 요청 (기본값: 구독의 메인 대화는 1시간, API 키 / 클라우드 제공자는 5분)

# 작업 관리
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# 에이전트 팀 (실험적)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# 서브에이전트 및 플러그인 구성
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=1

# 하위 프로세스 및 스트리밍
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000

# 출력 및 패키지 관리자 (v2.1.129+)
export CLAUDE_CODE_FORCE_SYNC_OUTPUT=1                      # 자동 감지가 실패하는 터미널(Emacs eat 등)에서 동기식 출력 강제
export CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1            # Homebrew/WinGet 설치의 백그라운드 업그레이드 활성화
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1         # ANTHROPIC_BASE_URL이 설정된 경우 /v1/models 게이트웨이 검색 옵트인

# Windows PowerShell 도구 (v2.1.143+) — Windows의 Bedrock/Vertex/Foundry에서 기본 활성화
export CLAUDE_CODE_USE_POWERSHELL_TOOL=0                    # PowerShell 도구 완전 비활성화
export CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1    # `-ExecutionPolicy Bypass` 대신 시스템 ExecutionPolicy 준수

# 워크로드 ID 페더레이션 (v2.1.141+)
export ANTHROPIC_WORKSPACE_ID=ws_abc123                     # 규칙이 여러 작업 공간을 포함할 때 페더레이션 토큰을 특정 작업 공간으로 한정

# Stop 훅 안전 상한 (v2.1.143+)
export CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=8                    # 세션이 경고와 함께 종료되기 전 허용되는 연속 Stop 훅 차단 최대 횟수. 0이면 상한 비활성화.

# 세션 전체 생성 상한 (v2.1.212)
export CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION=200         # 폭주하는 검색 루프를 막기 위한 세션당 WebSearch 도구 호출 상한. 기본값 200.
export CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR=100       # (v2.1.290) 해당 예산의 시간당 충전 횟수. 대화형은 기본값 100, -p에서는 0(충전 없음).

# 접근성 (v2.1.208)
export CLAUDE_AX_SCREEN_READER=1                            # 일반 텍스트 화면 낭독기 렌더링 모드 활성화. --ax-screen-reader 또는 사용자/관리형 설정의 "axScreenReader": true와 같은 효과 (v2.1.305부터 프로젝트/로컬 설정에서는 무시됨).

# 새 변수 (v2.1.221–v2.1.234) — 변경 로그 기반; CLI 참조 문서에는 환경 변수 섹션이 없음
export CLAUDE_CODE_ENABLE_TODO_TOOLS=1                      # (v2.1.233) 할 일/작업 추적 도구(TaskCreate/Get/Update/List, TodoWrite) 복원. 이 도구는 Claude 3.x 모델, Opus 4~4.7, Sonnet 4~4.6, Haiku 4.5에서만 기본 제공됨 (v2.1.268)
export CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS=900000             # (v2.1.233) WebFetch URL 캐시 TTL. 기본값 15분.
export CLAUDE_CODE_TOOL_MEMORY_LIMIT=2G                     # (v2.1.233, Linux) Bash 명령어에 적용되는 옵트인 메모리 cgroup
export ANTHROPIC_BEDROCK_REGION_PREFIX=us                   # (v2.1.224) 특정 Bedrock 교차 리전 추론 프로필 우선 사용
export CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT=1  # (v2.1.223) 인식되지 않는 모델 ID에 대해 v2.1.223 이전 자동 압축 동작 복원
export CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS=0             # (v2.1.229) 동적 워크플로 팬아웃의 프리픽스 시차 적용 비활성화
export CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS=300000            # (v2.1.224) dialogExpiry 설정 재정의
export CLAUDE_CODE_PROJECT_DIR_NAME=my-app                  # (v2.1.234) 세션마다 별도 구성 디렉터리를 주는 호스트용, 프로젝트별 트랜스크립트 디렉터리의 짧은 이름
export CLAUDE_CODE_GOAL_CHECKIN_MINUTES=30                  # (v2.1.234) /goal이 활성인 동안 Claude가 확인하기 전 백그라운드 작업이 멈춰 있을 수 있는 시간(분). 0이면 확인 비활성화.

# 새 변수 (v2.1.268-v2.1.278) - 변경 로그 기반
export CLAUDE_CODE_MCP_STARTUP_WAIT_MS=5000                 # (v2.1.274) 첫 비대화형 턴이 아직 연결 중인 MCP 서버를 기다리는 시간. 0 = 기다리지 않음. 단 --allowedTools나 mcp_tool 훅이 지정한 서버는 예외(여전히 최대 2초, v2.1.284+).
export CLAUDE_CODE_WEBFETCH_DEADLINE_MS=300000              # (v2.1.268) WebFetch의 새 300초 기한 재정의. 0이면 기한 비활성화.
export CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS=32        # (v2.1.269) Workflow 도구의 실행당 동시 에이전트 한도 상향. 1-256 허용.
export CLAUDE_CODE_AUTO_MODE_SERVER=0                       # (v2.1.278; v2.1.281부터 직접 Anthropic API) 서버 측 자동 모드 분류기 검토 옵트아웃

# 새 변수 (v2.1.299-v2.1.300)
export CLAUDE_CODE_DISABLE_FILE_MENTIONS=1                  # (v2.1.299) @ 파일/디렉터리 멘션을 확장하지 않음; Claude는 경로를 받아 파일 도구로 읽음. 프로젝트/로컬 설정에서는 무시됨.
export CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS=200000           # (v2.1.299, v2.1.290+ 필요) 유휴 압축이 적용되는 컨텍스트 크기. 기본값 200000, 최소 100000. "idleCompaction": false로 끔.
export CLAUDE_CODE_GZIP_REQUEST_BODIES=0                    # (v2.1.300) api.anthropic.com으로 가는 대용량 요청 본문의 gzip 끄기 (TLS 검사 프록시가 이를 잘못 처리하는 경우 사용).
export CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS=0                 # (v2.1.300) 게시 중 편집 대신, 파일 도구로 아티팩트 파일을 편집한 뒤 별도 단계로 게시.

# 새 변수 (v2.1.301-v2.1.302)
export CLAUDE_CODE_AUTO_MODE_MODEL=claude-sonnet-4-6  # 클라이언트 측 자동 모드 분류기 모델 (v2.1.302); Opus 5, Sonnet 5.5, Opus 5.5 또는 정책에서 제외한 모델에는 무시됨
export CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS=3600000  # 먼 사용 한도 재설정을 기다리지 않고 중지 (v2.1.301)

# 새 변수 (v2.1.304-v2.1.310) — 실행하는 셸에서 설정
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=200k                 # (v2.1.304) 자동 압축 창, 100000-1000000 토큰; k/M 접미사는 v2.1.304+ 필요, 숫자만 쓰면 토큰으로 해석
export CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT=1        # (v2.1.304) /Volumes/USB나 /mnt/c 같은 마운트된 드라이브에 대한 재귀 rm 프롬프트 끄기; 설정 env 블록에서는 무시됨
export CLAUDE_CODE_WARN_DISK_FREE_GIB=10                    # (v2.1.304) 작업 디렉터리 파일 시스템의 여유 공간이 N GiB 미만이 되면 Claude에 경고
export CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND=1            # (v2.1.304) 대화형 세션에서 Claude가 MCP 작업의 결과를 기다리게 함
export CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS=600000  # (v2.1.305) CLAUDE_CODE_RETRY_WATCHDOG과 함께, 이 주기(60000-10800000 ms)로 사용 한도를 재확인하여 한도가 풀리면 일찍 재개
export CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK=1        # (v2.1.309) 물어볼 수 없는 신뢰되지 않은 폴더(CI)에서 `claude ultrareview` 실행 허용; 체크아웃을 신뢰하는 경우에만 사용
```

> **v2.1.223 — `CLAUDE_CODE_DISABLE_1M_CONTEXT` 범위 확대**: 이 변수는 이제 고정된 모델 ID 목록만이
> 아니라 네이티브 1M 토큰 창을 가진 **모든** Claude 모델을 자동 압축을 통해 200K로 제한합니다.

> **v2.1.108**: `ENABLE_PROMPT_CACHING_1H=1` — 메인 대화와 기타 요청에 1시간 프롬프트 캐시 TTL을 요청합니다. 이 변수가 없으면 메인 대화는 플랜 사용량 내의 Claude 구독에서는 1시간, API 키, 사용 크레딧 또는 클라우드 제공자에서는 5분을 받습니다. `FORCE_PROMPT_CACHING_5M=1`은 5분을 강제합니다. (v2.1.129는 1시간 TTL이 조용히 5분으로 다운그레이드되던 회귀 버그를 수정합니다.)

> **v2.1.129**: `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1`은 기능 자동 감지가 실패하는 터미널 (예: Emacs `eat`)에 대해 동기식 출력을 강제합니다. `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1`은 Homebrew/WinGet 설치에 대한 백그라운드 업그레이드를 활성화하며, 그렇지 않으면 자동 업데이트되지 않습니다.

### 구성 관리 명령어

```
User: /config
[대화형 구성 메뉴 열기]
```

`/config` 명령어는 다음과 같은 설정을 전환하는 대화형 메뉴를 제공합니다:
- 확장 사고 켜기/끄기
- 자세한 출력
- 권한 모드
- 모델 선택
- 동적 워크플로 크기 (v2.1.219) — 설정 파일에 `workflowSizeGuideline`이 설정되어 있으면 숨겨집니다. [동적 워크플로](#동적-워크플로) 참조
- 유휴 압축 (v2.1.302)

대화형 메뉴에서 Enter 또는 Space를 눌러 선택한 설정을 변경하고, Esc를 눌러 저장하고 닫습니다 (v2.1.183+).

메뉴를 열지 않고도 프롬프트에서 직접 설정을 지정할 수도 있습니다:

```bash
/config thinking=false      # 단일 설정 인라인으로 지정 (v2.1.181+)
/config --help              # 사용 가능한 약식 키 목록 (v2.1.183+)
```

`key=value` 약식은 대화형 세션, `-p` 사용 시, 그리고 원격 제어에서 작동합니다.

### 프로젝트별 구성

프로젝트에 `.claude/settings.json`을 생성합니다:

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": [{ "type": "command", "command": "npm test && npm run lint" }] }]
  },
  "permissions": {
    "defaultMode": "manual"
  }
}
```

프로젝트의 MCP 서버는 프로젝트 루트의 `.mcp.json`에 넣습니다:

```json
{
  "mcpServers": {
    "project-db": {
      "command": "mcp-postgres",
      "env": {
        "DATABASE_URL": "${PROJECT_DB_URL}"
      }
    }
  }
}
```

`PROJECT_DB_URL`에는 읽기 전용 데이터베이스 사용자를 사용하십시오. 읽기 전용 설정은 [MCP → 데이터베이스 예시](../05-mcp/README.md)를 참조하십시오.

---

## 신뢰 및 권한 범위 지정

> **변경 로그 기반 (v2.1.222, v2.1.232)**: 이러한 강화 내용은 변경 로그에서 가져온 것이며,
> 설정 참조 문서에는 아직 자세히 나와 있지 않습니다.

최근 릴리스에서 반복되는 주제는 보안 관련 설정을 복제한 저장소가 더 이상 넓힐 수 없다는 것입니다. 알아 두어야 할 변경 사항은 세 가지입니다.

**중첩된 저장소는 자체 신뢰 확인이 필요합니다 (v2.1.232).** 신뢰된 상위 디렉터리 안에 있는 Git 저장소는 더 이상 그 신뢰를 상속하지 않습니다. `~/work/monorepo`를 신뢰하고 그 안에 벤더링된 서브모듈이 있다면, Claude Code가 처음 그 서브모듈 안에서 작업할 때 서브모듈을 별도로 신뢰할지 묻습니다.

**`sandbox.ripgrep`은 사용자 범위 전용입니다 (v2.1.232).** 샌드박스가 사용하는 ripgrep 바이너리를 지정하는 이 설정은 사용자 설정, 관리형 설정 또는 `--settings`에서만 적용됩니다. 프로젝트 설정으로는 더 이상 샌드박스가 다른 바이너리를 가리키게 할 수 없습니다.

**원격 제어 자동 시작은 사용자 범위 전용입니다 (v2.1.222).** 저장소 로컬 설정으로는 원격 제어 자동 시작을 활성화할 수 없으며, 사용자 범위에서 `/config`를 통해서만 켤 수 있습니다.

기억해야 할 패턴: 어떤 설정이 커밋된 파일로 Claude Code가 사용자 머신에서 할 수 있는 일을 확장하게 한다면, 이제 그 설정은 사용자 범위 전용이라고 가정하십시오.

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
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
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

- 다른 팀원이 다른 모듈을 처리하는 대규모 리팩터링 작업
- 병렬 코드 검토 및 구현
- 코드베이스 전체에 걸친 조정된 다중 파일 변경

> **참고**: 에이전트 팀은 실험적인 기능이며 향후 릴리스에서 변경될 수 있습니다. 전체 참조는 [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams)를 참조하십시오.

---

## 모범 사례

### 계획 모드
- ✅ 복잡한 다단계 작업에 사용
- ✅ 승인 전에 계획 검토
- ✅ 필요할 때 계획 수정
- ❌ 간단한 작업에는 사용하지 않음

### 확장 사고
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
- ✅ 자동화 워크플로에는 `acceptEdits` 사용
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

**최종 업데이트**: 2026년 10월 26일
**Claude Code 버전**: 2.1.310
**출처**:
- https://code.claude.com/docs/en/output-styles
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/auto-mode-classifier-billing
- https://code.claude.com/docs/en/env-vars
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/sandboxing
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/cli-reference
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/settings.md
- https://code.claude.com/docs/en/settings-reference
- https://code.claude.com/docs/en/whats-new/2026-w34
- https://code.claude.com/docs/en/model-config#adjust-effort-level
- https://code.claude.com/docs/en/interactive-mode
- https://code.claude.com/docs/en/keybindings#modifiers
- https://code.claude.com/docs/en/model-config#extended-thinking
- https://github.com/anthropics/claude-code/releases/tag/v2.1.281
- https://github.com/anthropics/claude-code/releases/tag/v2.1.283
- https://code.claude.com/docs/en/permission-modes#critical-paths
- https://code.claude.com/docs/en/settings-reference#ultracode
- https://code.claude.com/docs/en/permission-modes#which-mode-a-session-starts-in
- https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode
- https://github.com/anthropics/claude-code/releases/tag/v2.1.284
- https://github.com/anthropics/claude-code/releases/tag/v2.1.285
- https://code.claude.com/docs/en/tools-reference
- https://code.claude.com/docs/en/chrome
- https://github.com/anthropics/claude-code/releases/tag/v2.1.288
- https://github.com/anthropics/claude-code/releases/tag/v2.1.290
- https://github.com/anthropics/claude-code/releases/tag/v2.1.293
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/changelog#2-1-299
- https://code.claude.com/docs/en/changelog#2-1-300
- https://code.claude.com/docs/en/settings-reference#sandbox-enabled
- https://code.claude.com/docs/en/prompt-caching
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/monitoring-usage
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/managed-settings
- https://code.claude.com/docs/en/channels
- https://code.claude.com/docs/en/desktop
- https://code.claude.com/docs/en/fullscreen
- https://code.claude.com/docs/en/changelog#2-1-301
- https://code.claude.com/docs/en/changelog#2-1-302
- https://code.claude.com/docs/en/permission-modes#which-mode-a-non-interactive-run-starts-in
- https://code.claude.com/docs/en/permission-modes#choose-the-classifier-model
- https://code.claude.com/docs/en/changelog#2-1-309
- https://code.claude.com/docs/en/permission-modes#critical-path-removals-in-each-permission-mode
- https://code.claude.com/docs/en/permission-modes#the-mounted-drive-prompt
- https://code.claude.com/docs/en/permission-modes#time-limits-and-denials-in-auto-and-bypasspermissions-modes
- https://code.claude.com/docs/en/changelog#2-1-307
- https://code.claude.com/docs/en/settings-reference#axscreenreader
- https://code.claude.com/docs/en/routines#where-the-name-routines-still-appears
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/desktop#monitor-pull-request-status
- https://code.claude.com/docs/en/changelog#2-1-281
- https://code.claude.com/docs/en/mcp#example-query-your-postgresql-database
- https://code.claude.com/docs/en/routines#permission-prompts-during-a-run
- https://code.claude.com/docs/en/changelog#2-1-310
- https://code.claude.com/docs/en/tools-reference#monitor-tool
- https://code.claude.com/docs/en/monitoring-usage#safety-event
- https://code.claude.com/docs/en/monitoring-usage#standard-attributes
- https://code.claude.com/docs/en/monitoring-usage#tool-decision-event
- https://code.claude.com/docs/en/changelog#2-1-304
- https://code.claude.com/docs/en/sessions#the-resume-this-conversation-dialog
- https://code.claude.com/docs/en/worktrees#clean-up-worktrees
- https://code.claude.com/docs/en/sandboxing#run-commands-outside-the-sandbox-with-excludedcommands
- https://code.claude.com/docs/en/settings-reference#sandbox-allownestedusernamespaces
- https://code.claude.com/docs/en/env-vars#variables
- https://code.claude.com/docs/en/model-config#values-and-warnings-for-claude_code_auto_compact_window
- https://code.claude.com/docs/en/auto-mode-config#generate-environment-entries-with-auto-mode-setup
- https://code.claude.com/docs/en/remote-control#requirements
- https://code.claude.com/docs/en/cli-reference#cli-flags
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
