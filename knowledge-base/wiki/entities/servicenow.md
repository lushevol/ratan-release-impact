---
type: entity
title: ServiceNow
created: 2026-08-22
updated: 2026-08-22
tags: [ServiceNow, SNOW, change-management, release-governance]
related: [ado, release-readiness-attestation, ratan-bau-release-pre-cab-checklist]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan Pre-Cab Checklist 2026/2026_08_29_CHG1053540_Ratan BAU Release - 29th Aug.md"]
---

# ServiceNow

## Role in the RATAN release

ServiceNow, referred to as **SNOW** in the questionnaire, is the change-management context for the RATAN BAU release. The pre-cab checklist uses the SNOW section to capture change scope, justification, testing evidence, implementation, rollback, scheduling, resource booking, Safe Change attestation, documentation updates, and monitoring.

## Recorded controls

The checklist records:

- Six ADO work items as the change scope.
- An implementation plan of `All ADO pipelines`.
- A rollback plan of `All ADO pipelines`.
- A change date of `29/08/2026`.
- A PSS booking from `09:00~10:00`.
- A Safe Change response of `SAFE`.

The test evidence is incomplete: functional testing is marked `in progress`, while regression, performance, UAT, and DR evidence are not populated.

## Readiness limitation

ServiceNow checklist completion should be distinguished from evidence that the release is operationally ready. The source does not provide detailed UVT coverage, pipeline identifiers, database recovery steps, field-rename compatibility analysis, or supporting Safe Change Dashboard evidence.