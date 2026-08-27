---
type: source
title: Korea Migration Performance Testing Plan
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, korea-migration, performance-testing, murex, swift]
related: [murex, murex-korea, korea-migration-performance-testing, auto-netting-job, swift-message-reconciliation, what-were-the-results-of-the-korea-migration-performance-tests]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Performance Testing Plan.md"]
---
# Korea Migration Performance Testing Plan

## Summary

This document defines a planned validation sequence for the Korea migration test scope in [[entities/murex]]. It uses three Murex Korea end-of-day dumps and applies the same processing workflow to each dump before comparing generated SWIFT messages for a designated payment cohort.

The document records test activities only. It does not provide execution results, performance metrics, defect outcomes, approvals, or evidence of production readiness.

## Planned Test Cycles

| Cycle | Input | Processing sequence | SWIFT comparison scope |
|---|---|---|---|
| 1 | 15-June EOD dump | Push data, perform reconciliation and analysis, process the data, run the auto-netting job, and reprocess `waiting` cashflows | VD17 payments |
| 2 | 16-June EOD dump | Push data, perform reconciliation and analysis, process the data, run the auto-netting job, and reprocess `waiting` cashflows | VD18 payments |
| 3 | 18-June EOD dump | Push data, perform reconciliation and analysis, process the data, run the auto-netting job, and reprocess `waiting` cashflows | VD22 payments |

## Source Plan

The source document states:

1. Prepare three dumps in Murex Korea: the 15-June EOD dump, the 16-June EOD dump, and the 18-June EOD dump.
2. Push the first dump data, perform reconciliation and analysis, process it, run the auto-netting job, reprocess `waiting` cashflows, and compare SWIFT messages for VD17 payments.
3. Push the second dump data, perform reconciliation and analysis, process it, run the auto-netting job, reprocess `waiting` cashflows, and compare SWIFT messages for VD18 payments.
4. Push the third dump data, perform reconciliation and analysis, process it, run the auto-netting job, reprocess `waiting` cashflows, and compare SWIFT messages for VD22 payments.

An image attachment is referenced by the source:

`attachments/image-2026-7-28_0-17-51.png`

No extractable test results or acceptance criteria are available from the supplied content.

## Scope and Limitations

The plan establishes:

- Three dated input snapshots.
- A repeatable processing sequence for each snapshot.
- Explicit handling of cashflows in the `waiting` state.
- SWIFT-message comparison as an output validation step.

The plan does not specify:

- Dump volumes or cashflow populations.
- Reconciliation inputs, tolerances, or pass/fail criteria.
- The meaning or derivation of VD17, VD18, and VD22.
- Auto-netting eligibility rules or exclusions.
- The expected terminal state after `waiting` cashflows are reprocessed.
- The authoritative baseline for SWIFT-message comparison.
- Performance metrics such as latency, throughput, batch duration, concurrency, CPU, memory, or failure-rate thresholds.
- Test execution status, defects, sign-off, or production-readiness approval.

The generic auto-netting step should not be treated as evidence of the lien-aware behavior described in [[concepts/lien-aware-netting-and-auto-unnetting]].

## Evidence Assessment

This is a test-plan source with low-to-moderate evidence strength for intended coverage. It documents what the Korea migration testing is expected to do, not what the system actually achieved. Any conclusions about Murex, settlement processing, SWIFT output, or migration readiness must remain limited to this specific Murex Korea test scope.
