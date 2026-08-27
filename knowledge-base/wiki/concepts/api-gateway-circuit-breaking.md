---
type: concept
title: API Gateway Circuit Breaking
created: 2026-08-24
updated: 2026-08-24
tags: [api-gateway, circuit-breaker, resilience4j, availability]
related: [api-gateway, resilience4j, api-gateway-fallback-handling, gateway-closed-loop-observability]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md"]
---
# API Gateway Circuit Breaking

API Gateway circuit breaking prevents repeated calls to failing or slow downstream services. The current implementation has a global `CircuitBreaker` filter and [[entities/resilience4j]], but the source classifies it as baseline-only.

Production readiness requires route-level or backend-specific policies covering failure rates, slow calls, sliding windows, open-state duration, and half-open trials. Circuit breaking should be paired with [[concepts/api-gateway-fallback-handling]].