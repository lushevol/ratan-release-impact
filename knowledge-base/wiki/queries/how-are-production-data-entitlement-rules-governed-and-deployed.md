---
type: query
title: How Are Production Data Entitlement Rules Governed and Deployed?
created: 2026-08-24
updated: 2026-08-24
tags: [governance, production, data-entitlement, ems2, deployment]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technica--yw24rt, ems2, oud, static-data-service, query-service, api-gateway, group-management-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Option2  RATAN existing data entitlement implementation.md"]
---
# How Are Production Data Entitlement Rules Governed and Deployed?

## Question

Which system owns each production entitlement artifact, and how are entitlement changes approved, deployed, audited, and rolled back?

## Evidence

The source states that non-production onboarding requires manual database configuration. It states that production entitlement data is maintained in [[ems2|EMS2]], while also stating that adding rules requires a new deployment.

The documented architecture includes:

- [[ems2|EMS2]] roles, subjects, and actions for function entitlement.
- [[oud|OUD]] country data embedded in the login token.
- [[static-data-service|static-data-service]] entitlement-rule retrieval.
- [[query-service|Query Service]] record filtering.
- [[api-gateway|API gateway]] function-entitlement registration.

## Unknowns

The source does not distinguish whether `permitted_rule`, `forbidden_country`, and `forbidden_rule` are managed in EMS2, in static-data configuration, or in application code. It also does not identify approvers, change owners, audit records, rollback procedures, or emergency-access controls.

## Required Resolution

Document ownership and change controls for identity data, function entitlements, data-entitlement rules, service deployment, and downstream enforcement before treating the indicative estimates as a delivery commitment.