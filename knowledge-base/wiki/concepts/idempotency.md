---
type: "Concept"
sources: ["summaries/service-catalog.md", "summaries/operations-runbook.md"]
description: "Idempotency ensures repeated event processing produces the same result, preventing duplicate settlement releases."
---

# Idempotency

Idempotency is the property of an operation that can be applied multiple times without changing the result beyond the first application. In event-driven settlement systems, it ensures that duplicate events or retried messages do not create duplicate outcomes — such as releasing the same settlement batch twice.

## Role in Settlement Operations

The [[summaries/operations-runbook]] describes how operators handle duplicate completion events. The expected outcome is **one released settlement batch**. To verify correctness, operators check the event ID and the consumer idempotency record. If the idempotency record is missing, the workflow is paused and escalated to the platform owner — this prevents ambiguous state where a duplicate event might cause a second release.

## Relationship to Retries and Durable Logs

Idempotency is closely tied to [[concepts/retry-budget]] and [[concepts/durable-log]]. When a transient timeout occurs, [[entities/orchestration]] may retry up to three times with exponential backoff. Each retry must be safe — the consumer must recognize that it already processed the event. The durable event log provides the source of truth for replaying events, and idempotency records protect against side effects being applied twice during replay.

## Key Principles

- **Do not blindly retry validation errors** — correct the case or settlement instruction first, then replay the event. Idempotency applies to retries of the same event, not to re-processing invalid data.
- **Verify before assuming** — compare event IDs and idempotency records before releasing a batch.
- **Fail safe** — if the idempotency record is missing, pause and escalate rather than guessing.
- **Coordinate with correlation** — [[concepts/correlation-ids]] help trace whether a duplicate is a true duplicate or a different logical operation.

Idempotency is a core pattern in [[concepts/event-driven-architecture]], enabling reliable processing, replay, and recovery without duplicate side effects.


See also: [[summaries/service-catalog]]