---
type: query
title: What Is the Canonical RATAN eBBS Retry and Idempotency Contract?
tags: [ebbs, ratan, retry, idempotency, open-question]
related: [ebbs-payment-accounting-integration, accounting-posting-lifecycle, accounting-posting-retry-and-exception-handling, ebbs]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - EBBS Accounting.md"]
---
# What Is the Canonical RATAN eBBS Retry and Idempotency Contract?

The requirement says that technical retries reuse the original external-system key and occur at three-minute intervals for a minimum of three attempts. It also says that RATAN automatically resends three times and schedules `HOLD` retries every one or two hours.

The open points are the precise attempt count, timeout duration, response correlation, eBBS duplicate handling, manual-resend behavior, and authoritative duplicate key for `SETTLED` processing.