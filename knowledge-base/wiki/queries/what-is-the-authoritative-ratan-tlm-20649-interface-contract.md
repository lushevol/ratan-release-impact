---
type: query
title: What Is the Authoritative RATAN-TLM 20649 Interface Contract?
tags: [RATAN, TLM, interface-20649, API-contract, open-question]
related: [ratan-and-tlm-20649--1ovnb8w, ratan-tlm-reconciliation-query, tlm, ratan-interface-inventory, what-is-the-authoritative-ratan-interface-and-go-live-inventory, ratan-accounting-status-lifecycle, how-does-ratan-oltp-handle-eod-nacks]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and TLM 20649.md"]
---

# What Is the Authoritative RATAN-TLM 20649 Interface Contract?

## Question

What is the reviewed and production-authoritative contract for RATAN interface 20649, including its canonical endpoint, parameter encoding, response schema, status semantics, and operational controls?

## Current evidence

The source documents a TLM reconciliation query at:

```text
/api/ratan/v1/accounting/queryReconRecords
```

It identifies the current entity scope as `fmidList = 10036645`, requires GMT conversion for the time parameters, limits the longest query span to three days, and applies this effective predicate:

```text
ratan_accounting_request_task_history.task_status = 'SENT'
```

The documented time predicates are:

```text
ratan_accounting_request_task_history.created_at >= startReleaseTime
ratan_accounting_request_task_history.created_at < endReleaseTime
```

## Open questions

1. Which single URL is the canonical production endpoint?
2. Is `fmidList` a scalar string, a comma-separated list, or a repeated query parameter?
3. Does `task_status = 'SENT'` include ACKed, NACKed, and unanswered records, or are those outcomes represented in separate fields?
4. Which response fields identify ACK, NACK, and no-response states?
5. Do `startReleaseTime` and `endReleaseTime` map directly to `created_at`, or is there a separate release-time field?
6. Is the three-day maximum enforced by validation, and are its boundaries inclusive or exclusive?
7. What are the response schema, pagination rules, HTTP error codes, authentication requirements, and rate limits?
8. Who owns, reviews, and publishes the interface specification?
9. What performance thresholds were validated by the Apache JMeter test that returned 20,286 accounting feeds?

## Related evidence

The reconciliation purpose and accounting outcome requirements should be compared with [[concepts/ratan-accounting-status-lifecycle]] and [[queries/how-does-ratan-oltp-handle-eod-nacks]]. Interface inventory and publication status should be checked against [[concepts/ratan-interface-inventory]] and [[queries/what-is-the-authoritative-ratan-interface-and-go-live-inventory]].

The source has incomplete review metadata and should not yet be treated as a fully authoritative published contract.