<!-- i18n-source: QUICK_REFERENCE.md -->
<!-- i18n-source-sha: 553a319 -->
<!-- i18n-date: 2026-05-16 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 예제 — 퀵 레퍼런스 카드

> 한국어 메인 문서는 [README.md](README.md), 실무 적용 흐름은 [PRACTICAL-GUIDE.md](PRACTICAL-GUIDE.md)를 참조한다.

## 🚀 설치 빠른 명령

### 슬래시 커맨드
```bash
# 전체 설치
cp 01-slash-commands/*.md .claude/commands/

# 특정 항목 설치
cp 01-slash-commands/optimize.md .claude/commands/
```

### 메모리
```bash
# 프로젝트 메모리
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 개인 메모리
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### 스킬
```bash
# 개인 스킬
cp -r 03-skills/code-review ~/.claude/skills/

# 프로젝트 스킬
cp -r 03-skills/code-review .claude/skills/
```

### 서브에이전트
```bash
# 전체 설치
cp 04-subagents/*.md .claude/agents/

# 특정 항목 설치
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# 자격 증명 설정
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 설정 설치(프로젝트 스코프)
cp 05-mcp/github-mcp.json .mcp.json

# 또는 사용자 스코프: ~/.claude.json에 추가
```

### 훅
```bash
# 훅 설치
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 설정에서 구성 (~/.claude/settings.json)
```

### 플러그인
```bash
# 예제에서 설치(게시된 경우)
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### 체크포인트
```bash
# 체크포인트는 모든 사용자 프롬프트마다 자동 생성됨
# 되감으려면 Esc를 두 번 누르거나 다음을 사용:
/rewind

# 그다음 선택: 코드와 대화 복원, 대화 복원,
# 코드 복원, 여기서부터 요약, 취소
```

### 고급 기능
```bash
# 설정에서 구성 (.claude/settings.json)
# 09-advanced-features/config-examples.json 참조

# 플래닝 모드
/plan Task description

# 권한 모드 (--permission-mode 플래그 사용)
# default        - 위험한 동작은 승인 요청
# acceptEdits    - 파일 편집 자동 수락, 그 외는 요청
# plan           - 읽기 전용 분석, 수정 없음
# dontAsk        - 위험한 동작 외 모두 수락
# auto           - 백그라운드 분류기가 권한 자동 결정
# bypassPermissions - 모든 동작 수락(--dangerously-skip-permissions 필요)

# 세션 관리
/resume                # 이전 대화 재개
/rename "name"         # 현재 세션 이름 지정
/fork                  # 현재 세션 포크
claude -c              # 가장 최근 대화 이어가기
claude -r "session"    # 이름/ID로 세션 재개
```

---

## 📋 기능 치트시트

| 기능 | 설치 경로 | 사용법 |
|---------|-------------|-------|
| **슬래시 커맨드(60+)** | `.claude/commands/*.md` | `/command-name` |
| **메모리** | `./CLAUDE.md` | 자동 로드 |
| **스킬** | `.claude/skills/*/SKILL.md` | 자동 호출 |
| **서브에이전트** | `.claude/agents/*.md` | 자동 위임 |
| **MCP** | `.mcp.json`(프로젝트) 또는 `~/.claude.json`(사용자) | `/mcp__server__action` |
| **훅(29개 이벤트)** | `~/.claude/hooks/*.sh` | 이벤트 트리거(5종) |
| **플러그인** | `/plugin install` 경유 | 전체 번들 |
| **체크포인트** | 내장 | `Esc+Esc` 또는 `/rewind` |
| **플래닝 모드** | 내장 | `/plan <task>` |
| **권한 모드(6종)** | 내장 | `--allowedTools`, `--permission-mode` |
| **세션** | 내장 | `/session <command>` |
| **백그라운드 태스크** | 내장 | 백그라운드 실행 |
| **원격 제어** | 내장 | WebSocket API |
| **웹 세션** | 내장 | `claude web` |
| **Git 워크트리** | 내장 | `/worktree` |
| **자동 메모리** | 내장 | CLAUDE.md에 자동 저장 |
| **태스크 리스트** | 내장 | `/task list` |
| **번들 스킬(5종)** | 내장 | `/simplify`, `/loop`, `/claude-api`, `/voice`, `/browse` |

---

## 🎯 자주 쓰는 사용 사례

### 코드 리뷰
```bash
# 방법 1: 슬래시 커맨드
cp 01-slash-commands/optimize.md .claude/commands/
# 사용: /optimize

# 방법 2: 서브에이전트
cp 04-subagents/code-reviewer.md .claude/agents/
# 사용: 자동 위임

# 방법 3: 스킬
cp -r 03-skills/code-review ~/.claude/skills/
# 사용: 자동 호출

# 방법 4: 플러그인(최선)
/plugin install pr-review
# 사용: /review-pr
```

### 문서화
```bash
# 슬래시 커맨드
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# 서브에이전트
cp 04-subagents/documentation-writer.md .claude/agents/

# 스킬
cp -r 03-skills/doc-generator ~/.claude/skills/

# 플러그인(완성형 솔루션)
/plugin install documentation
```

### DevOps
```bash
# 완성형 플러그인
/plugin install devops-automation

# 명령: /deploy, /rollback, /status, /incident
```

### 팀 표준
```bash
# 프로젝트 메모리
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 팀에 맞게 편집
vim CLAUDE.md
```

### 자동화와 훅
```bash
# 훅 설치(29개 이벤트, 5종: command, http, mcp_tool, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 예제:
# - 커밋 전 테스트: pre-commit.sh
# - 코드 자동 포맷: format-code.sh
# - 보안 스캔: security-scan.sh

# 완전 자율 워크플로용 Auto 모드
claude --enable-auto-mode -p "Refactor and test the auth module"
# 또는 Shift+Tab으로 모드를 대화형으로 순환
```

### 안전한 리팩터링
```bash
# 체크포인트는 각 프롬프트 전에 자동 생성됨
# 리팩터링 시도
# 성공하면: 계속
# 실패하면: Esc+Esc 또는 /rewind로 되돌리기
```

### 복잡한 구현
```bash
# 플래닝 모드 사용
/plan Implement user authentication system

# Claude가 상세 계획 작성
# 검토 후 승인
# Claude가 체계적으로 구현
```

### CI/CD 통합
```bash
# 헤드리스 모드 실행(비대화형)
claude -p "Run all tests and generate report"

# CI용 권한 모드와 함께
claude -p "Run tests" --permission-mode dontAsk

# 완전 자율 CI 작업용 Auto 모드와 함께
claude --enable-auto-mode -p "Run tests and fix failures"

# 자동화를 위한 훅과 함께
# 09-advanced-features/README.md 참조
```

### 학습과 실험
```bash
# 안전한 분석을 위한 플랜 모드 사용
claude --permission-mode plan

# 안전하게 실험 - 체크포인트가 자동 생성됨
# 되감아야 하면: Esc+Esc 또는 /rewind 사용
```

### 에이전트 팀
```bash
# 에이전트 팀 활성화
export CLAUDE_AGENT_TEAMS=1

# 또는 settings.json에서
{ "agentTeams": { "enabled": true } }

# 시작: "팀 방식으로 기능 X를 구현해줘"
```

### 예약 작업
```bash
# 5분마다 명령 실행
/loop 5m /check-status

# 일회성 리마인더
/loop 30m "remind me to check the deploy"
```

---

## 📁 파일 위치 레퍼런스

```text
Your Project/
├── .claude/
│   ├── commands/              # 슬래시 커맨드를 여기에
│   ├── agents/                # 서브에이전트를 여기에
│   ├── skills/                # 프로젝트 스킬을 여기에
│   └── settings.json          # 프로젝트 설정(훅 등)
├── .mcp.json                  # MCP 설정(프로젝트 스코프)
├── CLAUDE.md                  # 프로젝트 메모리
└── src/
    └── api/
        └── CLAUDE.md          # 디렉터리별 메모리

User Home/
├── .claude/
│   ├── commands/              # 개인 커맨드
│   ├── agents/                # 개인 에이전트
│   ├── skills/                # 개인 스킬
│   ├── hooks/                 # 훅 스크립트
│   ├── settings.json          # 사용자 설정
│   ├── managed-settings.d/    # 관리형 설정(엔터프라이즈/조직)
│   └── CLAUDE.md              # 개인 메모리
└── .claude.json               # 개인 MCP 설정(사용자 스코프)
```

---

## 🔍 예제 찾기

### 카테고리별
- **슬래시 커맨드**: `01-slash-commands/`
- **메모리**: `02-memory/`
- **스킬**: `03-skills/`
- **서브에이전트**: `04-subagents/`
- **MCP**: `05-mcp/`
- **훅**: `06-hooks/`
- **플러그인**: `07-plugins/`
- **체크포인트**: `08-checkpoints/`
- **고급 기능**: `09-advanced-features/`
- **CLI**: `10-cli/`

### 사용 사례별
- **성능**: `01-slash-commands/optimize.md`
- **보안**: `04-subagents/secure-reviewer.md`
- **테스트**: `04-subagents/test-engineer.md`
- **문서**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### 복잡도별
- **간단**: 슬래시 커맨드
- **중간**: 서브에이전트, 메모리
- **고급**: 스킬, 훅
- **완성형**: 플러그인

---

## 🎓 학습 경로

### 1일차
```bash
# 개요 읽기
cat README.md

# 커맨드 설치
cp 01-slash-commands/optimize.md .claude/commands/

# 실행
/optimize
```

### 2~3일차
```bash
# 메모리 설정
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# 서브에이전트 설치
cp 04-subagents/code-reviewer.md .claude/agents/
```

### 4~5일차
```bash
# MCP 설정
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# MCP 명령 실행
/mcp__github__list_prs
```

### 2주차
```bash
# 스킬 설치
cp -r 03-skills/code-review ~/.claude/skills/

# 자동 호출되도록 두기
# "이 코드의 문제를 리뷰해줘"라고만 말하면 됨
```

### 3주차 이후
```bash
# 완성형 플러그인 설치
/plugin install pr-review

# 번들 기능 사용
/review-pr
/check-security
/check-tests
```

---

## 신규 기능 (2026년 3월)

| 기능 | 설명 | 사용법 |
|---------|-------------|-------|
| **Auto 모드** | 백그라운드 분류기로 완전 자율 동작 | `--enable-auto-mode` 플래그, `Shift+Tab`으로 모드 순환 |
| **채널** | Discord, Telegram 연동 | `--channels` 플래그, Discord/Telegram 봇 |
| **음성 받아쓰기** | Claude에 명령과 컨텍스트를 말로 전달 | `/voice` 명령 |
| **훅(29개 이벤트)** | 5종으로 확장된 훅 시스템 | command, http, mcp_tool, prompt, agent 훅 종류 |
| **MCP Elicitation** | MCP 서버가 런타임에 사용자 입력 요청 가능 | 서버가 명확화 필요 시 자동 프롬프트 |
| **플러그인 LSP** | 플러그인용 Language Server Protocol 지원 | `userConfig`, `${CLAUDE_PLUGIN_DATA}` 변수 |
| **원격 제어** | WebSocket API로 Claude Code 제어 | 외부 연동용 `claude --remote` |
| **웹 세션** | 브라우저 기반 Claude Code 인터페이스 | `claude web`으로 실행 |
| **데스크톱 앱** | 네이티브 데스크톱 애플리케이션 | claude.ai/download에서 다운로드 |
| **태스크 리스트** | 백그라운드 태스크 관리 | `/task list`, `/task status <id>` |
| **자동 메모리** | 대화에서 메모리 자동 저장 | 핵심 컨텍스트를 CLAUDE.md에 자동 저장 |
| **Git 워크트리** | 병렬 개발용 격리 작업공간 | `/worktree`로 격리 작업공간 생성 |
| **모델 선택** | Sonnet 4.6, Opus 4.7, Haiku 4.5 전환 | `/model` 또는 `--model` 플래그 |
| **에이전트 팀** | 여러 에이전트를 작업에 조율 | `CLAUDE_AGENT_TEAMS=1` 환경 변수로 활성화 |
| **예약 작업** | `/loop`로 반복 작업 | `/loop 5m /command` 또는 CronCreate 도구 |
| **Chrome 연동** | 브라우저 자동화 | `--chrome` 플래그 또는 `/chrome` 명령 |
| **키보드 커스터마이즈** | 커스텀 키 바인딩 | `/keybindings` 명령 |

---

## 팁과 요령

### 커스터마이즈
- 예제를 그대로 두고 시작
- 필요에 맞게 수정
- 팀과 공유 전 테스트
- 설정을 버전 관리

### 모범 사례
- 팀 표준에는 메모리 사용
- 완성형 워크플로에는 플러그인 사용
- 복잡한 작업에는 서브에이전트 사용
- 빠른 작업에는 슬래시 커맨드 사용

### 문제 해결
```bash
# 파일 위치 확인
ls -la .claude/commands/
ls -la .claude/agents/

# YAML 문법 확인
head -20 .claude/agents/code-reviewer.md

# MCP 연결 테스트
echo $GITHUB_TOKEN
```

---

## 📊 기능 매트릭스

| 필요 | 사용할 것 | 예제 |
|------|----------|---------|
| 빠른 단축 | 슬래시 커맨드(60+) | `01-slash-commands/optimize.md` |
| 팀 표준 | 메모리 | `02-memory/project-CLAUDE.md` |
| 자동 워크플로 | 스킬 | `03-skills/code-review/` |
| 전문 작업 | 서브에이전트 | `04-subagents/code-reviewer.md` |
| 외부 데이터 | MCP(+ Elicitation) | `05-mcp/github-mcp.json` |
| 이벤트 자동화 | 훅(29개 이벤트, 5종) | `06-hooks/pre-commit.sh` |
| 완성형 솔루션 | 플러그인(+ LSP 지원) | `07-plugins/pr-review/` |
| 안전한 실험 | 체크포인트 | `08-checkpoints/checkpoint-examples.md` |
| 완전 자율 | Auto 모드 | `--enable-auto-mode` 또는 `Shift+Tab` |
| 채팅 연동 | 채널 | `--channels`(Discord, Telegram) |
| CI/CD 파이프라인 | CLI | `10-cli/README.md` |

---

## 🔗 빠른 링크

- **메인 가이드(한국어)**: [README.md](README.md)
- **실무 적용 가이드**: [PRACTICAL-GUIDE.md](PRACTICAL-GUIDE.md)
- **전체 인덱스(영문)**: `../INDEX.md`
- **원본 가이드(영문)**: `../claude_concepts_guide.md`

---

## 📞 자주 묻는 질문

**Q: 무엇을 써야 하나?**
A: 슬래시 커맨드로 시작하고 필요에 따라 기능을 추가한다.

**Q: 기능을 섞을 수 있나?**
A: 그렇다! 함께 동작한다. 메모리 + 커맨드 + MCP = 강력함.

**Q: 팀과 어떻게 공유하나?**
A: `.claude/` 디렉터리를 git에 커밋한다.

**Q: 시크릿은 어떻게 하나?**
A: 환경 변수를 사용하고 절대 하드코딩하지 않는다.

**Q: 예제를 수정해도 되나?**
A: 물론이다! 커스터마이즈하라고 만든 템플릿이다.

---

## ✅ 체크리스트

시작 체크리스트:

- [ ] `README.md` 읽기
- [ ] 슬래시 커맨드 1개 설치
- [ ] 커맨드 실행해 보기
- [ ] 프로젝트 `CLAUDE.md` 생성
- [ ] 서브에이전트 1개 설치
- [ ] MCP 연동 1개 설정
- [ ] 스킬 1개 설치
- [ ] 완성형 플러그인 사용해 보기
- [ ] 필요에 맞게 커스터마이즈
- [ ] 팀과 공유

---

**빠른 시작**: `cat README.md`

**전체 인덱스**: `cat INDEX.md`

**이 카드**: 빠른 참조용으로 가까이 두자!

---
**최종 수정**: 2026년 5월 9일
**Claude Code 버전**: 2.1.138
**출처**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/commands
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
**호환 모델**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
