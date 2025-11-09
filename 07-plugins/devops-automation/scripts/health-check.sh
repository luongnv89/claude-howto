#!/bin/bash

echo "🏥 System Health Check"
echo "===================="

ENV=${1:-production}

# Check API
echo -n "API: "
if curl -sf http://api.$ENV.example.com/health > /dev/null; then
  echo "✅ Healthy"
else
  echo "❌ Unhealthy"
fi

# Check Database
echo -n "Database: "
if pg_isready -h db.$ENV.example.com > /dev/null 2>&1; then
  echo "✅ Healthy"
else
  echo "❌ Unhealthy"
fi

# Check Pods
echo -n "Kubernetes Pods: "
PODS_READY=$(kubectl get pods -n $ENV --no-headers | grep "Running" | wc -l)
PODS_TOTAL=$(kubectl get pods -n $ENV --no-headers | wc -l)
echo "$PODS_READY/$PODS_TOTAL ready"

echo "===================="
