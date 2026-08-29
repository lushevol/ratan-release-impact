---
type: concept
title: Released Resultant Amendment Handling
tags: [cashflow-auto-netting, netting-resultant, amendment, rebook-exception, lifecycle]
related: [netting-resultant-cashflow, netting-resultant-cashflow-lifecycle, netting-un-net-lifecycle, pending-auto-netting-state, cashflow-failure-and-reinstatement, rebook-cashflow-netting-exclusion, what-is-the-canonical-released-resultant-amendment-behavior]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Enhancement on Auto Netting.md"]
---
# Released Resultant Amendment Handling

Released resultant amendment handling concerns the asymmetric case in which one side of a [[netting-resultant-cashflow]] has been released and the other side is subsequently amended.

## Required outcome

The source states that the amendment on the opposite side should not generate a rebook exception.

## Unresolved lifecycle behavior

The source marks the solution as TBC. Suppressing a rebook exception is not, by itself, a lifecycle solution. The operating model must establish whether the system:

- retains the released resultant unchanged;
- reverses or un-nets a component where permitted;
- creates a replacement cashflow or resultant;
- re-nets the amended side; or
- records a controlled reconciliation or operational exception.

Any exception suppression should preserve an auditable record and must not conceal a settlement mismatch. This scenario should be evaluated against [[netting-resultant-cashflow-lifecycle]], [[netting-un-net-lifecycle]], and cashflow failure and reinstatement.