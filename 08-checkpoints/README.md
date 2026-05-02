<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Checkpoints and Rewind

Checkpoints allow you to save conversation state and rewind to previous points in your Claude Code session. This is invaluable for exploring different approaches, recovering from mistakes, or comparing alternative solutions.

## Overview

Checkpoints allow you to save conversation state and rewind to previous points, enabling safe experimentation and exploration of multiple approaches. They are snapshots of your conversation state, including:
- All messages exchanged
- File modifications made
- Tool usage history
- Session context

Checkpoints are invaluable when exploring different approaches, recovering from mistakes, or comparing alternative solutions.

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Checkpoint** | Snapshot of conversation state including messages, files, and context |
| **Rewind** | Return to a previous checkpoint, discarding subsequent changes |
| **Branch Point** | Checkpoint from which multiple approaches are explored |

## Accessing Checkpoints

You can access and manage checkpoints in two primary ways:

### Using Keyboard Shortcut
Press `Esc` twice (`Esc` + `Esc`) to open the checkpoint interface and browse saved checkpoints.

### Using Slash Command
Use the `/rewind` command (alias: `/checkpoint`) for quick access:

```bash
# Open rewind interface
/rewind

# Or use the alias
/checkpoint
```

## Rewind Options

When you rewind, you are presented with a menu of five options:

1. **Restore code and conversation** -- Revert both files and messages to that checkpoint
2. **Restore conversation** -- Rewind messages only, keep your current code as-is
3. **Restore code** -- Revert file changes only, keep the full conversation history
4. **Summarize from here** -- Compress the conversation from this point forward into an AI-generated summary, freeing context window space. Messages before the selected point stay intact. No files on disk are changed. The original messages are preserved in the session transcript. You can optionally provide instructions to focus the summary on specific topics.
5. **Never mind** -- Cancel and return to the current state

> **Note**: After restoring the conversation or summarizing, the original prompt from the selected message is restored into the input field so you can re-send or edit it.

## Automatic Checkpoints

Claude Code automatically creates checkpoints for you:

- **Every user prompt** - A new checkpoint is created with each user input
- **Persistent** - Checkpoints persist across sessions
- **Auto-cleaned** - Checkpoints are automatically cleaned up after 30 days

This means you can always rewind to any previous point in your conversation, from a few minutes ago to days before.

## Use Cases

| Scenario | Workflow |
|----------|----------|
| **Exploring Approaches** | Save → Try A → Save → Rewind → Try B → Compare |
| **Safe Refactoring** | Save → Refactor → Test → If fail: Rewind |
| **A/B Testing** | Save → Design A → Save → Rewind → Design B → Compare |
| **Mistake Recovery** | Notice issue → Rewind to last good state |

## Using Checkpoints

### Viewing and Rewinding

Press `Esc` twice or use `/rewind` to open the checkpoint browser. You'll see a list of all available checkpoints with timestamps. Select any checkpoint to rewind to that state.

### Checkpoint Details

Each checkpoint shows:
- Timestamp of when it was created
- Files that were modified
- Number of messages in the conversation
- Tools that were used

## Practical Examples

### Example 1: Exploring Different Approaches

```
User: Let's add a caching layer to the API

Claude: I'll add Redis caching to your API endpoints...
[Makes changes at checkpoint A]

User: Actually, let's try in-memory caching instead

Claude: I'll rewind to explore a different approach...
[User presses Esc+Esc and rewinds to checkpoint A]
[Implements in-memory caching at checkpoint B]

User: Now I can compare both approaches
```

### Example 2: Recovering from Mistakes

```
User: Refactor the authentication module to use JWT

Claude: I'll refactor the authentication module...
[Makes extensive changes]

User: Wait, that broke the OAuth integration. Let's go back.

Claude: I'll help you rewind to before the refactoring...
[User presses Esc+Esc and selects the checkpoint before the refactor]

User: Let's try a more conservative approach this time
```

### Example 3: Safe Experimentation

```
User: Let's try rewriting this in a functional style
[Creates checkpoint before experiment]

Claude: [Makes experimental changes]

User: The tests are failing. Let's rewind.
[User presses Esc+Esc and rewinds to the checkpoint]

Claude: I've rewound the changes. Let's try a different approach.
```

### Example 4: Branching Approaches

```
User: I want to compare two database designs
[Takes note of checkpoint - call it "Start"]

Claude: I'll create the first design...
[Implements Schema A]

User: Now let me go back and try the second approach
[User presses Esc+Esc and rewinds to "Start"]

Claude: Now I'll implement Schema B...
[Implements Schema B]

User: Great! Now I have both schemas to choose from
```

## Checkpoint Retention

Claude Code automatically manages your checkpoints:

- Checkpoints are created automatically with every user prompt
- Old checkpoints are retained for up to 30 days
- Checkpoints are cleaned up automatically to prevent unlimited storage growth

## Workflow Patterns

### Branching Strategy for Exploration

When exploring multiple approaches:

```
1. Start with initial implementation → Checkpoint A
2. Try Approach 1 → Checkpoint B
3. Rewind to Checkpoint A
4. Try Approach 2 → Checkpoint C
5. Compare results from B and C
6. Choose best approach and continue
```

### Safe Refactoring Pattern

When making significant changes:

