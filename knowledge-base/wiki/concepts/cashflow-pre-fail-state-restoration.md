---
type: concept
title: Cashflow Pre-Fail State Restoration
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, manual-fail, state-management, rejection, audit]
related: [bulk-cashflow-manual-fail, cashflow-manual-fail-maker-checker, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail.md"]
---
# Cashflow Pre-Fail State Restoration

## Definition

Cashflow Pre-Fail State Restoration is the requirement that rejecting a manual-fail request returns each cashflow to the state and sub-state it had before the maker submitted manual fail.

## State capture

Before submission, an eligible cashflow may be in `QUEUED`, `WAITING`, `READY`, `SWIFT_SUPPRESSED`, or `CASHFLOW_SUPPRESSED`, subject to the detailed eligibility rule for suppressed states.

After maker submission, the cashflow is normalized to:

```text
WAITING / Pending Manual Fail / Pending Verification
```

The workflow must retain the original state, sub-state type, and sub-state independently for each cashflow. This is especially important when a bulk selection contains cashflows from different states.

## Example

For a cashflow originally in `READY`:

```text
Before manual fail:
Cashflow State = "READY"
Cashflow Sub State Type = "NA"
Cashflow Sub State = "NA"

After maker submission:
Cashflow State = "WAITING"
Cashflow Sub State Type = "Pending Manual Fail"
Cashflow Sub State = "Pending Verification"

After checker rejection:
Cashflow State = "READY"
Cashflow Sub State Type = "NA"
Cashflow Sub State = "NA"
```

For a `WAITING` cashflow that had reached `Pending Exception / Pending Operator`, approval leads to `FAILED / NA / NA`; reinstatement subsequently returns it to the main flow and may restore the pending-exception path shown in the acceptance case.

## Open implementation issue

The source requires restoration but does not define the persistence mechanism, concurrency behavior, or treatment of a cashflow whose underlying state changes while approval is pending. These issues should be resolved alongside the bulk atomicity and stale-status contract.
