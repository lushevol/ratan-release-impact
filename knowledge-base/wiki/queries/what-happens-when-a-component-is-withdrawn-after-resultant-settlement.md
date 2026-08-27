---
type: query
title: What Happens When a Component Is Withdrawn After Resultant Settlement?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, bilateral-netting, withdrawal, settlement-finality, accounting]
related: [bilateral-netting, netting-withdrawal-timing, netting-resultant-cashflow-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md"]
---
# What Happens When a Component Is Withdrawn After Resultant Settlement?

The requirement states that when a component is withdrawn after the resultant is `SETTLED` or `RELEASED`, the resultant remains in that state, the withdrawn component is `WAITING`, and another component remains `NETTED`.

## Open issues

- Is the resultant economically valid after removal of one component?
- Is a reversal, adjustment, replacement, or exception generated?
- Can the withdrawn component be processed independently?
- How are accounting entries and payment records corrected?
- How are the original component, resultant, and withdrawal linked in audit history?
- Are `RELEASED` and `SETTLED` materially different for this workflow?

This is the highest-priority unresolved bilateral-netting behavior because it affects settlement finality, accounting, and operational recovery.