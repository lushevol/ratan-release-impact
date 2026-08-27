---
type: query
title: What Are the Authoritative Currency and Amount Tolerances for Razor-Stella FX Cashflow Matching?
tags: [currency, amount-tolerance, matching, fx, razor, ratan, stella]
related: [six-economic-field-cashflow-matching, fx-cashflow-status-write-back, razor, ratan, stella]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FX Cashflow Status Write Back - Razor to Stella.md"]
---
# What Are the Authoritative Currency and Amount Tolerances for Razor-Stella FX Cashflow Matching?

The requirement proposes first-two-character currency matching to accommodate Stella `CNY` and Razor `CNH`, and an amount tolerance described as “within the decimal” for non-JPY and within 100 for JPY.

These compromises can produce false-positive matches, while the source specifies no reconciliation or collision control.

## Questions to resolve

- What exact calculation defines the non-JPY tolerance?
- Is the JPY tolerance inclusive, and what business rationale supports 100 JPY?
- Which currencies and products may use the tolerance?
- Is a first-two-character currency comparison limited to the approved `CNY`/`CNH` mapping, or does it apply to all `CN*` values?
- Why does the interface table show Stella currency `CNO` while the narrative uses `CNY`?
- What control rejects or escalates multiple candidate matches?

The approved mapping and tolerance contract should be explicit, testable, and monitored before relying on it for duplicate-payment mitigation.