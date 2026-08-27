---
type: concept
title: CFI Code Mapping for Murex Vostro SSI
tags: [cfi-code, murex-2-11, vostro-ssi, ssi-plus, static-data, product-taxonomy]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--8-cfi-cod--i6t2qx, what-is-the-authoritative-cfi-code-mapping-for-murex-211-vostro-ssi-securities, murex-2-11, ssi-plus, scb-receive-vostro-validation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/CFI Code.md"]
---
# CFI Code Mapping for Murex Vostro SSI

CFI Code Mapping for Murex Vostro SSI is the association of SSI+ security records with Murex 2.11 product taxonomy fields—`Family`, `Group`, and `Type`—and CFI-code patterns.

The referenced material is restricted to Vostro SSI static-data context. It does not establish rules for Nostro selection, RFI handling, SWIFT generation, or cashflow lifecycle processing.

## Recorded structure

The historical mapping uses:

- `SSI+ Security ID`, such as `SCBIRDIRS` or `SCBCUFXFX`;
- an SSI security name prefixed with `MXG`;
- a Murex product taxonomy of `Family`, `Group`, and optionally `Type`;
- a CFI-code value expressed as a pattern, such as `SR****`, `JF****`, or `JF***N`.

The source does not define whether asterisks are wildcard-match semantics, partial display values, or placeholders for a complete six-character CFI code. Therefore, these values cannot be treated as complete executable classification rules.

## Historical status

All entries in the underlying table are struck through. They must be considered proposed, retired, superseded, or otherwise unverified until an approved static-data source confirms their current status.

Known data-quality concerns include:

- conflicting `HR****` and `SR****` values for `SCBIRDCF`;
- reuse of `SCBCUOSMP` for both `HF****` and `MM****`;
- missing SSI identities for several product classifications;
- a documented lack of an OTC identifier; and
- an unresolved requirement to distinguish principal from interest for loan and deposit records.

The two claimed Alert SSIs are also not identifiable from the available table.

## Relationship to other documentation

[[murex-2-11]] is the product-taxonomy context, while [[ssi-plus]] is the system identified by the `SSI+ Security ID` field. [[scb-receive-vostro-validation]] may use Vostro static data in a broader process context, but this source does not define validation behavior.

The current authoritative mapping, its wildcard semantics, and any replacement for this struck-through record remain tracked in [[what-is-the-authoritative-cfi-code-mapping-for-murex-211-vostro-ssi-securities]].