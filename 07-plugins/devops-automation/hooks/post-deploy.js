#!/usr/bin/env node

/**
 * Post-deployment hook (PostToolUse on Bash)
 *
 * Registered in hooks/hooks.json. Claude Code runs it after every Bash
 * command that succeeded; it acts only on deploy-like commands (see
 * DEPLOY_PATTERN) and exits 0 for everything else.
 *
 * Configuration (your own environment, optional):
 *   DEPLOY_APP_LABEL  pod label selector to wait for, e.g. app=myapp
 *   DEPLOY_NAMESPACE  namespace of those pods (default: kubeconfig context)
 *
 * Output: exit 0 + JSON adds a note for Claude next to the tool result;
 *         exit 2 + stderr tells Claude the pods did not become ready
 *         (the deploy already ran, so nothing is blocked).
 * Read-only: runs `kubectl wait` only. It never changes the cluster.
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

function addContext(text) {
  console.log(JSON.stringify({
    hookSpecificOutput: { hookEventName: 'PostToolUse', additionalContext: text },
  }));
  process.exit(0);
}

async function main() {
  const input = JSON.parse((await readStdin()) || '{}');
  const command = (input.tool_input && input.tool_input.command) || '';

  if (input.tool_name !== 'Bash' || !DEPLOY_PATTERN.test(command)) {
    process.exit(0); // Not a deployment: nothing to do.
  }

  const label = process.env.DEPLOY_APP_LABEL;
  if (!label) {
    addContext('The post-deploy hook skipped the pod readiness wait because DEPLOY_APP_LABEL is not set.');
  }

  const args = ['wait', '--for=condition=ready', 'pod', '-l', label, '--timeout=120s'];
  if (process.env.DEPLOY_NAMESPACE) args.push('-n', process.env.DEPLOY_NAMESPACE);

  try {
    execFileSync('kubectl', args, { cwd: input.cwd || process.cwd(), stdio: 'pipe', timeout: 150000 });
  } catch (error) {
    const detail = error.stderr ? error.stderr.toString().trim() : error.message;
    console.error(`Post-deploy check: pods with label ${label} are not ready after 120s. ${detail}`);
    process.exit(2);
  }

  // Add your smoke tests here, for example a read-only request to your own health endpoint.

  addContext(`The post-deploy hook confirmed that pods with label ${label} are ready.`);
}

main().catch((error) => {
  // Any exit code other than 0 or 2 is a non-blocking error.
  console.error(`post-deploy hook failed: ${error.message}`);
  process.exit(1);
});
