---
type: source
title: Cashflow Splitting UAT
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, cashflow-splitting, uat, settlement-day-2, ratan, integration-testing]
related: [cashflow-splitting, cashflow-unsplit, split-amount-amendment, split-child-threshold-redistribution, nostro-threshold-matching-precedence, split-cashflow-downstream-integration, ratan-cashflow-lifecycle-state-machine, netting-resultant-cashflow, clearing-swift-suppression, nds-auto-netting, cashflow-logical-model, murex-2-11, tds3, lms, stella, ssdr, dqsl]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md"]
authors: []
year: 2025
url: ""
venue: "Settlement Day 2 UAT record"
---

# Cashflow Splitting UAT

## Scope

This UAT record covers Settlement Day 2 cashflow splitting in Ratan, including manual splitting, unsplitting, split amendment, nostro-threshold distribution, withdrawal handling, suppression, querying by splitting ID, and downstream integration.

The tested landscape includes Ratan, Murex, Stella, TDS3, LMS, SSDR, DQSL, FMMIS, TLM, GoAML, CIS, FMMIS, BCS, LOANIQ, Blade, SWIFT, and accounting processes.

## Core outcomes

```text
Manual gross split:
Parent: WAITING or READY -> SPLIT
Children: generated with the same splitting ID -> releasable
Release output: SWIFT generated; accounting sent successfully

Unsplit before child release:
Parent: SPLIT -> WAITING with unsplit exception
Children: -> DEAD

Unsplit after child release:
Operation rejected
Error: not eligible for unsplit

Split-child over nostro threshold:
Parent: remains SPLIT
Original child: -> DEAD
Replacement child: generated and linked to parent
Replacement output: SWIFT/accounting generated

Withdrawal after split:
Withdrawal parent: -> SPLIT
Withdrawal children for non-released original children: -> CANCELLED
Withdrawal child for released original child: -> WAITING
Release output: reversal accounting and cancel SWIFT generated

Undo after withdrawal:
New event: -> ERROR
```

## Manual split behavior

Manual splitting is supported for eligible gross cashflows from Murex and Stella when the cashflow is in `WAITING` or `READY`.

A successful split moves the parent to `SPLIT`, generates child cashflows with the same splitting ID, and exposes the children from the parent cashflow details. Releasing the children generates SWIFT and sends accounting successfully.

The UAT explicitly excludes the following from manual splitting:

- BCS and LOANIQ cashflows.
- IRS aggregation resultant cashflows.
- Netting resultant cashflows.
- Split-child cashflows.

Split children also cannot be manually netted.

## Lifecycle and controls

Split children bypass manual and automatic netting rules, IRS check conditions, and NDS auto-netting rules. They are placed into the appropriate pending or exception path and may subsequently be released.

Suppression has two distinct outcomes:

| Action | Child status | SWIFT | Accounting |
| --- | --- | --- | --- |
| SWIFT suppression | `SWIFT_SUPPRESSED` | Suppressed | Generated |
| Cashflow suppression | `CASHFLOW_SUPPRESSED` | Not generated | Not generated |

A splitting ID query returns the parent and all associated child cashflows.

## Withdrawal behavior

When a withdrawal is received for a split parent, the withdrawal parent moves to `SPLIT`. Withdrawal children corresponding to unreleased original children move to `CANCELLED`. The withdrawal child corresponding to an original child that was released remains in `WAITING` and requires user action. Releasing that withdrawal child generates reversal accounting and cancel-SWIFT output.

If a new event is received after the withdrawal lifecycle has started, the new event moves to `ERROR`.

## Nostro-threshold distribution

The UAT covers automatic distribution at three levels:

1. A gross cashflow exceeding the nostro threshold.
2. A netting resultant exceeding the nostro threshold.
3. A split child exceeding the nostro threshold.

For gross and netting-resultant cases, the parent moves to `SPLIT`, children are generated, and released children produce SWIFT and accounting. For a split child that exceeds the threshold, the parent remains `SPLIT`, the original child moves to `DEAD`, and a replacement child is generated and linked to the parent.

The tested static-data setup included three records for the same currency:

```text
1. Currency only
2. Booking entity + currency
3. Nostro BIC + currency
```

The observed result was that the booking-entity-plus-currency record controlled distribution. The complete precedence between booking entity, nostro BIC, and currency-only records remains unspecified.

## Downstream UAT status

| Area | Source status | Important qualification |
| --- | --- | --- |
| Settlement | Done | 25 cases marked Pass |
| Blade | No populated result | Section exists without executed cases |
| Stella | Incomplete | Scenario documented; no tester or explicit result |
| Murex | Done heading | Rows lack explicit Pass/Fail values |
| LMS | Done | Rows marked Pass despite missing or duplicate message evidence |
| SSDR | Done / EOD In Process | Extract validation remains open |
| DQSL | Done | No explicit Pass/Fail value |
| CIS | Descoped | No testing expected in this scope |
| FMMIS | Done | Logic updated and tested with PO |
| TLM | Open | Test data shared; confirmation pending |
| GoAML | In Process | Depends on EOD report generation |
| Static Data OPS | Done | CRUD result cells are blank |

## Integration findings

Murex evidence indicates that Ratan sends released status messages to Murex and that Murex receives status updates for gross splits, withdrawals, and net-resultant split children. The Murex result fields are not explicitly populated.

The Stella scenario records the TDS3 sequence:

```text
PROJECTED -> SPLIT -> PROJECTED -> RELEASED
```

The scenario lacks a tester and explicit pass/fail result.

LMS evidence is contradictory. Cases are marked `Pass`, while the evidence reports missing parent or resultant messages, missing suppressed-child messages, and a released child received twice. Child messages were received in several cases. These results require reconciliation before LMS sign-off.

SSDR extract validation is still in process. DQSL is described as able to query and return split information, but no explicit result is recorded. TLM confirmation is pending, and GoAML depends on EOD report generation.

## Evidence assessment

The strongest evidence is the set of Settlement cases explicitly marked `Pass`, covering positive and negative eligibility paths, lifecycle transitions, threshold handling, withdrawal behavior, and suppression.

Evidence for Murex, Stella, DQSL, and Static Data OPS is incomplete because result metadata is missing. “Done” headings should not be interpreted as proof that every downstream acceptance criterion passed.

## Related knowledge

The UAT extends [[concepts/ratan-cashflow-lifecycle-state-machine]], [[concepts/netting-resultant-cashflow]], [[concepts/clearing-swift-suppression]], [[concepts/nds-auto-netting]], and [[concepts/cashflow-logical-model]]. The new functional concepts are documented in [[concepts/cashflow-splitting]], [[concepts/cashflow-unsplit]], [[concepts/split-amount-amendment]], and [[concepts/split-child-threshold-redistribution]].