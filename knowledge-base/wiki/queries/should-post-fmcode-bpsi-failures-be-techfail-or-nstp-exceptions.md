---
type: query
title: Should Post-FMCODE BPSI Failures Be TechFail or NSTP Exceptions?
created: 2026-08-24
updated: 2026-08-24
tags: [bpsi, dqsl, fmcode, techfail, nstp, cash-settlement]
related: [bpsi, dqsl, cash-settlement-dependent-service-failure, cash-settlement-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# Should Post-FMCODE BPSI Failures Be TechFail or NSTP Exceptions?

The source assigns different outcomes to BPSI unavailability based on when FMCODE retrieval fails.

Before FMCODE retrieval, the cashflow is described as technically failed because Razor cannot proceed without booking-entity or counterparty FMCODE. After successful FMCODE retrieval, the source records two NSTP exceptions: `GSAM client Unknown` and `CORP client Unknown`.

A documented comment proposes that the latter outcome should also be a technical failure. The intended classification, recovery path, operational owner, and reporting implications require an explicit decision.