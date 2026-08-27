---
type: query
title: What Is the Scope of the FXU Bulk Update Limit?
tags: [fxu, bulk-update, cashflow, trade, validation]
related: [settlement-method-update, trade-level-cashflow-update, cashflow-blotter, fxu-utilization-validation, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--20-fxu-technical-design--13-fxu-tes--1jiarro]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/FXU Phase2 Test Case.md"]
---
# What Is the Scope of the FXU Bulk Update Limit?

The FXU Phase 2 test case states that Settlement Method Update has a 100-cashflow bulk-update limit. The same flow automatically expands a partial cashflow selection to all cashflows belonging to selected trades.

## Questions to Resolve

- Is the limit applied to the initial cashflow selection or the expanded trade-level set?
- Is the threshold inclusive of 100 cashflows?
- Does the limit apply per trade, per user action, or per request?
- Are requests above the limit rejected, truncated, split, or displayed as insufficient?
- Is the count evaluated before or after eligibility filtering?

The answer determines whether users can select apparently valid sets that become invalid after [[trade-level-cashflow-update]] expansion.