---
type: concept
title: Camunda Task Completion Bottleneck
created: 2026-08-24
updated: 2026-08-24
tags: [camunda, task-completion, performance, workflow, checker, cash-settlement]
related: [bulk-exception-processing-performance, camunda, orchestration, rule-engine-vs-workflow-orchestration, cashflow-based-user-task-indexing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result.md"]
---

# Camunda Task Completion Bottleneck

The RATANONE Cash Settlement checker path identifies `taskService.complete` as the largest measured component of checker-operation latency.

## Measured contribution

The reported checker-operation breakdown assigns:

- `taskService.complete`: 4,336 ms.
- `checkUserLimitBasedProfileAccess`: 829 ms.
- `userTaskService.queryActiveTask`: 534 ms across three calls.
- `statusUpdateService.getLatestSCBMLMessage`: 120 ms across three calls.
- `authServerClient.getUserEntitlement`: 100 ms.
- `commonServiceCaller.execute`: 163 ms.
- Total reported time: 6,742 ms.

Some component timings are unspecified, and the source does not state whether the values are additive or nested. The figures nevertheless identify task completion as the first optimization target.

## Listener path

During completion, `CompleteTaskListener` reportedly:

1. Sleeps for approximately 1.5 seconds.
2. Accesses `userTask`.
3. Calls `getLatestSCBMLMessage`.
4. Performs additional operations.

The listener therefore extends the synchronous approval path beyond the core Camunda persistence operation.

## Optimization direction

The source proposes optimizing `taskService.complete` and making Camunda completion asynchronous, particularly where approval is responsible for saving task data. Any such change requires explicit handling for:

- User-visible approval status.
- Retry and duplicate-submission behavior.
- Failure reporting.
- Ordering and consistency between task completion and related status updates.
- Recovery of work accepted by the request but not completed by the background operation.

The source also notes that changing the implementation from asynchronous to synchronous, or vice versa, requires coordination with another implementation owner.

## Relationship to rule evaluation

The measured results distinguish workflow completion from profile limitation checking. The rule-related `checkLimitationsBatch` endpoint is much faster than the checker endpoint, so rule evaluation should not be assumed to be the primary source of bulk checker latency.
