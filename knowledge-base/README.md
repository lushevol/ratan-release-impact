# Ratan Settlement OpenKB

This directory is the portable business and design knowledge base for the
release-impact harness. It was migrated from the `Ratan-Settlement` LLM Wiki
project and is now shipped as an [OpenKB](https://github.com/VectifyAI/OpenKB)
knowledge base.

- `raw/` contains the imported source documents.
- `wiki/` contains the compiled, path-citable Markdown pages.
- `.openkb/config.yaml` contains the OpenKB model and language settings.
- `.qmd/index.yml` configures QMD's project-local hybrid search index over the
  compiled wiki. QMD's generated SQLite files stay ignored in that directory.
- LLM Wiki's `.llm-wiki/` indexes, sessions, and desktop state are deliberately
  excluded. They are generated state and are not required by OpenKB.

The imported `.openkb/hashes.json` is intentionally empty because these pages
were compiled by LLM Wiki rather than OpenKB. The compiled pages are available
to the Workbench and MCP immediately. `openkb add` registers and compiles future
or changed source documents in OpenKB's native hash registry.

## CLI

For a complete company-Mac installation, run `scripts/setup.sh` from the
repository root and follow `docs/SETUP_FOR_AI.md`.

Install OpenKB with its web dependencies, then run commands from the repository
root:

```sh
uv tool install 'openkb[web]'
openkb --kb-dir knowledge-base status
openkb --kb-dir knowledge-base list
openkb --kb-dir knowledge-base add path/to/document.md
```

QMD is the preferred retrieval backend for the `openkb_search` MCP tool. Install
it separately and build the project-local index from the knowledge-base directory:

```sh
npm install -g @tobilu/qmd@2.8.3
(cd knowledge-base && qmd update)
(cd knowledge-base && qmd embed)
```

`qmd embed` enables semantic retrieval for hybrid mode; keyword-only retrieval
works after `qmd update`. The MCP server's `openkb_search` defaults to
`backend=auto` and `qmd_mode=hybrid`, then falls back to its built-in local
keyword index if QMD cannot answer. Use `backend=qmd` to require QMD or
`backend=local` to force the fallback. The dedicated `openkb_qmd_query` tool is
QMD-only and defaults to the fast `mode=lex` path; pass `mode=hybrid` when local
model support and query expansion/reranking are available. Set
`OPENKB_SEARCH_BACKEND=qmd` or `OPENKB_SEARCH_BACKEND=local` to change the
default for `openkb_search`. `QMD_BIN` can point to a non-global QMD executable,
and `QMD_COLLECTION` can override the configured collection name (`ratan-wiki`
by default). `QMD_TIMEOUT_SECONDS` bounds each QMD subprocess call (default
30 seconds).

Model-backed `add`, `query`, `chat`, and skill compilation require the provider
credential configured by OpenKB. For the checked-in model, use
`knowledge-base/.env.example` as the template and set `LLM_API_KEY` in the
repository's untracked `.env` file.

Start the optional Workbench with:

```sh
./scripts/openkb-web
```

The default URL is <http://127.0.0.1:7566/>.

## MCP

Project-scoped configuration in `.mcp.json` and `.codex/config.toml` launches
`.claude/tools/openkb-mcp.py` through the existing trace proxy. It exposes:

- `openkb_status` for health and inventory;
- `openkb_search` for credential-free, ranked retrieval through QMD (with a local
  fallback and an explicit backend selector);
- `openkb_qmd_query` for a QMD-only query when the project-local index must be
  used;
- `openkb_read` for exact cited page content;
- `openkb_graph` for resolved `[[wikilink]]` relationships; and
- `openkb_query` for optional model-backed synthesis through the OpenKB CLI.

Restart the MCP client or open a new project session after changing project MCP
configuration. The legacy LLM Wiki desktop application is no longer required.
