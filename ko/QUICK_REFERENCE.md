<!-- i18n-source: QUICK_REFERENCE.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 예제 - 빠른 참조 카드

## 🚀 빠른 설치 명령

### Slash Commands
```bash
# 모두 설치
cp 01-slash-commands/*.md .claude/commands/

# 특정 명령만 설치
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memory
```bash
# 프로젝트 메모리
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 개인 메모리
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills
```bash
# 개인 Skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# 프로젝트 Skills
cp -r 03-skills/code-review-specialist .claude/skills/
```

### Subagents
```bash
# 모두 설치
cp 04-subagents/*.md .claude/agents/

# 특정 Subagent 설치
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# 자격 증명 설정
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 설정 설치(프로젝트 범위)
cp 05-mcp/github-mcp.json .mcp.json

# 또는 사용자 범위: ~/.claude.json에 추가
```

### Hooks
```bash
# Hook 설치
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 설정 파일(~/.claude/settings.json)에서 구성
```

### Plugins
```bash
# 예제에서 설치(게시된 경우)
claude --plugin-dir ./07-plugins/pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints
```bash
# 모든 사용자 프롬프트마다 Checkpoint가 자동 생성됩니다.
# 이전 상태로 되돌리려면 Esc를 두 번 누르거나 다음을 사용하세요.
/rewind

# 그런 다음, 이 중에 하나를 선택하세요: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, or Never mind
```

### 고급 기능
```bash
# 설정 파일(.claude/settings.json)에서 구성
# 09-advanced-features/config-examples.json 참고

# 계획 모드
/plan Task description

# 권한 모드(--permission-mode 플래그 사용)
# manual             - 모든 작업에 대해 승인 요청(구성 값 "default", v2.1.200부터 "manual"이 별칭)
# acceptEdits        - 파일 편집은 자동 승인, 그 외는 승인 요청
# plan               - 읽기 전용 분석, 수정 없음
# auto               - 백그라운드 분류기가 권한을 자동 결정
# dontAsk            - 사전 승인된 도구만 실행, 나머지는 모두 거부
# bypassPermissions  - 모든 작업 자동 승인(--permission-mode bypassPermissions, --dangerously-skip-permissions와 동일)

