---
type: query
title: What Is the Korea OLTP Retry and Recovery Policy?
tags: [oltp, retry, recovery, accounting, open-question]
related: [accounting-task-retry-exclusion, accounting-task-sod-recovery, oltp-ack-nack-processing, oltp-accounting]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# What Is the Korea OLTP Retry and Recovery Policy?

OLTP tasks are excluded from the EBBS retry job and have no documented retry mechanism. The SOD job can regenerate missing OLTP payloads for eligible `Hold` tasks, but it does not specify recovery after a sent request receives no response, a normal NACK, an EOD timeout NACK, or a transport failure.

The policy needs approved task-status mappings, retry or replay ownership, duplicate-message safeguards, escalation expectations, and reconciliation controls.