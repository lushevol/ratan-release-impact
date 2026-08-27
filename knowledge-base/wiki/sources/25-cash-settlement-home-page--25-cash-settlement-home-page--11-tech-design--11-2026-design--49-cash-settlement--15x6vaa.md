---
type: source
title: Audit API Migration Plan from GDC to ID
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, indonesia, gdc, api-migration, audit-logging, observability]
related: [cash-settlement-audit-api-migration, frontend-error-logging-and-user-action-analytics, shared-user-action-analytics-api, dev-only-analytics-api-retirement, which-service-owns-id-eslogging, 51358-ratanone-query-service, 51358-ratan-cash-settlement-query-service, audit-trail, single-ui-bff]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Audit API migration plan from GDC to ID.md"]
---
# Audit API Migration Plan from GDC to ID

This planning document records the intended GDC-to-Indonesia disposition of Cash Settlement frontend APIs for Custom Search/View, API-error logging, and user-action analytics. It is not a complete API specification: authentication, payload contracts, compatibility requirements, rollout controls, and retirement criteria are not supplied.

## Source Extract

| NO | function | API/kafka topic | location in GDC | location in ID | status | Conclusion | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Custom Search/View | /v2/customview/filters /v2/customview/views | 51358-ratanone-query-service | 51358-ratan-cash-settlement-query-service | | implement in 51358-ratan-cash-settlement-query-service, ID provide API as well | |
| 2-todo | UI call api err log save to logstash （1）API err | /v1/esLogging [https://fmo-mfe-dev.uk.dev.net:8453/api/ratan/v1/esLogging/production/warn](https://fmo-mfe-dev.uk.dev.net:8453/api/ratan/v1/esLogging/production/warn) **index = ratanrt-logs-app-*** | 51358-ratanone-query-service | 51358-ratan-cash-settlement-query-service | | Lu, Shuai suggests we keep this API. We will implement in audit-trail for ID FE log | should move to audit-trail? or stay in query-service |
| 3-todo | log user action to es (1)session control (2)cashflow blotter open | /v1/fmo/print **index = single-ui-bff-analytic** | single-ui-bff | | | no need BE implement, both GDC and ID should use same existing API | |
| 4-todo | log user action (1)only active in dev (API called by frontend ternary operatpr) (2)for non-dev call print API | [https://fmo-mfe-dev.uk.dev.net:8453/api/idns/ratan/v1/ratan-analytic](https://fmo-mfe-dev.uk.dev.net:8453/api/idns/ratan/v1/ratan-analytic) **index=ratan-analytic-data** | audit-trail | | | No need to implement, this API will be discarded | |

## Recorded Dispositions

- Implement `/v2/customview/filters` and `/v2/customview/views` in [[51358-ratan-cash-settlement-query-service]] for Indonesia.
- Retain `/v1/esLogging` for frontend API-error logs, but ownership is unresolved between [[audit-trail]] and [[51358-ratan-cash-settlement-query-service]].
- Reuse the shared [[single-ui-bff]] `/v1/fmo/print` API for session-control and cashflow-blotter-open analytics. The source states that no Indonesia backend implementation is needed.
- Do not implement the development-only `/v1/ratan-analytic` endpoint for Indonesia; the source states that it will be discarded. This does not retire user-action logging generally, because non-development environments use `/v1/fmo/print`.

## Open Architecture Issue

The `esLogging` row remains marked `todo` and explicitly asks whether the API should move to `audit-trail` or remain in the query service. Track this decision in [[which-service-owns-id-eslogging]].

The rows concerning shared analytics reuse and `ratan-analytic` retirement also remain marked `todo`; their stated conclusions should be treated as intended dispositions pending delivery confirmation.