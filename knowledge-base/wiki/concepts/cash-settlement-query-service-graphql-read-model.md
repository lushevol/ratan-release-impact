---
type: concept
title: Cash Settlement Query Service GraphQL Read Model
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, graphql, read-model, pagination, cashflow]
related: [cashflowsnew, query-service, cash-settlement-cashflow-read-model, stella, cashflow-query-response-null-semantics, cashflow-standing-settlement-instructions, trade-standing-settlement-instructions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/Cash flow query model.md"]
---
# Cash Settlement Query Service GraphQL Read Model

The Cash Settlement Query Service GraphQL read model is the client-selectable composite response exposed through [[cashflowsnew]]. It joins business and operational context around a cashflow in one request.

## Observed Composition

The source requests these result domains:

- `Cashflow`: identity, version, lifecycle, payment, netting, affirmation, STP, workflow, validation, exception, comment, and cutoff fields.
- `Trade`: trade identity, state, position, source, action, lifecycle timestamps, and settlement method.
- `Data_Flow`: publication timing and identifier, sender, source-system, domain, type, and message identifier.
- `Entity` and `Person`: booking entity, counterparty, general-ledger, marketer, and trader attributes.
- `Instrument_Common`, `Portfolio`, `Settlement_Instruction`, and `FMO_Comments`.

The observed response supplies per-record [[stella]] provenance for five sample `CashflowData` records. This does not establish Stella as the only possible source.

## Pagination

The documented contract is offset-style and zero-based: a client supplies `page` and `size`; the service returns `totalHits`, `pageNo`, `pageSize`, and `lastPage`. It does not specify ordering, maximum result size, or cursor behavior.

## Client Requirements

Consumers must treat the model as highly nullable. The sample contains missing nested objects and fields, including `Settlement_Instruction`, portfolio data, comments, and STP fields. Absent values use inconsistent encodings; see [[cashflow-query-response-null-semantics]].

Settlement-instruction projection contains account and payment-routing attributes. A client should request only needed fields and must not assume that broad field availability implies authorization. See [[what-authorization-and-masking-controls-govern-cashflowsnew-ssi-fields]].