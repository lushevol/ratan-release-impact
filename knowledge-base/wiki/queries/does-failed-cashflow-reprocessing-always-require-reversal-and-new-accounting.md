---
type: query
title: Does Failed Cashflow Reprocessing Always Require Reversal-and-New Accounting?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, cashflow, accounting, reversal-and-new, reprocessing]
related: [failed-cashflow-accounting, reversal-and-correction-cashflow-processing, cashflow-withdrawal-and-new, cashflow-event-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Cashflow Accounting.md"]
---

# Does Failed Cashflow Reprocessing Always Require Reversal-and-New Accounting?

## Question

Does simple re-processing of an unchanged failed cashflow require reversal-and-new accounting, or is reversal-and-new limited to a trade amendment or cancellation after the initial accounting?

## Evidence

The requirement prose associates reversal-and-new or reversal accounting with a latest cashflow event created by a trade amendment or cancellation. However, the normal re-processing table shows `Y(Reversal &New)` even though the event remains `New` and no amendment or cancellation is listed.

## Why It Matters

The answer determines whether a retry creates a correction to the original Value Date accounting, whether a second accounting action is required, and how accounting dates and audit history should be recorded.

## Current Position

Unresolved. The normal-case table and the prose requirement should not be treated as fully consistent until the accounting contract is confirmed.