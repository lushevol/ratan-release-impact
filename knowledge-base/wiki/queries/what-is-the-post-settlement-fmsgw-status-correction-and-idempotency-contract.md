---
type: query
title: What Is the Post-Settlement FMSGW Status Correction and Idempotency Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, settlement, swift, fmsgw, idempotency, status-correction]
related: [fmsgw-deletion-driven-cashflow-settlement, fmsgw, ratan, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--198hh9i]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow status sync with FMSGW deletion.md"]
---
# What Is the Post-Settlement FMSGW Status Correction and Idempotency Contract?

The requirement states when Ratan may move from `RELEASED` to `SETTLED`, but does not define the behavior of later or repeated downstream events.

## Decision Needed

Specify:

- whether duplicate FMSGW status events are idempotent;
- how responses arriving in either order are correlated for MT103/202 COV;
- whether a delayed error after settlement changes the cashflow state;
- how corrected or retracted statuses are processed;
- whether `SETTLED` is irreversible for this workflow;
- handling for pending, missing, and unrecognized component statuses.

This contract is necessary to make [[fmsgw-deletion-driven-cashflow-settlement]] safe under asynchronous downstream delivery.