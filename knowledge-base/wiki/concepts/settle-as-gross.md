---
type: concept
title: Settle as Gross
created: 2026-08-22
updated: 2026-08-22
tags: [gross-settlement, exception-handling, cashflow-operations]
related: [fmrp-china-cash-settlement, fmo-post-trade-portal, cashflow-status-and-substate-model, client-level-cashflow-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Settle as Gross

## Definition

Settle as gross is an operator action that bypasses a pending netting-related condition and allows a cashflow to proceed through gross settlement processing.

## Demonstrated inputs and result

The source tests cashflows with `Sub State Type` equal to `Pending Netting` and cashflows with `pending another leg`.

The action is available from the cashflow blotter. The operator enters a comment and submits. The stated observed result is:

- Cashflow state changes to `Queued`.
- `Sub State Type` changes to `NA`.

The scenario descriptions also mention `Pending Exception` as a possible subtype outcome, but do not define the condition producing it. This result distinction remains unresolved.

## Open detail

The source does not explain whether gross settlement removes a cashflow from future netting permanently, how comments are audited, or how the operation affects related component and resultant cashflows.
