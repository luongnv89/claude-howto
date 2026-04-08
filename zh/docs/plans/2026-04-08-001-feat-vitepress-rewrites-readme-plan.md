---
title: feat: Use VitePress Rewrites to Keep README.md Files Unchanged
type: feat
status: active
date: 2026-04-08
---

# feat: Use VitePress Rewrites to Keep README.md Files Unchanged

## Overview

Configure VitePress `rewrites` option to map `README.md` files to `index.md` routes, preserving the original file structure and minimizing git changes. This eliminates the need to rename files from `README.md` to `index.md`.

## Problem Statement / Motivation

### Current Issue

The current implementation manually renamed all module `README.md` files to `index.md`:
- Git status shows deletions (`D`) for original README.md files
- Git status shows additions (`??`) for new index.md files
- This disrupts the original repository structure
- Creates unnecessary diff noise when syncing with parent repo

### Why This Matters

1. **Minimal content impact**: Keep original files unchanged for easier maintenance
2. **Parent repo alignment**: The parent repo uses `README.md` as module index files
3. **Git history preservation**: Avoid showing deleted/added files in git status
4. **Convention consistency**: README.md is the standard documentation convention

## Proposed Solution

Use VitePress's `rewrites` configuration to map `README.md` source files to `index.md` output routes without renaming the actual files.

### VitePress Rewrites Documentation

From [VitePress Routing Guide](https://vitepress.dev/guide/routing):

```typescript
// Function-based rewrites (most flexible)
export default {
  rewrites(id) {
    return id.replace(/^packages\/([^/]+)\/src\//, '$1/')
  }
}
```

### Implementation Approach

Add a rewrites function to `.vitepress/config.ts` that:
1. Matches numbered module directories (01-10 pattern)
2. Converts `README.md` to `index.md` route output
3. Preserves original source file names

## Technical Considerations

### Architecture Impacts

- **VitePress build process**: The rewrites happen during build, generating correct routes
- **Output structure unchanged**: The dist folder still has `index.html` for each directory
- **Sidebar links**: Can use trailing slashes (`/01-slash-commands/`) or explicit `index`

### Pattern Matching

The regex pattern should match:
- Root level README.md files (INDEX.md → index.md)
- Module directory README.md files (01-slash-commands/README.md → 01-slash-commands/index.md)
- Any subdirectory README.md files (07-plugins/pr-review/README.md → 07-plugins/pr-review/index.md)

### Files to Restore

Current git status shows deleted README.md files that need to be restored:

| Directory | Current (index.md) | Should Be (README.md) |
|-----------|--------------------|-----------------------|
| root | index.md | README.md or INDEX.md |
| 01-slash-commands | index.md | README.md |
| 02-memory | index.md | README.md |
| 03-skills | index.md | README.md |
| 04-subagents | index.md | README.md |
| 05-mcp | index.md | README.md |
| 06-hooks | index.md | README.md |
| 07-plugins | index.md | README.md |
| 08-checkpoints | index.md | README.md |
| 09-advanced-features | index.md | README.md |
| 10-cli | index.md | README.md |

## Acceptance Criteria

- [ ] Add `rewrites` configuration to `.vitepress/config.ts`
- [ ] Restore original `README.md` files from parent repo or rename `index.md` back
- [ ] Delete the manually created `index.md` files (or rename them back)
- [ ] Verify build produces correct routes (`/01-slash-commands/` works)
- [ ] Verify sidebar navigation works correctly
- [ ] Docker build succeeds with new configuration
- [ ] Git status shows minimal changes (no deleted/added file pairs)

## MVP Implementation

### Step 1: Update VitePress Config

```typescript
// .vitepress/config.ts
export default defineConfig({
  title: 'Claude How To',
  description: '用一个周末掌握 Claude Code',
  lang: 'zh-CN',

  // Add rewrites configuration
  rewrites(id) {
    // Match README.md in any directory and map to index.md route
    // Handles: README.md, XX-module/README.md, XX-module/subdir/README.md
    if (id.endsWith('README.md') || id.endsWith('INDEX.md')) {
      return id.replace(/README\.md$/, 'index.md').replace(/INDEX\.md$/, 'index.md')
    }
    return id
  },

  // ... rest of config
})
```

### Step 2: Restore Original Files

```bash
# Option A: Rename index.md back to README.md
cd /app/sandbox/claude-howto/zh

# Root level
mv index.md README.md

# Module directories
for dir in 01-slash-commands 02-memory 03-skills 04-subagents 05-mcp 06-hooks 07-plugins 08-checkpoints 09-advanced-features 10-cli; do
  mv ${dir}/index.md ${dir}/README.md
done

# Plugin subdirectories
mv 07-plugins/pr-review/index.md 07-plugins/pr-review/README.md
mv 07-plugins/devops-automation/index.md 07-plugins/devops-automation/README.md
mv 07-plugins/documentation/index.md 07-plugins/documentation/README.md
```

### Step 3: Update Sidebar Links (Optional)

Sidebar can use trailing slashes for cleaner URLs:

```typescript
// Current (works)
{ text: '概述', link: '/01-slash-commands/index' }

// Alternative (also works with trailing slash)
{ text: '概述', link: '/01-slash-commands/' }
```

### Step 4: Verify Build

```bash
npm run docs:build
ls .vitepress/dist/01-slash-commands/index.html  # Should exist
```

## Sources & References

- **VitePress Routing**: https://vitepress.dev/guide/routing#route-rewrites
- **VitePress Rewrites Config**: https://vitepress.dev/reference/site-config#rewrites
- **Sidebar Links**: https://vitepress.dev/reference/default-theme-sidebar
- **Parent repo**: https://github.com/luongnv89/claude-howto (uses README.md convention)