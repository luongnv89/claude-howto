<!-- i18n-source: (original) -->
<!-- i18n-source-sha: 553a319 -->
<!-- i18n-date: 2026-05-16 -->

# 실무 적용 가이드 — claude-howto를 nexus / openpi에 바로 적용하기

> 이 문서는 영문 원문의 번역이 아니라, `claude-howto`의 10개 모듈을 실제
> 사내 코드베이스(**nexus**, **openpi**)에 어떻게 적용하는지 보여주는 한국어
> 실무 가이드다. 기능 설명은 [README.md](README.md)와
> [QUICK_REFERENCE.md](QUICK_REFERENCE.md), 원문 모듈은 `../01-slash-commands/`
> 처럼 루트 경로로 연결된다.

## 왜 이 가이드인가

`claude-howto`는 기능을 잘 가르치지만 "우리 코드에 어떻게 꽂나"가 비어 있다.
이 문서는 그 빈칸을 채운다. 각 모듈마다 **기능 → nexus 적용 → openpi 적용**을
한 줄 시나리오로 제시하고, 복사해 바로 쓰는 산출물은
[`artifacts/`](artifacts/README.md)에 둔다.

### 대상 레포 한눈에

| | nexus | openpi |
|--|-------|--------|
| 성격 | RL 실험 추적 허브(MLflow) | 로봇 VLA 모델(π₀ 계열) |
| 언어 | Python 3.10+ | Python 3.11+ |
| 테스트 | `python tests/smoke_test.py` (선행: `scheduled_sync/start_local_mlflow.sh`) | `pytest src scripts packages` |
| 포맷/린트 | `ruff format .` | `ruff check . && ruff format .` (pre-commit 有) |
| CLAUDE.md | **있음**(1100줄+) + `docs/00~32` | **없음** ← 우선 도입 대상 |
| .claude/ 설정 | 없음 | 없음 |
| 특이점 | URI(5100/5000) 변경 시 8개 파일 동기 수정, 태그/네이밍 규약 다수 | 거대한 `src/openpi/training/config.py` 설정 레지스트리 |

## 모듈별 실무 적용

### 01. 슬래시 커맨드 — 반복 작업을 한 단어로

| | 적용 |
|--|------|
| **기능** | `.claude/commands/*.md`에 둔 사용자 호출 단축 명령 |
| **nexus** | `/sync-check` — `scheduled_sync/validate_sync.sh`를 실행하고 cron/상태 파일을 점검(산출물 제공) |
| **openpi** | `/train-config <name>` — `src/openpi/training/config.py`에서 해당 학습 설정을 찾아 요약. `/run-tests` — `pytest src scripts packages` 실행 후 실패만 요약 |

원문: [`../01-slash-commands/`](../01-slash-commands/)

### 02. 메모리 — 팀 규약을 Claude에 상주시키기

| | 적용 |
|--|------|
| **기능** | `CLAUDE.md`가 세션마다 자동 로드 |
| **openpi** | **최우선.** 루트에 신규 `CLAUDE.md` 도입: 빌드/테스트/린트 명령, 디렉터리 지도, `config.py` 구조, 커밋 규약(산출물 제공) |
| **nexus** | 이미 1100줄 `CLAUDE.md` 보유 → `.claude/rules/`로 모듈 분할(태그 규약·URI 규약·커밋 규약 등)해 토큰 부담을 줄이고 디렉터리별 `CLAUDE.md`(`scheduled_sync/`, `post_upload/`) 추가 |

원문: [`../02-memory/`](../02-memory/)

### 03. 스킬 — 규약 검증을 자동 호출로

| | 적용 |
|--|------|
| **기능** | 관련 상황에서 자동 호출되는 재사용 기능(점진적 공개) |
| **nexus** | "태그/실험 네이밍 규약 검증" 스킬: `post_upload/config.py`와 `docs/01_EXPERIMENT_STANDARD.md`의 불변식을 코드 전반에서 감사 |
| **openpi** | "norm-stats 계산" 스킬: 새 데이터셋 추가 시 `scripts/compute_norm_stats.py` 절차를 안내·실행 |

원문: [`../03-skills/`](../03-skills/)

### 04. 서브에이전트 — 큰 탐색을 컨텍스트 격리로

| | 적용 |
|--|------|
| **기능** | 격리된 컨텍스트를 가진 전문 에이전트 |
| **openpi** | `config-explorer` 에이전트: 거대한 `config.py`를 메인 컨텍스트 오염 없이 탐색·요약(산출물 제공) |
| **nexus** | "URI 동기 수정 검증" 에이전트: 5100/5000 변경이 8개 파일에 빠짐없이 반영됐는지 교차 점검 |

원문: [`../04-subagents/`](../04-subagents/)

### 05. MCP — GitHub 연동

| | 적용 |
|--|------|
| **기능** | 외부 도구/데이터 실시간 접근 |
| **공통** | GitHub MCP로 PR 생성·CI 상태 확인·리뷰 코멘트 처리. 두 레포 모두 PR 기반 워크플로에 직접 활용 |
| **nexus** | 중앙 MLflow 서버가 HTTP면 향후 read-only MCP로 실험 메타 질의 가능(선택) |

