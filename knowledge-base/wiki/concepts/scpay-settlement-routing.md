---
type: concept
title: SCPAY Settlement Routing
created: 2026-08-23
updated: 2026-08-23
tags: [scpay, settlement-routing, downstream-processing, uat]
related: [scpay, amh, amh-acknowledgement-versus-downstream-delivery, country-specific-settlement-uat-coverage, what-was-the-final-outcome-of-bahrain-case-24-in-scpay]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/Manual entity (NG GH QA BH UG) testing with ISO.md"]
---
# SCPAY Settlement Routing

SCPAY settlement routing is the downstream path recorded for selected manual-entity payments after AMH processing.

The source records Bahrain case 24 as routed to [[scpay]] and pending. Nigeria cases 32–33 were received in AMH and routed to SCPAY, followed by a request to reinitiate them. These outcomes show that routing to SCPAY is not evidence of terminal settlement.

UAT reporting should record SCPAY receipt, processing state, reinitiation status, and final terminal outcome separately from AMH acknowledgement and the cashflow display status.