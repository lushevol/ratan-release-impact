---
type: concept
title: Kafka-Based Configuration Propagation
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, configuration, synchronization, eventual-consistency]
related: [ratan-static-data-service, ratan-static-entity-onboarding-config, ratan-static-entity-onboarding-config-sync-result, centralized-static-configuration-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# Kafka-Based Configuration Propagation

Kafka-based configuration propagation is the Option 3 proposal for [[ratan-static-data-service]] to distribute aggregate entity onboarding configuration to downstream services, which then persist the subsets they require.

The proposal introduces asynchronous distributed state. It records aggregate `sync_status` and `sync_success_count`, plus service-level results in [[ratan-static-entity-onboarding-config-sync-result]].

The source does not define the Kafka topic, event schema or version, partition key, consumer idempotency key, retry policy, DLT behavior, replay procedure, ordering guarantee, timeout, rollback, or reconciliation process. These controls are required before the design can establish reliable configuration synchronization.