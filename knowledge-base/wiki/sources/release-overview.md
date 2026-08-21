# Ratan Release 2026.08

The 2026.08 release coordinates four services: Lifecycle, Netting, Orchestration, and SSI Stamping. The release goal is to make settlement workflows observable from intake through completion while preserving existing API contracts.

Lifecycle owns case state transitions and emits a `case.completed` event. Orchestration consumes that event and schedules downstream work. Netting groups eligible obligations into settlement batches. SSI Stamping validates and records settlement instructions before a batch is released.

The release introduces correlation IDs across every service, a retry budget of three attempts for transient downstream failures, and a dashboard showing queue age and failed batches. Rollback is supported by redeploying the previous image and replaying events that remain in the durable event log.

Key risks are duplicate event delivery, stale settlement instructions, and a mismatch between the Netting batch schema and the Orchestration consumer. The release checklist requires contract tests, a replay drill, and confirmation that failed batches remain visible after rollback.
