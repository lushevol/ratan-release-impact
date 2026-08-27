---
type: concept
title: Indonesia Environment Readiness Dependencies
created: 2026-08-24
updated: 2026-08-24
tags: [indonesia, environment-readiness, infrastructure, deployment, cicd]
related: [ratan-indonesia-onshoring-2026, production-server-handover-definition-of-done, ratanone-api-gateway, microsoft-entra-id]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Development Integration Plan.md"]
---
# Indonesia Environment Readiness Dependencies

Indonesia RATAN readiness is tracked as a dependency chain rather than as a confirmed operational state.

## Explicit dependencies

- VIP precedes DNS and firewall provisioning.
- PostgreSQL account setup precedes the stated HashiCorp integration, which is described as applying only to database accounts.
- Foundation setup precedes service-property setup and service deployment.
- Nginx administration depends on an ADO pipeline.
- NAS is deferred until after OAT and remains conditional on FileIT, possible GDC Kafka data synchronization, and a pending DR solution.
- SSL certificates, keystores, and truststores remain planned work; application-server SSL is stated as not started.
- Entra integration through FMAA is marked “not now,” with an unresolved question about trusting the Indonesia hostname.

Foundation components listed in the plan are PostgreSQL, Redis, Kafka, ELK, Nginx, Prometheus, Grafana, generic service accounts, and ADO CI/CD enablement.

## Status limitation

Blank production and deployment-status fields must not be interpreted as completion. In non-production, the plan records API-gateway regional validation and gateway/auth-server combination work as `IN PROGRESS` in Dev, while most named integration, frontend, and QA activities are `NOT START` and QA ownership is `TBC`.

This is implementation-tracker evidence, not acceptance evidence under [[production-server-handover-definition-of-done]].