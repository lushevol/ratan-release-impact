#!/usr/bin/env zsh

set -euo pipefail

ROOT_DIR="${0:A:h:h}"
REPORT_PATH="${ROOT_DIR}/results/report.html"
LOG_PATH="${ROOT_DIR}/results/log.html"

if [[ ! -f "${REPORT_PATH}" ]]; then
  echo "Report not found at ${REPORT_PATH}. Run scripts/run_ccil.sh first." >&2
  exit 1
fi

if command -v open >/dev/null 2>&1; then
  open "${REPORT_PATH}" "${LOG_PATH}"
  exit 0
fi

if command -v xdg-open >/dev/null 2>&1; then
  xdg-open "${REPORT_PATH}"
  xdg-open "${LOG_PATH}"
  exit 0
fi

echo "No browser opener found. Open these files manually:" >&2
echo "${REPORT_PATH}" >&2
echo "${LOG_PATH}" >&2
exit 1