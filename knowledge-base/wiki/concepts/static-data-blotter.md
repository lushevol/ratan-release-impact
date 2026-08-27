---
type: concept
title: Static-Data Blotter
created: 2026-08-23
updated: 2026-08-23
tags: [static-data, blotter, user-interface, operations]
related: [concepts/self-service-entity-onboarding, entities/new-entity-onboarding, concepts/nostro-csv-bulk-maintenance, entities/nostro-upload-api]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Self‑service new entity & branch onboarding.md"]
---

# Static-Data Blotter

A static-data blotter is a user interface for viewing and editing operational configuration records. In the proposed self-service onboarding design, required static-data domains are presented as separate sub-tiles within the onboarding experience.

## Application to onboarding

The source proposes a new onboarding blotter rather than a single general Excel import. The blotter is expected to expose:

- Currency Mapping
- Branch Code
- Nostro Static
- Swift Generation
- Release Time
- Accounting Static

The existing Nostro Static blotter is specifically referenced as a reusable capability and permission-model precedent.

## Access and governance

Static Ops users are intended to edit records, while other user profiles are read-only. The requirement does not define approval workflows, audit trails, rollback, or whether permissions are uniform across all sub-tiles.

## Boundary

A blotter is a proposed UI mechanism, not a confirmed API or persistence contract. Existing Nostro upload behavior and validation rules must be verified before being reused for onboarding.