---
type: concept
title: Cashflow Group and Message State Machines
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, cashflow-events, state-machine, workflow, group-management]
related: [cashflow-group-management-service, major-version-cashflow-grouping, cashflow-lifecycle-state-machine-restructuring, upstream-cashflow-replay-for-group-completion]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events.md"]
---
# Cashflow Group and Message State Machines

The design separates group-level readiness from the processing status of each message within a group.

## Group statuses

| Status | Meaning |
|---|---|
| `PENDING` | Waiting for other cashflows in the same group |
| `PENDING_PRE_GROUP` | Waiting for previous groups to consume all necessary messages |
| `READY` | All cashflows have arrived and the group is ready to process |
| `PENDING_WITHDRAWAL` | A withdrawal and a new cashflow exist, but withdrawal processing has not ended |
| `COMPLETED` | Group processing completed with no remaining dependency |
| `PENDING_TRADE_VALIDATION` | Proposed state indicating that all messages arrived but the trade has not been validated |

## Group-message statuses

| Status | Meaning |
|---|---|
| `PENDING` | Waiting for other cashflows in the same group |
| `DELIVERED` | Delivered to workflow while awaiting the withdrawal's end status |
| `END` | Completed with no pending dependency on another cashflow |
| `OFFSET` | Proposed state for new and withdrawal messages arriving while both groups are pending or awaiting trade validation |

## Inconsistencies

The source's code definitions do not fully match its status tables:

- `PENDING_TRADE_VALIDATION` appears in the prose but not in `GroupStatus`.
- `END` and `OFFSET` appear in the message-status description but not in the enum.
- The code uses `COMPLETED` for `GroupMessageStatus`, while the table uses `END`.

The canonical enum values and transition rules therefore require confirmation before implementation or operational use.