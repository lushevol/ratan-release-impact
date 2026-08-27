---
type: query
title: Is Manual traceId Restoration Required After Enabling Camel MDC Logging?
created: 2026-08-24
updated: 2026-08-24
tags: [apache-camel, mdc, traceid, parallel-processing, message-bridge]
related: [message-bridge, async-mdc-trace-context-propagation, message-bridge-trace-id-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-bridge Analysis of the problem of missing traceId in logs.md"]
---
# Is Manual traceId Restoration Required After Enabling Camel MDC Logging?

## Question

After `MessageBridgeApplication` enables `setUseMDCLogging(true)` and configures `setMDCLoggingKeysPattern("traceId,trackingId,flowName")`, is explicit `traceId` header transfer in `TargetSplittingRoute` and MDC restoration in `SuppressionRouteBuilder` still required?

## Evidence

The source makes two related proposals:

- Camel MDC logging automatically synchronizes selected Exchange properties and transfers MDC through Camel thread switches, including `parallelProcessing()`.
- The split route should explicitly copy `traceId` to child-message headers, and the suppression route should explicitly restore the header to MDC and the Exchange property.

These approaches may be complementary if child messages are constructed outside the ordinary Exchange propagation path. The source does not explain whether this is the reason, nor does it identify a Camel version-specific limitation.

## Resolution criteria

- Record the deployed Apache Camel version and relevant executor configuration.
- Reproduce the split route with Camel MDC logging enabled, both with and without manual restoration.
- Verify behavior for custom `DefaultMessage` creation, retries, exceptions, and nested route transitions.
- Select one authoritative mechanism or document the conditions requiring both.
- Ensure the selected mechanism cannot restore stale or conflicting values.