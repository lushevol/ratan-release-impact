---
type: query
title: What Is the Canonical CCIL Resultant Cashflow Lifecycle?
created: 2026-08-22
updated: 2026-08-22
tags: [CCIL, resultant-cashflow, lifecycle, FMRP, auto-netting, open-question]
related: [ccil-guaranteed-and-non-guaranteed-netting, ccil-settlement-method-stamping, cashflow-logical-model, ratan, fmrp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CCIL Netting.md"]
---
# What Is the Canonical CCIL Resultant Cashflow Lifecycle?

## Question

What is the authoritative settlement-method, status, exception, SWIFT, and accounting lifecycle for CCIL resultants across manual CCIL Netting and FMRP 8.0 auto netting?

## Evidence Requiring Reconciliation

The source specifies several different stages:

- Eligible input cashflows use `Settlement Method = CCIL`.
- A manually generated non-guaranteed CCIL-netting resultant uses `Settlement_Method = CASH` and `Delivery_Method = CASH`, with state `QUEUED`.
- FMRP 8.0 IRS-netting intermediates `N1` and `N2` are expected to become `Pending Auto Netting`, then `DEAD`.
- The final `N3` is shown as `Gross`, `WAITING + Pending Exception`, and associated with `Auto Netting - INO IRS`.
- The background requires SWIFT suppression for CCIL netting resultants while retaining accounting.

## Clarifications Needed

The responsible teams should establish:

1. whether manual and automated resultants share one canonical state model;
2. when `CCIL`, `CASH`, and `Gross` are assigned and whether these values represent different lifecycle stages;
3. which component suppresses SWIFT automatically or requires manual action;
4. when accounting is generated;
5. who resolves the final `N3` exception;
6. how N1/N2 termination is reconciled to N3 creation.