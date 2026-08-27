---
type: concept
title: Client-Level Cashflow Netting
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-netting, client-level-netting, settlement, mixed-currency]
related: [fmrp-china-cash-settlement, fmo-post-trade-portal, cashflow-blotter, netting-eligibility-rule, resultant-cashflow, component-cashflow, cashflow-status-and-substate-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Client-Level Cashflow Netting

## Definition

Client-level cashflow netting consolidates eligible cashflows at the client level into resultant cashflows. The original records are component cashflows.

## Demonstrated workflow

In the cashflow blotter, the user selects eligible cashflows, chooses **Net Selected Cashflow**, reviews the netting window, chooses **Netting All Cashflow**, and submits the affirmation.

The stated result is:

- Component cashflows change to `Netted`.
- One or more resultant cashflows are created.
- Resultant cashflows initially appear as `Queued`–`Waiting`.
- Cashflows are grouped by currency when a selection contains multiple currencies.

A currency group with only one cashflow may remain unnetted and in `Waiting`, while another group with multiple eligible cashflows produces a resultant cashflow.

## Eligibility

The source associates this process with [[netting-eligibility-rule]]. The rule should be applied without silently changing its documented `CNO` value to `CNY`.

## Limitations

The source does not fully specify grouping criteria, direction matching, amount aggregation, or the formal handling of non-nettable groups.
