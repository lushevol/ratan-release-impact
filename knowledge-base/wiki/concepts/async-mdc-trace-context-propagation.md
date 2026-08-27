---
type: concept
title: Asynchronous MDC Trace Context Propagation
created: 2026-08-24
updated: 2026-08-24
tags: [mdc, traceid, asynchronous-processing, thread-pools, logging, observability]
related: [message-bridge, message-bridge-trace-id-lifecycle, ratan-central-business-monitoring, kafka-consumer-timing-interceptor, kafka-listener-consumption-time-tracking]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-bridge Analysis of the problem of missing traceId in logs.md"]
---
# Asynchronous MDC Trace Context Propagation

MDC is thread-local logging context. A `traceId` added to MDC on one thread is not automatically available to work executed on another thread unless the framework propagates it or the application captures and restores it.

For Message Bridge, this distinction is operationally important: a message can retain its business data while losing the log-correlation field required to reconstruct the processing chain.

## Required lifecycle

Correct asynchronous handling has four separate stages:

1. **Initialize** a correlation value before logs that need it are emitted.
2. **Capture and propagate** the relevant MDC context when work crosses a thread boundary.
3. **Restore** context from a captured map or durable message/Exchange state in the destination thread.
4. **Clear** MDC on reused worker threads after execution, including failure paths, to prevent one task's context leaking into another task.

## Framework boundaries

The source identifies different handling requirements by execution model:

- Apache Camel may propagate selected Exchange properties when Camel MDC logging is enabled, subject to deployed-version and executor behavior.
- Spring `@Async` requires an MDC-aware executor, such as a `TaskDecorator` that snapshots MDC at task submission.
- `CompletableFuture.runAsync()` requires an explicitly supplied context-aware executor or a wrapper; no solution is documented for the Message Bridge path.
- `@Scheduled` work may not have an originating message context. It should have an explicit policy defining whether it starts a new execution correlation ID or receives context by another means.

## Worker-thread hygiene

A task decorator should establish a known MDC state before invoking the task and clear it afterward:

```java
Map<String, String> mdcContext = MDC.getCopyOfContextMap();
return () -> {
    if (mdcContext != null) {
        MDC.setContextMap(mdcContext);
    } else {
        MDC.clear();
    }
    try {
        runnable.run();
    } finally {
        MDC.clear();
    }
};
```

The source's proposed Spring implementation includes cleanup in `finally`, but only restores a context map when one exists. Establishing an empty MDC state before work begins is safer against contaminated pooled threads.

## Relationship to operational monitoring

MDC trace correlation complements [[kafka-consumer-timing-interceptor|Kafka consumer timing interception]] and [[kafka-listener-consumption-time-tracking|Kafka listener consumption-time tracking]]. Timing instrumentation measures processing duration; trace propagation ties log records from one message flow together across services and threads.