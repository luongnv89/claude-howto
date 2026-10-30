<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 기능 카탈로그

> Claude Code의 모든 기능(명령어, 에이전트, 스킬, 플러그인, 훅)에 대한 빠른 참조 가이드입니다.

**탐색**: [Commands](#slash-commands) | [Permission Modes](#permission-modes) | [Subagents](#subagents) | [Skills](#skills) | [Plugins](#plugins) | [MCP Servers](#mcp-servers) | [Hooks](#hooks) | [Memory](#memory-files) | [New Features](#new-features)

---

## 요약

| Feature | Built-in | Examples | Total | Reference |
|---------|----------|----------|-------|-----------|
| **Slash Commands** | 60+ | 8 | 68+ | [01-slash-commands/](01-slash-commands/) |
| **Subagents** | 6 | 9 | 15 | [04-subagents/](04-subagents/) |
| **Skills** | 기본 제공 20개 | 6 | 26 | [03-skills/](03-skills/) |
| **Plugins** | - | 3 | 3 | [07-plugins/](07-plugins/) |
| **MCP Servers** | - | 4 | 4 | [05-mcp/](05-mcp/) |
| **Hooks** | 이벤트 33개 | 11 | 44 | [06-hooks/](06-hooks/) |
| **Memory** | 유형 7개 | 3 | 10 | [02-memory/](02-memory/) |
| **합계** | **126** | **44** | **170** | |

---

## Slash Commands

명령어는 사용자가 직접 실행하여 특정 작업을 수행하는 단축 명령입니다.

### 기본 제공 명령어

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/help` | 도움말 정보 표시 | 시작하기, 명령어 학습 |
| `/btw` | 메인 컨텍스트를 오염시키지 않는 임시 질문 | 짧은 주제 전환 질문 |
| `/chrome` | Chrome 연동 설정 | 브라우저 자동화 |
| `/clear` | 대화 기록 삭제 | 새로 시작, 컨텍스트 축소 |
| `/diff` | 대화형 diff 뷰어. 전체 화면 TUI(v2.1.260+)에서는 대화 옆에 diff 패널을 열어 계속 열어 두며, Claude가 파일을 편집하거나 명령어를 실행할 때마다 새로 고칩니다. 클래식 렌더러에서는 프롬프트 자리에 뷰어를 엽니다 | 변경 사항 검토 |
| `/config` | 설정 조회/수정 | 동작 사용자 지정 |
| `/status` | 세션 상태 표시 | 현재 상태 확인 |
| `/agents` | 제거됨: 마법사는 v2.1.198에서 제거되었고, 명령어는 v2.1.281에서 `/` 메뉴와 `/help`에서 빠졌습니다 — Claude에게 서브에이전트 생성·관리를 요청하거나 `.claude/agents/`를 직접 편집하세요 | Claude에게 요청하여 서브에이전트 관리 |
| `/skills` | 사용 가능한 스킬 목록 표시 | 자동 호출 기능 확인 |
| `/hooks` | 구성된 훅 목록 표시 | 자동화 디버깅 |
| `/insights` | 세션 패턴 분석 | 세션 최적화 |
| `/install-slack-app` | Claude Slack 앱 설치 | Slack 연동 |
| `/keybindings` | 키보드 단축키 사용자 지정 | 단축키 설정 |
| `/mcp` | MCP 서버 목록 표시 | 외부 연동 확인 |
| `/memory` | 로드된 메모리 파일 표시 | 컨텍스트 로딩 디버깅 |
| `/mobile` | 모바일 QR 코드 생성 | 모바일 접속 |
| `/passes` | 친구에게 Claude Code 무료 1주 이용권 공유(자격이 있는 계정만) | 추천 |
| `/plugin` | 플러그인 관리 | 확장 기능 설치/제거 |
| `/plan` | 계획 모드 진입 | 복잡한 구현 작업 |
| `/proactive` | `/loop`의 별칭 (v2.1.105) | `/loop`와 동일 |
| `/recap` | 세션에 다시 돌아왔을 때 요약 표시 | 자리를 비운 후 작업 내용 확인 |
| `/rewind` | 체크포인트로 되돌리기 | 변경 사항 취소, 대안 탐색 |
| `/checkpoint` | `/rewind`의 별칭 | `/rewind`와 동일 |
| `/cost` | `/usage`의 비용 탭을 여는 단축 별칭 (v2.1.118+) | 비용 모니터링 |
| `/context` | 컨텍스트 창 사용량 표시 | 대화 길이 관리 |
| `/export` | 대화 내보내기 | 참조용 저장 |
| `/usage-credits` | 추가 사용 한도 설정 (`/extra-usage`에서 이름 변경, v2.1.144, 기존 이름도 별칭으로 사용 가능) | 사용량 제한 관리 |
| `/feedback` | 피드백 또는 버그 리포트 제출 | 문제 신고 |
| `/login` | Anthropic 인증 | 기능 사용 |
| `/logout` | 로그아웃 | 계정 전환 |
| `/sandbox` | 샌드박스 모드 전환 | 안전한 명령 실행 |
| `/doctor` | 진단 실행 | 문제 해결 |
| `/reload-plugins` | 설치된 플러그인 다시 로드. v2.1.221부터 대부분의 설치는 즉시 활성화되므로, 설치 요약에 `Run /reload-plugins to activate.`가 표시될 때만 필요합니다. v2.1.260+부터 헤드리스 세션에서도 사용할 수 있어 Claude Code Desktop과 SDK 명령어 목록에 표시됩니다 | 플러그인 관리 |
| `/reload-skills` | 재시작 없이 스킬 디렉터리 다시 검색 (v2.1.152). v2.1.304부터 새로 추가되었거나 변경된 스킬만 Claude에게 보내며, 압축(compaction) 시에는 스킬 목록을 자동으로 다시 보냅니다 | 스킬 관리 |
| `/workflows` | 실행 중 및 완료된 동적 워크플로 실행 내역 표시 (v2.1.154) | 멀티 에이전트 오케스트레이션 |
| `/release-notes` | 릴리스 노트 표시 | 새로운 기능 확인 |
| `/remote-control` | 원격 제어 활성화 | 원격 접속 |
| `/permissions` | 권한 관리 | 접근 권한 제어 |
| `/auto-mode-setup` | 프로젝트와 최근 세션을 바탕으로 `autoMode.environment` 항목 초안을 만들고, 검토한 뒤 사용자 설정에 저장. Pro/Max/Team은 v2.1.228+(네이티브 Windows는 v2.1.233+), Enterprise 또는 Console API 키는 v2.1.283+, Bedrock·Vertex·Foundry 및 원격 측정이 꺼진 세션은 v2.1.304+. 클라우드 세션에서는 사용 불가 | 자동 모드에 환경 정보 알려 주기 |
| `/rename` | 현재 세션 이름 변경 | 세션 정리 |
| `/resume` | 이전 세션 이어서 작업 | 작업 계속하기 |
| `/tui [default\|fullscreen]` | 터미널 UI 렌더러 설정(`fullscreen` = 깜빡임 없는 대체 화면). 인수 없는 `/tui`는 현재 렌더러를 출력 | 전체 화면/tmux에서 깜빡임 없는 렌더링 |
| `/tasks` | 백그라운드 작업 표시 | 비동기 작업 모니터링 |
| `/schedule [description]` | 일정, API 호출 또는 GitHub 이벤트에 따라 Anthropic 클라우드에서 실행되는 클라우드 예약 작업(이전 이름 routines)을 생성, 수정, 조회, 실행. 별칭: `/routines` | 내 컴퓨터 없이 실행되는 반복 자동화 |
| `/copy` | 마지막 응답을 클립보드로 복사 | 출력물 빠르게 공유 |
| `/teleport` (별칭 `/tp`) | 웹의 Claude Code 세션을 이 터미널에서 재개. 선택기를 엽니다. claude.ai 구독 필요 | 원격으로 작업 이어가기 |
| `/desktop` | Claude Desktop 앱 열기 | 데스크톱 인터페이스로 전환 |
| `/theme` | 색상 테마 변경. v2.1.118부터 `~/.claude/themes/<name>.json`의 사용자 정의 테마 지원(플러그인은 `themes/` 디렉터리를 포함 가능) | 화면 테마 사용자 지정 |
| `/usage` | 사용량/비용/통계를 통합한 공식 명령어(`/cost`와 `/stats`를 탭 하나로 통합, v2.1.118). v2.1.149부터 비용을 범주별(스킬, 서브에이전트, 플러그인, MCP 서버별)로 구분하여 표시. **VSCode 확장**(v2.1.174)에서는 `/usage`(Account & usage) 대화상자에 캐시 미스, 긴 컨텍스트 비용, 서브에이전트, 스킬/에이전트/플러그인/MCP별 24시간 및 7일 사용량 분석이 추가됨. v2.1.305부터 각 `/usage` 권장 사항은 한 줄짜리 수정 방법이며, `f`를 누르면 적용 가능한 항목을 적용합니다(같은 수정 사항이 `/doctor`와 VS Code 대화상자에도 표시됨) | 사용량 및 비용 모니터링 |
| `/focus` | 집중 보기 모드 전환(방해 요소 없는 출력 표시) | 긴 작업 중 화면 잡음 최소화 |
| `/fork` | 대화를 새로운 독립 백그라운드 세션으로 복사 (v2.1.212+) | 대안을 병렬로 탐색 |
| `/subtask` | 대화를 상속하고 결과를 보고하는 포크된 서브에이전트 생성 (v2.1.212+) | 현재 위치를 잃지 않고 부수 작업 위임 |
| `/stats` | `/usage`의 통계 탭을 여는 단축 별칭 (v2.1.118+) | 세션 통계 확인 |
| `/statusline` | 상태 표시줄 구성 | 상태 표시 사용자 지정 |
| `/stickers` | Claude Code 스티커 주문 | 재미 요소 |
| `/fast` | 빠른 출력 모드 전환. **Opus 5.5**(v2.1.280부터 기본값), **Opus 5, Opus 4.8**에 적용 | 응답 속도 향상 |
| `/terminal-setup` | 터미널 연동 설정 | 터미널 기능 설정 |
| `/undo` | `/rewind`의 별칭 (v2.1.108) | `/rewind`와 동일 |
| `/upgrade` | 상위 플랜으로 전환하는 업그레이드 페이지 열기 | 플랜 업그레이드 |
| `/team-onboarding` | 현재 프로젝트의 Claude Code 사용 내역을 기반으로 팀원 온보딩 가이드 생성 | 신규 팀원 온보딩 (v2.1.101) |
| `/code-review ultra` | 현재 변경 사항에 대해 클라우드 기반 멀티 에이전트 코드 리뷰 실행. `/ultrareview`는 별칭으로 남아 있으며 `/code-review ultra`가 권장 호출 방식입니다. Pro와 Max에서 무료 3회 실행 후에는 사용량 크레딧이 필요합니다 | 여러 에이전트를 통한 병합 전 심층 리뷰 (v2.1.112) |
| `/fewer-permission-prompts` | 대화 기록을 분석하여 자주 사용하는 읽기 전용 도구의 허용 목록을 우선순위에 따라 제안 | 프로젝트에서 반복적인 권한 요청 감소 (v2.1.112) |
| `/skill-doctor` | 로드된 스킬 중 사용되지 않는 스킬과 그 컨텍스트 비용 표시. `/plugin` 관리자의 **Stats** 탭에서 열리며 `-p`에서는 텍스트로 출력 | 더 이상 필요 없는 스킬 정리 (v2.1.252+) |

### 사용자 정의 명령어 (예시)

| Command | Description | When to Use | Scope | Installation |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | 코드 최적화 분석 | 성능 개선 | 프로젝트 | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | Pull Request 준비 | PR 제출 전 | 프로젝트 | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | API 문서 생성 | API 문서화 | 프로젝트 | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | 컨텍스트를 반영한 Git 커밋 생성 | 변경 사항 커밋 | 사용자 | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | 스테이징, 커밋 및 푸시 수행 | 빠른 배포 | 사용자 | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | 문서 구조 재구성 | 문서 개선 | 프로젝트 | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | CI/CD 파이프라인 설정 | 신규 프로젝트 | 프로젝트 | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | 테스트 커버리지 확장 | 테스트 품질 향상 | 프로젝트 | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **Scope**: `User` = 개인 워크플로(`~/.claude/commands/`), `Project` = 팀 공유(`.claude/commands/`)

**참고 자료**: [01-slash-commands/](01-slash-commands/) | [Official Docs](https://code.claude.com/docs/en/interactive-mode)

**빠른 설치(모든 사용자 정의 명령어)**:
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## Permission Modes

Claude Code는 도구 사용 권한을 제어하는 6가지 권한 모드를 지원합니다.

| Mode | Description | When to Use |
|------|-------------|-------------|
| `manual` | 모든 도구 호출 시마다 권한 요청 | 모든 작업을 직접 검토할 때(v2.1.200부터 Manual로 표시되며, 구성 값은 여전히 `default`이고 `manual`은 별칭). v2.1.283부터 대화형 터미널과 VS Code 세션의 기본 시작 모드는 auto입니다. `claude -p`와 Agent SDK 실행은 v2.1.302부터 Manual로 시작하므로, 무언가가 승인하지 않는 한 승인이 필요한 호출은 거부됩니다 |
| `acceptEdits` | 파일 수정은 자동 승인하고 나머지는 권한 요청 | 신뢰할 수 있는 편집 워크플로 |
| `plan` | 조사 후 계획을 제안하며, 승인하기 전까지 소스를 편집하지 않음 | 계획 수립 및 탐색 |
| `auto` | 백그라운드 안전 분류기 검사와 함께 모든 작업 수행 | 긴 작업, 프롬프트 피로 감소 |
| `bypassPermissions` | 모든 권한 확인 건너뛰기 | CI/CD, 헤드리스 환경 |
| `dontAsk` | 권한이 필요한 도구는 건너뜀 | 비대화형 스크립트 |

> **참고**: `auto` 모드를 사용하려면 자격 요건을 갖춘 플랜, 모델, 공급자가 필요합니다. [09-advanced-features/](09-advanced-features/README.md#자동-모드)를 참고하세요. `bypassPermissions`는 신뢰할 수 있는 샌드박스 환경에서만 사용해야 합니다.

**참고 자료**: [Official Docs](https://code.claude.com/docs/en/permissions)

---

## Subagents

특정 작업을 위해 독립된 컨텍스트를 사용하는 전문 AI 보조 에이전트입니다.

> **중첩 생성은 기본적으로 켜져 있으며 깊이는 3 (v2.1.219)**: 서브에이전트는 주 대화 아래 세 단계까지 자체 서브에이전트를 생성할 수 있습니다. 제한을 바꾸려면 `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`를 설정하고, 중첩을 끄려면 `1`로 설정합니다. (이력: v2.1.172–v2.1.216은 변경할 방법 없이 기본적으로 최대 5단계까지 중첩, v2.1.217은 깊이 1의 옵트인 방식으로 변경, v2.1.219는 기본값을 3으로 설정.) 특정 서브에이전트가 생성할 수 있는 서브에이전트를 제한하는 `Agent(agent_type)` 문법은 [04-subagents/README.md](04-subagents/README.md#생성-가능한-서브에이전트-제한)를 참고하세요.

### 기본 제공 서브에이전트

| Agent | Description | Tools | Model | When to Use |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | 다단계 작업, 조사 | 모든 도구 | 상위 모델 상속 | 복잡한 조사, 다중 파일 작업 |
| **Plan** | 구현 계획 수립 | Read, Glob, Grep, Bash | 상위 모델 상속 | 아키텍처 설계, 계획 수립 |
| **Explore** | 코드베이스 탐색 | Read, Glob, Grep | 상속(최대 Opus) | 빠른 검색, 코드 이해 |
| **claude** | 더 전문화된 에이전트에 맞지 않는 작업을 처리하는 범용 에이전트 | 모든 도구 | 상위 모델 상속 | 전문 에이전트가 없는 작업, 디스패치된 백그라운드 세션의 기본 에이전트 |
| **statusline-setup** | 상태 표시줄 구성 | Bash, Read, Write | Sonnet | 상태 표시줄 설정 |
| **claude-code-guide** | 도움말 및 문서 | Read, Glob, Grep | Haiku | 도움말 확인, 기능 학습 |

### 서브에이전트 설정 필드

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | 에이전트 식별자 |
| `description` | string | 에이전트의 역할 |
| `model` | string | 사용할 모델 재정의(`sonnet`, `opus`, `haiku`, `fable`, 전체 모델 ID 또는 `inherit`) |
| `tools` | array | 허용된 도구 목록 |
| `effort` | string | effort 수준(`low`, `medium`, `high`, `xhigh`, `max`. 모델에 따라 다름) |
| `initialPrompt` | string | 에이전트가 주 세션 에이전트(`--agent`)로 실행될 때 자동 제출되는 첫 사용자 턴 |
| `disallowedTools` | array | 이 에이전트에 명시적으로 금지된 도구 목록 |

### 사용자 정의 서브에이전트 (예시)

| Agent | Description | When to Use | Scope | Installation |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | 종합 코드 품질 검토 | 코드 리뷰 | 프로젝트 | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `clean-code-reviewer` | Clean Code 원칙 기반 리뷰 | 유지보수성 검토 | 프로젝트 | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | 테스트 전략 및 커버리지 | 테스트 계획 | 프로젝트 | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | 기술 문서 작성 | API 문서, 가이드 | 프로젝트 | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | 보안 중심 코드 리뷰 | 보안 감사 | 프로젝트 | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | 전체 기능 구현 | 기능 개발 | 프로젝트 | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | 근본 원인 분석 | 버그 조사 | 사용자 | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL 쿼리 및 데이터 분석 | 데이터 작업 | 사용자 | `cp 04-subagents/data-scientist.md .claude/agents/` |
| `performance-optimizer` | 프로파일링 및 성능 튜닝 | 병목 분석 | 프로젝트 | `cp 04-subagents/performance-optimizer.md .claude/agents/` |

> **Scope**: `User` = 개인(`~/.claude/agents/`), `Project` = 팀 공유(`.claude/agents/`)

**참고 자료**: [04-subagents/](04-subagents/) | [Official Docs](https://code.claude.com/docs/en/sub-agents)

**빠른 설치(모든 사용자 정의 에이전트)**:
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## Skills

지침, 스크립트, 템플릿을 포함하며 필요 시 자동으로 호출되는 기능입니다.

### 예시 스킬

| Skill | Description | When Auto-Invoked | Scope | Installation |
|-------|-------------|-------------------|-------|--------------|
| `code-review-specialist` | 종합 코드 리뷰 | "Review this code", "Check quality" | 프로젝트 | `cp -r 03-skills/code-review-specialist .claude/skills/` |
| `brand-voice` | 브랜드 일관성 검사 | 마케팅 문서 작성 | 프로젝트 | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | API 문서 생성 | "Generate docs", "Document API" | 프로젝트 | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | Martin Fowler 방식의 체계적인 코드 리팩터링 | "Refactor this", "Clean up code" | 사용자 | `cp -r 03-skills/refactor ~/.claude/skills/` |
| `claude-md` | CLAUDE.md 파일 생성 또는 갱신 | "Create CLAUDE.md", "Audit CLAUDE.md" | 프로젝트 | `cp -r 03-skills/claude-md .claude/skills/` |
| `blog-draft` | 아이디어와 자료로 블로그 게시물 초안 작성 | "Write a blog post", "Draft an article" | 사용자 | `cp -r 03-skills/blog-draft ~/.claude/skills/` |

> **Scope**: `User` = 개인(`~/.claude/skills/`), `Project` = 팀 공유(`.claude/skills/`)

### Skill Structure

```
~/.claude/skills/skill-name/
├── SKILL.md          # 스킬 정의 및 지침
├── scripts/          # 보조 스크립트
└── templates/        # 출력 템플릿
```

### Skill Frontmatter Fields

스킬은 `SKILL.md`에서 설정을 위한 YAML 프런트매터를 지원합니다.

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | 스킬 표시 이름 |
| `description` | string | 스킬의 기능 설명 |
| `when_to_use` | string | `description`에 덧붙는 트리거 문구 또는 요청 예시 |
| `effort` | string | effort 수준(`low`, `medium`, `high`, `xhigh`, `max`. 모델에 따라 다름) |
| `shell` | string | 인라인 `` !`command` `` 블록에 사용할 셸(기본값 `bash`, 또는 `powershell`) |

**참고 자료**: [03-skills/](03-skills/) | [Official Docs](https://code.claude.com/docs/en/skills)

**빠른 설치(모든 스킬)**:
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### 기본 제공 스킬

| Skill | Description | When Auto-Invoked |
|-------|-------------|-------------------|
| `/artifact-capabilities` | 게시된 아티팩트가 사용할 수 있는 런타임 기능(커넥터, 파일 다운로드)에 대한 참조 자료 로드 | 이러한 기능을 사용하는 아티팩트 페이지를 만들기 전 |
| `/artifact-diagramming` *(v2.1.221+)* | 아티팩트용 다이어그램 가이드 로드: 다이어그램이 도움이 되는 경우, 무엇을 그릴지, 라이트·다크 테마에서 모두 읽기 쉬운 인라인 SVG | 아티팩트에 다이어그램을 그릴 때 |
| `/batch` | 큰 변경을 5–30개의 독립 단위로 나누고, 각 단위를 자체 worktree의 백그라운드 서브에이전트가 실행 | 대규모 병렬 리팩터링 |
| `/claude-api [subcommand]` | Claude API를 사용한 애플리케이션 개발. 하위 명령어로 `migrate`, `api-version`(코드를 `2026-10-21` 같은 최신 API 버전으로 갱신, v2.1.307+), `managed-agents-secure`(Managed Agents 에이전트 설정을 Anthropic 보안 가이드와 비교, `ant` CLI 필요, v2.1.304+)가 있음 | API 개발 |
| `/claude-in-chrome [task]` | Claude in Chrome을 통해 브라우저에서 작업 수행(페이지 테스트, 양식 작성, 콘솔 로그 읽기). Chrome 연동이 활성화된 경우 사용 가능 | 브라우저 작업 |
| `/dataviz [request]` | 차트, 그래프, 대시보드 디자인 가이드: 차트 형태, 역할별 색상, 색맹 안전성과 대비를 위한 팔레트 검증 | 차트나 대시보드를 만들 때 |
| `/debug [description]` | 세션의 디버그 로깅을 켜고 세션 디버그 로그로 문제 해결 | Claude Code 자체 디버깅 |
| `/design` *(v2.1.265+)* | 여러 아트보드로 구성된 디자인 캔버스 생성 — UI 목업, 화면 흐름, 랜딩 페이지, 포스터 — 코드가 아닌 시각적으로 다듬음. Pro/Max/Team/Enterprise | HTML보다 직접 다듬고 싶은 화면이나 페이지를 디자인할 때 |
| `/design-sync [hint]` | 저장소의 React 디자인 시스템을 변환해 Claude Design에 업로드하여 실제 컴포넌트로 디자인하게 함. Anthropic API 전용. 독립형 Claude Design(claude.ai/design)은 2026년 12월 14일에 종료됩니다. | 디자인 시스템을 Claude Design에 동기화할 때 |
| `/design-login` | `/design-sync`용 디자인 시스템 접근 권한 부여(2026년 12월 14일까지 종료되는 독립형 claude.ai/design 사이트에 로그인) | `/design-sync` 실행 전 |
| `/design consent`, `/design revoke` | Claude에게 Claude Design 접근 권한을 부여하거나 철회. Claude가 `/design consent` 실행을 요청하면 프롬프트에 직접 입력하세요 | Claude Design 접근 권한 부여 또는 해제 |
| `/doctor [prompt-audit [path]]` | 설치, 설정, 확장 기능, `CLAUDE.md` 문제를 진단하고 수정 방법을 제안하는 설정 점검. 별칭: `/checkup` | 설정 문제 해결 |
| `/fewer-permission-prompts` | 대화 기록을 분석하여 우선순위가 지정된 허용 목록 제안 | 반복적인 권한 요청 감소 |
| `/loop` | 일정 간격으로 프롬프트 실행 | 반복 작업 |
| `/run` *(v2.1.145+)* | 프로젝트 애플리케이션을 실행하여 변경 사항 확인 | 실제 애플리케이션에서 변경 사항 검증 |
| `/run-skill-generator` *(v2.1.145+)* | 특정 프로젝트에서 `/run`/`/verify`를 사용할 수 있도록 설정 | `/run` 최초 프로젝트 설정 |
| `/code-review [low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [pr#\|branch\|path]` | 현재 diff 또는 PR, 브랜치, 경로를 검토하여 정확성 버그 확인. `--fix`는 발견 사항을 적용하고 `--comment`는 PR 인라인 댓글로 게시. 수준을 지정하지 않으면 마지막으로 입력한 수준을 재사용(v2.1.223). 낮은 effort 수준은 v2.1.218에서 **백그라운드 서브에이전트**로 옮겨졌고 `high`, `xhigh`, `max`도 v2.1.232에서 뒤따라, 리뷰 출력이 더 이상 대화를 채우지 않음 | 코드 작성 후, PR 병합 전 |
| `/slides [brief]` *(v2.1.265+)* | 브리프를 바탕으로 Claude Slides 아티팩트로 새 프레젠테이션 생성. 아티팩트와 Slides 템플릿 필요 | 슬라이드 덱 만들기 |
| `/simplify` *(v2.1.154부터 다시 독립 기능)* | 정리만 수행하는 리뷰(재사용, 단순화, 효율성, 추상화 수준)를 실행하고 수정 사항을 적용. 버그 탐지는 수행하지 않음 | 버그 탐지 없이 코드 정리 |
| `/update-config [request]` | 설정 변경 내용(명령어 허용, 환경 변수 설정, 훅 추가)을 설명하면 Claude가 해당 `settings.json`을 편집 | JSON을 직접 편집하지 않고 설정 변경 |
| `/verify` *(v2.1.145+)* | 애플리케이션을 빌드, 실행 및 확인하여 수정 사항이 제대로 동작하는지 검증 | 수정 사항의 전체 동작 검증 |
| `/workflow-authoring` *(v2.1.248+)* | 동적 워크플로 스크립트 작성용 참조 자료(스크립트 API, 재개, 품질 패턴) 로드. 동적 워크플로가 활성화된 경우 사용 가능 | 워크플로 스크립트 작성 또는 편집 |

---

## Plugins

명령어, 에이전트, MCP 서버 및 훅을 묶어서 제공하는 기능 모음입니다.

### 플러그인 예시

| Plugin | Description | Components | When to Use | Scope | Installation |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | PR 리뷰 워크플로 | 명령어 3개, 에이전트 3개, GitHub MCP | 코드 리뷰 | 프로젝트 | `claude --plugin-dir ./07-plugins/pr-review` |
| `devops-automation` | 배포 및 모니터링 | 명령어 4개, 에이전트 3개, K8s MCP | DevOps 작업 | 프로젝트 | `/plugin install devops-automation` |
| `documentation` | 문서 생성 모음 | 명령어 4개, 에이전트 3개, 템플릿 | 문서 작성 | 프로젝트 | `/plugin install documentation` |

> **Scope**: `Project` = 팀 공유, `User` = 개인 워크플로

### 플러그인 구조

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json   # 매니페스트 파일(.claude-plugin/ 안의 유일한 파일)
├── commands/         # 슬래시 명령어
├── agents/           # 서브에이전트
├── skills/           # 스킬(<name>/SKILL.md)
├── hooks/
│   └── hooks.json    # 훅 구성
├── .mcp.json         # MCP 구성
├── bin/              # 실행 파일
└── scripts/          # 유틸리티 스크립트
```

**참고 자료**: [07-plugins/](07-plugins/) | [Official Docs](https://code.claude.com/docs/en/plugins)

**플러그인 관리 명령어**:
```bash
/plugin list              # 설치된 플러그인 목록
/plugin install <name>    # 플러그인 설치
/plugin uninstall <name>  # 플러그인 제거
claude plugin update <name>   # 플러그인 업데이트(CLI. /plugin update 슬래시 형식은 본문에는 언급되지만 명령어 레퍼런스에는 없음)
```

---

## MCP Servers

외부 도구 및 API에 접근하기 위한 Model Context Protocol 서버입니다.

### 일반적으로 사용하는 MCP 서버

| Server | Description | When to Use | Scope | Installation |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | PR 관리, 이슈, 코드 | GitHub 워크플로 | 로컬 | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL 쿼리 및 데이터 접근 | 데이터베이스 작업 | 로컬 | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | 고급 파일 작업 | 복잡한 파일 작업 | 로컬 | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | 팀 커뮤니케이션 | 알림, 업데이트 | 프로젝트 | 설정에서 구성 |
| **Google Docs** | 문서 접근 | 문서 편집 및 검토 | 프로젝트 | 설정에서 구성 |
| **Asana** | 프로젝트 관리 | 작업 추적 | 프로젝트 | 설정에서 구성 |
| **Stripe** | 결제 데이터 | 재무 분석 | 프로젝트 | 설정에서 구성 |
| **Memory** | 영구 메모리 | 세션 간 기억 유지 | 사용자 | 설정에서 구성 |
| **Context7** | 라이브러리 문서 | 최신 문서 조회 | 사용자 | 설정에서 구성(타사 서버) |

> **Scope**: `Local` = `--scope` 없이 실행한 `claude mcp add`의 기본값(이 프로젝트에서 나만 사용, `~/.claude.json`), `Project` = 팀(`.mcp.json`, `--scope project`), `User` = 개인(`~/.claude.json`, `--scope user`), `Built-in` = 기본 제공

### MCP 설정 예시

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**참고 자료**: [05-mcp/](05-mcp/) | [MCP Protocol Docs](https://modelcontextprotocol.io)

**빠른 설치(GitHub MCP)**:
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## Hooks

Claude Code 이벤트 발생 시 셸 명령을 실행하는 이벤트 기반 자동화 기능입니다.

### Hook 이벤트

| Event | Description | When Triggered | Use Cases |
|-------|-------------|----------------|-----------|
| `SessionStart` | 세션 시작 또는 재개 | 세션 초기화 시 | 초기 설정 작업 |
| `Setup` | 저장소 설정 또는 유지 관리 실행 | `--init-only` 사용 시, 또는 `-p`와 함께 `--init`/`--maintenance` 사용 시에만 | 도구 준비, 의존성 설치 |
| `InstructionsLoaded` | 지침 로드 완료 | CLAUDE.md 또는 규칙 파일 로드 | 사용자 정의 지침 처리 |
| `UserPromptSubmit` | 프롬프트 처리 전(v2.1.299부터는 스킬이나 사용자 정의 명령어가 확장되기 전에도) | 사용자가 메시지를 전송할 때 | 입력 검증 |
| `UserPromptExpansion` | 입력한 슬래시 명령어(스킬, 사용자 정의 명령어, MCP 프롬프트)가 프롬프트로 확장됨 | `UserPromptSubmit` 이후, 확장된 프롬프트가 Claude에 전달되기 전 | `/command` 직접 사용 차단, 스킬별 컨텍스트 추가, 명령어 로깅 |
| `PreToolUse` | 도구 실행 전 | 모든 도구 실행 전 | 검증, 로깅 |
| `PermissionRequest` | 권한 요청 대화상자 표시 | 민감한 작업 전 | 사용자 정의 승인 절차 |
| `PermissionDenied` | 사용자가 권한 요청을 거부 | 권한 거부 후 | 로깅, 분석, 정책 적용 |
| `PostToolUse` | 도구 실행 성공 후 | 모든 도구 실행 완료 후 | 포맷팅, 알림 |
| `PostToolUseFailure` | 도구 실행 실패 | 도구 오류 발생 후 | 오류 처리, 로깅 |
| `PostToolBatch` | 도구 실행 묶음 완료 후 | 도구 배치 종료 시 | 집계 보고, 일괄 검증 |
| `Notification` | 알림 전송 | Claude가 알림을 보낼 때 | 외부 알림 |
| `MessageDisplay` | 어시스턴트 메시지 텍스트 표시 | 메시지가 렌더링되는 동안 | 표시 텍스트 변환 또는 숨김 |
| `SubagentStart` | 서브에이전트 생성 | 서브에이전트 작업 시작 | 서브에이전트 컨텍스트 초기화 |
| `SubagentStop` | 서브에이전트 종료 | 서브에이전트 작업 완료 | 후속 작업 실행 |
| `Stop` | Claude 응답 완료 | 응답 종료 | 정리 작업, 보고 |
| `StopFailure` | API 오류로 턴 종료 | API 오류 발생 | 오류 복구, 로깅 |
| `TeammateIdle` | 팀원 에이전트 대기 상태 | 에이전트 팀 협업 중 | 작업 분배 |
| `TaskCompleted` | 작업 완료 표시(todo 도구가 활성화된 경우에만 실행 — [Hooks](06-hooks/README.md#훅-이벤트) 참고) | 작업 완료 시 | 작업 후 처리 |
| `TaskCreated` | TaskCreate를 통해 작업 생성(todo 도구가 활성화된 경우에만 실행 — [Hooks](06-hooks/README.md#훅-이벤트) 참고) | 새 작업 생성 시 | 작업 추적, 로깅 |
| `ConfigChange` | 설정 변경 | 설정 수정 시 | 설정 변경 대응 |
| `CwdChanged` | 작업 디렉터리 변경 | 디렉터리 변경 시 | 디렉터리별 초기 설정 |
| `DirectoryAdded` | 세션 중 새 작업 디렉터리 등록 | `/add-dir` 또는 SDK `register_repo_root` | 새 디렉터리용 도구 설정 |
| `FileChanged` | 감시 중인 파일 변경 | 파일 수정 시 | 파일 모니터링, 재빌드 |
| `PreCompact` | Compact 작업 전 | 컨텍스트 압축 전 | 상태 보존 |
| `PostCompact` | Compact 작업 후 | 압축 완료 후 | 후처리 작업 |
| `PreModelSwitch` | 요청된 모델 전환이 적용되기 전 | 모델 전환 요청 시 | 모델 변경 제어 또는 거부 |
| `PostModelSwitch` | 세션 모델 변경 후 | 모델 전환 완료 시 | 모델 변경 로깅 또는 대응 |
| `WorktreeCreate` | Worktree 생성 | Git Worktree 생성 시 | Worktree 환경 설정 |
| `WorktreeRemove` | Worktree 제거 | Git Worktree 제거 시 | Worktree 리소스 정리 |
| `Elicitation` | MCP 서버가 사용자 입력 요청 | MCP 입력 요청 시 | 입력 검증 |
| `ElicitationResult` | 사용자가 입력 요청에 응답 | 사용자 응답 시 | 응답 처리 |
| `SessionEnd` | 세션 종료 | 세션 종료 시 | 정리 작업, 상태 저장 |

### Hook 예시

| Hook | Description | Event | Scope | Installation |
|------|-------------|-------|-------|--------------|
| `pre-tool-check.sh` | 위험한 Bash 명령어 차단/경고 | PreToolUse:Bash | 사용자 | `cp 06-hooks/pre-tool-check.sh ~/.claude/hooks/` |
| `security-scan.sh` | 보안 검사 | PostToolUse:Write | 프로젝트 | `cp 06-hooks/security-scan.sh .claude/hooks/` |
| `format-code.sh` | 자동 코드 포맷팅 | PostToolUse:Write | 사용자 | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.sh` | 프롬프트 검증 | UserPromptSubmit | 프로젝트 | `cp 06-hooks/validate-prompt.sh .claude/hooks/` |
| `context-tracker.py` | 토큰 사용량 추적 | UserPromptSubmit, Stop | 사용자 | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `context-tracker-tiktoken.py` | 토큰 사용량 추적(tiktoken, 정확도 약 90-95%) | UserPromptSubmit, Stop | 사용자 | `cp 06-hooks/context-tracker-tiktoken.py ~/.claude/hooks/` |
| `pre-commit.sh` | 커밋 전 검증 | PreToolUse:Bash | 프로젝트 | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | 명령 실행 로그 기록 | PostToolUse:Bash | 사용자 | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |
| `dependency-check.sh` | 매니페스트 변경 시 취약점 검사 | PostToolUse:Write | 프로젝트 | `cp 06-hooks/dependency-check.sh .claude/hooks/` |
| `notify-team.sh` | git push 시 팀 알림 | PostToolUse:Bash | 프로젝트 | `cp 06-hooks/notify-team.sh .claude/hooks/` |
| `session-end.sh` | 세션 종료 시 진행 상황 기록 | SessionEnd | 사용자 | `cp 06-hooks/session-end.sh ~/.claude/hooks/` |

> **Scope**: `Project` = 팀(`.claude/settings.json`), `User` = 개인(`~/.claude/settings.json`)

### Hook Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "~/.claude/hooks/pre-tool-check.sh" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          { "type": "command", "command": "~/.claude/hooks/format-code.sh" }
        ]
      }
    ]
  }
}
```

**참고 자료**: [06-hooks/](06-hooks/) | [Official Docs](https://code.claude.com/docs/en/hooks)

**빠른 설치(모든 Hook)**:
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## Memory Files

세션 간 자동으로 로드되는 영구 컨텍스트입니다.

### 메모리 유형

| Type | Location | Scope | When to Use |
|------|----------|-------|-------------|
| **Managed Policy** | 조직에서 관리하는 정책 | 조직 | 조직 전체 표준 적용 |
| **Project** | `./CLAUDE.md` | 프로젝트(팀) | 팀 표준 및 프로젝트 컨텍스트 |
| **Project Rules** | `.claude/rules/` | 프로젝트(팀) | 모듈형 프로젝트 규칙 |
| **User** | `~/.claude/CLAUDE.md` | 사용자(개인) | 개인 설정 및 선호 사항 |
| **User Rules** | `~/.claude/rules/` | 사용자(개인) | 모듈형 개인 규칙 |
| **Local** | `./CLAUDE.local.md` | 로컬(git 제외) | 머신별 로컬 재정의(git 추적 제외). 개발자별 재정의 파일로 https://code.claude.com/docs/en/memory 에 문서화되어 있습니다. |
| **Auto Memory** | 자동 | 세션 | 인사이트와 수정 사항 자동 저장 |

> **Scope**: `Organization` = 관리자가 관리, `Project` = Git을 통해 팀과 공유, `User` = 개인 설정, `Local` = 커밋되지 않음, `Session` = 자동 관리

**참고 자료**: [02-memory/](02-memory/) | [Official Docs](https://code.claude.com/docs/en/memory)

**빠른 설치**:
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## New Features

| Feature | Description | How to Use |
|---------|-------------|------------|
| **/focus** | 집중 보기를 전환하여 방해 요소 없이 출력 표시 (v2.1.110) | 긴 작업 중 시각적 방해를 줄이려면 `/focus` 실행 |
| **/proactive** | `/loop`의 별칭으로 동일한 반복 작업 동작 제공 (v2.1.105) | `/loop` 대신 `/proactive` 사용 가능 |
| **/recap** | 기존 세션으로 돌아왔을 때 작업 요약 표시 (v2.1.108) | 자리를 비운 뒤 `/recap` 실행 |
| **/tui** | 터미널 UI 렌더러 설정: 깜빡임 없는 렌더링은 `/tui fullscreen`, 되돌리려면 `/tui default`. 인수 없는 `/tui`는 현재 렌더러를 출력 (v2.1.110) | 전체 화면 터미널 또는 tmux에서 `/tui fullscreen` 사용 |
| **/undo** | `/rewind`의 별칭 (v2.1.108) | `/undo`, `/checkpoint`, `/rewind`를 같은 용도로 사용 |
| **Monitor Tool** | 폴링 대신 백그라운드 명령의 stdout 스트림을 감시하고 이벤트에 반응 (v2.1.98+) | [Advanced Features](09-advanced-features/)의 Monitor Tool 사용 |
| **Output Styles** | 시스템 프롬프트를 통해 Claude의 역할, 어조, 기본 응답 형식 변경. 기본 제공: Default, Proactive, Explanatory, Learning, Concise | `/config` → Output style, `outputStyle` 설정, 또는 `/output-style` 실행(v2.1.91에서 제거된 뒤 v2.1.269에서 다시 추가). [Advanced Features](09-advanced-features/README.md#출력-스타일) 참고 |
| **Status Line** | stdin으로 세션, 모델, 비용, 컨텍스트 JSON을 받는 명령어로 사용자 지정 상태 표시줄 렌더링 | `/statusline` 또는 `statusLine` 설정. [Advanced Features](09-advanced-features/README.md#상태-표시줄) 참고 |
| **Community Marketplace** | Anthropic의 자동 검증을 통과한 타사 플러그인으로, 각각 커밋 SHA에 고정됨 | `/plugin marketplace add anthropics/claude-plugins-community` 후 `/plugin install <name>@claude-community` |
| **/team-onboarding** | 프로젝트의 Claude Code 구성을 기반으로 팀원 온보딩 가이드 자동 생성 (v2.1.101) | 프로젝트에서 `/team-onboarding` 실행 |
| **Remote Control** | API를 통해 Claude Code 세션 원격 제어. **더 이상 리서치 프리뷰가 아님** — `claude remote-control`을 실행 중인 모든 머신이 Claude 앱 Code 탭에 디바이스 카드로 표시되어, 휴대폰에서 해당 머신의 세션을 시작할 수 있음 | 머신에서 `claude remote-control`을 실행한 다음 Claude 앱에서 디바이스 카드 선택. [Advanced Features](09-advanced-features/README.md) 참고 |
| **Web Sessions** | 클라우드 세션에서 Claude Code 실행 | `claude --cloud "task"` 또는 claude.ai/code에서 시작 |
| **Desktop App** | Claude Code 네이티브 데스크톱 애플리케이션 | `/desktop` 사용 또는 Anthropic 웹사이트에서 다운로드 |
| **Cross-Session Messaging** | 세션끼리 메시지를 주고받을 수 있으며, 다른 머신과 클라우드 세션도 포함. `ListAgents`로 검색 (macOS/Linux는 v2.1.224+, 네이티브 Windows는 v2.1.234+) | [Advanced Features](09-advanced-features/README.md#세션-간-메시징) 참고. 수신은 `crossSessionInbound`로 제어 |
| **Self-Hosted Runner** | Claude Code 웹, 모바일, 데스크톱 세션을 자체 머신이나 컨테이너에서 실행 (v2.1.224+, Team/Enterprise) | `claude self-hosted-runner setup`. [CLI](10-cli/README.md) 참고 |
| **`archive` plugin source** | HTTPS zip에서 플러그인 설치, 선택적으로 `sha256`으로 고정 (v2.1.224+) | [Plugins](07-plugins/README.md#archive-소스-v21224) 참고 |
| **`command` plugin source** | 로컬에 설치된 도구가 플러그인 디렉터리 경로를 출력 (v2.1.229+) | [Plugins](07-plugins/README.md#command-소스-v21229) 참고 |
| **Marketplace owner wildcards** | `"owner/*"`로 GitHub 소유자 아래의 모든 마켓플레이스 저장소를 허용하거나 차단 — `strictKnownMarketplaces`와 `blockedMarketplaces`에서만 (v2.1.223+) | [Plugins](07-plugins/README.md#마켓플레이스-구성) 참고 |
| **Sandbox credential masking** | 샌드박스 명령어는 센티널 값을 읽고, 프록시가 이그레스 시 실제 비밀 값으로 치환 (v2.1.221+, Linux/WSL) | [Advanced Features](09-advanced-features/README.md#자격-증명-마스킹-v21221-v21224) 참고 |
| **Agent Teams** | 관련 작업을 수행하는 여러 에이전트 협업 | 컨텍스트를 공유하며 협업하는 팀원 에이전트 구성 |
| **Task List** | 백그라운드 작업 관리 및 모니터링 | `/tasks`로 백그라운드 작업 확인 및 관리 |
| **Prompt Suggestions** | 컨텍스트 기반 명령어 추천 | 현재 컨텍스트에 따라 자동 표시 |
| **Git Worktrees** | 병렬 개발을 위한 독립된 Git Worktree | Worktree 명령으로 안전한 병렬 브랜치 작업 수행 |
| **Sandboxing** | 안전한 실행을 위한 격리 환경 | `/sandbox`로 전환하여 제한된 환경에서 실행 |
| **MCP OAuth** | MCP 서버용 OAuth 인증 | 안전한 접근을 위해 MCP 서버 설정에서 OAuth 자격 증명 구성 |
| **MCP Tool Search** | MCP 도구 동적 검색 및 탐색 | 연결된 서버에서 사용 가능한 MCP 도구 검색 |
| **Scheduled Tasks (session-scoped)** | 세션 안에서 `/loop`와 cron 도구로 반복 작업 설정. 클라우드 예약 작업(이전 이름 routines)은 `/schedule` 사용 | `/loop 5m /command` 또는 CronCreate 도구 사용 |
| **Chrome Integration** | Claude in Chrome 확장 프로그램을 통해 사용자의 Chrome/Edge(보이는 창, 사용자 로그인 상태) 조작 | `--chrome` 플래그 또는 `/chrome` 사용 |
| **Keyboard Customization** | 조합 키를 포함한 키 바인딩 사용자 지정 | `/keybindings` 또는 `~/.claude/keybindings.json` 수정 |
| **Auto Mode** | 백그라운드 안전 분류기 검사를 통한 완전 자율 실행 | `Shift+Tab`으로 순환 전환하거나 `--permission-mode auto` 사용 |
| **Channels** | 다중 채널 통신(Telegram, Slack 등) (Research Preview) | 채널 플러그인 구성. 2026년 3월 |
| **Voice Dictation** | 프롬프트 음성 입력 | 마이크 아이콘 또는 음성 단축키 사용 |
| **Agent Hook Type** | 셸 명령 대신 서브에이전트를 실행하는 Hook | Hook 설정에서 `"type": "agent"` 지정 |
| **Prompt Hook Type** | Claude 모델에 프롬프트를 보내 단일 턴으로 평가하는 Hook. 모델은 결정을 JSON으로 반환 | Hook 설정에서 `"type": "prompt"` 지정 |
| **MCP Elicitation** | 도구 실행 중 MCP 서버가 사용자 입력 요청 가능 | `Elicitation` 및 `ElicitationResult` Hook 이벤트 처리 |
| **Plugin LSP Support** | 플러그인을 통한 Language Server Protocol 연동 | 에디터 기능을 위해 `plugin.json`에서 LSP 서버 구성 |
| **Managed Drop-ins** | 조직에서 관리하는 Drop-in 구성 (v2.1.83) | 관리 정책으로 설정되며 모든 사용자에게 자동 적용 |
| **`claude plugin init`** | `.claude/skills`에 새 플러그인 골격 생성. 마켓플레이스 없이 자동 로드됨 (v2.1.157) | `claude plugin init <name>` 실행 |
| **Auto Mode on third-party providers** | Amazon Bedrock, Google Cloud Agent Platform, Microsoft Foundry, 로그인한 Claude apps 게이트웨이 세션에서 기본적으로 사용 가능. 지원 모델은 Claude Sonnet 5 이상, Opus 4.7 이상, Haiku 5.5(v2.1.293+), Fable 모델 (v2.1.158–v2.1.206에서는 옵트인 필요, v2.1.207에서 제거 — `CLAUDE_CODE_ENABLE_AUTO_MODE`는 여전히 허용되지만 효과 없음) | `Shift+Tab`으로 순환 전환하거나 `--permission-mode auto` 사용 |
| **Immediate Dialog Commands** | Claude가 작업 중일 때도 `/permissions`를 열 수 있고(규칙 변경은 해당 턴의 나머지에 적용), `/add-dir`, `/autocompact`, `/theme`, `/help`, `/config`, `/advisor` 대화상자는 **전체 화면 TUI에서** Claude의 응답이 끝날 때까지 대기하지 않고 턴 중간에 열림(`/bug`는 v2.1.232부터 이미 이렇게 동작) (v2.1.234) | Claude가 작업 중일 때 이 명령어 중 하나 실행. [Slash Commands](01-slash-commands/README.md) 참고 |
| **`CLAUDE_CODE_PROJECT_DIR_NAME`** | 프로젝트별 트랜스크립트 디렉터리 이름을 제어하는 환경 변수 (v2.1.234) | Claude Code 실행 전에 셸/환경에서 설정. `CLAUDE_CONFIG_DIR`도 설정하지 않으면 무시됨. [CLI](10-cli/README.md) 참고 |
| **Goal Check-In Threshold** | `/goal`이 활성화된 동안 백그라운드 작업이 30분 이상 진척이 없으면, Claude가 조용히 계속하지 않고 상태 업데이트로 확인을 요청. `CLAUDE_CODE_GOAL_CHECKIN_MINUTES`로 조정하며 `0`으로 설정하면 비활성화 (v2.1.234) | 활성화된 `/goal`과 함께 `CLAUDE_CODE_GOAL_CHECKIN_MINUTES=<n>` 설정. [Slash Commands](01-slash-commands/README.md) 참고 |
| **Usage-Limit Auto-Continue** | claude.ai 사용량 한도에 막혀 있던 세션은 한도가 초기화되면 Claude Code가 자동으로 이어서 진행 (v2.1.234) | 기본적으로 켜져 있음. `/config` → "Continue automatically at usage limit"에서 끄기. [Advanced Features](09-advanced-features/) 참고 |
| **`spellcheck` setting** | `PATH`에 있는 aspell, hunspell, ispell 중 하나를 사용해 프롬프트 입력의 철자 오류에 밑줄 표시. 기본적으로 꺼짐 (v2.1.235) | 검사기를 설치한 뒤 `~/.claude/settings.json`에 `"spellcheck": { "enabled": true }` 설정. 사용자, `--settings`, 관리되는 설정에서만 동작하며 프로젝트 설정에서는 무시됨. [Advanced Features](09-advanced-features/) 참고 |
| **Agent Teams Default Model** | `/config`의 "Default teammate model" 설정이 제거됨. 생성 호출에서 명시적으로 지정하지 않으면 팀원은 이제 기본적으로 팀 리더의 모델을 상속 (v2.1.234) | [Subagents — Agent Teams](04-subagents/README.md#에이전트-팀-실험적) 참고 |
| **`/design`** | 디자인 캔버스 — 아티팩트 위에 만들어지고 코드가 아닌 시각적으로 다듬는 여러 아트보드 기반 시각 디자인(UI 목업, 화면 흐름, 랜딩 페이지, 포스터). v2.1.265+ 필요, Pro/Max/Team/Enterprise | CLI 또는 Desktop 앱에서 `/design` 실행. [Slash Commands](01-slash-commands/README.md) 참고 |
| **`notify_when_idle`** | 같은 머신의 다른 세션에 다음 번 유휴 상태가 될 때 알림을 한 번 보내 달라고 요청하는 세션 간 `SendMessage` 입력 — 옵트인, 일회성, 폴링 없음 (v2.1.236). 관련: `ListAgents`가 세션 자신의 이름을 보고하고 실행 중인 팀원 목록을 표시하며, Windows에서도 세션 간 메시징 지원 (v2.1.239) | `SendMessage`에 `notify_when_idle` 전달. [Advanced Features](09-advanced-features/README.md#세션-간-메시징) 참고 |
| **Plugin manifest fields** | `plugin.json`이 `workflows`, `channels`, `dependencies`(semver), `outputStyles`, `keywords`, `metadata`, `lspServers`, `experimental.themes` / `experimental.monitors`를 지원. CLI에는 `claude plugin new`, `remove`/`rm`, `prune`/`autoremove`와 `--with`, `-f`/`--force`, `--available`, `--push`, `--dry-run` 플래그가 추가됨 | [Plugins](07-plugins/README.md) 참고 |
| **Restricted Mode** | `--tools`가 개별적으로 지정하지 않는 한(`default` 프리셋으로는 안 됨) 명령어나 코드를 실행하는 기본 제공 도구(Bash, PowerShell 등)와 WebFetch를 제거하고, 사용자·프로젝트·로컬 설정을 무시하며(관리되는 설정과 `--settings`는 계속 적용), 파일 도구를 작업 디렉터리로 제한하고, `bypassPermissions`를 거부하며, 클라우드 세션 생성을 거부 (v2.1.248+) | `claude --restricted` 또는 `CLAUDE_CODE_RESTRICTED=1`. [CLI](10-cli/README.md) 참고 |
| **`/advisor` text form** | `/advisor`, `/advisor <model>`, `/advisor off`가 대화상자뿐 아니라 데스크톱 앱, Remote Control, 기타 헤드리스(`-p` / Agent SDK) 세션에서 텍스트 명령어로 동작 (v2.1.260+) | 헤드리스 세션에서 `/advisor off` 입력. [Slash Commands](01-slash-commands/README.md) 참고 |

---

## Quick Reference Matrix

### 기능 선택 가이드

| Need | Recommended Feature | Why |
|------|---------------------|-----|
| 빠른 단축 작업 | Slash Command | 수동 실행, 즉시 동작 |
| 지속적인 컨텍스트 | Memory | 자동 로드 |
| 복잡한 자동화 | Skill | 자동 호출 |
| 전문 작업 | Subagent | 독립된 컨텍스트 |
| 외부 데이터 | MCP Server | 실시간 접근 |
| 이벤트 자동화 | Hook | 이벤트 기반 실행 |
| 통합 솔루션 | Plugin | 올인원 번들 |

### 설치 우선순위

| Priority | Feature | Command |
|----------|---------|---------|
| 1. 필수 | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. 일상 사용 | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. 품질 향상 | Subagents | `cp 04-subagents/*.md .claude/agents/` |
| 4. 자동화 | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. 외부 연동 | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. 고급 기능 | Skills | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. 통합 기능 | Plugins | `claude --plugin-dir ./07-plugins/pr-review` |

---

## Complete One-Command Installation

이 저장소의 모든 예제를 한 번에 설치합니다.

```bash
# 디렉터리 생성
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# 모든 기능 설치
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## Additional Resources

- [Official Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Learning Roadmap](LEARNING-ROADMAP.md)
- [Main README](README.md)

---

**최종 업데이트**: 2026년 10월 26일
**Claude Code 버전**: 2.1.310
**출처**:
- https://code.claude.com/docs/en/sub-agents
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/changelog#2-1-172
- https://code.claude.com/docs/en/changelog#2-1-174
- https://github.com/anthropics/claude-code/releases/tag/v2.1.145
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/plugin-marketplaces
- https://code.claude.com/docs/en/discover-plugins
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/slash-commands
- https://code.claude.com/docs/en/fast-mode
- https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/chrome
- https://code.claude.com/docs/en/skills#bundled-skills
- https://code.claude.com/docs/en/plugins/manifest-reference
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/env-vars
- https://code.claude.com/docs/en/cross-session-messaging
- https://support.claude.com/en/articles/17440474-migrate-from-standalone-claude-design-to-claude
- https://code.claude.com/docs/en/permission-modes#which-mode-a-session-starts-in
- https://code.claude.com/docs/en/changelog#2-1-305
- https://code.claude.com/docs/en/costs#apply-recommendations-with-the-fix-shortcut
- https://code.claude.com/docs/en/changelog#2-1-304
- https://code.claude.com/docs/en/commands#all-commands
- https://code.claude.com/docs/en/context-window#what-survives-compaction
- https://code.claude.com/docs/en/changelog#2-1-307
- https://code.claude.com/docs/en/skills#work-on-claude-api-projects
- https://code.claude.com/docs/en/routines
- https://code.claude.com/docs/en/auto-mode-config#generate-environment-entries-with-auto-mode-setup
- https://code.claude.com/docs/en/scheduled-tasks
**호환 모델**: Claude Fable 5.1, Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
