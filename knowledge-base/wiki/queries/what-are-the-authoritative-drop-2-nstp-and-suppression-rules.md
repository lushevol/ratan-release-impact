---
type: query
title: What Are the Authoritative Drop 2 NSTP and Suppression Rules?
created: 2026-08-23
updated: 2026-08-23
tags: [drop-2, nstp, suppression-rules, static-data, requirements]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2024-changes--23-drop2--onyd9i, static-data-readiness, entity-onboarding-static-data-controls, fmrp-trade-attribute-cashflow-nstp, cashflow-suppression-vs-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Drop2 Drop3 Static Data.md"]
---
# What Are the Authoritative Drop 2 NSTP and Suppression Rules?

## Question

What are the complete and authoritative NSTP and suppression rules intended for Drop 2?

## Current Evidence

The source contains only the headings “Drop 2 NSTP Rules” and “Drop 2 Suppression Rules.” It does not provide executable logic, predicates, priorities, exceptions, expected outcomes, affected products or entities, currencies, settlement flows, configuration ownership, or evidence of testing and production deployment.

## Information Needed

Resolve the following:

- the meaning and scope of NSTP in the Drop 2 context;
- the affected products, entities, currencies, and settlement flows;
- rule conditions, precedence, exceptions, and expected outcomes;
- the authoritative configuration repository and owning team;
- approval, test, implementation, and production-deployment evidence;
- whether the suppression mechanism concerns cashflows, SWIFT messages, entities, or another layer.

Until this information is found, the document should be treated as an outline rather than a functional requirement. Its NSTP terminology must not be assumed to refer to [[fmrp-trade-attribute-cashflow-nstp]], [[nds-netting]], or another existing control without corroborating evidence.

## Related Context

This query supports the static-data governance concerns described in [[static-data-readiness]] and [[entity-onboarding-static-data-controls]]. The distinction in [[cashflow-suppression-vs-swift-suppression]] should remain unresolved for this source until the applicable suppression layer is identified.