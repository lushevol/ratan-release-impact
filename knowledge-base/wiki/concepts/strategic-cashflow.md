---
type: concept
title: Strategic Cashflow
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, stella, cn-settlement]
related: [stella, stella-channel, stella-cashflow-status-synchronization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# Strategic Cashflow

Strategic cashflow is the cashflow category synchronized from Ratan CN Settlement processing to Stella through the dedicated `RATANCASH_V2` / `ratancash-v2` channel.

Messages are marked with `stellaMessageType: STRATEGIC_CASHFLOW`. The source associates the category with status actions including `Net`, `Unnet`, `Release`, and `Settle`.