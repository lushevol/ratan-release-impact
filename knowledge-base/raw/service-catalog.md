# Service Catalog

## Lifecycle

Lifecycle is the system of record for case status. It exposes REST endpoints for opening, pausing, resuming, and completing a case. It publishes `case.completed` only after persistence succeeds.

## Orchestration

Orchestration turns lifecycle events into a dependency-aware work plan. It calls Netting first, then SSI Stamping, and records each attempt with the shared correlation ID. It must tolerate at-least-once delivery.

## Netting

Netting calculates which obligations can settle together. It rejects a batch when currency, value date, or counterparty eligibility differs. A rejected batch is safe to retry after the source case is corrected.

## SSI Stamping

SSI Stamping validates settlement instructions against the approved counterparty profile and stores the stamped instruction version. It blocks release when an instruction is expired or has been superseded.

## Shared contracts

All services use JSON over HTTPS for synchronous calls and CloudEvents-compatible envelopes for asynchronous events. Every request includes `X-Correlation-Id`; every error includes a stable `code` and a human-readable `message`.
