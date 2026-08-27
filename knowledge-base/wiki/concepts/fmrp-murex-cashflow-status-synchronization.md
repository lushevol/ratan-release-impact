---
type: concept
title: FMRP Murex Cashflow Status Synchronization
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, murex-211, cashflow-lifecycle, status-synchronization, integration]
related: [scb-fmrp-dbf, fmrp, murex-211, cashflow-lifecycle-state-model, fmrp-cashflow-responsibility-split, what-replaced-the-legacy-fmrp-inbound-acknowledgement-status-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md"]
---
# FMRP Murex Cashflow Status Synchronization

FMRP status synchronization is the Murex 2.11 configuration pattern that conditionally persists and publishes payment-flow changes through [[scb-fmrp-dbf]].

## Legacy outbound transitions

`client.scb.fmrp.SyncStatus` applies the following behavior:

- `FAIS` or `I2SR` with an `INIT` record changes the record to `SENT` and publishes.
- `FMSI` with a `SENT` record changes the record to `CANC` and produces cancellation output.
- `FMIS` with a `CANC` record changes the record to `SENT` and publishes.
- `FMIS` or `I2SR` with no record inserts a `SENT` record and publishes.
- `FMIS` with an `INIT` record changes the record to `SENT` and publishes.
- Other conditions are discarded.

This is a source-specific implementation of the broader [[cashflow-lifecycle-state-model]]. It should not be generalized to other cashflow routes without supporting evidence.

## Legacy inbound acknowledgement

The older inbound workflow validated a flow ID, a `razorID` source value, and record existence before setting `M_STATUS='MATH'`, persisting `M_RATAN_ID`, and recording `M_REC_DATETIME`.

This behavior is superseded within the source by RATAN-10822, which removes the related router and formulas. The replacement state model is undocumented in the supplied material. Therefore, `MATH` is historical evidence rather than a confirmed current state.

## Reliability boundary

The source shows separate existence checks and updates/inserts but provides no unique key, transaction scope, or concurrency rule for `M_FLOW_ID`. It establishes intended configuration behavior, not demonstrated runtime idempotency or production deployment.