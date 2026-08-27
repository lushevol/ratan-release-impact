---
type: concept
title: Blocked Story Handling
created: 2026-08-24
updated: 2026-08-24
tags: [blockers, on-hold, workflow, evidence, issue-management]
related: [story-status-lifecycle, cash-settlement-squad, how-does-an-on-hold-story-return-to-active-work]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Squad - Bug handling process.md"]
---
# Blocked Story Handling

`On Hold` is the documented exception status for a Cash Settlement story that cannot progress because of a critical issue or blocker.

## Required documentation

When placing a story on hold, the process requires:

1. A comment identifying the blocker or issue.
2. Attached supporting evidence.

The source also indicates that related analysis, development, and QA-case-development subtasks may independently be put on hold.

## Undocumented resumption process

The reference does not state who may remove the hold, what evidence demonstrates resolution, which prior status should be restored, or whether blocked-work age and escalation must be tracked. These omissions are tracked in [[how-does-an-on-hold-story-return-to-active-work]].

This workflow concept concerns work-management status; it does not describe runtime retry, DLT, or recovery behavior for the Uber integration.