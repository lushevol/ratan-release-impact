---
type: entity
title: Kong
created: 2026-08-24
updated: 2026-08-24
tags: [kong, api-gateway, architecture-evolution]
related: [api-gateway, spring-cloud-gateway, apisix]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md"]
---
# Kong

Kong is identified as an alternative northbound gateway for a possible dual-layer architecture. It could provide broader plugin and traffic-governance capabilities while the existing [[entities/spring-cloud-gateway]] remains responsible for southbound business orchestration.

The source does not recommend immediate migration to Kong.