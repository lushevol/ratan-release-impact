---
type: concept
title: Murex-RATAN Trade-ID Synchronization Gap
tags: [murex, murex-2-11, ratan, trade-id, non-economic-amendment, correlation]
related: [trade-economic-versus-non-economic-update, trade-event-id-lineage, trade-cashflow-reference-linkage, group-pending-validation-monitoring, manual-cashflow-push-from-group-blotter]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Grouping Blotter Monitoring.md"]
---
# Murex-RATAN Trade-ID Synchronization Gap

A Murex-RATAN trade-ID synchronization gap occurs when Murex has a newly amended and validated trade ID while RATAN retains the earlier trade ID.

The source attributes this scenario to a known Murex limitation and gives the example:

```text
RATAN trade ID: 96502251
Murex trade ID: 96522715
```

The change follows a non-economic amendment, so the identifier divergence does not necessarily indicate an economic discrepancy. However, it can prevent automatic cashflow correlation and leave the cashflow in `Pending Trade Validation`.

## Recovery

Operations must manually push the cashflow from the [[group-blotter]] to the Cashflow Blotter. This recovery path differs from a missing Murex payment, where the prescribed action is to follow the Murex DOI and deliver the missing payment to [[ratan]].

The source does not specify the authoritative fallback correlation key or the audit and approval controls for the manual action.