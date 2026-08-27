---
type: query
title: What Is the Missing CCY Pair Replay Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [query, CCY-Pair, exception-handling, replay, SSI-stamping]
related: [ssi-stamping-service, group-management-service, group-ready-ccy-pair-enrichment, ccy-pair-based-nostro-selection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md"]
---
# What Is the Missing CCY Pair Replay Contract?

The design raises the possibility of a new missing-`CCY Pair` exception so that affected cashflows can be replayed. It does not define whether the exception is required, which service raises it, or how incomplete groups are repaired.

A final contract should define detection, error status, remediation, replay eligibility, idempotency, and behavior when the pair remains unavailable.