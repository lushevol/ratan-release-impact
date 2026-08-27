---
type: concept
title: Cash Settlement Capacity Planning Baseline
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, capacity-planning, performance, volume, murex]
related: [cash-settlement-platform, which-cash-settlement-volume-baseline-is-authoritative-for-capacity-planning, cash-settlement-performance-and-stress-testing, cash-settlement-batch-job-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design.md"]
---
# Cash Settlement Capacity Planning Baseline

The source provides two incompatible workload baselines for Cash Settlement capacity planning.

The 2024 forecast estimates a daily maximum of 40,500 records. At the source's assumed eight-hour processing window, that is 84.3 records/minute; over 24 hours, it is 28.1 records/minute.

The Murex summary reports a daily average of 40,500 records and a daily maximum of 63,720 records. The latter requires 132.7 records/minute over eight hours, or 44.2 records/minute over 24 hours. This peak is approximately 57% higher than the forecast peak rate.

Neither figure is an approved capacity requirement based on the source alone. It does not define the unit represented by “record,” business-day assumptions, target processing window, latency or completion SLA, workload distribution, retry load, or safety headroom. Months 11 and 12 in the Murex table are incomplete.

The 63,720-record daily maximum should be retained as a candidate planning peak pending resolution in [[which-cash-settlement-volume-baseline-is-authoritative-for-capacity-planning]].