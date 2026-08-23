> **Canonical source of truth:** [`BEHAVIOR_CENTRIC_SDLC_IMPACT_FINAL_PROPOSAL.md`](../../../BEHAVIOR_CENTRIC_SDLC_IMPACT_FINAL_PROPOSAL.md). All specifications, design decisions, tasks, implementation changes, validation, and later amendments for this OpenSpec change MUST remain traceable to and consistent with that document. If an artifact conflicts with it, the canonical proposal takes precedence unless the user explicitly revises the canonical proposal.

## Why

Release managers cannot currently trace a PO-authored requirement from its business intent through the UI applications, backend services, contracts, data, configuration, rules, and regression tests that may be affected. The existing requirement-impact MVP is too coarse and can either return no match as low risk or expand across most of the graph, so the POC needs bounded, auditable reasoning that explicitly abstains when business or technical evidence is insufficient.

## What Changes

- Use a manual ADO-derived analysis request to retrieve requirement, acceptance-criteria, design, rule, and process evidence from the existing local LLM Wiki MCP, with immutable provenance and a visibly classified local fallback.
- Extend the existing SDLC scanner—without adding another code-analysis product—to cover all four React/TypeScript UI repositories and four Java/Spring backend repositories.
- Discover and identify release-relevant technical contracts: UI routes, REST and GraphQL operations, events and payload schemas, tables and other database objects, external dependencies, configuration, feature flags, business rules, and tests.
- Introduce versioned requirement snapshots, behavior/scenario identities, placeholder PO/BA confirmation, and explicit business-to-technical mapping assertions.
- Replace unrestricted bidirectional graph traversal and token-overlap matching with allow-listed directional paths, evidence classifications, bounded fan-out, and a mandatory `INDETERMINATE` outcome for stale, ambiguous, or insufficient evidence.
- Separate impact severity from uncertainty and classify results as direct consideration, regression verification, possible context, or unknown.
- Recommend regression tests as execute, update, or create actions while keeping `EXERCISES` distinct from business-level `VERIFIES` evidence.
- Produce aligned Markdown and JSON release-impact reports with baseline commits, Wiki evidence identity, auditable paths, diagnostics, unknowns, and clarification questions.
- Store POC inputs, catalogs, graph snapshots, evidence manifests, reports, and review decisions as versioned local Git artifacts.
- Keep live ADO integration, runtime telemetry, post-change behavioral verification, automated release gating, graph databases, and new code-analysis tools outside the initial POC.

## Capabilities

### New Capabilities

- `requirement-evidence-ingestion`: Accept a manual ADO-derived trigger, retrieve and cite LLM Wiki requirement/design evidence, manage live/fallback/unavailable states, and produce an immutable normalized requirement snapshot.
- `sdlc-evidence-graph`: Scan the eight-repository baseline for applications and release-relevant technical contracts with stable identities, provenance, coverage reporting, and explicit diagnostics.
- `behavior-impact-reasoning`: Propose a versioned behavior delta, map business evidence to technical seeds, traverse only approved evidence paths, separate severity from uncertainty, and safely return `INDETERMINATE`.
- `regression-test-recommendation`: Inventory and relate tests to affected behaviors and contracts, distinguish exercise evidence from verified business coverage, and recommend execute/update/create actions.
- `release-impact-reporting`: Generate consistent human and machine-readable impact reports, preserve end-to-end workflow contract identities, and capture release-manager review decisions.

### Modified Capabilities

None. The repository has no existing OpenSpec capability specifications; this change introduces the initial capability set.

## Impact

- **Governance constraint:** every downstream OpenSpec artifact and implementation task must cite or map to the canonical final proposal; deviations require an explicit recorded decision and user approval.
- **Existing implementation areas:** `.claude/skills/sdlc-graph`, `.claude/skills/requirement-impact`, `graph/`, and the existing GitNexus-assisted enrichment workflow.
- **New repository-local artifacts:** analysis requests, Wiki evidence manifests, normalized requirement snapshots, behavior/scenario catalogs, repository alias/configuration files, graph snapshots, impact reports, and release review records.
- **Scoped systems:** `mfe-base`, `mfe-cashflow-blotter`, `mfe-ratan-container`, `mfe-root-config`, `ratan-cashflow-lifecycle-service`, `ratan-cash-settlement-netting-service`, `ratan-cash-settlement-orchestration`, and `ratan-cash-settlement-ssi-stamping-service`.
- **Existing integrations:** local `llm-wiki` MCP project `Ratan-Settlement`, checked-in Wiki fallback, and the existing GitNexus index. No new external analysis dependency is introduced.
- **Operational behavior:** the graph and GitNexus baseline are refreshed manually before analysis; Wiki or scanner failures remain visible and may force `INDETERMINATE` rather than a reassuring risk result.
- **Compatibility:** no production API or runtime behavior is intentionally changed by the POC; changes are confined to analysis tooling, schemas, evidence artifacts, and reporting workflows.
