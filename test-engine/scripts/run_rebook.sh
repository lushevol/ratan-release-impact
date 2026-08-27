#!/usr/bin/env zsh

set -euo pipefail

ROOT_DIR="${0:A:h:h}"
exec "${ROOT_DIR}/scripts/run_domain.sh" rebook "$@"