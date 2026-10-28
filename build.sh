#!/bin/bash
set -e

rm -f bot.zip

zip -r bot.zip . \
  --exclude "*.git*" \
  --exclude "*__pycache__*" \
  --exclude "*.pyc" \
  --exclude "*.pyo" \
  --exclude "*/.pytest_cache/*" \
  --exclude "*.venv/*" \
  --exclude "*/venv/*" \
  --exclude "*/env/*" \
  --exclude "*/Lib/*" \
  --exclude "*/Scripts/*" \
  --exclude "bot.zip"
