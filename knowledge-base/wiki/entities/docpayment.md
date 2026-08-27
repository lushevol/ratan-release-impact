---
type: entity
title: docPayment
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, cashflow, routing, processing-task]
related: [murex-211, fmrp, fmrp-outbound-mq, production-performance-monitoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Production Performance Monitoring.md"]
---
# docPayment

`docPayment` is the source-recorded processing task at the head of the observed Murex 2.11 outbound cashflow routing chain.

For the `20231113` real-time snapshot, it received 10,012 records. Its reported outbound dispositions were:

- `OUT`: 2,658
- `DISCARD`: 839
- `C6`: 202
- `CCIL`: 2
- `insert`: 2,240
- `extSettle`: 4,071

The `extSettle` branch feeds `extSettleRouter`, which directs 4,057 records to the FMRP path represented by [[fmrp-outbound-mq]]. The source does not define the business semantics of `OUT`, `DISCARD`, `C6`, `CCIL`, or `insert`; these labels must not be treated as equivalent outcomes.