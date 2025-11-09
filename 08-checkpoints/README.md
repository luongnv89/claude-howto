![Claude How To](../claude-howto-logo.svg)

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

## Commands

All checkpoint operations are performed using the `/checkpoint` command:

```bash
# Create checkpoint
/checkpoint save "Before refactoring"

# List checkpoints
/checkpoint list

# Rewind to checkpoint
/checkpoint rewind "Before refactoring"

# Compare checkpoints
/checkpoint diff checkpoint-1 checkpoint-2

# Delete checkpoint
/checkpoint delete checkpoint-1

# Export checkpoint
/checkpoint export "name" ~/checkpoints/backup.json
```

## Creating Checkpoints

### Automatic Checkpoints
Claude Code automatically creates checkpoints at key moments:
- Before major refactoring operations
- Before potentially destructive commands
- At regular intervals during long sessions
- Before running tests or builds

### Manual Checkpoints
Create checkpoints explicitly:

```
User: /checkpoint save "Before API refactor"
```

```
User: /checkpoint create pre-deployment
```

## Use Cases

| Scenario | Workflow |
|----------|----------|
| **Exploring Approaches** | Save → Try A → Save → Rewind → Try B → Compare |
| **Safe Refactoring** | Save → Refactor → Test → If fail: Rewind |
| **A/B Testing** | Save → Design A → Save → Rewind → Design B → Compare |
| **Mistake Recovery** | Notice issue → Rewind to last good state |

## Using Checkpoints

### List Checkpoints
View all available checkpoints:

```
User: /checkpoint list
```

Output:
```
Checkpoints:
1. [2025-11-08 10:30:15] Auto: Before file edit
2. [2025-11-08 10:45:22] Manual: Before API refactor
3. [2025-11-08 11:02:10] Auto: Before git commit
4. [2025-11-08 11:15:45] Manual: pre-deployment
```

### Rewind to Checkpoint
Return to a previous checkpoint:

```
User: /checkpoint rewind 2
```

Or by name:
```
User: /checkpoint rewind "Before API refactor"
```

### Compare Checkpoints
See what changed between checkpoints:

```
User: /checkpoint diff 2 4
```

## Practical Examples

### Example 1: Exploring Different Approaches

```
User: Let's add a caching layer to the API

Claude: I'll add Redis caching to your API endpoints...
[Makes changes]

User: /checkpoint save "Redis approach"

User: Actually, let's try in-memory caching instead

Claude: I'll rewind and implement in-memory caching...
[Uses /checkpoint rewind to undo Redis changes]
[Implements in-memory caching]

User: /checkpoint save "In-memory approach"

User: /checkpoint diff "Redis approach" "In-memory approach"

Claude: Here are the differences between the two approaches...
```

### Example 2: Recovering from Mistakes

```
User: Refactor the authentication module to use JWT

Claude: I'll refactor the authentication module...
[Makes extensive changes]

User: Wait, that broke the OAuth integration. Let's go back.

Claude: I'll rewind to before the refactoring...
/checkpoint rewind "Before auth refactor"

User: Let's try a more conservative approach this time
```

### Example 3: Safe Experimentation

```
User: /checkpoint save "Working state before experiment"

User: Let's try rewriting this in a functional style

Claude: [Makes experimental changes]

User: The tests are failing. Let's rewind.

Claude: /checkpoint rewind "Working state before experiment"
```

### Example 4: Comparing Solutions

```
User: I want to compare two database designs

Claude: I'll create the first design...
[Implements Schema A]

User: /checkpoint save "Schema A"

Claude: /checkpoint rewind to start
[Implements Schema B]

User: /checkpoint save "Schema B"

User: /checkpoint compare "Schema A" "Schema B"

Claude: Here's a comparison of both schemas:
- Schema A uses normalization...
- Schema B uses denormalization...
```

## Checkpoint Management

### View Checkpoint Details

```
User: /checkpoint show 2
```

Output:
```
Checkpoint #2: "Before API refactor"
Created: 2025-11-08 10:45:22
Files modified: 5
- src/api/endpoints.ts
- src/api/middleware.ts
- src/utils/cache.ts
- tests/api.test.ts
- package.json

Message count: 23
Tools used: Read, Edit, Bash
```

### Delete Checkpoints

```
User: /checkpoint delete 1
```

Or delete all:
```
User: /checkpoint clear
```

### Export Checkpoints

Save checkpoint for later use:
```
User: /checkpoint export "Before API refactor" ~/checkpoints/api-refactor.json
```

### Import Checkpoints

Restore from saved checkpoint:
```
User: /checkpoint import ~/checkpoints/api-refactor.json
```

## Advanced Usage

### Branching Strategy

```markdown
Main conversation
├─ Checkpoint 1: "Initial state"
│
├─ Branch A: Redis implementation
│  ├─ Checkpoint 2: "Redis complete"
│  └─ Checkpoint 3: "Redis with clustering"
│
└─ Branch B: In-memory implementation
   ├─ Checkpoint 4: "In-memory complete"
   └─ Checkpoint 5: "In-memory optimized"
```

### Checkpoint Scripts

