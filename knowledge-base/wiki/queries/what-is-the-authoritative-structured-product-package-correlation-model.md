---
type: query
title: What Is the Authoritative Structured-Product Package Correlation Model?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, structured-products, package-correlation, RFQID, trade-identifiers]
related: [structured-product-package-trade-model, package-identifier-lineage, trade-event-id-lineage, trade-cashflow-reference-linkage, trade-confirmation-driven-cashflow-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Structure products.md"]
---
# What Is the Authoritative Structured-Product Package Correlation Model?

## Question

Which identifier is authoritative for correlating a structured-product package across Blade, Stella, CDU, trade messages, confirmations, and cashflows?

## Historical evidence

The deprecated source states that:

- Blade supplies a structure-booking link ID called `RFQID`.
- `RFQID` is available in each individual trade `SCBML`.
- Stella adds its own package ID to each trade `SCBML`.
- Individual trades and cashflows have separate identifiers.

The source does not define whether `RFQID` and the Stella package ID are aliases, mapped identifiers, or identifiers with distinct system-local responsibilities.

## Required resolution

A current requirement should document:

- The authoritative package key.
- The mapping between Blade and Stella package IDs.
- The uniqueness and immutability guarantees.
- The parent-child relationship between package, trade, and cashflow IDs.
- Correlation behavior for amendments, rebookings, cancellations, and confirmations.
- The fields required in trade and cashflow `SCBML`.

Until resolved by a current source, the deprecated document should not be used to infer a production correlation contract.