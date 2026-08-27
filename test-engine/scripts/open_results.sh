#!/usr/bin/env zsh

set -euo pipefail

ROOT_DIR="${0:A:h:h}"
RESULTS_DIR="${ROOT_DIR}/results"

if command -v open >/dev/null 2>&1; then
	open "${RESULTS_DIR}/report.html"
	open "${RESULTS_DIR}/log.html"
	exit 0
fi

if command -v xdg-open >/dev/null 2>&1; then
	xdg-open "${RESULTS_DIR}/report.html"
	xdg-open "${RESULTS_DIR}/log.html"
	exit 0
fi

echo "No supported opener found. Open these files manually:" >&2
echo "${RESULTS_DIR}/report.html" >&2
echo "${RESULTS_DIR}/log.html" >&2
exit 1