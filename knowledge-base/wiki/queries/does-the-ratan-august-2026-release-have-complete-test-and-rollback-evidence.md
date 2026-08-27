---
type: query
title: Does the RATAN August 2026 Release Have Complete Test and Rollback Evidence?
created: 2026-08-22
updated: 2026-08-22
tags: [RATAN, release-readiness, testing, rollback, open-question]
related: [ratan-bau-release-pre-cab-checklist, release-readiness-attestation, ado, servicenow, cashflow-technical-failure-recovery]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan Pre-Cab Checklist 2026/2026_08_29_CHG1053540_Ratan BAU Release - 29th Aug.md"]
---

# Does the RATAN August 2026 Release Have Complete Test and Rollback Evidence?

## Question

Does the RATAN BAU release scheduled for 29 August 2026 have sufficient story-level testing, UVT, implementation, and rollback evidence for production deployment?

## Evidence currently recorded

The checklist records:

- Functional testing as `in progress`.
- No populated regression, performance, UAT, or DR evidence.
- No story-level UVT plan.
- `All ADO pipelines` as both the implementation and rollback plan.
- A one-hour release window from 09:00 to 10:00.
- Safe Change status as `SAFE`.

## Why the question remains open

The release includes changes with materially different validation and recovery requirements:

- A table-drop activity requires a documented backup, retrieval, and restoration path.
- The `auto_dvp_msg` column rename requires producer and consumer compatibility validation.
- The NSTP enhancement requires workflow and status-transition tests.
- The auto-netting enhancement requires explicit tests for both resultant and single cashflows.
- The Last Mile Check service requires integration, failure-path, and post-release verification.
- Rule-field validation requires tests for invalid, incomplete, and valid rule configurations.

Pipeline automation may support deployment and rollback, but the source does not show that it restores database state, dropped data, or schema consumers.

## Required evidence to resolve the query

1. Attach completed functional, regression, performance, UAT, and DR evidence as applicable.
2. Provide a story-level UVT matrix and acceptance results.
3. Identify the ADO pipeline for each work item.
4. Document rollback steps for the table drop and column rename.
5. Confirm the affected producers, consumers, and compatibility window for `trade_version` and `major_version`.
6. Provide the Safe Change Dashboard record supporting the `SAFE` result.
7. Explain why monitoring and operational-documentation updates are marked `NA`.