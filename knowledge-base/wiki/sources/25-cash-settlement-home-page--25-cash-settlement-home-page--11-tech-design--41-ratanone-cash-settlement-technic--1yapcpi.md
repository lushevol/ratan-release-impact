---
type: source
title: Cash Settlement Squad Bug Handling Process
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, uber-integration, bug-handling, ado, workflow]
related: [cash-settlement-squad, story-status-lifecycle, development-completion-gate, blocked-story-handling, what-is-the-complete-cash-settlement-story-status-lifecycle, who-owns-each-ado-story-status-transition, what-evidence-is-required-to-exit-in-test, how-does-an-on-hold-story-return-to-active-work, does-the-bug-process-use-severity-and-priority-fields]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Squad - Bug handling process.md"]
authors: []
year: 2026
url: ""
venue: Internal process reference
---
# Cash Settlement Squad Bug Handling Process

An undated internal reference defining an ADO story-status workflow for the RATAN - Uber Integration workstream within RATANONE Cash Settlement.

The document describes intended process gates and required evidence. It does not establish that the workflow is enforced in ADO or consistently followed in practice. It also stops at `In Test` and does not define a final completion, closure, release, QA-failure, or rework state.

## Source content

```markdown
# Story Status Descirption

| ADO Status | Description | Story Mandatory Value | Related Sub Task |
| --- | --- | --- | --- |
| Open | Story initialized and yet prioritize | | |
| Prioritized | Story prioritized and ready for planning | 1. Priority 2. Release date 3. Exit criteria 4. Description | |
| In Analysis | Picked by engineer, if there is BA task then BA work in progress, if only developer task, then developer design in progress | | Yes Analysis task |
| Ready for Development | BA/DEV/QA analysis task done, or analysis partial complete and able to start development | 1. BA requirement clearly brief to DEV and QA | Yes Analysis task Development task QA case development task |
| On Hold | Critical issue / blockers result in the story can't be | 1. Blocker/issue commented attach evidence | Yes Analysis task - On Hold Development task- On Hold QA case development task - On Hold |
| In Development | Dev coding in progress QA case development in progress | 1. Technical design approved | Yes Development task QA case development task |
| Dev Done | Coding done UT done PR merge to target develop/release branch CI pass CD done to the target environment Sanity check done and ready for QA start QA case development done | 1. UT/dev testing evidence. 2. QA case get reviewed | Yes QA verification task |
| In Test | QA case execution in progress | 1. QA testing in progress 2. QA testing done with a release | Yes QA verification task |
```

## Recorded workflow

The documented primary sequence is:

`Open → Prioritized → In Analysis → Ready for Development → In Development → Dev Done → In Test`

`On Hold` is an exception status for stories blocked by a critical issue. A blocker comment and supporting evidence are required.

The process links cross-functional work among BA, DEV, and QA through analysis, development, QA-case-development, and QA-verification subtasks. It permits developer-led design analysis when no BA task exists.

## Limitations to resolve

- `In Test` is not followed by a documented final status.
- The meaning of permitted “partial” analysis at `Ready for Development` is unspecified.
- Approvers and owners of each transition are not identified.
- No return-to-work criteria are given for `On Hold`.
- Despite the document title, no bug-specific severity, reproduction, impact, environment, workaround, or regression fields are defined.

See [[story-status-lifecycle]], [[development-completion-gate]], and [[blocked-story-handling]]. The source concerns delivery workflow and does not validate the runtime behavior described in [[tdsx-uber-message-listener]] or [[uber-inbound-message-idempotency-and-error-state]].