---
type: entity
title: ratan_static__entity_onboarding_config
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, onboarding, jsonb, static-data]
related: [ratan-static-data-service, ratan-static-entity-onboarding-config-sync-result, kafka-based-configuration-propagation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# ratan_static__entity_onboarding_config

`ratan_static__entity_onboarding_config` is a proposed Option 3 aggregate table for whole-entity static configuration.

Its proposed fields include `fmId`, `booking_entity`, country fields, a GIN-indexed `content` JSONB payload, synchronization status/count fields, maker-checker fields, and timestamps. The table would support a single aggregate onboarding Blotter managed by [[ratan-static-data-service]].

The source does not specify uniqueness constraints, JSON schema/versioning, whether `content` is authoritative after propagation, or the relationship between approval and downstream synchronization.