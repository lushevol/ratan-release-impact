---
type: query
title: What Is the Canonical Auto-Netting Job Schedule and Timezone?
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, scheduling, controlm, timezone, operations]
related: [controlm, auto-netting-job-time, 26-auto-netting-page-md-files--112-cash-settlement-home-page-cash-settlement-home-page-tech-design-cash-settlem--1o5gc6g]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Auto Netting TechDesign.md"]
---
# What Is the Canonical Auto-Netting Job Schedule and Timezone?

The technical design says the ControlM job should execute every 15 minutes but supplies:

```text
0 */15 * * *
```

The intended cadence cannot be determined without the ControlM scheduling dialect. In standard five-field cron notation, this is not ordinarily an every-15-minute schedule. The operational timezone is also unspecified.

## Required confirmation

- ControlM expression syntax and parser mode;
- intended production cadence;
- scheduler timezone and daylight-saving behavior; and
- monitoring, retry, and missed-run handling.