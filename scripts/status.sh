#!/usr/bin/env sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
json_flag=
for argument in "$@"; do
  case "$argument" in
    --json) json_flag=--json ;;
    *) printf 'status: unsupported option: %s\n' "$argument" >&2; exit 2 ;;
  esac
done
printf '%s\n' '== dependencies =='
python3 "$root/scripts/ratan.py" deps $json_flag
printf '%s\n' '== knowledge base =='
python3 "$root/scripts/ratan.py" kb status $json_flag
printf '%s\n' '== repositories =='
python3 "$root/scripts/ratan.py" repos status $json_flag
printf '%s\n' '== MCP =='
python3 "$root/scripts/ratan.py" mcp status $json_flag
