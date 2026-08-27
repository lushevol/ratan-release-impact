---
type: entity
title: audit-trail
created: 2026-08-24
updated: 2026-08-24
tags: [service, audit, analytics, logging, indonesia]
related: [51358-ratan-cash-settlement-query-service, 51358-ratanone-query-service, frontend-error-logging-and-user-action-analytics, dev-only-analytics-api-retirement, which-service-owns-id-eslogging]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Audit API migration plan from GDC to ID.md"]
---
# audit-trail

`audit-trail` is identified as the GDC location of the development-only `/v1/ratan-analytic` user-action endpoint and as a proposed Indonesia implementation location for retained frontend API-error logging.

## Recorded Roles

- Hosts `/v1/ratan-analytic` in GDC, writing user-action analytics to `ratan-analytic-data`.
- Is proposed by Lu and Shuai as the Indonesia home for `/v1/esLogging` frontend error logs.
- Is not confirmed as the final owner of `/v1/esLogging`; the alternative is [[51358-ratan-cash-settlement-query-service]].
- Should not receive a new Indonesia implementation of `/v1/ratan-analytic`, which the plan says will be discarded.

See [[which-service-owns-id-eslogging]] for the unresolved ownership decision.