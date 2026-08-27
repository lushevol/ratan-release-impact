---
type: concept
title: Cashflow Precheck Validation
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, validation, precheck, normalization, data-quality]
related: [cashflow-lifecycle-stamping, lifecycle-service, cashflow-unnetting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Cashflow Lifecycle Stamping Logic.md"]
---
# Cashflow Precheck Validation

Cashflow precheck validation is the set of normalization, enrichment, and input checks performed before a cashflow is persisted and submitted for lifecycle processing.

## Normalization and enrichment

The source documents:

- Settlement amount rounding.
- `settlementDate` formatting as `yyyy-MM-dd`.
- Legal-entity enrichment for `party1` and `party2`.
- Event-reason enrichment.
- Beneficiary `bic`-flag enrichment.
- Construction of SCBML from the current message and persisted event.

A Withdrawal payment-date XPath is identified as no longer used and removed:

```text
/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow[scb:header/scb:event='Withdrawal']/scb:payment/conf:paymentDate/conf:unadjustedDate
```

## Validation list

The documented checks are:

1. Amount is numeric.
2. Value-date format is valid.
3. Amount is greater than zero.
4. Entity FMID exists.
5. CFI code exists.
6. Currency exists.
7. Counterparty FMID exists.
8. Entity FMID exists again; this is marked as a duplicate.
9. Cashflow length is 12.

The source does not define the error contract, validation order, lookup authorities, or the exact interpretation of cashflow length. “Cashflow length is 12” may refer to an identifier or another structural constraint, but the source does not resolve this.

## Design questions

The precheck sequence also raises questions about repeated `StellaInfo` conversion and common-event publication. These should be resolved before simplifying the persistence path.
