---
type: entity
title: SRI LANKA SCB COLOMBO CMB (In Country)
created: 2026-08-23
updated: 2026-08-23
tags: [manual-entity, settlement, sri-lanka, uat]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12tf8z2, ratan, fmsgw, amh, country-specific-settlement-uat-coverage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/010 SRI LANKA SCB COLOMBO CMB(In Country).md"]
---
# SRI LANKA SCB COLOMBO CMB (In Country)

SRI LANKA SCB COLOMBO CMB (In Country) is the manual-entity and country implementation scope documented in a passing FMSGW settlement UAT record.

The tested flow receives settlement messages from [[ratan]], processes routing and validation in [[fmsgw]], releases eligible messages to [[amh]], and returns acknowledgements to RATAN or the inbound system.

The source documents passing scenarios for standard inbound routing, back-valued messages, high-value payment approval, cancelled trades, MTn92 manual-cancellation processing, and duplicate-message processing. See [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12tf8z2]].

This entity is not assumed to be identical to Colombo FCB, which is referenced separately in [[what-is-the-approved-uat-scope-and-test-count-for-colombo-fcb]].