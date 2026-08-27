---
type: query
title: What Is the Authoritative Stella FX Rate Selection and Rounding Rule for Authorization Limits?
created: 2026-08-23
updated: 2026-08-23
tags: [query, stella, fx-rates, rounding, authorization, ratan]
related: [stella, ratan, cashflow-usd-equivalent-authorization-calculation, profile-based-usd-authorization-limits]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Profile USD Limit.md"]
---

# What Is the Authoritative Stella FX Rate Selection and Rounding Rule for Authorization Limits?

## Question

Which Stella rate must Ratan use, and how must it be converted and rounded, when evaluating a non-USD cashflow against a profile's USD limit?

## Known contract

The source specifies:

```text
API fx/rates/date/eodTag/baseCurrency/quoteCurrency
```

The base currency is `Cashflow.Payment_Currency`, the quote currency is USD, and the USD amount is the non-USD payment amount multiplied by `spotRate`.

## Unresolved rules

The requirement does not identify:

- The date used in the request.
- The applicable `eodTag`.
- Fallback and retry behavior.
- Handling of missing, stale, or multiple rates.
- Decimal precision and rounding.
- Whether the selected rate and result are persisted for audit.

These rules determine whether an authorization decision is reproducible.
