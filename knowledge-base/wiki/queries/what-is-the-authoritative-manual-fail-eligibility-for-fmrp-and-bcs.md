---
type: query
title: What Is the Authoritative Manual Fail Eligibility for FMRP and BCS?
created: 2026-08-22
updated: 2026-08-22
tags: [manual-fail, fmrp, bcs, cashflow, requirements-ambiguity]
related: [cashflow-failure-and-reinstatement, bcs, ratan-cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
---
# What Is the Authoritative Manual Fail Eligibility for FMRP and BCS?

FMRP lists Manual Fail for `QUEUED`, `WAITING`, and `READY`, with a likely continuation for `SWIFT_SUPPRESSED` and `CASHFLOW_SUPPRESSED` after payment date. BCS lists Manual Fail for `FAILED|QUEUED`, despite the action name.

Determine whether BCS describes a distinct failed-cashflow workflow, contains a state-selection defect, or has a different meaning for Manual Fail.