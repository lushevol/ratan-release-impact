---
type: concept
title: Force Gross Review
created: 2026-08-23
updated: 2026-08-23
tags: [force-gross, maker-checker, cashflow, settlement]
related: [cpn-netting, cashflow-netting, entities/cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Tech Design - Draft for now.md"]
---
# Force Gross Review

Force Gross Review is the maker/checker workflow for excluding selected cashflow components from CPN netting and processing them as gross cashflows.

## Workflow

A user may select some components for CPN netting and others for Force Gross in one blotter operation. Force Gross components:

1. Remain associated with their original trades.
2. Move to `Pending`.
3. Receive `Force Gross Review` as the cashflow sub-status type.
4. Expose `Force Gross Approve/Reject`.
5. Move to `Validated` / `Reviewed` after checker approval.

Force Gross components do not receive the CPN Netting ID and are not included in the CPN resultant. The draft does not specify the rejection outcome or whether a rejected component can later be selected for CPN netting without another workflow transition.