<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps Automation Plugin

完整的 DevOps 自動化，涵蓋部署、監控與事件回應。

## 功能

✅ 自動化部署
✅ 回滾程序
✅ 系統健康監控
✅ 事件回應工作流程
✅ Kubernetes 整合

## 安裝

```bash
/plugin install devops-automation
```

## 包含內容

### Slash Commands
- `/deploy` - 部署至正式環境或測試環境
- `/rollback` - 回滾至先前版本
- `/status` - 檢查系統健康狀態
- `/incident` - 處理正式環境事件

### Subagents
- `deployment-specialist` - 部署作業
- `incident-commander` - 事件協調
- `alert-analyzer` - 系統健康分析

### MCP Servers
- Kubernetes 整合

### 腳本
- `deploy.sh` - 部署自動化
- `rollback.sh` - 回滾自動化
- `health-check.sh` - 健康檢查工具

### Hooks
- `pre-deploy.js` - 預部署驗證
- `post-deploy.js` - 部署後任務

## 使用方式

### 部署至測試環境
```
/deploy staging
```

### 部署至正式環境
```
/deploy production
```

### 回滾
```
/rollback production
```

### 檢查狀態
```
/status
```

### 處理事件
```
/incident
```

## 需求

- Claude Code 1.0+
- Kubernetes CLI (kubectl)
- 已設定叢集存取權限

## 組態設定

設定 Kubernetes 組態：
```bash
export KUBECONFIG=~/.kube/config
```

## 範例工作流程

```
使用者：/deploy production

Claude：
1. 執行預部署 hook（驗證 kubectl、叢集連線）
2. 委派給 deployment-specialist subagent
3. 執行 deploy.sh 腳本
4. 透過 Kubernetes MCP 監控部署進度
5. 執行部署後 hook（等待 Pod、煙霧測試）
6. 提供部署摘要

結果：
✅ 部署完成
📦 版本：v2.1.0
🚀 Pod：3/3 就緒
⏱️  時間：2分34秒
```

