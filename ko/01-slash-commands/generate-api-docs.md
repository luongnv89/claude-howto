---
description: 소스 코드로부터 포괄적인 API 문서를 생성합니다.
---
<!-- i18n-source: 01-slash-commands/generate-api-docs.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

# API 문서 생성기

다음과 같은 방식으로 API 문서를 생성합니다:

1.  `/src/api/`의 모든 파일을 스캔하여
2.  함수 시그니처와 JSDoc 주석을 추출하고
3.  엔드포인트/모듈별로 정리하며
4.  예시를 포함한 마크다운을 생성하고
5.  요청/응답 스키마를 포함하며
6.  오류 문서를 추가합니다.

출력 형식:
- `/docs/api.md`에 마크다운 파일 생성
- 모든 엔드포인트에 대한 curl 예시 포함
- TypeScript 타입 추가

---
**최종 업데이트**: 2026년 8월 4일
**Claude Code 버전**: 2.1.220
**출처**:
- https://code.claude.com/docs/en/commands
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
