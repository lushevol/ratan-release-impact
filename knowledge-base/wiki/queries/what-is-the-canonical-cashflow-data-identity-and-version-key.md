---
type: query
title: What Is the Canonical cashflow_data Identity and Version Key?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, query-service, identity, versioning, data-quality, open-question]
related: [cashflow-data, cashflow-data-history, what-is-the-authoritative-current-and-history-lifecycle-for-cashflow-data, cash-settlement-cashflow-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design.md"]
---
# What Is the Canonical `cashflow_data` Identity and Version Key?

The schema exposes several identity and version candidates without declaring which combination identifies a business cashflow, a source event, a read-model row, or a historical version.

## Candidate fields

The candidates include:

- `id`
- `cashflow_id`
- `cashflow__cashflow_id`
- `cashflow_index`
- `cashflow_cashflow_business_version`
- `cashflow_cashflow_version`
- `cashflow__cashflow_business_version`
- `cashflow__cashflow_version`
- `cashflow_minor_version`
- `cashflow__cashflow_minor_version`
- `cashflow__cashflow_audit_version`
- `trade__trade_version`
- `data_flow__unique_identifier_message_id`
- `data_flow__data_publication_id`

Only `id` is declared as a primary key. No unique constraints are defined for business identifiers, version combinations, message identifiers, or publication identifiers.

## Questions

The service needs to document:

- The canonical business identity of a cashflow.
- The distinction between envelope fields and flattened payload fields.
- Whether duplicate-looking fields are compatibility fields, distinct values, or accidental duplication.
- The version used for current-row selection.
- The version used for history ordering.
- Idempotency and replay keys.
- Stale-event and out-of-order-event handling.
- Uniqueness constraints and validation rules.

Until these questions are resolved, duplicate records and ambiguous update ordering cannot be assessed from the DDL alone.