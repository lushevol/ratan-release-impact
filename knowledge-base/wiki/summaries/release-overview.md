---
type: "Summary"
description: "Overview of Ratan Release 2026.08 coordinating four settlement services with observability."
doc_type: short
full_text: "sources/release-overview.md"
---

# Ratan Release 2026.08

The 2026.08 release coordinates four services: [[entities/lifecycle]], [[entities/netting]], [[entities/orchestration]], and [[entities/ssi-stamping]]. Its goal is to make settlement workflows observable from intake through completion while preserving existing API contracts.

## Services and Responsibilities
- **[[entities/lifecycle]]** owns case state transitions and emits a `case.completed` event.
- **[[entities/orchestration]]** consumes that event and schedules downstream work.
- **[[entities/netting]]** groups eligible obligations into settlement batches.
- **[[entities/ssi-stamping]]** validates and records settlement instructions before a batch is released.

## Key Features
- **Correlation IDs** across every service for end-to-end tracing.
- **Retry budget** of three attempts for transient downstream failures.
- **Dashboard** showing queue age and failed batches.
- **Rollback** via redeploying the previous image and replaying events from the durable event log.

## Risks and Checklist
Key risks include duplicate event delivery, stale settlement instructions, and schema mismatch between [[entities/netting]] and [[entities/orchestration]]. The checklist requires contract tests, a replay drill, and confirmation that failed batches remain visible after rollback.

## Related Concepts
- [[concepts/event-driven-architecture]]
- [[concepts/correlation-ids]]
- [[concepts/retry-budget]]
- durable event log
- observability

## Entities
- [[entities/ratan]]
