---
type: concept
title: Netting Resultant Attribute Inheritance
created: 2026-08-22
updated: 2026-08-23
tags: [auto-netting, netting-resultant, cashflow, CIS, Germany, RATAN, cash-settlement, netting, resultant, murex, data-lineage]
related: [cashflow-netting-renetting, auto-netting-resultant-nstp, resultant-hard-blocker-stamping, ratan, beneficiary-bic-netting, what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features/Settlements BRP/Settlements BRP Prioritization.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting/Beneficiary BIC Netting Demo.md"]
---

# Netting Resultant Attribute Inheritance

Netting resultant attribute inheritance is the propagation of specified source-cashflow attributes to a resultant cashflow created by netting.

## Germany CIS requirement

The Strategic Cash Settlements Features tracker describes resultant attribute inheritance as a CIS requirement for Germany. That item is reported as done and released on October 19, 2024.

The tracker source does not specify:

- the exact attribute schema;
- inheritance precedence when source cashflows differ; or
- validation evidence.

## Beneficiary BIC Netting inheritance rule

For the proposed Beneficiary BIC Netting workflow, the Beneficiary BIC Netting Demo states a Murex inheritance rule for selected attributes:

> A resultant inherits a value from its component cashflows only when every component has the same value. If component values differ, the resultant attribute is empty.

The rule applies to:

- `Family`
- `Group`
- `Type`
- `Typology`
- `Strategy`
- `Trade ID`

This is a stated functional requirement for Beneficiary BIC netting resultants. It is not confirmation of deployed Murex behavior across all netting workflows.

Because components may originate from different trades, an empty resultant `Trade ID` may be expected.

## Scope and limitations

The Beneficiary BIC Netting Demo does not specify:

- null-versus-empty comparison semantics;
- case sensitivity or normalization rules;
- whether component ordering affects comparison;
- resultant-to-component lineage storage;
- resultant versioning;
- how component values and statuses are restored after un-netting; or
- downstream behavior when `Trade ID` is empty.

The required identity and lineage model remains tracked in [[what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity]].

## Relationship to netting

Resultant metadata can affect downstream settlement, reporting, suppression, and lifecycle handling. This concept therefore complements [[cashflow-netting-renetting]] and [[resultant-hard-blocker-stamping]].

The Germany-specific delivery statement comes from the Strategic Cash Settlements Features tracker, while the attribute-by-attribute inheritance rule comes from the Beneficiary BIC Netting Demo. Neither source establishes a general inheritance policy for every netting workflow.