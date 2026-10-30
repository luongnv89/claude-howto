---
name: setup-ci-cd
description: 품질 보증을 위한 pre-commit 훅 및 GitHub Actions 구현
---
<!-- i18n-source: 01-slash-commands/setup-ci-cd.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

# CI/CD 파이프라인 설정

프로젝트 유형에 맞춰 포괄적인 DevOps 품질 게이트를 구현합니다:

1.  **프로젝트 분석**: 언어, 프레임워크, 빌드 시스템 및 기존 툴링 감지
2.  언어별 도구를 사용하여 **pre-commit hooks 구성**:
    -   포매팅: Prettier/Black/gofmt/rustfmt/etc.
    -   린팅: ESLint/Ruff/golangci-lint/Clippy/etc.
    -   보안: Bandit/gosec/cargo-audit/npm audit/etc.
    -   타입 검사: TypeScript/mypy/flow (해당하는 경우)
    -   테스트: 관련 테스트 스위트 실행
3.  **GitHub Actions 워크플로 생성** (.github/workflows/):
    -   push/PR 시 pre-commit 검사 미러링
    -   다중 버전/플랫폼 매트릭스 (해당하는 경우)
    -   빌드 및 테스트 검증
    -   배포 단계 (필요한 경우)
4.  **파이프라인 검증**: 로컬에서 테스트하고, 테스트 PR을 생성하여 모든 검사가 통과하는지 확인

무료/오픈 소스 도구를 사용합니다. 기존 구성을 존중합니다. 빠른 실행 속도를 유지합니다.

---
**최종 업데이트**: 2026년 8월 4일
**Claude Code 버전**: 2.1.220
**출처**:
- https://code.claude.com/docs/en/commands
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
