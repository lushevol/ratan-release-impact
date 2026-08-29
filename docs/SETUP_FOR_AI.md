# Ratan Release Impact: AI Setup Runbook

This is the canonical setup guide for an AI agent or engineer preparing a fresh
company Mac checkout. The repository is an analysis harness. The business
repositories used by GitNexus are separate clones under `repos/` and are not
committed into this repository.

## 1. Prerequisites

Install or make available on `PATH`:

- Git and Xcode Command Line Tools.
- Python 3.10 or newer.
- Node.js 22 or newer. QMD will not install on older Node versions.
- `uv` from <https://docs.astral.sh/uv/>.
- A GitHub/company Git credential that can clone the required private repos.
- Podman Desktop only if local Langfuse tracing is needed.

The MCP search/read/graph path does not require an LLM credential. OpenKB's
model-backed query and the optional Workbench do require one.

## 2. Bootstrap

From the repository root:

```bash
./scripts/setup.sh
```

The script is safe to rerun. It creates `.venv`, installs the pinned Python
requirements, installs OpenKB and GitNexus if absent, installs
`@tobilu/qmd@2.8.3`, and runs `qmd update` against `knowledge-base/wiki`.

Useful variants:

```bash
# Core MCP and QMD only.
./scripts/setup.sh --skip-openkb --skip-test-engine --skip-gitnexus

# Also generate semantic vectors. This downloads/loads local models and may
# take a long time on the first run.
./scripts/setup.sh --embed

# Clone, install each Node/Maven checkout, and build GitNexus indexes.
./scripts/setup.sh --install-repo-deps --index-repos
```

The default setup intentionally builds the lexical QMD index only. This makes
the first setup deterministic and usable without local model downloads.

## 3. Environment and secrets

Never commit credentials. Configure only the services the deployment needs:

```bash
# Optional OpenKB model-backed operations.
cp knowledge-base/.env.example knowledge-base/.env
# Edit knowledge-base/.env and set LLM_API_KEY.

# Optional Langfuse tracing. The local file is ignored by Git.
cp .env.example .env.local
# Edit .env.local with the company's Langfuse values.
```

For local tracing infrastructure, copy `infra/langfuse/.env.example` to
`infra/langfuse/.env`, replace every `CHANGEME` value, then follow
`infra/langfuse/README.md`. Tracing is fail-open; MCP requests still work when
Langfuse is absent or unavailable.

## 4. Private repositories and GitNexus

`repos/manifest.json` is the checked-in inventory of business repositories and
contains the approved Azure DevOps origin URL for each entry. The AI-friendly
command is:

```bash
./scripts/clone-repos.sh --dry-run
./scripts/clone-repos.sh
```

Do not nest repositories deeper or commit them to the harness. Each repository
must be indexed from inside its own directory; the wrapper handles this for
the whole manifest:

```bash
./scripts/install-repo-deps.sh
./scripts/index-repos.sh
```

The project-scoped `gitnexusRepos` MCP filters its registry to these direct
children. Always pass the repository name explicitly when more than one repo is
indexed. The harness root itself has no GitNexus blast-radius index.

## 5. MCP client configuration

`.mcp.json` and `.codex/config.toml` already point to the local trace proxy and
the portable `.venv` paths. After setup, restart Codex/Claude or open a new
project session so the client reloads project MCP configuration.

The OpenKB MCP tools are:

- `openkb_search`: default `backend=auto`; prefers QMD and falls back to local
  keyword retrieval. Use `backend=qmd` to require QMD or `backend=local` to
  force the fallback.
- `openkb_qmd_query`: QMD-only retrieval. It defaults to `mode=lex`, which is
  fast and works immediately after `qmd update`; `mode=hybrid` enables local
  query expansion/reranking when vectors and model runtime support are ready.
- `openkb_read`: read the exact cited `wiki/...` page after searching.
- `openkb_graph`: inspect resolved wiki relationships.
- `openkb_query`: optional model-backed synthesis through OpenKB.

Manual smoke test:

```bash
./.venv/bin/python .claude/tools/openkb-mcp.py --kb-dir knowledge-base <<'EOF'
{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"openkb_status","arguments":{}}}
{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"openkb_qmd_query","arguments":{"query":"rebook payment date","top_k":3,"mode":"lex"}}}
EOF
```

Expect `openkb_status` to report `qmd.ready: true` and the query response to
contain `backend: "qmd"` plus `wiki/...` citations.

## 6. Verification and operations

Run the harness tests:

```bash
./scripts/run-tests.sh
```

Check QMD health and refresh it after wiki changes:

```bash
(cd knowledge-base && qmd status -c ratan-wiki)
(cd knowledge-base && qmd update)
```

The generated `.qmd/index.sqlite*` files are machine-local and ignored. They
must be rebuilt on each new Mac. Vector embedding is optional:

```bash
(cd knowledge-base && qmd embed -c ratan-wiki)
```

The test engine has its own locked environment and setup command:

```bash
test-engine/scripts/setup.sh
test-engine/scripts/run_all.sh
```

## 7. Maintenance commands

Use `./scripts/status.sh` for a complete read-only health report. Individual
commands are available through `python3 scripts/ratan.py` and thin wrappers:

```bash
./scripts/check-dependencies.sh
./scripts/check-mcp.sh
./scripts/kb-add.sh knowledge-base/raw/path/to/new-document.md
./scripts/kb-update.sh knowledge-base/raw/path/to/changed-document.md
./scripts/kb-delete.sh <OpenKB filename-or-unique-identifier>
./scripts/kb-compile.sh
python3 scripts/ratan.py graph build
```

Knowledge-base add/update/delete commands use OpenKB's native raw-document
registry, recompile the wiki, and refresh the local QMD index. Pass `--no-qmd`
only when an index refresh is intentionally deferred. `kb-delete.sh` is
destructive and should only be run for an explicit removal request.

## AI operating rules

1. Read `AGENTS.md` and this file before making changes.
2. Search OpenKB first, then read exact cited pages with `openkb_read` before
   treating business rules as evidence.
3. Query GitNexus with an explicit `repo` under `repos/`; do not invent a root
   harness blast-radius score.
4. Run impact analysis before changing a symbol and run `detect_changes` before
   committing.
5. Keep `.env*`, QMD SQLite state, `repos/`, virtual environments, and test
   outputs out of commits.
6. Treat unsupported business intent as unresolved rather than filling gaps
   from model intuition.

## Troubleshooting

- `qmd: command not found`: confirm Node 22+ and rerun `npm install -g
  @tobilu/qmd@2.8.3`; check that the npm global bin directory is on `PATH`.
- `openkb` is missing: install `uv`, then run `uv tool install 'openkb[web]'`.
- `qmd.ready` is false: run `cd knowledge-base && qmd update` and confirm
  `.qmd/index.yml` and `.qmd/index.sqlite` exist.
- Hybrid QMD is slow or fails during model initialization: use
  `mode=lex`/`qmd_mode=lex` for reliable lexical retrieval, then investigate
  local model/runtime support before enabling vectors.
- GitNexus lists no repositories: clone direct children under `repos/`, run
  `gitnexus analyze` in each one, and restart the MCP client.
