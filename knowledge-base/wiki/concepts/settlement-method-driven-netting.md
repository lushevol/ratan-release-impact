---
type: concept
title: Settlement-Method-Driven Netting
created: 2026-08-24
updated: 2026-08-24
tags: [settlement-method, netting, NSTP, frontend-filtering, cash-settlement]
related: [ccil-netting, ccil-cashflow-identification, rule-service, netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md"]
---
# Settlement-Method-Driven Netting

Settlement-method-driven netting uses the `Settlement_Method` classification to determine cashflow treatment, eligibility, and the operational workflow exposed to users.

In the CCIL design, `CCIL` identifies cashflows for special NSTP and netting treatment, while `CASH` identifies the settlement method of the resultant cashflow after CCIL netting. The frontend should expose a settlement-method filter with the values `CASH` and `CCIL Netting`, and should distinguish normal netting from CCIL netting.

This classification is intended to support workflow isolation:

- CCIL candidates are selected under CCIL-specific entity, value-date, currency, and status constraints.
- Normal netting cannot include CCIL cashflows.
- CCIL netting may include different counterparties.
- Existing service-layer netting logic should be reused behind a dedicated CCIL controller and preview flow.

The source does not establish whether settlement-method filtering is only a presentation concern or also an authorization boundary. It also leaves the relationship between `Waiting+IsNettingEligible` and `waiting+pending netting` unresolved.