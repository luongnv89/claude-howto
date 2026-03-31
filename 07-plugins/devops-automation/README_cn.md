<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps 自动化插件

用于部署、监控和故障响应的完整 DevOps 自动化解决方案。

## 功能特性

✅ 自动化部署
✅ 回滚流程
✅ 系统健康监控
✅ 故障响应工作流
✅ Kubernetes 集成

## 安装

```bash
/plugin install devops-automation
```

## 包含内容

### 斜杠命令
- `/deploy` - 部署到生产环境或预发布环境
- `/rollback` - 回滚到上一个版本
- `/status` - 检查系统健康状态
- `/incident` - 处理生产环境故障

### 子代理（Subagents）
- `deployment-specialist` - 部署操作专家
- `incident-commander` - 故障协调指挥
- `alert-analyzer` - 系统健康分析

### MCP 服务器
- Kubernetes 集成

### 脚本
- `deploy.sh` - 部署自动化
- `rollback.sh` - 回滚自动化
- `health-check.sh` - 健康检查工具

### 钩子（Hooks）
- `pre-deploy.js` - 部署前验证
- `post-deploy.js` - 部署后任务

## 使用方法

### 部署到预发布环境
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

### 处理故障
```
/incident
```

## 环境要求

- Claude Code 1.0+
- Kubernetes CLI（kubectl）
- 已配置集群访问权限

## 配置

配置您的 Kubernetes config：
```bash
export KUBECONFIG=~/.kube/config
```

## 工作流示例

```
用户：/deploy production

Claude：
1. 运行 pre-deploy 钩子（验证 kubectl、集群连接）
2. 委托给 deployment-specialist 子代理
3. 执行 deploy.sh 脚本
4. 通过 Kubernetes MCP 监控部署进度
5. 运行 post-deploy 钩子（等待 Pod 就绪、执行冒烟测试）
6. 提供部署摘要

结果：
✅ 部署完成
📦 版本：v2.1.0
🚀 Pod 状态：3/3 就绪
⏱️  耗时：2 分 34 秒
```
