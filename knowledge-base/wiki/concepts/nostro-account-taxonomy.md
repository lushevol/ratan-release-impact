---
type: concept
title: Nostro Account Taxonomy
created: 2026-08-24
updated: 2026-08-24
tags: [nostro-static-data, account-taxonomy, settlement, suspense-accounts, over-accounts]
related: [nostro-static-golden-source, nostro-centralization, nostro-stamping, nostro-record-composite-uniqueness, razor, ebbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/Nostro Static Golden Source.md"]
---

# Nostro Account Taxonomy

## Definition

The Nostro static model covers three account categories with different legal-entity relationships and settlement behavior.

| Category | Relationship | Purpose | Payment or receipt of funds |
| --- | --- | --- | --- |
| Nostro account | Account held by one legal entity with another legal entity | Paying or receiving funds | Yes |
| Over account | Account held within the same legal entity | Paying or receiving funds from clients of that entity | Yes |
| Suspense account | Internal account within the same legal entity | Posting settlement-accounting entries | No |

## Modeling implication

Although all three categories are maintained as Nostro static in the source systems, they should not be treated as operationally interchangeable. `Settlement_means` is proposed as the distinguishing field, with values such as `NOS`, `Over Account`, and `Suspense`.

Suspense accounts may require a separate lifecycle or ownership model because they do not generate payment or receipt instructions. The source leaves their ownership among NAMS, RDM, and RATAN unresolved.

## Matching implication

A settlement-account label such as `DVSUS` is not necessarily globally unique. Legal entity, currency, settlement means, account number, and effective dates may be required to identify a record. The proposed key must also account for possible mappings to EBBS ledger accounts.