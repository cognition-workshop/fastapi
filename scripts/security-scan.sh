#!/usr/bin/env bash

set -e
set -x

echo "🔒 Running Security Scans..."

echo "Running bandit security scan..."
bandit -r fastapi/ -f json -o security-report.json || true
bandit -r fastapi/ -f txt --severity-level medium || true

echo "Checking dependency vulnerabilities..."
safety check > safety-report.txt || true
safety check

echo "Running semgrep security analysis..."
semgrep --config=auto fastapi/ --json --output=semgrep-report.json || true
semgrep --config=auto fastapi/

echo "✅ Security scans completed. Reports generated."
