---
type: concept
title: FXU Settlement-Method Amendment
tags: [FXU, settlement-method, Gross, UTIL, FMO, hard-block]
related: [fxu, ratan, blade, stella, fmo-ops, cashflow-status-lifecycle]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Dependencies for expansion to other Markets.md"]
---
# FXU Settlement-Method Amendment

FXU requires trade-level amendment of the Settlement Method between Gross and UTIL. FMO users are expected to perform the change through Blade, subject to utilization-based restrictions.

## Blocking rule

The change must be hard-blocked when the trade is:

- Fully utilized.
- Partially utilized.
- Utilized through one cashflow of the trade.
- Utilized through one leg of an FX swap.

The source separately requires a hard block for Middle Office users, but does not identify which actions are prohibited for that role.

## Component responsibilities

Blade requires a new Ops profile. RATAN must trigger a new event to Stella. The source does not identify which component is the authoritative mutation point or define the event name, payload, acknowledgement, retry, or failure behavior.

## Related state questions

The rule requires a distinction between trade-level utilization, cashflow-level utilization, and utilization of an individual FX-swap leg. These distinctions should be reconciled with [[concepts/cashflow-status-lifecycle]] before implementation.