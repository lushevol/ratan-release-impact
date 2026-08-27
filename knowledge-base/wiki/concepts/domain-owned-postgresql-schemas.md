---
type: concept
title: Domain-Owned PostgreSQL Schemas
tags: [postgresql, schema, service-ownership, data-architecture, cash-settlement]
related: [postgresql, cash-settlement-platform, camunda, cashflow-lifecycle-service, cash-settlement-data-store-requirements]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Data Store Requirements.md"]
---
# Domain-Owned PostgreSQL Schemas

Domain-owned PostgreSQL schemas are the proposed storage-boundary model for the Cash Settlement Platform: different business-domain services use distinct schemas.

The source assigns ownership as follows:

- Cashflow data: [[cashflow-lifecycle-service]]
- Camunda workflow data: Settlement Orchestration
- Suppression rules: Suppression Service
- Processed raw messages from [[stella]]: Payment Lake Service
- Audit and login/logout audit: [[audit-trail]] / Audit Service
- Processing exceptions: Exception Service
- Customized blotter filters and views: BFF
- SWIFT-message display data: SWIFT processing Service

A schema-per-domain model can provide naming, migration, permission, and ownership boundaries. It is not by itself proof of isolation: the source does not specify whether all schemas share a PostgreSQL cluster, whether cross-schema foreign keys are allowed, how cross-service transactions work, or which roles may read sensitive SSI and audit data.