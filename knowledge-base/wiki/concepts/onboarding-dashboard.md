---
type: concept
title: Onboarding Dashboard
created: 2026-08-23
updated: 2026-08-23
tags: [entity-onboarding, dashboard, static-data, completeness]
related: [entities/new-entity-onboarding, concepts/self-service-entity-onboarding, entities/cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Self‑service new entity & branch onboarding.md"]
---

# Onboarding Dashboard

The onboarding dashboard is the proposed drilldown view opened from the `New Entity Onboarding` tile on the Cash Settlement Home Page.

## Proposed fields

| FMID | FMCODE | Status | Missing Static |
|---|---|---|---|
|  |  |  | Format to be confirmed |

The dashboard is intended to show which entities are being configured, their current status, and the required static-data categories that remain incomplete.

## Unresolved behavior

The source does not define:

- Allowed status values
- How status is derived
- How missing static data is calculated
- Whether completion is evaluated per domain or across the entire entity
- Whether partially configured entities can be used operationally
- Refresh, error, or retry behavior

These rules are necessary before the dashboard can serve as an authoritative onboarding control.