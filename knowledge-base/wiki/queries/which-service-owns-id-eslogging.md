---
type: query
title: Which Service Owns ID esLogging?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, eslogging, audit-logging, indonesia, service-ownership]
related: [audit-trail, 51358-ratan-cash-settlement-query-service, 51358-ratanone-query-service, cash-settlement-audit-api-migration, frontend-error-logging-and-user-action-analytics]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Audit API migration plan from GDC to ID.md"]
---
# Which Service Owns ID esLogging?

Should the retained Indonesia frontend API-error endpoint `/v1/esLogging` be implemented in [[audit-trail]] or [[51358-ratan-cash-settlement-query-service]]?

## Evidence

The source lists `51358-ratan-cash-settlement-query-service` as the Indonesia location, while attributing a proposal from Lu and Shuai to implement the endpoint in `audit-trail`. It closes with the unresolved question of whether the API should move to `audit-trail` or remain in the query service.

## Decision Criteria Needed

- Service ownership and operational support model.
- Compatibility with the existing GDC endpoint.
- Frontend routing and authentication requirements.
- Elasticsearch or Logstash integration for `ratanrt-logs-app-*`.
- Indonesia data residency, retention, privacy, and access-control requirements.
- Migration sequencing, rollback, and GDC endpoint retirement conditions.