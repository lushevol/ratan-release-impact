---
type: entity
title: ratanone-auth-server
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, authorization, token-validation, redis]
related: [ratan, ratanone-api-gateway, single-ui-bff, ratan-api-gateway-auth-server-consolidation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# ratanone-auth-server

`ratanone-auth-server` is documented as a Spring Boot MVC service responsible for token validation and a Redis session store.

The source distinguishes this authorization role from [[single-ui-bff]], which it says owns login, JWT issuance, and session management. The boundary is not fully established by the supplied routing evidence and requires verification.