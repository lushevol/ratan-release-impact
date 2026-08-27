---
type: query
title: What Are the RATAN-OLTP Accounting Status Transitions?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, oltp, accounting, status-lifecycle, reconciliation]
related: [ratan-accounting-status-lifecycle, ratan-oltp-korea-accounting-feed, how-does-ratan-oltp-handle-eod-nacks, 5-ratan--17-ratan-interfaces--14-ratan-and-oltp--2a76vb]
sources: ["RATAN/RATAN -Interfaces/Ratan and OLTP.md"]
---
# What Are the RATAN-OLTP Accounting Status Transitions?

## Question

Which transitions are valid among `HOLD`, `DISABLED`, `SENT`, `SUCCESS`, `REJECTED`, and `MISSING_INFO`, and which statuses are terminal, retryable, or manually remediated?

## Evidence

The source defines individual status meanings but does not provide a state-transition model, timeout thresholds, retry rules, or reconciliation workflow. It also does not state how a KREDMI EOD NACK is represented.

## Information needed

- A transition diagram or state machine.
- Entry criteria and exit criteria for every status.
- Timeout handling for `SENT`.
- Retry and correction rules for `REJECTED`.
- Separate reason codes and remediation paths for `MISSING_INFO`.
- The status assigned after an EOD NACK.