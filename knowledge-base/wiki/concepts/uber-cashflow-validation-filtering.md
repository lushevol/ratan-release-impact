---
type: concept
title: Uber Cashflow Validation Filtering
tags: [uber, ratan, cashflow-validation, fmid, message-filtering]
related: [ratanone, uber, tdsx, message-bridge, cashflow-validation-flag-contract, entity-scoped-validation-rollout, what-is-the-authoritative-uber-fmid-validation-scope, does-message-bridge-enforce-the-uber-fmid-filter-in-production]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Upstream Integration.md"]
---
# Uber Cashflow Validation Filtering

## Definition

Uber cashflow validation filtering is the proposed RATAN integration behavior that evaluates an upstream `Uber` message according to its `Entity.Booking_Entity_SCI_FMID` and the Boolean `cashflowCheckResult.passed` value.

The March 28 release identifies these target FMIDs:

```text
400007847
401036553
400991880
```

For a target-FMID message, `passed = true` allows processing, while `passed = false` causes RATAN to drop the message.

## Scope and limitations

The source associates the target FMIDs with `EG`, `NP`, and `SA`, but does not document the exact mapping. It also does not conclusively define whether non-target FMIDs are filtered by Message Bridge or merely receive legacy behavior.

The test environment was open to all entities. Consequently, the non-target-FMID test did not prove Message Bridge enforcement. The filter requires independent production or controlled-environment verification, tracked by [[does-message-bridge-enforce-the-uber-fmid-filter-in-production]].

## Ownership questions

The source describes behavior across three components:

- `TDSX` determines or supplies the validation result.
- `Message Bridge` is expected to apply the FMID-based routing or filtering.
- `RATAN` applies the acceptance rule and drops messages when the applicable validation result is not true.

The authoritative ownership boundary remains unresolved.