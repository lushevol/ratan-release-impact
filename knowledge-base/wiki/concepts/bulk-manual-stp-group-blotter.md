---
type: concept
title: Bulk Manual STP for Group Blotter
created: 2026-08-23
updated: 2026-08-23
tags: [bulk-processing, manual-stp, cash-settlement, group-blotter, trade-validation]
related: [group-blotter, trade-major-version-manual-stp-ordering, group-blotter-cashflow-state-lifecycle, allocation-cashflow-state-handling, cashflow-migration-readiness, settlement-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter.md"]
---
# Bulk Manual STP for Group Blotter

## Definition

Bulk manual STP is the processing of multiple selected cashflow messages through the manual straight-through-processing path from the [[entities/group-blotter]]. It extends the original single-group manual-delivery flow with trade-level orchestration.

## Processing Model

1. A single group follows the original logic.
2. A multi-group request is partitioned by trade.
3. Each trade is prechecked in full before execution.
4. Groups are ordered by ascending major version.
5. Eligible groups are executed using the original group-message logic.
6. The source proposes multiple threads for execution.
7. Precheck failures are returned to the frontend as error messages.

The trade is the principal validation boundary. A selected group can be rejected because another group for the same trade has unresolved earlier work.

## Eligibility and Dependencies

The source identifies `PENDING` and `ERROR` as eligible single-group message states, provided no previous major version has pending work. Multi-group scenarios additionally use `PENDING_TRADE_VALIDATION`, `PENDING_PRE_GROUP`, and an `is_trade_validated` flag.

Later major versions cannot bypass unresolved pending cashflows in earlier major versions. Groups belonging to different trades can be processed independently in the same request.

## Outcomes

The intended outcomes include:

- Selected messages transition to `END`.
- Completed groups transition to `COMPLETED`.
- Withdrawal messages may transition to `OFFSET`.
- Successful processing records `bookingSystemEvent='ManualDeliver'`.
- Processed cashflows flow to the Cashflow Blotter.

Partial selection is supported, but the source is inconsistent about whether a group can become `COMPLETED` while unselected cashflows remain pending or in error. Track this issue in [[queries/is-group-completed-when-unselected-cashflows-remain-pending]].

## Implementation Caveats

“Multiple threads” is a proposed execution model, not a fully specified concurrency contract. Transaction boundaries, rollback, retry behavior, and cross-trade failure isolation remain undefined. The rule involving `DATA_VALIDATION_FAILED` also requires clarification.