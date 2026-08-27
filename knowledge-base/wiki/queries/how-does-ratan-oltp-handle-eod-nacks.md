---
type: query
title: How Does RATAN-OLTP Handle EOD NACKs?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, oltp, kredmi, eod, nack, accounting]
related: [ratan-oltp-korea-accounting-feed, ratan-accounting-status-lifecycle, kredmi, oltp, 5-ratan--17-ratan-interfaces--14-ratan-and-oltp--2a76vb]
sources: ["RATAN/RATAN -Interfaces/Ratan and OLTP.md"]
---
# How Does RATAN-OLTP Handle EOD NACKs?

## Question

During the 11:30–12:30 KST EOD window, how does RATAN process a NACK returned by KREDMI, and how are unposted accounting entries retried and reconciled?

## Evidence

The source documents this EOD path:

`RATAN → FM Solace → KREDMI → NACK → FM Solace → RATAN`

It does not include OLTP in the EOD flow and does not explain whether the NACK is expected, temporary, retryable, or represented as a particular RATAN accounting status.

## Information needed

- The NACK reason codes and expected frequency.
- RATAN status changes following the NACK.
- Retry timing and post-EOD replay behavior.
- Duplicate-prevention and idempotency controls.
- Reconciliation ownership for entries not posted to OLTP.