---
type: "Concept"
sources: ["summaries/operations-runbook.md"]
description: "A persistent, append-only record of events enabling replay and safe recovery."
---

# Durable Log

The **durable log** is an append-only, persistent record of every event that has occurred in a system. It serves as the system of record for event-driven processing, enabling replay, audit, and recovery after failures or manual corrections.

## Role in Event-Driven Architecture

In [[concepts/event-driven-architecture]], the durable log is the backbone that decouples producers from consumers. Events are written to the log before being processed, guaranteeing that no event is lost and that consumers can re-read events at any point. This supports exactly-once or at-least-once semantics depending on consumer design.

The durable log also supplies the raw material for **replay**: when a message is corrected or a validation error is fixed, the event is replayed from the log rather than being re-sent from scratch. This ensures the exact same event payload is processed again, preserving traceability.

## Key Properties from the Runbook

From the [[summaries/operations-runbook]], the durable log plays a critical role in several operational procedures:

- **Retry and replay**: After a validation error is corrected, the event is replayed from the durable log. This avoids blind retries and keeps the event history consistent.
- **Rollback safety**: During a rollback, the durable event log is preserved so that no events are lost, and a replay drill can be performed against a test case before resuming production.
- **Audit and correlation**: The durable log works alongside [[concepts/correlation-ids]] to trace an event from ingestion through processing. Every retry or replay references the same correlation ID, making it possible to reconstruct the full lifecycle of a settlement release.

## Relationship to Idempotency

The durable log is tightly coupled with [[concepts/idempotency]]. When duplicate completion events appear, operators check the event ID and the consumer's idempotency record. The durable log provides the authoritative sequence of events, while idempotency ensures that consuming the same event twice produces only one released settlement batch. If an idempotency record is missing, the workflow is paused and escalated — the durable log is used to verify what actually happened.

## Operational Impact

The durable log is not merely a storage mechanism; it is an operational safety net. It allows operators to:

- Inspect event timestamps against service logs
- Replay corrected events without data loss
- Run replay drills during rollbacks
- Preserve evidence for post-incident analysis

In practice, this means that the durable log shifts recovery from "re-send the message" to "re-read the log," which is far more reliable and auditable. Properly maintaining the durable log is therefore a prerequisite for resilient event-driven operations.

## See Also

- [[concepts/event-driven-architecture]]
- [[concepts/idempotency]]
- [[concepts/correlation-ids]]
- [[concepts/retry-budget]] (for retry policies that respect the log)
- [[summaries/operations-runbook]]