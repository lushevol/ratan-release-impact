---
type: entity
title: ratanone-query-service
tags: [ratan, query-service, graphql, cashflow-blotter, monitoring]
related: [ratanone, itrs, ratan-itrs-alert-triage, ratan-data-entitlement, functional-versus-data-entitlement, ratan-nginx]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Monitoring/RATAN ITRS Log.md"]
---
# ratanone-query-service

`ratanone-query-service` serves RATAN query and cashflow-blotter requests and writes application errors to monitoring logs.

## Observed monitoring patterns

- A GraphQL `504 Gateway Time-out` was attributed to a complex cashflow-blotter filter.
- Browser notification websocket disconnections at `/api/ratan/notification/subscriptions` were considered normal consequences of VPN or network changes; the development disposition was to downgrade the log level.
- Missing data-entitlement roles are surfaced in the frontend and repeated in backend logs for PSS support.
- A GraphQL `BET` filter with `"values": null` produced `Between operator should have a value pair provided`.

The source classifies these events as having no confirmed systemic business impact, but invalid filters and missing entitlements can still prevent a user action. See [[concepts/ratan-itrs-alert-triage]].
