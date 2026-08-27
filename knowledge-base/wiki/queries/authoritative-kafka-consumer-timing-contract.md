---
type: query
title: What Is the Authoritative Kafka Consumer Timing Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, observability, monitoring-contract, retries, open-question]
related: [kafka-listener-consumption-time-tracking, spring-kafka-record-interceptor, kafka-consumer-timing-interceptor, ratan-central-business-monitoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka Listener Consumption Time Tracking Design Scheme.md"]
---
# What Is the Authoritative Kafka Consumer Timing Contract?

## Question

What exact timing, identity, trace-format, retry, failure, and ingestion rules should govern RATAN Kafka listener consumption-time monitoring?

## Why This Is Open

The source proposes an illustrative trace:

```text
.#|#.ms_in#ratan-cash-settlement-group-management-service_**businessDescription**#${trackingId}#Timer#end#1750063879234
```

However, it does not define whether the timing value represents record-arrival latency, listener processing duration, end-to-end latency, or time to acknowledgement or offset commit. It also does not specify the canonical header key, formal delimiters, escaping rules, versioning, or downstream parser.

## Questions to Resolve

- What are the exact start and end points for the duration?
- What clock and unit are authoritative?
- Is one event emitted per record or per delivery attempt?
- How are retries, redeliveries, failures, and dead-letter records represented?
- What happens when `trackingId` or `businessDescription` is missing or malformed?
- Which service or platform consumes the log output?
- How are trace schema changes versioned?
- What privacy, security, retention, and log-volume controls apply?
- Which Spring Kafka version and listener-container registrations are deployed?
- Is the topic-to-listener inventory complete and approved?

## Evidence

The source supports the choice of Spring Kafka `RecordInterceptor<K,V>` as the proposed interception mechanism and identifies the intended listener and topic scope. It does not resolve the operational contract.
