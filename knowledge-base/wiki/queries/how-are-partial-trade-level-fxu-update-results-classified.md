---
type: query
title: How Are Partial Trade-Level FXU Update Results Classified?
tags: [fxu, trade, cashflow, partial-success, notification]
related: [trade-level-cashflow-update, settlement-method-update, cashflow-blotter, does-mvp-support-partial-fx-utilization, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--20-fxu-technical-design--13-fxu-tes--1jiarro]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/FXU Phase2 Test Case.md"]
---
# How Are Partial Trade-Level FXU Update Results Classified?

The Phase 2 test case exposes insufficient cashflows at cashflow level but reports success and failure through trade-level responses and notifications.

## Questions to Resolve

- If some cashflows in a trade are ineligible, can eligible cashflows still be updated?
- Is an update atomic per cashflow, per trade, or per complete request?
- How is a trade with both successful and failed cashflow updates represented in the response?
- Does an insufficient cashflow prevent the whole trade from being submitted?
- What notification and audit data identify individual cashflow outcomes behind a trade-level result?

The test evidence confirms both cashflow-level insufficiency display and trade-level reporting, but does not define their aggregation or transaction semantics. This affects interpretation of [[does-mvp-support-partial-fx-utilization]].