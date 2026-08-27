---
type: entity
title: RATAN Cashflow Blotter
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, cashflow-blotter, settlement-operations, workflow]
related: [cashflow-blotter-action-eligibility, maker-checker-settlement-control, cashflow-failure-and-reinstatement, ad-hoc-cashflow-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
---
# RATAN Cashflow Blotter

The RATAN Cashflow Blotter is an operational user interface for performing and reviewing cashflow actions according to cashflow state, sub-state, data attributes, settlement method, user role, and—within BCS—explicit permissions.

The source defines separate FMRP and [[bcs]] blotter action models. It does not establish that their state guards or permissions are shared implementations.

## Responsibilities

- Display cashflow, trade, history, and eligible SWIFT-message details.
- Gate operational actions such as netting, suppression, release, reinstatement, hold, manual settlement, and split handling.
- Support maker/checker exception workflows.
- Expose BCS permissions in the `RATAN_CASHFLOW_BLOTTER` namespace.

See [[cashflow-blotter-action-eligibility]] for the action-gating model.