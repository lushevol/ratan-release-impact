---
type: concept
title: Cashflow Unsplit
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-splitting, unsplit, settlement, lifecycle]
related: [cashflow-splitting, ratan-cashflow-lifecycle-state-machine, netting-un-net-lifecycle, split-amount-amendment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md"]
---

# Cashflow Unsplit

Unsplit reverses a split when none of the child cashflows has been released.

## Eligible unsplit

The user may select unsplit from the parent or a child. After confirmation:

```text
Parent: SPLIT -> WAITING with an unsplit exception
Children: -> DEAD
```

The confirmation window displays parent and child cashflow information before the operation is confirmed.

## Ineligible unsplit

If any child has been released, unsplit is rejected. The confirmation dialog highlights the released child and Ratan reports that the cashflow is not eligible for unsplit.

This restriction prevents the system from reversing a split after downstream SWIFT, accounting, or lifecycle effects have already been produced.