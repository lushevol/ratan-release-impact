---
type: source
title: "Bulk Manual STP for Group Blotter"
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, group-blotter, bulk-manual-stp, functional-requirement, acceptance-testing]
related: [group-blotter, bulk-manual-stp-group-blotter, trade-major-version-manual-stp-ordering, group-blotter-cashflow-state-lifecycle, allocation-cashflow-state-handling, cashflow-migration-readiness, murex-reversal-and-new-cashflow-matching, cashflow-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter.md"]
---
# Bulk Manual STP for Group Blotter

## Summary

This functional requirement defines bulk manual straight-through processing (STP) for cashflows selected from the Group Blotter. Single-group requests retain the original manual-STP logic. Multi-group requests are grouped by trade, prechecked at trade level, ordered by major version, and then executed through the original group-message logic.

The source describes intended behavior for [[concepts/bulk-manual-stp-group-blotter]], including partial cashflow processing, dependencies between major versions, `is_trade_validated` handling, multi-thread execution, error feedback to the frontend, Cashflow Blotter routing, and the `ManualDeliver` audit event.

## Functional Logic

```text
1. For single group message, follow the original logic. Only a group message with status PENDING or ERROR and no pending work for a previous major version can be manually STP'd.

2. For multiple group messages, group them by trade and execute using multiple threads.

3. For each trade, precheck the entire trade:
   3.1 Pass: order by major version, filter group status = DATA_VALIDATION_FAILED/PENDING_PRE_GROUP, and execute each group message using the original logic.
   3.2 Failed: provide the error message to the frontend.
```

The source therefore places the trade, rather than the selected row alone, at the principal validation boundary. Later major versions are not expected to bypass unresolved pending work in an earlier major version.

## State and Routing Outcomes

The expected successful outcomes include:

- Selected cashflow messages change from `PENDING` to `END`.
- A successfully completed group changes to `COMPLETED`.
- Applicable cashflows are routed to the Cashflow Blotter.
- `bookingSystemEvent` is set to `ManualDeliver`.
- A withdrawal cashflow may change to `OFFSET` while its group becomes `COMPLETED`.

The scenarios also show that selected cashflows may be processed while other cashflows in the same group remain pending or in error. The exact rule for when a group is marked `COMPLETED` is not consistent across all examples; see [[queries/is-group-completed-when-unselected-cashflows-remain-pending]].

## Multi-Group Scenarios

The following structured cases are preserved from the source. `trade_group_majorVersion` identifies the trade, group, and major-version sequence.

| Case | Trade and group state | UI selection | Expected result |
|---|---|---|---|
| 1 | `T1_G1_V1`: `PENDING_TRADE_VALIDATION`; `C1:C294` are `PENDING` | Select `C1:C291` in `T1_G1_V1` | Selected messages become `END`; the source retains the group as `PENDING_TRADE_VALIDATION` |
| 1.2 | `T1_G1_V1`: `PENDING_TRADE_VALIDATION`; `c1:PENDING`, `c2:END`, `c3:ERROR`. `T1_G1_V2`: `PENDING_PRE_GROUP`; `c1:PENDING`, `c2:END`, `c3:PENDING` | Select `T1_G1_V1` cashflows and `T1_G1_V2:c1` | `T1_G1_V1` becomes `COMPLETED`; `c1` remains `PENDING` and `c3` remains `ERROR`; `T1_G1_V2` remains `PENDING_PRE_GROUP` |
| 1.3 | `T1_G1_V1`: `PENDING_TRADE_VALIDATION`; `c1,c2:PENDING`. `T1_G1_V2`: `PENDING_PRE_GROUP`; `c1,c2:PENDING` | Select all listed cashflows | Both groups become `COMPLETED` and selected cashflows become `END`. The source's expected result refers to `c3:END` although the selection lists `c2`; this is treated as a source inconsistency |
| 2.1 | `T1_G1_V1`: `PENDING_TRADE_VALIDATION`; `C1:C291:END`, `C292:C294:PENDING`. `T1_G2_V2` and `T1_G3_V3`: `PENDING_TRADE_VALIDATION` with one pending cashflow each | Select only `T1_G2_V2:C1` | `N/A`; the unresolved earlier version blocks the later version |
| 2.2 | Same state as case 2.1 | Select `T1_G2_V2:C1` and `T1_G3_V3:C1` | `N/A`; both later versions remain blocked |
| 2.3 | Same state as case 2.1 | Select only `T1_G3_V3:C1` | `N/A`; selecting the latest version does not bypass earlier pending work |
| 3.1 | `T1_G1_V1`: `C1:C291:END`, `C292:C294:PENDING`; later groups each contain pending cashflows | Select `T1_G1_V1:C292` and pending cashflows in later groups | `T1_G1_V1:C292` becomes `END`; later groups are not completed |
| 3.2 | `T1_G1_V1`: `C1:C292:END`, `C293:C294:PENDING`; later groups contain pending cashflows | Select `T1_G1_V1:C293` and `T1_G2_V2:C1` | `T1_G1_V1:C293` becomes `END`; the later group is not completed |
| 3.3 | `T1_G1_V1`: `C1:C293:END`, `C294:PENDING`; later groups contain pending cashflows | Select `T1_G1_V1:C294` and `T1_G3_V3:C1` | `T1_G1_V1` becomes `COMPLETED` and `C294` becomes `END`; the later group is not completed |
| 4.1 | `T1_G2_V2`: `PENDING_TRADE_VALIDATION`; `C1:PENDING`. `T1_G3_V3`: `PENDING_TRADE_VALIDATION`, `is_trade_validated=false`; `C1:PENDING` | Select `T1_G2_V2:C1` | `T1_G2_V2` becomes `COMPLETED`; `C1` becomes `END` |
| 4.2 | Same as case 4.1, but `T1_G3_V3.is_trade_validated=true` | Select `T1_G2_V2:C1` | Both groups' selected cashflows become `END`; both groups are eligible to complete |
| 4.3 | `T1_G2_V2`: `PENDING_TRADE_VALIDATION`; `C1:PENDING`. `T1_G3_V3`: `PENDING_PRE_GROUP`, `is_trade_validated=true`; `C1:PENDING` | Select `T1_G2_V2:C1` | Both groups become `COMPLETED` and their cashflows become `END` |
| 5.1 | `T1_G1_V1`: `PENDING_TRADE_VALIDATION`; `C11:PENDING`. `T2_G1_V1`: `PENDING_PRE_GROUP`; `C21:PENDING` | Select both cashflows | Both groups become `COMPLETED`; `C11` and `C21` become `END` |

## Acceptance Criteria

| AC-No | Function | Scenario | Expected result | Test evidence |
|---|---|---|---|---|
| 1 | Bulk manual deliver — partial STP cashflows in one group with the same trade | Book `C1,C2` in the same major version with count 3; Operations bulk-manually delivers the two cashflows | Initially `C1,C2:PENDING` and `G1:PENDING`. After delivery, `C1,C2:END`, `G1:COMPLETED`, `bookingSystemEvent='ManualDeliver'`, and the cashflows flow to the Cashflow Blotter | — |
| 2 | Bulk manual deliver — all STP cashflows in one group with the same trade | Book `C1,C2` in the same major version with count 2 and trade state `Booked`; Operations bulk-manually delivers them | Initially `C1,C2:PENDING` and `G1:PENDING_TRADE_VALIDATION`. After delivery, both messages are `END`, `G1:COMPLETED`, `bookingSystemEvent='ManualDeliver'`, and both cashflows flow to the Cashflow Blotter | `uat6 tradeId: 4364000000` |
| 3 | Bulk manual deliver — STP cashflows in two groups with the same trade | Book `C1` in major version 1 and `C3` in major version 2; Operations bulk-manually delivers both | Initially both messages and groups are `PENDING`. After delivery, `C1,C3:END` and both groups are `COMPLETED` | — |
| 4 | Bulk manual deliver — STP cashflows in two groups with the same trade | Book `C1,C2` in major version 1 and `C3` in major version 2; Operations bulk-manually delivers all three | After delivery, `C1,C2,C3:END`, both groups are `COMPLETED`, `bookingSystemEvent='ManualDeliver'`, and all three cashflows flow to the Cashflow Blotter | — |
| 5 | Bulk manual deliver — STP cashflows in two groups with the same trade | Book `C1,C2` in major version 1 and `C3,C4` in major version 2; Operations bulk-manually delivers three cashflows | Initially `G1:PENDING_TRADE_VALIDATION` and `G2:PENDING_PRE_GROUP`. After delivery, all four messages are `END`, both groups are `COMPLETED`, `bookingSystemEvent='ManualDeliver'`, and all four cashflows flow to the Cashflow Blotter | — |
| 6 | Bulk manual deliver — STP cashflows in three groups with the same trade | Book `C1(New),C2` in major version 1, `C1(Withdrawal)` in major version 2, and `C3,C4` in major version 3; Operations bulk-manually delivers `C2,C3` | The withdrawal becomes `OFFSET` and its group becomes `COMPLETED`. After delivery, `C2,C3,C4:END`, `G1:COMPLETED`, `G3:PENDING_TRADE_VALIDATION`, `bookingSystemEvent='ManualDeliver'`, and `C2,C3,C4` flow to the Cashflow Blotter | — |

## Limitations and Ambiguities

The source is an acceptance-style functional requirement rather than an implementation specification. It does not establish:

- Whether processing is atomic per trade, group, or cashflow.
- Whether a failed precheck blocks unrelated trades in the same bulk request.
- Whether multi-thread execution preserves completion order or only eligibility order.
- Whether `ERROR` is retryable under exactly the same conditions as `PENDING`.
- Whether `DATA_VALIDATION_FAILED` is a valid executable state or a transcription error.
- The precise precedence between group status and `is_trade_validated`.
- Whether `ManualDeliver` is recorded per cashflow, group, or bulk operation.

The source also contains duplicated or inconsistent case numbering, a mismatch between the selected and expected cashflow in case 1.3, and a discrepancy between the logic-table case 5.1 and acceptance-criteria case 5. These should be resolved before the requirement is used as an authoritative implementation contract.

## Related Operational Context

The requirement is likely relevant to [[entities/ratan]], [[projects/cashflow-migration]], and [[stakeholders/settlement-ops]], but the source does not explicitly identify its implementation platform or project scope. Its state behavior should be reconciled with [[concepts/allocation-cashflow-state-handling]], [[concepts/cashflow-migration-readiness]], and [[concepts/murex-reversal-and-new-cashflow-matching]].