---
type: comparison
title: Blade FX Utilization Data Access Options
created: 2026-08-23
updated: 2026-08-23
tags: [blade, fx-utilization, ratan, tds3, architecture, integration]
related: [blade, ratan, tds3, stella, fxu, fx-utilization-data-for-blade-controls, should-blade-source-fx-utilization-directly-from-ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/FX Utilization Process  Data Integration for Blade Controls & Visibility.md"]
---
# Blade FX Utilization Data Access Options

## Comparison

| Criterion | Option 1: RATAN → TDS3 | Option 2: Blade → RATAN | Option 3: Blade → RATAN UI through OpenFin |
|---|---|---|---|
| Primary access pattern | Blade reads replicated utilization data from TDS3. | Blade reads core trade data from TDS3 and utilization data directly from RATAN. | Users view RATAN information through a UI integration. |
| Authority | RATAN remains the golden source; TDS3 holds a replicated view. | RATAN remains the direct source for utilization decisions. | RATAN remains the source displayed through the UI. |
| Data freshness | Dependent on RATAN-to-TDS3 propagation latency. | Potentially closest to current RATAN state. | Depends on the UI integration and does not expose state to backend controls. |
| Blade integration complexity | Lower, because Blade retains one primary integration point. | Higher, because Blade merges TDS3 and RATAN data. | Lower for visual access but insufficient for backend processing. |
| TDS3 impact | Requires data-model, capacity, and downstream-consumer changes. | Leaves TDS3’s granular-utilization role unchanged. | Leaves TDS3 unchanged. |
| Hard-block support | Possible if synchronization is sufficiently fresh and reliable. | Directly supports control decisions if the RATAN API is suitable. | Not supported by UI integration alone. |
| Main architectural concern | Denormalized silver source and reconciliation with RATAN. | Coupling Blade to RATAN’s API, availability, and performance. | Solves presentation but not transactional validation. |

## Decision criteria

The unresolved decision should assess:

1. RATAN API completeness, performance, and availability.
2. Required freshness for display and hard-block decisions.
3. TDS3 capacity and the impact on its downstream consumers.
4. Correlation and reconciliation behavior when systems disagree.
5. Failure behavior, including whether controls fail closed.
6. Concurrency protection for simultaneous utilization requests.
7. Security, entitlement, audit, and rate-limiting requirements.
8. Whether FXU remains the orchestration layer.

## Current evidence

The source analysis favors Option 2 because it preserves RATAN as the golden source and avoids denormalizing utilization state into TDS3. This is an analysis-stage preference only; no approved decision is recorded.

Option 3 should not be treated as a complete alternative for the stated requirement because it does not provide utilization data to Blade backend processes.