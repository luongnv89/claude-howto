---
description: 모든 변경 사항을 스테이징하고, 커밋을 생성하며, 원격 저장소로 푸시합니다 (주의해서 사용하십시오).
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# 모든 것을 커밋하고 푸시하기

⚠️ **주의**: 모든 변경 사항을 스테이징하고, 커밋하며, 원격 저장소로 푸시합니다. 모든 변경 사항이 함께 속한다고 확신할 때만 사용하십시오.

## 워크플로우

### 1. 변경 사항 분석
다음 명령어를 병렬로 실행합니다:
- `git status` - 수정/추가/삭제/추적되지 않은 파일 표시
- `git diff --stat` - 변경 통계 표시
- `git log -1 --oneline` - 메시지 스타일을 위한 최근 커밋 표시

### 2. 안전성 검사

**❌ 다음 사항이 감지되면 중단하고 경고하십시오:**
- 비밀 정보: `.env*`, `*.key`, `*.pem`, `credentials.json`, `secrets.yaml`, `id_rsa`, `*.p12`, `*.pfx`, `*.cer`
- API 키: 실제 값이 포함된 모든 `*_API_KEY`, `*_SECRET`, `*_TOKEN` 변수 ( `your-api-key`, `xxx`, `placeholder`와 같은 플레이스홀더 제외)
- 대용량 파일: Git LFS 없이 `>10MB`인 파일
- 빌드 아티팩트: `node_modules/`, `dist/`, `build/`, `__pycache__/`, `*.pyc`, `.venv/`
- 임시 파일: `.DS_Store`, `thumbs.db`, `*.swp`, `*.tmp`

**API 키 유효성 검사:**
수정된 파일에서 다음과 같은 패턴을 확인하십시오:
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ Real key detected!
AWS_SECRET_KEY=AKIA...         # ❌ Real key detected!
STRIPE_API_KEY=sk_live_...    # ❌ Real key detected!

# ✅ Acceptable placeholders:
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ 다음 사항을 확인하십시오:**
- `.gitignore`가 올바르게 구성되었는지
- 병합 충돌이 없는지
- 올바른 브랜치인지 (main/master인 경우 경고)
- API 키가 플레이스홀더만 포함하는지

### 3. 확인 요청

요약을 제시합니다:
```
📊 Changes Summary:
- X files modified, Y added, Z deleted
- Total: +AAA insertions, -BBB deletions

🔒 Safety: ✅ No secrets | ✅ No large files | ⚠️ [warnings]
🌿 Branch: [name] → origin/[name]

I will: git add . → commit → push

Type 'yes' to proceed or 'no' to cancel.
```

**진행하기 전에 명시적인 "yes"를 기다리십시오.**

### 4. 실행 (확인 후)

다음 명령어를 순차적으로 실행합니다:
```bash
git add .
git status  # Verify staging
```

### 5. 커밋 메시지 생성

변경 사항을 분석하고 컨벤셔널 커밋을 생성합니다:

**형식:**
```
[type]: Brief summary (max 72 characters)

- Key change 1
- Key change 2
- Key change 3
```

**유형:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `build`, `ci`

**예시:**
```
docs: Update concept README files with comprehensive documentation

- Add architecture diagrams and tables
- Include practical examples
- Expand best practices sections
```

### 6. 커밋 및 푸시

```bash
git commit -m "$(cat <<'EOF'
[Generated commit message]
EOF
)"
git push  # If fails: git pull --rebase && git push
git log -1 --oneline --decorate  # Verify
```

### 7. 성공 확인

```
✅ Successfully pushed to remote!

Commit: [hash] [message]
Branch: [branch] → origin/[branch]
Files changed: X (+insertions, -deletions)
```

## 오류 처리

- **git add 실패**: 권한, 잠긴 파일, 저장소 초기화 여부를 확인하십시오.
- **git commit 실패**: pre-commit 훅을 수정하고, git config (user.name/email)를 확인하십시오.
- **git push 실패**:
  - 논-패스트포워드(Non-fast-forward): `git pull --rebase && git push`
  - 원격 브랜치 없음: `git push -u origin [branch]`
  - 보호된 브랜치: 대신 PR 워크플로우를 사용하십시오.

## 사용 시기

✅ **권장:**
- 여러 파일에 걸친 문서 업데이트
- 테스트와 문서가 포함된 기능
- 여러 파일에 걸친 버그 수정
- 프로젝트 전반의 형식 지정/리팩토링
- 구성 변경

❌ **피해야 할 경우:**
- 무엇을 커밋하는지 불확실한 경우
- 비밀 정보/민감한 데이터가 포함된 경우
- 검토 없이 보호된 브랜치에 푸시하는 경우
- 병합 충돌이 있는 경우
- 세분화된 커밋 히스토리를 원하는 경우
- pre-commit 훅이 실패하는 경우

## 대안

사용자가 더 많은 제어를 원할 경우, 다음을 제안합니다:
1. **선택적 스테이징**: 특정 파일을 검토/스테이징
2. **대화형 스테이징**: 패치 선택을 위한 `git add -p`
3. **PR 워크플로우**: 브랜치 생성 → 푸시 → PR (`/pr` 명령 사용)

**⚠️ 기억하십시오**: 푸시하기 전에 항상 변경 사항을 검토하십시오. 확신이 서지 않을 때는 개별 git 명령을 사용하여 더 많은 제어를 확보하십시오.

---
**최종 업데이트**: 2026년 4월 9일
