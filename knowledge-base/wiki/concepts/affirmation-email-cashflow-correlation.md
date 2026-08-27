---
type: concept
title: Affirmation Email Cashflow Correlation
created: 2026-08-23
updated: 2026-08-23
tags: [lineage, correlation, cashflow-versioning, settlement-affirmation]
related: [ratan, cdups, settlement-affirmation-email-automation, cashflow-lineage-and-amendment-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation.md"]
---
# Affirmation Email Cashflow Correlation

Affirmation email cashflow correlation links an outbound email and inbound client response to the relevant transaction, cashflow, cashflow version, and email batch.

The requirement includes manual or automated regeneration for revised cashflows and identifies a problem when new cashflows arrive after the previous dataset has been sent to CDUPS. Without a canonical correlation identifier and versioning contract, late-arriving or revised cashflows may require manual handling.

The required design should distinguish the original affirmation, regenerated messages, client responses, partial dispatch results, and the current cashflow state.