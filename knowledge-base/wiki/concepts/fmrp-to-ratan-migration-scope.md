---
type: concept
title: FMRP-to-RATAN Migration Scope
created: 2026-08-22
updated: 2026-08-22
tags: [fmrp, ratan, migration, tranche-1, scope, uat]
related: [fmrp, ratan, murex, projects/murex-cashflow-migration-to-ratan, fmrp-market-event-settlement-impact, allocation-cashflow-state-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement.md"]
---
# FMRP-to-RATAN Migration Scope

FMRP-to-RATAN migration scope is the set of trade-processing, cashflow, settlement, and testing dependencies created when FMRP changes or migrates Murex capabilities into the RATAN settlement landscape.

## Tranche 1 boundary

The stated Tranche 1 entity candidates are:

- HONGKONG
- SCS HK
- BANGKOK
- TAIPEI
- OBU TAIPEI
- NEWYORK

The source leaves the FMID, mandatory, and target-release fields blank. These names therefore establish candidate scope, not an approved release commitment.

## Scope categories

The document mixes several categories that must be separated during delivery planning:

1. RATAN development or configuration.
2. RATAN UAT and regression support without development.
3. Source-platform changes with an uncertain settlement dependency.
4. Future or later-milestone features, including Q3, Drop 2, and explicitly non-Q2 work.
5. Requirements requiring clarification before ownership can be assigned.

## Primary dependencies

RATAN may need to consume or validate:

- Allocation-related event and status data.
- `Structure id`.
- `TRAN_CLEAR`, representing intent to clear.
- `Trade_Purpose = 'Accrued_Interest'`.
- Clearing and counterparty-change event semantics.
- Deliverable and non-USD settlement currencies.
- Migration controls preventing duplicate payments.

The source is insufficient to define a complete implementation baseline. An authoritative scope matrix should link every feature to its milestone, owner, RATAN responsibility, interface mapping, test evidence, and acceptance criteria.