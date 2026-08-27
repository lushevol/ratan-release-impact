---
type: concept
title: Environment-Specific Kafka Consumer Configuration
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, configuration, environments, eks, consumer-resilience]
related: [kafka-consumer-poll-timeout, ratanone-trade-service, what-kafka-consumer-settings-and-processing-slo-apply-to-trade-service-fx-replicate]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka consumer issue for large lag during drop3 migration testing.md"]
---
# Environment-Specific Kafka Consumer Configuration

Environment-specific Kafka consumer configuration tailors client settings to the capacity, workload, and processing characteristics of a deployment environment.

## Reported Application

Following a poll-timeout warning in [[ratanone-trade-service]] running in EKS, the source proposed Kafka settings differentiated by environment. The documented configuration shape was:

```yaml
kafka:
       properties:
             max.poll.interval.ms: xxxxx
             session.timeout.ms: xxxxx
```

The source reports that these properties were added to Trade service `application.yml` and deployed to EKS.

## Scope and Limits

The source proposes a longer-term action for application services that need to recover property values. It does not define:

- Actual values for either property.
- The application services to which the standard applies.
- Workload, processing-time, or lag thresholds used to select values.
- Approval ownership or a deviation process.
- Compatibility checks with broker, client-library, and group-rebalance behavior.

Configuration should therefore be treated as a reported local remediation direction rather than an approved cross-service standard.

## Related Performance Work

For the Trade service incident, configuration was deployed alongside an FX-replication parsing optimization using [[rule-service]] and [[scbml]]. The source does not provide a controlled comparison that separates configuration effects from parser-performance effects.