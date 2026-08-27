---
type: concept
title: Split Cashflow API Contract
tags: [api, cashflow-splitting, ratan, ssi, rounding]
related: [cashflow-splitting, split-cashflow-persistence-and-lineage, split-rule-maker-checker-lifecycle, ratan-ssi-stamping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md"]
---
# Split Cashflow API Contract

The split capability exposes manual and automatic creation, currency rounding lookup, rule administration, unsplit, and split-amount amendment operations.

Manual split accepts a parent plus child cashflows, detailed child-level nostro and vostro SSI data, and affirmation metadata. It returns a conventional status/message/data response in the supplied example. The design does not specify whether manual split validates SSI, enforces child-total equality, limits children, or provides idempotency.

Automatic split is invoked through:

```text
POST /v1/cashSettlement/cashflows/camunda/autoSplit
```

Its request consists of `trackingId` and `message`; the documented response is empty. Consequently, synchronous acknowledgement, failure semantics, asynchronous completion, and retry behavior are undefined.

The rounding endpoint provides a currency, precision, and type such as `ROUNDING_OFF`. Its supported types and behavior for missing configuration are not documented.

The unsplit operation uses a UUID-like `splittingId`, but the amend request example supplies a cashflow-like value in its `splittingId` field. This ambiguity is tracked in [[what-is-the-canonical-splitting-id-and-rule-unique-id-contract]].