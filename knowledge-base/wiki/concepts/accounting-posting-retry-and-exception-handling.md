---
type: concept
title: Accounting Posting Retry and Exception Handling
tags: [payment-accounting, retry, exceptions, ebbs]
related: [accounting-posting-lifecycle, ebbs-payment-accounting-integration, ebbs, ratan]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - EBBS Accounting.md"]
---
# Accounting Posting Retry and Exception Handling

RATAN is expected to retry accounting postings when eBBS does not respond or returns specified technical exceptions.

## Retry paths

- Scheduled retry for `HOLD` postings: every one or two hours on value date.
- Automatic retry for no response, timeout, `TXN9999`, and `TEC0004`.
- Manual GUI resend for `HOLD`, `SENT`, `REJECTED`, and `MISSING_INFO`.
- PSS retry through an exposed API after a user raises a support ticket.

The technical design requires reuse of the original external-system key for technical retries and states a minimum of three attempts at three-minute intervals.

## Unresolved contract

The requirement does not establish whether “resend three times” means three total attempts or three retries after the original attempt. It also does not specify timeout duration, response correlation, idempotency enforcement in eBBS, or the exact scheduled interval between one and two hours.