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

### 脚本
- `deploy.sh` - 部署自动化
- `rollback.sh` - 回滚自动化
- `health-check.sh` - 健康检查工具

### Hooks

`hooks/hooks.json` 把这两个脚本注册到 Bash 工具调用上。它们只对部署命令生效（`deploy.sh`、`rollback.sh`、`kubectl apply`、`kubectl set image`、`kubectl rollout restart|undo`、`helm install|upgrade|rollback`），对其他所有命令都以退出码 0 退出：

- `pre-deploy.js`（`PreToolUse`）：当 `kubectl` 不存在或无法连接到集群时阻止该命令（退出码 2），并让 Claude 看到原因
- `post-deploy.js`（`PostToolUse`）：检查部署结果，如果失败会告知 Claude。设置了 `DEPLOY_DEPLOYMENT` 时，它运行 `kubectl rollout status`（最多 120 秒），等待新的 pods 就绪。否则，如果设置了 `DEPLOY_APP_LABEL`，它会退而使用 `kubectl wait` 等待带有该标签的 pods 变为 Ready；仍处于 Ready 状态的旧 pods 也会通过这项检查。两者都未设置时跳过检查。它给 Claude 的提示会说明运行了哪项检查

两个 hooks 都只读取集群状态（`kubectl version`、`cluster-info`、`rollout status`、`wait`）。

命令的识别方式：脚本会去掉 heredoc 正文和引号内的字符串，按换行符、`&&`、`||`、`;`、`|` 和 `&` 拆分命令，并查看每一段的第一个词（跳过 `VAR=value`、`sudo`、`env` 等包装命令，以及 `do`、`then`、`!` 等 shell 关键字）。动词之前的全局参数也会被识别，所以 `kubectl -n prod apply` 和 `helm -n prod upgrade` 算作部署，而 `echo "kubectl apply"`、`cat scripts/deploy.sh` 和 `git commit -m "helm upgrade notes"` 不算。这是一种启发式方法，而不是 shell 解析器：它会漏掉藏在引号里的部署（`bash -c "kubectl apply …"`）、藏在其他包装命令（`ssh`、`xargs`、`make deploy`）或包装命令参数（`sudo -E`、`env -i`）后面的部署、用 `source` 或 `.` 运行的部署、以带引号的脚本路径（`"./scripts/deploy.sh"`）开头的部署、位于未闭合引号或 `<<<` here-string 之后的部署，以及写在其他脚本里的部署。遇到 `kubectl -n apply get pods` 这类不寻常的参数值时，它也可能误报。不要把它当作安全边界。

如果你在部署命令运行期间按下 `Ctrl+Enter` 并因此结束了当前轮次，post-deploy hook 仍会在命令结束时运行，但无论其 `timeout` 设为多少，Claude Code 都会在 10 秒后终止它，因此检查可能无法完成。

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
- Node.js（运行 hook 脚本）
- Kubernetes CLI（kubectl）
- 已配置集群访问

## 配置

hooks 和脚本使用你常规的 `kubectl` 配置（`~/.kube/config`，如果设置了 `KUBECONFIG` 则使用它）。

可选，用于部署后的检查（设置 `DEPLOY_DEPLOYMENT`，或设置 `DEPLOY_APP_LABEL` 以使用 pod 就绪等待作为回退方案）：

```bash
export DEPLOY_DEPLOYMENT="myapp"
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## 示例工作流

```text
用户：/devops-automation:deploy production

Claude:
1. 将部署委派给 deployment-specialist subagent
2. 运行 deploy.sh 脚本；pre-deploy hook 会先检查 kubectl 和集群连接
3. post-deploy hook 等待 pods 就绪
4. 提供部署总结

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
