---
type: concept
title: MT103–MT202 COV Acknowledgement Sequencing
created: 2026-08-23
updated: 2026-08-23
tags: [swift, mt103, mt202cov, acknowledgement, sequencing, settlement]
related: [fmsgw, zambia-scb-zambia-lus-gbs, manual-entity-settlement-enablement, cashflow-suppression-and-swift-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/005 ZAMBIA SCB ZAMBIA LUS(GBS).md"]
---
# MT103–MT202 COV Acknowledgement Sequencing

In the Zambia UAT scope, MT202 COV should be released only after the associated MT103 receives a successful ACK.

The source marks the MT103/202COV scenario as Pass, but does not provide correlation identifiers, timestamps, hold-state evidence, timeout behavior, or the result of an MT103 ACK failure. This relationship is specific to MT103 and MT202 COV and must not be generalized to all settlement message pairs.