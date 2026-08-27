---
type: entity
title: Tanzania SCB DAR
created: 2026-08-23
updated: 2026-08-23
tags: [tanzania, scb, dar, settlement, uat, manual-entity]
related: [ratan, fmsgw, amh, country-specific-settlement-uat-coverage, manual-entity-settlement-onboarding, is-tanzani-the-intended-country-identifier-for-tanzania]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/007 TANZANIA SCB TANZANI DAR(In Country).md"]
---
# Tanzania SCB DAR

Tanzania SCB DAR is the in-country deployment scope represented by a seven-scenario FMSGW UAT record for manual-entity settlement messaging.

The documented tests cover routing between [[ratan]], [[fmsgw]], and [[amh]], including manual approval queues, duplicate handling, and inbound ACK flows. All seven listed scenarios are marked PASS.

## Identifier Caveat

The source filename contains `TANZANI DAR`, while its surrounding context indicates Tanzania. The source does not establish whether `TANZANI` is an approved system identifier, abbreviation, or naming error. This remains tracked in [[is-tanzani-the-intended-country-identifier-for-tanzania]].