---
type: query
title: What Is the Authoritative RATAN Correspondent BIC and MX Account Mapping?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, swift, mx, correspondent-bic, ssi, static-data]
related: [ratan-swift-reference-and-correspondent-derivation, ssi-driven-swift-and-mx-field-population, nostro-static]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/02 Swift Message Analysing for manual entities.md"]
---
# What Is the Authoritative RATAN Correspondent BIC and MX Account Mapping?

The source approves correspondent and account output behavior but relies partly on screenshots for the decisive logic.

A versioned text specification is needed for:

- Tag `:53A:` BIC derivation and fallback.
- `53AccNumber` and `SttlmAcct` eligibility.
- Field-54 and field-57 account mappings.
- `CdtrAcct`, `CdtrAgtAcct`, and `InstrForNxtAgt` output.
- `TranslateAccNumber` behavior, including IBAN handling.
- Validation, error handling, and static-data ownership.