---
type: query
title: What Are the Correct Dates for Inter-Entity Netting Rule Creation Events?
created: 2026-08-22
updated: 2026-08-22
tags: [inter-entity-netting, netting-rules, data-quality, date-normalization, rollout]
related: [auto-netting-static-go-live-sequencing, inter-entity-netting-coverage-metrics]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter entity Netting - Volume Tracker.md"]
---
# What Are the Correct Dates for Inter-Entity Netting Rule Creation Events?

The tracker includes rule-creation events but contains inconsistent date formats and two year values that conflict with the apparent June–August 2026 reporting sequence.

## Events Recorded as Written

- `06-08-2026` — HK vs CHO netting rule created.
- `6/18/2016` — UK vs TW netting rule created.
- `07-07-2016` — UK vs AG netting rule created.
- `7/15/2026` — DFC vs UK netting rule created.
- `7/31/2026` — UK vs SG netting rule created.
- `7/31/2026` — UK vs Dubai netting rule created.

## Questions to Resolve

- Are the `2016` entries data-entry errors intended to be 2026?
- Does dash-delimited notation use month-day-year or day-month-year?
- Are the final rows `05-08-2026`, `06-08-2026`, and `07-08-2026` intended to mean 5–7 August 2026?
- What are the authoritative expanded identities of HK, CHO, TW, AG, and DFC?
- Which system of record confirms rule creation, enablement, and deployment timestamps?

Do not use these milestones to infer performance causality until dates and entity identities are verified. The events are monitoring context for [[auto-netting-static-go-live-sequencing]], not evidence that a specific rule caused a coverage change.