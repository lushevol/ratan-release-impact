---
type: query
title: What Is the Pending Affirmation Exception Lifecycle and STP Release Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, exception-lifecycle, affirmation, waiting, nstp, stp]
related: [affirmation-driven-cashflow-release, ratan, held-cashflow-reinstatement, dvp-nstp-exception-handling, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--vhh9uf]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation.md"]
---
# What Is the Pending Affirmation Exception Lifecycle and STP Release Contract?

The source states that an accepted user confirmation should close the “pending affirmation” exception and release the cashflow from the NSTP queue. It does not define the authoritative state model.

The contract must establish:

- The formal exception code and whether “Pending Affirmation” is an exception, workflow status, or UI label.
- Entry criteria for a `WAITING` cashflow.
- Allowed transitions following affirmation, rejection, expiry, silence, and manual intervention.
- The post-release cashflow status and queue behavior.
- Atomicity between exception closure and NSTP release.
- Idempotency for duplicate, delayed, or replayed responses.
- Treatment of cashflows amended, withdrawn, failed, cancelled, or settled after email dispatch.
- Payment, SWIFT, accounting, notification, and audit events caused by release.

This question should be resolved before the proposed automation is represented as an established [[ratan]] lifecycle behavior.