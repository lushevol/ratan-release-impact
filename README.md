# Ratan Release Impact

An AI-operated analysis harness for Ratan settlement repositories, business
knowledge, SDLC graph projections, and local behavior evidence.

Start here after cloning:

```sh
./scripts/setup.sh
./scripts/status.sh
```

Setup always attempts to clone every repository in `repos/manifest.json`. With
the Azure DevOps credential available, one command can also install repository
dependencies and index every business repository:

```sh
./scripts/setup.sh --install-repo-deps --index-repos
```

Ask an AI agent to use the project skill `$ask-repo` for requests such as
"set up this project", "clone and index the repos", "generate the wiki",
"check MCP status", or "run the tests". The skill routes those requests to
the repeatable commands under `scripts/`.

Important locations:

- `docs/SETUP_FOR_AI.md`: complete fresh-checkout runbook.
- `repos/manifest.json`: clone inventory with Azure DevOps origin URLs.
- `knowledge-base/raw/`: source documents maintained by `kb-add.sh`,
  `kb-update.sh`, and `kb-delete.sh`.
- `knowledge-base/wiki/`: compiled, citable OpenKB pages.
- `config/`: checked-in SDLC graph and business-description policy.
- `tests/`: root MCP and trace-proxy tests.
