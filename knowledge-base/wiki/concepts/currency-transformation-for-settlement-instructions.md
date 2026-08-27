---
type: concept
title: Currency Transformation for Settlement Instructions
created: 2026-08-22
updated: 2026-08-22
tags: [currency, settlement-instructions, nostro, vostro, configuration]
related: [standard-settlement-instructions, ssi-stamping, ssi-selection-hierarchy, fxo]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# Currency Transformation for Settlement Instructions

Currency transformation for settlement instructions converts an incoming currency code into the code used to locate Nostro or Vostro settlement data.

## FXO Example

The FXO checklist gives the example of receiving `SGO` and using `SGD` for both Vostro and Nostro lookup. The same transformation is relevant to SSI auto stamping and default Nostro stamping.

This lookup transformation is related to, but distinct from, broader non-ISO-to-ISO currency mapping. The source also calls for separate consideration of onshore currencies and precious currency mapping.

## Control Requirements

A complete implementation should define:

- The authoritative mapping source.
- Whether transformation occurs before or after [[ssi-selection-hierarchy]] evaluation.
- Effective dates and versioning.
- Behavior when no mapping exists.
- Auditability of the received and transformed values.
- Whether transformed values affect messaging and accounting as well as account lookup.

The checklist does not state whether mappings beyond `SGO` to `SGD` are required.