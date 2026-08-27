---
type: concept
title: Self-Service Entity Onboarding
created: 2026-08-23
updated: 2026-08-23
tags: [self-service, entity-onboarding, branch-onboarding, static-data, cash-settlement]
related: [entities/cash-settlement-home-page, entities/new-entity-onboarding, concepts/static-data-blotter, concepts/onboarding-dashboard, comparisons/entity-onboarding-options, entities/nostro-upload-api, entities/settlement-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Self‑service new entity & branch onboarding.md"]
---

# Self-Service Entity Onboarding

Self-service entity onboarding is the proposed capability for configuring the static data required to introduce a new booking entity and its branches without relying on backend changes, static-data imports, or scheduled deployment windows.

## Proposed workflow

The workflow starts from the `New Entity Onboarding` tile on the [[entities/cash-settlement-home-page]]. An [[concepts/onboarding-dashboard]] provides a high-level view of each entity, including FMID, FMCODE, status, and missing static data. Users then access separate static-data sub-tiles for the required configuration areas.

The proposed areas are:

- Currency Mapping
- Branch Code
- Nostro Static
- Swift Generation
- Release Time
- Accounting Static

This is a coordinated onboarding experience across multiple static-data domains rather than a single front-end form.

## Access model

Static Ops users are proposed as editors, while other user profiles are read-only. The source aligns this model with the existing Nostro Static blotter. It does not establish whether maker-checker approval, category-specific authorization, audit history, or rollback is required.

## Mandatory and deferred scope

The initial UI scope includes the six required static-data areas listed above. PM CCY, PM CCY Receiver BIC, UDF_Strategy, UDF_SWF_LS, and CFI Code Mapping are explicitly deferred and remain in the backend for now.

The source does not define whether deferred data is required for later lifecycle stages or how it will eventually be configured.

## Design implications

The capability should provide:

- Visibility of incomplete static configuration
- Reuse of existing Nostro Static permissions and, where appropriate, upload behavior
- Validation across identifiers, currencies, BICs, accounting references, and time-zone fields
- Clear handling of partial saves and failed uploads
- An explicit definition of when an entity is fully onboarded

The source does not establish atomicity across the six static-data domains. Each domain may therefore require an independent persistence and error-handling contract unless the linked design specifies otherwise.