---
type: stakeholder
title: FMO
created: 2026-08-22
updated: 2026-08-24
tags: [operations, cash-settlement, ratan, maker-checker, business-function, post-trade]
related: [ratan-cashflow-lifecycle-state-machine, maker-checker-settlement-control, ad-hoc-cashflow-netting, swift-versus-cashflow-suppression, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Status Machine.md", "RATAN/RATAN -About App/RATAN -About App.md"]
---
# FMO

FMO is a business and operations function associated with [[ratan]].

According to the RATAN About App source, FMO is the intended user of [[ratan]] for processing and orchestrating trades, cashflows, events, and exception handling.

According to the RATAN lifecycle requirements, FMO is a human actor for non-STP cashflow processing.

## Documented responsibilities

The RATAN lifecycle requirements assign the following responsibilities to FMO:

- An FMO Maker performs manual netting for cashflows in `WAITING / Pending Operator / Pending Netting`.
- An FMO Checker resolves business exceptions in `WAITING / Pending Verification / Pending Exception`.
- Maker/checker workflows apply to manual cashflow suppression, SWIFT suppression, unsuppression, manual settlement, and netting review.

## Organisational definition

Neither source expands the FMO acronym.

The RATAN lifecycle requirements do not identify named team ownership or the currently assigned operational group. The RATAN About App source does not identify accountable owners or define FMO's organisational boundaries. FMO should therefore be treated as a functional designation pending confirmation.