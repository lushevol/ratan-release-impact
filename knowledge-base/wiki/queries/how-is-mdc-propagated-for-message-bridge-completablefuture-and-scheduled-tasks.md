---
type: query
title: How Is MDC Propagated for Message Bridge CompletableFuture and Scheduled Tasks?
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, mdc, completablefuture, scheduled-tasks, traceid, observability]
related: [message-bridge, async-mdc-trace-context-propagation, message-bridge-trace-id-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-bridge Analysis of the problem of missing traceId in logs.md"]
---
# How Is MDC Propagated for Message Bridge CompletableFuture and Scheduled Tasks?

## Question

What is the approved context-propagation or correlation-creation policy for `DispatchProducerRoute` work launched by `CompletableFuture.runAsync()` and for `TargetDestinationStatusDetector` work launched through `@Scheduled`?

## Evidence

The source identifies both execution models as trace-context loss paths:

- `DispatchProducerRoute` uses `CompletableFuture.runAsync()`.
- `TargetDestinationStatusDetector` runs through `@Scheduled`.

The proposed solution configures only Spring `@Async` through `EventAsyncConfigurer`. It supplies no equivalent executor, wrapper, or lifecycle policy for these two paths.

## Why this matters

`CompletableFuture.runAsync()` uses the common ForkJoinPool unless an executor is supplied. MDC will not automatically transfer to those worker threads.

A scheduled job may not have an originating message context to inherit. The system may instead need to generate a unique scheduled-execution correlation ID and define its relationship, if any, to messages processed by that execution.

## Resolution criteria

- Identify the executors used by `DispatchProducerRoute` and `TargetDestinationStatusDetector`.
- Define whether each path propagates a parent `traceId` or creates a new correlation ID.
- Require capture, restore, and cleanup for any propagated MDC context.
- Define error, retry, redelivery, and concurrent-execution behavior.
- Validate the policy with automated tests and representative log evidence.