Create automated checkpoint workflows:

```bash
#!/bin/bash
# create-safe-checkpoint.sh

# Create checkpoint
echo "/checkpoint save \"Safe point - $(date +%Y%m%d-%H%M%S)\"" | claude-code

# Run risky operation
echo "$1" | claude-code

# Check if successful
if [ $? -ne 0 ]; then
  echo "/checkpoint rewind last" | claude-code
  echo "Operation failed, reverted to checkpoint"
fi
```

### Checkpoint Hooks

Automatically create checkpoints on events:

```json
{
  "hooks": {
    "PreToolUse:Edit": "~/.claude/hooks/create-checkpoint.sh",
    "PreCommit": "~/.claude/hooks/checkpoint-before-commit.sh"
  }
}
```

Example hook:
```bash
#!/bin/bash
# ~/.claude/hooks/create-checkpoint.sh

FILE=$1
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Create checkpoint before editing important files
if [[ "$FILE" =~ (config|database|auth|api) ]]; then
  echo "Creating checkpoint before editing $FILE"
  # Trigger checkpoint creation
fi
```

## Best Practices

### When to Create Checkpoints

✅ **Do create checkpoints:**
- Before major refactoring
- Before trying experimental approaches
- Before potentially breaking changes
- At the end of successful feature implementations
- Before switching to a different task

❌ **Don't create checkpoints:**
- After every single change (too granular)
- For trivial changes (typo fixes, formatting)
- Without descriptive names

### Naming Conventions

Good checkpoint names:
- ✅ "Before auth refactor"
- ✅ "Working state - all tests passing"
- ✅ "Pre-deployment v1.2.0"
- ✅ "Schema A - normalized design"

Poor checkpoint names:
- ❌ "checkpoint1"
- ❌ "temp"
- ❌ "test"
- ❌ "backup"

### Checkpoint Hygiene

- **Limit active checkpoints**: Keep 5-10 meaningful checkpoints
- **Delete old checkpoints**: Remove outdated ones regularly
- **Use descriptive names**: Make it easy to identify later
- **Document major checkpoints**: Add notes about what was accomplished

## Configuration

Configure checkpoint behavior in settings. Here's the comprehensive configuration with all available options:

```json
{
  "checkpoints": {
    "autoCheckpoint": true,
    "autoCheckpointInterval": 30,
    "maxCheckpoints": 20,
    "compressionEnabled": true,
    "includeFileContents": true
  }
}
```

### Configuration Options

- `autoCheckpoint`: Enable automatic checkpoints (default: true)
- `autoCheckpointInterval`: Minutes between auto-checkpoints (default: 30)
- `maxCheckpoints`: Maximum number of checkpoints to retain (default: 20)
- `compressionEnabled`: Compress checkpoint data to save space (default: true)
- `includeFileContents`: Include full file contents in checkpoints (default: true)

## Limitations

- Checkpoints are session-specific
- External changes (outside Claude Code) are not tracked
- Large file changes may increase checkpoint size
- Some tool states may not be fully restorable

## Troubleshooting

### Checkpoint Too Large

**Problem**: Checkpoint creation is slow or fails

**Solution**:
```json
{
  "checkpoints": {
    "includeFileContents": false,
    "compressionEnabled": true
  }
}
```

### Missing Checkpoints

**Problem**: Expected checkpoint not found

**Solution**:
- Check if checkpoints were cleared
- Verify checkpoint retention settings
- Check disk space

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

## Example Workflows

### Safe Refactoring Workflow

```
1. /checkpoint save "Before refactoring"
2. Implement refactoring
3. Run tests
4. If tests pass: Commit to git
5. If tests fail: /checkpoint rewind "Before refactoring"
```

### Feature Exploration Workflow

```
1. /checkpoint save "Main branch"
2. Try approach A
3. /checkpoint save "Approach A"
4. /checkpoint rewind "Main branch"
5. Try approach B
6. /checkpoint save "Approach B"
7. /checkpoint compare "Approach A" "Approach B"
8. Choose best approach and commit
```

### Emergency Recovery Workflow

```
1. Notice major issue
2. /checkpoint list
3. Identify last known good state
4. /checkpoint rewind <good-state>
5. Verify system works
6. Proceed cautiously
```

## Related Concepts

- **[Advanced Features](../09-advanced-features/)** - Planning mode and other advanced capabilities
- **[Memory Management](../02-memory/)** - Managing conversation history and context
- **[Slash Commands](../01-slash-commands/)** - User-invoked shortcuts
- **[Hooks](../06-hooks/)** - Event-driven automation
- **[Plugins](../07-plugins/)** - Bundled extension packages

## Summary

Checkpoints are a powerful feature for safe exploration and experimentation in Claude Code. By combining checkpoints with your development workflow, you can:

- Experiment fearlessly with multiple approaches
- Quickly recover from mistakes without losing work
- Compare different solutions side-by-side
- Maintain clean, organized development sessions
- Integrate safely with version control systems

The key to effective checkpoint usage is creating them at meaningful points in your work and using descriptive names that make it easy to find and rewind to the right state when needed.
