#!/bin/bash
set -e

echo "🚀 Starting deployment..."

# Load environment
ENV=${1:-staging}
echo "📦 Target environment: $ENV"

# Pre-deployment checks
echo "✓ Running pre-deployment checks..."
npm run lint
npm test

# Build
echo "🔨 Building application..."
npm run build

# Deploy
echo "🚢 Deploying to $ENV..."
kubectl apply -f k8s/$ENV/

# Health check
echo "🏥 Running health checks..."
sleep 10
curl -f http://api.$ENV.example.com/health

echo "✅ Deployment complete!"
