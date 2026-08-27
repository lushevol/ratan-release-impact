---
type: query
title: Are RDM Common Files and Bank-Code Data Permanently Out of Scope for Indonesia?
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, indonesia, scope, bank-code, lei, rule-engine]
related: [rdm, rdm-api-based-holiday-compensation, ratan-indonesia-onshoring-2026]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation.md"]
---
# Are RDM Common Files and Bank-Code Data Permanently Out of Scope for Indonesia?

The source excludes common RDM configuration files and bank-code/LEI data from the immediate Indonesia compensation design. The stated basis is current caller analysis: common files are used for trade rule checking, while bank-code/LEI lookups are described as UK CHAPS-specific.

## Questions to Resolve

- Are any planned Indonesia trade-processing, rule-checking, SWIFT, or payment flows dependent on these datasets?
- What change trigger requires re-evaluation of the excluded RDM feeds?
- Can the Indonesia platform safely omit related tables, endpoints, monitoring, and reconciliation processes?
- Who approves a permanent scope exclusion versus a deferred integration?

## Evidence

The current decision supports minimizing the Indonesia implementation scope, but it is conditional on present integrations and does not establish a durable product-wide exclusion.