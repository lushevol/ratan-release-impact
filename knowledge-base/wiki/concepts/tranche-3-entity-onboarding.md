---
type: concept
title: Tranche 3 Entity Onboarding
created: 2026-08-22
updated: 2026-08-22
tags: [entity-onboarding, static-data, uat, cash-settlement, go-live]
related: [ratan, cash-settlement-home-page, jersey, zhengzhou, taeyuan, lms, payment-and-cashflow-suppression-governance, ssi-dual-blind-input]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3 Onboarding.md"]
---
# Tranche 3 Entity Onboarding

Tranche 3 entity onboarding is the controlled configuration and validation needed to introduce a legal entity to the [[ratan]] cash-settlement operating model.

The checklist evidence identifies these control areas:

1. Entity identifiers, branch information, accounts, and SWIFT BIC static.
2. Entity-specific SWIFT and cashflow-suppression rules.
3. NSTP and netting scope decisions.
4. Routing eligibility to downstream systems such as [[lms]].
5. Cashflow Blotter search, filter, dropdown, and grouping configuration.
6. Go-live controls, including CPT Control where applicable.
7. UAT maker-checker validation for settlement means and SSI changes.

UAT configuration, workflow execution, business confirmation, production deployment, and formal acceptance are distinct evidence states. The source records examples of each but does not reconcile them into a single approved readiness status.

Requirements must remain entity-specific. In particular, JERSEY’s LMS exclusion and suppression rules cannot be inferred for [[zhengzhou]] or [[taeyuan]].