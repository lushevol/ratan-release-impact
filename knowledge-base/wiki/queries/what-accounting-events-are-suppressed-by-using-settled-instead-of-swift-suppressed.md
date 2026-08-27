---
type: query
title: What Accounting Events Are Suppressed by Using SETTLED Instead of SWIFT_SUPPRESSED?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, accounting, settlement, swift-suppressed, duplicate-accounting, ratan]
related: [fmsgw-deletion-driven-cashflow-settlement, ratan, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--198hh9i]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow status sync with FMSGW deletion.md"]
---
# What Accounting Events Are Suppressed by Using SETTLED Instead of SWIFT_SUPPRESSED?

The requirement records a decision to use `SETTLED` rather than `SWIFT_SUPPRESSED` for FMSGW deletion-related outcomes because `SWIFT_SUPPRESSED` may trigger duplicate accounting.

## Decision Needed

Document the concrete accounting behavior for both status transitions:

- accounting events created, suppressed, or retried by each status;
- the duplicate-accounting sequence being prevented;
- the idempotency key or control that prevents repetition;
- reconciliation and operational reporting expectations;
- regression tests required for the status change.

The source gives the business decision but does not provide the accounting-event contract.