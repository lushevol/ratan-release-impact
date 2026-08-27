---
type: concept
title: RATAN Indonesia Dual-Environment UAT
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, uat, environment, fmrp1, dev]
related: [ratan-indonesia, ratan-indonesia-onshoring-2026, markets-operations-one, fmo-post-trade-portal-dev, ratan-indonesia-uat-access-provisioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RATAN ID Cash Settlements Migration - UAT Scope.md"]
---
# RATAN Indonesia Dual-Environment UAT

RATAN Indonesia migration UAT is scoped across two environments:

- [[markets-operations-one]] (FMRP1) is the primary environment.
- [[fmo-post-trade-portal-dev]] (DEV) is the secondary environment.

This designation alone does not define a test-execution strategy. The source does not identify which tests must run in each environment, whether tests must be repeated across both, or whether their data, integrations, and entitlement configuration are comparable. These gaps should be resolved before environment coverage is used as an acceptance measure.