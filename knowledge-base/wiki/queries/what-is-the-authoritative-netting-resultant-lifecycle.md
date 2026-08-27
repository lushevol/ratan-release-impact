---
type: query
title: What Is the Authoritative Netting Resultant Lifecycle?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, cashflow-netting, lifecycle, status-model, operational-risk]
related: [settlement-netting-validation-generation, netting-resultant-cashflow, netting-un-net-lifecycle, cashflow-lifecycle-versioning, cashflow-auto-netting, maker-checker-settlement-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Settlement Netting Validation Generation.md"]
---
# What Is the Authoritative Netting Resultant Lifecycle?

## Question

What is the approved lifecycle and persistence model for a netting resultant from creation through checker review, release, failure, un-netting, and trade-amendment reversal?

## Evidence requiring resolution

The requirement identifies the intended ordinary path as:

```text
Queued -> Pending / Netting / Pending Verification
        -> Validated
        -> Released
```

It identifies ordinary checker un-netting as:

```text
Resultant -> DEAD
Components: Netted -> Queued
```

However, the same source contains unresolved or inconsistent details:

- `Reject Netting` and `Un-Net` are not clearly distinct.
- `Dead` and `DEAD` are both used.
- Resultant NSTP workflow fields are required for review but mapped as blank.
- A failed resultant has no defined accounting or reconciliation process.
- Trade amendment reversal introduces `Suppressed`, `Pending Reversal`, cancellation, and version increments.
- A resultant cashflow ID is described with both 12-character and 16-character limits.
- Mixed-product netting inherits the product from the first component.
- The release race for `Validated` components is not specified.

## Required decision

The owning teams should approve:

1. Canonical status and sub-status enums.
2. Atomic validation and release-boundary behavior.
3. The difference between rejection and un-netting.
4. Resultant product and SSI selection rules.
5. Failed-resultant accounting and reconciliation.
6. Trade-amendment cancellation ownership and successor-flow sequencing.
7. The authoritative cashflow ID length constraint.
8. Rounding behavior.

Until resolved, the source should be treated as a functional design with implementation risks rather than a signed-off lifecycle contract.