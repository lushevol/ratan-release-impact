---
type: concept
title: Cashflow Suppression and SWIFT Generation
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-suppression, swift, settlement-means, nos, ratan]
related: [ratan, murex-2-11-cashflow-suppression, manual-entity-swift-mx-bifurcation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/02 Swift Message Analysing for manual entities.md"]
---
# Cashflow Suppression and SWIFT Generation

Cashflow suppression and SWIFT suppression are distinct controls.

## Entity-level cashflow suppression

SLATE ONE LLC*DOH, FMID `401081696`, is cashflow-suppressed in RATAN. It requires only cashflow-suppression static data and does not require general SWIFT or MX setup. This decision is specific to the SLATE entity and must not be extended to SCB DOHA*DOH, FMID `300010782`.

## Payment-level SWIFT suppression

For a NOS payment, RATAN generates a SWIFT message unless the cashflow matches a SWIFT-suppression rule. To prevent generation, configure a suppression rule or select a settlement means outside NOS and Over account.

The source records this as a stated business rule but does not define suppression-rule priority, validation behavior, or status impacts.