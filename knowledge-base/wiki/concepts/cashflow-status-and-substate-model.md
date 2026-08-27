---
type: concept
title: Cashflow Status and Substate Model
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-lifecycle, workflow-state, settlement-exceptions]
related: [fmrp-china-cash-settlement, cashflow-blotter, client-level-cashflow-netting, irs-auto-netting, hold-and-un-hold, manual-failure-and-reinstatement, settle-as-gross, adhoc-settlement-instructions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Cashflow Status and Substate Model

## Observed statuses and substates

The Q2 2023 demonstration refers to the following values:

- States or primary statuses: `Queued`, `Waiting`, `Ready`, `Hold`, `Netted`, `Dead`, and `Failed`.
- Secondary values: `Pending Netting`, `Pending Exception`, `Pending another leg`, `Pending Verification`, and `NA`.
- Terminology variants: `Sub State Type`, `sub status type`, `sub status`, and `Sub State`.

## Demonstrated transitions

| Operation | Observed transition |
| --- | --- |
| Client-level netting | Component `Pending Netting` cashflows → `Netted`; resultant → `Queued`–`Waiting` |
| IRS auto netting | Fixed/floating legs → `Netted` with `NA`; resultant → `Queued`–`Waiting` with `Pending Exception` |
| Post-IRS netting | Prior IRS resultants → `Dead`; new resultant → `Waiting` |
| Hold | `Waiting` or `Ready` → `Hold` |
| Un-hold | `Hold` → prior `Waiting` or `Ready` state |
| Manual failure | `Waiting` or `Ready` → `Failed` |
| Reinstate | `Failed` → `Queued` |
| Settle as gross | `Pending Netting` or `pending another leg` → `Queued` with stated subtype `NA` |
| Adhoc SSI | Eligible `Waiting` or `Ready` cashflow → `Pending Verification` substate |

## Qualification

This is an observed scenario model, not a complete authoritative state machine. The source does not define all allowed transitions, terminal-state semantics, ownership, retry behavior, or the distinction between `NA` and `Pending Exception` in gross settlement.
