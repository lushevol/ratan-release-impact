---
type: query
title: What Does ManualCraft Change in Murex 2.11 Payment MXML?
created: 2026-08-24
updated: 2026-08-24
tags: [manualcraft, mxml, murex-211, payment-integration, open-question]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-surrounding-system-int--b0grlq, manualcraft, manualcraft-mxml-enrichment, murex-ratan-cashflow-message-contract, cn-settlement-payment-message-catalogue]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Payment MXML sample files.md"]
---
# What Does ManualCraft Change in Murex 2.11 Payment MXML?

## Question

Which XML fields, structures, or values does ManualCraft add, remove, or transform when enriching payment MXML produced by [[entities/murex-211]]?

## Why this remains open

The source presents a comparison between “Raw MXML” and “After enrichment (ManualCraft)” for ten payment labels, but every comparison cell is empty. No payload pair or transformation description is available.

The source therefore cannot establish:

- Whether ManualCraft enriches every listed message variant.
- Which fields are changed for CMS or cover variants.
- Whether `mt202_210_cms` represents one composite message or multiple outputs.
- What the `_cover_new` suffix means.
- Which system consumes the enriched payload.
- Whether enrichment is validated, retried, rejected, or acknowledged.

## Evidence needed

Resolve this query with paired raw and enriched samples, field-level diffs, schema or interface documentation, message-version information, and validation or production test evidence. The evidence should identify whether each listed label is a standard SWIFT type or an internal integration classification.

Relevant context includes [[concepts/murex-ratan-cashflow-message-contract]], [[concepts/cms-dependent-swift-message-generation]], and [[concepts/cash-settlement-inbound-outbound-message-validation]].