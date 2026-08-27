---
type: concept
title: Six-Economic-Field Cashflow Matching
tags: [cashflow, matching, reconciliation, fx, ratan, data-quality]
related: [ratan, razor, stella, trade-cashflow-reference-linkage, cashflow-reference-consistency-validation, trade-economic-versus-non-economic-update, fx-cashflow-status-write-back, how-does-ratan-prevent-stale-or-ambiguous-razor-events-from-updating-the-wrong-stella-cashflow-version, what-are-the-authoritative-currency-and-amount-tolerances-for-razor-stella-fx-cashflow-matching]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FX Cashflow Status Write Back - Razor to Stella.md"]
---
# Six-Economic-Field Cashflow Matching

Six-economic-field cashflow matching is the specified [[ratan]] correlation method for associating a Razor FX cashflow event with the latest Stella cashflow version for the same trade. It compensates for Razor's lack of a trade-version value.

The fields are:

1. Booking Entity
2. Counterparty
3. Currency
4. Amount
5. Value Date
6. Pay/Receive

RATAN stores the Stella trade ID, trade version, and this field set for incoming Stella replication cashflows. It compares a latest cashflow version with its prior version to classify a Stella amendment as economic or non-economic, then uses the fields to match eligible Razor status events.

## Approximate matching rules

The design explicitly weakens exact matching in two areas:

- Currency comparison uses only the first two characters of the currency code, intended to treat Stella `CNY` and Razor `CNH` as equivalent.
- Amount matching accepts a difference “within the decimal” for non-JPY and within 100 for JPY.

The requirement acknowledges that any unknown `CN*` currency could be accepted under the currency rule. It does not define a precise non-JPY tolerance formula, currency-specific decimal rules, or collision-resolution procedure.

## Version and ambiguity risk

RATAN maps the incoming Razor event to the latest Stella version because Razor has no trade-version field. This can misapply a status when messages arrive late or out of order, multiple cashflows have equal economic attributes, an economic amendment changes a candidate during processing, or consumers process events concurrently.

The described `payment_indicator` persistence value concatenates the attributes for comparison, for example:

```text
10062461|400899993|CNO|62785.000000|2024-01-12|Receive|
```

The trailing delimiter and the `CNO` example should be validated. The source narrative instead identifies `CNY` as the Stella currency that Razor converts to `CNH`.