---
type: concept
title: Kafka Consumer Poll Timeout
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, consumer, polling, timeout, consumer-lag]
related: [ratanone-trade-service, environment-specific-kafka-consumer-configuration, what-kafka-consumer-settings-and-processing-slo-apply-to-trade-service-fx-replicate]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka consumer issue for large lag during drop3 migration testing.md"]
---
# Kafka Consumer Poll Timeout

A Kafka consumer poll timeout occurs when the elapsed time between successive calls to `poll()` exceeds `max.poll.interval.ms`. It commonly indicates that the consumer's poll loop is spending too long processing a fetched batch.

## Evidence in Trade Service

The source records this warning for consumer group `ratanone-trade-service-fx-replicate` in [[ratanone-trade-service]] on 19 March 2024. It directly establishes a polling-interval breach in that consumer group.

It does not establish the specific cause of long processing time or quantify the resulting consumer lag.

## Mitigation Levers

The Kafka warning cited by the source identifies two potential responses:

- Increase `max.poll.interval.ms` to permit a longer processing interval.
- Reduce `max.poll.records` to reduce the maximum batch returned by `poll()`.

The reported implementation adjusted `max.poll.interval.ms` and `session.timeout.ms`, and optimized SCBML-to-JSON parsing. The source does not state whether `max.poll.records` was changed or assessed.

## Distinguishing Session Timeout

`session.timeout.ms` governs consumer-session failure detection. It is distinct from the poll-interval limit that was named in the warning. Although the source reports both settings as part of [[environment-specific-kafka-consumer-configuration]], it provides no direct evidence that changing `session.timeout.ms` resolved the observed poll timeout.

## Operational Interpretation

Increasing a poll interval can prevent eviction due to long processing, but it does not by itself reduce processing latency or establish adequate throughput. Evaluation should include peak lag, processing duration, batch size, partition assignment, consumer concurrency, and recovery behavior.