원문: [`../05-mcp/`](../05-mcp/)

### 06. 훅 — 편집 후 자동 검증 게이트

| | 적용 |
|--|------|
| **기능** | 이벤트 기반 자동 실행(`PostToolUse` 등) |
| **openpi** | 파일 편집 후 `ruff check`/`ruff format`, 커밋 전 `pytest` 게이트(산출물 제공). 기존 `.pre-commit-config.yaml`과 정렬 |
| **nexus** | 로거 코드 편집 후 `ruff format .`, 커밋 전 `python tests/smoke_test.py` 게이트(산출물 제공) |

원문: [`../06-hooks/`](../06-hooks/)

### 07. 플러그인 — 팀 공용 워크플로 번들

| | 적용 |
|--|------|
| **기능** | 커맨드+에이전트+훅+MCP를 한 번에 배포 |
| **공통** | 위 슬래시 커맨드·에이전트·훅을 레포별 플러그인으로 묶어 팀원이 `/plugin install`로 동일 환경 확보 |

원문: [`../07-plugins/`](../07-plugins/)

### 08. 체크포인트 — 실험 A/B

| | 적용 |
|--|------|
| **기능** | 대화/코드 상태 스냅샷 후 되감기 |
| **openpi** | 모델 아키텍처/토크나이저 변형을 체크포인트 분기로 A/B 비교 |
| **nexus** | 동기 스크립트 리팩터를 체크포인트 후 시도, 실패 시 `/rewind` |

원문: [`../08-checkpoints/`](../08-checkpoints/)

### 09. 고급 기능 — 플래닝 모드 & 백그라운드

| | 적용 |
|--|------|
| **기능** | 플래닝 모드, 확장 사고, 백그라운드 태스크, 헤드리스 |
| **openpi** | 대규모 리팩터(예: PyTorch 포팅)는 플래닝 모드로 먼저 설계. 장시간 학습/평가는 백그라운드 태스크 |
| **nexus** | 다파일 동기 변경은 플래닝 모드로 영향 범위를 먼저 확정 |

원문: [`../09-advanced-features/`](../09-advanced-features/)

### 10. CLI — CI에서 비대화 실행

| | 적용 |
|--|------|
| **기능** | `claude -p` 헤드리스, JSON 출력 |
| **공통** | CI에서 `claude -p "Run tests and summarize failures" --permission-mode dontAsk`로 회귀 요약. openpi는 `pytest`, nexus는 `smoke_test.py`에 연결 |

원문: [`../10-cli/`](../10-cli/)

## 지금 당장 시작하기 (30분 온보딩)

**openpi (메모리 우선 — 가장 효과 큼):**

```bash
# 1. 신규 프로젝트 메모리 도입
cp ko/artifacts/openpi/CLAUDE.md /home/user/openpi/CLAUDE.md

# 2. 편집 후 자동 린트 훅 + 탐색 에이전트
mkdir -p /home/user/openpi/.claude/agents
cp ko/artifacts/openpi/.claude/settings.json /home/user/openpi/.claude/settings.json
cp ko/artifacts/openpi/.claude/agents/config-explorer.md /home/user/openpi/.claude/agents/

# 3. openpi에서 Claude Code 실행 → "config.py에서 pi05 droid 설정을 요약해줘"
#    config-explorer 에이전트가 자동 위임되어 메인 컨텍스트를 보호한다
```

**nexus (슬래시 커맨드 + 검증 게이트):**

```bash
# 1. 동기 점검 슬래시 커맨드
mkdir -p /home/user/nexus/.claude/commands
cp ko/artifacts/nexus/.claude/commands/sync-check.md /home/user/nexus/.claude/commands/

# 2. 커밋 전 smoke test 게이트
cp ko/artifacts/nexus/.claude/settings.json /home/user/nexus/.claude/settings.json

# 3. nexus에서 Claude Code 실행 → /sync-check 입력
```

> 산출물 상세와 커스터마이즈 방법은 [`artifacts/README.md`](artifacts/README.md) 참조.

## 검증 방법

- **claude-howto 문서 품질**(이 가이드/번역 자체):
  레포 루트에서 `python scripts/check_cross_references.py`,
  `python scripts/check_mermaid.py`, `python scripts/check_markdown_rendering.py`,
  가능하면 `pre-commit run --files ko/...`.
- **openpi 산출물 동작:** openpi 레포에서
  `pytest src scripts packages`와 `ruff check .`가 통과하는지 확인 후
  훅이 같은 명령을 호출하는지 대조.
- **nexus 산출물 동작:** `scheduled_sync/start_local_mlflow.sh` 기동 후
  `python tests/smoke_test.py`가 통과하는지 확인하고 `/sync-check`가
  `validate_sync.sh`를 올바로 실행하는지 점검.

## 다음 단계

1. openpi `CLAUDE.md`를 팀 리뷰 후 실제 레포에 커밋
2. 슬래시 커맨드/에이전트가 안정화되면 07-plugins 방식으로 번들화
3. GitHub MCP를 붙여 PR·CI 루프까지 자동화
