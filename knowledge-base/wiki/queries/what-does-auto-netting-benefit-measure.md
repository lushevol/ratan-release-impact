---
type: query
title: What Does Auto Netting Benefit Measure?
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, inter-entity-netting, kpi-definition, data-quality, volume-tracking]
related: [inter-entity-netting-benefit, inter-entity-netting-benefit-trend, settlement-day-2, auto-netting-datetime-calculation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter entity Netting - Volume Tracker/Inter entity Netting - Cash flow benefit.md"]
---
# What Does Auto Netting Benefit Measure?

The volume tracker reports daily values under the label **Auto netting benefit**, but it supplies no definition of the measure.

## Questions to resolve

- What unit does each value represent: payments eliminated, cashflows netted, trades, monetary value, operational workload, or another quantity?
- What formula produces the daily value?
- Does the tracker cover only inter-entity netting, or all auto-netting activity?
- Which source system is authoritative, and what population and statuses are included?
- Are absent dates weekends, holidays, unavailable reporting days, or zero-value days?
- Are the final entries `03-08-2026` through `07-08-2026` intended as 3–7 August 2026?
- Were measurement, scope, static data, or processing changes introduced around the observed peaks?
- What manual or pre-implementation baseline should be used to assess benefit?

## Why it matters

Without these answers, the 14,073 reported units and apparent later-series increase are descriptive observations only. They cannot be safely reported as financial savings, adoption growth, or a validated outcome of [[settlement-day-2]].

The open definition also prevents attribution to particular eligibility criteria in [[netting-eligibility-rules]] or particular resultant-cashflow behavior.