---
type: source
title: Group Management Service Non-Eco Amendment Technical Design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratan, group-management-service, non-economic-amendment, stella, technical-design]
related: [group-management-service, cashflow, stella, non-economic-cashflow-amendment, cashflow-replacement-mapping, ratan-cashflow-mapping, ratan-cashflow-mapping-history, ratan-cashflow-message-io]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
authors: []
year: 2024
url: ""
venue: ""
---
# Group Management Service Non-Eco Amendment Technical Design

## Summary

This technical design defines intended handling for non-economic cashflow amendments received by [[group-management-service]] before workflow publication in RATAN. The service groups inbound cashflows by trade ID and major version. A group that contains both `Withdrawal` and `New` events is an amendment group; it is classified as non-economic when the paired cashflows have matching Booking Entity ID, Counterparty FM ID, Payment Currency, Payment Amount, Value Date, and Direction.

The design proposes persistent original-to-replacement cashflow mappings, mapping history, and message I/O audit storage. Its POC scenarios expect Netting and Unnetting status synchronisation with [[stella]] to follow the replacement cashflow identity and expect Pending Affirmation exceptions to remain resolvable for the original cashflow after replacement.

This is an incomplete technical design. The overall design diagram, current-workflow diagram, lifecycle response-handling design, and trade-confirmation design sections contain no substantive implementation detail. POC scenarios therefore express expected behaviour rather than a complete operational contract.

## Amendment Classification

A non-economic amendment pair consists of two cashflows in the same amendment group with equal:

- Booking Entity ID
- Counterparty FM ID
- Payment Currency
- Payment Amount
- Value Date
- Direction

The two business events must be opposite: one `Withdrawal` and one `New`.

An amendment-group cashflow set that does not satisfy this condition is described as an economic amendment. The design's stated scope is limited to non-economic amendments.

## Proposed Persistence

The source provides logical table descriptions only; it does not include executable DDL, data types, constraints, indexes, retention rules, or concurrency semantics.

### `ratan_cashflow_mapping`

| Column name | Column description | Sample Value |
| --- | --- | --- |
| id | primary key | 1720275970604654592 |
| original_cashflow_id | Cashflow id of New event | 200094700143 |
| original_business_version | Cashflow business version of New event | 0 |
| original_cashflow_version | Cashflow version of New event | 0 |
| original_major_version | Cashflow major version of New event | 1 |
| replaced_cashflow_id | Cashflow id of New event on non-eco amend | 200094700145 |
| replaced_business_version | Cashflow business version of New event on non-eco amend | 1 |
| replaced_cashflow_version | Cashflow version of New event on non-eco amend | 1 |
| replaced_major_version | Cashflow major version of New event on non-eco amend | 2 |
| source_system | Cashflow source system | STELLA |
| created_at |  |  |
| updated_at |  |  |
| version |  |  |

### `ratan_cashflow_mapping_history`

| Column name | Column description | Sample Value |
| --- | --- | --- |
| id | primary key | 1720275971888111616 |
| mapping_id | ratan_cashflow_mapping primary key | 1720275970604654592 |
| original_cashflow_id | Cashflow id of New event | 200094700143 |
| original_business_version | Cashflow business version of New event | 0 |
| original_cashflow_version | Cashflow version of New event | 0 |
| original_major_version | Cashflow major version of New event | 1 |
| replaced_cashflow_id | Cashflow id of New event on non-eco amend | 200094700145 |
| replaced_business_version | Cashflow business version of New event on non-eco amend | 1 |
| replaced_cashflow_version | Cashflow version of New event on non-eco amend | 1 |
| replaced_major_version | Cashflow major version of New event on non-eco amend | 2 |
| source_system | Cashflow source system | STELLA |
| created_at |  |  |
| updated_at |  |  |
| version |  |  |

### `ratan_cashflow_message_io`

| Column name | Column description | Sample Value |
| --- | --- | --- |
| id | primary key |  |
| header | kafka message header |  |
| content | kafka message payload |  |
| direction | message inbound or outbound | IN OUT |
| message_key | message aggregate id, tradeId\|majorVersion\|cashflowId | 15700093\|1\|M00017700002 |
| version | technical version |  |
| created_at |  |  |
| updated_at |  |  |

## POC Expectations

For a non-economic replacement of C301 by C302, the Netting status-synchronisation scenario expects the blocking-queue record to reference the replacement cashflow ID. A failed acknowledgement from Stella ambassador changes the record to `FAILED` and generates an exception. Replay after exception closure returns the record to `IN_PROGRESS`; a later successful Netting acknowledgement changes it to `SUCCESS` and automatically triggers Unnet status synchronisation.

For trade confirmation, a matching trade event is expected to close a Pending Affirmation exception. When the original cashflow is replaced through a non-economic amendment, the source expects the exception for the original cashflow to close.

## Non-Touched Payments

The design states that direct ignoring of non-economic amendments should apply only when payments have been touched by users or already settled. It explicitly expects replacement payments in `PROJECTED` or `QUEUED` status to continue to workflow.

The source does not define user-touch detection, the meaning of settled, complete status coverage, or handling for statuses beyond `PROJECTED` and `QUEUED`.

## Limitations and Open Questions

The source does not specify how an original New cashflow is selected across major versions, even though its example maps a major-version-1 original to a major-version-2 replacement. It also leaves mapping cardinality, chained-replacement handling, idempotency, database integrity, acknowledgement correlation, queue ownership, retry timing, and auto-trigger conditions unspecified.

See [[what-is-the-canonical-non-economic-amendment-matching-and-pairing-rule]], [[how-is-the-original-cashflow-selected-across-major-version-amendment-groups]], and [[what-is-the-authoritative-stella-status-sync-retry-and-acknowledgement-correlation-contract]].