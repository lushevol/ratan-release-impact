---
type: query
title: What Is the Canonical Released Resultant Amendment Behavior?
tags: [netting-resultant, amendment, lifecycle, rebook-exception, settlement]
related: [released-resultant-amendment-handling, netting-resultant-cashflow-lifecycle, netting-un-net-lifecycle, cashflow-failure-and-reinstatement]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Enhancement on Auto Netting.md"]
---
# What Is the Canonical Released Resultant Amendment Behavior?

When one side of a netting resultant is released and the other side is amended, the source requires that no rebook exception be generated but leaves the solution TBC.

## Questions to resolve

- Is the released resultant retained, reversed, replaced, or reconciled?
- What processing occurs for the amended opposite side?
- Is a rebook exception suppressed, replaced with another event, or converted into an operational workflow?
- Which audit and reconciliation records are mandatory?
- Are there time, payment-status, or market constraints on the permitted remediation?

The answer must define a consistent lifecycle for [[released-resultant-amendment-handling]], rather than only suppressing an exception.