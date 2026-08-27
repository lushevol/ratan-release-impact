---
type: concept
title: Cashflow Splitting-ID Correlation
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, split, correlation, database, deprecated]
related: [cashflow-split-and-unsplit, trade-cashflow-reference-linkage, cashflow-event-versioning, what-is-the-authoritative-meaning-and-lifecycle-of-cashflow-splitting-id]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Split design -delete.md"]
---
# Cashflow Splitting-ID Correlation

Cashflow splitting-ID correlation is a historical, proposed persistence mechanism in which `cashflow__splitting_id` distinguishes records associated with the same `cashflow__cashflow_id`.

A deprecated migration for `cash_netting_service.t_cashflow` defines a unique constraint over:

```text
(cashflow__cashflow_id, cashflow__splitting_id)
```

This constraint scopes splitting-ID uniqueness to a cashflow ID rather than making the splitting ID globally unique. It allows multiple records with the same cashflow ID when their splitting IDs differ.

## Default representation

The proposed field is `NOT NULL` and defaults to `''`. This could indicate an unsplit record, but the source does not formally establish that meaning. It may also be ambiguous between an unsplit state, an unknown splitting ID, or a legacy record without backfilled split data.

## Limits of evidence

The source does not state whether `cashflow__splitting_id` identifies a split operation, a component group, a parent cashflow, or another correlation key. It also supplies no rules for split, unsplit, amendment, withdrawal, or netting events.

This is a historical implementation detail related to [[cashflow-split-and-unsplit]], not evidence of a current business lifecycle or versioning contract. The unresolved meaning and lifecycle are tracked in [[what-is-the-authoritative-meaning-and-lifecycle-of-cashflow-splitting-id]].