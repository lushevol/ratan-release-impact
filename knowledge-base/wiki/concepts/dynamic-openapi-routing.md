---
type: concept
title: Dynamic OpenApi Routing
created: 2026-08-24
updated: 2026-08-24
tags: [api-gateway, dynamic-routing, openapi, redis]
related: [api-gateway, spring-cloud-gateway, openapi, redis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md"]
---
# Dynamic OpenApi Routing

Dynamic OpenApi routing generates gateway routes at runtime from `OpenApi` definitions rather than requiring every route to be statically declared.

The implementation supports local configuration, Redis-backed definitions, management operations, and Redis Pub/Sub refresh across Kubernetes deployments. This capability is a core reason to evolve the current gateway rather than replace it immediately.