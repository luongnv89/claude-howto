#!/usr/bin/env node

/**
 * Pre-deployment hook
 * Validates environment and prerequisites before deployment
 */

async function preDeploy() {
  console.log('Running pre-deployment checks...');

  const { execSync } = require('child_process');

  // Check if kubectl is installed
  try {
    execSync('which kubectl', { stdio: 'pipe' });
  } catch (error) {
    console.error('❌ kubectl not found. Please install Kubernetes CLI.');
    process.exit(1);
  }

  // Check if connected to cluster
  try {
    execSync('kubectl cluster-info', { stdio: 'pipe' });
  } catch (error) {
    console.error('❌ Not connected to Kubernetes cluster');
    process.exit(1);
  }

  console.log('✅ Pre-deployment checks passed');
}

preDeploy().catch(error => {
  console.error('Pre-deploy hook failed:', error);
  process.exit(1);
});
