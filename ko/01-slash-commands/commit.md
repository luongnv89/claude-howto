---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: 컨텍스트를 사용하여 git 커밋 생성
---

## 컨텍스트

- 현재 git 상태: !`git status`
- 현재 git diff: !`git diff HEAD`
- 현재 브랜치: !`git branch --show-current`
- 최근 커밋: !`git log --oneline -10`

## 당신의 작업

위 변경 사항을 바탕으로 단일 git 커밋을 생성하세요.

인수를 통해 메시지가 제공된 경우, 해당 메시지를 사용하세요: $ARGUMENTS

그렇지 않은 경우, 변경 사항을 분석하여 conventional commits 형식에 맞는 적절한 커밋 메시지를 생성하세요:
- `feat:` 새로운 기능용
- `fix:` 버그 수정용
- `docs:` 문서 변경용
- `refactor:` 코드 리팩토링용
- `test:` 테스트 추가용
- `chore:` 유지보수 작업용

---
**최종 업데이트**: April 9, 2026
