---
type: entity
title: OpenApi
created: 2026-08-24
updated: 2026-08-24
tags: [openapi, api-gateway, route-configuration, configuration-model]
related: [api-gateway, dynamic-openapi-routing, api-gateway-rate-limiting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md"]
---
# OpenApi

`OpenApi` is the internal route-configuration model used by the API Gateway to generate dynamic routes. It is distinct from a general description of the OpenAPI specification in this source context.

The model is supplied from local configuration under `ratanone.api-gateway.open-apis` or from [[entities/redis]]. Management operations include querying, publishing, and deleting definitions.

The recommended model extension adds route-level resilience and rate-limiting configuration.