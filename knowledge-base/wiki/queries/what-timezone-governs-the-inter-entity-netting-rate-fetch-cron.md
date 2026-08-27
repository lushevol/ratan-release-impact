---
type: query
title: What Timezone Governs the Inter-Entity Netting Rate-Fetch Cron?
created: 2026-08-22
updated: 2026-08-22
tags: [query, cron, timezone, FMRP, inter-entity-netting]
related: [inter-entity-netting-spot-rate-retrieval, inter-entity-netting, what-is-the-canonical-auto-netting-job-schedule-and-timezone, ratan]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan New Onboarding Checklist 2026/2026_05_30_CHG0988640_Inter Entity Netting.md"]
---

# What Timezone Governs the Inter-Entity Netting Rate-Fetch Cron?

## Question

Which scheduler timezone governs the FMRP rate-fetch expression, and how does the schedule handle holidays and business dates?

## Evidence

The questionnaire gives the following task expression:

```text
0 0 1 * * TUE-SAT
```

It does not state the scheduler or timezone. The questionnaire separately states business hours as `08:00 - 18:00 GMT`, but that does not prove that the scheduled task runs in GMT.

## Required resolution

Confirm the scheduler implementation, timezone, daylight-saving behavior, holiday calendar, and whether `{date}` represents the calendar date, prior business date, settlement date, or another valuation date. Determine whether the Tuesday–Saturday schedule intentionally retrieves the prior-business-day official end-of-day rate.
