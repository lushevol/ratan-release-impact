---
type: concept
title: Ratan API Gateway and Auth Server Consolidation
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, api-gateway, authorization, service-consolidation, deprecated]
related: [ratanone-api-gateway, ratanone-auth-server, single-ui-bff, ratan-indonesia-isolated-deployment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# Ratan API Gateway and Auth Server Consolidation

The deprecated proposal recommends combining [[ratanone-api-gateway]] and [[ratanone-auth-server]] into one service because the gateway reportedly invokes the auth server for every incoming request.

The intended benefits are less integration overhead and a simpler Indonesia deployment. No evidence evaluates latency, independent scaling, fault isolation, audit controls, availability, migration sequencing, or the enlarged security blast radius. This is not an approved architectural decision.