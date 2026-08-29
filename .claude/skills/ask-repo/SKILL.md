---
name: ask-repo
description: "Operate the Ratan release-impact harness from natural-language requests: set it up, validate dependencies and MCP servers, clone or re-index manifest repositories, maintain the OpenKB raw/wiki lifecycle, run tests, and rebuild the SDLC graph."
---

# Ask Repo

Use this skill when a user asks to set up, check, maintain, or regenerate this
repository. Work from the repository root and read `AGENTS.md` first. Prefer
the checked-in scripts over ad-hoc commands so results are repeatable.

## Route requests

| User intent | Command |
| --- | --- |
| Set up harness and attempt all repo clones | `./scripts/setup.sh`, then `./scripts/status.sh` |
| Set up including repo dependencies and indexes | `./scripts/setup.sh --install-repo-deps --index-repos` |
| Check toolchain/dependencies | `./scripts/check-dependencies.sh` |
| Check MCP servers | `./scripts/check-mcp.sh` |
| Show complete project status | `./scripts/status.sh` |
| Clone missing business repos | `./scripts/clone-repos.sh` |
| Preview clone actions | `./scripts/clone-repos.sh --dry-run` |
| Re-index business repos | `./scripts/index-repos.sh` |
| Install Node/Maven repo dependencies | `./scripts/install-repo-deps.sh` |
| Re-index with PDG | `./scripts/index-repos.sh --pdg` |
| Add a raw knowledge document | `./scripts/kb-add.sh knowledge-base/raw/<file>` |
| Update a raw knowledge document | `./scripts/kb-update.sh knowledge-base/raw/<file>` |
| Delete a knowledge document | `./scripts/kb-delete.sh <OpenKB identifier>` |
| Recompile wiki and refresh QMD | `./scripts/kb-compile.sh` |
| Build the SDLC graph | `python3 scripts/ratan.py graph build` |
| Run harness tests | `./scripts/run-tests.sh` |

The underlying CLI is `python3 scripts/ratan.py`; use `--json` on an individual
`deps`, `kb status`, `repos status`, or `mcp status` command when another tool
needs machine-readable output. `repos/manifest.json`
is the source of truth for repository names, approved Azure DevOps remotes, and
paths. Cloning requires the user's Azure DevOps credential; setup always tries
all manifest entries and skips only repositories that are already cloned.

## Operating rules

1. Report missing prerequisites and the exact remediation; do not silently
   skip a required dependency.
2. Never expose or commit credentials. Keep `.env*`, virtual environments,
   QMD databases, repository clones, and GitNexus indexes local.
3. Treat `kb delete` as destructive: run it only when the user explicitly asks
   to remove a document, and show the identifier being removed.
4. After changing `knowledge-base/raw`, run the OpenKB compile path and refresh
   QMD. Use `--no-qmd` only when the user explicitly wants a deferred index.
5. After repository changes, run `repos index` and then `repos status`; no
   GitNexus blast-radius score exists for the harness root itself.
6. For business requirements, use the project OpenKB/GitNexus/SDLC Graph
   workflows and their evidence rules instead of treating this operational
   router as business authority.
