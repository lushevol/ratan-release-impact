---
type: query
title: What Is the Kafka Contract and Recovery Process for Onboarding Config Sync?
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, recovery, synchronization, onboarding]
related: [kafka-based-configuration-propagation, ratan-static-entity-onboarding-config, ratan-static-entity-onboarding-config-sync-result]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# What Is the Kafka Contract and Recovery Process for Onboarding Config Sync?

What Kafka topic, event schema and version, partitioning strategy, idempotency key, retry and DLT policy, replay procedure, reconciliation method, timeout, and rollback behavior govern Option 3 configuration propagation?

The draft provides only processing/success/failure status fields and per-service outcome records. It does not define the delivery and recovery contract required for reliable asynchronous configuration replication.