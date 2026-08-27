---
type: concept
title: Hold and Un-Hold
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-operations, workflow-control, settlement-exceptions]
related: [fmrp-china-cash-settlement, fmo-post-trade-portal, cashflow-blotter, cashflow-status-and-substate-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Hold and Un-Hold

## Definition

Hold and un-hold provide an operator-controlled pause and release flow for cashflows.

## Demonstrated behavior

The source demonstrates selecting `Waiting` and `Ready` cashflows in the cashflow blotter, choosing **Hold**, entering a comment, and submitting. Both cashflows change to `Hold`.

The operator can then choose **Un-Hold**, enter a comment, and submit. The cashflows return to `Waiting` and `Ready`, respectively. This suggests that un-hold restores the prior state, although the source does not define whether that behavior is guaranteed.

## Open detail

The source does not specify comment validation, permissions, audit retention, or how held cashflows interact with netting and settlement deadlines.
