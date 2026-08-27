---
type: entity
title: SCB DHAKA DAC (In Country)
created: 2026-08-23
updated: 2026-08-23
tags: [bangladesh, settlement, manual-entity, uat, in-country]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h, fmsgw, ratan, amh, country-specific-settlement-uat-coverage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/015 BANGLADESH SCB DHAKA DAC(In Country).md"]
---
# SCB DHAKA DAC (In Country)

SCB DHAKA DAC (In Country) is the Bangladesh in-country manual settlement entity covered by the recorded FMSGW UAT.

Its documented UAT evidence includes seven passed FMSGW scenarios covering inbound routing, acknowledgements, manual deletion approvals, back-valued messages, DEF-rule high-value processing, and duplicate-message queue placement. Two scenarios were de-scoped: deferred STP release and explicit duplicate-message reprocessing.

## System Context

Settlement messages are sent from [[ratan]] to [[fmsgw]], with released messages delivered to [[amh]] and acknowledgements returned to RATAN. The evidence is scoped to this entity and should not be generalized to all manual entities or jurisdictions.

See [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h]] and [[country-specific-settlement-uat-coverage]].