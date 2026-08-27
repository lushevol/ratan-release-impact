---
type: concept
title: Threshold-Based Cashflow Auto Distribution
tags: [cashflow, settlement, automation, nostro, threshold]
related: [nostro-threshold-static, release-cutoff-risk-for-unhold, manual-cashflow-splitting, ratan, authoritative-split-cashflow-lifecycle]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Split Demo Cases.md"]
---
# Threshold-Based Cashflow Auto Distribution

Threshold-based cashflow auto distribution is an automated process for cashflows exceeding the maximum amount a nostro agent can process.

## Trigger and outcome

At release cut-off time, the system must:

1. Detect that a cashflow exceeds the applicable nostro threshold.
2. Split the cashflow into lower-value child cashflows.
3. Directly generate SWIFT and accounting outputs for each child to downstream systems.

This has a distinct operational trigger and purpose from [[manual-cashflow-splitting]]. It should not be assumed that automatic and manual splits share the same parent status, `Splitting Id`, exceptions, amendment capability, or un-split behavior.

## Configuration dependency

Thresholds are managed through [[nostro-threshold-static]], scoped by mandatory currency and optional booking entity and nostro-agent BIC.

## Unspecified contract

The requirement does not define:

- Threshold matching precedence or fallback behavior.
- Child amount distribution and rounding-residual rules.
- Child statuses and exception states.
- Idempotency at release cut-off.
- Atomicity and recovery when SWIFT or accounting generation fails.
- The lifecycle of withdrawal events after automated distribution.