---
type: query
title: What Is the Authoritative FMRP Retry Limit and Counter?
created: 2026-08-24
updated: 2026-08-24
tags: [FMRP, retry, workflow, configuration]
related: [fmrp, fmrp-cashflow-publication-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change.md"]
---
# What Is the Authoritative FMRP Retry Limit and Counter?

The source contains conflicting retry controls:

- `payInsertionFilter` retries when `STPDOC_DATA_TYPE2` is empty or below `3.0`.
- `retryCheck` retries when `STPDOC_DATA_TYPE3` is empty or below `5.0`.
- `FmrpRetryCheck` is described as having a maximum retry count of three.
- Initial insertion and later retry processing use different document fields.

The authoritative counter field, retry ceiling, and relationship between `retry1` and `retry2` need confirmation before operational behavior can be relied upon.