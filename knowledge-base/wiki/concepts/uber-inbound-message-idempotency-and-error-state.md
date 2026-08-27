---
type: concept
title: Uber Inbound Message Idempotency and Error State
created: 2026-08-24
updated: 2026-08-24
tags: [uber, idempotency, inbound-message, error-state, group-processing, dlt]
related: [tdsx-uber-message-listener, kafka-persistent-retry-and-dlt-recovery, what-is-the-operational-recovery-process-for-uber-dlt-records, what-causes-duplicate-cashflow-ids-and-major-versions-in-uber-trades, cashflow-lifecycle-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]
---
# Uber Inbound Message Idempotency and Error State

Uber inbound processing requires durable state that survives delivery retries, terminal DLT routing, and operator-led replay. Deleting the inbound record after a processing exception removes both audit evidence and a basis for idempotent recovery.

## Persistence Scope

The source identifies three records that must be reconciled for terminal processing:

- `ratan_inbound_message` for the Uber inbound payload and processing status;
- `ratan_cashflow_group` for group lifecycle state; and
- `ratan_cashflow_group_message` for per-message group processing state.

## Terminal State Model

When retry attempts are exhausted:

| Persistence record | Expected state |
|---|---|
| `ratan_inbound_message` | `ERROR` |
| `ratan_cashflow_group_message` | `ERROR` |
| `ratan_cashflow_group` | `PENDING` |
| Downstream cashflow | Not emitted |

Reconciliation is proposed using `major_version` and cashflow event type (`New` or `Withdrawal`). Already processed data is skipped; required but incomplete work is marked as an error.

## Unspecified Idempotency Contract

The source does not provide the canonical inbound idempotency key, a database unique constraint, transaction boundaries, or an outbox/publication guarantee. Therefore, retry topics alone cannot establish duplicate-free business processing. Those controls must be explicit before DLT replay can be considered safe.