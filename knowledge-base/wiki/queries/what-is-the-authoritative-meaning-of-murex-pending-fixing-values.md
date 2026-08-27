---
type: query
title: What Is the Authoritative Meaning of Murex Pending-Fixing Values?
created: 2026-08-23
updated: 2026-08-23
tags: [Murex, pending-fixing, IRS, data-contract]
related: [murex-pending-fixing-flag-processing, murex, pending-another-leg-status]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---
# What Is the Authoritative Meaning of Murex Pending-Fixing Values?

The requirement maps `Y` to `Pending Another Leg`, `N` to normal STP processing, and `X` to `Fixing Unknown`. It does not define whether `X` is a provisional business state, a technical default, or another distinct condition.

## Questions to Resolve

- What are all valid values for `Cashflow.Pending_Fixing_flag`?
- Is `X` valid only in UK and DE real-time delivery?
- What validation and exception handling apply to blank, invalid, or changed values?
- Can a cashflow move from `N` back to `Y` after an earlier update?

Resolution is required before implementing a durable Murex flag state model.