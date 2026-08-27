---
type: query
title: What Evidence Is Required to Exit In Test?
created: 2026-08-24
updated: 2026-08-24
tags: [qa, test-evidence, release-readiness, ado, open-question]
related: [story-status-lifecycle, development-completion-gate, cash-settlement-squad]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Squad - Bug handling process.md"]
---
# What Evidence Is Required to Exit In Test?

The source says that `In Test` covers QA execution in progress and QA testing completed with a release, but it does not define an exit status or a test-completion evidence standard.

## Evidence needed

- QA acceptance criteria and expected execution records.
- Defect triage and rework rules for failed QA cases.
- Required release approval and deployment artifacts.
- ADO field configuration, attachment conventions, and closure rules.

The preceding implementation evidence is documented in [[development-completion-gate]]. The incomplete workflow boundary is documented in [[story-status-lifecycle]].