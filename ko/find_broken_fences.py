import re
from pathlib import Path

# 검사할 파일 경로
target_file = Path("./07-plugins/README.md")

if not target_file.exists():
    print(f"❌ 파일을 찾을 수 없습니다: {target_file}")
    exit(1)

with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 열려 있는 백틱의 위치를 추적할 리스트
fence_history = []
in_fence = False
open_line = None

print("🔍 코드 블록(```) 매핑 시작...")
for index, line in enumerate(lines, start=1):
    if re.match(r"^\s*```", line):
        if not in_fence:
            in_fence = True
            open_line = index
        else:
            in_fence = False
            fence_history.append((open_line, index))
            open_line = None

# 마지막에 닫히지 않은 블록이 있다면 기록
if in_fence:
    fence_history.append((open_line, "미종료 (문서 끝)"))

# 매핑 결과 출력 (에러 주변 위주로 출력)
print("\n--- 코드 블록 열림/닫힘 리스트 ---")
for open_ln, close_ln in fence_history:
    status = "✅ 정상 연결" if isinstance(close_ln, int) else "❌ 에러 발생"
    print(f"[{status}] 시작: {open_ln}줄 ➡️ 종료: {close_ln}줄")

print("\n💡 [팁] 짝이 맞지 않아 밀리기 시작한 첫 번째 '❌ 에러 발생' 또는 '시작 줄'의 바로 윗부분을 확인해 보세요!")
eof
