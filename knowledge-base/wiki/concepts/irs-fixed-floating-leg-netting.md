---
type: concept
title: IRS Fixed and Floating Leg Netting
created: 2026-08-23
updated: 2026-08-23
tags: [IRS, cashflow-netting, coupon, resultant, settlement]
related: [cashflow-netting, netting-resultant-cashflow, pending-another-leg-status, irs-refixing-unnetting-and-renetting, murex-pending-fixing-flag-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---
# IRS Fixed and Floating Leg Netting

IRS fixed and floating leg netting is the schedule-level process of combining the two coupon amounts for an IRS payment date into one settlement amount.

The source describes two implementation pathways:

- [[murex]] may provide a preliminary fixed leg, then later reverse it and deliver an upstream-calculated net resultant after floating-rate fixing.
- [[stella]] may provide fixed and floating coupon cashflows for RATAN to auto-net within a trade.

In the Stella auto-netting examples, both component coupons become `NETTED` and the intra-trade resultant remains `WAITING`. That resultant may either settle without further netting or participate in cross-trade netting. When cross-trade netting occurs, the intra-trade resultants become `DEAD` and a replacement cross-trade resultant is created.

The source does not define the authoritative netting key, resultant lineage attributes, or eligibility controls for cross-trade netting. It also uses “settle as Gross” alongside creation of a net resultant; the intended meaning requires clarification in [[what-is-the-authoritative-irs-netting-and-amendment-state-machine]].