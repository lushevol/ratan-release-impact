---
type: concept
title: Trade-Level Cashflow Selection Expansion
tags: [cashflow-blotter, trade, cashflow, bulk-update, user-interface]
related: [cashflow-blotter, settlement-method-update, trade-cashflow-reference-linkage]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Settlement Method Update.md"]
---
# Trade-Level Cashflow Selection Expansion

Trade-level cashflow selection expansion is the Cashflow Blotter behavior in which selecting one cashflow automatically displays or selects all cashflows belonging to the same trade.

For Settlement Method Update, this creates a distinction between:

- **Execution granularity:** the requirement describes the update as operating at cashflow level.
- **Interaction and response granularity:** selection warnings and success/failure feedback are handled at trade level.

The specified UI behavior is:

- Results are ordered by trade ID.
- Cashflows with status `+ERROR` are filtered out.
- Bulk update is limited to 100 trades/cashflows.
- A warning is shown when the selected cashflow count differs from the frontend feedback cashflow count.
- The system warns when it automatically selects all cashflows under trades such as `T01` and `T02`.

The source does not clarify whether the 100-item limit applies to trades, cashflows, or whichever count is reached first. It also does not define behavior when a trade contains both eligible and ineligible cashflows.