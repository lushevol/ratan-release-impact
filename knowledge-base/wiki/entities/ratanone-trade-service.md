---
type: entity
title: ratanone-trade-service
created: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka consumer issue for large lag during drop3 migration testing.md"]
tags: ["ratan", "trade-validation", "rule-engine", "counterparty-data", "service", "trade-processing", "kafka", "fx-replication"]
related: ["ratan", "ratanone-data-ambassador", "ratanone-rule-service", "eue-notice-trade-validation-rule-dependency", "kafka-consumer-poll-timeout", "environment-specific-kafka-consumer-configuration", "tds3", "rule-service", "scbml", "what-kafka-consumer-settings-and-processing-slo-apply-to-trade-service-fx-replicate"]
updated: 2026-08-23
---

# ratanone-trade-service

`ratanone-trade-service` invokes `ruleService.validate` with the `TRADE_VALIDATION` business flow.

During Drop3 migration testing, `ratanone-trade-service` was also described as an application service consuming FX-replication Kafka messages through the `ratanone-trade-service-fx-replicate` consumer group.

## Trade Validation and Counterparty Data

The validation payload investigated in the functional-requirement source contains counterparty facts under `Custom__CounterParty`, including `Legal_Entity_Main_Profile.LMP_Dodd_Stat.Lds_Eue_Notice`.

According to that source, removal of SCI `eueNotice` may affect this service's validation outcome through configured rules in [[ratanone-rule-service]]. The source demonstrates the dependency but does not define missing-field evaluation semantics or the intended replacement for the EUE notice condition.

## FX-Replication Kafka Consumer Incident

On 19 March 2024, the `ratanone-trade-service-fx-replicate` consumer group emitted a warning that the time between `poll()` calls exceeded `max.poll.interval.ms`.

The incident was reported in EKS. UAT was stated to work well, although the technical-design source does not demonstrate that the environments had equivalent workload or capacity.

The confirmed symptom is a [[kafka-consumer-poll-timeout]], rather than a measured determination of the underlying throughput or capacity cause.

## FX-Replication Processing Dependencies

The technical-design source associates the consumer path with:

- [[tds3]] as a possible high-volume upstream source and as the origin of an earlier SCBML parsing library.
- [[scbml]] as the payload format whose parsing was considered an optimization target.
- [[rule-service]] as the service used to parse SCBML to JSON through a newer TDS3-derived library.

The SCBML parsing optimization was reported as deployed to EKS and Staging. Its independent performance effect was not measured in the source.

## FX-Replication Configuration and Follow-up

The service was reported to have added environment-specific `max.poll.interval.ms` and `session.timeout.ms` properties to `application.yml` and deployed them to EKS. The actual values are not recorded.

A later migration-test rerun was reported to show no lag or delay. However, supporting lag metrics, workload equivalence, and acceptance thresholds are absent.

Open configuration and service-level objectives are tracked in [[what-kafka-consumer-settings-and-processing-slo-apply-to-trade-service-fx-replicate]].