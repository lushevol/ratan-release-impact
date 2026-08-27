---
type: concept
title: FX Utilization Data for Blade Controls
created: 2026-08-23
updated: 2026-08-23
tags: [fx-utilization, blade, hard-controls, golden-source, settlement]
related: [ratan, blade, tds3, stella, fxu, cashflow-status-lifecycle, cashflow-event-versioning, cashflow-expiry-versioning, cashflow-reference-consistency-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/FX Utilization Process  Data Integration for Blade Controls & Visibility.md"]
---
# FX Utilization Data for Blade Controls

## Definition

FX utilization data describes how much of a forward FX deal has been applied to cross-border payments and how much remains available for utilization. For Blade, the relevant information includes:

- Remaining unutilized amount at trade or cashflow level.
- Specific utilization status.
- Whether a proposed amendment, withdrawal, or `UTIL` trade is permitted against the remaining amount.

## Lifecycle context

A deal may be utilized fully or partially on the value date or through early utilization. If it remains unutilized, it may enter Past Due processing after the value date and remain available for a country-specific period of approximately 3–7 days. Remaining amounts may then be reversed, with rate-difference costs charged to the client.

The exact status vocabulary, amount semantics, and country-specific rules are not defined in the source.

## Control-grade versus display data

Display data allows a user to see an amount or status. Control-grade data must also be sufficiently fresh, correlated to the correct trade and cashflow, and authoritative enough to support an enforced decision.

Blade’s requirement is control-grade: it must use current utilization state to apply hard blocks to `UTIL` trades and validate amendments and withdrawals. A UI-only integration through OpenFin may support visibility but cannot independently implement backend controls.

## Source-of-truth boundary

RATAN is identified as the golden source for cashflow settlement, utilization amounts, and detailed utilization statuses. TDS3 currently supplies Blade’s core trade data but does not receive the described granular utilization information through STELLA.

Replicating RATAN data into TDS3 could simplify Blade’s integration but would introduce a silver source, synchronization latency, reconciliation requirements, and additional settlement-state scope for TDS3. Direct access from Blade to RATAN would preserve the authority boundary but require Blade to merge data from two systems.

## Design considerations

Any implementation should define:

- Correlation between Blade or TDS3 trades, FXU utilization requests, and RATAN cashflows.
- Freshness and latency requirements for display and blocking decisions.
- Behavior during RATAN unavailability or disagreement with TDS3.
- Concurrency protection against over-utilization.
- Audit, entitlement, rate-limiting, and reconciliation behavior.

These rules remain unresolved by the source.