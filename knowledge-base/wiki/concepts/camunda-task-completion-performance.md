---
type: concept
title: Camunda Task Completion Performance
created: 2026-08-24
updated: 2026-08-24
tags: [camunda, task-completion, performance, workflow, observability]
related: [camunda, bulk-maker-checker-processing, holding-release-precheck, orchestration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result/bulk maker checker Performance Analysis.md"]
---
# Camunda Task Completion Performance

Camunda task completion is the principal residual performance concern identified in the RATANONE Cash Settlement bulk maker-checker analysis.

## Evidence

After optimization, Camunda task-table lookup reportedly decreased from approximately 1,600 ms to 1–2 ms through index-based querying. Despite this improvement, three sampled bad cases still took 9,518–10,239 ms to complete, compared with 3,408 ms for one common case.

The trace records `sleep 1.5s` for every sample during `Query task for role （task start）`. This fixed delay may be polling, synchronization, an application workaround, or test instrumentation. It should not automatically be classified as Camunda internal execution.

## Critical-path ambiguity

The final completion duration may include several distinct operations:

- Camunda task and process-engine work.
- Holding-check execution, reported at 1–6 seconds.
- Database transaction and lock waits.
- `PublishEnrichedMessageService`.
- Domain-event insertion and publication.
- `handleDomainEventForOpenSearch`.
- Status updates and downstream service calls.

The source therefore supports Camunda as a leading investigation target, but not as a conclusively isolated root cause.

## Required instrumentation

A defensible performance profile should record start and end timestamps for each component, database query plans and wait events, transaction boundaries, Camunda engine metrics, holding-check dependencies, event-publication latency, and search-indexing latency. Results should include sample size, workload characteristics, concurrency, and p50/p95/p99 measurements.
