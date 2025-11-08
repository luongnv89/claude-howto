---
name: Commit and push everything
description: Stage all changes, create commit, and push to remote (use with caution)
tags: git, workflow, automation
---

# Commit and Push Everything

⚠️ **CAUTION**: This command will stage ALL changes, commit them, and push to the remote repository. Use only when you're confident all changes should be committed together.

## Pre-flight Safety Checks

Before proceeding, I will verify:

1. **Current Status**
   - Run `git status` to see what will be committed
   - Ensure no unwanted files are included
   - Verify you're on the correct branch

2. **Review Changes**
   - Run `git diff --stat` to see change statistics
   - Confirm all changes are intentional
   - Check for any uncommitted work

3. **Security Checks**
   - ❌ No secrets or credentials in changes
   - ❌ No API keys, passwords, or tokens
   - ❌ No `.env` files or private keys
   - ✅ `.gitignore` properly configured
   - ✅ No large binary files without Git LFS
   - ✅ No build artifacts (node_modules, dist, __pycache__)

## Workflow Steps

### Step 1: Show Current Status

Run `git status` and display:
- Modified files
- Added files
- Deleted files
- Untracked files

### Step 2: Show Change Statistics

Run `git diff --stat` to show:
- Number of files changed
- Total insertions
- Total deletions

### Step 3: Safety Verification

⚠️ **STOP if any of these are detected:**

```bash
# Sensitive files:
.env
.env.local
*.key
*.pem
credentials.json
secrets.yaml
config/database.yml (with passwords)
*.p12
*.pfx
id_rsa
*.cer

# Large files (>10MB)
*.mp4, *.mov, *.zip, *.tar.gz

# Build artifacts:
node_modules/
dist/
build/
__pycache__/
*.pyc
.DS_Store
thumbs.db
*.swp
```

If any detected, **WARN USER** and ask for confirmation.

### Step 4: Request Confirmation

Present summary and ask:

```
📊 Changes Summary:
- X files modified
- Y files added
- Z files deleted
- Total: +AAA insertions, -BBB deletions

⚠️ I will now:
1. Stage all changes (git add .)
2. Create a descriptive commit
3. Push to remote repository

Current branch: [branch-name]
Remote: [remote-url]

🔒 Safety checks:
✅ No secrets detected
✅ No large files
✅ .gitignore configured
⚠️ [Any warnings]

Type 'yes' to proceed or 'no' to cancel.
```

**WAIT for explicit user confirmation before proceeding.**

### Step 5: Stage All Changes (After Confirmation)

Execute:
```bash
git add .
```

Verify staging:
```bash
git status
```

### Step 6: Generate Commit Message

Analyze the changes and create a descriptive conventional commit message:

**Format:**
```
[type]: Brief summary (max 72 characters)

Detailed description of changes:
- Key change 1
- Key change 2
- Key change 3
```

**Commit Types:**
- `feat`: New feature or enhancement
- `fix`: Bug fix
- `docs`: Documentation changes only
- `style`: Code formatting, missing semicolons, etc.
- `refactor`: Code restructuring without behavior change
- `test`: Adding or updating tests
- `chore`: Maintenance, dependencies, config
- `perf`: Performance improvements
- `build`: Build system or external dependencies
- `ci`: CI/CD configuration changes

**Examples:**
```
feat: Add user authentication with JWT tokens

- Implement login and registration endpoints
- Add JWT token generation and validation
- Create authentication middleware
- Add comprehensive auth tests
```

```
docs: Update all concept README files with comprehensive documentation

Extract and consolidate information from guide into individual folders
- Add architecture diagrams and tables
- Include practical examples
- Expand best practices sections
```

### Step 7: Create Commit

Execute:
```bash
git commit -m "$(cat <<'EOF'
[Generated commit message]
EOF
)"
```

Show commit hash and message.

### Step 8: Push to Remote

Execute:
```bash
git push
```

If push fails, try:
```bash
git pull --rebase origin [branch-name]
git push
```

### Step 9: Verify Success

Show:
```bash
git log -1 --oneline --decorate
```

Confirm:
```
✅ Successfully pushed to remote!

Commit: [hash] [message]
Branch: [branch] → origin/[branch]
Files changed: X
```

## Safety Guidelines

### ❌ DO NOT Proceed If:

- **Secrets detected**: API keys, passwords, tokens, certificates
- **Sensitive data**: Database dumps, user data, PII
- **Large files**: Files >10MB without Git LFS
- **Build artifacts**: node_modules, dist, __pycache__, .venv
- **Temporary files**: .DS_Store, *.swp, *.tmp, thumbs.db
- **User hasn't confirmed**: Always wait for explicit "yes"
- **Protected branch**: main/master without proper review process
- **Merge conflicts**: Unresolved conflicts exist
- **Failing tests**: Pre-commit hooks or CI failing

### ✅ Good Use Cases:

- Documentation updates across multiple files
- Feature implementation with tests and docs
- Bug fixes with related test updates
- Configuration and setup changes
- Refactoring with comprehensive changes
- Project-wide formatting or linting fixes
- End-of-day commit of working feature

### ⚠️ Warning Signs - Ask User First:

```
Modified: .env
Modified: config/secrets.yml
Added: private_key.pem
Added: node_modules/ (1,234 files)
Warning: Large file detected: video.mp4 (45MB)
Warning: On protected branch: main
Warning: Pre-commit hook failed
```

## Error Handling

### If `git add .` fails:
1. Check file permissions
2. Look for locked files
3. Verify repository is initialized
4. Run `git status` for diagnostics

