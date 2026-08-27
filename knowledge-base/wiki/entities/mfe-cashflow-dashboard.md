---
type: entity
title: mfe-cashflow-dashboard
created: 2026-08-24
updated: 2026-08-24
tags: [micro-frontend, cashflow, static-configuration]
related: [static-data-service, mfe-cashflow-blotter, settlement-booking-entity-configuration, schema-validated-static-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft).md"]
---
# mfe-cashflow-dashboard

`mfe-cashflow-dashboard` is a web micro-frontend listed as a consumer of centrally managed static configuration.

The draft assigns it to `settlement_field_type_operator_mapping` and `settlement_booking_entities`. This indicates a shared configuration need with [[mfe-cashflow-blotter]], although the dashboard-specific user journeys and integration contract are not described.