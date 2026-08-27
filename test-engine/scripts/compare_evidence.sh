#!/usr/bin/env zsh

set -euo pipefail

ROOT_DIR="${0:A:h:h}"
CHANGE_ID=""
EVIDENCE_ROOT="${ROOT_DIR}/evidence"

while (( $# > 0 )); do
  case "$1" in
    --change-id)
      CHANGE_ID="${2:-}"
      shift 2
      ;;
    --evidence-root)
      EVIDENCE_ROOT="${2:-}"
      shift 2
      ;;
    *)
      echo "Usage: ${0} --change-id ID [--evidence-root DIR]" >&2
      exit 2
      ;;
  esac
done

if [[ -z "${CHANGE_ID}" || ! "${CHANGE_ID}" =~ '^[A-Za-z0-9._-]+$' ]]; then
  echo "--change-id is required and may contain only letters, numbers, dot, underscore, and hyphen." >&2
  exit 2
fi
if [[ ! -x "${ROOT_DIR}/.venv/bin/python" ]]; then
  echo "Test engine is not set up. Run ${ROOT_DIR}/scripts/setup.sh." >&2
  exit 1
fi

CHANGE_DIR="${EVIDENCE_ROOT:A}/${CHANGE_ID}"
exec "${ROOT_DIR}/.venv/bin/python" "${ROOT_DIR}/tools/evidence.py" compare \
  --before "${CHANGE_DIR}/before/run.json" \
  --after "${CHANGE_DIR}/after/run.json" \
  --output "${CHANGE_DIR}/comparison.json" \
  --markdown-output "${CHANGE_DIR}/impact-fragment.md"
