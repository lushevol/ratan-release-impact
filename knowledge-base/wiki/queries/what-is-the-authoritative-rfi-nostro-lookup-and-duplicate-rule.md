---
type: query
title: What Is the Authoritative RFI Nostro Lookup and Duplicate Rule?
tags: [RFI, Nostro, static-data, duplicate-validation, portfolio-matching]
related: [nostro-type-static-data-model, portfolio-based-rfi-nostro-stamping, rfi-nostro-account]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# What Is the Authoritative RFI Nostro Lookup and Duplicate Rule?

The requirement defines lookup by booking entity, currency, and portfolio, but duplicate validation additionally includes settlement means, settlement account, and Nostro Type.

Clarification is needed on:

- Whether a record containing multiple portfolios matches any one of those values.
- Portfolio delimiters, case sensitivity, normalization, and exact-match semantics.
- Whether settlement means and settlement account also constrain runtime lookup.
- Whether portfolio values belong in the duplicate key.
- Whether multiple matching records are valid static data.
- Whether multiple matches should use the existing missing-Nostro exception or a distinct ambiguity exception.
- What should happen when the portfolio is absent, invalid, or not configured.
