---
type: concept
title: FXU Cashflow Utilization
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, cashflow, utilization, cash-settlement]
related: [fxu, util-settlement-method, cashflow-utilization-status-lifecycle, cashflow-blotter, cash-settlement-query-service-graphql-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case.md"]
---
# FXU Cashflow Utilization

FXU cashflow utilization is the behavior described for cashflows using the `Util` settlement method. The intended workflow distinguishes utilization from ordinary cashflow actions and introduces visibility of a cashflow's remaining amount.

## Required behavior

For `Util` cashflows, the following actions must be unavailable:

- Netting
- Swift suppress
- Cashflow suppress
- Fail
- Update affirmation
- Early release
- Hold
- Settle As Gross

The source does not establish whether this restriction is enforced only by the UI or also by APIs and backend services. It also does not define whether actions are hidden, disabled, or rejected.

## Utilization visibility

`Cashflow.Remaining_Amount` must be exposed in the view builder. The field may support operational visibility into the amount still available for utilization, but the source does not state whether it is persisted, calculated, or supplied by an upstream system.

The source requests the statuses `UTILIZED` and `PARTIALLY-UTILIZED`, but it does not define the amount thresholds or transition rules that distinguish them.

## Test fixture

The documented fixture uses trade `6709074617`, a `ForeignExchange:Swap`, and four expected cashflows:

- `006709074618`
- `006709074619`
- `006709074620`
- `006709074621`

The initial status is `Ready`, and the source writes the settlement method as `Util`; the canonical relationship between `Util` and `UTIL` remains unresolved.