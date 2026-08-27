---
type: query
title: What Is the Complete Component Cashflow State Model After Withdrawal of a Released or Settled Resultant?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, withdrawal, released, settled, lifecycle]
related: [beneficiary-bic-netting, bic-netting-un-netting, automatic-un-netting-on-trade-market-events, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/03 Beneficiary BIC Netting.md"]
---
# What Is the Complete Component Cashflow State Model After Withdrawal of a Released or Settled Resultant?

For a withdrawal after N1 is `SETTLED` or `RELEASED`, the source says that N1 remains in that state, C1 becomes `WAITING`, and C2 remains `NETTED`. It does not specify C3.

## Questions

- What are the final states and sub-states for C1, C2, and C3?
- What sub-state accompanies C1 becoming `WAITING`?
- Can any returned component be re-netted, settled gross, cancelled, or otherwise processed?
- What accounting, payment, and reconciliation actions occur when withdrawal follows release or settlement?
- Does the result differ between `RELEASED` and `SETTLED`?

The source clearly specifies automatic un-netting only before the resultant reaches either lifecycle boundary; see [[automatic-un-netting-on-trade-market-events]].