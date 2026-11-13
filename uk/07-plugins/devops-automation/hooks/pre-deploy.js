#!/usr/bin/env node

/**
 * Pre-deployment hook (PreToolUse on Bash)
 *
 * Registered in hooks/hooks.json. Claude Code runs it before every Bash
 * command; it acts only on deploy commands (see isDeployCommand) and
 * exits 0 for everything else.
 *
 * Input:  hook JSON on stdin (uses `tool_input.command` and `cwd`).
 * Output: exit 2 + stderr blocks the Bash call, and Claude sees the reason;
 *         exit 0 lets the normal permission flow continue.
 * Read-only: runs `kubectl version --client` and `kubectl cluster-info`
 * against the cluster in your own kubeconfig. It never changes the cluster.
 */

const { execFileSync } = require('child_process');
const path = require('path');

/**
 * True when the Bash command runs a deploy: deploy.sh / rollback.sh,
 * kubectl apply | set image | rollout restart | rollout undo,
 * or helm install | upgrade | rollback.
 *
 * A simple heuristic, not a shell parser. It drops heredoc bodies and quoted
 * strings, splits on newlines, &&, ||, ;, |, &, ( and ), and looks only at
 * the first word of each piece, so `echo "kubectl apply"`, `cat deploy.sh`
 * and `git commit -m "helm upgrade"` don't count. Global flags before the
 * verb (`kubectl -n prod apply`) do count.
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

function block(reason) {
  // Exit 2 on PreToolUse blocks the tool call; stderr is the reason Claude sees.
  console.error(reason);
  process.exit(2);
}

async function main() {
  const input = JSON.parse((await readStdin()) || '{}');
  const command = (input.tool_input && input.tool_input.command) || '';

  if (input.tool_name !== 'Bash' || typeof command !== 'string' || !isDeployCommand(command)) {
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
