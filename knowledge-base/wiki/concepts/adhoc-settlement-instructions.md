---
type: concept
title: Adhoc Settlement Instructions
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-instructions, SSI, vost​ro, nostro, exception-handling]
related: [fmrp-china-cash-settlement, fmo-post-trade-portal, cashflow-status-and-substate-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Adhoc Settlement Instructions

## Definition

Adhoc settlement instructions allow an operator to manually enter settlement-instruction information for a cashflow.

## Demonstrated behavior

The source demonstrates the workflow for:

- `Waiting` cashflows without an SSI Exception.
- `Ready` cashflows.

The user opens cashflow details and uses the **Adhoc SI** button in both the `Vostro SI Information` and `Nostro SI Information` areas. After the required information is entered and submitted, the cashflow substate becomes `Pending Verification`.

The source uses both `Adhoc SSI` and the UI label `Adhoc SI`; both refer to this workflow in the documented scenarios.

## Open detail

The source does not specify the required Vostro and Nostro fields, validation rules, authorization requirements, or verification ownership.
