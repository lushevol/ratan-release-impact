---
type: concept
title: Rule Service Domain Boundaries
created: 2026-08-24
updated: 2026-08-24
tags: [service-boundaries, rule-engine, static-data, entitlement, cash-settlement]
related: [ratanone-rule-service, rule-service-consolidation, cash-settlement-data-entitlement, rule-engine-vs-workflow-orchestration, which-service-owns-fields-validation-rules-and-profile-limitation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# Rule Service Domain Boundaries

The archived migration design narrows the intended Rule Service scope by separating rule execution from adjacent data-management and frontend-validation responsibilities.

The stated boundary is:

- BAU Suppression and Netting Rules belong in [[ratanone-rule-service]].
- Data Entitlement Rule remains standalone and does not migrate.
- Fields and Fields Xpath should be removed from Rule Service and are most likely part of static data service.
- Frontend Validation Rules should be part of static data service rather than Rule Service.
- Profile Limitation remains within the Rule domain service.

The source identifies no concrete static data service, accountable owner, target API, migration mechanism, or client-transition plan. The question remains open in [[which-service-owns-fields-validation-rules-and-profile-limitation]].