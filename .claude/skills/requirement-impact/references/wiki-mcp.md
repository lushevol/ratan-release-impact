# Wiki MCP Adapter

The configured server is `llm-wiki`:

```json
{
  "command": "node",
  "args": ["/Applications/LLM Wiki.app/Contents/Resources/mcp-server/dist/src/index.js"]
}
```

The exact tool names may vary by server version. Discover the server tools first, then map them to these logical operations:

| Operation | Purpose |
|---|---|
| `search` | Find concepts, features, entities, rules, and processes from requirement terms |
| `get` / `context` | Retrieve the authoritative context for a matched item |
| `related` | Find related features, systems, requirements, and source documents |
| `source` | Retrieve the document section used as evidence |

For each response retain the item title/ID, source document, section or heading, retrieval time, and any server confidence. Query terms should include exact domain nouns and meaningful action phrases; avoid sending the entire requirement repeatedly.

If the MCP is unavailable, continue with the local graph and clearly mark business mappings as `unknown` or `inferred`. Do not fabricate Wiki citations.
