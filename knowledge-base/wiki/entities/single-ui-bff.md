---
type: entity
title: single-ui-bff
created: 2026-08-24
updated: 2026-08-23
tags: [ratan, bff, login, jwt, session-management, service, frontend, analytics, shared-service, cash-settlement]
related: [ratan, ratanone-api-gateway, ratanone-auth-server, oud, shared-user-action-analytics-api, frontend-error-logging-and-user-action-analytics, dev-only-analytics-api-retirement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Audit API migration plan from GDC to ID.md"]
---
# single-ui-bff

`single-ui-bff` is a Spring Boot MVC backend-for-frontend in the documented Ratan architecture. The deprecated API Gateway & Auth Server Combination source assigns it login, JWT issuance, and session management.

It accepts both OUD username/password and OIDC authorization-code login inputs through `/v2/sso/login`. Whether this controller is directly hosted by the BFF or reached through the gateway is unresolved.

## User-action analytics

The Audit API migration plan states that `single-ui-bff` hosts the existing `/v1/fmo/print` API used for user-action analytics.

Recorded user actions include:

- Session control.
- Cashflow-blotter opening.

Events are stored in the `single-ui-bff-analytic` Elasticsearch index.

## Indonesia reuse model

According to the Audit API migration plan, both GDC and Indonesia should use the same existing `/v1/fmo/print` API, and no Indonesia backend implementation is required.

The migration plan does not establish:

- Connectivity for Indonesia consumers.
- Data-residency compliance.
- Support ownership.
- Capacity.
- The API contract for Indonesia consumers.