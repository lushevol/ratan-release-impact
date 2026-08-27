---
type: concept
title: SSI-Driven SWIFT and MX Field Population
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, swift, iso-20022, settlement-instructions, ratan]
related: [ratan, nostro-static, vostro-field-57-routing-derivation, what-is-the-authoritative-ratan-correspondent-bic-and-mx-account-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/02 Swift Message Analysing for manual entities.md"]
---
# SSI-Driven SWIFT and MX Field Population

RATAN's reviewed message behavior is configuration-driven: optional SWIFT and MX fields are populated only when the relevant SSI or SSI+ values exist.

## MT fields

- MT202 can populate `:56A:` or `:56D:` and `:72:`.
- MT103 can populate `:56A:` or `:56D:`, `:70:`, and `:72:`.
- MT202 Flip can populate `:52:`, `:53B:`, and `:72:`.

The presence of a field in RATAN output is accepted when configured, even if the field is absent from a legacy sample. Tag 72 may be configured through SSI+ or entered manually in cases documented by the source.

## MX fields

For `pacs.009`, `SttlmAcct` is created only when `53AccNumber` exists and settlement method is `INDA` or `INGA`.

Other accepted conditional mappings include:

- `CdtrAcct` from configured field-57 account data.
- `CdtrAgtAcct` from configured field-54 account data in SSI+.
- `InstrForNxtAgt` when RATAN's condition is met.
- Account translation through `TranslateAccNumber`, including an IBAN path when the relevant source value contains an IBAN.

The source records business acceptance but leaves detailed conditions partly embedded in screenshots. The canonical mapping and validation contract remains open.