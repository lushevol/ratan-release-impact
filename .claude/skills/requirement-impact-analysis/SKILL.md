---
name: requirement-impact-analysis
description: Produce evidence-backed requirement impact reports by combining authoritative business/design material from OpenKB, cross-repository architecture from SDLC Graph, and exact symbol/process blast radius from GitNexus. Use when assessing what a requirement changes, which services, APIs, tables, topics, components, and tests are affected, or whether an intended behavior is proven.
---

# Requirement Impact Analysis

Use the three project MCP servers as an evidence chain, not as interchangeable search engines:

1. Use `openkb` to establish business intent, terminology, decisions, acceptance criteria, and known limitations.
2. Use `sdlcGraph` to identify candidate repositories and traverse business and runtime relationships.
3. Use `gitnexus` plus exact source inspection to confirm symbols, callers, execution processes, and blast radius.

Read [evidence and reporting](references/evidence-and-reporting.md) before issuing a confidence or proof verdict.

## Workflow

### 1. Normalize the requirement

Separate current behavior, desired behavior, invariants, removals, additions, boundary conditions, and undefined terms. Convert each rule into an independently testable predicate. Do not silently choose a meaning for an overloaded field such as payment type, settlement type, direction, or trade event.

If any material predicate remains ambiguous, invoke `$requirement-grill` before continuing. It must search OpenKB for authoritative background first, then ask the user or named business owner only for rules that the knowledge base cannot establish. Do not proceed to an implementation recommendation while the grill verdict is `BLOCKED ON REQUIREMENT DECISION`.

### 2. Establish business evidence

Search OpenKB for the exact control, business terms, prior decisions, and linked source pages. Read each exact cited page before using it as evidence. Prefer direct requirement/design pages over generated concept summaries. Record document title/path and which assertion it supports. If no authoritative source defines a requested term or behavior, mark it `UNRESOLVED` and state what owner or document is needed.

### 3. Find candidate architecture

Call SDLC Graph `analyze_requirement_impact`, then inspect likely repositories with `get_service_picture` and exact nodes with `get_node_neighborhood`. Treat semantic matches as candidates only. Exclude nodes reached solely through generic words unless a concrete business/runtime edge corroborates them.

List affected APIs, database tables, Kafka topics, external services, pages, and domain components. Database-table evidence must come from runtime clients, ORM mappings, or executed query builders; never infer required tables from migrations. Preserve unresolved topic expressions and external frontiers.

### 4. Confirm code and blast radius

Check GitNexus index freshness for the actual business repository under `repos/`. Do not use an index of the analysis harness itself as business-code evidence. Query the concept, inspect exact symbol context, and run upstream impact for every symbol proposed for modification. Disambiguate duplicate symbol names by file. Report HIGH or CRITICAL risk before recommending implementation.

Corroborate graph results against exact source paths and runtime configuration. If GitNexus is stale, incomplete, or fails to index, do not substitute a guessed score: state the limitation and report only directly observed callers.

### 5. Assess proof

This workflow verifies the quality of the requirement-impact analysis; it does not implement the requested business change. Static code and graph evidence can confirm that an implementation path exists; it cannot prove runtime behavior. A `PROVEN` verdict in this workflow means the analysis produced an evidence-backed, unambiguous impact contract, not that production behavior was changed or deployed. Separate runtime claims still require executable evidence for the requested behavior, including positive, negative, equality/inequality, null/missing-field, date-boundary/time-zone, status, source-system, and end-to-end persistence/transport cases as applicable.

Run the narrowest relevant existing tests and record the exact command and outcome. If tests cannot run, the proposed rule is absent, fixtures only mock the predicate, or production telemetry cannot distinguish false positives from false negatives, return `NOT PROVEN` even when confidence in the source reading is high.

### 6. Write the report

Use the contract in the reference. Link each component to its file or narrow wildcard path. Separate confirmed facts, inferences, contradictions, and open questions. Include an auditable decision log and ordered MCP/tool trace with inputs and material outputs; summarize reproducible rationale instead of private chain-of-thought. Finish with a go/no-go verdict and the minimum evidence needed to raise confidence.

## Failure policy

- Do not claim “no impact” from an empty semantic search.
- Do not claim an improvement from lower exception volume without labeled ground truth.
- Do not equate `RELEASED` with a broader post-release status set without documenting the difference.
- Do not claim a future rule exists because the input field is parsed or stored.
- Do not expose credentials or paste unredacted private documents into reports.
