---
type: concept
title: FMRP Market-Event Settlement Impact
created: 2026-08-22
updated: 2026-08-22
tags: [fmrp, market-events, trade-lineage, cashflows, ratan, settlement]
related: [fmrp, ratan, murex, cashflow-lifecycle-state-machine, murex-ratan-cashflow-integration, murex-ratan-migration-reconciliation, allocation-cashflow-state-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement.md"]
---
# FMRP Market-Event Settlement Impact

FMRP market-event settlement impact concerns how new or redesigned trade events affect trade identifiers, cashflows, lifecycle processing, and RATAN settlement behavior.

## Event inventory

| Market Event Type | Documented behavior | Stated RATAN position |
|---|---|---|
| Clearing | Dedicated clearing event; no new trade ID | No impact to RATAN |
| Remaining Party Full | Non-clearing counterparty change; new trade ID for the new trade | No impact to RATAN |
| Refresh | Calendar-update-driven event, similar to a trade amendment | RATAN position requires confirmation |
| Allocations | `MW → VPA → Stella`; block cashflows are `SUSPENDED`; child cashflows are `PROJECTED` | RATAN filters allocation-event cashflows |
| Remaining Party Partial | Non-clearing counterparty change, similar to a trade amendment | No impact to RATAN |
| UNDO for live trade | Extends UNDO events to live trades and events | RATAN position requires confirmation |
| Step In Partial | Similar to new-trade booking | No impact to RATAN |
| Step In Full | Similar to new-trade booking | No impact to RATAN |

## Lineage implications

The distinction between Clearing and Remaining Party Full is significant. Clearing preserves the trade ID, whereas Remaining Party Full creates a new trade ID. That difference can affect correlation, cancellation, replacement, historical lineage, and duplicate-payment controls even when the source labels both events as having no RATAN impact.

The phrase “no RATAN impact” should be treated as a scope classification rather than proof that no settlement data is published or changed. Confirmation is needed for event publication, cashflow amendment or replacement, and correlation between old and new trades.