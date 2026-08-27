---
type: query
title: What Is the Approved Ratan Indonesia Time-Zone Model?
created: 2026-08-22
updated: 2026-08-22
tags: [time-zone, utc-plus-7, scheduling, indonesia, ratan]
related: [ratan-id, indonesia-cash-settlement-onshoring, cashflow-netting-renetting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# What Is the Approved Ratan Indonesia Time-Zone Model?

Ratan ID servers and databases are expected to default to UTC+7. The source identifies possible effects on netting, accounting, and release schedules; timestamp-filtered queries; and upstream messages carrying timestamp attributes.

The approved model must specify time-zone treatment for application processes, databases, schedulers, stored timestamps, timestamp comparisons, user-facing displays, reporting, daylight-saving behavior in cross-region services, and recovery/replay processes.

The cited child design is not included in the ingested source, so no mitigation or approval can be inferred.