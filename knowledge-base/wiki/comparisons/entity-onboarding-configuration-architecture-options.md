---
type: comparison
title: Entity Onboarding Configuration Architecture Options
created: 2026-08-24
updated: 2026-08-24
tags: [architecture, onboarding, configuration-management, decision]
related: [self-service-entity-branch-onboarding, centralized-static-configuration-management, kafka-based-configuration-propagation, config-server, ratan-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# Entity Onboarding Configuration Architecture Options

The source presents four unselected approaches for self-service entity and branch onboarding.

| Criterion | Option 1 | Option 2 | Option 3 | Option 4 |
|---|---|---|---|---|
| UI experience | Multiple service-oriented Blotters | Multiple service-oriented Blotters | One aggregate Blotter | One Excel upload/download Blotter |
| Configuration storage | Service DB tables and Config Server | Service DB tables | Static-data aggregate table and downstream DB tables | Multiple DB schemas |
| Runtime distribution | Services read DB and Config Server | Services read DB | Kafka propagation to downstream services | Parsed upload inserts into schemas |
| Deployment independence | Intended | Intended | Intended | Intended, subject to Config Server for unmigrated settings |
| Operational complexity | Mixed storage and runtime dependencies | Service-local ownership | Highest: asynchronous replication and partial-failure handling | Bulk parsing, validation, and multi-schema write complexity |
| Source-of-truth risk | Split between DB and Config Server | Distributed across service databases | Ambiguous between aggregate record and downstream copies | Distributed across schemas |
| Audit approach | Per-Blotter audit proposed | Per-Blotter audit proposed | Aggregate audit proposed | Not specified beyond upload/download results |
| Batch onboarding suitability | Not decided | Not decided | Not decided | Intrinsic upload model, but validation and partial-success behavior unspecified |

No option is approved in the source. The critical decision is whether configuration ownership should remain service-local, be split with [[config-server]], or be centrally governed and replicated by [[ratan-static-data-service]].