#!/usr/bin/env node

/**
 * Pre-review hook (UserPromptExpansion)
 *
 * Registered in hooks/hooks.json. Runs when the user types
 * /pr-review:review-pr, /pr-review:check-security or /pr-review:check-tests,
 * before the command reaches Claude.
 *
 * Input:  hook JSON on stdin (uses `cwd` and `command_name`).
 * Output: exit 2 + stderr blocks the command (not a git repository);
 *         exit 0 + JSON adds context for Claude (e.g. uncommitted changes).
 * Read-only: runs `git rev-parse` and `git status` only.
 */

const { execFileSync } = require('child_process');

function readStdin() {
  return new Promise((resolve) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (chunk) => (data += chunk));
    process.stdin.on('end', () => resolve(data));
  });
}

function git(args, cwd) {
  return execFileSync('git', args, { cwd, encoding: 'utf8', stdio: 'pipe' });
}

async function main() {
  const input = JSON.parse((await readStdin()) || '{}');
  const cwd = input.cwd || process.cwd();
  const command = input.command_name || 'pr-review';

  try {
    git(['rev-parse', '--git-dir'], cwd);
  } catch {
    // Exit 2 blocks the expansion; stderr is shown to the user.
    console.error(`/${command} needs a git repository, and ${cwd} is not one.`);
    process.exit(2);
  }

  const notes = [];
  const branch = git(['rev-parse', '--abbrev-ref', 'HEAD'], cwd).trim();
  notes.push(`The current git branch is ${branch}.`);

  const status = git(['status', '--porcelain'], cwd);
  if (status.trim()) {
    const count = status.trim().split('\n').length;
    notes.push(`The working tree has ${count} uncommitted change(s), which are not part of any PR yet.`);
  }

  // Exit 0 with JSON: Claude Code adds additionalContext next to the prompt.
  console.log(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: 'UserPromptExpansion',
      additionalContext: notes.join(' '),
    },
  }));
}

main().catch((error) => {
  // Any exit code other than 0 or 2 is a non-blocking error: the command still runs.
  console.error(`pre-review hook failed: ${error.message}`);
  process.exit(1);
});
