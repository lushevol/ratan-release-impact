---
type: concept
title: Centralized Static Configuration Management
created: 2026-08-24
updated: 2026-08-24
tags: [configuration-management, config-server, database, ownership]
related: [self-service-entity-branch-onboarding, kafka-based-configuration-propagation, entity-onboarding-configuration-architecture-options, config-server]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# Centralized Static Configuration Management

Centralized static configuration management is the architectural choice to replace fragmented front-end hard-coded values and backend `application.yml` settings with administratively managed configuration.

The source considers three storage and ownership patterns:

- Service-local database tables, managed through multiple Blotters.
- Config Server for selected runtime settings plus service-local tables for other settings.
- A central aggregate record in [[ratan-static-data-service]], replicated to consumers through Kafka.

No pattern is selected. The database design itself marks selected fields and tables for removal when Config Server is used, while Options 2 and 3 require those settings to move into database storage. An approved design must identify the source of truth for each domain and define cache refresh, versioning, validation, audit, and rollback behavior.