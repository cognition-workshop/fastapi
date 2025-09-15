#!/usr/bin/env bash

set -e
set -x

echo "📦 Installing Quality Framework Tools..."

pip install -r requirements-quality.txt

pre-commit install

echo "✅ Quality framework tools installed successfully."
