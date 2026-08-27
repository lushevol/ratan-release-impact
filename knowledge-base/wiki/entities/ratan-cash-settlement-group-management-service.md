---
type: entity
title: ratan-cash-settlement-group-management-service
created: 2026-08-22
updated: 2026-08-23
tags: [software-service, cash-settlement, group-management, inter-entity-netting, ratan, amendments, economic-change, nostro, kafka, application-service]
related: [inter-entity-netting, ratan-cash-settlement-netting-service, ratanone-foundation, ratan-rule-service, nostro-selection-economic-change-detection, cashflow-versioning, amendment-driven-cashflow-correlation, rfi-nostro-stamping-based-on-portfolio, dedicated-nostro-selection, what-is-the-required-outcome-when-rfi-changes-in-a-non-economic-amendment, ratan, kafka, 51358-ratanone-static-data-service, cash-settlement-batch-job-performance, cash-settlement-static-data-batch-optimization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter Entity Netting Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PT Batch Group Stg.md"]
---
# ratan-cash-settlement-group-management-service

## Role in the design

The Inter Entity Netting Design lists `ratan-cash-settlement-group-management-service` as a participating service for the inter-entity netting feature. It places the service within implementation scope but does not define its specific responsibilities or confirm that it performs matching.

That design associates the service with the following feature branch:

```text
feature/autonetting-interEntity
```

The Inter Entity Netting Design provides no release version and does not establish deployment or production enablement.

## Role in performance testing

The PT Batch Group Stg technical design identifies `ratan-cash-settlement-group-management-service` as the central application service measured in the performance test. In that test context, it consumes Uber messages from Kafka topics and performs Cash Settlement group-management processing with dependent lifecycle, orchestration, and static-data services.

The performance-test role does not replace or expand the narrower responsibilities defined by the Inter Entity Netting Design. In particular, the Inter Entity Netting Design does not confirm that this service performs matching.

## Cashflow grouping and selected nostro changes

The Cashflow Dedicated Nostro Stamping Design states that the service groups new and withdrawal cashflows. It must treat a changed selected `nostroId` as an economic change, including:

- Non-RFI to RFI changes
- RFI to non-RFI changes
- Changes between RFI configurations

The required amendment behavior for these changes is documented in [[nostro-selection-economic-change-detection]].

## RFI change assessment

The Change List and API source states that the service must assess whether RFI changed between the previous and current states when an amendment meets the unspecified non-economic condition.

That source associates the `findDedicateds` lookup with `group-serivce` to help identify a changed `nostroId`. It does not define:

- The qualifying amendment rule
- The business action to take after detecting a difference

This implementation gap is tracked in [[what-is-the-required-outcome-when-rfi-changes-in-a-non-economic-amendment]].

The non-economic amendment assessment described by the Change List and API source is kept separate from the economic-change behavior described by the Cashflow Dedicated Nostro Stamping Design. The latter explicitly identifies selected-`nostroId` changes as economic changes, while the former does not specify the qualifying rule or subsequent business action for its non-economic condition.

## Performance-test configuration

The staging setup used:

- Four service instances
- Twelve partitions
- Concurrency of three
- A database pool configured with a minimum of two and a maximum of 32 connections

The test design split one input topic into seven topics.

## Performance observations

Across the reported 7,000-message tests:

- Group CPU utilization ranged from 94.6% to 100%.
- The initial worst-case run recorded a maximum of 25 database connections.
- The post-JVM and thread-pool-tuning worst-case run recorded 13,549 consumptions, including retries.
- The final reported run combined database-connection changes, thread-pool tuning, and a batch interface. It completed in 784 seconds with an average cashflow count of 357 and group CPU at 100%.

The optimization comparison reported:

| Configuration or scenario | Reported throughput |
|---|---:|
| Production-behavior seven-topic case | 44.8 TPS |
| After increasing static-data database connections | 70 TPS |
| After the combined batch-optimization change set | 420 TPS |

## Interpretation and measurement caveats

The performance results indicate that the service was close to CPU saturation and that its downstream static-data calls contributed materially to processing time. The results do not isolate the individual effects of:

- Topic count
- Database capacity
- JVM settings
- Thread-pool settings
- Batch interfaces
- Validation-factory reuse

Retry-inflated consumption counts must not be interpreted as successfully completed business messages. Further validation should measure completion, retries, duplicates, consumer lag, and Kafka rebalances separately.

## Related services and concepts

The Inter Entity Netting Design lists this service alongside [[ratanone-foundation]], [[ratan-cash-settlement-netting-service]], and [[ratan-rule-service]]. Its matching design is summarized in [[direction-dependent-prematch-key]].

Related amendment, cashflow, and static-data concepts include:

- [[nostro-selection-economic-change-detection]]
- [[cashflow-versioning]]
- [[amendment-driven-cashflow-correlation]]
- [[rfi-nostro-stamping-based-on-portfolio]]
- [[dedicated-nostro-selection]]
- [[what-is-the-required-outcome-when-rfi-changes-in-a-non-economic-amendment]]
- [[ratan]]
- [[kafka]]
- [[51358-ratanone-static-data-service]]
- [[cash-settlement-batch-job-performance]]
- [[cash-settlement-static-data-batch-optimization]]