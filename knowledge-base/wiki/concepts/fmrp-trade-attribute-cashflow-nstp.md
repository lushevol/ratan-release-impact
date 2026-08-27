---
type: concept
title: FMRP Trade-Attribute-Driven Cashflow NSTP
created: 2026-08-22
updated: 2026-08-22
tags: [fmrp, cashflow-nstp, trade-attributes, structure-id, tran-clear, hedge-accounting, ratan]
related: [fmrp, ratan, uber, nstp-exception-handling, payment-stp-exception-catalogue, fmrp-to-ratan-migration-scope]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement.md"]
---
# FMRP Trade-Attribute-Driven Cashflow NSTP

FMRP trade-attribute-driven cashflow NSTP is the use of new or changed trade classifications to determine whether cashflows can proceed through straight-through processing or require exception handling.

## Attributes and classifications

The source identifies the following settlement-relevant values:

| Attribute or value | Documented purpose |
|---|---|
| `Structure id` | Identifies structured trades or hedges and may be consumed for cashflow NSTP |
| `TRAN_CLEAR` | Represents intent to clear |
| `Trade_Purpose = 'Accrued_Interest'` | New SCF usage for hedge-accounting accruals and PV/MTM separation |

The source suggests that `Trade_Purpose = 'Accrued_Interest'` may require a new cashflow suppression rule. It also identifies a dependency between the new trade attributes and RATAN Uber feature `7797567`.

## Settlement implications

New attributes may influence:

- Cashflow NSTP classification.
- Settlement method and clearing treatment.
- Hedge-accounting payment type.
- Suppression or exception rules.
- Uber onboarding and downstream integration validation.

The source does not define the authoritative field names beyond the values shown, nor does it specify precedence when multiple attributes apply. Existing [[concepts/nstp-exception-handling]] rules should not be extended until the field mapping, validation rules, and acceptance criteria are confirmed.