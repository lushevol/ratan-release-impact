---
type: entity
title: Resilience4j
created: 2026-08-24
updated: 2026-08-24
tags: [resilience4j, circuit-breaker, api-gateway]
related: [api-gateway, api-gateway-circuit-breaking, api-gateway-fallback-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md"]
---
# Resilience4j

Resilience4j is the resilience library already included in the API Gateway dependency set. A global default `CircuitBreaker` filter is configured, but the source considers the current implementation baseline-only.

The recommended design uses independently named circuit breakers per backend service and explicitly configures failure-rate, slow-call, sliding-window, open-state, and half-open parameters.