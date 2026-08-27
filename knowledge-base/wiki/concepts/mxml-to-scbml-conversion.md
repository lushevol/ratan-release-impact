---
type: concept
title: MxML-to-SCBML Conversion
created: 2026-08-22
updated: 2026-08-22
tags: [mxml, scbml, murex, ratan, cashflow, transformation]
related: [murex, ratan, ratan-one, murex-to-ratan-cashflow-interface, post-settlement-amendment-and-cancellation-handling, what-is-the-canonical-mxml-cashflow-id-format, should-mxml-amount-mapping-use-flowamount-or-flowamountrounded]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Ratan MxML- SCBML Adaptor ( Entity CN, SG, IN, MY).md"]
---
# MxML-to-SCBML Conversion

MxML-to-SCBML conversion is the Ratan adaptor process that transforms a Murex `MxPayML` payment message into Ratan strategy-model cashflow data.

## Essential transformation responsibilities

The adaptor maps:

- payment identity, amount, currency, dates, and publication time;
- entity, counterparty, portfolio, trader, and business-unit identifiers;
- trade identifiers, validation state, and product attributes;
- payment direction using `isCredit`;
- reversal events using a `Reverse` payment comment;
- amendment-driven NSTP treatment using `amendmentFlag`.

It also applies Ratan defaults, including `Unaffirmed` affirmation status, `Projected` cashflow state, business and cashflow version `0`, and `Murex` as both data source and sender.

## Reversal semantics

A comment matching `Reverse%` produces a `Withdrawal` cashflow event, reverses payer and receiver references, and obtains the original cashflow ID from the final token of the comment. A non-reversal message is a `New` event.

## Data-quality constraints

The source leaves several conversion rules unresolved:

- `flowAmountRounded` appears in the mandatory-field list, while the final mapping rule changes the amount source to `flowAmount`;
- `VALD` validation handling is marked “To be done”;
- the cashflow-ID prefix and padding pseudocode conflicts with its example;
- payment-type mapping is explicitly TBD.

These unresolved mappings require confirmation before the adaptor is treated as an authoritative implementation specification.