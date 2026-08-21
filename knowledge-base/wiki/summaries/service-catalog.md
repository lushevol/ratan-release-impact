---
type: "Summary"
description: "Describes four services in a case-processing system: lifecycle, orchestration, netting, and SSI stamping."
doc_type: short
full_text: "sources/service-catalog.md"
---

# Service Catalog Summary

This document provides an overview of a service catalog for a case-processing platform. It describes four core services — Lifecycle, Orchestration, Netting, and SSI Stamping — along with the shared contracts that govern their interactions. The catalog emphasizes reliability, [[concepts/idempotency|idempotency]], and traceability in a distributed, [[concepts/event-driven-architecture|event-driven]] architecture.

## Key Services

- **Lifecycle** — The system of record for case status. It exposes REST endpoints to open, pause, resume, and complete a case. Crucially, it publishes the `case.completed` event only after persistence succeeds, ensuring that downstream consumers see a consistent view. Related: [[entities/lifecycle]].
- **Orchestration** — Translates lifecycle events into a dependency-aware work plan. It invokes services in a specific order (Netting first, then SSI Stamping) and records every attempt with a shared [[concepts/correlation-ids|correlation ID]]. It must tolerate [[concepts/at-least-once-delivery]], meaning retries are expected and safe.
- **Netting** — Determines which obligations can settle together in a batch. A batch is rejected if currency, value date, or counterparty eligibility differ. Rejected batches can be retried after the source case is corrected, making the operation [[concepts/idempotency|idempotent]]. Related: [[entities/netting]].
- **SSI Stamping** — Validates settlement instructions against the approved counterparty profile and stores the stamped instruction version. It blocks release when an instruction is expired or superseded, enforcing freshness and authorization. Related: [[entities/ssi-stamping]].

## Shared Contracts

All synchronous calls use **JSON over HTTPS**, while asynchronous events use [[entities/cloudevents|CloudEvents]]-compatible envelopes. Every request carries an `X-Correlation-Id` for end-to-end tracing. Every error response includes a stable `code` and a human-readable `message`, aiding debugging and automation. This design supports a consistent, observable system. Related concepts: [[concepts/event-driven-architecture]], [[concepts/correlation-ids]].

## Implications

- The catalog reflects a **reliable eventing** pattern: state changes are published only after durable persistence.
- **Dependency-aware [[entities/orchestration|orchestration]]** ensures correct ordering and failure isolation.
- **[[concepts/idempotency|Idempotent]] retries** and **[[concepts/correlation-ids|correlation IDs]]** are foundational for distributed operations.

This summary condenses the document's main ideas; for full details, refer to the original source document.

## Related Concepts
- [[concepts/idempotency]]
- [[concepts/retry-budget]]

## Entities
- [[entities/cloudevents]]
- [[entities/orchestration]]
- [[entities/ratan]]
