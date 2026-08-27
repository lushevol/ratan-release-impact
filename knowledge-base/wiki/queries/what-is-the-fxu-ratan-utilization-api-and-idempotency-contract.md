---
type: query
title: What Is the FXU-RATAN Utilization API and Idempotency Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, api, idempotency, solace]
related: [fxu, ratan, scpay, utilization-request-idempotency, utilization-remaining-amount]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md"]
---
# What Is the FXU-RATAN Utilization API and Idempotency Contract?

The source specifies Solace request/response interaction and calls for request/response enrichment, utilization currency 2, amount, remaining amount, IMS headers, decimal tolerance, and BLADE trade ID.

It does not define message schemas, mandatory fields, utilization-ID semantics, correlation identifiers, idempotency handling, error codes, timeout behaviour, or the precedence of late and duplicate ACK/NACK responses.