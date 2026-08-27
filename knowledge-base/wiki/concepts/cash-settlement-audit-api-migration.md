---
type: concept
title: Cash Settlement Audit API Migration
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, api-migration, indonesia, gdc, audit, observability]
related: [51358-ratanone-query-service, 51358-ratan-cash-settlement-query-service, audit-trail, single-ui-bff, frontend-error-logging-and-user-action-analytics, shared-user-action-analytics-api, dev-only-analytics-api-retirement, which-service-owns-id-eslogging]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Audit API migration plan from GDC to ID.md"]
---
# Cash Settlement Audit API Migration

Cash Settlement Audit API Migration is the planned disposition of frontend-facing search, error-logging, and user-action analytics APIs when moving from GDC to Indonesia.

## Intended Target State

- Implement Custom Search/View APIs in [[51358-ratan-cash-settlement-query-service]].
- Continue user-action logging through the shared [[single-ui-bff]] `/v1/fmo/print` API rather than creating an Indonesia backend.
- Discard the development-only `/v1/ratan-analytic` endpoint.
- Retain `/v1/esLogging`, with its final Indonesia host still undecided between [[audit-trail]] and the Indonesia query service.

## Boundaries

This migration evidence concerns frontend audit and observability APIs. It does not establish changes to Murex–RATAN cashflow processing, FMRP lifecycle processing, payment STP, or trade-validation controls.