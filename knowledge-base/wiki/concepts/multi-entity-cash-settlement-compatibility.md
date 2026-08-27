---
type: concept
title: Multi-Entity Cash Settlement Compatibility
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, multi-entity, configuration, RATAN, local-currency]
related: [ratan, ssi-stamping, group-ready-ccy-pair-enrichment, ccy-pair-based-nostro-selection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md"]
---
# Multi-Entity Cash Settlement Compatibility

Multi-entity cash settlement compatibility is the ability of the strategic settlement flow to process local-currency cashflows for multiple booking entities using configurable eligibility rules.

This design targets:

- Saudi Arabia — FM ID `400991880`
- Nepal — FM ID `400007847`
- Egypt — FM ID `401036553`

Future entities should be addable through configuration. The source does not specify where that configuration is stored, who governs it, or whether changes require deployment.