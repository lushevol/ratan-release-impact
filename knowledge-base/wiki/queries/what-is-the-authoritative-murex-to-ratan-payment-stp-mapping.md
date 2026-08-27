---
type: query
title: What Is the Authoritative Murex-to-RATAN Payment STP Mapping?
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, payment-stp, nstp, governance]
related: [murex, ratan-one, fmrp, payment-stp-exception-catalogue, murex-to-ratan-exception-mapping, murex-payment-stp-vs-ratan-nstp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 Payment Non-STP Exception.md"]
---
# What Is the Authoritative Murex-to-RATAN Payment STP Mapping?

The source documents intended handling for legacy Murex2.11 Payment STP rules, but it does not provide a version-controlled, complete target mapping.

The authoritative mapping should establish:

- the RATAN exception, NSTP condition, lifecycle state, or retention outcome for every Murex rule;
- entity and release applicability, including China Day 1 and Day 2 boundaries;
- the target static-data model for exclusions and eligibility;
- the SCI and TDS3 field contracts needed for `ATLAS Sub-segment` and `COMP`;
- whether each mapped control is deployed and enabled in production.

The mapping must preserve semantic differences, particularly for SSI validation, trade affirmation, amendment handling, reversals, cancellations, netting, and non-deliverable NDS flows.