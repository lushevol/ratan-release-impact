---
type: query
title: What Are the Authoritative Tranche 2 Entity Routing Lists?
created: 2026-08-22
updated: 2026-08-22
tags: [query, entity-onboarding, routing, configuration]
related: [2025-tranche2-entity-onboarding, entity-configuration-scope-separation, lms, nds-auto-netting, cashflow-suppression, ssi-selection-hierarchy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch2 Onboarding.md"]
---

# What Are the Authoritative Tranche 2 Entity Routing Lists?

## Question

How should the LMS blacklist, Murex H2 Adaptor whitelist, BCS and strategic-routing whitelist, SSI exceptions, NDS Auto Netting blacklist, and Pending Fixing STP/NSTP blacklist be reconciled?

## Evidence

The checklist defines different populations for these controls and leaves the NDS Auto Netting and Pending Fixing lists as `TBD`. It also describes legacy, strategic, and CPT routing populations without defining a complete decision table between BCS, RAZOR, and RATAN.

## Required Resolution

Produce an approved mapping from legal entity and branch to each independent configuration domain. The mapping should identify the authoritative owner, effective date, routing path, blacklist or whitelist status, and exception rationale.