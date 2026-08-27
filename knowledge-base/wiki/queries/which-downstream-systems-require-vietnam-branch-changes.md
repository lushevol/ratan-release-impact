---
type: query
title: Which Downstream Systems Require Vietnam Branch Changes?
created: 2026-08-22
updated: 2026-08-22
tags: [vietnam, downstream-systems, integration, open-question]
related: ["vietnam-ifc-branch", "ratan", "lms", "entity-branch-onboarding"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/2026 Entity Onboarding - new branch setup in Vietnam.md"]
---
# Which Downstream Systems Require Vietnam Branch Changes?

## Question

Which downstream systems require configuration, report migration, payload changes, or testing for the proposed [[vietnam-ifc-branch]]?

## Current Evidence

The checklist marks downstream engagement as not required, but the source directs the implementation team to check:

- RATAN EOD for report migration.
- SSDR for additional cashflow information.
- CIS for additional cashflow information.
- FMMIS for additional cashflow information.

Participation in [[lms]] is also unresolved. The “not required” checklist value may mean that no build is currently assumed, rather than that stakeholder engagement can be omitted.

## Evidence Needed

For each downstream system:

- Inclusion or exclusion decision.
- Required entity and branch identifiers.
- Data and report requirements.
- Historical or migration requirements.
- Interface and schema impact.
- SIT and UAT obligations.
- Production readiness owner.
- Written sign-off.