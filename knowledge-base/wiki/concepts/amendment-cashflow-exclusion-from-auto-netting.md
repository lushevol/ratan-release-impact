---
type: concept
title: Amendment Cashflow Exclusion from Auto-Netting
created: 2026-08-24
updated: 2026-08-24
tags: [netting, cashflow, amendment, eligibility, workflow]
related: [auto-netting, netting-service, t-auto-netting-task, what-is-the-authoritative-auto-netting-task-and-amendment-exclusion-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design/Auto Netting design.md"]
---
# Amendment Cashflow Exclusion from Auto-Netting

Amendment cashflow exclusion is the documented rule that amendment cashflows are removed from the collected auto-netting task set before [[auto-netting]] is executed.

The source defines the order of operations but not the meaning of either key term:

- An “amendment cashflow” is not identified by status, version, event, trade relationship, or other criterion.
- “Remove” is not defined as deletion, logical exclusion, task cancellation, state transition, deferral, or routing to another process.
- The subsequent treatment and auditability of removed cashflows or tasks are unspecified.

Accordingly, this concept must not be interpreted as a complete cashflow lifecycle rule or as evidence for behavior in other netting-related processes. The unresolved contract is tracked in [[what-is-the-authoritative-auto-netting-task-and-amendment-exclusion-contract]].