---
type: query
title: Is CANC-to-SENT Replay Behavior Intentional?
created: 2026-08-24
updated: 2026-08-24
tags: [query, fmrp, status-synchronization, replay, cancellation]
related: [fmrp-cashflow-status-synchronization, scb-fmrp-dbf, fmrp-murex-211-settlement-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md"]
---

# Is CANC-to-SENT Replay Behavior Intentional?

## Question

When `FMIS` finds an existing `CANC` record, is changing `M_STATUS` back to `SENT` and republishing the cashflow the intended replay behavior?

## Evidence

`client.scb.fmrp.SyncStatus` calls `client.scb.fmrp.updateFmrpPay` with `STATUS='CANC'`. The SQL implementation updates matching rows to `M_STATUS='SENT'`, not `CANC`.

## Verification needed

Confirm whether this is an intentional manual replay rule, a misleading parameter name, or an implementation defect. Tests should cover repeated `FMIS`, cancellation, republish, and RATAN acknowledgement sequences.