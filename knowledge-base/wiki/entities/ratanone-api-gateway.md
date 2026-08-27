---
type: entity
title: ratanone-api-gateway
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, api-gateway, spring-cloud-gateway, webflux]
related: [ratan, ratanone-auth-server, single-ui-bff, ratan-api-gateway-auth-server-consolidation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# ratanone-api-gateway

`ratanone-api-gateway` is the documented Ratan edge service, implemented with Spring Cloud Gateway, WebFlux, and Java 17. Its stated responsibilities are routing, authentication enforcement, and audit.

The deprecated proposal says the gateway calls [[ratanone-auth-server]] for each request and proposes merging the services. NGINX evidence routes `/api/auth/` to `ratan_backend_api_gateway`, creating an unresolved ownership question for the documented login endpoint.