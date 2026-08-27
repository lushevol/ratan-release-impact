---
type: concept
title: Story Status Lifecycle
created: 2026-08-24
updated: 2026-08-24
tags: [ado, workflow, story-management, delivery-lifecycle, cash-settlement]
related: [cash-settlement-squad, development-completion-gate, blocked-story-handling, what-is-the-complete-cash-settlement-story-status-lifecycle, who-owns-each-ado-story-status-transition, what-evidence-is-required-to-exit-in-test]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Squad - Bug handling process.md"]
---
# Story Status Lifecycle

A documented ADO workflow for Cash Settlement stories progresses through:

`Open → Prioritized → In Analysis → Ready for Development → In Development → Dev Done → In Test`

## Entry and planning

- **Open:** The story has been initialized but is not yet prioritized.
- **Prioritized:** The story is ready for planning and must include priority, release date, exit criteria, and a description.

## Analysis and readiness

- **In Analysis:** An engineer has picked up the story. BA work proceeds where there is a BA task; otherwise, developer design work may proceed.
- **Ready for Development:** BA, DEV, and QA analysis is complete, or sufficiently complete to begin development. BA requirements must be clearly briefed to DEV and QA.

This permits a developer-only analysis path, but the process does not define the minimum acceptable scope of partially complete analysis.

## Delivery and testing

- **In Development:** Coding and QA-case development are in progress. Technical design approval is mandatory.
- **Dev Done:** The story has passed the delivery-readiness conditions defined in [[development-completion-gate]].
- **In Test:** QA-case execution is in progress, or QA testing has completed with a release.

The documented lifecycle does not identify a status after `In Test`, nor does it define QA-failure, rework, production-release, or closure transitions. These gaps are tracked in [[what-is-the-complete-cash-settlement-story-status-lifecycle]] and [[what-evidence-is-required-to-exit-in-test]].

## Related subtasks

The source associates analysis tasks with `In Analysis`; analysis, development, and QA-case-development tasks with `Ready for Development`; development and QA-case-development tasks with `In Development`; and QA-verification tasks with `Dev Done` and `In Test`.

`On Hold` is an exception path described in [[blocked-story-handling]].