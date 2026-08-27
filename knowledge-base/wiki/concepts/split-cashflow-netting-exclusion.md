---
type: concept
title: Split Cashflow Netting Exclusion
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-splitting, nds, auto-netting, netting-eligibility, exclusion]
related: [cashflow-splitting, pending-nds-netting, nds-auto-netting, netting-eligibility-rules, nds-duplicate-payment-prevention, are-split-child-cashflows-excluded-from-all-netting-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Split Static.md"]
---
# Split Cashflow Netting Exclusion

The Cash Settlement Home Page requirement adds a condition to pending NDS auto-netting rule `7350773637874561024`:

```text
(Cashflow__Splitting_Id == null || Cashflow__Splitting_Id == "")
```

A cashflow with a non-null and non-empty `Cashflow__Splitting_Id` therefore does not match this pending NDS auto-netting rule.

## Scope

The exclusion applies to the pending NDS rule covering these product typologies:

```text
NDS
NDCF
NDFRA
ND CDS Fixing
ND CDS
ND-Convert
NDS Fixing
```

The rule continues to exclude `NDIRS` parent typology, `Reversal` and `Rebook` event reasons, cashflows with an existing netting ID, and cashflows marked by `Cashflow__Duplicate_NDS_FXD`.

This source does not establish that split child cashflows are excluded from manual netting, other NDS rules, NDS Fixing-specific rules, resultant-cashflow processing, or other netting mechanisms. That broader scope remains an open question in [[are-split-child-cashflows-excluded-from-all-netting-rules]].