---
type: concept
title: UTIL Settlement Method
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, settlement-method, util, fxu]
related: [fxu, fxu-cashflow-utilization, cashflow-blotter, static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case.md"]
---
# UTIL Settlement Method

`UTIL` is the settlement-method value that the FXU test case requires in the cashflow blotter. The test setup describes the value as `Util`, so the source does not establish whether `Util` is a display label for the canonical `UTIL` value or whether the values are distinct.

## Documented requirement

The cashflow blotter must support `UTIL` as a settlement method. Cashflows using this method must not expose or permit the actions listed in [[fxu-cashflow-utilization]].

The source does not define:

- The authoritative static-data owner.
- The persistence location or enumeration contract.
- Whether the value is valid for all cashflows or only FXU cashflows.
- Whether the value is exposed through GraphQL, events, or downstream write-back.
- Whether action restrictions are enforced server-side.

## Distinction from settlement means

`UTIL` is a cashflow settlement-method value. It is separate from the requested Vostro settlement-means value `FXBRREC-M`. The source does not specify whether `FXBRREC-M` is valid only with `UTIL`.