---
type: query
title: What Are the Authoritative FMRP Hold Eligibility Rules?
created: 2026-08-22
updated: 2026-08-22
tags: [fmrp, cashflow, hold, requirements-ambiguity]
related: [cashflow-hold-unhold, ratan-cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
---
# What Are the Authoritative FMRP Hold Eligibility Rules?

The FMRP matrix permits Hold only in `READY` after striking through `QUEUED` and `WAITING`. Historical requirements instead permit Hold after any status except `RELEASED`, `NET`, or `SPLIT`.

Resolve the canonical eligible states, whether `ON HOLD` and `HOLD` are separate UI or persisted values, the required maker/checker transitions, and whether Send To WAITING remains supported.