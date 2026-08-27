---
type: concept
title: FMSWG SWIFT Message Validation
created: 2026-08-23
updated: 2026-08-23
tags: [fmswg, swift, validation, bic, payment-controls]
related: [fmswg, amh, ssi-plus, ssi-data-quality-for-swift-generation, swift-network, cashflow-suppression-vs-swift-suppression, was-the-suppressxxx-mt604-control-defect-remediated]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Production Issue - Swift Message.md"]
---
# FMSWG SWIFT Message Validation

FMSWG SWIFT message validation is the preventative control layer that should reject invalid message content before a message is submitted to [[AMH]].

## Documented validation gaps

The source provides specific production examples of required control coverage:

- reject invalid BIC values in applicable party fields, including field `87A`;
- reject placeholder values such as `SUPPRESSXXX`;
- require the beneficiary account required for MT103 field `59` for MXN;
- validate delimiters, line structure, and field-format serialization for free-format party fields such as MT202 field `57D`.

AMH rejected invalid BICs and malformed content after generation. Downstream rejection is detective control evidence; it is not proof that FMSWG prevents recurrence.

## Suppression is separate

A client intended to be suppressed reached MT103 generation and then failed mandatory-field validation. [[Cashflow suppression versus SWIFT suppression|cashflow-suppression-vs-swift-suppression]] is therefore a separate control concern from validating fields on messages that are permitted to generate.

The MT604 placeholder-BIC incident has no recorded resolution; see [[was-the-suppressxxx-mt604-control-defect-remediated]].