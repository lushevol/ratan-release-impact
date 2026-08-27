---
type: concept
title: Accounting Posting Lifecycle
tags: [payment-accounting, lifecycle, status-management, ebbs]
related: [ebbs-payment-accounting-integration, ebbs, ratan, accounting-posting-retry-and-exception-handling]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - EBBS Accounting.md"]
---
# Accounting Posting Lifecycle

The accounting posting lifecycle describes how RATAN records an eBBS posting from generation through acknowledgement or exception handling.

## States

- `HOLD`: Generated but waiting for the value-date window.
- `SENT`: Sent to eBBS without a response.
- `SUCCESS`: eBBS consumed the entry and returned an ACK.
- `REJECTED`: eBBS returned an error code.
- `MISSING_INFO`: RATAN could not generate the entry because a mandatory value, especially Nostro data, was unavailable.
- `DISABLED`: A generated entry was invalidated before posting because a reversal scenario occurred.

## Recovery

`HOLD` postings are retried by a scheduled process on value date. No response, timeout, and specified technical errors are automatically retried. Users may manually resend postings in `HOLD`, `SENT`, `REJECTED`, or `MISSING_INFO`.

`REJECTED` and `MISSING_INFO` remediation is described as an out-of-RATAN BAU activity, potentially using [[entities/oscar]].

## Display rule

The blotter examples make `SUCCESS` dominant: once a success response exists for a cashflow ID, a later rejection does not replace the displayed success. This is distinct from a simple latest-response rule and requires separate response history for audit and reconciliation.