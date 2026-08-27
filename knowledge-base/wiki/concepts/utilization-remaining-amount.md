---
type: concept
title: Utilization Remaining Amount
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-balance, fx-utilization, api]
related: [ratan, fxu, blade, fx-utilization, partial-and-pastdue-utilization-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md"]
---
# Utilization Remaining Amount

Utilization Remaining Amount is the unutilized balance held at cashflow level for an eligible FX settlement amount.

The source assigns [[ratan]] responsibility for storing and exposing this balance. [[fxu]] uses it to support further utilization, while [[blade]] uses it when booking a reverse trade.

For full utilization, the amount becomes zero. Under Phase 2 partial utilization, it remains non-zero and is reduced by each accepted utilization; reversal restores it. The source does not specify precision, rounding, tolerance, concurrency controls, or an authoritative balance-calculation algorithm.