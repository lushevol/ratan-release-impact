---
type: query
title: Which Indexes and Data-Retention Controls Are Required for Cashflow Query Tables?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, query-service, postgresql, indexing, retention, data-protection, open-question]
related: [cashflow-data, cashflow-data-history, denormalized-cashflow-query-read-model, cash-settlement-cashflow-read-model, postgresql, what-is-the-authoritative-current-and-history-lifecycle-for-cashflow-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design.md"]
---
# Which Indexes and Data-Retention Controls Are Required for Cashflow Query Tables?

The supplied DDL defines primary keys on `id` but no secondary indexes, partitioning, retention policy, archival process, or data-protection controls.

## Indexing questions

Workload evidence is needed to determine whether indexes are required for:

- Cashflow and trade identifiers.
- Payment date and event date.
- Status, sub-status, validation, STP, and NSTP fields.
- Netting identifiers.
- Booking entity, counterparty, portfolio, and settlement method.
- Source publication and message identifiers.
- Creation, update, and provenance timestamps.
- History lookups by business identity and version.

Index choices should be validated against actual predicates, sort requirements, cardinality, write volume, and current query-performance evidence. The source itself contains no query plans or performance measurements.

## Retention and protection questions

The tables contain account numbers, BIC codes, names, addresses, remittance data, and payment-message content. The service should establish:

- Role-based access and least-privilege query permissions.
- Field masking or redaction for sensitive exports.
- Encryption and secret-management requirements.
- Audit logging for access and changes.
- Retention and deletion rules for current and historical records.
- Partitioning or archival strategy for history.
- Environment-specific controls for copied or test data.

The required controls should be decided together with the current/history lifecycle in [[what-is-the-authoritative-current-and-history-lifecycle-for-cashflow-data]].