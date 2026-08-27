---
type: entity
title: SCB Nigeria LAG(GBS)
created: 2026-08-23
updated: 2026-08-23
tags: [scb, nigeria, manual-entity, settlement, uat]
related: [ratan, fmsgw, amh, manual-entity-settlement-enablement, manual-entity-settlement-onboarding, country-specific-settlement-uat-coverage, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--51mg19]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/009 NIGERIA SCB NIGERIA LAG(GBS).md"]
---

# SCB Nigeria LAG(GBS)

SCB Nigeria LAG(GBS) is a manual settlement entity covered by Nigeria-specific UAT for settlement enablement.

## UAT Evidence

The documented FMSGW scenarios all passed. They cover standard inbound routing from [[ratan]] through [[fmsgw]] to [[amh]], acknowledgement return, and manual handling of back-valued, high-value, cancelled, and duplicate payment messages.

The source does not clarify whether `LAG` is a branch, location, or processing identifier.