---
type: concept
title: Cashflow Technical Failure Recovery
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, technical-failure, recovery, exception-handling, retry]
related: [cashflow-lifecycle-state-machine, cashflow-fail-and-reinstatement, nstp-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning/lifecycle service - state machine.md"]
---
# Cashflow Technical Failure Recovery

The lifecycle design treats `TechFail` as a recoverable technical-processing outcome in most active cashflow states. Rather than immediately terminating the cashflow, the action routes it to a pending exception state.

## Canonical recovery target

The common target is:

```text
QUEUED+Pending Exception+NA
```

The source applies this pattern from projected, queued, ready, netted, split, held, and waiting states.

Examples include:

```text
PROJECTED+NA+NA --TechFail--> QUEUED+Pending Exception+NA
QUEUED+NA+NA --TechFail--> QUEUED+Pending Exception+NA
READY+NA+NA --TechFail--> QUEUED+Pending Exception+NA
NETTED+Settled+NA --TechFail--> QUEUED+Pending Exception+NA
SPLIT+Settled+NA --TechFail--> QUEUED+Pending Exception+NA
```

## Contrast with terminal failure

The separate `Fail` action generally produces:

```text
FAILED+NA+NA
```

This distinction separates technical recovery and operator remediation from an explicit business or processing failure. The source does not define the criteria that determine whether an event is classified as `Fail`, `TechFail`, or `TestFail`.

## Operational consequences

A pending-exception cashflow can be reinstated, amended, withdrawn, netted, split, suppressed, or processed through maker/checker approval. Technical failures therefore re-enter controlled lifecycle processing rather than bypassing operational controls.

The recovery target and action classification should be validated against implementation and UAT evidence before being treated as production behavior.