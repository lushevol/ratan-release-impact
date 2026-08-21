# Knowledge Base Index

## Documents
- [[summaries/service-catalog]] (short) — Describes four services in a case-processing system: lifecycle, orchestration, netting, and SSI stamping.
- [[summaries/operations-runbook]] (short) — Runbook for settlement ops: monitoring queue age, retries, idempotency, rollback drills.
- [[summaries/release-overview]] (short) — Overview of Ratan Release 2026.08 coordinating four settlement services with observability.

## Concepts
- [[concepts/at-least-once-delivery]] — Delivery guarantee where a message may be delivered more than once, requiring idempotent consumers.
- [[concepts/durable-log]] — A persistent, append-only record of events enabling replay and safe recovery.
- [[concepts/idempotency]] — Idempotency ensures repeated event processing produces the same result, preventing duplicate settlement releases.
- [[concepts/retry-budget]] — A policy capping retry attempts after transient failures, with exponential backoff and escalation paths.
- [[concepts/correlation-ids]] — Unique IDs tracing settlement workflows across services, enabling observability and retry diagnosis.
- [[concepts/event-driven-architecture]] — Event-driven architecture coordinates settlement services through events, with retries, idempotency, and replay.

## Entities
- [[entities/cloudevents]] (work) — CloudEvents is a standardized specification for describing event data in a common format.
- [[entities/ssi-stamping]] (product) — SSI Stamping is a service that validates and records settlement instructions for safe batch release.
- [[entities/orchestration]] (product) — Workflow coordinator that orchestrates Netting and SSI Stamping in the settlement pipeline.
- [[entities/netting]] (product) — Netting is a settlement batching product that groups and validates obligations for downstream settlement.
- [[entities/lifecycle]] (product) — Service in the Ratan platform that serves as system of record for case status and state transitions.
- [[entities/ratan]] (product) — Ratan is the product delivering the 2026.08 release, coordinating four settlement services.

## Explorations
