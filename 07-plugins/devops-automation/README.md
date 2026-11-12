<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps Automation Plugin

Complete DevOps automation for deployment, monitoring, and incident response.

## Features

✅ Automated deployments
✅ Rollback procedures
✅ System health monitoring
✅ Incident response workflows
✅ Kubernetes integration

## Installation

```bash
claude --plugin-dir ./07-plugins/devops-automation
```

Check the plugin before you load it:

```bash
claude plugin validate ./07-plugins/devops-automation
```

## What's Included

### Slash Commands

Plugin commands are namespaced with the plugin `name` from `plugin.json`:

- `/devops-automation:deploy` - Deploy to production or staging
- `/devops-automation:rollback` - Rollback to previous version
- `/devops-automation:status` - Check system health
- `/devops-automation:incident` - Handle production incidents

### Subagents
- `deployment-specialist` - Deployment operations
- `incident-commander` - Incident coordination
- `alert-analyzer` - System health analysis

### MCP Servers

`.mcp.json` declares one server, `kubernetes`: the `mcp-server-kubernetes` npm package, run with `npx` and `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS=true`, so its delete tools are turned off. It shows up as `plugin:devops-automation:kubernetes` in `/mcp`.

### Scripts
- `deploy.sh` - Deployment automation
- `rollback.sh` - Rollback automation
- `health-check.sh` - Health check utilities

### Hooks

`hooks/hooks.json` registers both scripts on Bash tool calls. They act only on deploy commands (`deploy.sh`, `rollback.sh`, `kubectl apply`, `kubectl set image`, `kubectl rollout restart|undo`, `helm install|upgrade|rollback`) and exit 0 for every other command:

- `pre-deploy.js` (`PreToolUse`): blocks the command (exit code 2) when `kubectl` is missing or can't reach a cluster, and Claude sees why
- `post-deploy.js` (`PostToolUse`): waits up to 120s for pods labeled `DEPLOY_APP_LABEL` to be ready, and tells Claude if they aren't. It skips the wait when `DEPLOY_APP_LABEL` isn't set

Both hooks only read cluster state (`kubectl version`, `cluster-info`, `wait`).

## Usage

### Deploy to Staging
```text
/devops-automation:deploy staging
```

### Deploy to Production
```text
/devops-automation:deploy production
```

### Rollback
```text
/devops-automation:rollback production
```

### Check Status
```text
/devops-automation:status
```

### Handle Incident
```text
/devops-automation:incident
```

## Requirements

- Claude Code 2.1+
- Node.js (runs the hook scripts and the MCP server)
- Kubernetes CLI (kubectl)
- Cluster access configured

## Configuration

Set up your Kubernetes config (`.mcp.json` passes `KUBECONFIG` to the MCP server):
```bash
export KUBECONFIG=~/.kube/config
```

Optional, for the post-deploy readiness check:
```bash
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## Example Workflow

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

**Last Updated**: October 18, 2026
**Claude Code Version**: 2.1.302
**Sources**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
