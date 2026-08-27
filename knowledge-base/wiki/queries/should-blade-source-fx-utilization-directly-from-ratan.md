---
type: query
title: Should Blade Source FX Utilization Directly from RATAN?
created: 2026-08-23
updated: 2026-08-23
tags: [fx-utilization, blade, ratan, tds3, architecture-decision]
related: [blade, ratan, tds3, stella, fxu, fx-utilization-data-for-blade-controls, blade-fx-utilization-data-access-options]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/FX Utilization Process  Data Integration for Blade Controls & Visibility.md"]
---
# Should Blade Source FX Utilization Directly from RATAN?

## Question

Should Blade call RATAN directly for FX utilization data when displaying or validating `UTIL` trades, rather than receiving a replicated utilization view through TDS3?

## Why this is open

Blade needs granular utilization data for trade-level display, hard blocks, amendments, and withdrawals. RATAN is identified as the golden source, while TDS3 currently supplies Blade’s core trade data and does not receive the required granular utilization state through STELLA.

Direct access would preserve the source-of-truth boundary but would require Blade to integrate with and depend on RATAN. Replication through TDS3 would simplify Blade’s access pattern but introduce latency, reconciliation, TDS3 scope expansion, and a denormalized silver source. OpenFin UI integration would not satisfy backend control requirements.

## Evidence

The source analysis gives an implicit preference to direct Blade–RATAN integration because it aligns with the stated FM architectural pattern and avoids replicating golden-source data. It does not constitute an approved decision.

## Information needed to resolve the query

- RATAN API endpoints, schemas, and service-level targets.
- Correlation keys across Blade, TDS3, FXU, and RATAN cashflows.
- Exact utilization statuses and remaining-amount semantics.
- Freshness targets for display and action validation.
- Failure behavior when RATAN is unavailable or disagrees with TDS3.
- Concurrency controls preventing over-utilization.
- Caching, authorization, audit, and rate-limiting requirements.
- Confirmation of whether Blade should call RATAN directly or use FXU as an orchestration layer.