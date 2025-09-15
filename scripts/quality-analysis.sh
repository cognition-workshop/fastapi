#!/usr/bin/env bash

set -e
set -x

echo "📊 Running Code Quality Analysis..."

echo "Analyzing code complexity with radon..."
radon cc fastapi/ --json > complexity-report.json
radon cc fastapi/ --show-complexity --min B

echo "Checking complexity thresholds with xenon..."
xenon --max-absolute B --max-modules A --max-average A fastapi/

echo "Detecting dead code with vulture..."
vulture fastapi/ --json > deadcode-report.json || true
vulture fastapi/ --min-confidence 80

echo "Checking documentation coverage..."
interrogate fastapi/ --generate-badge interrogate_badge.svg
interrogate fastapi/ --verbose --fail-under 80

echo "✅ Quality analysis completed. Reports generated."
