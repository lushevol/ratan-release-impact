---
type: concept
title: STRATEGIC_FM_LIST SWIFT Generation
created: 2026-08-23
updated: 2026-08-23
tags: [swift, ratan, allow-list, cashflow-suppression]
related: [ratan, cashflow-suppression-rule, cashflow-suppression-and-swift-generation, qatar-slate-one-llc-doh-gbs, why-is-slate-one-not-configured-for-downstream-settlement-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche2.md"]
---
# STRATEGIC_FM_LIST SWIFT Generation

`STRATEGIC_FM_LIST` is described as the Ratan entity allow-list checked during SWIFT-message generation. An entity in the list generates a SWIFT message; other manual entities are expected to have their FMIDs added.

The checklist records an exception for `SLATE_QFC` / `SLATE ONE LLC*DOH` (FMID `401081696`): because it is cashflow-suppressed, it does not need `STRATEGIC_FM_LIST` configuration.

This exception is limited to the stated SWIFT-list requirement. It does not prove that cashflow suppression is deployed or that all other downstream settlement requirements are unnecessary.