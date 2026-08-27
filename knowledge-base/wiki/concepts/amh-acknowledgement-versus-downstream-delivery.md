---
type: concept
title: AMH Acknowledgement Versus Downstream Delivery
created: 2026-08-23
updated: 2026-08-23
tags: [amh, acknowledgement, downstream-delivery, settlement, uat]
related: [settlement-acknowledgement-flow, mts-downstream-settlement-validation, scpay-settlement-routing, country-specific-settlement-uat-coverage, amh, mts, scpay]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/Manual entity (NG GH QA BH UG) testing with ISO.md"]
---
# AMH Acknowledgement Versus Downstream Delivery

The UAT source explicitly defines an AMH `ACKED` result as successful processing from the AMH side. It does not establish that a payment was delivered to, received by, or terminally processed in a downstream system.

The evidence supports distinct checkpoints:

1. Receipt and acknowledgement in [[amh]].
2. Dispatch to SWIFT, where recorded.
3. Receipt and processing in [[mts]] or MTS US.
4. Receipt and terminal processing in [[scpay]].
5. The independently displayed cashflow status, such as `SETTLED` or `RELEASED`.

Ghana cases 17–18 demonstrate the distinction: both were acknowledged in AMH but not received in MTS US. Bahrain case 24 was acknowledged and marked `SETTLED`, yet was pending in SCPAY. Therefore, a UAT pass requires evidence for the relevant downstream terminal checkpoint, not only AMH acknowledgement or cashflow status.