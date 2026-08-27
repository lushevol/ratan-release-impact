---
type: entity
title: TAEYUAN
created: 2026-08-22
updated: 2026-08-22
tags: ["legal-entity", "tranche-3", "static-data", "routing", "cash-settlement", "swift"]
related: ["zhengzhou", "jersey", "lms", "entity-onboarding-static-data-controls", "what-is-the-authoritative-lms-routing-policy-for-jersey-zhengzhou-and-taeyuan", "ratan", "tranche-3-entity-onboarding", "ssi-dual-blind-input"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3  Static data go live checklist.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3 Onboarding.md"]
---
# TAEYUAN

TAEYUAN is a Tranche 3 entity configured for [[ratan]] settlement processing and intended to flow to [[lms]]. The Tranche 3 static-data checklist names TAEYUAN as requiring entity-level SWIFT static-data configuration and routing to [[lms]].

## Static-data configuration

The onboarding source records the following values:

| Attribute | Value |
|---|---|
| FMID | `400516443` |
| Branch code | `73` |
| Sender BIC | `SCBLCNSXTAY` |
| Field 53 BIC | `SCBLCNSXGMO` |
| Field 53 currency | `CNY` |
| Field 58 BIC | `SCBLCNSXGMO` |

The static-data go-live checklist itself does not provide the underlying static-data values.

## Testing and production status

The onboarding source records TAEYUAN as already in production for Cashflow Blotter configuration as of 2025-09-16. UAT case 31, message `M00119946456`, records a maker settlement-means modification followed by checker approval.

The supplied checklist does not establish formal UAT acceptance or production routing verification. It also does not provide LMS test evidence or production deployment confirmation.