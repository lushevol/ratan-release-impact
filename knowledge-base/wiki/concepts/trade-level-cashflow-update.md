---
type: concept
title: Trade-Level Cashflow Update
tags: [cashflow, trade, bulk-update, selection-expansion, fxu]
related: [cashflow-blotter, settlement-method-update, transaction-synchronization, fx-utilization, how-are-partial-trade-level-fxu-update-results-classified, what-is-the-scope-of-the-fxu-bulk-update-limit]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/FXU Phase2 Test Case.md"]
---
# Trade-Level Cashflow Update

A trade-level cashflow update is a bulk-operation pattern in which an initial user selection of cashflows is expanded to include all cashflows associated with the relevant `Trade Id` values.

In the FXU Phase 2 Settlement Method Update flow, selecting one cashflow causes the Cashflow Blotter to query all cashflows under the same trade and display that expanded set in the dialog.

## Scope Expansion

The UI compares:

```text
selected cashflow count != by trade id query cashflow count
```

When the counts differ, it informs the user:

> System automatically selected all cashflows under trades

This distinguishes a user selection that already covers all cashflows in its trades from one whose effective update scope was expanded automatically.

## Mixed Eligibility and Results

Eligibility remains observable at cashflow level: cashflows that do not meet update conditions are displayed as insufficient cashflows. Presentation and completion semantics are nonetheless trade-oriented:

- Dialog results are ordered by `Trade Id ASC`.
- Success and failure responses are reported at trade level.
- Notifications accompany the trade-level response.

The source does not define whether a trade with mixed eligible and ineligible cashflows is partially updated, rejected as a whole, or classified through another aggregation rule. That gap is tracked by [[how-are-partial-trade-level-fxu-update-results-classified]].

## Relationship to Transaction Synchronization

This behavior is a concrete UI-side consistency mechanism related to [[transaction-synchronization]]. It prevents an update initiated from one cashflow from necessarily applying to only a partial subset of a trade.