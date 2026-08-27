---
type: query
title: How Does NAMS Nostro SSI Classification Map to Cash Settlement SSI Processing?
tags: [nams, nostro, ssi, cash-settlement, mapping, open-question]
related: [nostro-account-ssi-classification, ssi-selection-as-non-adhoc-ssi, ssi-id-persistence-and-edit-provenance, nostro-stamping, ssi-plus]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/How to create a Nostro Account in NAMS.md"]
---

# How Does NAMS Nostro SSI Classification Map to Cash Settlement SSI Processing?

## Question

Does the NAMS account-level `SSI` or `NON-SSI` classification map to SSI+ records, Cash Settlement SSI selection, ad hoc SSI behavior, cashflow stamping eligibility, or downstream SSI identifiers?

## Evidence

The source states that NAMS defaults the account classification to `NON-SSI` and allows the requestor to select `SSI` for special-purpose activity or a single client. It does not describe downstream propagation or processing semantics.

Existing wiki coverage describes Cash Settlement SSI selection, provenance, identifiers, and ad hoc exceptions. The source does not establish that those concepts use the same field, lifecycle, or identifier as the NAMS classification.

## Required investigation

Identify:

- The field-level mapping, if any, between NAMS and SSI+.
- Whether the classification is propagated to Cash Settlement or only used for NAMS governance.
- The relationship to SSI IDs and reference IDs.
- Whether `SSI` changes stamping, selection, or approval behavior.
- Amendment and historical-effective-date behavior.
- Rules for reconciling conflicting classifications across systems.
