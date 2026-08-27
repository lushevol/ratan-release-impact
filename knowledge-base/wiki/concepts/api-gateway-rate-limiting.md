---
type: concept
title: API Gateway Rate Limiting
created: 2026-08-24
updated: 2026-08-24
tags: [api-gateway, rate-limiting, throttling, redis]
related: [api-gateway, dynamic-openapi-routing, rate-limit-key-resolution, gateway-closed-loop-observability]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md"]
---
# API Gateway Rate Limiting

API Gateway rate limiting restricts request volume according to route-specific quotas. The current implementation can assemble `RequestRateLimiter` filters for dynamic routes, but the source considers the capability only partially production-configured.

The recommended configuration includes:

```text
replenishRate
burstCapacity
requestedTokens
keyType: PATH | USER | TOKEN | IP
```

Dynamic route assembly should explicitly bind:

```yaml
key-resolver: "#{@apiGatewayRatelimiterKeyResolver}"
deny-empty-key: false
```

High-concurrency tests should validate quota enforcement, 429 responses, and recovery behavior.