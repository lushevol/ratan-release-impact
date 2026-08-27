---
type: concept
title: Entity Routing and Cashflow Suppression
created: 2026-08-22
updated: 2026-08-22
tags: [routing, cashflow-suppression, entity-whitelist, settlement]
related: [manual-entity-settlement-onboarding, ratan, cashflow-auto-netting, auto-netting-rule-management, clearing-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/00 Manual Entities Onboarding Checklist.md"]
---
# Entity Routing and Cashflow Suppression

Entity onboarding can require configuration of several distinct allow/deny lists. The source does not state that these lists share matching logic, scope, or precedence.

## Identified routing controls

The checklist distinguishes:

- An LMS feed blacklist.
- Legacy workflow entities: `EG/NP/SAUDI/LOANIQ`.
- Strategic-flow entities: `CN/SG/MY/IN/UK/DE`.
- A CPT entity list: `HK/TW/TH`.
- A RAZOR routing whitelist using `ORIGINAL_SYSTME_TAG:LOANIQ`.
- A SWIFT routing whitelist named `STRATEGIC_FM_LIST`.
- An existing non-FMRP cashflow-suppression rule to which manual entities should be added.

When a cashflow is routed to [[ratan]] rather than RAZOR, the source states that RATAN generates SWIFT and accounting output.

## Control boundary

Cashflow suppression, workflow routing, LMS feeds, and SWIFT suppression are related but separate controls. The checklist does not authorize treating membership in one list as membership in another.

`ORIGINAL_SYSTME_TAG` is reproduced exactly as written in the source. Its spelling must not be normalized without validating the actual configuration field.

See [[what-is-the-current-lms-feed-entity-filter-policy]] and [[are-loaniq-and-loanid-distinct-onboarding-identifiers]].