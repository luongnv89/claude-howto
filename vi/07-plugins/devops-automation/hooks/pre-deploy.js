#!/usr/bin/env node

/**
 * Pre-deployment hook (PreToolUse on Bash)
 *
 * Registered in hooks/hooks.json. Claude Code runs it before every Bash
 * command; it acts only on deploy-like commands (see DEPLOY_PATTERN) and
 * exits 0 for everything else.
 *
 * Input:  hook JSON on stdin (uses `tool_input.command` and `cwd`).
 * Output: exit 2 + stderr blocks the Bash call, and Claude sees the reason;
 *         exit 0 lets the normal permission flow continue.
 * Read-only: runs `kubectl version --client` and `kubectl cluster-info`
 * against the cluster in your own kubeconfig. It never changes the cluster.
 */

const { execFileSync } = require('child_process');

const DEPLOY_PATTERN =
  /(deploy|rollback)\.sh\b|\bkubectl\s+(apply|set\s+image|rollout\s+(restart|undo))\b|\bhelm\s+(install|upgrade|rollback)\b/;

function readStdin() {
  return new Promise((resolve) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (chunk) => (data += chunk));
    process.stdin.on('end', () => resolve(data));
  });
}

function block(reason) {
  // Exit 2 on PreToolUse blocks the tool call; stderr is the reason Claude sees.
  console.error(reason);
  process.exit(2);
}

async function main() {
  const input = JSON.parse((await readStdin()) || '{}');
  const command = (input.tool_input && input.tool_input.command) || '';

  if (input.tool_name !== 'Bash' || !DEPLOY_PATTERN.test(command)) {
    process.exit(0); // Not a deployment: nothing to check.
  }

  const opts = { cwd: input.cwd || process.cwd(), stdio: 'pipe', timeout: 20000 };

  try {
    execFileSync('kubectl', ['version', '--client'], opts);
  } catch {
    block('Deployment blocked by pre-deploy hook: kubectl was not found. Install the Kubernetes CLI first.');
  }

  try {
    execFileSync('kubectl', ['cluster-info', '--request-timeout=10s'], opts);
  } catch {
    block('Deployment blocked by pre-deploy hook: kubectl cannot reach a cluster. Check your kubeconfig context.');
  }

  process.exit(0); // Checks passed: the deploy command goes ahead.
}

main().catch((error) => {
  // Any exit code other than 0 or 2 is a non-blocking error: the command still runs.
  console.error(`pre-deploy hook failed: ${error.message}`);
  process.exit(1);
});
