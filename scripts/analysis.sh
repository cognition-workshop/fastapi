#!/usr/bin/env bash

set -e
set -x

echo "Running advanced static analysis..."

echo "=== Code Complexity Analysis ==="
radon cc fastapi --json > complexity-report.json || true
radon cc fastapi || true

echo "=== Maintainability Index ==="
radon mi fastapi --json > maintainability-report.json || true
radon mi fastapi || true

echo "=== Dead Code Detection ==="
vulture fastapi --json > vulture-report.json || true
vulture fastapi || true

echo "Advanced static analysis completed."
