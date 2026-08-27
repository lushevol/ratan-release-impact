---
type: concept
title: Cash Settlement OLA Break Monitoring
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ola, monitoring, alerting, operations]
related: [cash-settlement-exception-handling, murex, razor, itrs, ims, cashflow-notification-and-auto-refresh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# Cash Settlement OLA Break Monitoring

Cash Settlement OLA-break monitoring covers delayed or missing cashflows and acknowledgements across Murex, Ratan, and Razor.

## Murex to Ratan

[[itrs]] monitoring in Murex is the preferred real-time control for missing cashflows. [[ratan-pss]] performs second-level group-completeness monitoring: when a group remains `PENDING` for more than five minutes, RATAN PSS alerts Murex PSS for investigation.

The source presents Ratan group monitoring as a safety net, not a replacement for Murex real-time monitoring.

## Ratan to Murex

A Murex status write-back failure is identified through the Murex adaptor log signature:

```text
++++++++Receive ack overtime, flowid and netted resultant cashflow id
```

The runbook calls for ITRS alerting, PSS notification to OPS, and an OPS decision on status replay through Ratan.

## Ratan to Razor

A Ratan-to-[[razor]] OLA break leaves a cashflow in `READY+Pending Ack`. The stated design is to configure Ratan API calls to [[ims]] and notify OPS for possible replay from the cashflow blotter.

Ownership boundaries, alert thresholds, and escalation SLAs are not fully specified. See [[what-is-the-authoritative-ola-monitoring-owner-between-murex-and-ratan]].