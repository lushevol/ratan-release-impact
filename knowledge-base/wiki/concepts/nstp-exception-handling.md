---
type: concept
title: NSTP Exception Handling
created: 2026-08-22
updated: 2026-08-22
tags: [nstp, exception-management, cash-settlement, maker-checker, ratan]
related: [ssi-dual-blind-input, settlement-suppression-exceptions, auto-netting-resultant-nstp, comparisons/maker-checker-hard-blocker-operational-levels, settlement-day-2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md"]
---
# NSTP Exception Handling

NSTP exception handling is the process for resolving cashflows that cannot proceed through straight-through processing. The source proposes a consistent model in RATAN:

1. Detect the exception using an identifier, static-data condition, status, or external event.
2. Apply automatic resolution when a configured condition removes the exception.
3. Present a defined manual action when automation is unavailable.
4. Expose a cashflow action or button.
5. Track a sub-status such as Pending Operator or Pending Verification.
6. Apply authority limits and Maker–Checker segregation where required.

The exception inventory spans SSI enrichment, affirmation, netting, bad business days, failed payments, NSTP static criteria, GSAM classification, payment release, DVP, liens, and reversal acknowledgements.

This is a requirements framework rather than confirmation of implemented behavior. Day 1 labels, TBC items, and future-country rollout scope require independent validation.
