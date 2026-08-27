---
type: concept
title: Go-Live Decision Criteria
created: 2026-08-22
updated: 2026-08-22
tags: [go-live, UVT, onboarding, release-readiness, controls]
related: [f2b, fmrp, entity-branch-onboarding, production-release-management, post-implementation-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list.md"]
---
# Go-Live Decision Criteria

Go-live decision criteria are the explicit conditions and evidence required to approve production activation for an entity, branch, product, currency, or settlement flow.

## F2B checklist context

The final checklist item requires GO Decision Criteria and UVT Verification points. The source names this governance need but does not provide the criteria, verification results, approval record, or decision owner.

## Expected evidence areas

Criteria should cover:

- SSI and Nostro static-data completeness.
- Currency transformation and non-ISO currency handling.
- Netting eligibility and rule-conflict testing.
- Cashflow suppression and SWIFT suppression.
- MT/MX message generation and branch-specific mappings.
- EBBS, Aspire, LMS, RAZOR, CDUPS, and FMMIS routing.
- Migration cutover and duplicate-payment controls.
- Event, confirmation-match, and STP/NSTP behavior.
- Reconciliation, rollback readiness, and post-implementation monitoring.

The checklist should not be treated as evidence of go-live approval until these criteria and UVT outcomes are recorded.
