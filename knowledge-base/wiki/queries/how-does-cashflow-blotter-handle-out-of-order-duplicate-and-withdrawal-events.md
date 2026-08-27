---
type: query
title: How Does Cashflow Blotter Handle Out-of-Order, Duplicate, and Withdrawal Events?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, lifecycle, withdrawal, audit-history, open-question]
related: [cashflow-blotter, cashflow-lifecycle-supersession-and-audit-history, ratan, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--26-cn-settlement-demo-se--10ylmrb]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 17.md"]
---
# How Does Cashflow Blotter Handle Out-of-Order, Duplicate, and Withdrawal Events?

Sprint 17 requires Cashflow Blotter to display only the latest Amendment or Withdrawal while retaining New plus the later event in Cashflow History Page. It does not define how “latest” is determined or how exceptional event delivery is handled.

## Questions to Resolve

- Is lifecycle ordering determined by source sequence, business effective time, event timestamp, or RATAN receipt time?
- How are duplicate New, Amendment, and Withdrawal messages identified and handled?
- What fields and status are displayed for a withdrawn cashflow?
- Is history immutable and complete when messages arrive out of order?
- What happens when a lifecycle event is received for a netted or un-netted cashflow?

## Evidence Needed

Obtain event-schema documentation, lifecycle correlation rules, Cashflow Blotter display specifications, and test evidence covering delayed, duplicate, and post-netting lifecycle events.