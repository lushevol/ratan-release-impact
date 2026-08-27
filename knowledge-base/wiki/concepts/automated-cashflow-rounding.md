---
type: concept
title: Automated Cashflow Rounding
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, rounding, static-data, settlement, automation]
related: [ratan, stella, murex-2-11, currency-rounding-static-data, cashflow-payment-amount-canonicalization, manual-cashflow-rounding, what-is-the-authoritative-cashflow-rounding-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Rounding Rule - Tactical solution for H1 2024 Cashflow Migration.md"]
---
# Automated Cashflow Rounding

Automated cashflow rounding transforms an original payment amount into a configured currency-specific precision and rounding mode before settlement processing.

For the H1 2024 migration requirement, [[ratan]] performs this operation for original amounts received from [[stella]] and [[murex-2-11]].

## Required sequence

1. Read `Cashflow.Payment_Currency`.
2. Resolve the currency's precision and rounding type from [[currency-rounding-static-data]].
3. Apply `Round Off` or `Round Down`.
4. Remove insignificant trailing zeros from the result.
5. Persist the result in `Cashflow.Payment_Amount`.

`Round Off` is defined as 4 down and 5 up. `Round Down` is specifically configured for `CLP`, `JPY`, and `KRO`; it must not be inferred for other zero-decimal currencies.

## Scope boundary

This is system-driven migration and settlement processing. It is distinct from [[manual-cashflow-rounding]], which concerns user-driven amendments and may carry separate maker/checker, authorization, lifecycle, and versioning controls.

## Temporary ownership

Ratan's responsibility for Stella cashflows is tactical. Stella is intended to implement strategic rounding in the future. The source does not provide an activation date, retirement trigger, or cutover design.