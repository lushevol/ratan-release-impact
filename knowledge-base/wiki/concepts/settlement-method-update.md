---
type: concept
title: Settlement Method Update
tags: [cash-settlement, settlement-method, FX, cashflow, RATAN, fxu, cashflow-blotter, validation, bulk-update]
related: [ratan, cashflow-blotter, util-to-gross-settlement-update, gross-to-util-settlement-update, trade-level-cashflow-selection-expansion, cashflow-status-lifecycle, what-is-the-authoritative-settlement-method-update-contract, fxu, fx-utilization, fxu-utilization-validation, trade-level-cashflow-update, what-is-the-authoritative-fxu-settlement-method-transition-matrix, what-is-the-scope-of-the-fxu-bulk-update-limit]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Settlement Method Update.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/FXU Phase2 Test Case.md"]
---
# Settlement Method Update

**Settlement Method Update** is a user-triggered Cashflow Blotter right-menu action, tested as part of FXU Phase 2. It changes the settlement-method field for eligible FX cashflows and presents validation and results through a dialog.

The functional-requirement version describes two separate business rules:

- [[util-to-gross-settlement-update]] applies to `UTIL` cashflows in `WAITING`, `READY`, or `PASTDUE`.
- [[gross-to-util-settlement-update]] applies to `GROSS` or blank-method cashflows subject to status, source-system, FX taxonomy, and event-restriction rules.

In both directions, the cashflow is reinstated for the target settlement path. The UTIL-to-Gross path sets the remaining amount to `0` and has narrowly scoped `PASTDUE` reversal-accounting behavior. The Gross-to-UTIL path sets the payment amount to the remaining amount and derives settlement means from client static data.

The FXU Phase 2 test-case version describes the background as a bidirectional `GROSS` and `UTIL` change and records the explicit tested transition:

```text
GROSS <=> ""
```

That test-case version also treats `UTIL` as an eligible current settlement method, but does not state a complete target-value transition matrix. In particular, it does not establish whether `UTIL` transitions to `GROSS`, blank, or either value. This ambiguity is tracked by [[what-is-the-authoritative-fxu-settlement-method-transition-matrix]]. The explicit functional-requirement direction rules and the test-case version's explicitly recorded `GROSS <=> ""` transition are therefore kept as separate source claims.

## Access and Eligibility

The FXU Phase 2 test-case version requires profile:

```text
RATAN_STRATEGIC_CASHFLOW_BLOTTER:F_Cashflow_Status_Change_Release
```

For that tested flow, eligible records:

- Must not have `data_source_system = Ratan`.
- Must have one of these ISDA taxonomies:
  - `ForeignExchange:Forward`
  - `ForeignExchange:Spot`
  - `ForeignExchange:Swap`

The source defines separate eligibility branches for `GROSS` or blank settlement method and for `UTIL`; the stated status sets differ between those branches. The functional-requirement version further specifies that the `UTIL` branch applies to `WAITING`, `READY`, or `PASTDUE`, while the `GROSS` or blank-method branch is subject to status, source-system, FX taxonomy, and event-restriction restrictions. See [[fxu-utilization-validation]] for the validation context.

## Validation

When the menu is opened, the FXU Phase 2 test-case version records these checks:

1. The requested settlement-method value must differ from the current value.
2. The bulk update is limited to 100 cashflows.

The source does not say whether the 100-cashflow limit is evaluated against the original selection or the trade-expanded set. This is tracked by [[what-is-the-scope-of-the-fxu-bulk-update-limit]].

The functional-requirement version does not establish whether trade-level responses are atomic or support partial success.

## User Visibility and Results

The dialog displays:

- Cashflow identifiers
- Trade identifiers
- Current settlement method
- Payment and status details
- Booking entity
- Counterparty FMCODE
- Currency
- Pay/receive direction
- Value date

Results are sorted by `Trade Id ASC`.

The UI displays insufficient cashflows rather than silently hiding records that do not meet the update condition. Completion feedback is reported at trade level.

## Selection and Execution Scope

Execution is described at cashflow level, while selection expansion and success/failure reporting are described at trade level. The functional-requirement version does not establish whether trade-level responses are atomic or support partial success.

The action should not be treated as a general NSTP bypass. The statement that no special NSTP rule is required is explicitly associated with the UTIL-to-Gross scenario.
