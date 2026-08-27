---
type: concept
title: Murex-to-RATAN Cashflow Integration
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, cashflow-routing, settlement, vd-7]
related: [murex, ratan, razor, murex-cashflow-status-lifecycle, murex-ratan-migration-reconciliation, auto-netting-datetime-calculation, manual-entity-lms-feed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration.md"]
---
# Murex-to-RATAN Cashflow Integration

Murex-to-RATAN Cashflow Integration is the interim routing pattern in which [[murex]] generates China cashflows but sends qualifying flows to [[ratan]] for settlement processing while trade migration to [[stella]] has not yet occurred.

## Dispatch boundary

A cashflow must be in a FMRP-enabled China entity, be in `INIT`, fall within the VD-7 window, and not meet an exclusion. Documented exclusions include precious-metal deals, NDS non-deliverable currency, zero payments, and specified FXD flows. The struck-through trade-validation criterion is not an established active rule.

Precious-metal cashflows remain in Murex BAU. Eligible non-precious-metal cashflows move to RATAN for netting or grossing, SWIFT, and settlement processing, with [[razor]] proposed for settlement accounting.

## Duplicate-output prevention

For eligible flows, Murex must not also issue LMS and FMSRE messages or produce settlement-accounting output to Aspire and EBBS. Murex continues trade accounting to Aspire. This control is specific to the documented China Murex integration and does not establish a general rule for all RATAN flows.

## Operational controls

- Dispatch is real time only when the value date enters the seven-day window.
- Murex should expose outbound and acknowledgement status to settlement users.
- RATAN acknowledgement is expected for every outbound cashflow.
- Murex payment STP and China BAU queue handling must exclude eligible flows to prevent Murex settlement after routing.

The detailed source-side lifecycle is documented in [[murex-cashflow-status-lifecycle]].