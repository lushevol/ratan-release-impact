---
type: concept
title: Vostro SSI Redundancy and Product Scoping
created: 2026-08-24
updated: 2026-08-24
tags: [vostro-ssi, static-data, redundancy, product-classification, ssi-plus]
related: [ssi-plus, murex-2-11, ratAN-10123, vostro-data-sourcing-from-ssi-plus, cfi-code-mapping-for-murex-vostro-ssi, what-is-the-canonical-uniqueness-key-for-vostro-ssi-records]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI.md"]
---
# Vostro SSI Redundancy and Product Scoping

A Vostro SSI should only be treated as an exact duplicate when all fields in its authoritative uniqueness and selection key match. Records that share settlement-routing attributes but carry different `Security` classifications are product-scoped candidates for analysis, not proven redundant records.

## Distinctions

- **Exact duplicate:** every field required by the authoritative SSI key is identical.
- **Product-scoped matching record:** settlement attributes match but `Security` differs, such as `MXG IRD` versus `MXG IRD IRS`.
- **Near-duplicate:** `Security` differs and another potentially material field differs, such as `SwiftType` or `AccountRef`.
- **Business-valid product differentiation:** separate records are intentionally retained because product classification controls eligibility, routing, or message behavior.

The RATAN-10123 source shows all these categories as apparent duplicates only after excluding `Security` from comparison. It does not provide a rule that permits this exclusion.

## Material fields requiring confirmation

The source identifies these candidate discriminators:

- Parent Trading Account
- Currency
- Branch
- Security
- Country
- Method
- BIC
- AccountRef
- SwiftType

`SwiftType` values including `MT202`, `MT103`, and `Default` may affect message selection. `AccountRef` differences indicate distinct account-routing data. Neither difference should be treated as non-material without an approved selection contract.

## Operational consequence

Do not deduplicate SSI+ records merely because BIC, account, currency, and other displayed settlement fields match. First resolve [[what-is-the-canonical-uniqueness-key-for-vostro-ssi-records]] and validate whether the Murex product classification is used by Vostro SSI lookup.

This topic extends [[vostro-data-sourcing-from-ssi-plus]] and is related to, but does not establish, [[cfi-code-mapping-for-murex-vostro-ssi]].