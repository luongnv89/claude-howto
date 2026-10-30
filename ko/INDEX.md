<!-- i18n-source: INDEX.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 예시 - 전체 색인

이 문서는 기능 유형별로 정리된 모든 예시 파일의 전체 색인을 제공합니다.

## 요약 통계

- **총 파일 수**: 100개 이상
- **카테고리**: 10가지 기능 카테고리
- **플러그인**: 3개의 완벽한 플러그인
- **스킬**: 6개의 완벽한 스킬
- **훅**: 11가지 예시 훅
- **즉시 사용 가능**: 모든 예시

---

## 01. 슬래시 명령어 (10개 파일)

일반적인 워크플로를 위한 사용자 호출 단축 명령어입니다.

| 파일 | 설명 | 사용 사례 |
|------|-------------|----------|
| `optimize.md` | 코드 최적화 분석기 | 성능 문제 찾기 |
| `pr.md` | 풀 리퀘스트 준비 | PR 워크플로 자동화 |
| `generate-api-docs.md` | API 문서 생성기 | API 문서 생성 |
| `commit.md` | 커밋 메시지 도우미 | 표준화된 커밋 |
| `setup-ci-cd.md` | CI/CD 파이프라인 설정 | 데브옵스 자동화 |
| `push-all.md` | 모든 변경사항 푸시 | 빠른 푸시 워크플로 |
| `unit-test-expand.md` | 단위 테스트 커버리지 확장 | 테스트 자동화 |
| `doc-refactor.md` | 문서 리팩터링 | 문서 개선 |
| `pr-slash-command.png` | 스크린샷 예시 | 시각적 참고 자료 |
| `README.md` | 문서 | 설정 및 사용 가이드 |

**설치 경로**: `.claude/commands/`

**사용법**: `/optimize`, `/pr`, `/generate-api-docs`, `/commit`, `/setup-ci-cd`, `/push-all`, `/unit-test-expand`, `/doc-refactor`

---

## 02. 메모리 (6개 파일)

영구적인 컨텍스트와 프로젝트 표준입니다.

| 파일 | 설명 | 범위 | 위치 |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | 팀 프로젝트 표준 | 프로젝트 전체 | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API별 규칙 | 디렉터리 | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | 개인 설정 | 사용자 | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | 스크린샷: 메모리 저장됨 | - | 시각적 참고 자료 |
| `memory-ask-claude.png` | 스크린샷: Claude에게 질문 | - | 시각적 참고 자료 |
| `README.md` | 문서 | - | 참조 |

**설치**: 적절한 위치에 복사

**사용법**: Claude가 자동으로 로드합니다.

