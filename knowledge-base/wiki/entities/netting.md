---
sources: ["summaries/service-catalog.md", "summaries/operations-runbook.md", "summaries/release-overview.md"]
type: "Product"
description: "Netting is a settlement batching product that groups and validates obligations for downstream settlement."
---

# Netting

**Netting** is one of the four services coordinated in the [[summaries/release-overview]] release. It calculates which obligations can settle together and groups eligible obligations into settlement batches, which are then released for downstream processing.

## Role in the Release
- Groups eligible obligations into settlement batches.
- Works alongside [[entities/lifecycle]], [[entities/orchestration]], and [[entities/ssi-stamping]].
- Called first by Orchestration before SSI Stamping; each attempt is recorded with a shared correlation ID.
- Emits or relies on batch-related data consumed by Orchestration.
- In operations, Netting is one of the first services checked when queue age exceeds ten minutes: operators inspect the [[concepts/correlation-ids|correlation ID]] to determine whether work is waiting on Netting or on [[entities/ssi-stamping]].

## Key Facts
- Netting validates a batch by currency, value date, and counterparty eligibility; if any of these differ, the batch is rejected.
- A rejected batch is safe to retry after the source case is corrected, making Netting operations [[concepts/idempotency|idempotent]] in nature.
- Netting batches are released only after SSI Stamping validates and records settlement instructions.
- A known risk in the release is a mismatch between the Netting batch schema and the Orchestration consumer.
- Failed batches must remain visible after rollback, as required by the release checklist.
- Transient timeouts in Netting can be retried by Orchestration up to three times with exponential backoff; validation errors must not be blindly retried — the case or settlement instruction must be corrected and the event replayed from the [[concepts/durable-log|durable log]].
- Duplicate completion events for a Netting batch are checked against the event ID and consumer [[concepts/idempotency|idempotency]] record; the expected result is one released settlement batch. If the record is missing, the affected workflow is paused.
- During rollback, Netting batch visibility and the durable event log must be preserved; the replay drill is run against a single test case before resuming production traffic.

## Related Concepts
- [[concepts/event-driven-architecture]]
- [[concepts/correlation-ids]]
- [[concepts/retry-budget]]
- [[concepts/durable-log]]
- [[concepts/idempotency]]

See the overall release summary in [[summaries/release-overview]] and the operational runbook in [[summaries/operations-runbook]]. The service is also described in [[summaries/service-catalog]].