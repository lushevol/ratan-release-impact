---
type: query
title: Does CCIL Netting Require Backend Enforcement Separate From Frontend Filtering?
created: 2026-08-24
updated: 2026-08-24
tags: [CCIL, netting, backend-validation, frontend-filtering, controls]
related: [ccil-netting, settlement-method-driven-netting, netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md"]
---
# Does CCIL Netting Require Backend Enforcement Separate From Frontend Filtering?

The design requires the frontend to prevent normal netting from including CCIL cashflows, but it does not state whether the netting service independently rejects invalid combinations.

The open question is whether backend validation must enforce:

- settlement-method homogeneity;
- matching entity, value date, and currency;
- permitted status transitions;
- cross-counterparty authorization for CCIL netting; and
- audit and reconciliation requirements.

Frontend filtering alone should not be assumed to provide a sufficient control boundary for a netting operation.