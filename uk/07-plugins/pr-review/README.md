<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# Плагін PR Review

Повний робочий процес рев'ю PR з перевірками безпеки, тестування та документації.

## Функції

✅ Аналіз безпеки
✅ Перевірка покриття тестами
✅ Верифікація документації
✅ Оцінка якості коду
✅ Аналіз впливу на продуктивність

## Встановлення

```bash
claude --plugin-dir ./07-plugins/pr-review
```

Перевірте плагін перед завантаженням:

```bash
claude plugin validate ./07-plugins/pr-review
```

## Що включено

```text
pr-review/
├── .claude-plugin/
│   └── plugin.json      # "name": "pr-review" sets the command prefix
├── commands/            # each file becomes /pr-review:<file>
├── agents/
├── hooks/
│   ├── hooks.json       # registers pre-review.js
│   └── pre-review.js
└── .mcp.json            # GitHub MCP server
```

### Слеш-команди

Команди плагіна мають простір імен за `name` плагіна з `plugin.json`:

- `/pr-review:review-pr` — Комплексне рев'ю PR
- `/pr-review:check-security` — Рев'ю з фокусом на безпеці
- `/pr-review:check-tests` — Аналіз покриття тестами

### Субагенти
- `security-reviewer` — Виявлення вразливостей безпеки
- `test-checker` — Аналіз покриття тестами
- `performance-analyzer` — Оцінка впливу на продуктивність

### MCP-сервери

`.mcp.json` оголошує один сервер, `github`: офіційний MCP-сервер GitHub (`ghcr.io/github/github-mcp-server`), що запускається через Docker у режимі лише для читання. Образ закріплено на [релізі v2.1.0](https://github.com/github/github-mcp-server/releases/tag/v2.1.0); щоб оновити, змініть тег у `.mcp.json`. У `/mcp` він відображається як `plugin:pr-review:github`.

### Хуки

`hooks/hooks.json` реєструє `pre-review.js` на подію `UserPromptExpansion` з matcher для трьох команд вище. Matcher приймає і `pr-review:review-pr` (`command_name`, яке Claude Code 2.1.322 надсилає для команди плагіна), і просте `review-pr`. Коли ви вводите одну з них, хук:

- блокує команду (код виходу 2), якщо поточний каталог не є git-репозиторієм
- інакше додає до контексту Claude поточну гілку (або примітку, що HEAD відокремлений чи що в репозиторії ще немає комітів) та примітку про незакомічені зміни
- у bare-репозиторії (або всередині `.git`) додає лише примітку, що робочого дерева для перевірки немає

## Використання

### Базове рев'ю PR
```text
/pr-review:review-pr
```

### Тільки перевірка безпеки
```text
/pr-review:check-security
```

### Перевірка покриття тестами
```text
/pr-review:check-tests
```

## Вимоги

- Claude Code 2.1+
- Node.js (запускає скрипт хука)
- Docker (запускає MCP-сервер GitHub)
- Персональний токен доступу GitHub
- Git-репозиторій

## Конфігурація

Задайте GitHub-токен перед запуском Claude Code:
```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json` передає його серверу як `GITHUB_PERSONAL_ACCESS_TOKEN` — змінну, яку читає сервер. Запустіть `/mcp`, щоб перевірити, що `plugin:pr-review:github` підключено.

## Приклад робочого процесу

```text
User: /pr-review:review-pr

Claude:
1. pre-review хук перевіряє git-репозиторій і додає гілку до контексту
2. Отримує дані PR через GitHub MCP
3. Делегує рев'ю безпеки субагенту security-reviewer
4. Делегує тестування субагенту test-checker
5. Делегує продуктивність субагенту performance-analyzer
6. Синтезує всі знахідки
7. Надає комплексний звіт рев'ю

Результат:
✅ Безпека: Критичних проблем не знайдено
⚠️  Тестування: Покриття 65%, рекомендовано 80%+
✅ Продуктивність: Суттєвого впливу немає
📝 Рекомендації: Додати тести для граничних випадків
```

---

**Останнє оновлення**: 18 жовтня 2026
**Версія Claude Code**: 2.1.302
**Джерела**:
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
