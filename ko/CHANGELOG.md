# 변경 로그

## [v2.1.160] — 2026-06-02

### Claude Code v2.1.160와 동기화

튜토리얼 범위가 Claude Code v2.1.160 릴리스까지 확장되었습니다. 중간에 있었던 v2.1.156 동기화(Claude Opus 4.8, #129)는 문서에는 적용되었으나 별도로 변경 로그에 기록되지 않았습니다. 이 항목은 해당 시점부터 v2.1.157–v2.1.160 사이의 변경 사항을 다룹니다. 이 범위에서 치명적인 변경 사항은 없었으며, 몇 가지 새로운 CLI/기능 표면 추가와 정기적인 푸터 업데이트가 있었습니다. 타사 공급자의 자동 모드는 새로운 기본 설정이 아니라 **선택 사항**입니다.

### 추가됨

- **`claude plugin init <name>` (v2.1.157)** — `.claude/skills`에 새 플러그인을 직접 스캐폴딩합니다. 여기에 배치된 플러그인은 이제 마켓플레이스 없이 자동으로 로드됩니다. `10-cli/README.md`, `07-plugins/README.md`, `CATALOG.md`에 문서화되어 있습니다.
- **Bedrock / Vertex / Foundry의 자동 모드 (v2.1.158)** — Opus 4.7/4.8용 세 가지 타사 공급자에서 자동 모드를 사용할 수 있으며, `CLAUDE_CODE_ENABLE_AUTO_MODE=1` 환경 변수를 통해 **선택 사항**으로 활성화할 수 있습니다. `09-advanced-features/README.md`, `10-cli/README.md`, `CATALOG.md`에 문서화되어 있습니다.
- **세션 중 `EnterWorktree` 전환 (v2.1.157)** — `EnterWorktree` 도구를 통해 이제 세션 내에서 Claude가 관리하는 작업 트리 간에 전환할 수 있으며, 완료된 작업 트리는 잠금 해제 상태로 유지되어 `git worktree remove`/`prune` 명령으로 정리할 수 있습니다. `09-advanced-features/README.md`에 문서화되어 있습니다.

### 동작 변경

- **`acceptEdits` 쓰기 안전 프롬프트 (v2.1.160)** — `acceptEdits` 모드에서도 Claude Code는 이제 셸 시작 파일(`.zshenv`, `.zlogin`, `.bash_login`, `~/.config/git/`) 및 코드 실행 빌드 구성 파일(`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`, `.pre-commit-config.yaml`, `.devcontainer/`)에 쓰기 전에 프롬프트를 표시합니다. 이는 의도치 않은 명령 실행으로 이어질 수 있기 때문입니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- **동적 워크플로우 트리거 키워드 `workflow` → `ultracode` (v2.1.160)** — "workflow" 단독으로는 더 이상 동적 워크플로우를 실행하지 않으며, 트리거 키워드는 이제 `ultracode`입니다. `09-advanced-features/README.md`에 명시되어 있습니다.

### 제거됨

- **`CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE`가 이제 아무런 동작도 하지 않음 (v2.1.160)** — 해당 환경 변수는 제거되었으며 이제 아무런 효과가 없습니다. `10-cli/README.md`의 환경 변수 표 설명은 "2026-06-01 제거됨"에서 "제거됨 (v2.1.160부터 아무런 동작도 하지 않음)"으로 업데이트되었습니다.

### 문서

- `README.md` 내부에 일관성이 없었던 세 가지 버전 문자열(배지 및 FAQ 본문이 `2.1.145` / `v2.1.150`에 머물러 있었음)을 수정하고 오래된 소스 링크를 정규화했습니다.
- 일관된 동기화를 위해 모든 영어 문서의 메타데이터 푸터가 **v2.1.160 / 2026년 6월 2일**로 업데이트되었습니다.

## [v2.1.150] — 2026-05-25

### Claude Code v2.1.150와 동기화

튜토리얼 범위가 Claude Code v2.1.145 → v2.1.150 (2026년 5월 23일 릴리스)로 확장되었습니다. 마지막 동기화 이후 Anthropic은 5개의 패치(v2.1.146부터 v2.1.150까지)를 제공했습니다. 주요 변경 사항은 **번들된 `/simplify` 스킬이 `/code-review`로 이름 변경** (v2.1.146)된 것입니다. 이는 **별칭 없이** 순수하게 이름만 변경되었으므로 이전 이름은 더 이상 작동하지 않습니다. 이 리포지토리에는 자체 로컬 코드 검토 스킬도 포함되어 있으므로, 새로운 내장 스킬을 가리지 않도록 디렉토리 이름이 `code-review-specialist`로 변경되었습니다. 기타 주요 변경 사항으로는 `/usage`가 이제 범주별로 비용을 분류하고, 백그라운드 세션을 `Ctrl+T`로 고정할 수 있으며, 마크다운 렌더러가 GFM 작업 목록 확인란을 지원하고, 새로운 `allowAllClaudeAiMcps` 관리 설정이 추가되었습니다. 이 동기화는 또한 v2.1.143에 고정되어 있던 4개의 모듈 README(`04-subagents`, `05-mcp`, `07-plugins`, `09-advanced-features`)를 업데이트했습니다.

### 동작 변경

- **`/simplify`가 `/code-review`로 이름 변경됨 (v2.1.146)**: 번들된 검토 스킬은 이제 `/code-review`로 호출되며 선택적 노력 수준(예: `/code-review high`)을 사용할 수 있습니다. `--comment`를 전달하여 GitHub PR 인라인 댓글로 발견 사항을 게시할 수 있습니다(v2.1.147). 이전 `/simplify` 이름은 더 이상 작동하지 않으며, 별칭도 없습니다. `01-slash-commands/README.md`, `03-skills/README.md`, `CATALOG.md`, `QUICK_REFERENCE.md`, `claude_concepts_guide.md`에 업데이트되었습니다.

### 변경됨

- **리포지토리의 로컬 `code-review` 스킬을 `code-review-specialist`로 이름 변경**하여 새로운 내장 `/code-review`와 충돌을 피했습니다. 디렉토리 `03-skills/code-review/` → `03-skills/code-review-specialist/`로 변경되었으며, 모든 설치 명령, 디렉토리 트리 및 상호 참조가 `README.md`, `QUICK_REFERENCE.md`, `INDEX.md`, `CATALOG.md`, `LEARNING-ROADMAP.md`, `claude_concepts_guide.md`, `03-skills/README.md`에 업데이트되었습니다. 충돌과 내장 스킬을 가리지 않는 방법에 대한 설명도 추가되었습니다.

### 추가됨

- **`/usage` 범주별 비용 분석 (v2.1.149)** — 이제 비용 보기에 지출이 범주별(스킬, 서브 에이전트, 플러그인, MCP 서버별 비용)로 분류되어 표시됩니다. `CATALOG.md` 및 `claude_concepts_guide.md`에 문서화되어 있습니다.
- **고정된 백그라운드 세션 — `Ctrl+T` (v2.1.147)** — `claude agents`에서 세션을 고정하면 유휴 상태일 때 세션을 활성 상태로 유지하고, Claude Code 업데이트를 적용하기 위해 제자리에서 다시 시작하며, 메모리 압박 시 고정되지 않은 세션 이후에만 종료됩니다. `10-cli/README.md`에 문서화되어 있습니다.
- **GFM 작업 목록 확인란 렌더링 (v2.1.149)** — 마크다운 렌더러가 이제 `- [ ]` / `- [x]`를 확인란으로 렌더링합니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- **`allowAllClaudeAiMcps` 관리 설정 (v2.1.149)** — claude.ai 클라우드 MCP 커넥터를 조직 전체에서 로드할 수 있도록 허용합니다. `05-mcp/README.md`에 문서화되어 있습니다.

### 제거됨

- **Stop/SubagentStop 훅 입력 필드 `background_tasks` 및 `session_crons`** — `06-hooks/README.md` 및 `resources.md`에서 제거되었습니다. 이들은 v2.1.145 릴리스 노트에서 추가되었지만 공식 훅 참조 페이지에는 열거되어 있지 않아 게시된 참조와 문서의 일관성을 유지하기 위해 제거되었습니다.

### 문서

- v2.1.143에서 v2.1.150으로 4개의 모듈 README를 업데이트했습니다: `04-subagents/README.md`, `05-mcp/README.md`, `07-plugins/README.md`, `09-advanced-features/README.md`.
- 일관된 동기화를 위해 모든 영어 문서의 메타데이터 푸터가 **v2.1.150 / 2026년 5월 25일**로 업데이트되었습니다.

## [v2.1.145] — 2026-05-20

### Claude Code v2.1.145와 동기화

튜토리얼 범위가 Claude Code v2.1.143 → v2.1.145 (2026년 5월 19일 릴리스)로 확장되었습니다. 마지막 동기화 이후 Anthropic은 두 개의 패치(v2.1.144 및 v2.1.145)를 제공했습니다. 주요 변경 사항: `/extra-usage`가 `/usage-credits`로 이름 변경, `/model`이 기본적으로 세션 전용으로 변경, 세 가지 새로운 번들 스킬(`/run`, `/verify`, `/run-skill-generator`) 추가, Stop/SubagentStop 훅 입력 필드 `background_tasks` 및 `session_crons` 추가, 스크립팅을 위한 `claude agents --json` 추가, 그리고 베어 환경 변수 Bash 자동 승인 취약점을 해결하는 보안 수정이 있었습니다. 이 동기화는 또한 v2.1.143 동기화에서 누락되어 여전히 v2.1.138에 고정되어 있던 6개의 최상위 참조 문서(`LEARNING-ROADMAP.md`, `QUICK_REFERENCE.md`, `INDEX.md`, `resources.md`, `claude_concepts_guide.md`, `STYLE_GUIDE.md`)를 업데이트했습니다.

### 추가됨

- `/usage-credits` 슬래시 명령 (v2.1.144) — `/extra-usage`를 대체하는 기본 이름입니다. `/extra-usage`는 여전히 별칭으로 작동합니다. `01-slash-commands/README.md` 및 `CATALOG.md`에 문서화되어 있습니다.
- 세 가지 새로운 번들 스킬 (v2.1.145) — `/run` (변경 사항이 실행되는 것을 확인하기 위해 프로젝트 앱을 시작함), `/verify` (수정 사항이 작동하는지 확인하기 위해 앱을 빌드, 실행 및 관찰함), `/run-skill-generator` (프로젝트별 스킬을 생성하여 `/run`/`/verify`가 특정 프로젝트를 처리하는 방법을 가르침). `03-skills/README.md`, `CATALOG.md`, `QUICK_REFERENCE.md`에 문서화되어 있습니다. 번들 스킬의 표준 개수를 **9개**로 늘립니다.
- Stop/SubagentStop 훅 입력 필드 `background_tasks` 및 `session_crons` (v2.1.145) — 훅 작성자는 이를 읽어 백그라운드 작업이나 예약된 작업이 아직 보류 중인 동안 중지를 차단할지 결정할 수 있습니다. `06-hooks/README.md`에 문서화되어 있습니다.
- `claude agents --json` (v2.1.145) — 스크립팅(상태 표시줄, 세션 선택기, tmux-resurrect)을 위해 에이전트 목록을 기계가 읽을 수 있는 JSON 형식으로 출력합니다. `10-cli/README.md`에 문서화되어 있습니다.
- 요약 표에서 누락되었던 5개의 훅 이벤트 행 — `Setup`, `UserPromptExpansion`, `PermissionDenied`, `PostToolBatch` (설명에서는 이미 "29개 이벤트"라고 주장했지만, `CATALOG.md`, `claude_concepts_guide.md`, `INDEX.md`의 요약 표에는 25개만 나열되어 있었습니다).

### 동작 변경

- **`/model`이 기본적으로 세션 전용으로 변경됨 (v2.1.144)**: 모델 선택은 이제 현재 세션에만 적용됩니다. 선택 후 `d`를 눌러 향후 세션을 위한 새로운 기본값으로 설정할 수 있습니다. `01-slash-commands/README.md`에 문서화되어 있습니다.
- **Bash 베어 env-var 자동 승인 취약점 해결 (v2.1.145 보안 수정)**: `FOO=bar somecommand` 형식의 명령은 `FOO=bar`만 허용 목록에 있었을 때 더 이상 자동 승인되지 않습니다. 전체 명령을 포함하는 `Bash(...)` 권한 규칙을 통해 해당 명령을 명시적으로 다시 허용해야 합니다. `06-hooks/README.md`에 문서화되어 있습니다.
- **`context: fork` 무한 루프 수정 (v2.1.145)**: `context: fork`를 사용하는 스킬이 이전에 드물게 무한 재호출 루프를 트리거할 수 있었습니다. `03-skills/README.md`에 참고 사항으로 문서화되어 있습니다.

### 문서

- v2.1.138에서 v2.1.145로 6개의 최상위 참조 문서(`LEARNING-ROADMAP.md`, `QUICK_REFERENCE.md`, `INDEX.md`, `resources.md`, `claude_concepts_guide.md`, `STYLE_GUIDE.md`)를 업데이트했습니다.
- 번들 스킬 불일치를 수정했습니다 — `CATALOG.md`, `QUICK_REFERENCE.md`, `03-skills/README.md`는 이전에 세 가지 다른 5개 항목 목록을 나열했습니다. 이를 표준 9개(`/batch`, `/claude-api`, `/debug`, `/fewer-permission-prompts`, `/loop`, `/run`, `/run-skill-generator`, `/simplify`, `/verify`)로 조정했습니다. `QUICK_REFERENCE.md` 셀에는 `/voice`와 `/browse`가 번들 스킬로 잘못 나열되어 있었는데, 둘 다 번들 스킬이 아닙니다.
- `QUICK_REFERENCE.md` 및 `resources.md`에서 "New Features (March 2026)" → "New Features (May 2026)"로 이름을 변경하여 리포지토리의 다른 부분과 일치시켰습니다.
- `README.md`의 버전 배지를 `2.1.138`에서 `2.1.145`로 업데이트하고 본문의 "latest: v2.1.138" 두 가지 주장을 업데이트했습니다.
- 기여자들이 현재 버전을 복사하도록 STYLE_GUIDE 샘플 메타데이터 푸터를 `2.1.97`에서 `2.1.145`로 업데이트했습니다.

## [v2.1.143] — 2026-05-19

### Claude Code v2.1.143와 동기화

튜토리얼 범위가 Claude Code v2.1.138 → v2.1.143 (2026년 5월 15일 릴리스)로 확장되었습니다. 마지막 동기화 이후 Anthropic은 5개의 패치(v2.1.139–v2.1.143)를 제공했습니다. 주요 변경 사항: `/goal` 및 `/scroll-speed` 슬래시 명령, 전체 디스패치 플래그 세트가 포함된 `claude agents` 에이전트 뷰(연구 미리보기), Stop 훅 안전 제한, 훅 실행 형식(`args`), PostToolUse의 `continueOnBlock`, 훅 `terminalSequence` 출력, Opus 4.7을 기본으로 하는 빠른 모드, Bedrock/Vertex/Foundry용 Windows에서 PowerShell 기본 설정, 그리고 `worktree.bgIsolation` 설정이 추가되었습니다.

### 추가됨

- `/goal <statement>` 슬래시 명령 (v2.1.139) — 경과 시간, 턴 수, 토큰 사용량을 보여주는 실시간 오버레이 패널과 함께 세션 수준 완료 조건을 등록합니다. `01-slash-commands/README.md`에 문서화되어 있으며 `10-cli/README.md`에서 상호 연결되어 있습니다.
- `/scroll-speed <±N>` 슬래시 명령 (v2.1.139) — TUI 실시간 미리보기 스크롤 속도를 조정하며, 머신별로 유지됩니다. `01-slash-commands/README.md`에 문서화되어 있습니다.
- `claude agents` 에이전트 뷰 (연구 미리보기, v2.1.139)와 디스패치 플래그 `--cwd` (v2.1.141), `--add-dir`, `--settings`, `--mcp-config`, `--plugin-dir`, `--permission-mode`, `--model`, `--effort`, `--dangerously-skip-permissions` (v2.1.142)가 추가되었습니다. `10-cli/README.md`에 문서화되어 있습니다.
- `claude plugin details <name>` (v2.1.139) — 전체 플러그인 목록과 턴별/호출별 예상 토큰 비용 추정치를 제공합니다. v2.1.142에서는 세부 정보 창에 LSP 서버가 추가되었습니다. `07-plugins/README.md`에 문서화되어 있습니다.
- `/plugin` 찾아보기 창에 마켓플레이스 컨텍스트 비용 예상치 (v2.1.143)가 추가되었습니다. `07-plugins/README.md`에 문서화되어 있습니다.
- 훅 **실행 형식** (`args: string[]`, v2.1.139) — 셸 파싱 없이 직접 `execve()`를 생성하며, 셸 형식 `command` 필드와 상호 배타적입니다. `06-hooks/README.md`에 문서화되어 있습니다.
- PostToolUse의 훅 `continueOnBlock: true` 필드 (v2.1.139) — 차단된 도구 결과를 턴을 중단하는 대신 `tool_result`로 Claude에 다시 전달합니다. `06-hooks/README.md`에 문서화되어 있습니다.
- 훅 `terminalSequence` JSON 출력 필드 (v2.1.141) — 데스크톱 알림, 창 제목 및 벨소리를 위한 원시 OSC 이스케이프 시퀀스를 방출합니다. `06-hooks/README.md`에 문서화되어 있습니다.
- `worktree.bgIsolation: "none"` 설정 (v2.1.143) — 백그라운드 세션은 격리된 작업 트리 대신 현재 작업 복사본을 직접 편집합니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- `CLAUDE_PROJECT_DIR`은 이제 모든 MCP stdio 서버의 환경으로 전달되며 (v2.1.139), 플러그인 및 프로젝트 `.mcp.json` `command`/`args`/`env` 필드에서 `${CLAUDE_PROJECT_DIR}` 대체가 지원됩니다. `05-mcp/README.md`에 문서화되어 있습니다.
- 서브 에이전트 OTEL 헤더 `x-claude-code-agent-id` 및 `x-claude-code-parent-agent-id` (v2.1.139)는 `claude_code.llm_request` OTEL 스팬의 `agent_id` / `parent_agent_id` 속성으로 노출됩니다. `04-subagents/README.md`에 문서화되어 있습니다.
- `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1` (v2.1.142) — v2.1.142 기본값이 Opus 4.7로 변경된 후 빠른 모드를 Opus 4.6으로 되돌립니다. `10-cli/README.md`에 문서화되어 있습니다.
- `CLAUDE_CODE_USE_POWERSHELL_TOOL=0` 및 `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1` (v2.1.143) — 기본 활성화된 PowerShell 도구를 선택 해제하거나, `-ExecutionPolicy Bypass` 대신 시스템 실행 정책을 따르도록 설정합니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` (v2.1.143) — Stop 훅에 대한 8회 연속 블록 안전 제한을 재정의합니다(비활성화하려면 `0`으로 설정). `06-hooks/README.md` 및 `09-advanced-features/README.md`에 문서화되어 있습니다.
- `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` (v2.1.141) — SSH 키가 없는 CI 러너를 위해 플러그인 설치 시 GitHub 플러그인 소스를 HTTPS를 통해 강제로 클론하도록 합니다. `07-plugins/README.md`에 문서화되어 있습니다.
- `ANTHROPIC_WORKSPACE_ID` (v2.1.141) — 연합 워크로드 ID 토큰을 특정 작업 공간으로 범위 지정합니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- 최상위 `SKILL.md` 플러그인 패턴 (v2.1.142) — 최상위 `SKILL.md`만 있고 `skills/` 하위 디렉토리가 없는 플러그인은 단일 스킬로 표시됩니다. `07-plugins/README.md`에 문서화되어 있습니다.
- `/schedule`의 플러그인 마케팅 이름 **Routines** (Anthropic 블로그, 2026-05-14) — `09-advanced-features/README.md`에 한 줄 메모로 표시됩니다. CLI 표면은 `/schedule`로 유지됩니다.

### 동작 변경

- **빠른 모드 기본값이 Opus 4.7로 변경됨 (v2.1.142)**: `/fast`는 이제 기본적으로 Opus 4.7을 실행합니다(이전에는 Opus 4.6). `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1`을 설정하여 다시 선택할 수 있습니다.
- **Bedrock/Vertex/Foundry용 Windows에서 PowerShell 도구가 기본적으로 활성화됨 (v2.1.143)**: Claude Code는 `-ExecutionPolicy Bypass`로 PowerShell을 호출합니다. `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1` (시스템 정책 따르기) 또는 `CLAUDE_CODE_USE_POWERSHELL_TOOL=0` (도구 비활성화)으로 선택 해제할 수 있습니다.
- **API 키 인증 설정 시 원격 제어, `/schedule`, claude.ai MCP 커넥터 및 알림 기본 설정 자동 비활성화 (v2.1.139)**: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, 또는 `apiKeyHelper`를 설정하면 claude.ai 로그인도 활성화되어 있더라도 4가지 claude.ai 연결 표면이 모두 비활성화됩니다.
- **Stop 훅 블록 루프가 8회 연속 블록으로 제한됨 (v2.1.143)**: 8회 연속 블록 이후 세션이 경고와 함께 종료되어 버그가 있는 Stop 훅이 세션을 무한정 반복하는 것을 방지합니다. `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`으로 재정의할 수 있습니다.
- **`subagent_type` 매칭이 이제 대소문자 및 구분자 비구분으로 변경됨 (v2.1.140)**: `code-reviewer`, `Code Reviewer`, `code_reviewer` 모두 동일한 에이전트로 해석됩니다. `04-subagents/README.md`에 문서화되어 있습니다.

### 변경됨

- `Setup` 훅이 v2.1.138에 추가된 후, 최상위 참조 문서(`README.md`, `CATALOG.md`)가 `28 hook events`에서 `29 hook events`로 업데이트되었습니다. 이는 `06-hooks/README.md` 및 `LEARNING-ROADMAP.md`와 일치합니다.

### 번역자를 위한 참고 사항

- 튜토리얼 번역(`vi/`, `ja/`, `uk/`, `zh/`)은 영어를 따릅니다. 이번 라운드의 모듈 README 및 위 변경 로그의 차이점을 동기화하십시오. 푸터는 `최종 업데이트: 2026년 5월 19일` 및 `Claude Code 버전: 2.1.143`을 반영해야 합니다.

## [v2.1.138] — 2026-05-09

### Claude Code v2.1.138와 동기화

튜토리얼 범위가 Claude Code v2.1.131 → v2.1.138 (2026년 5월 9일 릴리스)로 확장되었습니다. 마지막 동기화 이후 Anthropic은 v2.1.132부터 v2.1.138까지 7개의 패치를 제공했습니다.

### 추가됨 (영문 문서)

- `worktree.baseRef` 설정 (v2.1.133) — `claude --worktree`가 `origin/<default>` (`"fresh"`, 기본값)에서 분기할지 아니면 로컬 `HEAD` (`"head"`)에서 분기할지 제어합니다. **동작 변경**: `"fresh"` 기본값은 v2.1.128의 동작을 되돌리므로, v2.1.128 이후 로컬 `HEAD` 분기에 의존했던 사용자는 다시 선택해야 합니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- `autoMode.hard_deny` 관리 키 (v2.1.136) — 추론된 사용자 의도와 관계없이 특정 종류의 작업을 차단하는 분류자 규칙 배열입니다. 자동 모드에서 절대로 실행되어서는 안 되는 작업(예: `rm -rf /`, 보호된 브랜치로 강제 푸시)에 사용됩니다. `soft_deny`와 달리, 하드 거부 규칙은 분류자에 의해 협상되지 않습니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- `parentSettingsBehavior` 관리 키 (v2.1.133 이상, 관리자 등급) — SDK의 `managedSettings`가 상위 프로세스 설정과 병합되는 방식을 제어합니다. `"first-wins"`는 기존 우선 순위를 유지하고, `"merge"`는 값을 깊이 병합합니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- `Setup` 훅 이벤트 — 초기 환경 설정(세션당 1회); 도구를 프로비저닝하거나 종속성을 설치하는 데 사용합니다. 문서화된 훅 이벤트 총 개수가 28개에서 29개로 증가했습니다. `06-hooks/README.md`에 문서화되어 있습니다.
- 훅 입력 JSON의 `effort.level` 필드 (v2.1.133) — 활성 노력 수준(`low`/`medium`/`high`/`xhigh`/`max`)을 훅에 노출합니다. `06-hooks/README.md`에 문서화되어 있습니다.
- Bash 서브프로세스의 `CLAUDE_CODE_SESSION_ID` 환경 변수 (v2.1.132) — 훅 입력 JSON의 `session_id` 필드와 일치하는 세션 UUID로, Bash 로그를 훅 텔레메트리와 연관시키는 데 사용됩니다. `06-hooks/README.md`에 문서화되어 있습니다.
- Bash 서브프로세스의 `CLAUDE_EFFORT` 환경 변수 (v2.1.133) — 훅 입력 JSON의 `effort.level`과 일치하는 활성 노력 수준입니다. `06-hooks/README.md`에 문서화되어 있습니다.
- `sandbox.bwrapPath` 및 `sandbox.socatPath` 설정 (v2.1.133 이상, Linux/WSL) — `bubblewrap` 및 `socat`의 비표준 설치 위치를 Claude Code에 지정합니다. 기본값은 `$PATH` 검색입니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` 환경 변수 (v2.1.132). `09-advanced-features/README.md`에 문서화되어 있습니다.
- `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL` 환경 변수 (v2.1.136) — OpenTelemetry 데이터를 캡처하는 조직을 위해 세션 품질 설문조사를 다시 활성화합니다. OTEL 배포에서는 기본적으로 비활성화되어 있습니다. `09-advanced-features/README.md`에 문서화되어 있습니다.

### 변경됨

- **동작 변경**: 계획 모드는 이제 `permissions.allow`에 일치하는 `Edit(...)` 규칙이 있는 경우에도 모든 파일 쓰기를 무조건 차단합니다(v2.1.136). 이전에는 관대한 `Edit(...)` 규칙이 계획 모드에서 쓰기를 허용할 수 있었지만, 해당 우회 경로는 폐쇄되었습니다. 이전 동작에 의존했던 워크플로우는 편집 전에 계획 모드(`Shift+Tab`)를 종료해야 합니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- 플러그인 공백 슬래시 명령(예: `/myplugin review`)은 이제 `/myplugin:review`로 해석됩니다. 플러그인 `skills` 구성 항목은 더 이상 기본 `skills/` 디렉토리를 숨기지 않으며, 둘 다 병합됩니다. `07-plugins/README.md`에 문서화되어 있습니다.
- MCP 서버는 이제 `/clear` 명령을 실행해도 유지됩니다(v2.1.132 이상). `05-mcp/README.md`에 문서화되어 있습니다.
- 서브 에이전트는 스킬 도구(v2.1.133)를 통해 프로젝트, 사용자 및 플러그인 스킬을 검색합니다. `04-subagents/README.md`에 문서화되어 있습니다.
- `--permission-mode`는 이제 계획 모드 세션을 재개할 때 적용됩니다(v2.1.132). `09-advanced-features/README.md`에 문서화되어 있습니다.
- `CronList` 출력에 이제 한정자 및 예약된 프롬프트 본문이 포함되어(v2.1.136), 각 cron이 무엇을 실행할지 열어보지 않고도 감사할 수 있습니다. `09-advanced-features/README.md`에 문서화되어 있습니다.

### 수정됨

- OAuth 새로 고침 토큰 동시 새로 고침 경쟁 조건을 수정했습니다.
- INDEX.md 개수 불일치: 스킬 28 → 16, 플러그인 40 → 27, 훅 스크립트 8 → 9 (마크다운 콘텐츠 트리에서 다시 계산됨). 새로운 총계는 빌드 아티팩트 및 구성 대신 튜토리얼 콘텐츠에 개수를 제한하는 `.md` 전용 방법론을 반영합니다.
- `CATALOG.md` (v2.1.118 → v2.1.138) 및 `claude_concepts_guide.md` (v2.1.117 → v2.1.138)의 오래된 소스 URL을 수정했습니다. 개념 가이드에서 중복된 레거시 푸터를 제거했습니다.

### 번역 관리자를 위한 참고 사항

`vi/`, `zh/`, `uk/`, `ja/` 로컬라이즈된 트리는 커뮤니티에서 유지 관리되며 영어 원본보다 지연될 수 있습니다. 번역을 동기화하는 기여자는 이 릴리스에서 업데이트된 영어 파일과 차이점을 비교해야 합니다.

## [v2.1.131] — 2026-05-06

### Claude Code v2.1.131와 동기화

튜토리얼 범위가 Claude Code v2.1.126 → v2.1.131 (2026년 5월 6일 릴리스)로 확장되었습니다. 마지막 동기화 이후 Anthropic은 v2.1.128, v2.1.129, v2.1.131을 제공했습니다. v2.1.127 및 v2.1.130은 건너뛰어졌고 공개적으로 릴리스되지 않았습니다.

### 추가됨 (영문 문서)

- `--plugin-url <url>` 플래그 (v2.1.129) — 현재 세션을 위해 URL에서 플러그인 `.zip` 아카이브를 가져옵니다. 반복 가능합니다. `07-plugins/README.md`에 문서화되어 있습니다.
- `CLAUDE_CODE_FORCE_SYNC_OUTPUT` 환경 변수 (v2.1.129) — 자동 감지가 실패하는 터미널(예: Emacs `eat`)에 대해 동기식 출력을 강제합니다. `10-cli/README.md` 및 `09-advanced-features/README.md`에 문서화되어 있습니다.
- `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE` 환경 변수 (v2.1.129) — Homebrew/WinGet 설치(일반적으로 자동 업데이트되지 않음)에 대한 백그라운드 업그레이드를 활성화합니다. `10-cli/README.md` 및 `09-advanced-features/README.md`에 문서화되어 있습니다.
- `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` 환경 변수 (v2.1.129) — `/v1/models` 게이트웨이 검색에 옵트인하는 데 필요합니다(변경됨 섹션 참조). `10-cli/README.md`에 문서화되어 있습니다.
- `disableRemoteControl` 설정 (v2.1.128) — 관리자는 관리/정책 범위 설정을 통해 `claude remote-control` 및 `/remote-control`을 차단할 수 있습니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- `--plugin-dir`는 디렉토리 입력과 함께 `.zip` 아카이브를 허용합니다(v2.1.128). `07-plugins/README.md`에 문서화되어 있습니다.
- `skillOverrides`는 기존의 `"on"`/`"off"` 외에 `"name-only"` 및 `"user-invocable-only"`를 허용합니다(v2.1.129). `03-skills/README.md`에 문서화되어 있습니다.

### 변경됨

- **동작 변경**: 게이트웨이 `/v1/models` 검색이 이제 **선택 사항**으로 변경되었습니다(v2.1.129). 이전(v2.1.126)에는 `ANTHROPIC_BASE_URL`을 설정하면 게이트웨이의 `/v1/models` 엔드포인트에서 `/model`이 자동으로 채워졌습니다. v2.1.129부터는 사용자가 추가로 `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`을 설정해야 합니다. 이 환경 변수가 없으면 `/model`은 내장된 정적 목록으로 대체됩니다. `10-cli/README.md`에 문서화되어 있습니다.
- `/mcp`는 서버별 도구 수를 표시하고, 0개의 도구를 보고하는 서버를 시각적으로 표시합니다(v2.1.128). `05-mcp/README.md`에 문서화되어 있습니다.
- 인수가 없는 `/color`는 무작위 세션 색상을 선택합니다(v2.1.128). 명시적인 `/color <name|hex>`는 특정 색상을 계속 설정합니다. `01-slash-commands/README.md`에 문서화되어 있습니다.
- `--channels` 플래그는 이제 API 키(콘솔) 인증과 함께 작동합니다(v2.1.128). 이전 릴리스에서는 Pro/Max OAuth가 필요했습니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- Ctrl+R 기록 선택기는 기본적으로 **모든 프로젝트의 모든 프롬프트**를 표시합니다(v2.1.129). 선택기 내에서 Ctrl+S를 눌러 현재 프로젝트로 범위를 좁힐 수 있습니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- `/context`는 더 이상 ASCII 시각화를 대화에 덤프하지 않습니다(v2.1.129). 시각화는 UI 내에서만 표시되며, 호출당 약 1.6k 토큰 비용이 더 이상 발생하지 않습니다. `09-advanced-features/README.md`에 문서화되어 있습니다.
- 드래그 앤 드롭에서 너무 큰 이미지는 자동으로 축소됩니다(v2.1.128) — 이전 버전에서는 이미지를 즉시 거부했습니다.

### 수정됨

- Windows에서 VS Code 확장 활성화 문제를 수정했습니다(v2.1.131).
- Mantle 엔드포인트 인증 문제를 수정했습니다(v2.1.131).
- 1시간 프롬프트 캐시 TTL이 더 이상 5분으로 잘리지 않습니다(v2.1.129).
- 10MB보다 큰 stdin 페이로드에서 발생하는 충돌 문제를 수정했습니다(v2.1.128).

### 번역 관리자를 위한 참고 사항

`vi/`, `zh/`, `uk/`, `ja/` 로컬라이즈된 트리는 커뮤니티에서 유지 관리되며 영어 원본보다 지연될 수 있습니다. 번역을 동기화하는 기여자는 이 릴리스에서 업데이트된 영어 파일과 차이점을 비교해야 합니다.

## [v2.1.126] — 2026-05-02

### Claude Code v2.1.126와 동기화

튜토리얼 범위가 Claude Code v2.1.119 → v2.1.126 (2026년 5월 1일 릴리스)로 확장되었습니다. v2.1.120은 첫 릴리스 당일(2026년 4월 24일) 롤백되었지만, 원래 보고된 회귀 문제가 수정되어 2026년 4월 28일에 성공적으로 재릴리스되었습니다. v2.1.124와 v2.1.125는 Anthropic에 의해 건너뛰어졌고 릴리스되지 않았습니다.

### 추가됨 (영문 문서)

- `claude project purge [path]` 서브커맨드 (v2.1.126) — 프로젝트의 모든 Claude Code 상태(대화 기록, 작업, 디버그 로그, 파일 편집 기록, 프롬프트 기록, `~/.claude.json` 항목)를 삭제합니다. `--dry-run`, `-y/--yes`, `-i/--interactive`, `--all` 옵션을 지원합니다. `10-cli/README.md`에 문서화되어 있습니다.
- `claude plugin prune` 서브커맨드 (v2.1.121) — 고아 상태의 자동 설치된 플러그인 종속성을 제거합니다. `plugin uninstall --prune`은 연쇄적으로 작동합니다. `07-plugins/README.md`에 문서화되어 있습니다.
- `claude ultrareview [target]` 서브커맨드 (v2.1.120) — CI/스크립트에서 `/ultrareview`를 비대화형으로 실행하고, 발견 사항을 표준 출력으로 인쇄하며, 성공 시 0, 실패 시 1로 종료합니다. `--json` 및 `--timeout <minutes>` 옵션을 지원합니다. `10-cli/README.md`에 문서화되어 있습니다.
- 스킬 내용 내에서 `${CLAUDE_EFFORT}` 플레이스홀더 사용 가능 (v2.1.120) — 현재 노력 수준으로 해석됩니다. `03-skills/README.md`에 문서화되어 있습니다。
- `alwaysLoad` MCP 서버 구성 옵션 (v2.1.121) — `true`인 경우, 해당 서버의 모든 도구는 도구 검색 연기를 건너뜁니다. `05-mcp/README.md`에 문서화되어 있습니다.
- `PostToolUse.hookSpecificOutput.updatedToolOutput`은 이제 모든 도구에서 작동합니다(v2.1.121). 이전에는 MCP 전용이었습니다. `06-hooks/README.md`에 문서화되어 있습니다.
- `ANTHROPIC_BEDROCK_SERVICE_TIER` 환경 변수 (v2.1.122) — Bedrock 서비스 티어(`default`, `flex`, `priority`)를 선택합니다. `10-cli/README.md` 환경 변수 표에 문서화되어 있습니다.
- `--dangerously-skip-permissions` 확장 경로 적용 범위 (v2.1.121, v2.1.126) — 이제 `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/`, `.git/`, `.vscode/`, 셸 구성 파일에 대한 쓰기 프롬프트를 우회합니다. 치명적인 삭제 명령(`rm -rf /` 등)은 여전히 프롬프트를 표시합니다. `09-advanced-features/README.md`의 권한 모드 섹션에 문서화되어 있습니다.
- OAuth 코드 붙여넣기 폴백 (v2.1.126) — 브라우저 콜백이 localhost에 도달할 수 없을 때(WSL2, SSH, 컨테이너), `claude auth login`은 터미널에 붙여넣은 OAuth 코드를 허용합니다. `10-cli/README.md`에 문서화되어 있습니다.
- `/skills` 메뉴의 입력 필터링 기능 (v2.1.121). `03-skills/README.md`에 문서화되어 있습니다.
- `AI_AGENT` 환경 변수 (v2.1.120) — `gh`가 트래픽을 Claude Code에 귀속시킬 수 있도록 서브프로세스에 설정됩니다. `10-cli/README.md` 환경 변수 표에 문서화되어 있습니다.

### 변경됨

- `--from-pr` (v2.1.119) 및 `/resume` PR-URL 검색 (v2.1.122)은 이제 GitHub, GitHub Enterprise, GitLab 및 Bitbucket URL을 모두 지원합니다.
- Windows: Git for Windows / Git Bash는 더 이상 필요하지 않습니다(v2.1.120) — Git Bash가 없는 경우 Claude Code는 PowerShell을 셸 도구로 사용합니다. v2.1.126부터는 PowerShell 도구가 활성화되면 PowerShell이 기본 셸이 됩니다. Microsoft Store, PATH가 없는 MSI, 또는 `.NET 전역 도구`를 통해 설치된 PowerShell 7까지 감지 범위가 확장되었습니다. `09-advanced-features/README.md` 플랫폼 노트에 문서화되어 있습니다.
- `ANTHROPIC_BASE_URL`이 Anthropic 호환 게이트웨이를 가리킬 때, `/model` 선택기는 이제 게이트웨이의 `/v1/models` 엔드포인트에서 모델을 나열합니다(v2.1.126). `10-cli/README.md`에 문서화되어 있습니다.
- `--dangerously-skip-permissions`는 이제 훨씬 더 넓은 허용 목록에 대한 쓰기 프롬프트를 더 이상 표시하지 않습니다(추가됨 섹션 참조). 치명적인 제거 명령은 여전히 프롬프트를 표시합니다.
- 이미지 붙여넣기 자동 축소 (v2.1.126) — 2000px보다 큰 이미지는 붙여넣기 시 자동으로 축소됩니다. 기록에 있는 너무 큰 이미지는 자동으로 제거되고 요청이 재시도됩니다. (안전/UX 참고 사항으로서만 튜토리얼과 관련이 있습니다.)

### 보안

- 더 높은 우선순위의 관리 설정 소스에 `sandbox` 블록이 없을 때 `allowManagedDomainsOnly` / `allowManagedReadPathsOnly`가 무시되던 문제를 수정했습니다(v2.1.126).

### 번역 관리자를 위한 참고 사항

`vi/`, `zh/`, `uk/`, `ja/` 로컬라이즈된 트리는 커뮤니티에서 유지 관리되며 영어 원본보다 지연될 수 있습니다. 번역을 동기화하는 기여자는 이 릴리스에서 업데이트된 영어 파일과 차이점을 비교해야 합니다.

## [v2.4.0] — 2026-04-27

### Claude Code v2.1.119와 동기화

튜토리얼 범위가 Claude Code v2.1.112 → v2.1.119 (2026년 4월 23일 릴리스)로 확장되었습니다. v2.1.120은 4월 24일에 게시되었으나, 회귀 문제로 인해 같은 날 잠시 롤백된 후 4월 28일에 수정 사항과 함께 재릴리스되어 이제 일반 릴리스 라인의 일부가 되었습니다. 이후 v2.1.126 (2026년 5월 1일)은 다음 안정적인 목표이며 위 v2.1.126 항목에서 다루고 있습니다.

### 추가됨 (영문 문서)

- 네이티브 바이너리 패키징 참고 사항 (v2.1.113) — CLI는 이제 플랫폼별 네이티브 바이너리를 제공합니다.
- 네이티브 macOS/Linux 빌드에서 `bfs`/`ugrep` Glob/Grep 대체 각주 (v2.1.117)
- 예제와 함께 `mcp_tool` 훅 유형 (v2.1.118)
- PostToolUse / PostToolUseFailure 입력의 `duration_ms` 필드 (v2.1.119)
- `prUrlTemplate` 설정 (v2.1.119) 및 확장된 `--from-pr` 공급자 목록 (GitLab, Bitbucket)
- `cleanupPeriodDays` 확장 범위 (체크포인트 + 작업 + 셸 스냅샷 + 백업, v2.1.117)
- 모든 라이프사이클 이벤트에서 플러그인 마켓플레이스 강제 적용 (v2.1.117) 및 `hostPattern`/`pathPattern` 정규식 (v2.1.119)
- 새로운 환경 변수: `DISABLE_UPDATES`, `CLAUDE_CODE_HIDE_CWD`, `CLAUDE_CODE_FORK_SUBAGENT`, `OTEL_LOG_TOOL_DETAILS`, `ENABLE_TOOL_SEARCH` Vertex 선택적 참여
- 새로운 슬래시 명령: `/btw`, 사용자 정의 테마를 포함한 `/theme`
- `/usage` 표준 명령 ( `/cost` + `/stats` 병합, v2.1.118)
- 포크된 서브 에이전트 (`CLAUDE_CODE_FORK_SUBAGENT=1`, v2.1.117)
- 자동 모드 `"$defaults"` 토큰 (v2.1.118)
- `wslInheritsWindowsSettings` 관리 정책 (v2.1.118)
- Vim 시각/시각-라인 모드 (v2.1.118)
- `claude install [version]` 및 `claude plugin tag` 서브커맨드

### 변경됨

- 문서 호스트가 이전되었습니다: `docs.anthropic.com/en/docs/claude-code/*` → `code.claude.com/docs/en/*`
- Opus 4.7 노력 수준: `xhigh`는 2026년 4월 16일 출시 이후 Claude Code의 기본값이 되었습니다. Opus 4.7 네이티브 컨텍스트 창은 1M으로 확인되었습니다 (v2.1.117에서 `/context`가 200K로 잘못 계산하던 문제 수정).
- Pro/Max 구독자의 Opus 4.6 / Sonnet 4.6 기본 노력 수준이 `medium`에서 `high`로 상향 조정되었습니다 (v2.1.117).
- `STYLE_GUIDE.md`의 소스 URL이 Claude Apps 문서에서 `code.claude.com/docs/en/changelog`로 업데이트되었습니다.

### 사용 중단됨 (추적 중, 제거되지 않음)

- `includeCoAuthoredBy` 설정 → `attribution.commit` / `attribution.pr` 사용
- `voiceEnabled` 설정 → `voice.enabled` 사용

### 번역 관리자를 위한 참고 사항

`vi/`, `zh/`, `uk/` 로컬라이즈된 트리는 커뮤니티에서 유지 관리되며 영어 원본보다 지연될 수 있습니다. 번역을 동기화하는 기여자는 이 릴리스에서 업데이트된 영어 파일과 차이점을 비교해야 합니다.

## v2.1.112 — 2026-04-16

### 주요 변경 사항

- 모든 영어 튜토리얼을 Claude Code v2.1.112 및 새로운 Opus 4.7 모델(`claude-opus-4-7`)과 동기화했습니다. 여기에는 새로운 `xhigh` 노력 수준(Opus 4.7의 기본값으로 `high`와 `max` 사이), 두 가지 새로운 내장 슬래시 명령(`/ultrareview`, `/less-permission-prompts`), Opus 4.7 Max 구독자에게 더 이상 `--enable-auto-mode`가 필요 없는 자동 모드, Windows의 PowerShell 도구, "자동(터미널 일치)" 테마, 그리고 프롬프트 이름을 따서 명명된 계획 파일이 포함됩니다. 모든 18개 EN 문서 푸터는 Claude Code v2.1.112로 업데이트되었습니다. @Luong NGUYEN

### 기능

- 모든 모듈, 최상위 문서, 예제 및 참조에 걸쳐 완전한 우크라이나어(uk) 현지화 추가 (039dde2) @Evgenij I

### 버그 수정

- pre-tool-check.sh 훅 프로토콜 버그 수정 (bce7cf8) @yarlinghe
- CI 통과를 위해 잘못된 머메이드 예제를 텍스트 블록으로 변경 (b8a7b1f) @Evgenij I
- 우크라이나어 claude_concepts_guide.md ToC의 CP1251 인코딩 수정 (d970cc6) @Evgenij I
- 스텁 우크라이나어 README를 전체 번역으로 교체하고 깨진 앵커 수정 (f6d73e2) @Evgenij I
- 모든 푸터에 Claude Code 버전을 2.1.97로 수정 (63a1416) @Luong NGUYEN
- 2026-04-09 문서 정확성 업데이트 적용 (e015f39) @Luong NGUYEN

### 문서

- Claude Code v2.1.112 (Opus 4.7, `xhigh` 노력, `/ultrareview`, `/less-permission-prompts`, PowerShell 도구, 자동 일치 터미널 테마)와 동기화 @Luong NGUYEN
- Claude Code v2.1.110 (TUI, 푸시 알림, 세션 요약)과 동기화 (15f0085) @Luong NGUYEN
- `/team-onboarding`, `/ultraplan`, Monitor 도구와 함께 Claude Code v2.1.101과 동기화 (2deba3a) @Luong NGUYEN
- 베트남어 문서를 영어 원본과 동기화 (561c6cb) @Thiên Toán
- 모든 파일의 최종 업데이트 날짜 및 Claude Code 버전 업데이트 (7f2e773) @Luong NGUYEN
- 언어 전환기에 우크라이나어 링크 추가 (9c224ff) @Luong NGUYEN
- 기여자 섹션 제거 (f07313d) @Luong NGUYEN
- GitHub 지표를 21,800개 이상의 별, 2,585개 이상의 포크로 업데이트 (4f55374) @Luong NGUYEN

**전체 변경 로그**: https://github.com/luongnv89/claude-howto/compare/v2.3.0...v2.1.112

---

## v2.3.0 — 2026-04-07

### 기능

- 언어별 EPUB 아티팩트 빌드 및 게시 (90e9c30) @Thiên Toán
- 06-hooks에 누락된 pre-tool-check.sh 훅 추가 (b511ed1) @JiayuWang
- zh/ 디렉토리에 중국어 번역 추가 (89e89d4) @Luong NGUYEN
- 성능 최적화 서브 에이전트 및 종속성 확인 훅 추가 (f53d080) @qk

### 버그 수정

- Windows Git Bash 호환성 + stdin JSON 프로토콜 수정 (2cbb10c) @Luong NGUYEN
- 08-checkpoints의 autoCheckpoint 구성 문서 수정 (749c79f) @JiayuWang
- SVG 이미지를 자리 표시자로 대체하는 대신 임베드 (1b16709) @Thiên Toán
- 메모리 README의 중첩 코드 펜스 렌더링 수정 (ce24423) @Zhaoshan Duan
- 스쿼시 병합으로 누락된 검토 수정 사항 적용 (34259ca) @Luong NGUYEN
- 훅 스크립트가 Windows Git Bash와 호환되도록 하고 stdin JSON 프로토콜 사용 (107153d) @binyu li

### 문서

- 모든 튜토리얼을 최신 Claude Code 문서(2026년 4월)와 동기화 (72d3b01) @Luong NGUYEN
- 언어 전환기에 중국어 링크 추가 (6cbaa4d) @Luong NGUYEN
- 영어와 베트남어 간 언어 전환기 추가 (100c45e) @Luong NGUYEN
- GitHub #1 Trending 배지 추가 (0ca8c37) @Luong NGUYEN
- 컨텍스트 영역 모니터링을 위한 cc-context-stats 소개 (d41b335) @Luong NGUYEN
- luongnv89/skills 컬렉션 및 luongnv89/asm 스킬 관리자 소개 (7e3c0b6) @Luong NGUYEN
- 현재 GitHub 지표(5,900개 이상의 별, 690개 이상의 포크)를 반영하도록 README 통계 업데이트 (5001525) @Luong NGUYEN
- 현재 GitHub 지표(3,900개 이상의 별, 460개 이상의 포크)를 반영하도록 README 통계 업데이트 (9cb92d6) @Luong NGUYEN

### 리팩토링

- Kroki HTTP 종속성을 로컬 mmdc 렌더링으로 대체 (e76bbe4) @Luong NGUYEN
- 품질 검사를 pre-commit으로 이동, CI는 2차 통과로 사용 (6d1e0ae) @Luong NGUYEN
- 자동 모드 권한 기준선 좁히기 (2790fb2) @Luong NGUYEN
- auto-adapt 훅을 일회성 권한 설정 스크립트로 교체 (995a5d6) @Luong NGUYEN

### 기타

- 품질 게이트를 왼쪽으로 이동 — mypy를 pre-commit에 추가하고 CI 실패 수정 (699fb39) @Luong NGUYEN
- 베트남어 (Tiếng Việt) 현지화 추가 (a70777e) @Thiên Toán

**전체 변경 로그**: https://github.com/luongnv89/claude-howto/compare/v2.2.0...v2.3.0

---

## v2.2.0 — 2026-03-26

### 문서

- 모든 튜토리얼 및 참조를 Claude Code v2.1.84와 동기화 (f78c094) @luongnv89
  - 슬래시 명령을 55개 이상의 내장 + 5개의 번들 스킬로 업데이트하고, 3개는 사용 중단됨으로 표시
  - 훅 이벤트를 18개에서 25개로 확장하고, `agent` 훅 유형 추가 (현재 4개 유형)
  - 고급 기능에 자동 모드, 채널, 음성 받아쓰기 추가
  - `effort`, `shell` 스킬 프론트매터 필드 추가; `initialPrompt`, `disallowedTools` 에이전트 필드 추가
  - WebSocket MCP 전송, 유도, 2KB 도구 제한 추가
  - 플러그인 LSP 지원, `userConfig`, `${CLAUDE_PLUGIN_DATA}` 추가
  - 모든 참조 문서(CATALOG, QUICK_REFERENCE, LEARNING-ROADMAP, INDEX) 업데이트
- README를 랜딩 페이지 구조화된 가이드로 재작성 (32a0776) @luongnv89

### 버그 수정

- CI 준수를 위해 누락된 cSpell 단어 및 README 섹션 추가 (93f9d51) @luongnv89
- cSpell 사전에 `Sandboxing` 추가 (b80ce6f) @luongnv89

**전체 변경 로그**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### 버그 수정

- CI 링크 검사 실패의 원인이 되는 죽은 마켓플레이스 링크 제거 (3fdf0d6) @luongnv89
- cSpell 사전에 `sandboxed` 및 `pycache` 추가 (dc64618) @luongnv89

**전체 변경 로그**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### 기능

- 자기 평가 및 레슨 퀴즈 스킬을 통한 적응형 학습 경로 추가 (1ef46cd) @luongnv89
  - `/self-assessment` — 10가지 기능 영역에 걸친 대화형 숙련도 퀴즈와 개인화된 학습 경로
  - `/lesson-quiz [lesson]` — 8-10개의 목표 질문으로 구성된 레슨별 지식 확인

### 버그 수정

- 깨진 URL, 사용 중단된 항목, 오래된 참조 업데이트 (8fe4520) @luongnv89
- 리소스 및 자기 평가 스킬의 깨진 링크 수정 (7a05863) @luongnv89
- 개념 가이드의 중첩 코드 블록에 물결표 펜스 사용 (5f82719) @VikalpP
- cSpell 사전에 누락된 단어 추가 (8df7572) @luongnv89

### 문서

- 5단계 QA — 문서 전체의 일관성, URL 및 용어 수정 (00bbe4c) @luongnv89
- 3-4단계 완료 — 새로운 기능 적용 범위 및 참조 문서 업데이트 (132de29) @luongnv89
- MCP 컨텍스트 오버로드 섹션에 MCPorter 런타임 추가 (ef52705) @luongnv89
- 6개 가이드에 걸쳐 누락된 명령, 기능 및 설정 추가 (4bc8f15) @luongnv89
- 기존 리포지토리 규칙을 기반으로 스타일 가이드 추가 (84141d0) @luongnv89
- 가이드 비교 표에 자기 평가 행 추가 (8fe0c96) @luongnv89
- PR #7에 대한 기여자 목록에 VikalpP 추가 (d5b4350) @luongnv89
- README 및 로드맵에 자기 평가 및 레슨 퀴즈 스킬 참조 추가 (d5a6106) @luongnv89

### 새로운 기여자

- @VikalpP 님이 #7에서 첫 기여를 했습니다.

**전체 변경 로그**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### 기능

- 모든 문서를 Claude Code 2026년 2월 기능과 동기화 (487c96d)
  - 10개 튜토리얼 디렉토리와 7개 참조 문서에 걸쳐 26개 파일 업데이트
  - **자동 메모리** — 프로젝트별 영구 학습 기능 문서 추가
  - **원격 제어**, **웹 세션**, **데스크톱 앱** 문서 추가
  - **에이전트 팀** (실험적 다중 에이전트 협업) 문서 추가
  - **MCP OAuth 2.0**, **도구 검색**, **Claude.ai 커넥터** 문서 추가
  - 서브 에이전트용 **영구 메모리** 및 **작업 트리 격리** 문서 추가
  - **백그라운드 서브 에이전트**, **작업 목록**, **프롬프트 제안** 문서 추가
  - **샌드박싱** 및 **관리 설정** (엔터프라이즈) 문서 추가
  - **HTTP 훅** 및 7가지 새로운 훅 이벤트 문서 추가
  - **플러그인 설정**, **LSP 서버**, 마켓플레이스 업데이트 문서 추가
  - **체크포인트에서 요약** 되감기 옵션 문서 추가
  - 17가지 새로운 슬래시 명령(`/fork`, `/desktop`, `/teleport`, `/tasks`, `/fast` 등) 문서화
  - 새로운 CLI 플래그(`--worktree`, `--from-pr`, `--remote`, `--teleport`, `--teammate-mode` 등) 문서화
  - 자동 메모리, 노력 수준, 에이전트 팀 등을 위한 새로운 환경 변수 문서화

### 디자인

- 로고를 최소한의 팔레트를 가진 컴패스-괄호 모양으로 재디자인 (20779db)

### 버그 수정 / 정정

- 모델 이름 업데이트: Sonnet 4.5 → **Sonnet 4.6**, Opus 4.5 → **Opus 4.6**
- 권한 모드 이름 수정: 가상의 "Unrestricted/Confirm/Read-only"를 실제 `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions`로 교체
- 훅 이벤트 수정: 가상의 `PreCommit`/`PostCommit`/`PrePush`를 제거하고 실제 이벤트(`SubagentStart`, `WorktreeCreate`, `ConfigChange` 등) 추가
- CLI 구문 수정: `claude-code --headless`를 `claude -p` (인쇄 모드)로 교체
- 체크포인트 명령 수정: 가상의 `/checkpoint save/list/rewind/diff`를 실제 `Esc+Esc` / `/rewind` 인터페이스로 교체
- 세션 관리 수정: 가상의 `/session list/new/switch/save`를 실제 `/resume`/`/rename`/`/fork`로 교체
- 플러그인 매니페스트 형식 수정: `plugin.yaml` → `.claude-plugin/plugin.json`으로 마이그레이션
- MCP 구성 경로 수정: `~/.claude/mcp.json` → `.mcp.json` (프로젝트) / `~/.claude.json` (사용자)
- 문서 URL 수정: `docs.claude.com` → `docs.anthropic.com`; 가상의 `plugins.claude.com` 제거
- 여러 파일에서 가상의 구성 필드 제거
- 모든 "최종 업데이트" 날짜를 2026년 2월로 업데이트

**전체 변경 로그**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
