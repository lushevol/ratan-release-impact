---
type: project
title: RATAN Rule Engine v2 Migration
status: on-hold
owner: ""
start_date: 2024-01-31
target_date: ""
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, migration, rule-engine, scbml, json]
related: [ratan-rule-engine, json-based-rule-evaluation, client-json-input-vs-scbml-to-json-conversion]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]
---
# RATAN Rule Engine v2 Migration

## Objective

Move consumers from RATAN Rule Engine v1 to the proposed RatanOne Rule Service v2, with direct JSON input and domain-owned fact enrichment.

## Scope

The archived plan identifies:

- Rules migration for BCS, CN, and Trade Review.
- XML/SCBML-to-JSON migration for those consumers.
- Trade Review ownership of trade-relative functionality.
- CN ownership of specific processor functions.
- Drools performance enhancement by the Rule Service team.

## Risks

The migration transfers transformation responsibility to domain services and requires coordination of logical-model fields. Retaining v1 while ceasing maintenance creates operational risk for unmigrated consumers. The source also records unresolved custom-fact support and `tl-model-client` cashflow-parsing limitations.

## Status

This page is marked on-hold because the source is archived and provides no current completion evidence. The planned action date, 2024-01-31, is historical and does not establish whether migration activities were completed.

## Retrospective

A retrospective cannot be written from the source. Current consumer inventory, migration sign-offs, v1 decommissioning evidence, and v2 production ownership are required.