# 세션 관리
/resume                # 이전 대화 이어서 진행(인수 없으면 과거 세션 선택기)
/rename "name"         # 현재 세션 이름 변경
/fork [prompt]         # 대화를 새 백그라운드 세션으로 복사하고 여기서 계속 작업
/subtask <task>        # 대화를 상속하고 결과를 보고하는 포크된 서브에이전트 생성
/branch [name]         # 원본을 보존한 채 대화 사본으로 전환
claude -c              # 가장 최근 대화 이어서 진행
claude -r "session"    # 이름 또는 ID로 세션 재개
```

---

## 📋 기능 요약표

| 기능 | 설치 위치 | 사용 방법 |
|---------|-------------|-------|
| **Slash Commands (60+)** | `.claude/commands/*.md` | `/command-name` |
| **Memory** | `./CLAUDE.md` | 자동 로드 |
| **Skills** | `.claude/skills/*/SKILL.md` | 자동 호출 |
| **Subagents** | `.claude/agents/*.md` | 자동 위임 |
| **MCP** | `.mcp.json`(프로젝트) 또는 `~/.claude.json`(사용자) | `/mcp__server__action` |
| **Hooks (33개 이벤트)** | `~/.claude/hooks/*.sh` | 이벤트 기반 실행(5가지 유형) |
| **Plugins** | `/plugin install` 사용 | 모든 기능을 번들로 제공 |
| **Checkpoints** | 내장 | `Esc+Esc` 또는 `/rewind` |
| **Planning Mode** | 내장 | `/plan <task>` |
| **Permission Modes (6)** | 내장 | `--allowedTools`, `--permission-mode` |
| **Sessions** | 내장 | `/resume`, `/rename`, `/branch`, `/fork` |
| **Background Tasks** | 내장 | 백그라운드 실행 |
| **Remote Control** | 내장 | `claude --remote-control` 또는 `/remote-control` |
| **Web Sessions** | 내장 | `claude --cloud "task"` |
| **Git Worktrees** | 내장 | `claude -w <name>` |
| **Auto Memory** | 내장 | `~/.claude/projects/<project>/memory/`에 자동 저장 |
| **Task List** | 내장 | `Ctrl+T`(체크리스트), `/tasks`(백그라운드 작업) |
| **Bundled Skills** | 내장 | `/batch`, `/claude-api`, `/code-review [low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [pr#\|branch\|path]` *(Claude가 스스로 시작할 수도 있으며 v2.1.246부터 모든 환경에서 가능. 수준을 지정하지 않으면 마지막으로 입력한 수준을 재사용, v2.1.223)*, `/simplify` *(정리 전용 리뷰. v2.1.154부터 다시 `/code-review`와 별도 기능)*, `/debug`, `/fewer-permission-prompts`, `/loop`, `/run` *(v2.1.145+)*, `/run-skill-generator` *(v2.1.145+)*, `/verify` *(v2.1.145+, v2.1.215부터 명시적 호출 전용 — Claude가 스스로 실행하지 않음)* |

---

## 🎯 일반적인 사용 사례

### 코드 리뷰
```bash
# 방법 1: Slash Command
cp 01-slash-commands/optimize.md .claude/commands/
# 사용: /optimize

# 방법 2: Subagent
cp 04-subagents/code-reviewer.md .claude/agents/
# 사용: 자동 위임

# 방법 3: Skill
cp -r 03-skills/code-review-specialist ~/.claude/skills/
# 사용: 자동 호출

# 방법 4: Plugin (권장)
claude --plugin-dir ./07-plugins/pr-review
# 사용: /review-pr
```

### 문서 작성
```bash
# Slash Command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Plugin (완전한 솔루션)
/plugin install documentation
```

### DevOps
```bash
# 전체 Plugin 설치
/plugin install devops-automation

# 명령어: /deploy, /rollback, /status, /incident
```

### 팀 표준 관리
```bash
# 프로젝트 Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 팀에 맞게 수정
vim CLAUDE.md
```

### 자동화 및 Hooks
```bash
# Hook 설치(33개 이벤트, 5가지 유형: command, http, mcp_tool, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 예시:
# - 커밋 전 테스트: pre-commit.sh
# - 코드 자동 포맷: format-code.sh
# - 보안 검사: security-scan.sh

# 완전 자율 워크플로를 위한 Auto Mode
claude --permission-mode auto -p "Refactor and test the auth module"
# 또는 Shift+Tab으로 모드를 순환 전환
```

### 안전한 리팩터링
```bash
# 모든 프롬프트 전에 Checkpoint가 자동 생성됩니다.
# 리팩터링을 시도합니다.
# 성공하면 계속 진행합니다.
# 실패하면 Esc를 두 번 누르거나 /rewind를 사용하여 이전 상태로 되돌립니다.
```

### 복잡한 구현
```bash
# 계획 모드 사용
/plan Implement user authentication system

# Claude가 상세한 계획을 생성
# 검토 후 승인
# Claude가 체계적으로 구현 진행
```

### CI/CD 통합
```bash
# 헤드리스 모드에서 실행(비대화형). 권한 모드를 지정하지 않으면 -p는 Manual 모드로 시작합니다
# (구성 값 "default", v2.1.302+): 승인이 필요한 도구 호출은 거부되므로
# --allowedTools "Bash(npm test *)" 또는 --permission-mode auto를 추가하세요
claude -p "Run all tests and generate report"

# CI용 권한 모드 사용
claude -p "Run tests" --permission-mode dontAsk

# 완전 자율 CI 작업을 위한 Auto Mode 사용
claude --permission-mode auto -p "Run tests and fix failures"

# Hook를 이용한 자동화
# 09-advanced-features/README.md 참고
```

### 학습 및 실험
```bash
# 안전한 분석을 위해 계획 모드 사용
claude --permission-mode plan

# 안전하게 실험 - Checkpoint는 자동으로 생성됩니다.
# 이전 상태로 되돌리려면 Esc를 두 번 누르거나 /rewind를 사용하세요.
```

### Agent Teams
```bash
# Agent Teams 활성화
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# 또는 settings.json에서 설정
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }

# 다음과 같이 시작:
# "Implement feature X using a team approach"
```

### 예약 작업
```bash
# 5분마다 명령 실행
/loop 5m /check-status

# 일회성 알림: 자연어로 요청합니다(/loop는 취소할 때까지 반복)
remind me in 30 minutes to check the deploy
```

---

## 📁 파일 위치 참조

```text
프로젝트/
├── .claude/
│   ├── commands/              # Slash Command 저장 위치
│   ├── agents/                # Subagent 저장 위치
│   ├── skills/                # 프로젝트 Skill 저장 위치
│   └── settings.json          # 프로젝트 설정(Hook 등)
├── .mcp.json                  # MCP 설정(프로젝트 범위)
├── CLAUDE.md                  # 프로젝트 Memory
└── src/
    └── api/
        └── CLAUDE.md          # 디렉터리별 Memory

사용자 홈/
├── .claude/
│   ├── commands/              # 개인 명령어
│   ├── agents/                # 개인 Agent
│   ├── skills/                # 개인 Skill
│   ├── hooks/                 # Hook 스크립트
│   ├── settings.json          # 사용자 설정
│   └── CLAUDE.md              # 개인 Memory
└── .claude.json               # 개인 MCP 설정(사용자 범위)

시스템 디렉터리/               # macOS /Library/Application Support/ClaudeCode/, Linux /etc/claude-code/, Windows C:\Program Files\ClaudeCode\
├── managed-settings.json      # 관리되는 설정(Enterprise/Organization)
└── managed-settings.d/        # 관리되는 설정 드롭인
```

---

## 🔍 예제 찾기

### 카테고리별
- **Slash Commands**: `01-slash-commands/`
- **Memory**: `02-memory/`
- **Skills**: `03-skills/`
- **Subagents**: `04-subagents/`
- **MCP**: `05-mcp/`
- **Hooks**: `06-hooks/`
- **Plugins**: `07-plugins/`
- **Checkpoints**: `08-checkpoints/`
- **Advanced Features**: `09-advanced-features/`
- **CLI**: `10-cli/`

### 사용 사례별
- **성능 최적화**: `01-slash-commands/optimize.md`
- **보안**: `04-subagents/secure-reviewer.md`
- **테스트**: `04-subagents/test-engineer.md`
- **문서화**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### 난이도별
- **쉬움**: Slash Commands
- **중간**: Subagents, Memory
- **고급**: Skills, Hooks
- **완성형**: Plugins

---

## 🎓 학습 로드맵

### Day 1
```bash
# 개요 읽기
cat README.md

# 명령어 설치
cp 01-slash-commands/optimize.md .claude/commands/

# 실행
/optimize
```

### Day 2-3
```bash
# Memory 설정
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# Subagent 설치
cp 04-subagents/code-reviewer.md .claude/agents/
```

### Day 4-5
```bash
# MCP 설정
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# MCP 명령 실행
/mcp__github__list_prs
```

### Week 2
```bash
# Skill 설치
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# 자동 호출 사용
# 다음과 같이 입력하기만 하면 됩니다: "Review this code for issues"
```

### Week 3+
```bash
# 전체 Plugin 설치
claude --plugin-dir ./07-plugins/pr-review

# 번들 기능 사용
/review-pr
/check-security
/check-tests
```

---

## 주요 기능

| 기능 | 설명 | 사용 방법 |
|---------|-------------|-------|
| **Auto Mode** | 백그라운드 분류기를 이용한 완전 자율 실행. v2.1.207부터 Bedrock/Vertex/Foundry에서 기본적으로 사용 가능 | `Shift+Tab`으로 모드 전환 또는 `--permission-mode auto` |
| **Channels** | Discord 및 Telegram 통합 | `--channels` 플래그, Discord/Telegram 봇 |
| **Voice Dictation** | 음성으로 명령과 컨텍스트 입력 | `/voice` 명령 |
| **Output Styles** | Claude의 역할, 어조, 기본 응답 형식 변경 | `/config` → Output style 또는 `outputStyle` 설정. 기본 제공: Default, Proactive, Explanatory, Learning, Concise |
| **Status Line** | 명령어로 만드는 세션 하단 사용자 지정 상태 표시줄 | `/statusline` 또는 `statusLine` 설정. stdin으로 세션/모델/비용/컨텍스트 JSON을 받음 |
| **Hooks (33개 이벤트)** | 5가지 유형으로 확장된 Hook 시스템 | command, http, mcp_tool, prompt, agent Hook 유형 |
| **MCP Elicitation** | MCP 서버가 실행 중 사용자 입력을 요청 가능 | 서버가 추가 정보가 필요하면 자동으로 프롬프트 표시 |
| **Plugin LSP** | Plugin용 Language Server Protocol 지원 | `userConfig`, `${CLAUDE_PLUGIN_DATA}` 변수 |
| **Remote Control** | claude.ai 또는 Claude 앱에서 로컬 세션 조작 | `claude --remote-control`(또는 세션 안에서 `/remote-control`) |
| **Web Sessions** | claude.ai/code의 클라우드 세션 | 터미널에서 `claude --cloud "task"`로 시작 |
| **Desktop App** | 네이티브 데스크톱 애플리케이션 | `claude.ai/download`에서 다운로드 |
| **Task List** | 백그라운드 작업 관리 | `/tasks`(별칭 `/bashes`) |
| **Auto Memory** | 대화 내용을 자동으로 Memory에 저장 | Claude가 `~/.claude/projects/<project>/memory/MEMORY.md`에 메모를 저장하며 `/memory`로 관리 |
| **AGENTS.md** *(v2.1.277)* | 여러 도구에서 쓰는 프로젝트 컨텍스트 파일로, 작업 디렉터리나 그 상위에 `CLAUDE.md`가 없으면 프로젝트 지침으로 읽힘 | `/config`의 **Project instructions**에서 모드 전환. [AGENTS.md](02-memory/README.md#agentsmd) 참고 |
| **Git Worktrees** | 병렬 개발을 위한 격리된 작업 공간 | `claude --worktree <name>`(또는 `-w`) |
| **Model Selection** | Fable 5.1, Fable 5, Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5, Sonnet 4.6, Opus 4.8, Haiku 5.5, Haiku 4.5 간 모델 전환 | `/model`(Anthropic API에서 `sonnet`은 Sonnet 5.5로 해석, v2.1.284+) — v2.1.153부터 선택한 모델이 새 세션의 기본값으로 저장되며, `s`를 누르면 현재 세션에만 적용 |
| **Agent Teams** | 여러 Agent가 협업하여 작업 수행 | `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 환경 변수로 활성화(실험적) |
| **Dynamic Workflows** *(v2.1.154)* | 결정론적 멀티 Agent 오케스트레이션. v2.1.219부터 기본 크기 가이드라인은 중간(에이전트 10개 미만 목표) | `/workflows`로 실행 내역 확인, Claude에게 생성 요청, `/config`의 **Dynamic workflow size**로 크기 변경 |
| **Scheduled Tasks (세션 범위)** | 세션 안에서 `/loop`를 이용한 반복 작업 | `/loop 5m /command` 또는 CronCreate 도구 |
| **Chrome Integration** | 브라우저 자동화 | `--chrome` 플래그 또는 `/chrome` 명령 |
| **Keyboard Customization** | 사용자 지정 키 바인딩 | `/keybindings` 명령 |
| **/usage-credits** | 추가 사용량 한도 설정(v2.1.144에서 `/extra-usage`에서 이름 변경, 기존 이름도 별칭으로 사용 가능) | `/usage-credits` |
| **/run** *(v2.1.145+)* | 변경 사항이 적용된 프로젝트 앱 실행 | `/run` |
| **/verify** *(v2.1.145+)* | 빌드, 실행 및 동작 확인을 통해 수정 사항 검증(v2.1.215부터 명시적 호출 전용 — Claude가 스스로 실행하지 않음) | `/verify` |
| **/run-skill-generator** *(v2.1.145+)* | 특정 프로젝트에서 `/run`과 `/verify`를 사용할 수 있도록 설정 | `/run-skill-generator` |
| **Subagent Output Scanning** *(v2.1.210+)* | 서브에이전트 보고서에서 프롬프트 인젝션 패턴을 검사하고 무력화 | 기본적으로 켜져 있으며 끌 수 없음 |
| **WebSearch Cap and Subagent Fan-Out Limits** *(v2.1.212, v2.1.219에서 확장)* | 세션당 WebSearch 호출 200회(`-p`와 Agent SDK에서는 턴당). v2.1.290부터 대화형 세션에서는 시간당 100회씩 다시 채워짐. 동시 서브에이전트 상한(기본값 20)은 v2.1.217에서 추가. v2.1.219부터 서브에이전트는 **기본적으로 깊이 3**까지 중첩 서브에이전트를 생성할 수 있음(v2.1.217에서는 중첩이 비활성화되어 있었음). 세션당 서브에이전트 200개 생성 상한은 **v2.1.224에서 제거**되어, 이제 세션당 전체 서브에이전트 수에 제한이 없음 | `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`(기본값 200, `/clear`로 초기화), `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR`(대화형 기본값 100, `-p`에서는 0), `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`(기본값 20), `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`(기본값 3, 1로 설정하면 비활성화) |
| **Screen Reader Mode** *(v2.1.208)* | 스크린 리더용 일반 텍스트 렌더링 모드 | `--ax-screen-reader` 플래그, 셸에서 `CLAUDE_AX_SCREEN_READER=1`, 또는 사용자 설정(`~/.claude/settings.json`), 관리되는 설정, `--settings` 파일의 `"axScreenReader": true` — v2.1.305부터 프로젝트 및 로컬 설정에서는 무시됨 |
| **Restricted Mode** *(v2.1.248+)* | `--tools`가 개별적으로 지정하지 않는 한(`default` 프리셋으로는 안 됨) 명령어나 코드를 실행하는 기본 제공 도구(Bash, PowerShell 등)와 WebFetch를 제외하고, 사용자·프로젝트·로컬 설정을 무시하며(관리되는 설정과 `--settings`는 계속 적용), 파일 도구를 작업 디렉터리로 제한하고, `bypassPermissions`와 클라우드 세션을 거부 | `claude --restricted` 또는 `CLAUDE_CODE_RESTRICTED=1` |
| **Subagent Cache TTL** *(v2.1.248+)* | 에이전트 프런트매터의 `experimental.cacheTtl` 필드로 서브에이전트 프롬프트 캐시 유지 시간 설정 | 에이전트 프런트매터에 `experimental:`과 `cacheTtl: "5m"`(또는 `"1h"`) 추가. [Subagents](04-subagents/README.md) 참고 |
| **Forced Subagent Model** *(v2.1.257+)* | `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`로 `CLAUDE_CODE_SUBAGENT_MODEL`이 에이전트 프런트매터를 재정의. v2.1.251부터 이 환경 변수는 기본적으로 우선하지 않으며, 이 값을 설정하지 않으면 프런트매터(`model: inherit` 포함)가 우선함 | `CLAUDE_CODE_SUBAGENT_MODEL=sonnet CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1 claude` |

