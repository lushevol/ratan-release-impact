---
type: concept
title: Trade Lock Status for MO Validation
tags: [trade-lock, middle-office, mo-validation, stella, ratan, trade-control]
related: [ratan-fmrp-stella-interface, ratan-stella-ambassador, fmrp-stella, trade-validation]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (FMRP STELLA)-29126.md"]
---
# Trade Lock Status for MO Validation

## Purpose

Trade-lock status allows Middle Office (MO) users to determine whether a trade or trade package is locked before initiating manual intervention.

## Documented flow

RATAN queries the Stella SDK Booking REST API through the Ratan Stella Ambassador service. The documented endpoint pattern is:

```text
https://sabre-prod-cloud-global.gdc.standardchartered.com//fmrp-stella-ts/prod/getLockStatusByContractId/{contract_id}
```

The source also gives this example:

```text
https://sabre-prod-cloud-1.gdc.standardchartered.com//fmrp-stella-ts/prod/getLockStatusByContractId/5028387294
```

## Returned information

When a lock is present, Stella provides:

- The identity of the user or system holding the lock.
- The lock duration or expiry time.

This information supports a controlled decision about whether manual MO action may proceed.

## Operational limitations

The source does not define lock semantics, stale-response handling, authorization, timeout, retry behavior, or the consequence of a lock-status query failure. The two hostnames and the double slash in the documented paths require validation before operational use.
