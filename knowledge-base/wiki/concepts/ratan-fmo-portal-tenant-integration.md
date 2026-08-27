---
type: concept
title: RATAN FMO Portal Tenant Integration
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, fmo-portal, tenant-integration, entitlement, request-forwarding]
related: [fmo-portal, ratan-sdk, ratan-nginx, ems2, ratan-data-entitlement, ratan-interface-architecture, what-is-the-authoritative-fmo-portal-tenant-integration-contract, what-do-ratan-fmo-portal-integration-statuses-mean]
sources: ["RATAN/RATAN -Interfaces/Ratan(FMO Portal) and STAMP FSS LOANIQ SSI+ SSDR CES.md"]
---

# RATAN FMO Portal Tenant Integration

## Definition

RATAN FMO Portal tenant integration is the documented pattern in which RATAN supports tenant applications through entitlement-list retrieval and request forwarding. The source presents this as a shared integration capability for tenants entering the FMO Portal environment.

## Documented flow

The source describes two distinct paths:

```text
Entitlement list: Tenant -- (RATAN SDK)--> EMS2
Request forwarding: Tenant Front End page --> RATAN Nginx --> Tenant Back End server
```

The first path assigns EMS2 the role of receiving entitlement-list requests through the RATAN SDK. The second path assigns RATAN Nginx the intermediary routing role between a tenant front end and tenant back end.

These paths should not be merged into a single fully specified authorization or gateway contract. The source does not state whether entitlement retrieval returns functional entitlements, data entitlements, or both.

## Tenant readiness

The source lists seven tenants with the statuses `Technical Online`, `Online`, and `Pending`. These values are retained as source terminology rather than normalized into a formal readiness model. Their criteria, scope, and production meaning are unknown.

## Boundaries

This concept does not establish:

- API endpoints or SDK method signatures
- Authentication or authorization mechanisms
- Tenant back-end routing rules
- Availability, caching, timeout, or retry behavior
- Monitoring and alerting requirements
- Support ownership or escalation procedures
- Acceptance criteria for tenant readiness

The concept therefore describes a high-level integration pattern, not an authoritative interface specification.