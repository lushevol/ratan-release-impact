---
type: concept
title: Go-Live Readiness for Manual-Entity Settlement
created: 2026-08-23
updated: 2026-08-23
tags: [go-live, operational-readiness, manual-entities, settlement, tranche-1]
related: [manual-entity-settlement-enablement, settlement-day-2, ebbs-accounting-configuration, non-iso-to-iso-currency-mapping, manual-entity-swift-mx-bifurcation, what-is-the-authoritative-tranche-1-manual-entity-go-live-schedule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche1.md"]
---
# Go-Live Readiness for Manual-Entity Settlement

Go-live readiness for a manual entity is the coordinated completion and verification of the technical, operational, accounting, and control prerequisites required to process its settlement cashflows.

## Readiness domains

The Tranche 1 checklist identifies these readiness domains:

- Nostro, FMID, FMCODE, country, and branch reference data.
- SWIFT sender and Field 53/58 BIC data, currency selection, and MX eligibility.
- Release cutoff time, shifter, and timezone configuration.
- RATAN non-ISO-to-ISO currency mappings where required.
- EBBS bridge account, posting branch, transaction type, and debit/credit transaction-code configuration.
- Cashflow-suppression and `STRATEGIC_FM_LIST` business-rule treatment.
- UAT sign-off and LMS-linked verification.
- CPT and post-go-live operational monitoring.

## Evidence standard

A checklist that names required values or links to an attachment demonstrates configuration intent, not necessarily completed deployment. Completion requires accessible evidence that values were configured, tested, approved, and effective for the relevant entity.

The source is incomplete as final evidence because its static-data completion columns are blank, some values are delegated to Razor without being shown, and its UAT and CPT evidence is external.

## Tranche 1 dependencies

For Bangladesh and Tanzania, release cutoff configuration is stated to come from Razor rather than explicit checklist values. Pakistan requires the stated `PKO` to `PKR` RATAN mapping. Tanzania has a specifically amended EBBS credit code of `578`.

See [[manual-entity-settlement-enablement]] for the wider enablement scope and [[ebbs-accounting-configuration]] for accounting-specific readiness.