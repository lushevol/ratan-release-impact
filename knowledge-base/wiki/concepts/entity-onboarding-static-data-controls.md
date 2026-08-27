---
type: concept
title: Entity Onboarding Static-Data Controls
created: 2026-08-22
updated: 2026-08-22
tags: [entity-onboarding, static-data, settlement, go-live-controls]
related: [static-data-readiness, cashflow-migration-readiness, cashflow-suppression-vs-swift-suppression, payment-and-cashflow-suppression-governance, release-readiness-attestation, jersey, zhengzhou, taeyuan, lms]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3  Static data go live checklist.md"]
---
# Entity Onboarding Static-Data Controls

Entity onboarding static-data controls are the coordinated configuration checks needed before an entity can participate safely in settlement processes.

## Control categories

The Tranche 3 checklist identifies the following categories:

- SSI and nostro data;
- bridge-account configuration;
- entity-level SWIFT static data;
- currency-category suppression rules;
- non-FMRP entity classification;
- CPT Control;
- manual-entity setup in a blotter; and
- downstream LMS routing.

These controls are interdependent. An entity record alone does not establish operational readiness if routing, suppression, account, or settlement-instruction configuration remains unresolved.

## Readiness boundary

A configuration checklist and UAT rule identifiers demonstrate planned or environment-specific setup, not formal production approval. A readiness claim requires evidence of production deployment, validation, ownership, rollback capability, and authorised sign-off. See [[release-readiness-attestation]].

## Tranche 3 example

For [[jersey]], the source records SSI and account references, a non-FMRP cashflow-suppression requirement, manual blotter setup, and exclusion from [[lms]]. For [[zhengzhou]] and [[taeyuan]], it records entity-level SWIFT static data and inclusion in LMS routing.