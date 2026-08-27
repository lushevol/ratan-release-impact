---
type: concept
title: Cashflow Expiry Event Filtering
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, expiry, filtering, versioning, stella, ratan, deprecated]
related: [cashflow-events-control-draft2, stella, ratan, cashflow-status-lifecycle, cashflow-lifecycle-supersession-and-audit-history, what-is-the-authoritative-ratan-expiry-filtering-key-and-version-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft2.md"]
---
# Cashflow Expiry Event Filtering

The deprecated Cashflow Events Control Draft2 proposes that [[stella]] expiry processing on VD+1 creates a later physical cashflow version with `Physical Status = Dead`, and that [[ratan]] filters that new expiry record instead of replacing the prior operational record.

## Proposed behavior

The proposal applies to prior records that are:

- `FAILED` on value date;
- `RELEASED` or `SETTLED`;
- `NETTED`; or
- `SPLIT`.

Ratan is expected to retain and continue using the prior record, rather than act on the expiry-created `Dead` version.

## Unresolved contract

The draft does not specify the filtering key or precedence model. In particular, it does not establish how `Business Version`, `Cashflow Version`, `Ratan Version`, physical status, event ordering, and lifecycle status interact.

This is a historical, non-authoritative proposal. The required current behavior is tracked in [[what-is-the-authoritative-ratan-expiry-filtering-key-and-version-model]].