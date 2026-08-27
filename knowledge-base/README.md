# Ratan Settlement OpenKB

This directory is the portable business and design knowledge base for the
release-impact harness. It was migrated from the `Ratan-Settlement` LLM Wiki
project and is now shipped as an [OpenKB](https://github.com/VectifyAI/OpenKB)
knowledge base.

- `raw/` contains the imported source documents.
- `wiki/` contains the compiled, path-citable Markdown pages.
- `.openkb/config.yaml` contains the OpenKB model and language settings.
- LLM Wiki's `.llm-wiki/` indexes, sessions, and desktop state are deliberately
  excluded. They are generated state and are not required by OpenKB.

The imported `.openkb/hashes.json` is intentionally empty because these pages
were compiled by LLM Wiki rather than OpenKB. The compiled pages are available
to the Workbench and MCP immediately. `openkb add` registers and compiles future
or changed source documents in OpenKB's native hash registry.

## CLI

Install OpenKB with its web dependencies, then run commands from the repository
root:

```sh
uv tool install 'openkb[web]'
openkb --kb-dir knowledge-base status
openkb --kb-dir knowledge-base list
openkb --kb-dir knowledge-base add path/to/document.md
```

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
- `openkb_search` for credential-free, ranked local retrieval;
- `openkb_read` for exact cited page content;
- `openkb_graph` for resolved `[[wikilink]]` relationships; and
- `openkb_query` for optional model-backed synthesis through the OpenKB CLI.

Restart the MCP client or open a new project session after changing project MCP
configuration. The legacy LLM Wiki desktop application is no longer required.