**AGENTS.md** (v2.1.277): 작업 디렉터리나 그 상위에 `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md`가 없으면 프로젝트 지침으로 읽힙니다. [`02-memory/README.md#agentsmd`](02-memory/README.md#agentsmd)를 참고하세요.

---

## 03. 스킬 (23개 파일)

스크립트 및 템플릿과 함께 자동으로 호출되는 기능입니다.

### 코드 검토 스킬 (5개 파일)
```
code-review-specialist/
├── SKILL.md                          # 스킬 정의
├── scripts/
│   ├── analyze-metrics.py            # 코드 메트릭 분석기
│   └── compare-complexity.py         # 복잡도 비교
└── templates/
    ├── review-checklist.md           # 검토 체크리스트
    └── finding-template.md           # 발견 사항 문서
```

**목적**: 보안, 성능 및 품질 분석을 포함한 종합적인 코드 검토입니다.

**자동 호출**: 코드를 검토할 때

---

### 브랜드 보이스 스킬 (4개 파일)
```
brand-voice/
├── SKILL.md                          # 스킬 정의
├── templates/
│   ├── email-template.txt            # 이메일 형식
│   └── social-post-template.txt      # 소셜 미디어 형식
└── tone-examples.md                  # 예시 메시지
```

**목적**: 커뮤니케이션에서 일관된 브랜드 보이스를 보장합니다.

**자동 호출**: 마케팅 문구를 작성할 때

---

### 문서 생성기 스킬 (2개 파일)
```
doc-generator/
├── SKILL.md                          # 스킬 정의
└── generate-docs.py                  # 파이썬 문서 추출기
```

**목적**: 소스 코드로부터 포괄적인 API 문서를 생성합니다.

**자동 호출**: API 문서를 생성/업데이트할 때

---

### 리팩터 스킬 (5개 파일)
```
refactor/
├── SKILL.md                          # 스킬 정의
├── scripts/
│   ├── analyze-complexity.py         # 복잡도 분석기
│   └── detect-smells.py              # 코드 스멜 감지기
├── references/
│   ├── code-smells.md                # 코드 스멜 카탈로그
│   └── refactoring-catalog.md        # 리팩터링 패턴
└── templates/
    └── refactoring-plan.md           # 리팩터링 계획 템플릿
```

**목적**: 복잡도 분석을 통한 체계적인 코드 리팩터링입니다.

**자동 호출**: 코드를 리팩터링할 때

---

### Claude MD 스킬 (1개 파일)
```
claude-md/
└── SKILL.md                          # 스킬 정의
```

**목적**: CLAUDE.md 파일을 관리하고 최적화합니다.

---

### 블로그 초안 스킬 (3개 파일)
```
blog-draft/
├── SKILL.md                          # 스킬 정의
└── templates/
    ├── draft-template.md             # 블로그 초안 템플릿
    └── outline-template.md           # 블로그 개요 템플릿
```

**목적**: 일관된 구조로 블로그 게시물 초안을 작성합니다.

**추가**: `README.md` - 스킬 개요 및 사용 가이드

**설치 경로**: `~/.claude/skills/` 또는 `.claude/skills/`

---

## 04. 서브에이전트 (10개 파일)

사용자 지정 기능을 갖춘 특화된 AI 어시스턴트입니다.

| 파일 | 설명 | 도구 | 사용 사례 |
|------|-------------|-------|----------|
| `code-reviewer.md` | 코드 품질 분석 | Read, Grep, Glob, Bash | 종합적인 검토 |
| `test-engineer.md` | 테스트 커버리지 분석 | Read, Write, Bash, Grep | 테스트 자동화 |
| `documentation-writer.md` | 문서 작성 | Read, Write, Grep | 문서 생성 |
| `secure-reviewer.md` | 보안 검토 (읽기 전용) | Read, Grep | 보안 감사 |
| `implementation-agent.md` | 전체 구현 | Read, Write, Edit, Bash, Grep, Glob | 기능 개발 |
| `debugger.md` | 디버깅 전문가 | Read, Edit, Bash, Grep, Glob | 버그 조사 |
| `data-scientist.md` | 데이터 분석 전문가 | Bash, Read, Write | 데이터 워크플로 |
| `clean-code-reviewer.md` | 클린 코드 표준 | Read, Grep, Glob, Bash | 코드 품질 |
| `performance-optimizer.md` | 성능 병목 분석 | Read, Edit, Bash, Grep, Glob | 최적화 작업 |
| `README.md` | 문서 | - | 설정 및 사용 가이드 |

**설치 경로**: `.claude/agents/`

**사용법**: 메인 에이전트에 의해 자동으로 위임됩니다.

---

## 05. MCP 프로토콜 (5개 파일)

외부 도구 및 API 통합입니다.

| 파일 | 설명 | 통합 대상 | 사용 사례 |
|------|-------------|-----------------|----------|
| `github-mcp.json` | GitHub 통합 | GitHub API | PR/이슈 관리 |
| `database-mcp.json` | 데이터베이스 쿼리 | PostgreSQL/MySQL | 실시간 데이터 쿼리 |
| `filesystem-mcp.json` | 파일 작업 | 로컬 파일 시스템 | 파일 관리 |
| `multi-mcp.json` | 다중 서버 | GitHub + DB + Slack | 완전한 통합 |
| `README.md` | 문서 | - | 설정 및 사용 가이드 |

**설치 경로**: `.mcp.json` (프로젝트 범위) 또는 `~/.claude.json` (사용자 범위)

**사용법**: `/mcp__github__list_prs`, 등.

---

## 06. 훅 (12개 파일)

자동으로 실행되는 이벤트 기반 자동화 스크립트입니다.

| 파일 | 설명 | 이벤트 | 사용 사례 |
|------|-------------|-------|----------|
| `format-code.sh` | 코드 자동 포맷 | PostToolUse (matcher: Write) | 코드 포맷팅 |
| `pre-commit.sh` | 커밋 전 테스트 실행 | PreToolUse (matcher: Bash) | 테스트 자동화 |
| `pre-tool-check.sh` | 명령어 실행 전 검증 및 감사 | PreToolUse (matcher: Bash) | 가드레일, 감사 로그 |
| `security-scan.sh` | 보안 스캐닝 | PostToolUse (matcher: Write) | 보안 검사 |
| `dependency-check.sh` | 의존성 매니페스트의 취약점 검사 | PostToolUse (matcher: Write) | 공급망 검사 |
| `log-bash.sh` | Bash 명령어 로깅 | PostToolUse (matcher: Bash) | 명령어 로깅 |
| `notify-team.sh` | 알림 보내기 | PostToolUse (matcher: Bash) | 팀 알림 |
| `validate-prompt.sh` | 프롬프트 유효성 검사 | UserPromptSubmit | 입력 유효성 검사 |
| `session-end.sh` | 세션 종료 시 진행 상황 기록 | SessionEnd | 진행 상황 추적 |
| `context-tracker.py` | 컨텍스트 창 사용량 추적 | UserPromptSubmit, Stop | 컨텍스트 모니터링 |
| `context-tracker-tiktoken.py` | 토큰 기반 컨텍스트 추적 | UserPromptSubmit, Stop | 정확한 토큰 계산 |
| `README.md` | 문서 | - | 설정 및 사용 가이드 |

**설치 경로**: `~/.claude/settings.json`에서 구성

**사용법**: 설정에서 구성되며 자동으로 실행됩니다.

**훅 유형** (5가지): `command`, `http`, `prompt`, `mcp_tool`, `agent` — 훅이 실행되는 방식입니다.

**훅 이벤트** (33가지, 4개 범주) — 훅이 실행되는 시점입니다.
- 도구 훅: PreToolUse, PostToolUse, PostToolUseFailure, PostToolBatch, PermissionRequest, PermissionDenied
- 세션 훅: SessionStart, Setup, SessionEnd, Stop, StopFailure, SubagentStart, SubagentStop
- 태스크 훅: UserPromptSubmit, UserPromptExpansion, MessageDisplay, TaskCompleted, TaskCreated, TeammateIdle (TaskCompleted/TaskCreated는 todo 도구가 활성화된 경우에만 실행되며, 이 도구는 Claude 3.x 모델, Opus 4~4.7, Sonnet 4~4.6, Haiku 4.5에서만 기본으로 제공됩니다)
- 수명 주기 훅: ConfigChange, CwdChanged, DirectoryAdded, FileChanged, PreCompact, PostCompact, PreModelSwitch, PostModelSwitch, WorktreeCreate, WorktreeRemove, Notification, InstructionsLoaded, Elicitation, ElicitationResult

---

## 07. 플러그인 (3개의 완전한 플러그인, 39개 파일)

기능들을 묶어 놓은 모음집입니다.

### PR 검토 플러그인 (10개 파일)
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # 플러그인 매니페스트
├── commands/
│   ├── review-pr.md                  # 종합 검토
│   ├── check-security.md             # 보안 검사
│   └── check-tests.md                # 테스트 커버리지 검사
├── agents/
│   ├── security-reviewer.md          # 보안 전문가
│   ├── test-checker.md               # 테스트 전문가
│   └── performance-analyzer.md       # 성능 전문가
├── mcp/
│   └── github-config.json            # GitHub 통합
├── hooks/
│   └── pre-review.js                 # 사전 검토 유효성 검사
└── README.md                         # 플러그인 문서
```

**기능**: 보안 분석, 테스트 커버리지, 성능 영향

**명령어**: `/review-pr`, `/check-security`, `/check-tests`

**설치**: `claude --plugin-dir ./07-plugins/pr-review` (저장소 루트에서 실행)

---

### 데브옵스 자동화 플러그인 (15개 파일)
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # 플러그인 매니페스트
├── commands/
│   ├── deploy.md                     # 배포
│   ├── rollback.md                   # 롤백
│   ├── status.md                     # 시스템 상태
│   └── incident.md                   # 인시던트 대응
├── agents/
│   ├── deployment-specialist.md      # 배포 전문가
│   ├── incident-commander.md         # 인시던트 코디네이터
│   └── alert-analyzer.md             # 경고 분석기
├── mcp/
│   └── kubernetes-config.json        # Kubernetes 통합
├── hooks/
│   ├── pre-deploy.js                 # 배포 전 검사
│   └── post-deploy.js                # 배포 후 작업
├── scripts/
│   ├── deploy.sh                     # 배포 자동화
│   ├── rollback.sh                   # 롤백 자동화
│   └── health-check.sh               # 상태 검사
└── README.md                         # 플러그인 문서
```

**기능**: Kubernetes 배포, 롤백, 모니터링, 인시던트 대응

**명령어**: `/deploy`, `/rollback`, `/status`, `/incident`

**설치**: `claude --plugin-dir ./07-plugins/devops-automation` (저장소 루트에서 실행)

---

### 문서화 플러그인 (14개 파일)
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # 플러그인 매니페스트
├── commands/
│   ├── generate-api-docs.md          # API 문서 생성
│   ├── generate-readme.md            # README 생성
│   ├── sync-docs.md                  # 문서 동기화
│   └── validate-docs.md              # 문서 유효성 검사
├── agents/
│   ├── api-documenter.md             # API 문서 전문가
│   ├── code-commentator.md           # 코드 주석 전문가
│   └── example-generator.md          # 예시 생성기
├── mcp/
│   └── github-docs-config.json       # GitHub 통합
├── templates/
│   ├── api-endpoint.md               # API 엔드포인트 템플릿
│   ├── function-docs.md              # 함수 문서 템플릿
│   └── adr-template.md               # ADR 템플릿
└── README.md                         # 플러그인 문서
```

**기능**: API 문서, README 생성, 문서 동기화, 유효성 검사

**명령어**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**설치**: `claude --plugin-dir ./07-plugins/documentation` (저장소 루트에서 실행)

**추가**: `README.md` - 플러그인 개요 및 사용 가이드

---

## 08. 체크포인트 및 되감기 (2개 파일)

대화 상태를 저장하고 대안적인 접근 방식을 탐색합니다.

| 파일 | 설명 | 내용 |
|------|-------------|---------|
| `README.md` | 문서 | 포괄적인 체크포인트 가이드 |
| `checkpoint-examples.md` | 실제 예시 | 데이터베이스 마이그레이션, 성능 최적화, UI 반복, 디버깅 |
| | | |

**주요 개념**:
- **체크포인트**: 대화 상태의 스냅샷
- **되감기**: 이전 체크포인트로 돌아가기
- **분기점**: 여러 접근 방식 탐색

**사용법**:
```
# 체크포인트는 사용자 프롬프트마다 자동으로 생성됩니다.
# 되감으려면 Esc를 두 번 누르거나 다음을 사용하십시오:
/rewind
# 그런 다음 선택하십시오: 코드 및 대화 복원, 대화 복원,
# 코드 복원, 여기부터 요약, 여기까지 요약 또는 취소
```

**사용 사례**:
- 다양한 구현 시도
- 실수에서 복구
- 안전한 실험
- 솔루션 비교
- A/B 테스트

---

## 09. 고급 기능 (4개 파일)

복잡한 워크플로를 위한 고급 기능입니다.

| 파일 | 설명 | 기능 |
|------|-------------|----------|
| `README.md` | 완벽 가이드 | 모든 고급 기능 문서 |
| `config-examples.json` | 구성 예시 | 10가지 이상의 사용 사례별 구성 |
| `planning-mode-examples.md` | 계획 예시 | REST API, 데이터베이스 마이그레이션, 리팩터링 |
| `setup-auto-mode-permissions.py` | 자동 모드용 `permissions.allow` 초기 설정 | 멱등성, `--dry-run` 및 옵트인 플래그 |
| 동적 워크플로 | `/workflows` (v2.1.154)를 통한 확정적 다중 에이전트 오케스트레이션 | 포괄적인 감사, 마이그레이션, 스케일 아웃 |
| 예약 작업 | `/loop` 및 cron 도구를 사용한 세션 범위 반복 작업 | 자동화된 반복 워크플로 |
| Chrome 통합 | Claude in Chrome 확장 프로그램을 통해 사용자의 Chrome에서 브라우저 자동화 | 웹 테스트 및 스크래핑 |
| 원격 제어 (확장됨) | 연결 방법, 보안, 비교 표, 디바이스 카드 | 원격 세션 관리 (더 이상 리서치 프리뷰가 아님) |
| 세션 간 메시징 | `notify_when_idle`(v2.1.236)을 포함한 `SendMessage` / `ListAgents` | 같은 머신의 세션 간 협업 |
| 키보드 사용자 지정 | 사용자 지정 키 바인딩, 코드 지원, 컨텍스트 | 개인화된 단축키 |
| 데스크톱 앱 (확장됨) | 커넥터, launch.json, 엔터프라이즈 기능 | 데스크톱 통합 |
| | | |

**다루는 고급 기능**:

### 계획 모드
- 상세 구현 계획 생성
- 시간 추정 및 위험 평가
- 체계적인 작업 분할

### 확장 사고
- 복잡한 문제에 대한 심층 추론
- 아키텍처 의사 결정 분석
- 트레이드오프 평가

### 백그라운드 작업
- 블로킹 없이 장기 실행 작업
- 병렬 개발 워크플로
- 작업 관리 및 모니터링

### 동적 워크플로 (v2.1.154)
- 수십에서 수백 개의 백그라운드 서브에이전트의 확정적 오케스트레이션
- 포괄적인 커버리지를 위한 팬아웃 / 파이프라인 / 병렬 단계
- `/workflows`로 실행을 확인합니다. `/effort`의 Ultracode 토글(`/effort ultracode [on|off]`)은 effort 수준을 바꾸지 않고 세션에서 이를 켜며(v2.1.284), `ultracode` 설정으로 지속시킬 수 있습니다.
- v2.1.219부터 기본 크기 가이드라인은 중간(에이전트 10개 미만 목표)이며, `/config`의 **Dynamic workflow size**로 변경할 수 있습니다.

### 권한 모드
- **manual**: 읽기 이외의 모든 작업 전에 확인 (v2.1.200부터 Manual로 표시되며, 구성 값은 여전히 `default`)
- **acceptEdits**: 파일 편집 자동 승인, 다른 작업은 요청
- **plan**: 읽기 전용 분석, 수정 없음
- **auto**: 모든 작업을 백그라운드 안전 검사와 함께 수행 — 분류기가 명령어와 보호된 디렉터리 쓰기를 검토 (`autoMode` 설정 객체로 구성)
- **dontAsk**: 사전 승인된 도구만 실행 — 프롬프트가 필요한 모든 호출을 자동 거부. Claude는 `permissions.allow`에 일치하는 항목, 읽기 전용 Bash 명령어, `PreToolUse` 훅이 승인한 호출만 실행
- **bypassPermissions**: 모든 작업 승인 (`--permission-mode bypassPermissions` 또는 동등한 `--dangerously-skip-permissions`로 활성화)

### 헤드리스 모드 (`claude -p`)
- CI/CD 통합
- 자동화된 작업 실행
- 배치 처리

### 세션 관리
- 다중 작업 세션
- 세션 전환 및 저장
- 세션 지속성

### 대화형 기능
- 키보드 단축키
- 명령어 기록
- 탭 자동 완성
- 다중 라인 입력

### 구성
- 포괄적인 설정 관리
- 환경별 구성
- 프로젝트별 사용자 지정

### 예약 작업
- `/loop` 명령을 사용한 세션 범위 반복 작업
- Cron 도구: CronCreate, CronList, CronDelete
- 자동화된 반복 워크플로

### Chrome 통합
- Claude in Chrome 확장 프로그램을 통해 사용자의 Chrome에서 브라우저 자동화
- 웹 테스트 및 스크래핑 기능
- 페이지 상호 작용 및 데이터 추출

### 원격 제어 (확장됨)
- 연결 방법 및 프로토콜
- 보안 고려 사항 및 모범 사례
- 원격 액세스 옵션 비교 표
- 리서치 프리뷰 종료 — `claude remote-control`을 실행 중인 머신이 Claude 앱 Code 탭에 디바이스 카드로 표시됨

### 세션 간 메시징
- 같은 머신의 세션 간 `SendMessage`
- `notify_when_idle` — 상대 세션이 다음에 유휴 상태가 될 때 한 번 알림(옵트인, v2.1.236)
- `ListAgents`가 세션 자신의 이름을 보고하고 실행 중인 팀원 목록을 표시(v2.1.239)

### 키보드 사용자 지정
- 사용자 지정 키 바인딩 구성
- 다중 키 단축키를 위한 코드 지원
- 컨텍스트 인식 키 바인딩 활성화

### 데스크톱 앱 (확장됨)
- IDE 통합을 위한 커넥터
- launch.json 구성
- 엔터프라이즈 기능 및 배포

---

## 10. CLI 사용법 (1개 파일)

명령줄 인터페이스 사용 패턴 및 참조.

| 파일 | 설명 | 내용 |
|------|-------------|----------|
| `README.md` | CLI 문서 | 플래그, 옵션 및 사용 패턴 |

**주요 CLI 기능**:
- `claude` - 대화형 세션 시작
- `claude -p "prompt"` - 헤드리스/비대화형 모드
- `claude --cloud "task"` - 클라우드(웹) 세션 시작
- `claude --model` - 모델 선택 (Opus 5.5, Sonnet 5.5, Opus 5, Sonnet 5, Sonnet 4.6, Opus 4.8, Haiku 5.5, Haiku 4.5)
- `claude --permission-mode` - 권한 모드 설정
- `claude --remote-control` - claude.ai 또는 Claude 앱에서도 조작할 수 있는 세션 시작

---

## 문서 파일 (13개 파일)

| 파일 | 위치 | 설명 |
|------|----------|-------------|
| `README.md` | `/` | 주요 예시 개요 |
| `INDEX.md` | `/` | 이 전체 색인 |
| `QUICK_REFERENCE.md` | `/` | 빠른 참조 카드 |
| `README.md` | `/01-slash-commands/` | 슬래시 명령어 가이드 |
| `README.md` | `/02-memory/` | 메모리 가이드 |
| `README.md` | `/03-skills/` | 스킬 가이드 |
| `README.md` | `/04-subagents/` | 서브에이전트 가이드 |
| `README.md` | `/05-mcp/` | MCP 가이드 |
| `README.md` | `/06-hooks/` | 훅 가이드 |
| `README.md` | `/07-plugins/` | 플러그인 가이드 |
| `README.md` | `/08-checkpoints/` | 체크포인트 가이드 |
| `README.md` | `/09-advanced-features/` | 고급 기능 가이드 |
| `README.md` | `/10-cli/` | CLI 가이드 |

---

## 전체 파일 트리

```
claude-howto/
├── README.md                                    # 주요 개요
├── INDEX.md                                     # 이 파일
├── QUICK_REFERENCE.md                           # 빠른 참조 카드
├── claude_concepts_guide.md                     # 원본 가이드
│
├── 01-slash-commands/                           # 슬래시 명령어
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # 메모리
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # 스킬
│   ├── code-review-specialist/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # 서브에이전트
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # MCP 프로토콜
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # 훅
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # 플러그인
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # 체크포인트
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # 고급 기능
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # CLI 사용법
    └── README.md
```

---

## 사용 사례별 빠른 시작

### 코드 품질 및 검토
```bash
# 슬래시 명령어 설치
cp 01-slash-commands/optimize.md .claude/commands/

# 서브에이전트 설치
cp 04-subagents/code-reviewer.md .claude/agents/

# 스킬 설치
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# 또는 전체 플러그인 설치
claude --plugin-dir ./07-plugins/pr-review
```

### 데브옵스 및 배포
```bash
# 플러그인 설치 (모든 것 포함)
claude --plugin-dir ./07-plugins/devops-automation
```

### 문서화
```bash
# 슬래시 명령어 설치
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# 서브에이전트 설치
cp 04-subagents/documentation-writer.md .claude/agents/

# 스킬 설치
cp -r 03-skills/doc-generator ~/.claude/skills/

# 또는 전체 플러그인 설치
claude --plugin-dir ./07-plugins/documentation
```

### 팀 표준
```bash
# 프로젝트 메모리 설정
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 팀의 표준에 맞게 편집
```

### 외부 통합
```bash
# 환경 변수 설정
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
export DATABASE_URL="postgresql://..."
export SLACK_BOT_TOKEN="your-slack-bot-token"
export SLACK_TEAM_ID="T0000000000"

# MCP 구성 설치 (프로젝트 범위)
cp 05-mcp/multi-mcp.json .mcp.json
```

### 자동화 및 유효성 검사
```bash
# 훅 설치
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 설정에서 훅 구성 (~/.claude/settings.json)
# 06-hooks/README.md 참조
```

### 안전한 실험
```bash
# 체크포인트는 사용자 프롬프트마다 자동으로 생성됩니다.
# 되감기: Esc+Esc를 누르거나 /rewind 사용
# 그런 다음 되감기 메뉴에서 복원할 항목을 선택하십시오.

# 예시는 08-checkpoints/README.md 참조
```

### 고급 워크플로
```bash
# 고급 기능 구성
# 09-advanced-features/config-examples.json 참조

# 계획 모드 사용
/plan Implement feature X

# 권한 모드 사용
claude --permission-mode plan          # 코드 검토용 (읽기 전용)
claude --permission-mode acceptEdits   # 편집 자동 승인
claude --permission-mode auto          # 안전한 작업 자동 승인

# CI/CD를 위해 헤드리스 모드로 실행
claude -p "Run tests and report results" --permission-mode auto

# 백그라운드 작업 실행
Run tests in background

# 완전한 가이드는 09-advanced-features/README.md 참조
```

---

## 기능 커버리지 매트릭스

| 카테고리 | 명령어 | 에이전트 | MCP | 훅 | 스크립트 | 템플릿 | 문서 | 이미지 | 합계 |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 슬래시 명령어** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 메모리** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 스킬** | - | - | - | - | 5 | 7 | 11 | - | **23** |
| **04 서브에이전트** | - | 9 | - | - | - | - | 1 | - | **10** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 훅** | - | - | - | 11 | - | - | 1 | - | **12** |
| **07 플러그인** | 11 | 9 | 3 | 3 | 3 | 3 | 7 | - | **39** |
| **08 체크포인트** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 고급** | - | - | - | - | 1 | 1 | 2 | - | **4** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## 학습 경로

### 초급 (1주차)
1. ✅ `README.md` 읽기
2. ✅ 슬래시 명령어 1-2개 설치
3. ✅ 프로젝트 메모리 파일 생성
4. ✅ 기본 명령어 시도

### 중급 (2-3주차)
1. ✅ GitHub MCP 설정
2. ✅ 서브에이전트 설치
3. ✅ 작업 위임 시도
4. ✅ 스킬 설치

### 고급 (4주차 이상)
1. ✅ 완벽한 플러그인 설치
2. ✅ 사용자 지정 슬래시 명령어 생성
3. ✅ 사용자 지정 서브에이전트 생성
4. ✅ 사용자 지정 스킬 생성
5. ✅ 자신만의 플러그인 구축

### 전문가 (5주차 이상)
1. ✅ 자동화를 위한 훅 설정
2. ✅ 실험을 위한 체크포인트 사용
3. ✅ 계획 모드 구성
4. ✅ 권한 모드를 효과적으로 사용
5. ✅ CI/CD를 위한 헤드리스 모드 설정
6. ✅ 세션 관리 마스터

---

## 키워드로 검색

### 성능
- `01-slash-commands/optimize.md` - 성능 분석
- `04-subagents/code-reviewer.md` - 성능 검토
- `03-skills/code-review-specialist/` - 성능 지표
- `07-plugins/pr-review/agents/performance-analyzer.md` - 성능 전문가

### 보안
- `04-subagents/secure-reviewer.md` - 보안 검토
- `03-skills/code-review-specialist/` - 보안 분석
- `07-plugins/pr-review/` - 보안 검사

### 테스트
- `04-subagents/test-engineer.md` - 테스트 엔지니어
- `07-plugins/pr-review/commands/check-tests.md` - 테스트 커버리지

### 문서화
- `01-slash-commands/generate-api-docs.md` - API 문서 명령어
- `04-subagents/documentation-writer.md` - 문서 작성 에이전트
- `03-skills/doc-generator/` - 문서 생성기 스킬
- `07-plugins/documentation/` - 완벽한 문서 플러그인

### 배포
- `07-plugins/devops-automation/` - 완벽한 데브옵스 솔루션

### 자동화
- `06-hooks/` - 이벤트 기반 자동화
- `06-hooks/pre-commit.sh` - 사전 커밋 자동화
- `06-hooks/format-code.sh` - 자동 포맷팅
- `09-advanced-features/` - CI/CD를 위한 헤드리스 모드

### 유효성 검사
- `06-hooks/security-scan.sh` - 보안 유효성 검사
- `06-hooks/validate-prompt.sh` - 프롬프트 유효성 검사

### 실험
- `08-checkpoints/` - 되감기를 통한 안전한 실험
- `08-checkpoints/checkpoint-examples.md` - 실제 예시

### 계획
- `09-advanced-features/planning-mode-examples.md` - 계획 모드 예시
- `09-advanced-features/README.md` - 확장 사고

### 구성
- `09-advanced-features/config-examples.json` - 구성 예시

---

## 참고 사항

- 모든 예시는 즉시 사용할 수 있습니다.
- 특정 요구사항에 맞게 수정하십시오.
- 예시는 Claude Code 모범 사례를 따릅니다.
- 각 카테고리에는 상세 지침이 포함된 자체 README가 있습니다.
- 스크립트에는 적절한 오류 처리가 포함되어 있습니다.
- 템플릿은 사용자 지정 가능합니다.

---

## 기여

더 많은 예시를 추가하고 싶으십니까? 다음 구조를 따르십시오:
1. 적절한 하위 디렉터리 생성
2. 사용법이 포함된 README.md 추가
3. 명명 규칙 준수
4. 철저히 테스트
5. 이 색인 업데이트

---

**최종 업데이트**: 2026년 10월 26일
**Claude Code 버전**: 2.1.310
**출처**:
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/memory#agents-md
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/permission-modes
- https://github.com/anthropics/claude-code/releases/tag/v2.1.153
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/plugins/install
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/chrome
- https://code.claude.com/docs/en/headless#auto-approve-tools
- https://code.claude.com/docs/en/permission-modes#which-mode-a-non-interactive-run-starts-in
- https://code.claude.com/docs/en/scheduled-tasks
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
**총 예시 수**: 100개 이상 파일
**카테고리**: 10가지 기능
**훅**: 11가지 자동화 스크립트
**구성 예시**: 10가지 이상 시나리오
**즉시 사용 가능**: 모든 예시
