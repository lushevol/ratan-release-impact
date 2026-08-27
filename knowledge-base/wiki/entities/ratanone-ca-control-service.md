---
type: entity
title: ratanone-ca-control-service
tags: [ratan, ca-control, pv-check, postgres, monitoring]
related: [ratanone, pv-check-bypass-risk, what-is-the-impact-and-remediation-status-of-ca-pv-check-bypass, ratan-itrs-alert-triage]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Monitoring/RATAN ITRS Log.md"]
---
# ratanone-ca-control-service

`ratanone-ca-control-service` performs CA control and PV-related processing.

## Findings

The service logged a PostgreSQL length violation because `event_reason` is constrained to `varchar(25)` while the value `REMAINING_PARTY_FULL_NOVATION` is 29 characters. The source explicitly states that the affected trade major version will skip PV checking. This is a functional control defect, not routine monitoring noise.

A separate null `TradeValuation.getTrackingVersion()` caused a `NullPointerException` in `PvServiceImpl.isTradeVersionEqual(PvServiceImpl.java:163)`. The source does not establish whether this failure is related to the schema constraint.