### If `git commit` fails:
1. **Pre-commit hooks failed**: Fix issues and retry
2. **No changes to commit**: Already up to date
3. **Invalid commit message**: Adjust format
4. **Git config missing**: Set user.name and user.email

### If `git push` fails:
1. **Rejected (non-fast-forward)**:
   ```bash
   git pull --rebase
   git push
   ```

2. **Permission denied**: Check credentials and access

3. **Remote branch doesn't exist**:
   ```bash
   git push -u origin [branch-name]
   ```

4. **Protected branch**: Use pull request workflow

## Alternative Workflows

If user wants more control, suggest:

**Option 1: Selective Staging**
```
Would you like to:
1. Select specific files to commit?
2. Review each file individually?
3. Create multiple commits by category?
```

**Option 2: Interactive Staging**
```
Use `git add -p` for interactive patch selection?
This lets you review each change before staging.
```

**Option 3: Pull Request Flow**
```
Instead of direct push, would you like to:
1. Create a feature branch
2. Push to branch
3. Create pull request
Use the /pr command for this workflow.
```

## Post-Push Actions

After successful push:

### 1. Verify on Remote
- Check GitHub/GitLab/Bitbucket web interface
- Confirm commit appears correctly
- Review diff on remote

### 2. CI/CD Pipeline (if applicable)
- Confirm pipeline started
- Monitor build status
- Check for any failures

### 3. Team Notification (if applicable)
- Notify in Slack/Teams channel
- Update issue tracker (close/link issues)
- Tag reviewers for PR

### 4. Local Cleanup
```bash
# Verify everything is clean
git status

# Should show:
# On branch [name]
# Your branch is up to date with 'origin/[name]'.
# nothing to commit, working tree clean
```

## Example Interaction

**User**: `/push-all`

**Assistant**:
```
🔍 Analyzing repository status...

📊 Current Status:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Modified files (9):
  ✏️  01-slash-commands/README.md
  ✏️  02-subagents/README.md
  ✏️  03-memory/README.md
  ✏️  04-mcp/README.md
  ✏️  05-skills/README.md
  ✏️  06-plugins/README.md
  ✏️  07-hooks/README.md
  ✏️  08-checkpoints/README.md
  ✏️  09-advanced-features/README.md

📈 Change Statistics:
  9 files changed
  +3,706 insertions
  -587 deletions

🔒 Safety Checks:
  ✅ No secrets detected
  ✅ No large files (>10MB)
  ✅ .gitignore properly configured
  ✅ No build artifacts
  ✅ No temporary files

🌿 Branch Information:
  Current: main
  Remote: origin/main
  Status: Up to date (can fast-forward)

📝 Proposed commit message:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
docs: Update all concept README files with comprehensive documentation

Extract and consolidate information from guide into individual folders:
- Add architecture diagrams, tables, and flowcharts
- Include practical code examples and templates
- Expand best practices and troubleshooting sections
- Provide installation instructions for all concepts

Total: +3,706 lines of comprehensive documentation

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  I will now:
  1. Stage all changes (git add .)
  2. Commit with the message above
  3. Push to origin/main

⚠️  This affects 9 files. Please confirm.

Type 'yes' to proceed, 'no' to cancel, or 'review' to see diffs.
```

**User**: `yes`

**Assistant**:
```
✅ Staging all changes...
   git add .

✅ Creating commit...
   git commit -m "docs: Update all concept README files..."

✅ Pushing to remote...
   git push origin main

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 Successfully pushed to remote!

Commit: 41527ae docs: Update all concept README files...
Branch: main → origin/main
Files: 9 changed (+3,706, -587)
Remote: https://github.com/user/repo

✅ All changes have been successfully pushed!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Quick Reference Card

**What this command does:**
1. ✅ Checks git status and shows changes
2. ✅ Displays change statistics
3. ✅ Performs comprehensive safety checks
4. ⚠️ Requests explicit user confirmation
5. ✅ Stages all changes with `git add .`
6. ✅ Generates descriptive conventional commit
7. ✅ Creates commit with proper message
8. ✅ Pushes to remote repository
9. ✅ Verifies and confirms success

**When to use:**
- ✅ Coordinated multi-file documentation updates
- ✅ Feature implementation with tests and docs
- ✅ Bug fixes affecting multiple files
- ✅ Project-wide refactoring or formatting
- ✅ End-of-day commits of working features
- ✅ Configuration and setup changes

**When NOT to use:**
- ❌ Uncertain about what's being committed
- ❌ Contains sensitive data or secrets
- ❌ On protected branches (main/master) without review
- ❌ Merge conflicts are present
- ❌ Want granular commit history for different changes
- ❌ Pre-commit hooks are failing
- ❌ Want to review each change individually

## Related Commands

- **`/pr`** - Full pull request preparation with checklist
- **`/optimize`** - Code optimization before committing
- **Individual git commands** - For more granular control

## Best Practices

1. **Use descriptive branch names**: `feature/auth`, `fix/login-bug`
2. **Commit related changes together**: Don't mix features and fixes
3. **Review before pushing**: Always check `git diff`
4. **Pull before push**: Avoid conflicts with `git pull --rebase`
5. **Use conventional commits**: Helps with changelog generation
6. **Test before commit**: Run tests to catch issues early
7. **Keep commits atomic**: One logical change per commit when possible
8. **Write clear messages**: Future you will thank present you

---

**⚠️ Remember**: With great automation comes great responsibility. Always review your changes before pushing! When in doubt, use individual git commands for more control.
