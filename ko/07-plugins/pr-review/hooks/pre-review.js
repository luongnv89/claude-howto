#!/usr/bin/env node

/**
 * Pre-review hook
 * Runs before starting PR review to ensure prerequisites are met
 */

async function preReview() {
  console.log('Running pre-review checks...');

  // Check if git repository
  const { execSync } = require('child_process');
  try {
    execSync('git rev-parse --git-dir', { stdio: 'pipe' });
  } catch (error) {
    console.error('❌ Not a git repository');
    process.exit(1);
  }

  // Check for uncommitted changes
  try {
    const status = execSync('git status --porcelain', { encoding: 'utf-8' });
    if (status.trim()) {
      console.warn('⚠️  Warning: Uncommitted changes detected');
    }
  } catch (error) {
    console.error('❌ Failed to check git status');
    process.exit(1);
  }

  console.log('✅ Pre-review checks passed');
}

preReview().catch(error => {
  console.error('Pre-review hook failed:', error);
  process.exit(1);
});