---

## Tips & Tricks

### 사용자 지정
- 먼저 예제를 그대로 사용해 보세요.
- 필요에 맞게 수정하세요.
- 팀과 공유하기 전에 테스트하세요.
- 설정 파일을 버전 관리하세요.

### 모범 사례
- 팀 표준은 Memory를 사용하세요.
- 완전한 워크플로에는 Plugin을 사용하세요.
- 복잡한 작업에는 Subagent를 사용하세요.
- 빠른 작업에는 Slash Command를 사용하세요.


### 문제 해결
```bash
# 파일 위치 확인
ls -la .claude/commands/
ls -la .claude/agents/

# YAML 문법 확인
head -20 .claude/agents/code-reviewer.md

# MCP 연결 확인
echo $GITHUB_PERSONAL_ACCESS_TOKEN
```

---

## 📊 기능 매트릭스

| 필요 사항 | 사용할 기능 | 예제 |
|------|----------|---------|
| 빠른 단축 명령 | Slash Command (60+) | `01-slash-commands/optimize.md` |
| 팀 표준 | Memory | `02-memory/project-CLAUDE.md` |
| 자동 워크플로 | Skill | `03-skills/code-review-specialist/` |
| 전문 작업 | Subagent | `04-subagents/code-reviewer.md` |
| 외부 데이터 | MCP (+ Elicitation) | `05-mcp/github-mcp.json` |
| 이벤트 자동화 | Hook (33개 이벤트, 5가지 유형) | `06-hooks/pre-commit.sh` |
| 완전한 솔루션 | Plugin (+ LSP 지원) | `07-plugins/pr-review/` |
| 안전한 실험 | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| 완전 자율 실행 | Auto Mode | `--permission-mode auto` 또는 `Shift+Tab` |
| 채팅 플랫폼 연동 | Channels | `--channels` (Discord, Telegram) |
| CI/CD 파이프라인 | CLI | `10-cli/README.md` |

