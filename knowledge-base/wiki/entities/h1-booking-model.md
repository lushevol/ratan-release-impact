---
type: entity
title: H1 Booking Model
created: 2026-08-24
updated: 2026-08-24
tags: [booking-model, h1, cash-settlement, historical-data]
related: [h2-booking-model, h1-h2-historical-cashflow-group-continuity, murex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/H1 -  H2 booking model historical data analyse.md"]
---
# H1 Booking Model

H1 is the pre-cutover booking model in the supplied March transition scenarios. The source states that H1 groups cashflows satisfying:

```text
MxSystemDate <= VD <= MxSystemDate+9
```

Groups created under H1 must remain discoverable to H2 processing after the model switch. The source does not define the H1 booking algorithm, group key, ownership, or its relationship to [[murex]] beyond use of `MxSystemDate`.

See [[h1-h2-historical-cashflow-group-continuity]] and [[what-is-the-authoritative-h1-h2-historical-group-identity-and-cutover-rule]].