---
type: query
title: What Static Data Changes Are Required in Rule Service for Beneficiary BIC Netting?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, beneficiary-bic, rule-service, static-data, open-question]
related: [beneficiary-bic-netting, cash-settlement-beneficiary-bic-netting-design, ratanone-rule-service, 51358-ratanone-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Beneficiary BIC Netting Design.md"]
---
# What Static Data Changes Are Required in Rule Service for Beneficiary BIC Netting?

## Question

What does the source’s “Rule service (only static data)” scope mean in concrete technical and operational terms?

## Confirmed Boundary

The source explicitly limits Rule service changes to static-data concerns. It does not state that Rule service evaluates transactional Beneficiary BIC netting rules, owns netting decisions, or controls Lifecycle service processing.

## Unresolved Scope

The source does not clarify whether the Rule service must support:

- Static-data storage or schema changes.
- Beneficiary BIC validation.
- Reference-data configuration.
- BIC enrichment or normalization.
- Distribution to Netting service, Lifecycle service, Query service, or Front End.
- Versioning, activation, deactivation, or effective dating.
- Synchronization with [[51358-ratanone-static-data-service]] or another reference-data owner.
- Audit, reconciliation, migration, or rollback behavior.

It also does not identify whether [[ratanone-rule-service]] is the concrete service referred to by the generic “Rule service” label.

## Evidence

The only direct evidence is the service inventory in [[cash-settlement-beneficiary-bic-netting-design]], where Rule service is annotated as “only static data.” No endpoint, schema, event, repository, deployment, or acceptance criterion is provided.

## Current Assessment

The static-data-only boundary should be preserved, but no more specific responsibility should be inferred until a detailed design or implementation reference identifies the required changes and ownership model.