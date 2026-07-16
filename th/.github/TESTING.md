<!-- i18n-source: .github/TESTING.md -->
<!-- i18n-date: 2026-05-09 -->
# คู่มือการทดสอบ

เอกสารนี้อธิบายโครงสร้างพื้นฐานการทดสอบของ Claude How To

## ภาพรวม

โครงการใช้ GitHub Actions เพื่อรันการทดสอบโดยอัตโนมัติในทุก push และ pull request การทดสอบครอบคลุม:

- **Unit Tests**: การทดสอบ Python โดยใช้ pytest
- **Code Quality**: การตรวจสอบและจัดรูปแบบโค้ดด้วย Ruff
- **Security**: การสแกนช่องโหว่ด้วย Bandit
- **Type Checking**: การวิเคราะห์ประเภทสถิตด้วย mypy
- **Build Verification**: การทดสอบการสร้าง EPUB

## การรันการทดสอบในเครื่อง

### ข้อกำหนดเบื้องต้น

```bash
# ติดตั้ง uv (ตัวจัดการแพ็กเกจ Python ที่รวดเร็ว)
pip install uv

# หรือบน macOS ด้วย Homebrew
brew install uv
```

### ตั้งค่าสภาพแวดล้อม

```bash
# clone repository
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# สร้าง virtual environment
uv venv

# เปิดใช้งาน
source .venv/bin/activate  # macOS/Linux
# หรือ
.venv\\Scripts\\activate     # Windows

# ติดตั้ง development dependencies
uv pip install -r requirements-dev.txt
```

### รันการทดสอบ

```bash
# รัน unit tests ทั้งหมด
pytest scripts/tests/ -v

# รันการทดสอบพร้อม coverage
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# รันไฟล์ทดสอบเฉพาะ
pytest scripts/tests/test_build_epub.py -v

# รันฟังก์ชันทดสอบเฉพาะ
pytest scripts/tests/test_build_epub.py::test_function_name -v

# รันการทดสอบในโหมด watch (ต้องการ pytest-watch)
ptw scripts/tests/
```

### รัน Linting

```bash
# ตรวจสอบการจัดรูปแบบโค้ด
ruff format --check scripts/

# แก้ไขการจัดรูปแบบโดยอัตโนมัติ
ruff format scripts/

# รัน linter
ruff check scripts/

# แก้ไขปัญหา linter โดยอัตโนมัติ
ruff check --fix scripts/
```

### รัน Security Scan

```bash
# รัน Bandit security scan
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# สร้างรายงาน JSON
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/ -f json -o bandit-report.json
```

### รัน Type Checking

```bash
# ตรวจสอบประเภทด้วย mypy
mypy scripts/ --ignore-missing-imports --no-implicit-optional
```

## GitHub Actions Workflow

### เงื่อนไขการเรียกใช้

- **Push** ไปยัง branch `main` หรือ `develop` (เมื่อ scripts มีการเปลี่ยนแปลง)
- **Pull Request** ไปยัง `main` (เมื่อ scripts มีการเปลี่ยนแปลง)
- การเรียกใช้ workflow ด้วยตนเอง

### Jobs

#### 1. Unit Tests (pytest)

- **รันบน**: Ubuntu latest
- **เวอร์ชัน Python**: 3.10, 3.11, 3.12
- **สิ่งที่ทำ**:
  - ติดตั้ง dependencies จาก `requirements-dev.txt`
  - รัน pytest พร้อมรายงาน coverage
  - อัปโหลด coverage ไปยัง Codecov
  - เก็บถาวรผลการทดสอบและ coverage HTML

**ผลลัพธ์**: หากการทดสอบใดล้มเหลว workflow จะล้มเหลว (สำคัญ)

#### 2. Code Quality (Ruff)

- **รันบน**: Ubuntu latest
- **เวอร์ชัน Python**: 3.11
- **สิ่งที่ทำ**:
  - ตรวจสอบการจัดรูปแบบโค้ดด้วย `ruff format`
  - รัน linter ด้วย `ruff check`
  - รายงานปัญหาแต่ไม่ทำให้ workflow ล้มเหลว

