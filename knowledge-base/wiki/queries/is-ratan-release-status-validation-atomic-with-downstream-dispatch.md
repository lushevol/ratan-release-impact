---
type: query
title: Is RATAN Release Status Validation Atomic With Downstream Dispatch?
created: 2026-08-24
updated: 2026-08-24
tags: [RATAN, concurrency, downstream-dispatch, duplicate-payment]
related: [ratan, cashflow-release-and-netting-race-condition, release-time-cashflow-status-gating, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--11-2026-design--40-ops-allowed-actio--pckrjd]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/OPS Allowed Actions Post Pending Release.md"]
---
# Is RATAN Release Status Validation Atomic With Downstream Dispatch?

## Question

Does RATAN make release eligibility validation, cashflow locking or version checking, outgoing-instruction creation, and downstream dispatch one atomic or serialized operation?

## Why it matters

The source states that only `READY` payments may be sent downstream, but reports a case where automatic release and ad-hoc netting overlapped on the same `READY` gross cashflow. A non-atomic status check could still permit dispatch based on a stale eligibility read.

## Evidence needed

- Release-job component ownership and transaction boundaries.
- Locking, optimistic-versioning, or compare-and-set behavior for `READY` transitions.
- Concurrent-action integration tests for release versus netting and splitting.
- Audit records correlating eligibility checks, status changes, instruction creation, and downstream acknowledgement.

Primary evidence is [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--11-2026-design--40-ops-allowed-actio--pckrjd]].