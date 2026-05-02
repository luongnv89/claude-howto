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
/plugin install devops-automation
```

## What's Included

### Slash Commands
- `/deploy` - Deploy to production or staging
- `/rollback` - Rollback to previous version
- `/status` - Check system health
- `/incident` - Handle production incidents

### Subagents
- `deployment-specialist` - Deployment operations
- `incident-commander` - Incident coordination
- `alert-analyzer` - System health analysis

### MCP Servers
- Kubernetes integration

### Scripts
- `deploy.sh` - Deployment automation
- `rollback.sh` - Rollback automation
- `health-check.sh` - Health check utilities

### Hooks
- `pre-deploy.js` - Pre-deployment validation
- `post-deploy.js` - Post-deployment tasks

## Usage

### Deploy to Staging
```
/deploy staging
```

### Deploy to Production
```
/deploy production
```

### Rollback
```
/rollback production
```

### Check Status
```
/status
```

### Handle Incident
```
/incident
```

## Requirements

- Claude Code 1.0+
- Kubernetes CLI (kubectl)
- Cluster access configured

## Configuration

Set up your Kubernetes config:
```bash
export KUBECONFIG=~/.kube/config
```

## Example Workflow

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

**Last Updated**: May 2, 2026
**Claude Code Version**: 2.1.126
**Sources**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.126
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
