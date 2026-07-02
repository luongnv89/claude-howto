import os
from pathlib import Path
from google import genai
import time

# 1. 클라이언트 초기화
client = genai.Client()

# 번역 대상 경로 (우리가 복사해둔 ko 폴더)
# TARGET_DIR = Path("./06-hooks")

# LLM에게 줄 번역 가이드라인 지시서 (시스템 프롬프트)
SYSTEM_PROMPT = """
You are a professional technical translator specializing in software engineering.
Your task is to translate the provided Markdown document from English to Korean.

Strictly adhere to the following rules:
1. Translate only the explanatory text sentences into natural, professional Korean.
2. NEVER translate or modify code blocks (```python, ```sh, ```json, ```mermaid, etc.). Keep them exactly as they are.
3. NEVER translate Git commands, Claude Code slash commands (e.g., /init, /compact), or configuration keys.
4. Maintain all Markdown syntax, headings (#, ##), bold texts (**), and relative links ([text](./path)) exactly as in the original.
5. Return ONLY the translated markdown content without any introduction or out-of-context remarks.
6. Heading and Table of Contents (TOC) Translation Rules:
   - When translating headings (e.g., `# Heading`, `## Subheading`), do NOT keep the original English text alongside the Korean translation. Replace the English title completely with the natural Korean translation.
   - Example: Change `## Configuration` directly to `## 구성`. Do NOT output `## Configuration\n## 구성`.
7. Internal Anchor Link Rules:
   - When translating a Table of Contents or internal links (e.g., `[Overview](#overview)`), translate the visible text into Korean and update the anchor block link to match the newly translated Korean heading.
   - Spaces in Korean headings must be replaced with hyphens (-) in the anchor link, and all special characters should be handled according to standard Markdown slug rules.
   - Example:
     - `1. [Overview](#overview)` -> `1. [개요](#개요)`
     - `2. [Planning Mode](#planning-mode)` -> `2. [기획 모드](#기획-모드)`
     - `3. [File Format](#file-format)` -> `3. [파일 형식](#파일-형식)`
"""

def translate_file(file_path: Path):
    print(f"📄 번역 시작: {file_path}")

    # 파일 읽기 (인코딩 에러 방지를 위해 utf-8 명시)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        return

    # 2. Gemini API 호출
    response = client.models.generate_content(
        model='gemini-2.5-flash', # 빠르고 비용 효율적인 모델 선택
        contents=f"{SYSTEM_PROMPT}\n\n[Document to Translate]\n{content}"
    )

    translated_text = response.text

    # 3. 번역본 덮어쓰기
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(translated_text)

    print(f"✅ 번역 완료: {file_path}\n")

def main():
    # 🎯 특정 파일 경로 지정 (역슬래시 \ 대신 파이썬 Path가 호환되도록 슬래시 / 사용)
    target_file = Path("./CHANGELOG.md")

    if target_file.exists():
        try:
            translate_file(target_file)
        except Exception as e:
            print(f"❌ 에러 발생 ({target_file}): {e}")
    else:
        print(f"❌ 파일을 찾을 수 없습니다: {target_file}")

if __name__ == "__main__":
    main()
