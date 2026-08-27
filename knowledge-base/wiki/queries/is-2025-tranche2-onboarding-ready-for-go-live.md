---
type: query
title: Is 2025 Tranche 2 Onboarding Ready for Go-Live?
created: 2026-08-22
updated: 2026-08-22
tags: [query, go-live, readiness, uat, regression-testing]
related: [2025-tranche2-entity-onboarding, 2025-tranche2-onboarding-readiness, entity-configuration-scope-separation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch2 Onboarding.md"]
---

# Is 2025 Tranche 2 Onboarding Ready for Go-Live?

## Question

Are all required configuration, static-data, downstream, access, UAT, and regression-testing activities complete for the 2025 Tranche 2 entities and branches?

## Current Evidence

The source explicitly marks firewall access as `Done`. It marks UAT and regression testing as `No`, leaves downstream engagement incomplete, and records unresolved NDS Auto Netting and Pending Fixing STP/NSTP blacklists. It does not provide completion evidence for most configuration and static-data rows.

## Decision Standard

Go-live readiness should require:

- Approved legal entity and branch mappings.
- Verified routing, suppression, SSI, SWIFT, accounting, Nostro, and Vostro configuration.
- Resolution of all `TBD` blacklists and scope questions.
- Downstream impact assessment and sign-off.
- Completed UAT and regression testing with recorded evidence.
- Explicit approval of exceptions and items marked not required for Tranche 2.