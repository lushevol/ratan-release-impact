---
type: concept
title: Shared User-Action Analytics API
created: 2026-08-24
updated: 2026-08-24
tags: [analytics, shared-service, frontend, indonesia, gdc]
related: [single-ui-bff, frontend-error-logging-and-user-action-analytics, dev-only-analytics-api-retirement, cash-settlement-audit-api-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Audit API migration plan from GDC to ID.md"]
---
# Shared User-Action Analytics API

The shared user-action analytics approach reuses [[single-ui-bff]] `/v1/fmo/print` for both GDC and Indonesia rather than implementing a new Indonesia backend service.

The source associates the API with session-control and cashflow-blotter-open events and the `single-ui-bff-analytic` Elasticsearch index.

This is an intended reuse decision. The source does not confirm network availability, security approval, operational support, capacity, or Indonesia data-residency suitability.