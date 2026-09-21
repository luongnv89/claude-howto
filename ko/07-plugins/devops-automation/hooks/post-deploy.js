#!/usr/bin/env node

/**
 * Post-deployment hook
 * Runs after deployment completes
 */

async function postDeploy() {
  console.log('Running post-deployment tasks...');

  const { execSync } = require('child_process');

  // Wait for pods to be ready
  console.log('Waiting for pods to be ready...');
  try {
    execSync('kubectl wait --for=condition=ready pod -l app=myapp --timeout=300s', {
      stdio: 'inherit'
    });
  } catch (error) {
    console.error('❌ Pods failed to become ready');
    process.exit(1);
  }

  // Run smoke tests
  console.log('Running smoke tests...');
  // Add your smoke test commands here

  console.log('✅ Post-deployment tasks complete');
}

postDeploy().catch(error => {
  console.error('Post-deploy hook failed:', error);
  process.exit(1);
});
