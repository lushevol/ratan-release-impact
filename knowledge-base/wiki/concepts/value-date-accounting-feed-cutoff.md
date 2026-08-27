---
type: concept
title: Value-Date Accounting-Feed Cutoff
created: 2026-08-24
updated: 2026-08-24
tags: [accounting, value-date, batch-processing, cash-settlement]
related: [country-local-time-accounting-batch-scheduling, accounting-feed-file-generation-idempotency, aspire, ebbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md"]
---
# Value-Date Accounting-Feed Cutoff

The proposed accounting-feed design holds a cashflow’s feed work until its value date has arrived. Once value-date eligibility has been reached by the local 22:05 processing threshold, the work is intended to be published in a batch file.

The source states a task-selection condition of payment date no later than the current date and `create_time` before 22:00 on that date. It does not define treatment of tasks created at exactly 22:00 or in the interval before a later scheduled run.