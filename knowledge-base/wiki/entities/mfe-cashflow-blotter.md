---
type: entity
title: mfe-cashflow-blotter
created: 2026-08-24
updated: 2026-08-24
tags: [micro-frontend, cashflow, static-configuration, ratan, frontend]
related: [static-data-service, mfe-cashflow-dashboard, settlement-booking-entity-configuration, schema-validated-static-configuration, ratanone, ratan-static-data-service, static-code-in-ui]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft).md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft)/Static Code In UI.md"]
---
# mfe-cashflow-blotter

`mfe-cashflow-blotter` is a web micro-frontend and frontend module identified in the draft design as a consumer of static configuration and as the principal location of hard-coded Cash Settlement UI configuration.

## Static-configuration usage

The draft design assigns `mfe-cashflow-blotter` to the following configuration contexts:

| Configuration context | Change frequency | Intended use |
|---|---:|---|
| `settlement_field_type_operator_mapping` | Low | Filter-builder and advanced-search operator conversion |
| `settlement_booking_entities` | High | Booking-entity options |

The proposed configuration service would remove these mutable values from UI code and releases.

The draft assigns `mfe-cashflow-blotter` to both contexts but does not define its API contract, cache TTL, stale-data tolerance, or authorization requirements. See [[cache-first-static-configuration-retrieval]].

## Hard-coded UI configuration inventory

The inventory in [[static-code-in-ui]] covers the following Cashflow Blotter areas:

- Quick search
- Advanced-search operator conversion
- Quick filters
- Grid definitions
- Detail history
- Bulk exception preview
- Gross-exception behavior
- Dashboard search options
- Status indicators

## Migration boundary

`mfe-cashflow-blotter` is a migration subject for centralized configuration; this does not itself establish that every embedded value should be remotely managed.

Executable behavior—including comparators, date calculation, conditional styling, and UI component implementations—requires a trusted frontend boundary under [[declarative-ui-configuration]].