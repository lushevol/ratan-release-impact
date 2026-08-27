---
type: entity
title: 51358-ratanone-query-service
created: 2026-08-24
updated: 2026-08-24
tags: [service, gdc, cash-settlement, query-service, logging]
related: [51358-ratan-cash-settlement-query-service, audit-trail, cash-settlement-audit-api-migration, which-service-owns-id-eslogging]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Audit API migration plan from GDC to ID.md"]
---
# 51358-ratanone-query-service

`51358-ratanone-query-service` is identified as the GDC location for the Custom Search/View APIs and the `/v1/esLogging` frontend API-error logging endpoint.

## Migration Scope

The Indonesia migration plan assigns the following current GDC responsibilities to this service:

- `/v2/customview/filters`
- `/v2/customview/views`
- `/v1/esLogging`

Custom Search/View is intended to move to [[51358-ratan-cash-settlement-query-service]]. The final Indonesia owner for `/v1/esLogging` remains unresolved between that query service and [[audit-trail]].