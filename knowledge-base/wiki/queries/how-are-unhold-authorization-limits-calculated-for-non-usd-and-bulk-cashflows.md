---
type: query
title: How Are UNHOLD Authorization Limits Calculated for Non-USD and Bulk Cashflows?
tags: [cashflow, unhold, authorization, usd-limit, bulk-processing]
related: [cashflow-hold-unhold-authorization, cashflow-hold-and-unhold, ratan]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Hold UnHold.md"]
---
# How Are UNHOLD Authorization Limits Calculated for Non-USD and Bulk Cashflows?

The requirement permits an eligible Checker to complete UNHOLD only when the cashflow amount is below the user's USD profile limit. It provides no calculation specification beyond an example where amount 1000 exceeds a profile limit of 100.

## Questions to resolve

- Does “below” mean `<` or `≤` the configured profile limit?
- Which cashflow amount is authoritative: gross, net, settlement, or another amount?
- How are non-USD cashflows converted to USD, including FX rate source and valuation timestamp?
- Are amount limits assessed per cashflow or cumulatively for a bulk request?
- Does a bulk UNHOLD request partially succeed for eligible rows, or fail atomically?
- What user-facing error and audit event are required for denied rows?

A canonical authorization and bulk-execution contract is required for testable implementation.