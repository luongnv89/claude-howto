#!/bin/bash
set -e

echo "⏪ Starting rollback..."

ENV=${1:-staging}
echo "📦 Target environment: $ENV"

# Get previous deployment
PREVIOUS=$(kubectl rollout history deployment/app -n $ENV | tail -2 | head -1 | awk '{print $1}')
echo "🔄 Rolling back to revision: $PREVIOUS"

# Execute rollback
kubectl rollout undo deployment/app -n $ENV

# Wait for rollback
echo "⏳ Waiting for rollback to complete..."
kubectl rollout status deployment/app -n $ENV

# Health check
echo "🏥 Running health checks..."
sleep 5
curl -f http://api.$ENV.example.com/health

echo "✅ Rollback complete!"
