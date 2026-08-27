---
type: concept
title: Accounting-Task SOD Recovery
tags: [accounting, recovery, sod, task-processing, oltp]
related: [cash-settlement-accounting-service, oltp-accounting, ebbs, accounting-task-retry-exclusion]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# Accounting-Task SOD Recovery

Accounting-task SOD Recovery is the scheduled regeneration process for accounting tasks in `Hold` status with `payment_date <= current_date`.

The job runs from `06:00` at hourly intervals until `18:00`. For EBBS, it generates a message when `request_info` is empty. For OLTP, it generates a message when `extColumn2` is empty. The routing-specific storage check is essential to avoid applying EBBS recovery logic to an OLTP task.