---
type: concept
title: Settlement Booking-Entity Configuration
created: 2026-08-24
updated: 2026-08-24
tags: [settlement, booking-entity, fmid, fmcode, static-configuration]
related: [static-configuration-management, schema-validated-static-configuration, mfe-cashflow-blotter, mfe-trades, ratanone-settlement-orchestration-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft).md"]
---
# Settlement Booking-Entity Configuration

Settlement booking-entity configuration is high-change, shared configuration that associates an FMID, FM Code, flow classification, and country metadata for settlement onboarding and related user interfaces.

The draft models this as the `settlement_booking_entities` context. Example flow values are `NORMAL`, `STRATEGIC`, and `CPT`; example records associate IDs `10036642` and `400899993` with China booking entities.

## Consumers

The source assigns the context to:

- [[mfe-cashflow-blotter]]
- [[mfe-cashflow-dashboard]]
- [[mfe-trades]]
- [[ratanone-settlement-orchestration-service]]

This shared consumption is the central reason to manage the data outside individual UI code. The source does not define whether service consumers read the same context directly, derive whitelist fields from it, or receive replicated configuration.

## Relationship to whitelist fields

The source presents `FM_LIST`, `STRATEGIC_FM_LIST`, and `CPT_ENTITY_LIST` as backend configuration examples. It does not define a canonical transformation between those pipe-delimited fields and structured booking-entity records. That mapping, including country filtering and flow semantics, remains an implementation question.