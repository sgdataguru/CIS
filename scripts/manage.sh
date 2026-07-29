#!/usr/bin/env bash
set -euo pipefail

case "${1:-}" in
  start) docker compose up --build ;;
  stop) docker compose down ;;
  test) pytest ;;
  lint) ruff check . ;;
  *) echo "Usage: $0 {start|stop|test|lint}"; exit 1 ;;
esac
