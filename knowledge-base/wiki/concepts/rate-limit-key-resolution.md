---
type: concept
title: Rate-Limit Key Resolution
created: 2026-08-24
updated: 2026-08-24
tags: [api-gateway, rate-limiting, authorization, identity]
related: [api-gateway-rate-limiting, api-gateway, openapi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md"]
---
# Rate-Limit Key Resolution

Rate-limit key resolution selects the identity or request dimension whose quota is enforced. Possible dimensions in the proposed gateway design are user, token, IP address, and request path.

The current path-only expression is:

```java
exchange.getRequest().getURI().getPath()
```

Path-only keying can unintentionally share one quota across all users of an endpoint. The proposed priority is user identity or token, then client IP, and finally request path. The actual binding of `apiGatewayRatelimiterKeyResolver` must be verified at runtime.