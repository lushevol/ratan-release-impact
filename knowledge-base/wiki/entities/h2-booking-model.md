---
type: entity
title: H2 Booking Model
created: 2026-08-24
updated: 2026-08-24
tags: [booking-model, h2, cash-settlement, cutover]
related: [h1-booking-model, h1-h2-historical-cashflow-group-continuity, cashflow-group-force-completion-on-cancellation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/H1 -  H2 booking model historical data analyse.md"]
---
# H2 Booking Model

H2 is the post-switch booking model in the supplied March scenarios. Its realtime processing is expected to locate a group formed under [[h1-booking-model]], count received cashflows in that existing group, and complete the group when the expected scenario count is reached.

For a `CNCL` member in the four-cashflow cancellation scenario, H2 processing is instructed to send force complete to the historical group. The source does not define H2’s grouping algorithm, persistence model, event ordering, or idempotency behavior.

See [[h1-h2-historical-cashflow-group-continuity]] and [[cashflow-group-force-completion-on-cancellation]].