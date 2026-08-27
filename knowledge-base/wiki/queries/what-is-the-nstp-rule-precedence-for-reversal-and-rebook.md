---
type: query
title: What Is the NSTP Rule Precedence for Reversal and Rebook?
created: 2026-08-23
updated: 2026-08-23
tags: [nstp, reversal, rebook, rule-precedence, open-question]
related: [nstp-rule-routing, cashflow-suppression-rules, cashflow-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data.md"]
---
# What Is the NSTP Rule Precedence for Reversal and Rebook?

The static-data inventory defines conflicting routes for the same event reasons:

- `Reversal` is routed as `CHECKER_ONLY` / `HIGH_RISK_NSTP` and later as `MAKER_ONLY` / `NSTP`.
- `Rebook` is routed as `CHECKER_ONLY` / `HIGH_RISK_NSTP` and later as `MAKER_ONLY` / `NSTP`.

## Questions

1. Do later rules supersede earlier rules?
2. Can multiple exceptions be raised for one cashflow?
3. Does the route depend on product, state, source system, or effective date?
4. Which operation level and category are authoritative in production?

An authoritative rule export, version history, or runtime decision trace is needed to resolve this query.