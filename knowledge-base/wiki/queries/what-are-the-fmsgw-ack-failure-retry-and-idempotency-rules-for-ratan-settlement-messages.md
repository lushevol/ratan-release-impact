---
type: query
title: What Are the FMSGW ACK Failure, Retry, and Idempotency Rules for RATAN Settlement Messages?
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, ratan, acknowledgement, retry, idempotency, resilience]
related: [ratan, fmsgw, amh, ratan-fmsgw-amh-settlement-message-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/002 QATAR SCB DOHA DOH(GBS).md"]
---
# What Are the FMSGW ACK Failure, Retry, and Idempotency Rules for RATAN Settlement Messages?

The Qatar SCB Doha UAT records successful forwarding and ACK return only. It does not describe resilience or failure semantics for the [[ratan]]–[[fmsgw]]–[[amh]] integration.

## Questions to resolve

- How are messages correlated across RATAN, FMSGW, and AMH?
- Which ACK states are returned to RATAN, and at what delivery stage?
- What happens when AMH is unavailable, times out, or returns an error?
- Which party retries, using what schedule and maximum attempts?
- How are duplicate submissions and duplicate ACKs detected and handled?
- How are partial outcomes reconciled after service restart or recovery?

The source's Duplicate Message Queue scenario confirms a manual route for duplicate payment messages, but does not establish end-to-end idempotency behavior.