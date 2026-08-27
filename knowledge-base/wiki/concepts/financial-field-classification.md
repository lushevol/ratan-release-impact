---
type: concept
title: Financial-Field Classification
created: 2026-08-22
updated: 2026-08-22
tags: [financial-field, amendments, trade-migration, FMRP, controls]
related: [fmrp, murex, stella, cash-settlement-migration, f2b]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list.md"]
---
# Financial-Field Classification

Financial-field classification determines whether a changed trade field is treated as financially material during amendment processing.

## F2B onboarding requirement

The checklist states that a new field must be added as a financial field; otherwise amendments involving that field may be dropped as non-financial amendments.

This requirement applies when new products, STELLA attributes, migration fields, settlement attributes, or booking-model identifiers are introduced. Onboarding should therefore verify the field classification, amendment propagation, downstream event generation, and regression coverage.

The source does not list the affected fields or identify the authoritative FMRP classification rules.
