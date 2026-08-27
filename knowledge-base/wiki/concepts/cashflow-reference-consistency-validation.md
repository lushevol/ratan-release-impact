---
type: concept
title: Cashflow Reference Consistency Validation
tags: [cashflow, Reference-ID, validation, stale-data, exception-handling, STP]
related: [trade-cashflow-reference-linkage, trade-confirmation-driven-cashflow-stp, fmo-ops, cashflow-amendment-supersession, cashflow-lifecycle-supersession-and-audit-history]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/CDU Trade Confirmation Notification & Cashflow.md"]
---
# Cashflow Reference Consistency Validation

Cashflow Reference Consistency Validation is the proposed check that compares the Reference ID in a CDU confirmation notification with the Reference ID on the latest cashflow available to Ratan.

The intended outcomes are:

- Equal Reference IDs: the cashflow may proceed to further STP checks.
- Different Reference IDs: the cashflow must not enter STP.
- Missing expected cashflow or unresolved linkage: raise an exception for [[fmo-ops]].

The validation addresses a gap in the rule:

```text
tracking_version(trade) >= tracking_version(cashflow)
```

A lower cashflow version can satisfy that comparison while still being stale if a newer amended cashflow has not arrived. Reference equality is intended to validate business correspondence more directly, but the source does not define how “latest cashflow” is determined or whether version ordering remains an additional required check.