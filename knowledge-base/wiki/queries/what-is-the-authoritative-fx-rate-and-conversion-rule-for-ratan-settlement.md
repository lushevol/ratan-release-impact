---
type: query
title: What Is the Authoritative FX Rate and Conversion Rule for RATAN Settlement?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, tds3, settlement, spot-rate, fx-conversion, ops]
related: [ratan-tds3-trade-lake-integration, ratan-settlement, settlement-accounting, tds3]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (TDS3)-29126.md"]
---
# What Is the Authoritative FX Rate and Conversion Rule for RATAN Settlement?

The source states that RATAN obtains spot rates from TDS3 to convert cashflow amounts to USD so OPS users can apply per-amount limitations. It does not define the rate-selection or calculation rules.

## Information Needed

- The applicable valuation date and timestamp for the TDS3 spot rate.
- Currency-pair orientation and cross-rate conventions.
- Rate type, source index, precision, rounding, and decimal-scale rules.
- The calculation formula for conversion to USD.
- Treatment of missing, stale, invalid, or late rates.
- Whether rates may be overridden and how overrides are controlled.
- The exact point at which OPS amount limitations are evaluated.
- Reconciliation, audit, and correction procedures for converted amounts.

The documented behaviour establishes a TDS3 dependency for this RATAN settlement use case but does not establish the authoritative FX-rate policy.