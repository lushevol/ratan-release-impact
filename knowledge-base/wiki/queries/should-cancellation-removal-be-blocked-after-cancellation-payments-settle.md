---
type: query
title: Should Cancellation Removal Be Blocked After Cancellation Payments Settle?
created: 2026-08-23
updated: 2026-08-23
tags: [cancellation-removal, settlement-status, murex, ratan, payment-lifecycle, exception-handling]
related: [murex, ratan, cashflow-status-lifecycle, reversal-and-correction-cashflow-processing, cashflow-withdrawal-and-new, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--28-m--1b3wu0h]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Murex Trade & Cashflow Events.md"]
---
# Should Cancellation Removal Be Blocked After Cancellation Payments Settle?

## Question

When a trade was booked, cancelled, and has cancellation-related payments that are already settled, is cancellation removal permitted? If it is permitted in [[murex]], what downstream settlement treatment must [[ratan]] apply?

## Distinctions to resolve

- Murex business permissibility versus Ratan downstream acceptance policy.
- The relevant settlement state: cashflow status, payment status, or confirmation of external settlement.
- Whether already settled payments require a reversal, correction, adjustment, compensating payment, or manual exception.
- Required approvals, controls, and audit evidence for any post-settlement correction.
- Whether cancellation removal is rejected, blocked, queued, or processed with a distinct exception path.

## Evidence and boundary

The cited deprecated note asks whether cancellation removal “will be blocked” if cancellation payments are settled. It provides no answer and must not be read as evidence of an implemented blocking rule.