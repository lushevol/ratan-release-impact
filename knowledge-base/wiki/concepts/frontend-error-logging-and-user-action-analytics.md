---
type: concept
title: Frontend Error Logging and User-Action Analytics
created: 2026-08-24
updated: 2026-08-24
tags: [frontend, error-logging, user-action, analytics, elasticsearch, observability]
related: [cash-settlement-audit-api-migration, shared-user-action-analytics-api, dev-only-analytics-api-retirement, audit-trail, single-ui-bff, which-service-owns-id-eslogging]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Audit API migration plan from GDC to ID.md"]
---
# Frontend Error Logging and User-Action Analytics

Frontend error logging and user-action analytics are distinct observability functions in the Indonesia migration plan.

## Error Logging

`/v1/esLogging` records UI API errors to the `ratanrt-logs-app-*` index. The plan indicates that the API should be retained, but its Indonesia service ownership is unresolved.

## User-Action Analytics

`/v1/fmo/print` records session-control and cashflow-blotter-open actions in `single-ui-bff-analytic`. It is intended for shared GDC and Indonesia use.

The separate development-only `/v1/ratan-analytic` endpoint writes to `ratan-analytic-data` and is intended for retirement. Retiring that endpoint does not remove user-action analytics because `/v1/fmo/print` remains the non-development mechanism.

## Missing Controls

The source does not define a common event schema, correlation identifier, retention policy, access model, or dashboard strategy across these indices.