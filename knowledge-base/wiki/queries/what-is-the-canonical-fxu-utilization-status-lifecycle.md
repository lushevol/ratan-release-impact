---
type: query
title: What Is the Canonical FXU Utilization Status Lifecycle?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, cashflow, utilization, status-lifecycle, open-question]
related: [fxu-cashflow-utilization, cashflow-utilization-status-lifecycle, cashflow-status-change-event-contract, fx-cashflow-status-write-back]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case.md"]
---
# What Is the Canonical FXU Utilization Status Lifecycle?

The FXU test case requests `UTILIZED`, `PARTIALLY-UTILIZED`, and `PASTDUE` statuses and uses `Ready` as the initial status. It does not define the valid transitions, status ownership, or relationship to `Cashflow.Remaining_Amount`.

## Questions

1. What transitions are valid among `Ready`, `PARTIALLY-UTILIZED`, `UTILIZED`, and `PASTDUE`?
2. Is `PARTIALLY-UTILIZED` determined by a positive remaining amount?
3. Can `PASTDUE` coexist with either utilization status?
4. Which service persists or derives each status?
5. Are status changes published through the existing cashflow event contract or written back to an upstream system?

The answer should be reconciled with [[cashflow-status-change-event-contract]] and [[fx-cashflow-status-write-back]] before the new statuses are added to canonical documentation.