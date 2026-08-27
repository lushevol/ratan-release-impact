---
type: entity
title: Vietnam SCB Hanoi HNI(GBS)
created: 2026-08-23
updated: 2026-08-23
tags: [settlement-entity, manual-entity, vietnam, hni, gbs, uat]
related: [fmsgw, ratan, amh, vietnam-scb-hanoi-hni-gbs-settlement-uat-coverage, manual-entity-settlement-onboarding, country-specific-settlement-uat-coverage, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--pf0rmf]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/012 VIETNAM SCB HANOI HNI(GBS).md"]
---

# Vietnam SCB Hanoi HNI(GBS)

## Identity and role

Vietnam SCB Hanoi HNI(GBS) is a named manual settlement entity in the Settlement Day 2 enablement UAT scope. The entity is the target of inbound settlement-message testing through [[entities/fmsgw]].

## Integration context

The documented flow is:

1. [[entities/ratan]] submits settlement messages.
2. [[entities/fmsgw]] receives and processes the messages.
3. Eligible messages are sent to [[entities/amh]].
4. FMSGW returns an acknowledgement to RATAN.

## UAT status

The associated UAT evidence records four passing scenarios:

- MT103 with associated MT202 COV routing and ACK-dependent COV release.
- MT202 routing and acknowledgement.
- MT192/292 scenario routing and acknowledgement.
- Back value-dated message handling through the Back Valued Messages Queue.

Four additional scenarios were descoped because a production scenario was not available: high-value payment approval, cancelled-trade processing, MTn92 manual cancellation, and duplicate-message processing. The source also has no numbered test case 5.

This entity-specific status is detailed in [[concepts/vietnam-scb-hanoi-hni-gbs-settlement-uat-coverage]].