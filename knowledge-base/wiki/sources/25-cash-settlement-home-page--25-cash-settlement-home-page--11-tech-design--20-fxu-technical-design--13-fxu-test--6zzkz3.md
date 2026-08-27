---
type: source
title: FXU Test Case
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, fxu, test-case, cashflows, utilization]
related: [fxu, fxu-cashflow-utilization, util-settlement-method, cashflow-utilization-status-lifecycle, cashflow-blotter, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case.md"]
---
# FXU Test Case

This source defines an FXU technical test scenario and implementation checklist for the Cash Settlement platform. It specifies a trade fixture, expected cashflows, UI action restrictions, view-builder and filter fields, cashflow statuses, a settlement method, and a Vostro settlement-means value.

The document records requirements and expected setup only. It does not provide execution results, pass/fail evidence, acceptance criteria, API responses, database records, or production deployment confirmation.

## Test fixture

The scenario requires booking one `ForeignExchange:Swap` trade and generating four cashflows.

- Trade ID: `6709074617`
- Expected cashflow count: 4
- Initial cashflow status: `Ready`
- Settlement method: `Util`

| Cashflow | Identifier |
|---|---|
| C1 | `006709074618` |
| C2 | `006709074619` |
| C3 | `006709074620` |
| C4 | `006709074621` |

The source does not specify the cashflow currencies, amounts, dates, legs, or utilization relationships.

## Required action restrictions

The following actions must be removed or made unavailable for a cashflow using the `Util` settlement method:

- Netting
- Swift suppress
- Cashflow suppress
- Fail
- Update affirmation
- Early release
- Hold
- Settle As Gross

The source does not define whether these actions are hidden, disabled, or rejected server-side. It also does not define whether the restriction applies to every lifecycle status or only to cashflows in the initial `Ready` state.

## View-builder and customer-filter fields

The following fields must be added:

- `Cashflow.Remaining_Amount` on the view builder
- `Trade.Source_System_Trade_Internal_Id` on the view builder and in customer filters

The source does not define the field types, nullability, display labels, supported filter operators, authorization rules, or source mappings. It does not establish whether `Cashflow.Remaining_Amount` is persisted or calculated.

## Cashflow statuses

The source requests the addition of these cashflow statuses:

- `UTILIZED`
- `PARTIALLY-UTILIZED`
- `PASTDUE`

No state-transition rules, terminal-state semantics, owning service, or relationship between `PARTIALLY-UTILIZED` and `Cashflow.Remaining_Amount` is defined.

## Settlement values

The source requests two distinct reference-data changes:

- Add `UTIL` as a settlement method in the cashflow blotter.
- Add settlement means value `FXBRREC-M` in Vostro.

The source does not identify the authoritative reference-data owner, persistence location, validation rules, or whether `FXBRREC-M` is valid only for `UTIL` or for additional settlement methods.

## Source context

```text
1, book a ForeignExchange:Swap trade, and generate 4 cashflows, cashflow status = Ready, Settlement-method = Util

tradeId: 6709074617

cashflows: 006709074618(C1), 006709074619(C2), 006709074620(C3), 006709074621(C4)

1, Remove action for netting/swift suppress/cashflow suppress/fail/update affirmation/early release/hold /Settle As Gross for Util cashflow

2, Add Cashflow.Remaining_Amount on view builder

3, Add Trade.Source_System_Trade_Internal_Id on view builder/customer filters

Add cashflow status UTILIZED, PARTIALLY-UTILIZED, PASTDUE

Settlement method in cashflow blotter to add UTIL

Add Settlement Means value--FXBRREC-M in vostro
```

## Related wiki context

The test case extends the existing [[cash-settlement-platform]] and [[cashflow-blotter]] context. Its field and read-model implications relate to [[centralized-cashflow-field-mapping-governance]], [[dynamic-cashflow-query-field-mapping]], and [[cash-settlement-query-service-graphql-read-model]]. Any event-processing or downstream write-back behavior should be verified separately against [[cashflow-status-change-event-contract]] and [[fx-cashflow-status-write-back]].