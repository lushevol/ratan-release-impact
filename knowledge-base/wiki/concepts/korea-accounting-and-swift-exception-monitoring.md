---
type: concept
title: Korea Accounting and SWIFT Exception Monitoring
created: 2026-08-23
updated: 2026-08-23
tags: [korea, accounting, swift, exception-monitoring, cashflow-dashboard]
related: [ratan, oltp, enisis, ops, accounting-posting-lifecycle, accounting-posting-statuses, accounting-posting-retry-and-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md"]
---
# Korea Accounting and SWIFT Exception Monitoring

The Korea operating guide defines two Cashflow Dashboard monitoring paths in [[ratan]].

## Accounting errors

Users select `Accounting Error` and filter yesterday, today, and tomorrow by accounting status:

- `SENT`
- `REJECTED`
- `MISSING_INFO`

Users inspect an item's `Accounting Detail` tab for accounting information, status, and reason. [[ops]] is expected to process the identified accounting items in [[oltp]].

The source does not identify whether `SENT` is terminal, retryable, pending acknowledgement, or otherwise an error condition.

## SWIFT errors

Users select `Swift Error` and filter for SWIFT errors over yesterday, today, and tomorrow. `FinalCancelled` is identified as a NACK status from [[enisis]].

The prescribed response is exception-blotter processing or replay in ENISIS. The guide does not specify replay authorization, idempotency, or confirmation requirements.