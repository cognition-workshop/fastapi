#!/usr/bin/env bash

set -e
set -x

echo "Running security scans..."

echo "=== Bandit Security Scan ==="
bandit -r fastapi -f json -o security-report.json || true
bandit -r fastapi || true

echo "=== Safety Dependency Scan ==="
safety check --json --output safety-report.json || true
safety check || true

echo "=== Pip-Audit Supply Chain Scan ==="
pip-audit --format=json --output=pip-audit-report.json || true
pip-audit || true

echo "Security scans completed."
