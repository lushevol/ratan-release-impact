---
type: concept
title: Accounting-Task Retry Exclusion
tags: [accounting, retry, oltp, ebbs, operational-resilience]
related: [oltp-accounting, ebbs, korea-cashflow-migration, accounting-task-sod-recovery, what-is-the-korea-oltp-retry-and-recovery-policy]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# Accounting-Task Retry Exclusion

Accounting-task retry exclusion prevents Korea OLTP tasks from entering the retry job designed for EBBS.

EBBS retries three times at four-minute intervals for absent responses and for `TXN99999` or `TEC0004` responses. The design states that OLTP has no retry mechanism. Consequently, timeout, transport failure, NACK, and manual or automated reconciliation procedures need an explicitly approved operational policy.