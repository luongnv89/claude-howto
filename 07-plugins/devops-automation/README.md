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

### Scripts
- `deploy.sh` - Deployment automation
- `rollback.sh` - Rollback automation
- `health-check.sh` - Health check utilities

### Hooks

`hooks/hooks.json` registers both scripts on Bash tool calls. They act only on deploy commands (`deploy.sh`, `rollback.sh`, `kubectl apply`, `kubectl set image`, `kubectl rollout restart|undo`, `helm install|upgrade|rollback`) and exit 0 for every other command:

- `pre-deploy.js` (`PreToolUse`): blocks the command (exit code 2) when `kubectl` is missing or can't reach a cluster, and Claude sees why
- `post-deploy.js` (`PostToolUse`): checks the deploy and tells Claude if it failed. With `DEPLOY_DEPLOYMENT` set, it runs `kubectl rollout status` (up to 120s), which waits for the new pods. Otherwise, with `DEPLOY_APP_LABEL` set, it falls back to `kubectl wait` for pods with that label to be Ready; old pods that are still Ready also pass this check. With neither set, it skips the check. Its note to Claude says which check ran

Both hooks only read cluster state (`kubectl version`, `cluster-info`, `rollout status`, `wait`).

How a command is recognized: the scripts drop heredoc bodies and quoted strings, split the command on newlines, `&&`, `||`, `;`, `|` and `&`, and look at the first word of each part (after `VAR=value` and wrappers such as `sudo` or `env`). Global flags before the verb count, so `kubectl -n prod apply` and `helm -n prod upgrade` are deploys, while `echo "kubectl apply"`, `cat scripts/deploy.sh` and `git commit -m "helm upgrade notes"` are not. This is a heuristic, not a shell parser: it misses deploys hidden in quotes (`bash -c "kubectl apply …"`), behind other wrappers (`ssh`, `xargs`, `make deploy`) or inside other scripts. Don't rely on it as a safety boundary.

If you press `Ctrl+Enter` while a deploy command runs and that ends the turn, the post-deploy hook still runs when the command finishes, but Claude Code kills it after 10 seconds, whatever its `timeout`, so the check may not finish.

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
- Node.js (runs the hook scripts)
- Kubernetes CLI (kubectl)
- Cluster access configured

## Configuration

The hooks and scripts use your normal `kubectl` configuration (`~/.kube/config`, or `KUBECONFIG` if you set it).

Optional, for the post-deploy check (set `DEPLOY_DEPLOYMENT`, or `DEPLOY_APP_LABEL` for the pod-ready fallback):
```bash
export DEPLOY_DEPLOYMENT="myapp"
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## Example Workflow

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

**Last Updated**: October 18, 2026
**Claude Code Version**: 2.1.302
**Sources**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**Compatible Models**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
