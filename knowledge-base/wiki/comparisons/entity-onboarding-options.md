---
type: comparison
title: Entity Onboarding Options
created: 2026-08-23
updated: 2026-08-23
tags: [entity-onboarding, static-data, design-options, cash-settlement]
related: [concepts/self-service-entity-onboarding, entities/new-entity-onboarding, concepts/static-data-blotter, concepts/nostro-csv-bulk-maintenance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Self‑service new entity & branch onboarding.md"]
---

# Entity Onboarding Options

The requirement presents two approaches for reducing deployment dependency in new-entity onboarding.

| Dimension | Option 1: Excel template import | Option 2: Onboarding blotter with sub-tiles |
|---|---|---|
| Primary interaction | User uploads a file containing static data | User accesses separate static-data areas through an onboarding UI |
| Scope presentation | One general import for all static data | Required domains are exposed as separate sub-tiles |
| Source treatment | Struck through in the requirement | Emphasized as the proposed direction |
| Existing capability reuse | Not specified | Explicitly reuses the Nostro Static blotter and adds bulk upload |
| Completeness visibility | Not specified | Includes an onboarding dashboard with missing-static visibility |
| Governance model | Not specified | Static Ops edit; other profiles read-only, following Nostro Static |
| Main unresolved risk | File schema, validation, and failure handling | Cross-domain consistency, completion state, and API ownership |

## Assessment

Option 2 is the apparent preferred direction because it provides a dashboard and separates the required static-data areas. However, the source does not record a formal approval, implementation decision, or rejection rationale for Option 1.

The final design may be hybrid: UI entry for several domains and bulk upload for Nostro Static. Existing upload contracts should be validated rather than assumed to apply automatically.