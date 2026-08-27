---
type: concept
title: NSTP Hard-Blocker Bulk Eligibility
created: 2026-08-22
updated: 2026-08-22
tags: [nstp, hard-blocker, bulk-processing, maker-checker, settlement]
related: [nstp, sal-swap-agent-hard-blocker, auto-netting-rule-management, settlement-suppression-exceptions, cashflow-blotter-netting-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Self testing evdience.md"]
---
# NSTP Hard-Blocker Bulk Eligibility

`Bulk Eligible` does not override an NSTP hard blocker.

## Tested behavior

The UAT scenarios tested both configurations:

- `Bulk Eligible` disabled
- `Bulk Eligible` enabled

In both configurations, a cashflow carrying the NSTP hard-blocker exception was not eligible for bulk submission. A selected cashflow or resultant without the hard blocker could continue through the normal process.

This indicates that bulk eligibility is constrained by the exception itself, not solely by the rule-level `Bulk Eligible` setting.

## Control boundary

The safeguard prevents bulk submission of the hard-blocked item, but it does not imply that all actions on the item are unavailable. The source separately reports successful testing of actions such as status changes, Swift suppression, or resultant unnetting in relevant scenarios.

The precise front-end and service-side enforcement points should be confirmed before relying on this behavior as an implementation specification.