---
type: query
title: Has LMS Confirmed All-Entity RATAN Feed Compatibility?
tags: [lms, ratan, cashflow-feed, integration, readiness, reconciliation]
related: [ratan, lms, ratan-lms-entity-filter-removal, manual-entity-lms-reference-data-feed, what-is-the-manual-entity-lms-feed-contract-and-reconciliation-evidence]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/LMS - Remove the entity filter in LMS feed.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Has LMS Confirmed All-Entity RATAN Feed Compatibility?

The requirement directs [[ratan]] to send all entity cashflow messages to [[lms]], but the source explicitly records that LMS-side impact and correct consumption still require confirmation.

## Evidence needed

- LMS confirmation that all RATAN entity records, including previously excluded entities, are accepted.
- An approved specification for any LMS prefixing rule, including the proposed `DV`, `LQ`, and `MX` values.
- Expected treatment for unknown entities, invalid records, and rejected messages.
- Volume and performance assessment for the increased feed population.
- Retry, idempotency, reconciliation, and operational-monitoring evidence.
- End-to-end test results proving that the unchanged SCBML `CashflowData` contract is accepted for the broadened entity population.

Until this evidence is obtained, the all-entity feed is a stated requirement rather than a confirmed integration outcome.