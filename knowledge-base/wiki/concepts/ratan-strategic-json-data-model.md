---
type: concept
title: RATAN Strategic JSON Data Model
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, json, data-model, uber, scbml, migration]
related: [ratan, ratan-one, uber, scbml, uber-legacy-workflow-isolation, murex-ratan-migration-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/RATAN - Uber Integration - Proposals.md"]
---
# RATAN Strategic JSON Data Model

## Definition

The RATAN strategic JSON data model is the target representation for Uber cashflow processing. It is intended to provide a strategic alternative to the legacy SCBML representation within RATAN settlement processing.

## Migration role

The design evaluates a full strategic migration, a Murex-preserving dual-workflow model, and a smallest-change approach that adds SCBML compatibility alongside JSON. The preferred proposal uses a new Uber workflow while integrating historical and Murex SCBML data in a later phase.

The target state is not yet fully specified. The source does not provide a JSON schema, field-level mapping, validation contract, or authoritative conversion rules.

## Scope distinction

Uber entity scope and JSON message format are separate attributes. Historical cashflows for `EG`, `NP`, and `SA` may be in Uber scope while still carrying SCBML. In some operations the source suggests real-time conversion so that resultants become JSON, but it does not define this as a final rule.

## Risks

The principal risks are dual-format persistence, inconsistent routing, incomplete historical migration, and behavioral differences between old and new lifecycle APIs.