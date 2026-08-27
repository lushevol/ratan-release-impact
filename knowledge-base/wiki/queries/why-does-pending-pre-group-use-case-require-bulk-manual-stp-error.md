---
type: query
title: Why Does the PENDING_PRE_GROUP Use Case Require a Bulk Manual STP Error?
created: 2026-08-23
updated: 2026-08-23
tags: [manual-stp, pending-pre-group, trade-id, group-blotter, requirement-ambiguity]
related: [bulk-manual-stp, group-blotter-bulk-stp-eligibility, what-is-the-partial-success-contract-for-bulk-manual-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Group Blotter Enhancement.md"]
---
# Why Does the PENDING_PRE_GROUP Use Case Require a Bulk Manual STP Error?

The stated bulk Manual STP rule permits selected cashflows where every selected cashflow's group status is `PENDING_TRADE_VALIDATION` or `PENDING_PRE_GROUP`.

However, Business Use Case 2 selects C3 and C4 in a `PENDING_PRE_GROUP` group and expects a system error. A separate group with the same trade ID contains one received `PENDING` cashflow and one unreceived cashflow.

## Questions to Resolve

- Does eligibility evaluate all groups associated with a trade ID rather than only selected groups?
- Must all cashflows in related groups be received before bulk Manual STP is permitted?
- Is `PENDING_PRE_GROUP` conditionally eligible rather than independently eligible?
- Is the use case erroneous or incomplete?
- What exact error condition and message should operators receive?

Until resolved, the apparent rule cannot be implemented or tested unambiguously. See [[group-blotter-bulk-stp-eligibility]].