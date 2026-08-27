---
type: comparison
title: Auto, Manual, and PastDue Utilization
created: 2026-08-23
updated: 2026-08-23
tags: [comparison, fx-utilization, auto-utilization, pastdue]
related: [fx-utilization, fxu, ratan, utilization-status-lifecycle, partial-and-pastdue-utilization-accounting, utilization-eligibility-static]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md"]
---
# Auto, Manual, and PastDue Utilization

## Manual utilization

Manual utilization is initiated through [[fxu]] following an operational payment instruction. For MVP, it is full utilization on value date: FXU queries [[ratan]], submits a Solace request, and receives ACK/NACK.

A proposal identifies manual utilization through settlement means/account `FXBRREC-M`; an alternative recommends a separate classification flag. Neither is confirmed.

## Auto utilization

Auto utilization is proposed as RATAN-triggered full utilization on value date. Its indicators are a trade-level auto-utilization indicator, counterparty eligibility, and settlement means `FXBRREC`.

The source provides country-specific timing proposals for EG, SA, and NP. It also says that unutilized cashflows at EOD may be auto-utilized to FXBRREC, but this is not reconciled with the Phase 2 PastDue model.

## PastDue utilization

PastDue utilization is Phase 2 only. It applies to an unutilized balance after an entity-configured cutoff and moves the balance through a Past Due Account. A later utilization reverses the Past Due position before utilization accounting is posted.

The source says FXU should reject post-value-date requests in MVP, which conflicts with the Phase 2 post-value-date PastDue flow. See [[what-is-the-authoritative-pastdue-and-auto-utilization-accounting-model]].