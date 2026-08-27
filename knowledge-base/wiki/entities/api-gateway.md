---
type: entity
title: API gateway
created: 2026-08-24
updated: 2026-08-24
tags: ["api-gateway", "cash-settlement", "indonesia", "platform-architecture", "API gateway", "authorization", "function-entitlement", "RATANONE"]
related: ["spring-cloud-gateway", "dynamic-openapi-routing", "api-gateway-circuit-breaking", "api-gateway-fallback-handling", "api-gateway-rate-limiting", "auth-service", "function-entitlement", "data-entitlement", "single-ui-authorization"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Authentication flow.md"]
---
# API gateway

The API gateway is the request-entry component responsible for checking function entitlement before an API request proceeds.

## Authorization flow

For each request, the gateway sends the `Single-UI-Authorization` bearer token to [[auth-service]]. The returned authorization context includes function roles, permitted actions, data-entitlement roles, and user information.

The source explicitly assigns function-entitlement checking to the gateway. It does not establish whether the gateway itself enforces data filtering or merely forwards data-entitlement context to downstream services.