---
type: entity
title: ratan-static-data-service
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, service, static-data, onboarding]
related: [ratan-static-entity-onboarding-config, ratan-static-entity-onboarding-config-sync-result, self-service-entity-branch-onboarding, kafka-based-configuration-propagation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# ratan-static-data-service

`ratan-static-data-service` is proposed as the central owner of front-end static configuration and, in Option 3, the aggregate owner of entity onboarding configuration.

The draft assigns it responsibility for storing aggregate onboarding records, exposing a single administrative Blotter API, and distributing configuration subsets to downstream services through Kafka. It is also identified as a consumer of a proposed migration from `sd.branch-code.mappings` into `ratan_static__entity_conf`.

The source does not establish that this ownership model is approved or implemented. In particular, it does not define whether this service remains authoritative after consumer services persist propagated configuration.

See [[centralized-static-configuration-management]] and [[entity-onboarding-configuration-architecture-options]].