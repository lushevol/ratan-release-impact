---
type: entity
title: New Entity Onboarding
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, onboarding, user-interface, static-data]
related: [entities/cash-settlement-home-page, concepts/self-service-entity-onboarding, concepts/onboarding-dashboard, concepts/static-data-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Self‑service new entity & branch onboarding.md"]
---

# New Entity Onboarding

New Entity Onboarding is the proposed entry point for self-service entity and branch configuration in the Cash Settlement Home Page.

## Role

The feature is intended to replace or reduce the current process of backend configuration changes, static-data imports, and scheduled deployments. It is expected to open an [[concepts/onboarding-dashboard]] and provide access to required static-data areas through separate sub-tiles.

## Proposed sub-tiles

- Currency Mapping
- Branch Code
- Nostro Static
- Swift Generation
- Release Time
- Accounting Static

The source does not define the final navigation, implementation status, completion criteria, or persistence model.

## Permissions

Static Ops users are proposed to have edit access. Other user profiles are proposed to have read-only access, matching the existing Nostro Static blotter model.