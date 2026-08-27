---
type: comparison
title: Group Service vs Orchestration for SSI Stamping
created: 2026-08-24
updated: 2026-08-24
tags: [SSI-stamping, architecture, service-ownership, Group-service, orchestration]
related: [cashflow-stamping-domain-ownership, trade-level-ssi-stamping, orchestration, nstp-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md"]
---
# Group Service vs Orchestration for SSI Stamping

The source presents two unselected locations for trade and cashflow SSI stamping.

| Dimension | Option A: Group service | Option B: Orchestration |
| --- | --- | --- |
| Primary responsibility | Batch stamping and cashflow enrichment | UBER-triggered trade stamping and cashflow coordination |
| Trade result reuse | Trade stamping and enrichment occur together | Trade result is stored when UBER is received and reused later |
| SSI service calls | Batch-oriented | Described as `1 + N` invocations |
| Cashflow impact | Enriched data later overrides lifecycle-service data | Cashflows use the previously stored trade result |
| Concurrency concern | Must prevent concurrent access to the same cashflow | Must coordinate arrivals, reuse, retries, and version selection |
| Failure handling | Requires batch and lifecycle-service recovery semantics | Requires missing or failed trade-result compensation |
| Current status | Proposed alternative; not selected | Proposed alternative; not selected |

## Decision criteria

Selection requires measured cashflow and trade volumes, latency targets, ownership of persisted enrichment, locking or optimistic-concurrency design, retry and NSTP semantics, lifecycle-service integration, and operational observability.

Neither option is supported by performance evidence in the source. This page must not be treated as an accepted architecture decision.