**ผลลัพธ์**: ไม่บล็อก (เฉพาะคำเตือน)

#### 3. Security Scan (Bandit)

- **รันบน**: Ubuntu latest
- **เวอร์ชัน Python**: 3.11
- **สิ่งที่ทำ**:
  - สแกนช่องโหว่ความปลอดภัย
  - สร้างรายงาน JSON
  - อัปโหลดรายงานเป็น artifact

**ผลลัพธ์**: ไม่บล็อก (เฉพาะคำเตือน)

#### 4. Type Checking (mypy)

- **รันบน**: Ubuntu latest
- **เวอร์ชัน Python**: 3.11
- **สิ่งที่ทำ**:
  - วิเคราะห์ประเภทสถิต
  - รายงานความไม่สอดคล้องของประเภท
  - ช่วยตรวจจับข้อบกพร่องตั้งแต่เนิ่น ๆ

**ผลลัพธ์**: ไม่บล็อก (เฉพาะคำเตือน)

#### 5. Build EPUB

- **รันบน**: Ubuntu latest
- **ขึ้นอยู่กับ**: pytest, lint, security (ทุกอย่างต้องผ่าน)
- **สิ่งที่ทำ**:
  - สร้างไฟล์ EPUB โดยใช้ `scripts/build_epub.py`
  - ตรวจสอบว่า EPUB ถูกสร้างเรียบร้อย
  - อัปโหลด EPUB เป็น artifact

**ผลลัพธ์**: หาก build ล้มเหลว workflow จะล้มเหลว (สำคัญ)

#### 6. Summary

- **รันบน**: Ubuntu latest
- **ขึ้นอยู่กับ**: Jobs อื่นทั้งหมด
- **สิ่งที่ทำ**:
  - สร้างสรุป workflow
  - แสดงรายการ artifacts ทั้งหมด
  - รายงานสถานะโดยรวม

## การเขียนการทดสอบ

### โครงสร้างการทดสอบ

ควรวางการทดสอบใน `scripts/tests/` โดยมีชื่อแบบ `test_*.py`:

```python
# scripts/tests/test_example.py
import pytest
from scripts.example_module import some_function

def test_basic_functionality():
    """ทดสอบว่า some_function ทำงานถูกต้อง"""
    result = some_function("input")
    assert result == "expected_output"

def test_error_handling():
    """ทดสอบว่า some_function จัดการข้อผิดพลาดอย่างเหมาะสม"""
    with pytest.raises(ValueError):
        some_function("invalid_input")

@pytest.mark.asyncio
async def test_async_function():
    """ทดสอบฟังก์ชัน async"""
    result = await async_function()
    assert result is not None
```

### แนวปฏิบัติที่ดีในการทดสอบ

- **ใช้ชื่อที่อธิบายได้**: `test_function_returns_correct_value()`
- **หนึ่ง assertion ต่อการทดสอบ** (เมื่อเป็นไปได้): ง่ายต่อการระบุจุดที่ล้มเหลว
- **ใช้ fixtures** สำหรับการตั้งค่าที่ใช้ซ้ำ: ดู `scripts/tests/conftest.py`
- **Mock บริการภายนอก**: ใช้ `unittest.mock` หรือ `pytest-mock`
- **ทดสอบ edge cases**: อินพุตว่าง ค่า None ข้อผิดพลาด
- **รักษาการทดสอบให้เร็ว**: หลีกเลี่ยง sleep() และ I/O ภายนอก
- **ใช้ pytest markers**: `@pytest.mark.slow` สำหรับการทดสอบที่ช้า

### Fixtures

fixtures ที่ใช้ทั่วไปกำหนดไว้ใน `scripts/tests/conftest.py`:

```python
# ใช้ fixtures ในการทดสอบ
def test_something(tmp_path):
    """tmp_path fixture จัดเตรียม temporary directory"""
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    assert test_file.read_text() == "content"
```

## รายงาน Coverage

### Coverage ในเครื่อง

```bash
# สร้างรายงาน coverage
pytest scripts/tests/ --cov=scripts --cov-report=html

# เปิดรายงาน coverage ในเบราว์เซอร์
open htmlcov/index.html
```

