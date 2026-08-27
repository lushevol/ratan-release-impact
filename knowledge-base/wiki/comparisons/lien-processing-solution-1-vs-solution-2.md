---
type: comparison
title: LIEN Processing Solution 1 vs Solution 2
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lien, architecture, workflow, trade-event-notification]
related: [lien, lien-stamping-and-re-stamping, lifecycle-service, fixing-notification-event-ordering, what-is-the-authoritative-lien-stamping-and-restamping-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LIEN Processing & Pending Fixing Flag Technical Design.md"]
---
# LIEN Processing Solution 1 vs Solution 2

## Comparison

| Dimension | Solution 1 | Solution 2 |
| --- | --- | --- |
| Workflow impact | No workflow change is proposed. | A workflow node would change and may be reusable in future scenarios. |
| LIEN stamping | LIEN stamping can occur with other attribute stamping when the target is intended to be `QUEUD + NA + NA`. | The design claims there is no re-stamping-only case. |
| Trade Event Notification | More complicated. | Simpler. |
| Documented disadvantages | Trade Event Notification complexity. | None listed in the source. |
| Evidence | High-level and low-level diagrams are empty. | The exact workflow-node change is not described. |

## Assessment

The source does not provide enough information to select a solution. The apparently one-sided comparison is likely incomplete because Solution 2 has no documented disadvantages, while its workflow change could introduce migration, operational, or compatibility risks.

The status spelling `QUEUD` appears only in the Solution 1 text; the lifecycle matrix consistently uses `QUEUED`. The canonical spelling and meaning of `QUEUED + NA + NA` require confirmation.

## Decision inputs still required

- Exact workflow-node change in Solution 2.
- Event volume and latency impact under each solution.
- Re-stamping, retry, and idempotency semantics.
- Compatibility with existing Trade Event Notification ordering and deduplication.
- Operational rollback and migration plan.
- Test evidence for all lifecycle breakpoints, especially `WAITING + Pending Fixing`.

No solution selection is recorded by the source.