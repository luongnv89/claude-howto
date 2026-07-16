<!-- i18n-source: scripts/README.md -->
<!-- i18n-date: 2026-05-09 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# สคริปต์สร้าง EPUB

สร้าง EPUB ebook จากไฟล์ Markdown ของ Claude How-To

## ฟีเจอร์

- จัดเรียงบทตามโครงสร้าง folder (01-slash-commands, 02-memory ฯลฯ)
- Render Mermaid diagram เป็นภาพ PNG ผ่าน Kroki.io API
- Async concurrent fetching — render diagram ทั้งหมดแบบ parallel
- สร้างภาพ cover จาก logo โปรเจกต์
- แปลง internal Markdown link เป็น reference บท EPUB
- Strict error mode — หยุดทำงานหาก render diagram ใดล้มเหลว

## ความต้องการ

- Python 3.10 ขึ้นไป
- [uv](https://github.com/astral-sh/uv)
- การเชื่อมต่ออินเทอร์เน็ตสำหรับ render Mermaid diagram

## เริ่มต้นอย่างรวดเร็ว

```bash
# วิธีที่ง่ายที่สุด — uv จัดการทุกอย่าง
uv run scripts/build_epub.py
```

## การตั้งค่าสำหรับพัฒนา

```bash
# สร้าง virtual environment
uv venv

# Activate และติดตั้ง dependencies
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# รัน test
pytest scripts/tests/ -v

# รัน script
python scripts/build_epub.py
```

## ตัวเลือก Command-Line

```
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]

options:
  -h, --help            แสดงข้อความช่วยเหลือและออก
  --root, -r ROOT       Root directory (ค่าเริ่มต้น: root ของ repo)
  --output, -o OUTPUT   เส้นทาง output (ค่าเริ่มต้น: claude-howto-guide.epub)
  --verbose, -v         เปิด verbose logging
  --timeout TIMEOUT     API timeout เป็นวินาที (ค่าเริ่มต้น: 30)
  --max-concurrent N    จำนวน request พร้อมกันสูงสุด (ค่าเริ่มต้น: 10)
```

## ตัวอย่าง

```bash
# สร้างพร้อม verbose output
uv run scripts/build_epub.py --verbose

# กำหนด output location เอง
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# จำกัด concurrent request (กรณีถูก rate-limit)
uv run scripts/build_epub.py --max-concurrent 5
```

## ผลลัพธ์

สร้าง `claude-howto-guide.epub` ใน root directory ของ repository

EPUB ประกอบด้วย:
- ภาพ cover พร้อม logo โปรเจกต์
- สารบัญพร้อม nested section
- เนื้อหา Markdown ทั้งหมดแปลงเป็น HTML ที่รองรับ EPUB
- Mermaid diagram ที่ render เป็นภาพ PNG

## การรัน Test

```bash
# กับ virtual environment
source .venv/bin/activate
pytest scripts/tests/ -v

# หรือใช้ uv โดยตรง
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with httpx --with pillow --with tenacity \
    pytest scripts/tests/ -v
```

## Dependencies

จัดการผ่าน PEP 723 inline script metadata:

| Package | วัตถุประสงค์ |
|---------|------------|
| `ebooklib` | สร้าง EPUB |
| `markdown` | แปลง Markdown เป็น HTML |
| `beautifulsoup4` | parse HTML |
| `httpx` | Async HTTP client |
| `pillow` | สร้างภาพ cover |
| `tenacity` | Retry logic |

## การแก้ไขปัญหา

**Build ล้มเหลวด้วย network error**: ตรวจสอบการเชื่อมต่ออินเทอร์เน็ตและสถานะ Kroki.io ลอง `--timeout 60`

**Rate limiting**: ลด concurrent request ด้วย `--max-concurrent 3`

**Logo หาย**: script สร้าง cover แบบ text-only หากไม่พบ `claude-howto-logo.png`
