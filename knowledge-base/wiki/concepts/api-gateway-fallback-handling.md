---
type: concept
title: API Gateway Fallback Handling
created: 2026-08-24
updated: 2026-08-24
tags: [api-gateway, fallback, resilience, error-handling]
related: [api-gateway, api-gateway-circuit-breaking, gateway-closed-loop-observability]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md"]
---
# API Gateway Fallback Handling

Fallback handling defines the response or alternate path used when a downstream service fails or a circuit breaker opens.

The source identifies fallback handling as the most critical missing capability in the gateway. The proposed design adds a route-level `fallbackUri`, an internal endpoint at `forward:/internal/fallback/{routeId}`, and a `FallbackController`.

The standardized response should contain an error code, error message, `routeId`, `traceId`, and timestamp. The approved HTTP status and whether read and write APIs require different fallback behavior remain open design questions.