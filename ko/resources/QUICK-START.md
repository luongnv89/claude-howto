# 빠른 시작 - 브랜드 에셋

## 프로젝트에 에셋 복사하기

```bash
# 모든 리소스를 웹 프로젝트에 복사
cp -r resources/ /path/to/your/website/

# 또는 웹용 파비콘만 복사
cp resources/favicons/* /path/to/your/website/public/
```

## HTML에 추가하기 (복사 후 붙여넣기)

```html
<!-- 파비콘 -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
<meta name="theme-color" content="#000000">
```

## Markdown/문서에서 사용하기

```markdown
# Claude How To

![Claude How To Logo](resources/logos/claude-howto-logo.svg)

![Icon](resources/icons/claude-howto-icon.svg)
```

## 권장 크기

| Purpose | Size | File |
|---------|------|------|
| 웹사이트 헤더 | 520×120 | `logos/claude-howto-logo.svg` |
| 앱 아이콘 | 256×256 | `icons/claude-howto-icon.svg` |
| 브라우저 탭 | 32×32 | `favicons/favicon-32.svg` |
| 모바일 홈 화면 | 128×128 | `favicons/favicon-128.svg` |
| 데스크톱 앱 | 256×256 | `favicons/favicon-256.svg` |
| 작은 아바타 | 64×64 | `favicons/favicon-64.svg` |

## 색상 값

```css
/* CSS에서 다음 값을 사용하세요 */
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

## 아이콘 디자인의 의미

**코드 브래킷이 있는 나침반**:
- 나침반 링 = 내비게이션, 체계적인 학습 경로
- 초록 북쪽 바늘 = 방향, 진전, 안내
- 검정 남쪽 바늘 = 기반, 탄탄한 토대
- `>` 브래킷 = 터미널 프롬프트, 코드, CLI 컨텍스트
- 눈금 표시 = 정밀함, 체계적인 단계

이는 "명확한 안내를 받으며 코드 속에서 길을 찾는 것"을 상징합니다.

## 용도별 사용 에셋

### 웹사이트
- **헤더**: 로고 (`logos/claude-howto-logo.svg`)
- **파비콘**: 32px (`favicons/favicon-32.svg`)
- **소셜 미리보기**: 아이콘 (`icons/claude-howto-icon.svg`)

### GitHub
- **README 배지**: 아이콘 (`icons/claude-howto-icon.svg`), 64-128px
- **저장소 아바타**: 아이콘 (`icons/claude-howto-icon.svg`)

### 소셜 미디어
- **프로필 사진**: 아이콘 (`icons/claude-howto-icon.svg`)
- **배너**: 로고 (`logos/claude-howto-logo.svg`)
- **썸네일**: 256×256px 아이콘

### 문서
- **챕터 헤더**: 로고 또는 아이콘(크기에 맞게 조절)
- **내비게이션 아이콘**: 파비콘 (32-64px)

---

전체 문서는 [README.md](README.md)를 참고하세요.
