---
type: concept
title: Configuration-Driven Onboarding
created: 2026-08-22
updated: 2026-08-22
tags: [onboarding, configuration, static-data, change-management, cash-settlement]
related: [entity-branch-onboarding, production-release-management, maker-checker-segregation, nostro-static-management, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list.md"]
---
# Configuration-Driven Onboarding

Configuration-driven onboarding is the controlled addition of an entity, branch, or product through platform configuration, static data, rule maintenance, and release governance rather than bespoke core-application development.

For [[ratan]], the intended global operating model is configuration-led. Required setup can include routing scope, SWIFT local static data, release cutoffs, SSI behavior, currency mappings, settlement accounting, GUI dropdowns, Nostro and Vostro data, business rules, firewall access, and downstream-system analysis.

## Delivery Models

Two complementary operating models are documented:

1. **Bulk project delivery:** Operations reviews data or rules, Dev Team applies scripts, and a Change Request deploys the result to production.
2. **BAU maintenance:** Authorized operational teams maintain lower-volume static data and rules through the RATAN GUI, with maker/checker control.

Configuration-led does not mean no engineering effort. Dev Team involvement may still be required for CR deployment, scripts, network access, regression testing, and downstream impact assessment.

## Required Controls

- Operational review and approval of static data.
- CR-controlled production deployment where required.
- Maker/checker segregation for GUI maintenance.
- UAT by Settlement Ops, regression testing by Dev Team, and CPT by MO/Settlement Ops.
- Entity-specific assessment of routing, LMS eligibility, and downstream reporting or data needs.

## Related Pages

- [[entity-branch-onboarding]]
- [[production-release-management]]
- [[maker-checker-segregation]]
- [[nostro-static-management]]
- [[ratan]]