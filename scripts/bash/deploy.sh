#!/bin/bash

ORG=$1

if [ -z "$ORG" ]; then
  echo "Usage: ./deploy.sh <OrgAlias>"
  exit 1
fi

echo "Validating deployment..."
sf project deploy start --dry-run --target-org $ORG || exit 1

echo "Deploying to $ORG..."
sf project deploy start --target-org $ORG
