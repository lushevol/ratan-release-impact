---
type: query
title: What Is VD in the RATAN-OLTP Accounting Lifecycle?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, oltp, accounting, hold-status, vd]
related: [ratan-accounting-status-lifecycle, ratan-oltp-korea-accounting-feed, 5-ratan--17-ratan-interfaces--14-ratan-and-oltp--2a76vb]
sources: ["RATAN/RATAN -Interfaces/Ratan and OLTP.md"]
---
# What Is VD in the RATAN-OLTP Accounting Lifecycle?

## Question

What does `VD` represent, and what event, dependency, or validation condition must occur before an accounting entry can leave `HOLD` status?

## Evidence

The source defines `HOLD` as an accounting entry that has been generated but has not “reached VD yet,” so posting is held. No definition of `VD` or release criteria is provided.

## Information needed

- The expansion and system role of `VD`.
- The event that marks an entry as having reached VD.
- Whether `HOLD` is automatic, manually released, timeout-driven, or terminal.
- The operational owner and monitoring procedure for prolonged `HOLD` entries.