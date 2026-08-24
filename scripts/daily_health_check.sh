#!/bin/bash
# Runs a headless Claude health check and saves JSON output

claude -p "List all exported functions in src/ and count how many have type hints" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"total":{"type":"integer"},"typed":{"type":"integer"}},"required":["total","typed"]}' \
  | jq '.structured_output' > health_report.json

echo "Health report saved to health_report.json"