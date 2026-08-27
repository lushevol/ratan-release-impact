---
type: source
title: Kafka Consumer Issue for Large Lag During Drop3 Migration Testing
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, consumer-lag, drop3, migration-testing, eks, trade-service]
related: [ratanone-trade-service, kafka-consumer-poll-timeout, environment-specific-kafka-consumer-configuration, what-kafka-consumer-settings-and-processing-slo-apply-to-trade-service-fx-replicate, tds3, rule-service, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka consumer issue for large lag during drop3 migration testing.md"]
authors: []
year: 2024
url: ""
venue: "Internal technical design"
---
# Kafka Consumer Issue for Large Lag During Drop3 Migration Testing

## Summary

During Drop3 migration testing, `ratanone-trade-service` experienced delayed Kafka consumption in EKS, while UAT was reported to operate normally. A Kafka warning on 19 March 2024 established that consumer group `ratanone-trade-service-fx-replicate` exceeded its configured `max.poll.interval.ms`.

The reported remediation combined environment-specific Kafka client settings with an optimization of the FX-replication path: [[rule-service]] parses [[scbml]] to JSON using a newer library upgraded from [[tds3]]. The source reports that both changes were deployed and that a rerun beginning on “5/9” found no Trade service lag or delay. The date is ambiguous but is likely 9 May 2024 based on the attached-image name.

The warning confirms a missed polling interval. The proposed contributors—high TDS3 message volume, EKS capacity relative to UAT, and more complex FX-replication processing—remain unquantified hypotheses rather than demonstrated root causes.

## Observed Kafka Warning

```text
Mar 19, 2024 @ 17:09:02.860
log: {"@timestamp":"2024-03-19T09:09:02.859Z","sequence":323166,"level":"WARN","logger_name":"org.apache.kafka.clients.consumer.internals.ConsumerCoordinator","hostname":"ratanone-trade-service-594979864d-2ggxh","appName":"ratanone-trade-service","port":"8080","PID":"7","thread":"kafka-coordinator-heartbeat-thread | ratanone-trade-service-fx-replicate","message":"[Consumer clientId=consumer-ratanone-trade-service-fx-replicate-2, groupId=ratanone-trade-service-fx-replicate] consumer poll timeout has expired. This means the time between subsequent calls to poll() was longer than the configured [max.poll.interval.ms](http://max.poll.interval.ms), which typically implies that the poll loop is spending too much time processing messages. You can address this either by increasing [max.poll.interval.ms](http://max.poll.interval.ms) or by reducing the maximum size of batches returned in poll() with max.poll.records."}
```

This is direct evidence for [[kafka-consumer-poll-timeout]] in the specified Trade service consumer group. It does not provide the configured values, lag magnitude, rebalance history, processing duration, or a root-cause measurement.

## Reported Contributors

The source identifies the following possible contributors:

1. High data volume sent from [[tds3]] to Kafka.
2. Lower EKS resource performance than UAT, described as a developer view.
3. Higher processing complexity in the new `fx-replication` process.

No throughput, resource-utilization, consumer-lag, message-size, partition, or processing-profile measurements are supplied to validate these contributors.

## Proposal and Configuration

The proposal was to restrict EKS business testing to small data volumes and customize Kafka settings by environment so messages could continue to be consumed.

The source preserves the following configuration form; actual values are unavailable:

```yaml
kafka:
       properties:
             max.poll.interval.ms: xxxxx
             session.timeout.ms: xxxxx
```

The document does not state whether `max.poll.records`, consumer concurrency, topic partitioning, back-pressure, or autoscaling were evaluated.

## Short-Term Actions

| Service name | optimize point | owner | process | note |
| --- | --- | --- | --- | --- |
| Trade service | Trade service modify the application.yml to add properties and then do one testing kafka: properties: [ max.poll.interval.ms](http://max.poll.interval.ms): xxxxx [ session.timeout.ms](http://session.timeout.ms): xxxxx | ben /hawk | already change setting and deployed to EKS | testing so far so good |
|  | Consider to optimizing the performance of the trade fx-replication part How to optimize: use rule service to parse the scbml to Json, since rule service upgrade to new library from TDS3 which use to parse the scbml. | ben /hawk | already deploy to EKS and Staging. |  |

The two changes are distinct:

- Configuration change: addition of `max.poll.interval.ms` and `session.timeout.ms` properties in Trade service `application.yml`, deployed to EKS.
- Processing optimization: use of [[rule-service]] to parse [[scbml]] to JSON through a newer TDS3-derived library, deployed to EKS and Staging.

The source does not isolate the effect of either change.

## Long-Term Action

| Service name | properties | owner | process | note |
| --- | --- | --- | --- | --- |
| Application service which need to recover the properties value | kafka: properties: [ max.poll.interval.ms](http://max.poll.interval.ms): xxxxx [ session.timeout.ms](http://session.timeout.ms): xxxxx | deliver lead/Owner | | |

This is a proposed standardization direction, not a documented approved configuration standard. Values, eligibility criteria, ownership, and deviation policy are unspecified.

## Reported Closure

The source concludes that the Drop3 migration-test rerun from “5/9” showed no lag or delay in Trade service after optimization and that the topic should be closed.

This is a qualitative post-change observation. There are no stated success thresholds, before-and-after lag measurements, equivalent-load evidence, or sustained monitoring period. See [[what-kafka-consumer-settings-and-processing-slo-apply-to-trade-service-fx-replicate]] for unresolved operational evidence.