### เป้าหมาย Coverage

- **Coverage ขั้นต่ำ**: 80%
- **Branch coverage**: เปิดใช้งาน
- **บริเวณที่ให้ความสำคัญ**: ฟังก์ชันหลักและ error paths

## Pre-commit Hooks

โครงการใช้ pre-commit hooks เพื่อรันการตรวจสอบโดยอัตโนมัติก่อน commit:

```bash
# ติดตั้ง pre-commit hooks
pre-commit install

# รัน hooks ด้วยตนเอง
pre-commit run --all-files

# ข้าม hooks สำหรับ commit (ไม่แนะนำ)
git commit --no-verify
```

hooks ที่กำหนดค่าใน `.pre-commit-config.yaml`:
- Ruff formatter
- Ruff linter
- Bandit security scanner
- YAML validation
- การตรวจสอบขนาดไฟล์
- การตรวจจับ merge conflict

## การแก้ไขปัญหา

### การทดสอบผ่านในเครื่องแต่ล้มเหลวใน CI

สาเหตุทั่วไป:
1. **ความแตกต่างของเวอร์ชัน Python**: CI ใช้ 3.10, 3.11, 3.12
2. **Dependencies ที่ขาดหายไป**: อัปเดต `requirements-dev.txt`
3. **ความแตกต่างของแพลตฟอร์ม**: ตัวคั่น path, environment variables
4. **Flaky tests**: การทดสอบที่ขึ้นอยู่กับเวลาหรือลำดับ

วิธีแก้ไข:
```bash
# ทดสอบด้วยเวอร์ชัน Python เดียวกัน
uv python install 3.10 3.11 3.12

# ทดสอบด้วยสภาพแวดล้อมที่สะอาด
rm -rf .venv
uv venv
uv pip install -r requirements-dev.txt
pytest scripts/tests/
```

### Bandit รายงาน False Positives

คำเตือนความปลอดภัยบางอย่างอาจเป็น false positives กำหนดค่าใน `pyproject.toml`:

```toml
[tool.bandit]
exclude_dirs = ["scripts/tests"]
skips = ["B101"]  # ข้ามคำเตือน assert_used
```

### Type Checking เข้มงวดเกินไป

ผ่อนปรน type checking สำหรับไฟล์เฉพาะ:

```python
# เพิ่มที่ต้นไฟล์
# type: ignore

# หรือสำหรับบรรทัดเฉพาะ
some_dynamic_code()  # type: ignore
```

## แนวปฏิบัติที่ดีสำหรับ Continuous Integration

1. **รักษาการทดสอบให้เร็ว**: แต่ละการทดสอบควรเสร็จสิ้นใน <1 วินาที
2. **ห้ามทดสอบ API ภายนอก**: Mock บริการภายนอก
3. **ทดสอบแบบแยกส่วน**: แต่ละการทดสอบควรเป็นอิสระ
4. **ใช้ assertion ที่ชัดเจน**: `assert x == 5` ไม่ใช่ `assert x`
5. **จัดการ async tests**: ใช้ `@pytest.mark.asyncio`
6. **สร้างรายงาน**: Coverage, security, type checking

## แหล่งข้อมูล

- [pytest Documentation](https://docs.pytest.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## การมีส่วนร่วมในการทดสอบ

เมื่อส่ง pull request:

1. **เขียนการทดสอบ** สำหรับฟังก์ชันใหม่
2. **รันการทดสอบในเครื่อง**: `pytest scripts/tests/ -v`
3. **ตรวจสอบ coverage**: `pytest scripts/tests/ --cov=scripts`
4. **รัน linting**: `ruff check scripts/`
5. **Security scan**: `bandit -r scripts/ --exclude scripts/tests/`
6. **อัปเดตเอกสาร** หากการทดสอบมีการเปลี่ยนแปลง

การทดสอบเป็นข้อกำหนดสำหรับ pull request ทั้งหมด! 🧪

---

หากมีคำถามหรือปัญหาเกี่ยวกับการทดสอบ โปรดเปิด GitHub issue หรือ discussion
