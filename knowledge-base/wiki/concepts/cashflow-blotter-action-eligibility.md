---
type: concept
title: Cashflow Blotter Action Eligibility
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-blotter, authorization, state-machine, settlement-operations]
related: [ratan-cashflow-blotter, maker-checker-settlement-control, cashflow-exception-handling, settlement-message-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
---
# Cashflow Blotter Action Eligibility

Cashflow blotter action eligibility is the control model that exposes an operational action only when all applicable conditions are satisfied: main state, sub-state, sub-state type, settlement method, cashflow attributes, selected-row consistency, user role, and permission.

## Distinct Models

The FMRP model frequently excludes `Settlement_Method<> "UTIL"` and contains routing rules for strategic SWIFT processing, BIC/CCIL netting, split cashflows, and manual settlement.

The [[bcs]] model is permission-led. Its controls use permissions such as `RATAN_CASHFLOW_BLOTTER:F_Perform_Ad_Hoc_Netting`, plus conditions including `Pending Operator`, `Pending Verification`, `NSTP Release`, `Un-Net`, `Adhoc SSI Amendment`, and `Adhoc Suppression`.

These are separate functional models and should not be generalized into a single RATAN eligibility rule set.

## Control Implication

The source is clear that eligibility is a guarded workflow mechanism, but it does not identify canonical persisted state values or show enforcement in production. See [[what-are-the-canonical-cashflow-state-and-sub-state-values]].