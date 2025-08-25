#!/usr/bin/env bash

set -e
set -x

echo "Running performance tests..."

export PYTHONPATH=./docs_src

echo "=== Running API Performance Benchmarks ==="
python tests/performance/api_performance.py

echo "Performance tests completed."
