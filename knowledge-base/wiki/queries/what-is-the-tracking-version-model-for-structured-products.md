---
type: query
title: What Is the Tracking Version Model for Structured Products?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, structured-products, versioning, tracking-version, cashflows]
related: [structured-product-package-trade-model, package-identifier-lineage, cashflow-event-versioning, trade-event-id-lineage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Structure products.md"]
---
# What Is the Tracking Version Model for Structured Products?

## Question

What does `Tracking Version` version in the structured-product package model, and when should it change?

## Historical evidence

The deprecated source includes `Tracking Version` in its example table with a value of `0`. It does not define whether the value applies to:

- The package.
- An individual trade.
- A confirmation.
- A cashflow.
- A message lineage spanning multiple objects.

No increment, reset, or reconciliation rules are provided.

## Required resolution

A current requirement should define:

- The object or aggregate versioned by `Tracking Version`.
- Initial-value rules.
- Increment triggers.
- Behavior for trade amendments, package amendments, cancellations, and rebookings.
- Relationship to existing trade and cashflow event versions.
- Idempotency and duplicate-event handling.
- Whether the version is carried in trade `SCBML`, cashflow `SCBML`, CDU confirmations, or all of them.

The value `0` in the historical example is insufficient evidence for a production versioning contract.