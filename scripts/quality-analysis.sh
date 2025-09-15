#!/usr/bin/env bash

set -x

echo "📊 Running Code Quality Analysis..."

echo "Analyzing code complexity with radon..."
radon cc fastapi/ --json > complexity-report.json
radon cc fastapi/ --show-complexity --min B

echo "Checking complexity thresholds with xenon..."
xenon --max-absolute B --max-modules A --max-average A fastapi/ || true

echo "Detecting dead code with vulture..."
vulture fastapi/ --min-confidence 80 > deadcode-report.txt || true
vulture fastapi/ --min-confidence 80

echo "Checking documentation coverage..."
interrogate fastapi/ --generate-badge interrogate_badge.svg || true
interrogate fastapi/ --verbose --fail-under 15 || true

echo "✅ Quality analysis completed. Reports generated."
