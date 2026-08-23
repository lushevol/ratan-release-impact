---
name: requirement-impact
description: Analyze a business requirement against the Wiki MCP and SDLC Graph to predict affected features, repositories, code paths, contracts, data, tests, and uncertainties. Use when a user asks what a new requirement will change before implementation, or wants to compare predicted and actual impact after a change.
---

# Requirement Impact

Use this skill for requirement-level change impact, not for ordinary code review or a single-symbol blast-radius check.

## Sources and authority

Combine three evidence layers:

1. Business meaning from the `llm-wiki` MCP server. Query concepts, features, entities, processes, rules, and related requirements before interpreting code names.
2. Static code and service relationships from the SDLC Graph (`graph/graph.json`) and, when available, GitNexus execution flows and symbol context.
3. Repository source and configuration for line-level confirmation.

The graph and source establish technical facts. The Wiki establishes business meaning. Model output may propose mappings and changes, but must label them as `inferred` and include the supporting paths. Never turn an absent edge into proof that a dependency does not exist.

Read [references/wiki-mcp.md](references/wiki-mcp.md) when the Wiki MCP is available. Read [references/report-schema.md](references/report-schema.md) when producing machine-readable output.

## Workflow

1. Normalize the requirement into actors, business terms, entities, actions, constraints, events, acceptance criteria, and explicit unknowns.
2. Search the Wiki MCP using the business terms. Retrieve context for matched features and processes, retaining document/section evidence and freshness.
3. Match those concepts to `Feature` nodes and service catalogs in the SDLC Graph. Use the local deterministic helper for a baseline candidate set when useful:

   ```text
   python3 .claude/skills/requirement-impact/scripts/impact_report.py \
     --graph graph/graph.json --requirement "..." --out impact.json
   ```

4. Expand each matched feature through typed edges: `IMPLEMENTS`, `PROVIDES`, `CALLS`, `DEPENDS_ON`, `PUBLISHES`, `SUBSCRIBES_TO`, `READS_FROM`, `WRITES_TO`, and `CONTAINS`. Then use GitNexus `context`/`query` for symbol and execution-flow detail where the graph is too coarse.
5. Confirm high-value paths in source: API controllers, clients, consumers/producers, domain services, migrations, configuration, and tests. Run upstream impact analysis before editing any existing symbol.
6. Classify each result as `direct`, `indirect`, `inferred`, `unknown`, or `stale`; include a relationship path, confidence, and evidence. Assign risk from graph reachability and contract/data changes, not intuition alone.
7. Produce a concise human report and the JSON shape in [references/report-schema.md](references/report-schema.md). Include affected repositories/features/symbols/interfaces/data/flows, predicted change types, test scope, risks, unresolved dependencies, and clarification questions.

## Before/after modes

- **Prediction:** represent the requirement as a proposed change set over the baseline graph. Do not claim that files will change; say what must be inspected or is likely to change.
- **Validation:** scan the before and after commits, run graph diff, and compare actual changes with the predicted set. Report missed predictions and unexplained changes separately.

## Guardrails

- Preserve provenance for every conclusion; prefer a smaller evidence-backed result to a broad guessed inventory.
- Do not expose secrets from Wiki, source, configuration, or MCP responses.
- Treat unresolved dynamic service discovery, topic names, reflection, and environment-specific configuration as explicit uncertainty.
- Distinguish business impact from implementation impact and from deployment/operational impact.
- Ask focused clarification questions only when ambiguity changes the affected boundary or risk.
