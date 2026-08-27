---
type: entity
title: Cashflow Group Management Service
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, cash-settlement, service, group-management, Kafka]
related: [ratanone, group-management-service, scbml, major-version-cashflow-grouping, cashflow-group-and-message-state-machines]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events.md"]
---
# Cashflow Group Management Service

The Cashflow Group Management Service is a proposed RATANONE service for consuming SCBML cashflow events, grouping them by trade ID and major version, and controlling when groups are released to workflow.

## Responsibilities

The design assigns the service these responsibilities:

- Consume SCBML events through a Kafka consumer.
- Detect the group flag composed of major version, trade ID, and cashflow count.
- Group events by `(tradeId, majorVersion)`.
- Wait until all expected cashflow events in a group have arrived.
- Prevent processing while a previous major-version group remains pending.
- Publish complete and eligible groups to workflow.
- Pass events directly into the existing flow when the SCBML event has no group flag.
- Provide APIs for UI queries by trade ID, cashflow ID, and major version.
- Resume later groups after predecessor groups reach an eligible terminal state.

The design associates this work with JIRA `RATAN-14250`.

## State coordination

At group level, the proposed states include `PENDING`, `PENDING_PRE_GROUP`, `READY`, `PENDING_WITHDRAWAL`, `COMPLETED`, and a proposed `PENDING_TRADE_VALIDATION`. At message level, the design uses `PENDING`, `DELIVERED`, and completion-oriented states such as `END` or `COMPLETED`.

The source does not define the canonical persistence schema, expected-count algorithm, duplicate handling, retry policy, or recovery behavior for missing messages. See [[concepts/cashflow-group-and-message-state-machines]].