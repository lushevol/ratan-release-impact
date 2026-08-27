---
type: entity
title: ratan_inbound_message
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, uber, inbound-message, group-management, ratanone]
related: [group-management-service, tdsx-uber-message-listener, uber-inbound-message-idempotency-and-error-state, what-is-the-ratan-inbound-message-idempotency-status-and-version-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Standardization Service.md"]
---
# ratan_inbound_message

`ratan_cashflow_group_management_service.ratan_inbound_message` persists inbound messages associated with the RATAN–Uber integration.

## Physical Contract

The table uses `id bigserial` as its primary key. It requires `correlation_id`, `trade_id`, `message`, `message_type`, timestamps, and `version`. `status` is required and defaults to `VALIDATED`.

Indexes are declared independently for `trade_id` and `correlation_id`, supporting lookup by either field.

## Limits

No unique constraint is declared on `correlation_id`, `trade_id`, `version`, or any combination of those fields. The table therefore provides storage and lookup fields but does not prove database-enforced duplicate suppression or idempotency.

The source does not define valid status values beyond the default, state transitions, message formats, version semantics, retention, replay behavior, or error handling. These questions are tracked in [[what-is-the-ratan-inbound-message-idempotency-status-and-version-contract]].

This table is relevant to [[tdsx-uber-message-listener]] and [[uber-inbound-message-idempotency-and-error-state]], but the source does not show that it implements Kafka retry or DLT recovery.