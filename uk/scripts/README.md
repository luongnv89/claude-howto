<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Скрипт збірки EPUB

Збірка EPUB-книги з markdown-файлів Claude How-To.

## Функції

- Організує розділи за структурою каталогів (01-slash-commands, 02-memory тощо)
- Рендерить Mermaid-діаграми як PNG-зображення через Kroki.io API
- Асинхронне паралельне завантаження — рендерить усі діаграми одночасно
- Генерує обкладинку з логотипу проєкту
- Конвертує внутрішні markdown-посилання у посилання на розділи EPUB
- Суворий режим помилок — падає, якщо діаграма не може бути відрендерена

## Вимоги

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- Інтернет-з'єднання для рендерингу Mermaid-діаграм

## Швидкий старт

```bash
# Simplest way - uv handles everything
uv run scripts/build_epub.py
```

## Налаштування розробки

```bash
# Create virtual environment
uv venv

# Activate and install dependencies
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# Run tests
pytest scripts/tests/ -v

# Run the script
python scripts/build_epub.py
```

## Параметри командного рядка

```
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --timeout TIMEOUT     API timeout in seconds (default: 30)
  --max-concurrent N    Max concurrent requests (default: 10)
```

## Приклади

```bash
# Build with verbose output
uv run scripts/build_epub.py --verbose

# Custom output location
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# Limit concurrent requests (if rate-limited)
uv run scripts/build_epub.py --max-concurrent 5
```

## Вивід

Створює `claude-howto-guide.epub` у кореневому каталозі репозиторію.

EPUB включає:
- Обкладинку з логотипом проєкту
- Зміст з вкладеними секціями
- Весь markdown-контент, конвертований у EPUB-сумісний HTML
- Mermaid-діаграми, відрендерені як PNG-зображення

## Запуск тестів

```bash
# With virtual environment
source .venv/bin/activate
pytest scripts/tests/ -v

# Or with uv directly
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with httpx --with pillow --with tenacity \
    pytest scripts/tests/ -v
```

## Залежності

Керуються через PEP 723 inline script metadata:

| Пакет | Призначення |
|-------|-------------|
| `ebooklib` | Генерація EPUB |
| `markdown` | Конвертація Markdown → HTML |
| `beautifulsoup4` | Парсинг HTML |
| `httpx` | Асинхронний HTTP-клієнт |
| `pillow` | Генерація обкладинки |
| `tenacity` | Логіка повторних спроб |

## Усунення проблем

**Збірка падає з мережевою помилкою**: Перевірте інтернет-з'єднання та стан Kroki.io. Спробуйте `--timeout 60`.

**Обмеження частоти**: Зменште паралельні запити з `--max-concurrent 3`.

**Відсутній логотип**: Скрипт генерує текстову обкладинку, якщо `claude-howto-logo.png` не знайдено.
