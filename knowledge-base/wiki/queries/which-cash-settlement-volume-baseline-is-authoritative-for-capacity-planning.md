---
type: query
title: Which Cash Settlement Volume Baseline Is Authoritative for Capacity Planning?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, capacity-planning, murex, performance, open-question]
related: [cash-settlement-capacity-planning-baseline, cash-settlement-performance-and-stress-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design.md"]
---
# Which Cash Settlement Volume Baseline Is Authoritative for Capacity Planning?

## Question

Should Cash Settlement capacity be planned against the 2024 forecast maximum of 40,500 records per day or the Murex-derived maximum of 63,720 records per day?

## Evidence

The source converts the forecast maximum to 84.3 records/minute over eight hours. It converts the Murex maximum to 132.7 records/minute over eight hours.

The Murex maximum is higher, but the source does not establish that Murex data covers the complete production workload or that a record maps directly to a unit of platform work.

## Required resolution

Confirm:

- the authoritative source and scope of volume data;
- the meaning of a record;
- business-day and processing-window assumptions;
- expected burst, retry, and downstream amplification factors;
- completion SLA and required headroom; and
- whether the Murex data is complete and production-representative.

Until resolved, retain both figures as distinct candidate baselines and do not treat either as a validated performance commitment.