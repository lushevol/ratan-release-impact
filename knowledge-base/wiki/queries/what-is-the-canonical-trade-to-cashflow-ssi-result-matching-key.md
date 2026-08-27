---
type: query
title: What Is the Canonical Trade-to-Cashflow SSI Result Matching Key?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, SSI-stamping, cashflow, matching, correctness]
related: [trade-level-ssi-stamping, product-agnostic-ssi-stamping, cashflow, nstp-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md"]
---
# What Is the Canonical Trade-to-Cashflow SSI Result Matching Key?

## Question

Which complete set of attributes proves that a stored trade SSI result can be safely applied to a cashflow?

## Current proposal

The source mentions matching by currency and direction, but leaves the remaining matching attributes unspecified.

## Required resolution

The contract should define currency representation, pay/receive versus debit/credit semantics, account role, settlement method and type, booking and counterparty entities, product, CFI, netting context, and any other SSI determinant. It should also define behavior for multiple matches, no match, partial match, stale results, and conflicting trade versions.