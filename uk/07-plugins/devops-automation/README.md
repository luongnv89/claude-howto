<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# Плагін DevOps Automation

Повна автоматизація DevOps для розгортання, моніторингу та реагування на інциденти.

## Функції

✅ Автоматизовані розгортання
✅ Процедури відкату
✅ Моніторинг стану системи
✅ Робочі процеси реагування на інциденти
✅ Інтеграція з Kubernetes

## Встановлення

```bash
claude --plugin-dir ./07-plugins/devops-automation
```

Перевірте плагін перед завантаженням:

```bash
claude plugin validate ./07-plugins/devops-automation
```

## Що включено

### Слеш-команди

Команди плагіна мають простір імен за `name` плагіна з `plugin.json`:

- `/devops-automation:deploy` — Розгортання на продакшен або стейджинг
- `/devops-automation:rollback` — Відкат до попередньої версії
- `/devops-automation:status` — Перевірка стану системи
- `/devops-automation:incident` — Обробка інцидентів на продакшені

### Субагенти
- `deployment-specialist` — Операції розгортання
- `incident-commander` — Координація інцидентів
- `alert-analyzer` — Аналіз стану системи

### MCP-сервери

`.mcp.json` оголошує один сервер, `kubernetes`: npm-пакет `mcp-server-kubernetes`, що запускається через `npx` з `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS=true`, тож його інструменти видалення вимкнено. У `/mcp` він відображається як `plugin:devops-automation:kubernetes`.

### Скрипти
- `deploy.sh` — Автоматизація розгортання
- `rollback.sh` — Автоматизація відкату
- `health-check.sh` — Утиліти перевірки стану

### Хуки

`hooks/hooks.json` реєструє обидва скрипти на виклики інструмента Bash. Вони діють лише на команди розгортання (`deploy.sh`, `rollback.sh`, `kubectl apply`, `kubectl set image`, `kubectl rollout restart|undo`, `helm install|upgrade|rollback`) і завершуються з кодом 0 для будь-якої іншої команди:

- `pre-deploy.js` (`PreToolUse`): блокує команду (код виходу 2), коли `kubectl` відсутній або не може дістатися кластера, і Claude бачить причину
- `post-deploy.js` (`PostToolUse`): чекає до 120 с, поки поди з міткою `DEPLOY_APP_LABEL` стануть готовими, і повідомляє Claude, якщо вони не готові. Пропускає очікування, коли `DEPLOY_APP_LABEL` не задано

Обидва хуки лише читають стан кластера (`kubectl version`, `cluster-info`, `wait`).

## Використання

### Розгортання на стейджинг
```text
/devops-automation:deploy staging
```

### Розгортання на продакшен
```text
/devops-automation:deploy production
```

### Відкат
```text
/devops-automation:rollback production
```

### Перевірка стану
```text
/devops-automation:status
```

### Обробка інциденту
```text
/devops-automation:incident
```

## Вимоги

- Claude Code 2.1+
- Node.js (запускає скрипти хуків і MCP-сервер)
- Kubernetes CLI (kubectl)
- Налаштований доступ до кластера

## Конфігурація

Налаштуйте конфіг Kubernetes (`.mcp.json` передає `KUBECONFIG` MCP-серверу):
```bash
export KUBECONFIG=~/.kube/config
```

Опціонально, для перевірки готовності після розгортання:
```bash
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## Приклад робочого процесу

```text
User: /devops-automation:deploy production

Claude:
1. Делегує субагенту deployment-specialist
2. Запускає скрипт deploy.sh; pre-deploy хук спершу перевіряє kubectl і з'єднання з кластером
3. Моніторить прогрес розгортання через Kubernetes MCP
4. post-deploy хук чекає, поки поди стануть готовими
5. Надає підсумок розгортання

Результат:
✅ Розгортання завершено
📦 Версія: v2.1.0
🚀 Поди: 3/3 готові
⏱️  Час: 2хв 34с
```

---

**Останнє оновлення**: 18 жовтня 2026
**Версія Claude Code**: 2.1.302
**Джерела**:
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
