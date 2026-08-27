---
type: concept
title: Country-Local-Time Accounting Batch Scheduling
created: 2026-08-24
updated: 2026-08-24
tags: [accounting, scheduling, timezone, country-processing, control-m]
related: [control-m, value-date-accounting-feed-cutoff, accounting-feed-file-generation-idempotency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md"]
---
# Country-Local-Time Accounting Batch Scheduling

The proposed accounting-feed schedule is evaluated in local time for each processing country. HK is the only illustrated jurisdiction: generation runs every 30 minutes from 22:05 to 02:05, and an empty-file job runs at 03:30.

The source does not establish how calendars, weekends, holidays, daylight-saving changes, non-HK time zones, or malformed timestamp conversions are handled. The HK examples therefore do not constitute a general time-zone or business-calendar specification.