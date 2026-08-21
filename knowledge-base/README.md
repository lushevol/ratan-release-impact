# OpenKB Knowledge Base

This directory is the standalone OpenKB root for the repository. It contains
the OpenKB state, raw inputs, and compiled Markdown wiki:

- `.openkb/` — configuration, registry, and ingest state
- `raw/` — copies of ingested documents
- `wiki/` — summaries, concepts, entities, and reports
- `mock-data/` — small local fixtures used for smoke testing

Run the wrappers from the repository root:

```bash
./scripts/openkb-status
./scripts/openkb-list
./scripts/openkb-add path/to/document-or-directory
./scripts/openkb-query "What does this knowledge base say about...?"
./scripts/openkb-lint
./scripts/openkb-web
```

Paths passed to `openkb-add` are resolved from the repository root, so
`./scripts/openkb-add repos/lifecycle/README.md` works from any directory.

The wrappers use `DEEPSEEK_OPENAI_BASE_URL`, `DEEPSEEK_API_KEY`, and
`DEEPSEEK_LLM_MODEL` from the process environment. They map those values to
OpenKB's `OPENAI_API_BASE` and `LLM_API_KEY` names for the duration of each
command; credentials are not written here.
