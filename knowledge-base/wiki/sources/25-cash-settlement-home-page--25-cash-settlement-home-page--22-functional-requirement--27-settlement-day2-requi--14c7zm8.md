---
type: source
title: Cashflow Auto Distribution Design
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page functional requirements"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cashflow-splitting, auto-distribution, nostrо, ratan, razor]
related: [ratan, razor, nostro-static, nostro-threshold-static-data, cashflow-auto-distribution, nostro-threshold-splitting-algorithm, cashflow-auto-split-failure, cashflow-withdrawal-during-split-failure, ratan-fail-and-autofail-status-transitions, cashflow-pre-fail-state-restoration, held-cashflow-reinstatement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Auto Distribution Design.md"]
---
# Cashflow Auto Distribution Design

## Summary

This design describes automatic splitting of a RATAN cashflow when its amount exceeds a configured Nostro threshold. The configuration is maintained in RAZOR and includes a `threshold`, `deductAmount`, and `limitation`. RATAN creates child cashflows using the threshold-based distribution algorithm and retains a residual cashflow when the remaining amount no longer requires splitting.

The document attributes the major splitting algorithm to RAZOR but does not provide a complete executable specification for RATAN. The examples should therefore be treated as illustrative until the iteration, rounding, duplicate handling, and persistence rules are confirmed.

## Threshold configuration

The example configuration is:

```text
threshold = 80,000,000
deductAmount = 200,000
limitation = 60,000,000
```

The basic trigger is:

```text
if cashflow amount > threshold:
    split the cashflow into child cashflows
else:
    do not split further
```

## Described algorithm

The document gives the following formulas:

```text
accDeductAmount = accDeductAmount + deductAmount
xchild = threshold - accDeductAmount
restAmount = restAmount - xchild
```

Additional behavior is described as follows:

- A split child is skipped every ten iterations according to the existing RAZOR behavior.
- If the final child would duplicate an earlier child, the remaining amount is split into a reduced child and a separate `deductAmount`.
- When `xchild` is less than or equal to `limitation`, `deductAmount` is reduced by a factor of ten:

```text
deductAmount = deductAmount / 10
```

- If `deductAmount` becomes less than `1`, the design proposes throwing an exception to prevent infinite splitting.

## Worked examples

### Cashflow amount: 100,000,000

The first child is:

```text
80,000,000 - 200,000 = 79,800,000
```

The residual is:

```text
100,000,000 - 79,800,000 = 20,200,000
```

Because `20,200,000` is below the threshold, it is not split further.

### Cashflow amount: 554,800,000

The described sequence is:

| Child | Amount | Remaining amount |
|---:|---:|---:|
| 1 | 79,800,000 | 475,000,000 |
| 2 | 79,600,000 | 395,400,000 |
| 3 | 79,400,000 | 316,000,000 |
| 4 | 79,200,000 | 236,800,000 |
| 5 | 79,000,000 | 157,800,000 |
| 6 | 78,800,000 | 79,000,000 |

The remaining `79,000,000` is below the threshold but duplicates an earlier child amount. The document describes a further split as:

```text
78,980,000 and 200,000
```

These amounts total `79,180,000`, not `79,000,000`; the example therefore requires reconciliation before it can serve as an acceptance criterion.

### Cashflow amount: 7,389,700,000

The initial sequence is described as:

```text
79,800,000
79,600,000
79,400,000
79,200,000
79,000,000
78,800,000
...
```

The document states that the tenth-child condition would otherwise produce `78,000,000`, but that the RAZOR algorithm skips a split child every ten times and RATAN should retain this behavior.

The source does not define whether a skipped child is omitted, retained as part of the residual, or processed through another branch. It also does not state whether skipped iterations increment `accDeductAmount`.

## Failure handling

The original proposal was:

1. Throw an exception when `deductAmount < 1`.
2. Move the cashflow to `READY+NA+Pending_Exception`.
3. Use the new `AutoSplitFail` action.
4. Require the user to correct the Nostro threshold static configuration.
5. Recover the cashflow through manual fail and reinstate processing.

The design identifies a lifecycle gap: if a withdrawal message arrives while the cashflow is in `READY+NA+Pending_Exception`, RATAN cannot currently move the cashflow from that status and the withdrawal cashflow may be lost.

## Recommended solution

The document recommends reusing the existing `TechFail` action instead of introducing or extending `AutoSplitFail`.

The stated rationale is:

- `AutoSplitFail` would be a new action that is not currently used by other systems.
- Extending `AutoSplitFail` and its result handling could require additional actions and substantial effort.
- `TechFail` is already supported in production and is considered mature.
- Users are familiar with the existing `TechFail` behavior.
- The `TechFail` flow should be enhanced with the required comment and result information.

The exact enhanced status transition, comment text, result schema, withdrawal behavior, and audit fields are not included in the text because they are shown only in a referenced image.

## Evidence and limitations

This is a functional/design description with numerical examples and UI references. It does not include implementation evidence, test results, formal state transitions, acceptance criteria, or a complete algorithm specification.

The distinction between RAZOR and RATAN is important: RAZOR is the source or reference for static data and the major algorithm, while RATAN executes cashflow processing and manages statuses. RAZOR behavior should not automatically be treated as the complete RATAN implementation contract.

See [[cashflow-auto-distribution]] for the business concept, [[nostro-threshold-splitting-algorithm]] for algorithm details, and [[cashflow-auto-split-failure]] for failure and recovery considerations.