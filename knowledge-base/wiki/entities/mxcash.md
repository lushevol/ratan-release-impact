---
type: entity
title: MxCash
created: 2026-08-22
updated: 2026-08-22
tags: ["upstream-system", "cashflow-source", "netting", "razor", "cashflow-id", "cash-settlement"]
related: ["ad-hoc-cashflow-netting", "ratan-cashflow-blotter", "ratan", "ratan-cashflow-id-management"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Cashflow & Payment cashflow id management.md"]
---
# MxCash

MxCash is an upstream TP system described as supplying Razor cashflow IDs to [[ratan]]. The requirement assigns these IDs an `R` prefix to denote a Razor cashflow.

Ratan converts a source ID of maximum length 10 into a 12-character ID by zero-padding after the `R` prefix.

```text
1234567    -> R00001234567
1234567890 -> R01234567890
```

The source does not specify handling for invalid or overlength MxCash source IDs.