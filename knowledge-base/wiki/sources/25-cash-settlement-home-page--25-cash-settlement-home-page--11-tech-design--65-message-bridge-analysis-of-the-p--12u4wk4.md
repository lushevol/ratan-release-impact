---
type: source
title: Message Bridge Analysis of Missing traceId in Logs
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, traceid, logging, mdc, apache-camel, spring-async, observability]
related: [message-bridge, async-mdc-trace-context-propagation, message-bridge-trace-id-lifecycle, how-is-mdc-propagated-for-message-bridge-completablefuture-and-scheduled-tasks, is-manual-traceid-restoration-required-after-enabling-camel-mdc-logging, scbml, fxu, ratan-central-business-monitoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-bridge Analysis of the problem of missing traceId in logs.md"]
---
# Message Bridge Analysis of Missing traceId in Logs

This internal technical-design note diagnoses missing `traceId` values in Message Bridge logs, including production logs. The identified operational impact is broken end-to-end correlation for message-processing chains.

The source attributes the issue primarily to the thread-local scope of MDC. Context can be absent either because it was never initialized on a route branch or because execution moved to a different thread without context propagation.

## Affected execution paths

The source identifies these context-loss scenarios:

- `TargetSplittingRoute` uses Camel `split().parallelProcessing()`, which processes split messages on separate threads.
- `EventProducerRoute` uses Spring `@Async`.
- `TargetDestinationStatusDetector` runs through `@Scheduled`.
- `DispatchProducerRoute` uses `CompletableFuture.runAsync()`.

An additional non-async initialization gap exists for empty-body messages: the route records `trackingId` in an Exchange property but does not invoke `MDC.put()`.

## Proposed remediation

The design proposes four measures:

1. Configure Apache Camel MDC logging in `MessageBridgeApplication`, including `traceId`, `trackingId`, and `flowName`.
2. Standardize application MDC usage on `org.slf4j.MDC` rather than `org.jboss.logging.MDC`.
3. Initialize a preliminary identifier at consumer-route ingress, then permit `TrackingIdProcessor` to replace it with the business `trackingId`.
4. Capture and restore MDC for Spring `@Async` execution through a `ThreadPoolTaskExecutor` `TaskDecorator`.

The document also proposes explicit header propagation and restoration in the split route. This overlaps with the claim that Camel MDC logging handles Camel thread transitions. The source does not establish whether both mechanisms are required.

## Proposed Camel configuration

```java
// MessageBridgeApplication.java
@Override
public void afterPropertiesSet() throws Exception {
    if (this.camelContext != null) {
        this.camelContext.setNameStrategy(new DefaultCamelContextNameStrategy("Message-Bridge-CamelContext"));
        this.camelContext.getExecutorServiceManager().setThreadNamePattern("CamelThread-##counter#");
        this.camelContext.setMessageHistory(false);

// ① Enable Camel MDC logging to automatically synchronize Exchange properties to the MDC.
        this.camelContext.setUseMDCLogging(true);
        // ② Specify which Exchange Properties need to be synchronized to MDC
        this.camelContext.setMDCLoggingKeysPattern("traceId,trackingId,flowName");
    }
}
```

## Proposed ingress initialization

```java
// AbstractConsumerClientRouteBuilder.initRoute() 
from(camelRoute).noAutoStartup().routeId(routeId).startupOrder(StartOrderLevel.SECOND.order())
    .log(...)
    // Immediately after receiving a message, the route generates a temporary traceId and writes it to the Exchange Property.
    // Subsequently, the TrackingIdProcessor will overwrite it with the actual trackingId from the message.
    .process(exchange -> {
        String earlyTraceId = exchange.getIn().getHeader("JMSMessageID", String.class);
        if (earlyTraceId == null) {
            earlyTraceId = exchange.getIn().getHeader(KafkaConstants.OFFSET,
                    exchange.getExchangeId(), Object.class).toString();
        }
        exchange.setProperty("traceId", earlyTraceId);
        MDC.put("traceId", earlyTraceId);
    })
    .setProperty(IGNORE_SOURCE_RAW_MESSAGE_PROPERTY, ...)
```

The identifier contract remains undefined. `JMSMessageID`, Kafka offset, and Camel Exchange ID have different uniqueness scopes, while replacement by `trackingId` means a single flow can produce logs under more than one value.

## Proposed split-route propagation

```java
// TargetSplittingRoute.EndpointSplitter
for (TargetEndpoint endpoint : endpointProperty) {
    DefaultMessage message = new DefaultMessage(camelContext);
    message.setHeaders(new HashMap<>(exchange.getIn().getHeaders()));
    // Pass traceId into sub-message
    message.setHeader("traceId", exchange.getProperty("traceId", String.class));
    message.setHeader(BRIDGE_FLOW_ID, endpoint.getTarget().getItemId());
}
```

```java
from(MessageBridgeConstants.DIRECT_SUPPRESSION_ROUTE)
    .routeId(thisRouteBuilderId())
    .startupOrder(StartOrderLevel.FIRST.order())
    // Sub-thread recovery MDC traceId
    .process(exchange -> {
        String traceId = exchange.getIn().getHeader("traceId", String.class);
        if (traceId != null) {
            MDC.put("traceId", traceId);
            exchange.setProperty("traceId", traceId);
        }
    }).id("restoreMdcTraceIdProcessor")
    .process(exchange -> {
        final TargetEndpoint targetEndpoint = ...;
        log.info("...");
    }).id("suppressionMsgInLogProcessor")
```

## Proposed Spring async executor

```java
@Component
public static class EventAsyncConfigurer implements AsyncConfigurer {

@Override
    public Executor getAsyncExecutor() {
        // Wrap the thread with an MDC-aware TaskDecorator to ensure that the @Async thread inherits the MDC of the calling thread.
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setTaskDecorator(runnable -> {
            // Capture the current MDC when submitting a task
            Map<String, String> mdcContext = MDC.getCopyOfContextMap();
            return () -> {
                // Restore MDC while performing tasks
                if (mdcContext != null) {
                    MDC.setContextMap(mdcContext);
                }
                try {
                    runnable.run();
                } finally {
                    MDC.clear();
                }
            };
        });
        executor.setThreadNamePrefix("EventThread-");
        executor.initialize();
        return executor;
    }
}
```

The `finally` cleanup prevents context leakage from worker-thread reuse. Explicitly clearing MDC before execution when the captured context is null should also be considered.

## Validation evidence

The note reports screenshot-based validation in:

- Uber, `uat4`
- [[scbml|SCBML]], `fmrp1`
- [[fxu|FXU]], `uat4`

This indicates manual validation was attempted. It does not demonstrate merged implementation status, route-by-route coverage, quantitative improvement, retry and error-path behavior, or production readiness.

## Unresolved coverage

The source diagnoses but does not provide a solution for:

- MDC propagation through `CompletableFuture.runAsync()` in `DispatchProducerRoute`.
- Correlation behavior for `@Scheduled` work in `TargetDestinationStatusDetector`.
- Apache Camel runtime-version compatibility for the proposed MDC APIs.
- Canonical, stable semantics for the initial and business-level correlation identifiers.

See [[how-is-mdc-propagated-for-message-bridge-completablefuture-and-scheduled-tasks]] and [[is-manual-traceid-restoration-required-after-enabling-camel-mdc-logging]].