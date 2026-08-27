---
type: concept
title: Manual Cashflow Push from Group Blotter
tags: [cash-settlement, group-blotter, manual-recovery, cashflow-processing]
related: [group-blotter, murex-ratan-trade-id-synchronization-gap, cashflow-blotter-functional-scope, cashflow-partial-update, trade-event-id-lineage]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Grouping Blotter Monitoring.md"]
---
# Manual Cashflow Push from Group Blotter

Manual cashflow pushing is the recovery action used when a cashflow cannot be automatically synchronized because the trade ID in RATAN differs from the validated trade ID in Murex.

The user initiates the action in the [[group-blotter]] and pushes the cashflow to the Cashflow Blotter.

## Trigger

The documented trigger is a Murex non-economic amendment that changes the trade ID, such as the change from `96502251` to `96522715`, while RATAN remains associated with the original ID.

## Distinction from missing-payment repair

Manual pushing is not the prescribed response for every Group Pending exception. When a payment was generated but not sent from Murex to RATAN, operations should investigate with the Murex 2.11 PSS team and follow the Murex DOI instead.

The source does not define whether manual pushing requires maker-checker approval, creates an audit record, prevents duplicates, or supports reversal.