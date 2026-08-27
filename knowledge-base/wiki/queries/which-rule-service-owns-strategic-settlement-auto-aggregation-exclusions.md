---
type: query
title: Which Rule Service Owns Strategic Settlement Auto-Aggregation Exclusions?
created: 2026-08-24
updated: 2026-08-24
tags: [rules, auto-aggregation, strategic-settlement, governance, netting]
related: [ratan-rule-engine, ratanone-rule-service, ratan-rule-service-ratan-rule, business-flow-and-rule-type-classification, rule-governance-and-auditability, strategic-cashflow, netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Product Agnostic Aggregation Design.md"]
---
# Which Rule Service Owns Strategic Settlement Auto-Aggregation Exclusions?

The source calls for a Rule Engine Service rule classified as `AUTO_AGGREGATION` and `STRATEGIC_SETTLEMENT`, with a hard-coded booking-entity and counterparty FMID condition. It does not identify the actual service that owns, deploys, evaluates, or communicates the rule result.

## Questions to Resolve

- Does the rule belong to [[ratan-rule-engine]], [[ratanone-rule-service]], [[ratan-rule-service-ratan-rule]], or another service?
- Are `AUTO_AGGREGATION` and `STRATEGIC_SETTLEMENT` canonical rule-type and business-flow values?
- What rule result blocks aggregation, and how does [[netting-service]] enforce it?
- Are all combinations of the stated booking-entity and counterparty FMIDs intended to match?
- Who owns the exception list, its business rationale, approval, audit trail, expiry date, and periodic review?
- Is the exclusion temporary, environment-specific, or a permanent policy?

The rule should not be treated as a governed operational control until these ownership and lifecycle details are established.