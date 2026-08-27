---
type: concept
title: SCBML Event Payload Storage Impact
created: 2026-08-24
updated: 2026-08-24
tags: [scbml, event-store, storage, capacity-planning, cash-settlement]
related: [ratanone-cashflow-service-cqrs-cashflow-events, ratan-query-service, cash-settlement-capacity-planning-baseline]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Ratan query service message consuming control.md"]
---
# SCBML Event Payload Storage Impact

SCBML event payload storage impact is the scenario-specific capacity effect of adding SCBML to event types that currently do not contain it in [[ratanone-cashflow-service-cqrs-cashflow-events]].

## Reported scenario

The source assumes that these currently non-SCBML event types grow from `1.14 kB` to the `5.76 kB` size stated for `CashflowAmendEvent`:

- `CashflowHoldInRatan`
- `CashflowSkipped`
- `CashflowStatusUpdateEvent`

On that assumption, the reported table size rises from `2,301 MB` to `3,658.6 MB`, an increase of **59%**.

## Interpretation limits

This is a planning estimate rather than a validated storage model. It assumes a common `5.76 kB` size for all three expanded event types. The source does not provide actual SCBML serialization sizes, compression behavior, physical row sizes, index growth, TOAST behavior, WAL volume, replication impact, or retention requirements.

Capacity decisions should validate the real payload-size distribution and the complete database storage footprint before using this estimate as a forecast.