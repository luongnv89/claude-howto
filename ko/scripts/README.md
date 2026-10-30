<!-- i18n-source: scripts/README.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 빌드 스크립트

이 디렉터리에는 튜토리얼 Markdown 파일을 배포 가능한 형식으로 변환하는 두 개의 생성기가 포함되어 있습니다.

- [**EPUB 빌더**](#epub-빌더-스크립트) — `build_epub.py`
- [**정적 웹사이트 빌더**](#정적-웹사이트-빌더) — `build_website.py`

두 생성기 모두 `.md` 파일을 단일 원본(Source of Truth)으로 사용합니다. Markdown을 수정한 후에는 해당 스크립트를 다시 실행하여 결과물을 생성하십시오.

---

# EPUB 빌더 스크립트

Claude How-To Markdown 파일로 EPUB 전자책을 생성합니다.

## 기능

- 폴더 구조(01-slash-commands, 02-memory 등)에 따라 챕터 구성
- Node.js로 실행하는 고정 버전 번들인 [Pele](https://github.com/obsidianmd/pele)로 Mermaid 다이어그램을 SVG 이미지로 렌더링. 모든 EPUB 리더에서 표시되도록 CSS 변수를 흰색 배경 위의 일반 색상으로 평탄화
- 동일한 다이어그램을 캐시하여 고유한 다이어그램마다 한 번만 렌더링
- 프로젝트 로고를 사용하여 표지 이미지 생성
- 내부 Markdown 링크를 EPUB 챕터 참조로 변환
- 엄격한 오류 처리 모드 - 다이어그램 하나라도 렌더링에 실패하면 빌드 실패

## 요구 사항

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- Mermaid 다이어그램 렌더링을 위해 `PATH`에 Node.js >= 20 필요. 고정 버전 Pele 번들은 첫 실행 시 다운로드되며(네트워크는 한 번만 필요), sha256 검증 후 `scripts/.vendor-cache/pele/`에 캐시됩니다.

## 빠른 시작

```bash
# Simplest way - uv handles everything
uv run scripts/build_epub.py
```

## 개발 환경 설정

```bash
# Create virtual environment
uv venv

# Activate and install dependencies
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# Run tests
pytest scripts/tests/ -v

# Run the script
python scripts/build_epub.py
```

## 명령줄 옵션

```
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--lang {en,vi,zh,ja,ko}]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --lang {en,vi,zh,ja,ko}  Language to build (default: en)
```

## 예제

```bash
# Build with verbose output
uv run scripts/build_epub.py --verbose

# Custom output location
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# Build a translated edition
uv run scripts/build_epub.py --lang vi
```

## 출력 결과

저장소 루트 디렉터리에 `claude-howto-guide.epub` 파일을 생성합니다.

EPUB에는 다음이 포함됩니다.

- 프로젝트 로고가 포함된 표지 이미지
- 중첩된 섹션이 포함된 목차
- EPUB 호환 HTML로 변환된 모든 Markdown 콘텐츠
- SVG 이미지로 렌더링된 Mermaid 다이어그램

## 테스트 실행

```bash
# With virtual environment
source .venv/bin/activate
pytest scripts/tests/ -v

# Or with uv directly
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with pillow \
    pytest scripts/tests/ -v
```

## 의존성

PEP 723 인라인 스크립트 메타데이터를 통해 관리됩니다.

| 패키지 | 용도 |
|---------|---------|
| `ebooklib` | EPUB 생성 |
| `markdown` | Markdown을 HTML로 변환 |
| `beautifulsoup4` | HTML 파싱 |
| `pillow` | 표지 이미지 생성 |

## 문제 해결

**`Pele is unavailable` 오류로 빌드 실패**: Node.js >= 20을 설치하고 `node`가 `PATH`에 있는지 확인하십시오(`node --version`).

**Pele 번들 다운로드 또는 체크섬 실패**: 첫 빌드에서는 고정 버전 Pele 번들을 cdn.jsdelivr.net에서 다운로드하고 모든 파일의 sha256을 확인합니다. 오프라인이거나 프록시 뒤에 있다면 네트워크에 접근 가능한 환경에서 한 번 빌드하십시오. 이후 빌드는 `scripts/.vendor-cache/pele/<version>/`의 캐시를 사용합니다. 체크섬이 일치하지 않으면 다운로드가 변조되었거나 잘린 것이므로, 해당 폴더를 삭제하고 다시 빌드하십시오.

**로고 파일 없음**: `claude-howto-logo.png`를 찾을 수 없으면 텍스트만 포함된 표지를 생성합니다.

---

# 정적 웹사이트 빌더

EPUB 생성에 사용하는 동일한 Markdown 파일로 세련되고 모바일 친화적인 정적 웹사이트를 생성합니다. 웹사이트는 렌더링된 결과물이며, `.md` 파일은 계속해서 단일 원본(Source of Truth)으로 유지됩니다.

## 기능

- Markdown 파일마다 하나의 HTML 페이지 생성 — 내부 `.md` 링크는 해당 웹페이지 링크로 자동 변환
- Markdown이 아닌 저장소 파일(템플릿, 스크립트, JSON) 참조는 github.com에서 소스 파일을 여는 GitHub blob URL로 변환
- Mermaid 다이어그램은 빌드된 사이트에서 제공되는 Pele(`pele.global.js`)로 클라이언트 측에서 렌더링(런타임에 CDN 불필요). 다크 모드 전환을 따름
- 독립 실행형 Tailwind CSS CLI(Go 바이너리, Node.js 불필요)로 CSS를 컴파일하여 사이트에 포함 — 반응형 레이아웃, 사이드바 탐색, 페이지 내 목차, 다크 모드 전환, 이전/다음 페이지 탐색 제공
- Inter 및 JetBrains Mono 글꼴을 CSS와 함께 자체 호스팅 — 페이지 로드 시 외부 요청 없음
- EPUB의 커리큘럼 순서(`01-` … `10-` 및 최상위 문서 포함) 유지
- 일반 정적 파일로 호스팅 가능 — GitHub Pages 배포에 최적화

## 빠른 시작

```bash
# Build the English website into ./site/
uv run scripts/build_website.py

# Preview locally
python -m http.server --directory site 8080
# then open http://localhost:8080
```

## 명령줄 옵션

```
usage: build_website.py [-h] [--root ROOT] [--output OUTPUT]
                        [--lang {en,vi,zh,ja,uk,ko}] [--repo-url REPO_URL]
                        [--branch BRANCH] [--verbose]

options:
  --root, -r ROOT       Source root (default: repo root)
  --output, -o OUTPUT   Output directory (default: <repo>/site)
  --lang LANG           Language to build: en | vi | zh | ja | uk | ko
  --repo-url URL        GitHub repo for blob links (default: luongnv89/claude-howto)
  --branch BRANCH       Branch for blob links (default: main)
  --verbose, -v         Enable verbose logging
```

## GitHub Pages 배포

이 저장소에는 `.github/workflows/pages.yml` 워크플로가 포함되어 있으며, `main` 브랜치에 푸시될 때마다(`.md` 또는 생성기 파일이 변경된 경우) 사이트를 빌드한 후 `actions/deploy-pages`를 통해 게시합니다.

이를 활성화하려면 저장소 설정에서 GitHub Pages의 **Source: GitHub Actions**를 선택하십시오.

## 아키텍처

`build_website.py`는 `build_epub.py`의 챕터 정렬 로직을 재사용하며, `scripts/website_templates/` 아래의 HTML 템플릿을 사용합니다.

- `page.html.j2` — 사이드바 탐색, 목차, 이전/다음 페이지 기능을 포함하는 페이지별 Jinja2 템플릿
- `tailwind.config.js`, `tailwind.input.css` — Tailwind 독립 실행형 CLI를 위한 설정 및 입력 CSS. CLI는 생성된 HTML을 분석하여 실제 사용되는 유틸리티만 포함한 `site/assets/tailwind.css`를 생성합니다.
- `site.css` — 사이트 전용 스타일과 Pygments 테마를 포함하는 작은 스타일 레이어

Tailwind CLI 바이너리, Pele 번들 및 글꼴 파일은 첫 번째 빌드 시 `scripts/.vendor-cache/`(gitignore 적용)로 다운로드됩니다. 자세한 내용은 `scripts/vendor_assets.py`를 참고하십시오.

제목(anchor) 링크는 `check_cross_references.heading_to_anchor`와 동일한 알고리즘으로 생성되므로, pre-commit 훅에서 검증한 `#anchor` 링크가 렌더링된 사이트에서도 올바르게 동작합니다.
