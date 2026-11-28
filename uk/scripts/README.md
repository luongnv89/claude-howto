<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Скрипти збірки

Цей каталог містить два генератори, що перетворюють markdown-файли посібника
у формати для розповсюдження:

- [**Конструктор EPUB**](#скрипт-збірки-epub) — `build_epub.py`
- [**Статичний конструктор вебсайту**](#статичний-конструктор-вебсайту) — `build_website.py`

Обидва вважають `.md`-файли єдиним джерелом істини — після редагування markdown
перезапустіть відповідний скрипт, щоб згенерувати вихід заново.

---

# Скрипт збірки EPUB

Збірка EPUB-книги з markdown-файлів Claude How-To.

## Функції

- Організує розділи за структурою каталогів (01-slash-commands, 02-memory тощо)
- Рендерить Mermaid-діаграми як SVG-зображення через [Pele](https://github.com/obsidianmd/pele) — закріплений бандл, який запускає Node.js; CSS-змінні замінюються звичайними кольорами на білому тлі, тож діаграми видно в будь-якій EPUB-читалці
- Кешує однакові діаграми — кожна унікальна діаграма рендериться лише раз
- Генерує обкладинку з логотипу проєкту
- Конвертує внутрішні markdown-посилання у посилання на розділи EPUB
- Суворий режим помилок — падає, якщо діаграма не може бути відрендерена

## Вимоги

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- Node.js >= 20 у `PATH` для рендерингу Mermaid-діаграм. Закріплений бандл Pele завантажується під час першого запуску (мережа потрібна лише раз), перевіряється за sha256 і кешується в `scripts/.vendor-cache/pele/`

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
                     [--lang {en,vi,zh,ja}]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --lang {en,vi,zh,ja}  Language to build (default: en)
```

## Приклади

```bash
# Build with verbose output
uv run scripts/build_epub.py --verbose

# Custom output location
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# Build a translated edition
uv run scripts/build_epub.py --lang vi
```

## Вивід

Створює `claude-howto-guide.epub` у кореневому каталозі репозиторію.

EPUB включає:
- Обкладинку з логотипом проєкту
- Зміст з вкладеними секціями
- Весь markdown-контент, конвертований у EPUB-сумісний HTML
- Mermaid-діаграми, відрендерені як SVG-зображення

## Запуск тестів

```bash
# With virtual environment
source .venv/bin/activate
pytest scripts/tests/ -v

# Or with uv directly
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with pillow \
    pytest scripts/tests/ -v
```

## Залежності

Керуються через PEP 723 inline script metadata:

| Пакет | Призначення |
|-------|-------------|
| `ebooklib` | Генерація EPUB |
| `markdown` | Конвертація Markdown → HTML |
| `beautifulsoup4` | Парсинг HTML |
| `pillow` | Генерація обкладинки |

## Усунення проблем

**Збірка падає з `Pele is unavailable`**: Встановіть Node.js >= 20 і переконайтеся, що `node` є у `PATH` (`node --version`).

**Помилка завантаження або контрольної суми бандла Pele**: Перша збірка завантажує закріплений бандл Pele з cdn.jsdelivr.net і перевіряє sha256 кожного файлу. Офлайн або за проксі виконайте одну збірку з доступом до мережі; наступні збірки використовують кеш у `scripts/.vendor-cache/pele/<version>/`. Невідповідність контрольної суми означає, що завантаження змінене або обірване: видаліть цю папку й зберіть знову.

**Відсутній логотип**: Скрипт генерує текстову обкладинку, якщо `claude-howto-logo.png` не знайдено.

---

# Статичний конструктор вебсайту

Згенеруйте елегантний, зручний для мобільних пристроїв статичний вебсайт з тих самих markdown-файлів, які використовує збірка EPUB. Вебсайт — це лише відрендерений вигляд; `.md`-файли залишаються єдиним джерелом істини.

## Функції

- Одна HTML-сторінка на кожен markdown-джерело — внутрішні `.md`-посилання переписуються на відповідні сторінки сайту
- Посилання на не-markdown файли репозиторію (шаблони, скрипти, JSON) стають GitHub blob URL, що відкривають джерело на github.com
- Mermaid-діаграми рендеряться на клієнті через Pele (`pele.global.js`), який подається зі зібраного сайту (без CDN у runtime); вони слідують за перемикачем темної теми
- Tailwind CSS компілюється standalone CLI (Go-бінарник, без Node.js) і подається зі зібраного сайту — адаптивний макет із бічною навігацією, внутрішньосторінковим змістом, перемикачем темної теми та навігацією попередня/наступна сторінка
- Шрифти Inter + JetBrains Mono самолокалізуються поруч із CSS — жодних сторонніх запитів під час завантаження сторінки
- Віддзеркалює порядок навчальної програми EPUB (`01-` … `10-` плюс документи верхнього рівня)
- Хоститься як звичайні статичні файли — розроблено для розгортання на GitHub Pages

## Швидкий старт

```bash
# Збірка англійського вебсайту в ./site/
uv run scripts/build_website.py

# Локальний перегляд
python -m http.server --directory site 8080
# потім відкрийте http://localhost:8080
```

## Параметри командного рядка

```
usage: build_website.py [-h] [--root ROOT] [--output OUTPUT]
                        [--lang {en,vi,zh,ja,uk,ko,fa}] [--repo-url REPO_URL]
                        [--branch BRANCH] [--verbose]

options:
  --root, -r ROOT       Source root (default: repo root)
  --output, -o OUTPUT   Output directory (default: <repo>/site)
  --lang LANG           Language to build: en | vi | zh | ja | uk | ko | fa
  --repo-url URL        GitHub repo for blob links (default: luongnv89/claude-howto)
  --branch BRANCH       Branch for blob links (default: main)
  --verbose, -v         Enable verbose logging
```

## Розгортання на GitHub Pages

У репозиторії є workflow `.github/workflows/pages.yml`, який збирає сайт
при кожному пуші в `main` (коли змінюється будь-який `.md` або файл генератора)
і публікує через `actions/deploy-pages`. Увімкніть GitHub Pages у налаштуваннях
репозиторію, обравши **Source: GitHub Actions**.

## Архітектура

`build_website.py` повторно використовує логіку порядку розділів із `build_epub.py` і
постачає HTML-шаблони в `scripts/website_templates/`:

- `page.html.j2` — Jinja2-шаблон сторінки з бічною навігацією, змістом,
  навігацією попередня/наступна сторінка
- `tailwind.config.js`, `tailwind.input.css` — конфігурація та вхідний CSS для
  Tailwind standalone CLI; CLI сканує зібраний HTML і створює
  `site/assets/tailwind.css` лише з реально використовуваних утиліт
- `site.css` — невеликий шар специфічних для сайту стилів плюс тема Pygments

Бінарник Tailwind CLI, бандл Pele і файли шрифтів завантажуються
під час першої збірки в `scripts/.vendor-cache/` (у gitignore) — див.
`scripts/vendor_assets.py`.

Анкори заголовків генеруються за точно таким самим алгоритмом з
`check_cross_references.heading_to_anchor`, тож посилання `#anchor`, перевірені
pre-commit-хуком, коректно розв'язуються на відрендереному сайті.
