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

### スクリプト
- `deploy.sh` — デプロイ自動化
- `rollback.sh` — ロールバック自動化
- `health-check.sh` — ヘルスチェックユーティリティ

### フック

`hooks/hooks.json` は両方のスクリプトを Bash ツール呼び出しに登録する。スクリプトはデプロイ系のコマンド（`deploy.sh`、`rollback.sh`、`kubectl apply`、`kubectl set image`、`kubectl rollout restart|undo`、`helm install|upgrade|rollback`）にのみ反応し、それ以外のコマンドでは終了コード 0 で終了する：

- `pre-deploy.js`（`PreToolUse`）：`kubectl` が見つからないかクラスタに到達できない場合、コマンドをブロックし（終了コード 2）、Claude にその理由が伝わる
- `post-deploy.js`（`PostToolUse`）：デプロイを確認し、失敗していれば Claude に伝える。`DEPLOY_DEPLOYMENT` が設定されている場合は `kubectl rollout status` を実行し（最大 120 秒）、新しい Pod を待つ。そうでなく `DEPLOY_APP_LABEL` が設定されている場合は、そのラベルの Pod が Ready になるのを `kubectl wait` で待つ方式にフォールバックする。この場合、まだ Ready な古い Pod もチェックを通過してしまう。どちらも未設定の場合はチェックをスキップする。Claude への注記には、どのチェックを実行したかが示される

どちらのフックもクラスタの状態を読み取るだけである（`kubectl version`、`cluster-info`、`rollout status`、`wait`）。

コマンドの判定方法：スクリプトはヒアドキュメントの本文とクォートされた文字列を取り除き、コマンドを改行、`&&`、`||`、`;`、`|`、`&` で分割し、各部分の最初の単語を見る（`VAR=value`、`sudo`、`env` などのラッパー、`do`、`then`、`!` などのシェルキーワードの後）。動詞の前にあるグローバルフラグも考慮されるため、`kubectl -n prod apply` や `helm -n prod upgrade` はデプロイとみなされるが、`echo "kubectl apply"`、`cat scripts/deploy.sh`、`git commit -m "helm upgrade notes"` はみなされない。これはシェルパーサーではなくヒューリスティックであり、クォート内に隠れたデプロイ（`bash -c "kubectl apply …"`）、他のラッパー（`ssh`、`xargs`、`make deploy`）やラッパーのフラグ（`sudo -E`、`env -i`）を介したデプロイ、`source` や `.` で実行されるデプロイ、クォートされたスクリプトパス（`"./scripts/deploy.sh"`）で始まるデプロイ、閉じていないクォートや `<<<` ヒアストリングの後にあるデプロイ、他のスクリプト内のデプロイは検出できない。また、`kubectl -n apply get pods` のような変わったフラグ値で誤検出することもある。安全上の境界として頼らないこと。

デプロイコマンドの実行中に `Ctrl+Enter` を押してターンが終了した場合でも、post-deploy フックはコマンドの完了時に実行される。ただし Claude Code は `timeout` の値にかかわらず 10 秒後にフックを強制終了するため、チェックが完了しない可能性がある。

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
- Node.js（フックスクリプトの実行用）
- Kubernetes CLI（kubectl）
- クラスタへのアクセス設定

## 設定

フックとスクリプトは通常の `kubectl` 設定（`~/.kube/config`、または設定していれば `KUBECONFIG`）を使用する。

任意（デプロイ後のチェック用。`DEPLOY_DEPLOYMENT` を設定するか、Pod の ready 待機によるフォールバックには `DEPLOY_APP_LABEL` を設定する）：
```bash
export DEPLOY_DEPLOYMENT="myapp"
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## ワークフロー例

```text
User: /devops-automation:deploy production

Claude:
1. Delegates to deployment-specialist subagent
2. Runs deploy.sh script; the pre-deploy hook first checks kubectl and the cluster connection
3. post-deploy hook waits for pods to be ready
4. Provides deployment summary

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
