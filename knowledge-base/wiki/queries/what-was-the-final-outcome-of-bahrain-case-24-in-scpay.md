---
type: query
title: What Was the Final Outcome of Bahrain Case 24 in SCPAY?
created: 2026-08-23
updated: 2026-08-23
tags: [bahrain, scpay, uat, pending-payment, settlement]
related: [bahrain-scb-bahrai-man-gbs, scpay, scpay-settlement-routing, amh-acknowledgement-versus-downstream-delivery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/Manual entity (NG GH QA BH UG) testing with ISO.md"]
---
# What Was the Final Outcome of Bahrain Case 24 in SCPAY?

Bahrain case 24 is a `pacs.009.001.08` payment with Tag20 `DV55152971013802` and UETR `f8c16d31-83fa-4dd7-be0b-cb884d510158`. It was received and acknowledged in AMH, sent to SWIFT, and recorded as routed to [[scpay]] but pending.

The evidence log supplies no subsequent SCPAY state, completion confirmation, failure reason, or reprocessing result. Obtain the terminal SCPAY outcome before treating this scenario as an end-to-end UAT pass.