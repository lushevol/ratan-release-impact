---
type: concept
title: SWIFT Status Lifecycle and Reconciliation
created: 2026-08-23
updated: 2026-08-23
tags: [swift, status, reconciliation, cashflow, settlement]
related: [ratan-swift-message-generation, cashflow-lifecycle-state-machine, fmswiftgateway, fmsre, enisis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# SWIFT Status Lifecycle and Reconciliation

The FMRP SWIFT-generation requirement overlays operational SWIFT statuses on RATAN cashflow statuses. These dimensions must not be treated as synonymous.

## Status dimensions

- Cashflow status: primarily `READY`, `RELEASED`, and `SETTLED`.
- Cashflow sub-status: includes `Pending Ack`.
- SWIFT status: includes `Pending FMSGW Ack`, `Pending FMSRE Ack`, `Pending Manual Rel`, `FMSGW Error`, `AMH Error`, and downstream release labels.
- SWIFT status reason: a returned description or a reconciliation instruction.

A generation failure is stated to leave the cashflow `READY` with `Pending Ack` and `Ratan Internal Error`, before an EOD job changes it to `FAILED`. The requirement does not define the `FAILED` lifecycle, owner, recovery path, or retry semantics.

## Dual-message COV reconciliation

MT103/202 COV creates two independently dispatched messages. RATAN should use the standard mapping only where both returned statuses match. When they differ, the UI must direct the operator to `Check in FMSGW` or `Check in FMSRE`, depending on route.

## Manual-deletion risk

`FMSGW Deleted`, `FMSRE Deleted`, and `Manual Delete` map to `SETTLED` while payment is expected to be made manually through Oscar or AMH. Therefore, this status may mean RATAN workflow closure rather than verified payment completion.

This business-facing overlay may differ from later technical behavior documented in [[cashflow-lifecycle-state-machine]].