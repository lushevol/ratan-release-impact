---
type: query
title: What Is the Authoritative NSTP Rule and Exception State Machine?
created: 2026-08-24
updated: 2026-08-24
tags: [nstp, rule-management, exception-management, state-machine, open-question]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--35-ratan-rule-service-technical-desi--j5csbt, nstp-exception-operation-levels, nstp-exception-metadata, rule-maintenance-and-validation-pipeline]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design.md"]
---
# What Is the Authoritative NSTP Rule and Exception State Machine?

The design explicitly identifies selected exception statuses and successful closure paths, but its NSTP Rule and NSTP Exception state-machine sections contain no extractable state definition.

## Known exception transitions

- Maker-only exceptions: `PENDING_OPERATOR` to `CLOSED` after successful maker submission.
- Checker-only exceptions: `PENDING_VERIFICATION` to `CLOSED` after successful checker approval.
- Maker-checker exceptions: `PENDING_OPERATOR` to `PENDING_VERIFICATION` after maker fix, then to `CLOSED` after checker approval.

## Questions to resolve

- What are the rule lifecycle states for draft, maker submission, checker approval, rejection, activation, deletion request, and deletion approval?
- What transitions support exception rejection, rework, cancellation, expiry, and failed verification?
- Which actor may perform each transition?
- What controls concurrent edits and duplicate actions?
- How are existing exceptions handled after their generating rule is deleted or disabled?