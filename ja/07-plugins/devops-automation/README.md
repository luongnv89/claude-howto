<!-- i18n-source: 07-plugins/devops-automation/README.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps Automation プラグイン

デプロイ、監視、インシデントレスポンスを統合した DevOps 自動化プラグイン。

## 機能

✅ 自動デプロイ
✅ ロールバック手順
✅ システム健全性の監視
✅ インシデントレスポンスのワークフロー
✅ Kubernetes 連携

## インストール

```bash
claude --plugin-dir ./07-plugins/devops-automation
```

読み込む前にプラグインをチェックする：

```bash
claude plugin validate ./07-plugins/devops-automation
```

## 同梱内容

### スラッシュコマンド

プラグインのコマンドは、`plugin.json` のプラグイン `name` で名前空間が付く：

- `/devops-automation:deploy` — 本番またはステージングへデプロイ
- `/devops-automation:rollback` — 前バージョンへロールバック
- `/devops-automation:status` — システムの健全性を確認
- `/devops-automation:incident` — 本番インシデントに対応

### サブエージェント
- `deployment-specialist` — デプロイ作業
- `incident-commander` — インシデント統括
- `alert-analyzer` — システム健全性の解析

### MCP サーバー

`.mcp.json` は `kubernetes` という 1 つのサーバーを宣言する。npm パッケージ `mcp-server-kubernetes` を `npx` で `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS=true` を付けて実行するため、削除系のツールは無効になる。`/mcp` では `plugin:devops-automation:kubernetes` として表示される。

### スクリプト
- `deploy.sh` — デプロイ自動化
- `rollback.sh` — ロールバック自動化
- `health-check.sh` — ヘルスチェックユーティリティ

### フック

`hooks/hooks.json` は両方のスクリプトを Bash ツール呼び出しに登録する。スクリプトはデプロイ系のコマンド（`deploy.sh`、`rollback.sh`、`kubectl apply`、`kubectl set image`、`kubectl rollout restart|undo`、`helm install|upgrade|rollback`）にのみ反応し、それ以外のコマンドでは終了コード 0 で終了する：

- `pre-deploy.js`（`PreToolUse`）：`kubectl` が見つからないかクラスタに到達できない場合、コマンドをブロックし（終了コード 2）、Claude にその理由が伝わる
- `post-deploy.js`（`PostToolUse`）：`DEPLOY_APP_LABEL` のラベルが付いた Pod が ready になるまで最大 120 秒待機し、ready にならなければ Claude に伝える。`DEPLOY_APP_LABEL` が未設定の場合は待機をスキップする

どちらのフックもクラスタの状態を読み取るだけである（`kubectl version`、`cluster-info`、`wait`）。

## 使い方

### ステージングへデプロイ
```text
/devops-automation:deploy staging
```

### 本番へデプロイ
```text
/devops-automation:deploy production
```

### ロールバック
```text
/devops-automation:rollback production
```

### ステータス確認
```text
/devops-automation:status
```

### インシデント対応
```text
/devops-automation:incident
```

## 必要要件

- Claude Code 1.0 以上
- Node.js（フックスクリプトと MCP サーバーの実行用）
- Kubernetes CLI（kubectl）
- クラスタへのアクセス設定

## 設定

Kubernetes 設定をセットアップする（`.mcp.json` は `KUBECONFIG` を MCP サーバーに渡す）：
```bash
export KUBECONFIG=~/.kube/config
```

任意（デプロイ後の readiness チェック用）：
```bash
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## ワークフロー例

```text
User: /devops-automation:deploy production

Claude:
1. Delegates to deployment-specialist subagent
2. Runs deploy.sh script; the pre-deploy hook first checks kubectl and the cluster connection
3. Monitors deployment progress via Kubernetes MCP
4. post-deploy hook waits for pods to be ready
5. Provides deployment summary

Result:
✅ Deployment complete
📦 Version: v2.1.0
🚀 Pods: 3/3 ready
⏱️  Time: 2m 34s
```

---

**最終更新**: 2026 年 10 月 18 日
**Claude Code バージョン**: 2.1.302
**出典**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**対応モデル**: Claude Fable 5.2、Claude Fable 5.1、Claude Fable 5、Claude Opus 5.5、Claude Opus 5、Claude Sonnet 5.5、Claude Sonnet 5、Claude Sonnet 4.6、Claude Opus 4.8、Claude Haiku 5.5、Claude Haiku 4.5
