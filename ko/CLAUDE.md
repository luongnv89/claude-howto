<!-- i18n-source: CLAUDE.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

# CLAUDE.md

튜토리얼 저장소입니다. 결과물은 앱이 아니라 `01-`부터 `10-`까지 번호가 매겨진 모듈의 Markdown입니다. `scripts/`의 스크립트는 문서 검증과 EPUB 빌드를 위해서만 존재합니다.

스택과 설정(uv, Node.js >= 20, pre-commit)은 [CONTRIBUTING.md](CONTRIBUTING.md#3-개발-환경-설정)를, 강의 구조는 [STYLE_GUIDE.md](STYLE_GUIDE.md)를 참고하세요.

## 사용자가 학습 중인 경우

많은 사람이 기여가 아니라 학습을 위해 이 저장소를 클론합니다. 사용자가 저장소 변경을 요청하지 않는 한, 아래 규칙은 사용자의 선호가 아니라 관리자(maintainer) 규약으로 취급하세요. 강의를 수정하거나, 저장소 수정 사항을 제안하거나, 사용자를 위해 훅을 설정하지 마세요. 사용자 자신의 컨텍스트는 저장소 루트에 직접 만드는 `CLAUDE.local.md`(gitignore 대상이며 이 파일과 함께 로드됨)에 두도록 안내하세요. 사용자가 변경, 커밋, PR을 요청하면 아래의 모든 규칙이 그대로 적용됩니다.

## 핵심 명령어

```bash
# 품질 게이트 (pre-commit 훅을 통해 커밋 시에도 실행됨)
pre-commit run --all-files

# 테스트
pytest scripts/tests/ -v

# EPUB 빌드 (Pele로 Mermaid 렌더링 — Node.js >= 20 필요. 고정된 번들을 한 번 내려받은 뒤에는 오프라인으로 동작)
uv run scripts/build_epub.py

# Python 도구
ruff check scripts/ && ruff format scripts/
mypy scripts/ --ignore-missing-imports
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/
```

Pre-commit은 `.md` 변경 시 5가지 문서 검사(markdown-lint, cross-references, mermaid-syntax, link-check, markdown-rendering)를 실행합니다. 모두 통과해야 합니다. EPUB 빌드는 pre-commit 훅이 **아닙니다**. 전체 책을 빌드하는 느린 작업이므로 CI에서만 실행되며(`.github/workflows/test.yml`의 `build-epub` 잡), mermaid-syntax 훅이 이미 같은 Pele 번들로 모든 다이어그램을 렌더링합니다.

## 아키텍처 맵

- `01-` … `10-` — 튜토리얼 모듈입니다. **번호 접두사 = 학습 순서**이며 알파벳순이 아닙니다. 재구성하지 마세요.
- 각 모듈: `README.md` + 복사해 붙여넣을 수 있는 템플릿(`.md`, `.json`, `.sh`).
- `scripts/` — 유틸리티(EPUB 빌더, 링크/Mermaid/상호 참조 검증기)입니다. 제품이 아닙니다.
- `02-memory/*.md` — 사용자가 자신의 프로젝트에 복사하는 CLAUDE.md 템플릿입니다. 이 파일과 혼동하지 마세요.

## 엄격한 규칙

- **사용자의 명시적 요청 없이 커밋하거나 푸시해서는 안 됩니다.**
- 어떤 커밋 메시지에도 **`Co-Authored-By: Claude`를 추가해서는 안 됩니다.**
- Python 스크립트를 실행하기 전에 항상 `.venv`를 활성화하세요(`venv/`, `.venv/`, `env/` 확인).
- 내부 링크는 **상대 경로**를 사용합니다(예: `01-slash-commands/README.md`). 앵커는 `#heading-name`을 사용합니다.
- 코드 펜스에는 언어(`bash`, `python`, `json`, …)를 **반드시** 선언해야 합니다. 그렇지 않으면 cross-reference 검사가 실패합니다.
- 외부 URL은 접근 가능하고 안정적이어야 합니다. 일시적인 링크는 사용하지 마세요.
- Mermaid 다이어그램은 Pele로 렌더링되어야 합니다. pre-commit Mermaid 훅은 pre-commit에서 Node.js 22를 받아 strict 모드로 실행되므로 건너뛰지 않고 실패합니다. 첫 실행에는 Node.js와 고정된 Pele 번들을 내려받기 위한 네트워크가 필요합니다(오프라인: `SKIP=mermaid,vietnamese-mermaid,japanese-mermaid,korean-mermaid`). `scripts/check_mermaid.py`를 직접 실행하면 Node.js >= 20이 없을 때 경고만 하고, `--strict`나 CI에서는 실패합니다. EPUB 빌드가 깨지는 원인은 대개 잘못된 Mermaid, Node.js >= 20 누락, 또는 번들 다운로드 실패입니다.
- 커밋 형식: `type(scope): subject`이며 `scope`는 모듈 폴더와 일치합니다(예: `feat(slash-commands):`, `docs(memory):`, `fix(README):`).
- `01-`–`10-` 번호 체계를 재구성하지 마세요. 순서가 곧 커리큘럼입니다.

## 워크플로 선호 사항

- 강의를 수정할 때는 구조/명명/다이어그램에 관해 `STYLE_GUIDE.md`를 따르세요.
- 작은 수정 → 최소한의 diff. 오타 하나를 고치려고 섹션 전체를 다시 쓰지 마세요.
- 모듈 페이지를 추가할 때: README + 템플릿을 먼저 작성한 다음, 순서나 소요 시간이 바뀌면 루트 `README.md` 인덱스와 `LEARNING-ROADMAP.md`를 업데이트하세요.
- 튜토리얼 > 라이브러리: 재사용 가능한 추상화보다 명확한 설명과 복사해 붙여넣을 수 있는 예제를 우선합니다.
- 품질 검사가 실패하면 근본 원인을 수정하세요. `--no-verify`로 우회하지 마세요.

## 토큰 효율성
- 방금 작성하거나 수정한 파일을 다시 읽지 마세요. 내용은 이미 알고 있습니다.
- 결과가 불확실한 경우가 아니라면 "확인"을 위해 명령어를 다시 실행하지 마세요.
- 요청받지 않는 한 큰 코드 블록이나 파일 내용을 그대로 되풀이하지 마세요.
- 관련된 편집은 한 번의 작업으로 묶으세요. 1번이면 될 편집을 5번에 나눠 하지 마세요.
- "계속하겠습니다..." 같은 확인 문구는 생략하고 바로 실행하세요.
- 도구 호출 1번이면 되는 작업에 3번을 쓰지 마세요. 행동하기 전에 계획하세요.
- 결과가 모호하거나 추가 입력이 필요한 경우가 아니라면 방금 한 일을 요약하지 마세요.
