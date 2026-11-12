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
claude --plugin-dir ./07-plugins/devops-automation
```

加载插件之前先检查它：

```bash
claude plugin validate ./07-plugins/devops-automation
```

## 包含内容

### Slash 命令

插件命令以 `plugin.json` 中的插件 `name` 作为命名空间：

- `/devops-automation:deploy` - 部署到生产或预发环境
- `/devops-automation:rollback` - 回滚到上一个版本
- `/devops-automation:status` - 检查系统健康
- `/devops-automation:incident` - 处理生产事故

### 子 agents
- `deployment-specialist` - 部署操作
- `incident-commander` - 事故协调
- `alert-analyzer` - 系统健康分析

### MCP 服务器

`.mcp.json` 声明了一个服务器 `kubernetes`：npm 包 `mcp-server-kubernetes`，通过 `npx` 运行并设置 `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS=true`，因此其删除类工具会被关闭。它在 `/mcp` 中显示为 `plugin:devops-automation:kubernetes`。

### 脚本
- `deploy.sh` - 部署自动化
- `rollback.sh` - 回滚自动化
- `health-check.sh` - 健康检查工具

### Hooks

`hooks/hooks.json` 把这两个脚本注册到 Bash 工具调用上。它们只对部署命令生效（`deploy.sh`、`rollback.sh`、`kubectl apply`、`kubectl set image`、`kubectl rollout restart|undo`、`helm install|upgrade|rollback`），对其他所有命令都以退出码 0 退出：

- `pre-deploy.js`（`PreToolUse`）：当 `kubectl` 不存在或无法连接到集群时阻止该命令（退出码 2），并让 Claude 看到原因
- `post-deploy.js`（`PostToolUse`）：最多等待 120 秒，直到带有 `DEPLOY_APP_LABEL` 标签的 pods 就绪；如果没有就绪，会告知 Claude。未设置 `DEPLOY_APP_LABEL` 时跳过等待

两个 hooks 都只读取集群状态（`kubectl version`、`cluster-info`、`wait`）。

## 使用

### 部署到预发环境

```text
/devops-automation:deploy staging
```

### 部署到生产环境

```text
/devops-automation:deploy production
```

### 回滚

```text
/devops-automation:rollback production
```

### 检查状态

```text
/devops-automation:status
```

### 处理事故

```text
/devops-automation:incident
```

## 要求

- Claude Code 2.1+
- Node.js（运行 hook 脚本和 MCP 服务器）
- Kubernetes CLI（kubectl）
- 已配置集群访问

## 配置

设置 Kubernetes 配置（`.mcp.json` 会把 `KUBECONFIG` 传给 MCP 服务器）：

```bash
export KUBECONFIG=~/.kube/config
```

可选，用于部署后的就绪检查：

```bash
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## 示例工作流

```text
用户：/devops-automation:deploy production

Claude:
1. 将部署委派给 deployment-specialist subagent
2. 运行 deploy.sh 脚本；pre-deploy hook 会先检查 kubectl 和集群连接
3. 通过 Kubernetes MCP 监控部署进度
4. post-deploy hook 等待 pods 就绪
5. 提供部署总结

结果：
✅ 部署完成
📦 版本：v2.1.0
🚀 Pods：3/3 已就绪
⏱️  用时：2m 34s
```

---

**最后更新**: 2026 年 10 月 18 日
**Claude Code 版本**: 2.1.302
**来源**:
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
