---
type: concept
title: Netting Eligibility Static Data
created: 2026-08-23
updated: 2026-08-23
tags: [netting, eligibility, static-data, cashflow]
related: [nstp-rule-routing, nostro-stamping, ratan, ssi-plus]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data.md"]
---
# Netting Eligibility Static Data

Netting Eligibility Rules are configurable multi-attribute criteria maintained through Maker/Checker controls. The documented dimensions are booking entity, portfolio, client, product type, and payment currency.

## Data Structure

| Attribute | Operator | Logical Model Field | Can Be Blank? | Sample |
|---|---|---|---|---|
| Booking Entity FMID/FM Code | IS | `Entity.Booking_Entity_SCI_FMID Entity.Booking_Entity_SCI_FMCODE` |  | `1007522 SCB LONDON*LDN` |
| Portfolio | IS |  | Y |  |
| Client FMID/FM Code | IS | `Entity.Counterparty_SCI_FMID Entity.Counterparty_SCI_FMCODE` |  | `10036739 BARCLAYS FX*LDN` |
| Product Type? | IS/IN | `Instrument_Common.CFI_Code Instrument_Common.ISDA_Taxonomy` | Y | `SRACCP InterestRate:CrossCurrency:Basis` |
| Currency | IS/IN | `Cashflow.Payment_Currency` | Y | `USD/Blank` |

The supplied CN Day1 expression is:

```text
Entity.Counterparty_SCI_FMID==400202766&&Cashflow.Netting_Id==null
```

The reason is recorded as `Shanghai Clearing Hourse`.

## Unresolved Semantics

The source calls the configuration a Netting Eligibility Rule but does not state whether a matching rule means that netting is allowed, prohibited, or routed for exception handling. This is tracked in [[what-is-the-outcome-semantics-of-netting-eligibility-rules]].