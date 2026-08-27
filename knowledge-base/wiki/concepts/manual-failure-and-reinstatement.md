---
type: concept
title: Manual Failure and Reinstatement
created: 2026-08-22
updated: 2026-08-22
tags: [exception-handling, cashflow-operations, settlement]
related: [fmrp-china-cash-settlement, fmo-post-trade-portal, cashflow-status-and-substate-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Manual Failure and Reinstatement

## Definition

Manual failure and reinstatement are operator workflows for moving a cashflow into an exception state and returning it to processing.

## Demonstrated behavior

A `Waiting` or `Ready` cashflow can be selected in the cashflow blotter and moved to `Failed` through the **Failed** action and a comments window.

For a failed `Ready` cashflow, the source states that:

1. The original failure comment persists.
2. **Reinstate** becomes available.
3. A reinstatement comment window appears.
4. Submission returns the cashflow to `Queued` so it can be processed again.

The source uses both `Failed` and the misspelled UI-related form `Faild`; the normalized concept name is **Failed**.

## Open detail

The source does not define failure reason taxonomy, permissions, retry limits, or whether reinstatement is available for every failed state.
