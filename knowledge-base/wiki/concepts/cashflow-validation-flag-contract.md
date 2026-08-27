---
type: concept
title: Cashflow Validation Flag Contract
tags: [cashflow, validation, uber, ratan, tdsx, boolean-contract]
related: [uber, ratanone, tdsx, tdsx-uber-message-listener, uber-cashflow-validation-filtering, entity-scoped-validation-rollout, what-is-the-authoritative-behavior-for-false-cashflow-validation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Upstream Integration.md"]
---
# Cashflow Validation Flag Contract

## Contract

The upstream `Uber` payload adds the following block:

```json
"cashflowCheckResult": {
  "passed": true
}
```

`passed` is intended to be a Boolean. For an applicable target-FMID message:

- `true` indicates that cashflow validation succeeded and the message may be accepted.
- `false` indicates that validation failed and RATAN drops the particular `Uber` message.

The source does not specify whether the block or field is mandatory, how an absent value is handled, or whether values other than a Boolean are possible.

## Producer behavior

For the March 28 release, `TDSX` checks the actual cashflow validation result only for `EG`, `NP`, and `SA`, corresponding to the three target FMIDs listed in the source. For other entities, TDSX supplies a hardcoded `true`.

Hardcoding `true` prevents the new validation rule from rejecting non-configured entities, but it also means that incomplete cashflows for those entities may not be detected by this flag.

## Open contract boundary

The source does not establish whether `TDSX`, Message Bridge, or RATAN owns the final rejection decision. It also does not define retry, observability, or operational recovery requirements after a message is dropped.

These omissions are tracked in [[what-is-the-authoritative-behavior-for-false-cashflow-validation]].