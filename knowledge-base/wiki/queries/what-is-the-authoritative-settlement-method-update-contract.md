---
type: query
title: What Is the Authoritative Settlement Method Update Contract?
tags: [open-question, settlement-method, cashflow, RATAN, cashflow-blotter]
related: [settlement-method-update, util-to-gross-settlement-update, gross-to-util-settlement-update, ratan, cashflow-blotter]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Settlement Method Update.md"]
---
# What Is the Authoritative Settlement Method Update Contract?

The source describes a bidirectional Settlement Method Update but leaves important contract details unresolved.

## Questions

1. What does `READY + NA + NA` mean in the Gross-to-UTIL eligibility condition?
2. Is blank settlement method (`""`) a valid eligible state, or does it identify legacy or incomplete data?
3. Does the 100-item limit apply to trades, cashflows, or whichever limit is reached first?
4. What happens when a trade contains both eligible and ineligible cashflows?
5. Is processing atomic at trade level, or can cashflows partially succeed?
6. What fields and error codes are returned in the trade-level response?
7. Are filtered `+ERROR` cashflows excluded before trade expansion, after expansion, or both?
8. How are duplicate or repeated update actions handled?
9. What does “reinstate” mean operationally in RATAN: a status transition, event generation, version creation, or re-queuing?
10. Is “post settle” a settlement event, an accounting posting, a final settlement state, or an external settlement instruction?

Until these questions are resolved, the two directional rules should remain separate and the source's status expressions should not be normalized.