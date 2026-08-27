#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
NODE_BIN="${NODE_BIN:-node}"
NPM_BIN="${NPM_BIN:-npm}"
QMD_VERSION="${QMD_VERSION:-2.8.3}"
INSTALL_OPENKB=1
INSTALL_TEST_ENGINE=1
INSTALL_GITNEXUS=1
EMBED_QMD=0

usage() {
  cat <<'EOF'
Usage: scripts/setup.sh [options]

Creates the root Python environment, installs the local MCP dependencies,
installs QMD and GitNexus when needed, and rebuilds the project-local QMD index.

Options:
  --skip-openkb       Do not install the optional OpenKB CLI/workbench.
  --skip-test-engine  Do not create test-engine/.venv.
  --skip-gitnexus     Do not install the GitNexus CLI.
  --embed             Attempt QMD vector embedding after lexical indexing.
  -h, --help          Show this help.
EOF
}

die() {
  printf 'setup: %s\n' "$1" >&2
  exit 1
}

has_command() {
  command -v "$1" >/dev/null 2>&1
}

require_command() {
  if ! has_command "$1"; then
    die "missing '$1'. See SETUP_FOR_AI.md for the company-Mac prerequisites."
  fi
}

while (( $# > 0 )); do
  case "$1" in
    --skip-openkb)
      INSTALL_OPENKB=0
      shift
      ;;
    --skip-test-engine)
      INSTALL_TEST_ENGINE=0
      shift
      ;;
    --skip-gitnexus)
      INSTALL_GITNEXUS=0
      shift
      ;;
    --embed)
      EMBED_QMD=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      die "unknown option: $1"
      ;;
  esac
done

require_command git
require_command "$PYTHON_BIN"
require_command "$NODE_BIN"
require_command "$NPM_BIN"

"$PYTHON_BIN" - <<'PY'
import sys

if sys.version_info < (3, 10):
    raise SystemExit("Python 3.10 or newer is required")
PY

"$NODE_BIN" -e '
const major = Number(process.versions.node.split(".")[0]);
if (major < 22) {
  console.error("Node.js 22 or newer is required by QMD");
  process.exit(1);
}
'

if (( INSTALL_OPENKB == 1 || INSTALL_TEST_ENGINE == 1 )) && ! has_command uv; then
  die "missing 'uv'. Install it from https://docs.astral.sh/uv/ and rerun setup."
fi

ROOT_VENV="${ROOT_DIR}/.venv"
if [[ ! -x "${ROOT_VENV}/bin/python" ]]; then
  printf 'Creating %s\n' "${ROOT_VENV}"
  "$PYTHON_BIN" -m venv "$ROOT_VENV"
fi
"${ROOT_VENV}/bin/python" -m pip install --requirement "${ROOT_DIR}/requirements.txt"

if (( INSTALL_OPENKB == 1 )); then
  if has_command openkb; then
    printf 'OpenKB already available: '
    openkb --version || true
  else
    uv tool install 'openkb[web]'
  fi
fi

if ! has_command qmd || ! qmd --version 2>/dev/null | grep -Fq "qmd ${QMD_VERSION}"; then
  "$NPM_BIN" install --global "@tobilu/qmd@${QMD_VERSION}"
fi
require_command qmd

if (( INSTALL_GITNEXUS == 1 )); then
  if has_command gitnexus; then
    printf 'GitNexus already available: '
    gitnexus --version || true
  else
    "$NPM_BIN" install --global gitnexus
  fi
fi

printf 'Updating QMD lexical index\n'
( cd "${ROOT_DIR}/knowledge-base" && qmd update )
if (( EMBED_QMD == 1 )); then
  printf 'Generating QMD vectors\n'
  ( cd "${ROOT_DIR}/knowledge-base" && qmd embed -c ratan-wiki )
fi

if (( INSTALL_TEST_ENGINE == 1 )); then
  "${ROOT_DIR}/test-engine/scripts/setup.sh"
fi

printf '\nSetup verification\n'
printf '%s\n' "- QMD: $(qmd --version)"
if has_command openkb; then
  printf '%s\n' "- OpenKB: $(openkb --version 2>/dev/null || printf 'available')"
else
  printf '%s\n' '- OpenKB: not installed (optional; use --skip-openkb only for core MCP/QMD setup)'
fi
if has_command gitnexus; then
  printf '%s\n' "- GitNexus: $(gitnexus --version 2>/dev/null || printf 'available')"
else
  printf '%s\n' '- GitNexus: not installed (optional until repos/ are cloned)'
fi
printf '%s\n' '- MCP: run .venv/bin/python .claude/tools/openkb-mcp.py --kb-dir knowledge-base'
printf '%s\n' '- Next: read SETUP_FOR_AI.md for environment, private-repository, and MCP-client setup.'