---

## 🔗 빠른 링크

- **메인 가이드**: `README.md`
- **전체 색인**: `INDEX.md`
- **원본 가이드**: `claude_concepts_guide.md`

---

## 📞 자주 묻는 질문

**Q: 어떤 기능부터 사용해야 하나요?**
A: 먼저 Slash Command부터 시작하고, 필요에 따라 기능을 추가하세요.

**Q: 여러 기능을 함께 사용할 수 있나요?**
A: 네! 서로 함께 사용할 수 있습니다. Memory + Commands + MCP를 조합하면 더욱 강력하게 활용할 수 있습니다.

**Q: 팀과 공유하려면 어떻게 하나요?**
A: `.claude/` 디렉터리를 Git에 커밋하세요.

**Q: 비밀 정보는 어떻게 관리하나요?**
A: 환경 변수를 사용하고, 절대로 하드코딩하지 마세요.

**Q: 예제를 수정해도 되나요?**
A: 물론입니다! 예제는 자유롭게 사용자 환경에 맞게 수정할 수 있는 템플릿입니다.

---

## ✅ 체크리스트

시작하기 체크리스트:

- [ ] `README.md` 읽기
- [ ] Slash Command 1개 설치
- [ ] 명령 실행해 보기
- [ ] 프로젝트 `CLAUDE.md` 생성
- [ ] Subagent 1개 설치
- [ ] MCP 연동 1개 설정
- [ ] Skill 1개 설치
- [ ] 완전한 Plugin 사용해 보기
- [ ] 필요에 맞게 사용자 지정
- [ ] 팀과 공유하기

---

**빠른 시작**: `cat README.md`

**전체 색인**: `cat INDEX.md`

**이 참조 카드**: 빠르게 참고할 수 있도록 가까이에 보관하세요!

---

**최종 업데이트**: 2026년 10월 26일
**Claude Code 버전**: 2.1.310
**출처**:
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/memory#agents-md
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/cli-reference
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/env-vars
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/memory#storage-location
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/managed-settings
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/code-review-local
- https://code.claude.com/docs/en/changelog#2-1-307
- https://code.claude.com/docs/en/settings-reference#axscreenreader
- https://code.claude.com/docs/en/headless
- https://code.claude.com/docs/en/permission-modes#tool-calls-denied-in-claude-p-and-agent-sdk-runs
- https://code.claude.com/docs/en/tools-reference#session-search-limit
- https://code.claude.com/docs/en/routines
**호환 모델**: Claude Fable 5.1, Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
