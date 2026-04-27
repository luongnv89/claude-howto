<!-- i18n-source: 07-plugins/devops-automation/README.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
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
/plugin install devops-automation
```

## 同梱内容

### スラッシュコマンド
- `/deploy` — 本番またはステージングへデプロイ
- `/rollback` — 前バージョンへロールバック
- `/status` — システムの健全性を確認
- `/incident` — 本番インシデントに対応

### サブエージェント
- `deployment-specialist` — デプロイ作業
- `incident-commander` — インシデント統括
- `alert-analyzer` — システム健全性の解析

### MCP サーバー
- Kubernetes 連携

### スクリプト
- `deploy.sh` — デプロイ自動化
- `rollback.sh` — ロールバック自動化
- `health-check.sh` — ヘルスチェックユーティリティ

### フック
- `pre-deploy.js` — デプロイ前検証
- `post-deploy.js` — デプロイ後処理

## 使い方

### ステージングへデプロイ
```
/deploy staging
```

### 本番へデプロイ
```
/deploy production
```

### ロールバック
```
/rollback production
```

### ステータス確認
```
/status
```

### インシデント対応
```
/incident
```

## 必要要件

- Claude Code 1.0 以上
- Kubernetes CLI（kubectl）
- クラスタへのアクセス設定

## 設定

Kubernetes 設定をセットアップする：
```bash
export KUBECONFIG=~/.kube/config
```

## ワークフロー例

```
User: /deploy production

Claude:
1. Runs pre-deploy hook (validates kubectl, cluster connection)
2. Delegates to deployment-specialist subagent
3. Runs deploy.sh script
4. Monitors deployment progress via Kubernetes MCP
5. Runs post-deploy hook (waits for pods, smoke tests)
6. Provides deployment summary

Result:
✅ Deployment complete
📦 Version: v2.1.0
🚀 Pods: 3/3 ready
⏱️  Time: 2m 34s
```

---

**最終更新**: 2026 年 4 月 24 日
**Claude Code バージョン**: 2.1.119
**出典**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
**対応モデル**: Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
