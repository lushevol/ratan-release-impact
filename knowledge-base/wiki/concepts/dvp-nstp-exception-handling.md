---
type: concept
title: DVP NSTP Exception Handling
created: 2026-08-23
updated: 2026-08-23
tags: [dvp, nstp, exception-management, cashflow]
related: [auto-dvp, ratan, ssi-exception-state-model, ratan-accounting-status-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# DVP NSTP Exception Handling

DVP NSTP exception handling classifies and controls cashflows held for Delivery versus Payment processing.

For Auto DVP, only exception codes exactly equal to `DVP Strategy` or `DVP` are eligible for automatic closure. A future user-defined code such as `DVP AAA` must not be treated as eligible merely because it contains `DVP`.

The pay cashflow must be in `Waiting` status when RATAN processes a valid linked receipt. Other statuses remain unchanged. Existing production NSTP rule configuration is the source of classification, but its intended pay-only versus pay-and-receive applicability remains unresolved.