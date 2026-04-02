<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps Automation Plugin

用于部署、监控与故障响应的 DevOps 自动化插件。

## Features

✅ 自动化部署  
✅ 回滚流程  
✅ 系统健康监控  
✅ 生产事故响应工作流  
✅ Kubernetes 集成

## Installation

```bash
/plugin install devops-automation
```

## What's Included

### Slash Commands
- `/deploy` - 部署到生产或预发环境
- `/rollback` - 回滚到上一版本
- `/status` - 检查系统健康状态
- `/incident` - 处理生产事故

### Subagents
- `deployment-specialist` - 负责部署操作
- `incident-commander` - 负责事故协调
- `alert-analyzer` - 负责系统告警分析

### MCP Servers
- Kubernetes 集成

### Scripts
- `deploy.sh` - 部署自动化脚本
- `rollback.sh` - 回滚自动化脚本
- `health-check.sh` - 健康检查脚本

### Hooks
- `pre-deploy.js` - 部署前校验
- `post-deploy.js` - 部署后任务

## Usage

### Deploy to Staging

```text
/deploy staging
```

### Deploy to Production

```text
/deploy production
```

### Rollback

```text
/rollback production
```

### Check Status

```text
/status
```

### Handle Incident

```text
/incident
```

## Requirements

- Claude Code 1.0+
- Kubernetes CLI（`kubectl`）
- 已配置集群访问

## Configuration

设置 Kubernetes 配置：

```bash
export KUBECONFIG=~/.kube/config
```

## Example Workflow

```text
User: /deploy production

Claude:
1. 运行 pre-deploy hook（校验 kubectl 与集群连通性）
2. 委派 deployment-specialist subagent
3. 执行 deploy.sh
4. 通过 Kubernetes MCP 监控部署进度
5. 运行 post-deploy hook（等待 pods、执行 smoke tests）
6. 输出部署摘要

Result:
✅ Deployment complete
📦 Version: v2.1.0
🚀 Pods: 3/3 ready
⏱️  Time: 2m 34s
```
