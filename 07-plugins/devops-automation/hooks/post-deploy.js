#!/usr/bin/env node

/**
 * Post-deployment hook (PostToolUse on Bash)
 *
 * Registered in hooks/hooks.json. Claude Code runs it after every Bash
 * command that succeeded; it acts only on deploy commands (see
 * isDeployCommand) and exits 0 for everything else.
 *
 * Configuration (your own environment, optional):
 *   DEPLOY_DEPLOYMENT  Deployment name: runs `kubectl rollout status`
 *   DEPLOY_APP_LABEL   pod label selector, e.g. app=myapp: used when
 *                      DEPLOY_DEPLOYMENT isn't set, runs `kubectl wait`
 *   DEPLOY_NAMESPACE   namespace (default: your kubeconfig context)
 *
 * Output: exit 0 + JSON adds a note for Claude next to the tool result;
 *         exit 2 + stderr tells Claude the check failed
 *         (the deploy already ran, so nothing is blocked).
 * Read-only: runs `kubectl rollout status` or `kubectl wait` only.
 * It never changes the cluster.
 */

const { execFileSync } = require('child_process');
const path = require('path');

/**
 * True when the Bash command runs a deploy. Same heuristic as in
 * pre-deploy.js: it skips heredoc bodies and quoted strings, and looks
 * only at the first word of each simple command.
 */
// Words skipped before the program name: simple wrappers, then shell
// keywords and grouping tokens (`for …; do kubectl apply …`, `{ …; }`, `! …`).
const SKIP_WORDS = ['sudo', 'env', 'time', 'nohup', 'exec', 'command',
  'if', 'then', 'else', 'elif', 'do', 'while', 'until', '{', '!'];

function isDeployCommand(command) {
  const text = command
    .replace(/(<<-?\s*['"]?(\w+)['"]?[^\n]*)\n[\s\S]*?(?:\n\s*\2\s*(?=\n|$)|$)/g, '$1\n') // heredoc bodies (keep the opening line)
    .replace(/'[^']*'|"(?:\\.|[^"\\])*"/g, "''"); // quoted strings

  return text.split(/&&|\|\||[\n;|&()`]/).some((piece) => {
    const words = piece.trim().split(/\s+/).filter(Boolean);
    while (words.length && (/^\w+=/.test(words[0]) || SKIP_WORDS.includes(words[0]))) {
      words.shift(); // VAR=value prefixes, simple wrappers and shell keywords
    }
    if (!words.length) return false;

    const program = path.basename(words[0]);
    if (/^(deploy|rollback)\.sh$/.test(program)) return true;
    if (['bash', 'sh', 'zsh'].includes(program)) {
      const script = words.slice(1).find((w) => !w.startsWith('-'));
      return Boolean(script) && /^(deploy|rollback)\.sh$/.test(path.basename(script));
    }

    const verbs = { kubectl: ['apply', 'set', 'rollout'], helm: ['install', 'upgrade', 'rollback'] }[program];
    if (!verbs) return false;
    let i = 1;
    while (i < words.length && words[i].startsWith('-')) {
      // Skip global flags; `-n prod` style flags also skip their value.
      const takesValue = !words[i].includes('=') && i + 1 < words.length
        && !words[i + 1].startsWith('-') && !verbs.includes(words[i + 1]);
      i += takesValue ? 2 : 1;
    }
    const [verb, sub] = [words[i], words[i + 1]];
    if (program === 'helm') return verbs.includes(verb);
    return verb === 'apply' || (verb === 'set' && sub === 'image')
      || (verb === 'rollout' && ['restart', 'undo'].includes(sub));
  });
}

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

  if (input.tool_name !== 'Bash' || typeof command !== 'string' || !isDeployCommand(command)) {
    process.exit(0); // Not a deployment: nothing to do.
  }

  const { DEPLOY_DEPLOYMENT: deployment, DEPLOY_APP_LABEL: label, DEPLOY_NAMESPACE: namespace } = process.env;
  let args;
  let what;
  if (deployment) {
    // Waits for the new ReplicaSet to finish rolling out.
    args = ['rollout', 'status', `deployment/${deployment}`, '--timeout=120s'];
    what = `kubectl rollout status deployment/${deployment}`;
  } else if (label) {
    // Fallback: old pods that are still Ready also pass this check.
    args = ['wait', '--for=condition=ready', 'pod', '-l', label, '--timeout=120s'];
    what = `kubectl wait for pods with label ${label}`;
  } else {
    addContext('The post-deploy hook skipped its check because neither DEPLOY_DEPLOYMENT nor DEPLOY_APP_LABEL is set.');
  }
  if (namespace) args.push('-n', namespace);

  try {
    // 150s cap: above kubectl's own 120s timeout, below the 180s hook timeout.
    execFileSync('kubectl', args, { cwd: input.cwd || process.cwd(), stdio: 'pipe', timeout: 150000 });
  } catch (error) {
    if (error.code === 'ENOENT') {
      console.error('Post-deploy check skipped: kubectl was not found, so the rollout could not be checked.');
    } else {
      const detail = error.stderr ? error.stderr.toString().trim() : error.message;
      console.error(`Post-deploy check failed (${what}): ${detail}`);
    }
    process.exit(2);
  }

  // Add your smoke tests here, for example a read-only request to your own health endpoint.

  if (deployment) {
    addContext(`The post-deploy hook ran ${what}: the rollout finished.`);
  }
  addContext(`The post-deploy hook ran ${what}: those pods were Ready. This does not prove the new version rolled out; set DEPLOY_DEPLOYMENT for a rollout check.`);
}

main().catch((error) => {
  // Any exit code other than 0 or 2 is a non-blocking error.
  console.error(`post-deploy hook failed: ${error.message}`);
  process.exit(1);
});
