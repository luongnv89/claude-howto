# 실사용 산출물 (artifacts)

[실무 적용 가이드](../PRACTICAL-GUIDE.md)에서 참조하는, **복사해서 바로 쓰는**
설정 파일 모음이다. 각 파일 상단 주석에 대상 레포의 목적지 경로가 적혀 있다.

## 구성

```text
artifacts/
├── openpi/
│   ├── CLAUDE.md                       # → openpi 루트 CLAUDE.md
│   └── .claude/
│       ├── settings.json               # 편집 후 ruff 자동 실행 훅
│       └── agents/config-explorer.md   # 거대 config.py 탐색 서브에이전트
└── nexus/
    └── .claude/
        ├── commands/sync-check.md      # /sync-check 슬래시 커맨드
        └── settings.json               # git commit 전 smoke test 게이트
```

## 적용 방법

### openpi

```bash
cp ko/artifacts/openpi/CLAUDE.md /home/user/openpi/CLAUDE.md
mkdir -p /home/user/openpi/.claude/agents
cp ko/artifacts/openpi/.claude/settings.json /home/user/openpi/.claude/settings.json
cp ko/artifacts/openpi/.claude/agents/config-explorer.md /home/user/openpi/.claude/agents/
```

### nexus

```bash
mkdir -p /home/user/nexus/.claude/commands
cp ko/artifacts/nexus/.claude/commands/sync-check.md /home/user/nexus/.claude/commands/
cp ko/artifacts/nexus/.claude/settings.json /home/user/nexus/.claude/settings.json
```

## 주의

- `settings.json`의 훅 명령은 레포 루트에서 실행된다고 가정한다. 모노레포나
  하위 디렉터리 작업 시 `cwd`를 확인한다.
- 훅은 처음에는 비파괴적으로(실패해도 차단하지 않게) 검증한 뒤, 팀이
  합의하면 차단형으로 강화한다.
- 이 파일들은 가이드 보관용으로 `claude-howto`에 있다. 실제 사용 시 각 레포로
  복사하며, 그 레포의 컨벤션에 맞게 조정한다.
