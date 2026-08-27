---
type: concept
title: Split-Child Threshold Redistribution
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-splitting, nostro-threshold, auto-distribution, settlement]
related: [cashflow-splitting, nostro-threshold-matching-precedence, netting-resultant-cashflow, ratan-cashflow-lifecycle-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md"]
---

# Split-Child Threshold Redistribution

A split child that exceeds its applicable nostro threshold is redistributed automatically rather than released as an over-threshold payment.

The tested lifecycle is:

```text
Parent: remains SPLIT
Original child: -> DEAD
Replacement child: generated and linked to the parent
Replacement child: released with SWIFT and accounting output
```

The replacement retains the split-parent relationship, and the split parent amount is reflected in SWIFT field 70 or 72.

This behavior differs from ordinary manual splitting because the threshold check operates on an already-generated child. Related threshold behavior also applies to gross cashflows and netting resultants; see [[concepts/netting-resultant-cashflow]].