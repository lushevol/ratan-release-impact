---
type: concept
title: Murex Cashflow Status Lifecycle
created: 2026-08-22
updated: 2026-08-22
tags: [murex, cashflow-lifecycle, acknowledgement, reversal, replacement]
related: [murex-to-ratan-cashflow-integration, event-driven-component-cashflow-status-management, cashflow-netting-renetting, released-resultant-amendment-handling, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration.md"]
---
# Murex Cashflow Status Lifecycle

The documented source-system lifecycle for a cashflow routed from [[murex]] to [[ratan]] is:

```text
INIT → SNTR → RLSR
```

`INIT` is the Murex-created cashflow state. `SNTR` indicates that Murex sent the flow to RATAN or CashPlatform. `RLSR` is reached after RATAN releases the flow. These are Murex integration statuses; they should not be assumed to represent RATAN's internal lifecycle.

## Reverse-and-new behavior

Murex does not amend an already sent or released cashflow in place. On cancellation and reissue, cancellation, fixing, exercise, early termination, or restructuring, it retains the original `SNTR` or `RLSR` record and creates reversal and replacement flows in `INIT`. Each new flow is evaluated independently for dispatch.

Expiry is an exception in the documented examples: trade expiry at end of the maturity date does not generate reversal or replacement payments.

## Acknowledgement dependency

RATAN should acknowledge each received outbound cashflow. Murex is expected to record the RATAN ID, acknowledgement timestamp, and `Ratan acknowledged` UDF value. Missing acknowledgements after timeout should result in a technical exception.

Past-value-date reversals are a material exception: they may remain for manual Murex handling, leaving RATAN's displayed settlement state inconsistent with Murex. See [[how-are-past-value-date-murex-reversals-reconciled-in-ratan]].