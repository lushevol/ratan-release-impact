---
type: entity
title: APISIX
created: 2026-08-24
updated: 2026-08-24
tags: [apisix, api-gateway, architecture-evolution]
related: [api-gateway, spring-cloud-gateway, kong]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md"]
---
# APISIX

APISIX is identified as a possible future northbound gateway in a dual-layer architecture. In that model, APISIX would handle broader traffic governance while the existing [[entities/spring-cloud-gateway]] implementation would continue southbound business orchestration.

The source presents this as a medium- to long-term option, not an immediate replacement recommendation.