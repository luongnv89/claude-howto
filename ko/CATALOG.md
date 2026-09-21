<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 기능 카탈로그

> Claude Code의 모든 기능(명령어, 에이전트, 스킬, 플러그인, 훅)에 대한 빠른 참조 가이드입니다.

**탐색**: [Commands](#slash-commands) | [Permission Modes](#permission-modes) | [Subagents](#subagents) | [Skills](#skills) | [Plugins](#plugins) | [MCP Servers](#mcp-servers) | [Hooks](#hooks) | [Memory](#memory-files) | [New Features](#new-features-may-2026)

---

## 요약

| Feature | Built-in | Examples | Total | Reference |
|---------|----------|----------|-------|-----------|
| **Slash Commands** | 60+ | 8 | 68+ | [01-slash-commands/](01-slash-commands/) |
| **Subagents** | 6 | 11 | 17 | [04-subagents/](04-subagents/) |
| **Skills** | 기본 제공 9개 | 6 | 15 | [03-skills/](03-skills/) |
| **Plugins** | - | 3 | 3 | [07-plugins/](07-plugins/) |
| **MCP Servers** | 1 | 8 | 9 | [05-mcp/](05-mcp/) |
| **Hooks** | 이벤트 29개 | 8 | 8 | [06-hooks/](06-hooks/) |
| **Memory** | 유형 7개 | 3 | 3 | [02-memory/](02-memory/) |
| **합계** | **103** | **47** | **125** | |

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
| `/diff` | 대화형 diff 뷰어 | 변경 사항 검토 |
| `/config` | 설정 조회/수정 | 동작 사용자 지정 |
| `/status` | 세션 상태 표시 | 현재 상태 확인 |
| `/agents` | 사용 가능한 에이전트 목록 표시 | 위임 가능한 에이전트 확인 |
| `/skills` | 사용 가능한 스킬 목록 표시 | 자동 호출 기능 확인 |
| `/hooks` | 구성된 훅 목록 표시 | 자동화 디버깅 |
| `/insights` | 세션 패턴 분석 | 세션 최적화 |
| `/install-slack-app` | Claude Slack 앱 설치 | Slack 연동 |
| `/keybindings` | 키보드 단축키 사용자 지정 | 단축키 설정 |
| `/mcp` | MCP 서버 목록 표시 | 외부 연동 확인 |
| `/memory` | 로드된 메모리 파일 표시 | 컨텍스트 로딩 디버깅 |
| `/mobile` | 모바일 QR 코드 생성 | 모바일 접속 |
| `/passes` | 사용 패스 조회 | 구독 정보 확인 |
| `/plugin` | 플러그인 관리 | 확장 기능 설치/제거 |
| `/plan` | 계획 모드 진입 | 복잡한 구현 작업 |
| `/proactive` | `/loop`의 별칭 (v2.1.105) | `/loop`와 동일 |
| `/recap` | 세션에 다시 돌아왔을 때 요약 표시 | 자리를 비운 후 작업 내용 확인 |
| `/rewind` | 체크포인트로 되돌리기 | 변경 사항 취소, 대안 탐색 |
| `/checkpoint` | 체크포인트 관리 | 상태 저장/복원 |
| `/cost` | `/usage`의 비용 탭을 여는 단축 별칭 (v2.1.118+) | 비용 모니터링 |
| `/context` | 컨텍스트 창 사용량 표시 | 대화 길이 관리 |
| `/export` | 대화 내보내기 | 참조용 저장 |
| `/usage-credits` | 추가 사용 한도 설정 (`/extra-usage`에서 이름 변경, v2.1.144, 기존 이름도 별칭으로 사용 가능) | 사용량 제한 관리 |
| `/feedback` | 피드백 또는 버그 리포트 제출 | 문제 신고 |
| `/login` | Anthropic 인증 | 기능 사용 |
| `/logout` | 로그아웃 | 계정 전환 |
| `/sandbox` | 샌드박스 모드 전환 | 안전한 명령 실행 |
| `/doctor` | 진단 실행 | 문제 해결 |
| `/reload-plugins` | 설치된 플러그인 다시 로드 | 플러그인 관리 |
| `/reload-skills` | 재시작 없이 스킬 디렉터리 다시 검색 (v2.1.152) | 스킬 관리 |
| `/workflows` | 실행 중 및 완료된 동적 워크플로 실행 내역 표시 (v2.1.154) | 멀티 에이전트 오케스트레이션 |
| `/release-notes` | 릴리스 노트 표시 | 새로운 기능 확인 |
| `/remote-control` | 원격 제어 활성화 | 원격 접속 |
| `/permissions` | 권한 관리 | 접근 권한 제어 |
| `/session` | 세션 관리 | 다중 세션 워크플로 |
| `/rename` | 현재 세션 이름 변경 | 세션 정리 |
| `/resume` | 이전 세션 이어서 작업 | 작업 계속하기 |
| `/todo` | 할 일 목록 조회/관리 | 작업 추적 |
| `/tui` | 전체 화면 TUI(Text User Interface) 모드 전환 | 전체 화면/tmux에서 깜빡임 없는 출력 |
| `/tasks` | 백그라운드 작업 표시 | 비동기 작업 모니터링 |
| `/copy` | 마지막 응답을 클립보드로 복사 | 출력물 빠르게 공유 |
| `/teleport` | 다른 컴퓨터로 세션 전송 | 원격으로 작업 이어가기 |
| `/desktop` | Claude Desktop 앱 열기 | 데스크톱 인터페이스로 전환 |
| `/theme` | 색상 테마 변경. v2.1.118부터 `~/.claude/themes/<name>.json`의 사용자 정의 테마 지원(플러그인은 `themes/` 디렉터리를 포함 가능) | 화면 테마 사용자 지정 |
| `/usage` | 사용량/비용/통계를 통합한 공식 명령어(`/cost`와 `/stats` 통합, v2.1.118). v2.1.149부터 비용을 스킬, 서브에이전트, 플러그인, MCP 서버별로 구분하여 표시. **VSCode 확장**(v2.1.174)에서는 `/usage` 대화상자에 캐시 미스, 긴 컨텍스트 비용, 서브에이전트, 스킬/에이전트/플러그인/MCP별 24시간 및 7일 사용량 분석이 추가됨 | 사용량 및 비용 모니터링 |
| `/focus` | 집중 보기 모드 전환 | 긴 작업 중 화면 잡음 최소화 |
| `/fork` | 현재 대화 분기 | 대안 탐색 |
| `/stats` | `/usage`의 통계 탭을 여는 단축 별칭 (v2.1.118+) | 세션 통계 확인 |
| `/statusline` | 상태 표시줄 구성 | 상태 표시 사용자 지정 |
| `/stickers` | 세션 스티커 보기 | 재미 요소 |
| `/fast` | 빠른 출력 모드 전환 | 응답 속도 향상 |
| `/terminal-setup` | 터미널 연동 설정 | 터미널 기능 설정 |
| `/undo` | `/rewind`의 별칭 (v2.1.108) | `/rewind`와 동일 |
| `/upgrade` | 업데이트 확인 | 버전 관리 |
| `/team-onboarding` | 현재 프로젝트의 Claude Code 사용 내역을 기반으로 팀원 온보딩 가이드 생성 | 신규 팀원 온보딩 (v2.1.101) |
| `/ultraplan` | 계획 작업을 웹 기반 Claude Code 세션의 계획 모드로 위임 | 대규모 계획 작업 오프로드 (Research Preview, v2.1.91+) |
| `/ultrareview` | 현재 변경 사항에 대해 클라우드 기반 멀티 에이전트 코드 리뷰 실행 | 병합 전 심층 코드 리뷰 (v2.1.112) |
| `/less-permission-prompts` | 대화 기록을 분석하여 자주 사용하는 읽기 전용 도구의 허용 목록을 우선순위에 따라 제안 | 반복적인 권한 요청 감소 (v2.1.112) |

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
| `default` | 모든 도구 호출 시마다 권한 요청 | 일반적인 대화형 사용 |
| `acceptEdits` | 파일 수정은 자동 승인하고 나머지는 권한 요청 | 신뢰할 수 있는 편집 워크플로 |
| `plan` | 읽기 전용 도구만 허용, 쓰기 금지 | 계획 수립 및 탐색 |
| `auto` | 모든 도구를 권한 요청 없이 허용 | 완전 자율 실행 (Research Preview) |
| `bypassPermissions` | 모든 권한 확인 건너뛰기 | CI/CD, 헤드리스 환경 |
| `dontAsk` | 권한이 필요한 도구는 건너뜀 | 비대화형 스크립트 |

> **참고**: `auto` 모드는 2026년 3월 기준 Research Preview 기능입니다. `bypassPermissions`는 신뢰할 수 있는 샌드박스 환경에서만 사용해야 합니다.

**참고 자료**: [Official Docs](https://code.claude.com/docs/en/permissions)

---

## Subagents

특정 작업을 위해 독립된 컨텍스트를 사용하는 전문 AI 보조 에이전트입니다.

> **중첩 생성(v2.1.172)**: 서브에이전트는 최대 5단계까지 자신의 서브에이전트를 생성할 수 있습니다. 이전 버전에서는 중첩 생성이 지원되지 않았습니다. 특정 서브에이전트만 생성하도록 제한하는 `Agent(agent_type)` 문법은 [04-subagents/README.md](04-subagents/README.md#restrict-spawnable-subagents)를 참고하세요.

### 기본 제공 서브에이전트

| Agent | Description | Tools | Model | When to Use |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | 다단계 작업, 조사 | 모든 도구 | 상위 모델 상속 | 복잡한 조사, 다중 파일 작업 |
| **Plan** | 구현 계획 수립 | Read, Glob, Grep, Bash | 상위 모델 상속 | 아키텍처 설계, 계획 수립 |
| **Explore** | 코드베이스 탐색 | Read, Glob, Grep | Haiku 4.5 | 빠른 검색, 코드 이해 |
| **Bash** | 명령 실행 | Bash | 상위 모델 상속 | Git 작업, 터미널 작업 |
| **statusline-setup** | 상태 표시줄 구성 | Bash, Read, Write | Sonnet 4.6 | 상태 표시줄 설정 |
| **Claude Code Guide** | 도움말 및 문서 | Read, Glob, Grep | Haiku 4.5 | 도움말 확인, 기능 학습 |

### 서브에이전트 설정 필드

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | 에이전트 식별자 |
| `description` | string | 에이전트의 역할 |
| `model` | string | 사용할 모델 재정의(예: `haiku-4.5`) |
| `tools` | array | 허용된 도구 목록 |
| `effort` | string | 추론 수준(`low`, `medium`, `high`) |
| `initialPrompt` | string | 에이전트 시작 시 주입되는 시스템 프롬프트 |
| `disallowedTools` | array | 명시적으로 금지된 도구 목록 |

### 사용자 정의 서브에이전트 (예시)

| Agent | Description | When to Use | Scope | Installation |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | 종합 코드 품질 검토 | 코드 리뷰 | 프로젝트 | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | 기능 아키텍처 설계 | 신규 기능 설계 | 프로젝트 | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | 심층 코드베이스 분석 | 기존 기능 분석 | 프로젝트 | `cp 04-subagents/code-explorer.md .claude/agents/` |
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

> **Scope**: `User` = 개인(`~/.claude/skills/`), `Project` = 팀 공유(`.claude/skills/`)
### Skill Structure

```
~/.claude/skills/skill-name/
├── SKILL.md          # Skill definition & instructions
├── scripts/          # Helper scripts
└── templates/        # Output templates
```

### Skill Frontmatter Fields

스킬은 `SKILL.md`에서 설정을 위한 YAML 프론트매터를 지원합니다.

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | 스킬 표시 이름 |
| `description` | string | 스킬의 기능 설명 |
| `autoInvoke` | array | 자동 호출을 위한 트리거 문구 |
| `effort` | string | 추론 수준 (`low`, `medium`, `high`) |
| `shell` | string | 스크립트에 사용할 셸 (`bash`, `zsh`, `sh`) |

**참고 자료**: [03-skills/](03-skills/) | [Official Docs](https://code.claude.com/docs/en/skills)

**빠른 설치(모든 스킬)**:
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### 기본 제공 스킬

| Skill | Description | When Auto-Invoked |
|-------|-------------|-------------------|
| `/batch` | 여러 파일에 프롬프트 실행 | 일괄 작업 |
| `/claude-api` | Claude API를 사용한 애플리케이션 개발 | API 개발 |
| `/debug` | 실패한 테스트 및 오류 디버깅 | 디버깅 작업 |
| `/fewer-permission-prompts` | 대화 기록을 분석하여 우선순위가 지정된 허용 목록 제안 | 반복적인 권한 요청 감소 |
| `/loop` | 일정 간격으로 프롬프트 실행 | 반복 작업 |
| `/run` *(v2.1.145+)* | 프로젝트 애플리케이션을 실행하여 변경 사항 확인 | 실제 애플리케이션에서 변경 사항 검증 |
| `/run-skill-generator` *(v2.1.145+)* | 특정 프로젝트에서 `/run`/`/verify`를 사용할 수 있도록 설정 | `/run` 최초 프로젝트 설정 |
| `/code-review` | 현재 diff를 선택한 추론 수준(예: `/code-review high`)으로 검토하여 정확성 및 버그를 확인. `--comment`를 지정하면 결과를 PR의 인라인 댓글로 게시 | 코드 작성 후, PR 병합 전 |
| `/simplify` *(v2.1.154부터 다시 독립 기능)* | 정리만 수행하는 리뷰(재사용, 단순화, 효율성, 추상화 수준)를 실행하고 수정 사항을 적용. 버그 탐지는 수행하지 않음 | 버그 탐지 없이 코드 정리 |
| `/verify` *(v2.1.145+)* | 애플리케이션을 빌드, 실행 및 확인하여 수정 사항이 제대로 동작하는지 검증 | 수정 사항의 전체 동작 검증 |

---

## Plugins

명령어, 에이전트, MCP 서버 및 훅을 묶어서 제공하는 기능 모음입니다.

### 플러그인 예시

| Plugin | Description | Components | When to Use | Scope | Installation |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | PR 리뷰 워크플로 | 명령어 3개, 에이전트 3개, GitHub MCP | 코드 리뷰 | 프로젝트 | `/plugin install pr-review` |
| `devops-automation` | 배포 및 모니터링 | 명령어 4개, 에이전트 3개, K8s MCP | DevOps 작업 | 프로젝트 | `/plugin install devops-automation` |
| `documentation` | 문서 생성 모음 | 명령어 4개, 에이전트 3개, 템플릿 | 문서 작성 | 프로젝트 | `/plugin install documentation` |

> **Scope**: `Project` = 팀 공유, `User` = 개인 워크플로

### 플러그인 구조

```
.claude-plugin/
├── plugin.json       # 매니페스트 파일
├── commands/         # Slash Commands
├── agents/           # Subagents
├── skills/           # Skills
├── mcp/              # MCP 설정
├── hooks/            # Hook 스크립트
└── scripts/          # 유틸리티 스크립트
```

**참고 자료**: [07-plugins/](07-plugins/) | [Official Docs](https://code.claude.com/docs/en/plugins)

**플러그인 관리 명령어**:
```bash
/plugin list              # 설치된 플러그인 목록
/plugin install <name>    # 플러그인 설치
/plugin remove <name>     # 플러그인 제거
/plugin update <name>     # 플러그인 업데이트
```

---

## MCP Servers

외부 도구 및 API에 접근하기 위한 Model Context Protocol 서버입니다.

### 일반적으로 사용하는 MCP 서버

| Server | Description | When to Use | Scope | Installation |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | PR 관리, 이슈, 코드 | GitHub 워크플로 | 프로젝트 | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL 쿼리 및 데이터 접근 | 데이터베이스 작업 | 프로젝트 | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | 고급 파일 작업 | 복잡한 파일 작업 | 사용자 | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | 팀 커뮤니케이션 | 알림, 업데이트 | 프로젝트 | 설정에서 구성 |
| **Google Docs** | 문서 접근 | 문서 편집 및 검토 | 프로젝트 | 설정에서 구성 |
| **Asana** | 프로젝트 관리 | 작업 추적 | 프로젝트 | 설정에서 구성 |
| **Stripe** | 결제 데이터 | 재무 분석 | 프로젝트 | 설정에서 구성 |
| **Memory** | 영구 메모리 | 세션 간 기억 유지 | 사용자 | 설정에서 구성 |
| **Context7** | 라이브러리 문서 | 최신 문서 조회 | 기본 제공 | 기본 제공 |

> **Scope**: `Project` = 팀(`.mcp.json`), `User` = 개인(`~/.claude.json`), `Built-in` = 기본 제공

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
| `Setup` | 초기 환경 설정(세션당 1회) | 최초 세션 부트스트랩 | 도구 준비, 의존성 설치 |
| `InstructionsLoaded` | 지침 로드 완료 | CLAUDE.md 또는 규칙 파일 로드 | 사용자 정의 지침 처리 |
| `UserPromptSubmit` | 프롬프트 처리 전 | 사용자가 메시지를 전송할 때 | 입력 검증 |
| `UserPromptExpansion` | 사용자 프롬프트 확장(@멘션, Slash Commands 해석) | 확장 후, 제출 전 | 확장된 프롬프트 변환 또는 검사 |
| `PreToolUse` | 도구 실행 전 | 모든 도구 실행 전 | 검증, 로깅 |
| `PermissionRequest` | 권한 요청 대화상자 표시 | 민감한 작업 전 | 사용자 정의 승인 절차 |
| `PermissionDenied` | 사용자가 권한 요청을 거부 | 권한 거부 후 | 로깅, 분석, 정책 적용 |
| `PostToolUse` | 도구 실행 성공 후 | 모든 도구 실행 완료 후 | 포맷팅, 알림 |
| `PostToolUseFailure` | 도구 실행 실패 | 도구 오류 발생 후 | 오류 처리, 로깅 |
| `PostToolBatch` | 도구 실행 묶음 완료 후 | 도구 배치 종료 시 | 집계 보고, 일괄 검증 |
| `Notification` | 알림 전송 | Claude가 알림을 보낼 때 | 외부 알림 |
| `SubagentStart` | 서브에이전트 생성 | 서브에이전트 작업 시작 | 서브에이전트 컨텍스트 초기화 |
| `SubagentStop` | 서브에이전트 종료 | 서브에이전트 작업 완료 | 후속 작업 실행 |
| `Stop` | Claude 응답 완료 | 응답 종료 | 정리 작업, 보고 |
| `StopFailure` | API 오류로 턴 종료 | API 오류 발생 | 오류 복구, 로깅 |
| `TeammateIdle` | 팀원 에이전트 대기 상태 | 에이전트 팀 협업 중 | 작업 분배 |
| `TaskCompleted` | 작업 완료 표시 | 작업 완료 시 | 작업 후 처리 |
| `TaskCreated` | TaskCreate를 통해 작업 생성 | 새 작업 생성 시 | 작업 추적, 로깅 |
| `ConfigChange` | 설정 변경 | 설정 수정 시 | 설정 변경 대응 |
| `CwdChanged` | 작업 디렉터리 변경 | 디렉터리 변경 시 | 디렉터리별 초기 설정 |
| `FileChanged` | 감시 중인 파일 변경 | 파일 수정 시 | 파일 모니터링, 재빌드 |
| `PreCompact` | Compact 작업 전 | 컨텍스트 압축 전 | 상태 보존 |
| `PostCompact` | Compact 작업 후 | 압축 완료 후 | 후처리 작업 |
| `WorktreeCreate` | Worktree 생성 | Git Worktree 생성 시 | Worktree 환경 설정 |
| `WorktreeRemove` | Worktree 제거 | Git Worktree 제거 시 | Worktree 리소스 정리 |
| `Elicitation` | MCP 서버가 사용자 입력 요청 | MCP 입력 요청 시 | 입력 검증 |
| `ElicitationResult` | 사용자가 입력 요청에 응답 | 사용자 응답 시 | 응답 처리 |
| `SessionEnd` | 세션 종료 | 세션 종료 시 | 정리 작업, 상태 저장 |

### Hook 예시

| Hook | Description | Event | Scope | Installation |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | 명령 검증 | PreToolUse:Bash | 프로젝트 | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | 보안 검사 | PostToolUse:Write | 프로젝트 | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | 자동 코드 포맷팅 | PostToolUse:Write | 사용자 | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | 프롬프트 검증 | UserPromptSubmit | 프로젝트 | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | 토큰 사용량 추적 | Stop | 사용자 | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | 커밋 전 검증 | PreToolUse:Bash | 프로젝트 | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | 명령 실행 로그 기록 | PostToolUse:Bash | 사용자 | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |
| `dependency-check.sh` | 매니페스트 변경 시 취약점 검사 | PostToolUse:Write | 프로젝트 | `cp 06-hooks/dependency-check.sh .claude/hooks/` |

> **Scope**: `Project` = 팀(`.claude/settings.json`), `User` = 개인(`~/.claude/settings.json`)

### Hook Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "~/.claude/hooks/validate-bash.py"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "~/.claude/hooks/format-code.sh"
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

## New Features (May 2026)

| Feature | Description | How to Use |
|---------|-------------|------------|
| **/focus** | 집중 모드를 전환하여 방해 요소 없이 출력 표시 (v2.1.110) | 긴 작업 중 시각적 방해를 줄이려면 `/focus` 실행 |
| **/proactive** | `/loop`의 별칭으로 동일한 반복 작업 동작 제공 (v2.1.105) | `/loop` 대신 `/proactive` 사용 가능 |
| **/recap** | 기존 세션으로 돌아왔을 때 작업 요약 표시 (v2.1.108) | 작업을 중단한 뒤 `/recap` 실행 |
| **/tui** | 전체 화면 TUI(Text User Interface) 모드 전환으로 깜빡임 없는 출력 제공 (v2.1.110) | 전체 화면 터미널 또는 tmux에서 `/tui` 사용 |
| **/undo** | `/rewind`의 별칭으로 이전 체크포인트로 되돌림 (v2.1.108) | `/rewind` 대신 `/undo` 사용 가능 |
| **Monitor Tool** | 폴링 대신 백그라운드 명령의 stdout 스트림을 감시하고 이벤트에 반응 | [Advanced Features](09-advanced-features/)의 Monitor Tool 사용 |
| **/team-onboarding** | 프로젝트의 Claude Code 구성을 기반으로 팀원 온보딩 가이드 자동 생성 (v2.1.101) | 프로젝트에서 `/team-onboarding` 실행 |
| **Ultraplan auto-create** | 최초 `/ultraplan` 실행 시 클라우드 환경 자동 생성(수동 설정 불필요) (v2.1.101) | `/ultraplan <prompt>` 사용 |
| **Remote Control** | API를 통해 Claude Code 세션 원격 제어 | 원격 제어 API를 사용하여 프롬프트 전송 및 응답 수신 |
| **Web Sessions** | 브라우저 기반 환경에서 Claude Code 실행 | `claude web` 또는 Anthropic Console 사용 |
| **Desktop App** | Claude Code 네이티브 데스크톱 애플리케이션 | `/desktop` 사용 또는 Anthropic 웹사이트에서 다운로드 |
| **Agent Teams** | 관련 작업을 수행하는 여러 에이전트 협업 | 컨텍스트를 공유하는 팀 에이전트 구성 |
| **Task List** | 백그라운드 작업 관리 및 모니터링 | `/tasks`로 백그라운드 작업 확인 및 관리 |
| **Prompt Suggestions** | 컨텍스트 기반 명령어 추천 | 현재 컨텍스트에 따라 자동 표시 |
| **Git Worktrees** | 병렬 개발을 위한 독립된 Git Worktree | Worktree 명령으로 안전한 병렬 브랜치 작업 수행 |
| **Sandboxing** | 안전한 실행을 위한 격리 환경 | `/sandbox`로 전환하여 제한된 환경에서 실행 |
| **MCP OAuth** | MCP 서버용 OAuth 인증 | MCP 서버 설정에서 OAuth 자격 증명 구성 |
| **MCP Tool Search** | MCP 도구 검색 및 탐색 | 연결된 서버에서 사용 가능한 MCP 도구 검색 |
| **Scheduled Tasks** | `/loop` 및 cron 도구를 이용한 반복 작업 예약 | `/loop 5m /command` 또는 CronCreate 도구 사용 |
| **Chrome Integration** | Headless Chromium을 이용한 브라우저 자동화 | `--chrome` 플래그 또는 `/chrome` 사용 |
| **Keyboard Customization** | 조합 키를 포함한 키 바인딩 사용자 지정 | `/keybindings` 또는 `~/.claude/keybindings.json` 수정 |
| **Auto Mode** | 권한 요청 없이 완전 자동 실행(Research Preview) | `--mode auto` 또는 `/permissions auto` 사용 (2026년 3월) |
| **Channels** | 다중 채널 통신(Telegram, Slack 등) (Research Preview) | 채널 플러그인 구성 (2026년 3월) |
| **Voice Dictation** | 프롬프트 음성 입력 | 마이크 아이콘 또는 음성 단축키 사용 |
| **Agent Hook Type** | 셸 명령 대신 서브에이전트를 실행하는 Hook | Hook 설정에서 `"type": "agent"` 지정 |
| **Prompt Hook Type** | 대화에 프롬프트를 삽입하는 Hook | Hook 설정에서 `"type": "prompt"` 지정 |
| **MCP Elicitation** | 도구 실행 중 MCP 서버가 사용자 입력 요청 가능 | `Elicitation` 및 `ElicitationResult` Hook 이벤트 처리 |
| **Plugin LSP Support** | 플러그인을 통한 Language Server Protocol 연동 | `plugin.json`에서 LSP 서버 구성 |
| **Managed Drop-ins** | 조직에서 관리하는 Drop-in 구성 (v2.1.83) | 관리 정책으로 설정되며 모든 사용자에게 자동 적용 |
| **`claude plugin init`** | `.claude/skills`에 새 플러그인 골격 생성. 마켓플레이스 없이 자동 로드됨 (v2.1.157) | `claude plugin init <name>` 실행 |
| **Auto Mode on Bedrock/Vertex/Foundry** | Opus 4.7/4.8용 Auto Mode를 서드파티 제공자에서도 사용 가능(선택 기능) (v2.1.158) | `CLAUDE_CODE_ENABLE_AUTO_MODE=1` 설정 |

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
| 7. 통합 기능 | Plugins | `/plugin install pr-review` |

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

**Last Updated**: June 15, 2026
**Claude Code Version**: 2.1.176
**Sources**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/changelog#2-1-172
- https://code.claude.com/docs/en/changelog#2-1-174
- https://github.com/anthropics/claude-code/releases/tag/v2.1.145
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/cli-reference
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
