---
type: query
title: Which Cash Settlement Actions Publish Domain Events Versus Process Messages?
created: 2026-08-24
updated: 2026-08-24
tags: [domain-events, kafka, process-in, lifecycle, orchestration]
related: [uber-restructured-workflow-integration, cashflow-lifecycle-state-machine-restructuring, eventual-consistency-for-cashflow-exceptions-and-swift-status, orchestration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing.md"]
---
# Which Cash Settlement Actions Publish Domain Events Versus Process Messages?

The source proposes that lifecycle actions including `ResendToRazor`, `ReGenerateSwift`, and `EarlyRelease` publish no data except a domain event. It separately records missing `process_in` publication for `NetNew` and unsuppress flows.

The resulting publication boundary between lifecycle, [[orchestration]], and downstream Kafka processing is unresolved.

## Actions requiring an explicit contract

- `ResendToRazor`
- `ReGenerateSwift`
- `EarlyRelease`
- `RevertToQueued`
- `ReInstate`
- `NetNew`
- Manual unsuppress and manual Swift unsuppress
- Materialize and release batch-job actions

## Resolution criteria

For every action, define persistence behaviour, emitted domain event, processing-message topic when applicable, publisher, idempotency key, retry policy, and expected consumer outcome.