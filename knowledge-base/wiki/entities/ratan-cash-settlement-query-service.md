---
type: entity
title: ratan-cash-settlement-query-service
created: 2026-08-22
updated: 2026-08-23
tags: ["ratan", "cashflow", "query-service", "graphql", "read-model", "cash-settlement", "deployment", "query", "nostro"]
related: ["ratan", "ratan-cashflow-lifecycle-service", "ratan-cqrs-cashflow-read-model", "rfi-dedicated-nostro-stamping", "rfi-nostro-stamping-based-on-portfolio", "nostro-notification-and-refresh"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md"]
---
# ratan-cash-settlement-query-service

`ratan-cash-settlement-query-service` is the stated read-side service for RATAN cashflow data. It consumes lifecycle events to maintain query data and provides UI and external query APIs.

## Capabilities

The technical-design source assigns the service:

- Cashflow creation and update data storage for query purposes.
- Cashflow blotter queries and notifications.
- Cashflow-detail queries.
- External APIs for RATAN EOD and SSDR.

Its GraphQL interface combines cashflow details with trade details, exception details, exception-stashing data, and Vostro/Nostro SSI candidates.

The listed tables are:

- `cashflow_data`
- `cashflow_data_history`
- `t_event`

The design does not specify consistency targets, replay, recovery, or data-authority precedence; see [[ratan-cqrs-cashflow-read-model]].

## RFI dedicated-Nostro enablement

The RFI dedicated-Nostro stamping design includes `ratan-cash-settlement-query-service` in its proposed deployment set. That source does not specify detailed functional changes for this service.

The Change List and API requirement specifies cashflow-detail response changes for RFI classification:

- The GraphQL cashflow-detail contract adds `Nostro_Type` and `Dedicated { Portfolio }` to `ratanNostroCandidates`.
- Cashflow-detail `nostroType` is based on the domain event, connecting this read model to [[ratan-cashflow-lifecycle-service]].