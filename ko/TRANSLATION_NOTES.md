# 번역 용어집 및 스타일 가이드

# Translation Glossary & Style Guide (Korean)

> **중요:** 이 문서는 Claude How To 문서를 한국어로 번역·동기화할 때 지켜야 할 규칙을 정의합니다. 작업 전에 반드시 읽어 주세요.

## 기본 원칙

- **문체:** 합니다체(격식체)로 통일합니다. 예: "~합니다", "~입니다", "~할 수 있습니다". 사용자에게 동작을 안내하는 명령형 문장은 "~하세요"도 허용합니다.
- **원문 구조 유지:** 헤딩, 코드 블록, 표, Mermaid 다이어그램의 개수와 순서는 영어 원문과 같아야 합니다.
- **코드 보존:** 실행 가능한 코드, 명령어, 설정 키, 파일 경로, 플래그는 100% 원문 그대로 둡니다. 코드 내 주석만 번역합니다.
- **Mermaid:** 다이어그램 안의 텍스트는 번역하지 않습니다(렌더링·검증 일관성 유지).
- **원문 추적:** 각 파일에 `i18n-source-sha` 주석을 넣어 어느 영어 커밋을 기준으로 번역했는지 기록합니다.

---

## 용어집

| English | 한국어 | 비고 |
|---------|--------|------|
| slash command | 슬래시 명령어 | 명령어 이름(`/optimize`)은 번역하지 않음 |
| command | 명령어 | |
| skill | 스킬 | Claude Code 기능명 |
| hook | 훅 | "후크" 사용하지 않음 |
| subagent | 서브에이전트 | |
| agent | 에이전트 | |
| agent team | 에이전트 팀 | |
| memory | 메모리 | |
| checkpoint | 체크포인트 | |
| rewind | 되감기 | 명령어 `/rewind`는 원문 유지 |
| plugin | 플러그인 | |
| marketplace | 마켓플레이스 | |
| MCP (Model Context Protocol) | MCP | 프로토콜명은 원문 유지 |
| MCP server | MCP 서버 | |
| permission mode | 권한 모드 | 모드 값(`manual`, `acceptEdits` 등)은 원문 유지 |
| planning mode / plan mode | 계획 모드 | |
| extended thinking | 확장 사고 | |
| headless mode | 헤드리스 모드 | |
| background task | 백그라운드 작업 | |
| session | 세션 | |
| context / context window | 컨텍스트 / 컨텍스트 창 | |
| prompt | 프롬프트 | |
| workflow | 워크플로 | "워크플로우" 사용하지 않음 |
| directory | 디렉터리 | "디렉토리" 사용하지 않음 |
| repository | 저장소 | |
| pull request / PR | 풀 리퀘스트 / PR | |
| commit / branch / merge | 커밋 / 브랜치 / 병합 | 명령어(`git merge`)는 원문 유지 |
| issue | 이슈 | |
| code review | 코드 리뷰 | |
| refactoring | 리팩터링 | "리팩토링" 사용하지 않음 |
| shell | 셸 | "쉘" 사용하지 않음 |
| mod (Claude Code) | 모드(mod) | 첫 등장 시 병기, mode와 구분 |
| settings | 설정 | 파일명 `settings.json`은 원문 유지 |
| frontmatter | 프런트매터 | |
| template | 템플릿 | |
| deprecated | 지원 중단(deprecated) | 첫 등장 시 병기 |

## 번역하지 않는 고유명사

Claude, Claude Code, Claude Desktop, Anthropic, CLAUDE.md, SKILL.md, Opus, Sonnet, Haiku, Fable, Mythos, MCP, LSP, CLI, SDK, API, GitHub, VS Code, JetBrains, 모든 명령어·플래그·환경 변수·설정 키·이벤트 이름(`PreToolUse` 등)

## 세부 규칙

1. **코드와 명령어:** 코드 블록 안의 실행 코드는 바꾸지 않습니다. 주석(`#`, `//`)은 번역합니다.
2. **예시 파일(SKILL.md, 에이전트, 명령어 템플릿):** 독립 파일(예: `ko/03-skills/refactor/SKILL.md`)은 프런트매터 키와 `name` 값만 원문 유지하고 `description` 같은 자연어 값과 본문은 번역합니다. README 안의 코드 블록에 들어 있는 예시는 코드로 보아 원문을 유지하고 주석만 번역합니다.
3. **CLI 출력 예시, 커밋 메시지 예시, UI 라벨:** 원문 유지합니다(필요하면 뒤에 한국어 설명을 붙입니다).
4. **링크:** 같은 언어 문서로의 상대 링크는 `ko/` 안의 대응 파일을 가리키게 하고, 앵커는 한국어 헤딩 기준으로 다시 생성합니다. 외부 URL은 그대로 둡니다.
5. **표:** 열 수와 행 수를 원문과 맞춥니다. 셀 안의 `|`는 `\|`로 이스케이프합니다.
6. **기술 약어:** 첫 등장 시 "한국어(영어)" 병기가 필요하면 한 번만 씁니다.
7. **숫자·단위:** 반각 숫자를 쓰고, 버전 번호는 원문과 동일하게 둡니다.

## 푸터 표기

문서 끝의 메타데이터 라벨은 `**최종 업데이트**`, `**Claude Code 버전**`, `**출처**`, `**호환 모델**`로 쓰고, 날짜는 `2026년 10월 26일` 형식으로 씁니다. 값(버전, 출처 URL, 모델명)은 영어 원문과 같게 둡니다.

## 버전 추적 주석

각 파일 맨 위(프런트매터가 있는 파일은 프런트매터 바로 아래)에 다음 주석을 둡니다.

```markdown
<!-- i18n-source: 02-memory/README.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->
```

프런트매터가 있는 예시 파일은 `---`가 첫 줄이어야 Claude Code가 그대로 인식하므로, 주석을 프런트매터 아래에 둡니다.

## 동기화 방법

```bash
# 마지막 번역 기준 커밋 이후 영어 원문 변경분 확인
git diff <i18n-source-sha> main -- 02-memory/README.md
```

변경분을 대응하는 `ko/` 파일에 반영한 뒤 `i18n-source-sha`와 `i18n-date`를 갱신합니다.

## 커밋 전 체크리스트

- [ ] 헤딩·코드 블록·Mermaid 개수가 영어 원문과 같음
- [ ] 코드·명령어·설정 키가 원문과 동일
- [ ] 용어집 표기 준수
- [ ] `pre-commit run --all-files` 통과