```
1. Current state → Checkpoint (auto)
2. Start refactoring
3. Run tests
4. If tests pass → Continue working
5. If tests fail → Rewind and try different approach
```

## Best Practices

Since checkpoints are created automatically, you can focus on your work without worrying about manually saving state. However, keep these practices in mind:

### Using Checkpoints Effectively

✅ **Do:**
- Review available checkpoints before rewinding
- Use rewind when you want to explore different directions
- Keep checkpoints to compare different approaches
- Understand what each rewind option does (restore code and conversation, restore conversation, restore code, or summarize)

❌ **Don't:**
- Rely on checkpoints alone for code preservation
- Expect checkpoints to track external file system changes
- Use checkpoints as a substitute for git commits

## Configuration

Checkpoints are a built-in default behavior in Claude Code and do not require any configuration to enable. Every user prompt automatically creates a checkpoint.

The only checkpoint-related setting is `cleanupPeriodDays`, which controls how long sessions and checkpoints are retained:

```json
{
  "cleanupPeriodDays": 30
}
```

- `cleanupPeriodDays`: Number of days to retain session history and checkpoints (default: `30`)

> **v2.1.117 update**: `cleanupPeriodDays` now governs retention for four on-disk caches, not just checkpoints:
>
> - Session checkpoints
> - `~/.claude/tasks/` — persistent task lists
> - `~/.claude/shell-snapshots/` — captured shell-environment snapshots
> - `~/.claude/backups/` — rolling setting / CLAUDE.md backups
>
> A single setting now prunes all four directories uniformly after the same number of days.

## Limitations

Checkpoints have the following limitations:

- **Bash command changes NOT tracked** - Operations like `rm`, `mv`, `cp` on the filesystem are not captured in checkpoints
- **External changes NOT tracked** - Changes made outside Claude Code (in your editor, terminal, etc.) are not captured
- **Not a replacement for version control** - Use git for permanent, auditable changes to your codebase

## Troubleshooting

### Missing Checkpoints

**Problem**: Expected checkpoint not found

**Solution**:
- Check if checkpoints were cleared
- Check disk space
- Ensure `cleanupPeriodDays` is set high enough (default: 30 days)

### Rewind Failed

**Problem**: Cannot rewind to checkpoint

**Solution**:
- Ensure no uncommitted changes conflict
- Check if checkpoint is corrupted
- Try rewinding to a different checkpoint

## Integration with Git

Checkpoints complement (but don't replace) git:

| Feature | Git | Checkpoints |
|---------|-----|-------------|
| Scope | File system | Conversation + files |
| Persistence | Permanent | Session-based |
| Granularity | Commits | Any point |
| Speed | Slower | Instant |
| Sharing | Yes | Limited |

Use both together:
1. Use checkpoints for rapid experimentation
2. Use git commits for finalized changes
3. Create checkpoint before git operations
4. Commit successful checkpoint states to git

## Quick Start Guide

### Basic Workflow

1. **Work normally** - Claude Code creates checkpoints automatically
2. **Want to go back?** - Press `Esc` twice or use `/rewind`
3. **Choose checkpoint** - Select from the list to rewind
4. **Select what to restore** - Choose from restore code and conversation, restore conversation, restore code, summarize from here, or cancel
5. **Continue working** - You're back at that point

### Keyboard Shortcuts

- **`Esc` + `Esc`** - Open checkpoint browser
- **`/rewind`** - Alternative way to access checkpoints
- **`/checkpoint`** - Alias for `/rewind`

## Knowing When to Rewind: Context Monitoring

Checkpoints let you go back — but how do you know *when* you should? As your conversation grows, Claude's context window fills up and model quality silently degrades. You might be shipping code from a half-blind model without realizing it.

**[cc-context-stats](https://github.com/luongnv89/cc-context-stats)** solves this by adding real-time **context zones** to your Claude Code status bar. It tracks where you are in the context window — from **Plan** (green, safe to plan and code) through **Code** (yellow, avoid starting new plans) to **Dump** (orange, finish up and rewind). When you see the zone shift, you know it's time to checkpoint and start fresh instead of pushing through with degraded output.

## Related Concepts

- **[Advanced Features](../09-advanced-features/)** - Planning mode and other advanced capabilities
- **[Memory Management](../02-memory/)** - Managing conversation history and context
- **[Slash Commands](../01-slash-commands/)** - User-invoked shortcuts
- **[Hooks](../06-hooks/)** - Event-driven automation
- **[Plugins](../07-plugins/)** - Bundled extension packages

## Additional Resources

- [Official Checkpointing Documentation](https://code.claude.com/docs/en/checkpointing)
- [Advanced Features Guide](../09-advanced-features/) - Extended thinking and other capabilities

## Summary

Checkpoints are an automatic feature in Claude Code that lets you safely explore different approaches without fear of losing work. Every user prompt creates a new checkpoint automatically, so you can rewind to any previous point in your session.

Key benefits:
- Experiment fearlessly with multiple approaches
- Quickly recover from mistakes
- Compare different solutions side-by-side
- Integrate safely with version control systems

Remember: checkpoints are not a replacement for git. Use checkpoints for rapid experimentation and git for permanent code changes.

---

**Last Updated**: May 2, 2026
**Claude Code Version**: 2.1.126
**Sources**:
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/settings
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
