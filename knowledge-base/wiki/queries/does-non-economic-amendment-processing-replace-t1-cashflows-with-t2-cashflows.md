---
type: query
title: Does Non-Economic Amendment Processing Replace T1 Cashflows With T2 Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [non-economic-amendment, cashflow, replacement, trade-id, duplicate-payment]
related: [uber-message, non-economic-cashflow-amendment-handling, non-economic-cashflow-suppression, cashflow-lineage-and-operational-visibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Uber Message Analysis.md"]
---
# Does Non-Economic Amendment Processing Replace T1 Cashflows With T2 Cashflows?

## Question

Why does the illustrative non-economic amendment scenario move from withdrawn cashflows under `T1` to replacement new cashflows under `T2`?

## Evidence

The source shows withdrawals for `T1/C1` and `T1/C2`, followed by new cashflows `T2/C3` and `T2/C4`. It does not define the formal replacement linkage or explain whether the trade-ID transition is intentional.

## Required resolution

Confirm the relationship between original and replacement trades, establish the authoritative lineage and duplicate-payment control, and define behavior when withdrawal and replacement events arrive out of order or are retried.