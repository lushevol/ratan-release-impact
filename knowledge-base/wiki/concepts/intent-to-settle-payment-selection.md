---
type: concept
title: Intent-to-Settle Payment Selection
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, payment-selection, scbml, settlement, xva]
related: [scbml, ratan-settlement, scbml-cashflow-ingestion-and-persistence, cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md"]
---
# Intent-to-Settle Payment Selection

A SCBML `<scb:cashflow>` may contain several `<scb:payment>` elements. `scb:isIntentToSettle` identifies the payment intended for settlement:

- `true` identifies a settlement-bearing payment.
- `false` identifies an informational or query/display payment, normally related to XVA.

When multiple payments exist, the stated rule selects the only `true` payment if exactly one exists and removes the `false` payments. If no payment, or more than one payment, is marked `true`, Ratan selects the first payment in message order.

This fallback makes XML order operationally significant and does not specify rejection, exception creation, monitoring, or escalation for ambiguous upstream flags. See [[what-should-ratan-do-with-ambiguous-intent-to-settle-flags]].

The source is also ambiguous on whether removed false-intent payments remain available in raw-message storage, persisted data, or the GUI. See [[are-non-settlement-payments-retained-in-ratan]].