---
type: concept
title: Manual Cashflow Netting
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, netting, operations, manual-processing, settlement-ops]
related: [ratan, settlement-ops, netting-eligibility-rules, dvp-nstp, ad-hoc-cashflow-netting, what-is-the-ratan-nstp-hold-and-release-lifecycle-for-netting-eligible-cashflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Rules Static Data.md"]
---
# Manual Cashflow Netting

Manual cashflow netting is the documented CN Day 1 operational flow in which [[settlement-ops]] filters pending-netting cashflows and manually performs netting.

In this flow, [[netting-eligibility-rules]] first determine whether a cashflow is eligible and should be held as NSTP in [[ratan]]. The source does not state the exact NSTP state or sub-state, the selection criteria used by Settlement Ops, approval steps, result creation, or how a hold is released.

## Distinction from Auto Netting

The source explicitly excludes auto netting from CN Day 1. It therefore provides no evidence that an EOD auto-netting job is active for this scope.

Manual cashflow netting is not assumed to be equivalent to [[ad-hoc-cashflow-netting]]; the source only specifies a pending-netting filter and a manual operational action.