---
type: concept
title: Netting Resultant Allotment Default
created: 2026-08-24
updated: 2026-08-24
tags: [netting, allotment, taxonomy, lms, cashflow]
related: [lms, ratan, netting-eligibility-static-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/LMS Feed.md"]
---
# Netting Resultant Allotment Default

The netting-resultant allotment default is an LMS-feed rule for netting across different products.

## Rule

Ratan populates the allotment with:

```text
NETTING RESULTANT
```

only when all of the following conditions hold:

1. The cashflow is a netting-resultant cashflow.
2. The cashflow ID starts with `N*`.
3. The original allotment is blank because the component cashflows came from different products.

If a product taxonomy already exists, it is retained rather than replaced.

## Examples

| Netting type | Resultant cashflow allotment |
| --- | --- |
| Ben BIC Netting, mixed component taxonomy | `NETTING RESULTANT` |
| Ben BIC Netting, same product taxonomy | `CURR|FXD|FXD` |
| Bilateral Netting, same product taxonomy | `COM|SWAP` |
| Bilateral Netting, mixed component taxonomy | `NETTING RESULTANT` |
| NDS Fixing Netting, mixed component taxonomy | `NETTING RESULTANT` |

The value is sent to LMS and consumed successfully in each example documented by the source.