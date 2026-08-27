---
type: concept
title: Development Completion Gate
created: 2026-08-24
updated: 2026-08-24
tags: [definition-of-done, ci-cd, unit-testing, qa, release-readiness]
related: [story-status-lifecycle, cash-settlement-squad, what-evidence-is-required-to-exit-in-test, who-owns-each-ado-story-status-transition]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Squad - Bug handling process.md"]
---
# Development Completion Gate

The documented `Dev Done` gate is the handoff point from implementation to QA verification in the Cash Settlement story workflow.

## Required completion conditions

A story at `Dev Done` is described as having:

- Coding completed.
- Unit testing completed.
- A pull request merged to the target develop or release branch.
- CI passed.
- CD completed to the target environment.
- A sanity check completed.
- QA ready to start.
- QA-case development completed.

## Mandatory evidence

The story must contain:

1. Unit-test or development-testing evidence.
2. Evidence that the QA case has been reviewed.

The source does not prescribe evidence format, storage location, responsible approver, required environment, or acceptance threshold. It therefore describes an intended gate rather than an auditable enforcement mechanism.

## Relationship to the workflow

Technical design must be approved before work enters `In Development`. Completion of this gate enables the QA-verification task and transition to `In Test` within [[story-status-lifecycle]].

The test-exit requirements remain unresolved in [[what-evidence-is-required-to-exit-in-test]].