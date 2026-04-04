---
name: DevOps 自动化插件
description: 为部署、监控和故障处理提供自动化工作流
tags: plugins, devops, automation
---

# DevOps 自动化插件

完整的 DevOps 自动化工作流，覆盖部署、监控和事故响应。

## 功能

✅ 自动化部署
✅ 回滚流程
✅ 系统健康监控
✅ 事故响应工作流
✅ Kubernetes 集成

## 安装

```bash
/plugin install devops-automation
```

## 包含内容

### Slash 命令
- `/deploy` - 部署到生产或预发环境
- `/rollback` - 回滚到上一个版本
- `/status` - 检查系统健康
- `/incident` - 处理生产事故

### 子 agents
- `deployment-specialist` - 部署操作
- `incident-commander` - 事故协调
- `alert-analyzer` - 系统健康分析

### MCP 服务器
- Kubernetes 集成

### 脚本
- `deploy.sh` - 部署自动化
- `rollback.sh` - 回滚自动化
- `health-check.sh` - 健康检查工具

### Hooks
- `pre-deploy.js` - 部署前验证
- `post-deploy.js` - 部署后任务

## 使用

### 部署到预发环境

```
/deploy staging
```

### 部署到生产环境

```
/deploy production
```

### 回滚

```
/rollback production
```

### 检查状态

```
/status
```

### 处理事故

```
/incident
```

## 要求

- Claude Code 1.0+
- Kubernetes CLI（kubectl）
- 已配置集群访问

## 配置

设置 Kubernetes 配置：

```bash
export KUBECONFIG=~/.kube/config
```

## 示例工作流

```
用户：/deploy production

Claude:
1. 运行 pre-deploy hook（验证 kubectl 和集群连接）
2. 将部署委派给 deployment-specialist subagent
3. 运行 deploy.sh 脚本
4. 通过 Kubernetes MCP 监控部署进度
5. 运行 post-deploy hook（等待 pods 就绪，执行 smoke tests）
6. 提供部署总结

结果：
✅ 部署完成
📦 版本：v2.1.0
🚀 Pods：3/3 已就绪
⏱️  用时：2m 34s
```
