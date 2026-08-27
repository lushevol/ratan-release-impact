---
type: entity
title: ControlM
created: 2026-08-22
updated: 2026-08-22
tags: [scheduler, batch-processing, cash-settlement, auto-netting]
related: [auto-netting-job-time, what-is-the-canonical-auto-netting-job-schedule-and-timezone]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Auto Netting TechDesign.md"]
---
# ControlM

ControlM is the scheduled-execution dependency proposed for the cash-settlement auto-netting job.

The technical design states that a new job should execute every 15 minutes and provides:

```text
0 */15 * * *
```

This expression must not be treated as confirmed every-15-minute scheduling until the ControlM expression dialect and applicable timezone are verified. In five-field cron syntax, it can have a materially different interpretation.