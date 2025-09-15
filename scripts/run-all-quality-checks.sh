#!/usr/bin/env bash

set -e
set -x

echo "🚀 Running Complete Quality Framework..."

echo "Installing quality framework tools..."
pip install -r requirements-quality.txt

echo "Running existing quality checks..."
bash scripts/lint.sh
bash scripts/test.sh

echo "Running security scans..."
bash scripts/security-scan.sh

echo "Running quality analysis..."
bash scripts/quality-analysis.sh

echo "Generating quality report..."
python scripts/generate-quality-report.py

echo "✅ Complete quality framework execution finished!"
echo "📊 Reports generated:"
echo "  - quality-framework-report.json"
echo "  - QUALITY_FRAMEWORK_REPORT.md"
echo "  - security-report.json"
echo "  - complexity-report.json"
echo "  - deadcode-report.json"
