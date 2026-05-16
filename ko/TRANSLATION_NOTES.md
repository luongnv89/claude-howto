# 번역 용어집 및 스타일 가이드

# Translation Glossary & Style Guide (Korean)

> **중요:** 이 문서는 Claude Code 문서를 한국어로 번역할 때의 규칙을 정한다.
> `ko/` 디렉터리에 새 번역을 추가하기 전에 반드시 읽는다.

## 기본 방침

- **문체:** ~한다체(평서체, 종결어미 `-다`). 경어체(`-습니다`)는 쓰지 않는다.
- **용어 방침:** IT 업계에 정착된 외래어는 한글 음차를 우선한다
  (슬래시 커맨드, 훅, 스킬, 서브에이전트 등).
- **코드 보존:** 실행 코드·명령·플래그·파일명은 100% 원문 유지.
  주석과 산문만 번역한다. 코드 블록 안의 영어 프롬프트 문자열도 원문 유지.
- **Mermaid 다이어그램:** 라벨 텍스트는 영어 원문 유지(렌더링 안정성).
- **원전 추종:** 각 파일 선두에 `i18n-source` / `i18n-source-sha` / `i18n-date`
  메타데이터를 넣어 재동기화 가능하게 한다.
- **링크 규칙:** `ko/`는 레포 루트보다 한 단계 깊다. 번역되지 않은 루트 문서·
  모듈로의 링크는 `../`로 시작한다(예: `../CATALOG.md`, `../01-slash-commands/`).
  `ko/` 안에서 번역된 문서끼리는 상대 경로(예: `README.md`).
- **앵커:** 제목을 한국어로 번역하면 앵커도 한국어가 된다. 목차의 앵커는
  GitHub 슬러그 규칙(소문자화, 공백→`-`, 구두점 제거)에 맞춰 제목과 정확히
  일치시킨다. cross-reference 검사가 불일치를 잡아낸다.

## i18n 헤더 형식

각 번역 파일 최상단에 다음 3줄을 둔다:

```text
<!-- i18n-source: README.md -->
<!-- i18n-source-sha: <번역 시점 원문의 git short SHA> -->
<!-- i18n-date: YYYY-MM-DD -->
```

## 기술 용어 대응표

전 파일에서 통일하기 위한 대역표:

| English | 한국어 | 비고 |
|---------|--------|------|
| slash command | 슬래시 커맨드 | Claude Code 기능명 |
| hook | 훅 | IT 정착어 |
| skill | 스킬 | Claude Code 기능명 |
| subagent | 서브에이전트 | Claude Code 기능명 |
| agent | 에이전트 | 일반 외래어 |
| agent team | 에이전트 팀 | Claude Code 기능명 |
| memory | 메모리 | Claude Code 기능명(영속 컨텍스트) |
| checkpoint | 체크포인트 | 세션 스냅샷 |
| rewind | 되감기 | UI 동작 |
| plugin | 플러그인 | 일반 외래어 |
| pull request / PR | 풀 리퀘스트 / PR | GitHub 용어 |
| commit | 커밋 | Git 용어 |
| branch | 브랜치 | Git 용어 |
| merge | 머지 | Git 용어 |
| MCP (Model Context Protocol) | MCP | 프로토콜명은 원문 유지 |
| CLAUDE.md | CLAUDE.md | 파일명 원문 유지 |
| prompt | 프롬프트 | 정착 외래어 |
| workflow | 워크플로 | 정착 외래어 |
| repository | 레포(지토리) | Git 용어, 본문은 "레포" 허용 |
| issue | 이슈 | GitHub 용어 |
| release | 릴리스 | 정착 외래어 |
| API / CLI / CI/CD | API / CLI / CI/CD | 원문 유지 |
| pre-commit hook | pre-commit 훅 | 도구명 유지 |
| environment variable | 환경 변수 | 번역어 정착 |
| dependencies | 의존성 | 번역어 정착 |
| template | 템플릿 | 외래어 |
| worktree | 워크트리 | Git 용어 |
| frontmatter | 프론트매터 | YAML 선두 블록 |
| token | 토큰 | 외래어 |
| context window | 컨텍스트 윈도우 | 외래어 |
| fork | 포크 | Git 용어 |
| clone | 클론 | Git 용어 |
| sandbox | 샌드박스 | 외래어 |
| linting | 린팅 | 외래어 |
| refactoring | 리팩터링 | 외래어 |
| build | 빌드 | 외래어 |
| headless mode | 헤드리스 모드 | 외래어 |
| planning mode | 플래닝 모드 | Claude Code 기능명 |
| extended thinking | 확장 사고 | Claude Code 기능명 |
| background task | 백그라운드 태스크 | 외래어 |
| permission mode | 권한 모드 | 번역어 |
| progressive disclosure | 점진적 공개 | 번역어 |

## 검증

번역 추가 후 레포 루트에서:

```bash
python scripts/check_cross_references.py
python scripts/check_mermaid.py
python scripts/check_markdown_rendering.py
```

`.markdownlint.json` 규칙을 준수한다(코드 펜스에는 반드시 언어 지정).
가능하면 `pre-commit run --files ko/...`로 일괄 검증한다.
