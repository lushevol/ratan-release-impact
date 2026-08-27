---
type: entity
title: ZHENGZHOU
created: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3  Static data go live checklist.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3 Onboarding.md"]
tags: ["legal-entity", "tranche-3", "static-data", "routing", "cash-settlement", "swift"]
related: ["taeyuan", "jersey", "lms", "entity-onboarding-static-data-controls", "what-is-the-authoritative-lms-routing-policy-for-jersey-zhengzhou-and-taeyuan", "ratan", "tranche-3-entity-onboarding", "ssi-dual-blind-input"]
updated: 2026-08-22
---

# ZHENGZHOU

ZHENGZHOU is a Tranche 3 entity configured for [[ratan]] settlement processing and intended to flow to [[lms]].

The Tranche 3 static-data go-live checklist names ZHENGZHOU as requiring entity-level SWIFT static-data configuration and routing to [[lms]].

## Static-data attributes

| Attribute | Value |
|---|---|
| FMID | `400516442` |
| Branch code | `73` |
| Sender BIC | `SCBLCNSXZZH` |
| Field 53 BIC | `SCBLCNSXGMO` |
| Field 53 currency | `CNY` |
| Field 58 BIC | `SCBLCNSXGMO` |

## Configuration and testing status

The onboarding source records ZHENGZHOU as already in production for Cashflow Blotter configuration as of 2025-09-16.

That source also references UAT maker-checker cases for ad hoc SSI submission, rejection, correction, resubmission, and approval. It does not provide formal UAT sign-off or end-to-end LMS-routing evidence.

The static-data go-live checklist does not provide the underlying static-data values, LMS test evidence, or production deployment confirmation.