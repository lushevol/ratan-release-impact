---
type: concept
title: FMSGW Duplicate Message Processing
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, duplicate-message, validation-queue, swift, settlement]
related: [fmsgw, zambia-scb-zambia-lus-gbs, manual-entity-settlement-enablement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/005 ZAMBIA SCB ZAMBIA LUS(GBS).md"]
---
# FMSGW Duplicate Message Processing

FMSGW duplicate-message processing is a controlled validation-queue workflow rather than an automatically terminal disposition.

For the tested Zambia configuration, duplicate MT103, MT202, and MT202COV messages are found in the Duplicate Message Queue. A user Process action advances the transaction to SCB Specific Validations.

The source does not identify the duplicate-detection key, idempotency behavior, user authorization controls, alternative dispositions, or the rules evaluated by SCB Specific Validations.