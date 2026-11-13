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

### Скрипти
- `deploy.sh` — Автоматизація розгортання
- `rollback.sh` — Автоматизація відкату
- `health-check.sh` — Утиліти перевірки стану

### Хуки

`hooks/hooks.json` реєструє обидва скрипти на виклики інструмента Bash. Вони діють лише на команди розгортання (`deploy.sh`, `rollback.sh`, `kubectl apply`, `kubectl set image`, `kubectl rollout restart|undo`, `helm install|upgrade|rollback`) і завершуються з кодом 0 для будь-якої іншої команди:

- `pre-deploy.js` (`PreToolUse`): блокує команду (код виходу 2), коли `kubectl` відсутній або не може дістатися кластера, і Claude бачить причину
- `post-deploy.js` (`PostToolUse`): перевіряє розгортання і повідомляє Claude, якщо воно не вдалося. Коли задано `DEPLOY_DEPLOYMENT`, запускає `kubectl rollout status` (до 120 с), що чекає на нові поди. Інакше, коли задано `DEPLOY_APP_LABEL`, як запасний варіант виконує `kubectl wait`, доки поди з цією міткою не стануть Ready; старі поди, що досі Ready, теж проходять цю перевірку. Коли не задано жодної з них, пропускає перевірку. У повідомленні для Claude зазначено, яку перевірку виконано

Обидва хуки лише читають стан кластера (`kubectl version`, `cluster-info`, `rollout status`, `wait`).

Як розпізнається команда: скрипти відкидають тіла heredoc і рядки в лапках, розбивають команду за переносами рядків, `&&`, `||`, `;`, `|` і `&` та дивляться на перше слово кожної частини (після `VAR=value`, обгорток на кшталт `sudo` чи `env` і ключових слів shell на кшталт `do`, `then` чи `!`). Глобальні прапорці перед підкомандою враховуються, тож `kubectl -n prod apply` і `helm -n prod upgrade` вважаються розгортаннями, а `echo "kubectl apply"`, `cat scripts/deploy.sh` і `git commit -m "helm upgrade notes"` — ні. Це евристика, а не парсер shell: вона пропускає розгортання, сховані в лапках (`bash -c "kubectl apply …"`), за іншими обгортками (`ssh`, `xargs`, `make deploy`) чи прапорцями обгорток (`sudo -E`, `env -i`), запущені через `source` чи `.`, що починаються зі шляху до скрипту в лапках (`"./scripts/deploy.sh"`), що стоять після незакритої лапки чи here-string `<<<`, або всередині інших скриптів. Вона також може спрацювати на незвичних значеннях прапорців, як-от `kubectl -n apply get pods`. Не покладайтеся на неї як на межу безпеки.

Якщо ви натиснете `Ctrl+Enter`, поки виконується команда розгортання, і це завершить хід, post-deploy хук однаково запуститься, коли команда завершиться, але Claude Code зупинить його через 10 секунд незалежно від його `timeout`, тож перевірка може не завершитися.

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
- Node.js (запускає скрипти хуків)
- Kubernetes CLI (kubectl)
- Налаштований доступ до кластера

## Конфігурація

Хуки та скрипти використовують вашу звичайну конфігурацію `kubectl` (`~/.kube/config` або `KUBECONFIG`, якщо ви його задали).

Опціонально, для перевірки після розгортання (задайте `DEPLOY_DEPLOYMENT` або `DEPLOY_APP_LABEL` для запасної перевірки готовності подів):
```bash
export DEPLOY_DEPLOYMENT="myapp"
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## Приклад робочого процесу

```text
User: /devops-automation:deploy production

Claude:
1. Делегує субагенту deployment-specialist
2. Запускає скрипт deploy.sh; pre-deploy хук спершу перевіряє kubectl і з'єднання з кластером
3. post-deploy хук чекає, поки поди стануть готовими
4. Надає підсумок розгортання

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
