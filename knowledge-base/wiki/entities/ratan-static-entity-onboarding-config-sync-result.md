---
type: entity
title: ratan_static__entity_onboarding_config_sync_result
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, synchronization, kafka, onboarding]
related: [ratan-static-entity-onboarding-config, ratan-static-data-service, kafka-based-configuration-propagation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# ratan_static__entity_onboarding_config_sync_result

`ratan_static__entity_onboarding_config_sync_result` is a proposed Option 3 table for recording propagation outcomes by downstream service.

The draft fields are `config_id`, `service_name`, `exec_status`, `reason`, and timestamps. `exec_status` is documented as `1` for success and `0` for failure.

This proposed outcome record is insufficient by itself to define operational recovery. The source does not specify retries, replay, dead-letter handling, idempotency, ordering, timeouts, or reconciliation of a failed consumer with the aggregate configuration record.