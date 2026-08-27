---
type: concept
title: Entity Configuration Scope Separation
created: 2026-08-22
updated: 2026-08-22
tags: [entity-onboarding, configuration-management, routing, static-data]
related: [2025-tranche2-entity-onboarding, entity-branch-onboarding, ssi-selection-hierarchy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch2 Onboarding.md"]
---

# Entity Configuration Scope Separation

Entity onboarding controls may use different entity populations and must be maintained independently. In the Tranche 2 checklist, the LMS blacklist, Murex H2 Adaptor whitelist, routing whitelist, SSI exceptions, NDS Auto Netting blacklist, and Pending Fixing STP/NSTP blacklist are separate configuration domains.

For example, the LMS blacklist is `EG/NP/SAUDI/KL/TH/TW`, while the routing lists distinguish legacy flow, strategic flow, and an additional CPT list. The NDS Auto Netting and Pending Fixing lists are unresolved. Combining these populations without an explicit mapping creates a risk of incorrect filtering, routing, or settlement behavior.