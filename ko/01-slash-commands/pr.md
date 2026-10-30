---
description: 코드 정리, 변경사항 스테이징, 풀 리퀘스트 준비
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# 풀 리퀘스트 준비 체크리스트

PR을 생성하기 전에 다음 단계를 수행하십시오:

1. 린팅 실행: `prettier --write .`
2. 테스트 실행: `npm test`
3. git diff 검토: `git diff HEAD`
4. 변경사항 스테이징: `git add .`
5. 컨벤셔널 커밋(conventional commits) 규칙에 따라 커밋 메시지 작성:
   - `fix:` 버그 수정
   - `feat:` 새로운 기능 추가
   - `docs:` 문서 업데이트
   - `refactor:` 코드 리팩터링
   - `test:` 테스트 추가
   - `chore:` 유지보수 작업

6. 다음 내용을 포함하여 PR 요약 생성:
   - 변경 내용
   - 변경 이유
   - 수행된 테스트
   - 잠재적 영향

---
**최종 업데이트**: 2026년 8월 4일
**Claude Code 버전**: 2.1.220
**출처**:
- https://code.claude.com/docs/en/commands
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
