---
type: concept
title: UTIL-to-Gross Settlement Update
tags: [UTIL, GROSS, settlement-method, cashflow, PASTDUE, accounting]
related: [settlement-method-update, ratan, cashflow-status-lifecycle, reversal-and-correction-cashflow-processing, accounting-feed-reconciliation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Settlement Method Update.md"]
---
# UTIL-to-Gross Settlement Update

The UTIL-to-Gross path changes an eligible `UTIL` cashflow to Gross settlement.

## Eligibility

```text
Settlement method = 'UTIL'
cashflow status IN (WAITING, READY, PASTDUE)
```

## Processing

For an eligible cashflow, [[ratan]]:

1. Sets the settlement method to Gross.
2. Reinstates the cashflow for Gross settlement.
3. Sets the remaining amount to `0`.
4. Removes the `PASTDUE` sub-status.

For a `PASTDUE` cashflow specifically, the cashflow is post-settled as Gross, a reversed accounting entry is generated, and the reversed entry is sent out. This accounting consequence must not be generalized to every UTIL-to-Gross update.

The source states that no special NSTP rule is required for this scenario. It does not define the broader NSTP behavior of Settlement Method Update.