---
type: query
title: What Happens When a Floating IRS Leg Arrives After the Fixed Leg Is Manually Netted with Other Products?
created: 2026-08-23
updated: 2026-08-23
tags: [IRS, CDS, manual-netting, amendments, resultant-lineage]
related: [pending-another-leg-status, irs-fixed-floating-leg-netting, irs-refixing-unnetting-and-renetting, cashflow-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---
# What Happens When a Floating IRS Leg Arrives After the Fixed Leg Is Manually Netted with Other Products?

The requirement permits a fixed IRS coupon in `WAITING` / `Pending Another Leg` to be manually netted with CDS cashflows before its floating-leg counterpart is received. It does not define the subsequent lifecycle.

## Questions to Resolve

- Must RATAN automatically un-net the cross-product resultant when the floating leg arrives?
- Is the incoming floating leg held, manually remediated, or combined into a revised resultant?
- How are client affirmation, authorization, accounting, and audit records preserved?
- Does the answer differ when the manual resultant has been released or settled?
- What prevents duplicate settlement of the preliminary fixed leg and the later IRS net amount?

Resolution is necessary before enabling this manual-netting path operationally.