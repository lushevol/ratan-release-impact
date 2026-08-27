---
type: source
title: UAT Test Cases — Murex 2.11 Booking
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [uat, murex-211, ratan, cashflow, trade-validation, settlement]
related: [murex-211, ratan, tds3, trade-validation-cashflow-gating, fmrp-cashflow-status-synchronization, non-economic-cashflow-amendment-handling, what-is-the-v1-v2-cashflow-stp-blocking-rule, why-did-tds3-vald-messages-not-reach-ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/UAT test cases - Murex 2.11 booking.md"]
---
# UAT Test Cases — Murex 2.11 Booking

## Scope

This source records UAT scenarios for [[entities/murex-211]] trade booking, trade-status validation, modification, rejection, cancellation, C&R, market-event removal, fixing cashflows, typology changes, non-economic amendments, and cashflow publication into [[entities/ratan]].

The opening requirement—“Control to prevent STP of v1 cashflow if v2 cashflows are in Group Blotter”—is marked “To Be Enriched.” The document does not define or conclusively test this control.

## Core UAT Behavior

A payment generated while a trade is in `TRAD` is expected to enter RATAN’s Group Blotter with status `Pending Validation`. After RATAN receives the applicable validated trade status, normally `VALD`, the relevant current cashflow is expected to move automatically to the Cashflow Blotter.

Ordinary modification, rejection-and-rework, cancellation, C&R, market-event removal, typology update, and fixing scenarios generally passed. The observed behavior is conditional on successful end-to-end propagation of trade status from Murex through [[entities/tds3]] to RATAN.

## Scenario Results

| Scenario | Test path | Trade or payment identifiers | Recorded result |
|---:|---|---|---|
| 1 | `TRAD`, then `PEND/CHCK/VALD` | `96120339-107761880` | `PASS`; `p1(T1)` moved from `Pending Validation` to the Cashflow Blotter |
| 2 | Direct `VALD` booking | `96120353--107761895` | `PASS`; `p1(T1)` was auto-pushed |
| 3 | `TRAD`, then direct `COMP` | `96120340-107761881` | Initial pending check `PASS`; final release result was not recorded |
| 4 | `TRAD`, FO modification, then validation | `96120355-107761899` | Initially failed, then marked `Retest PASS`; `VALD` was not initially flown from TDS3 to RATAN |
| 5 | `TRAD`, reject to `TQRY`, modify, then validate | `96120354-107761898` | `PASS`; replacement `p3` was auto-pushed |
| 6 | `TRAD`, `TQRY`, C&R `T1→T2`, validate `T2` | `96120344-107761885`; `T2: 96120356` | Initially failed, then marked `Retest PASS`; Elastic showed `VALD` in TDS3, while AKHQ showed no matching RATAN message |
| 7 | C&R followed by market-event removal and validation of restored `T1` | `96120346-107761887` | `PASS`; final `p5(T1)` was auto-pushed |
| 8 | C&R, modification of `T2`, then validation | `96120345-107761886`; `T2: 96120360` | `PASS`; final `p5(T2)` was auto-pushed |
| 9 | Cancellation, cancellation removal, then validation | `96120343-107761884` | `PASS`; restored `p3(T1)` was auto-pushed |
| 10 | `TQRY`, cancellation, then validation of cancellation | `96120348-107761889` | `PASS`; validation caused no further RATAN change |
| 11 | Non-economic C&R `T1→T2` | `96120347-107761888` | `PASS` exception case; `p1(T1)` remained pending and required manual Operations processing |
| 12 | Validate `T1`, C&R, then remove market event | `96120350-107761891`; `T2: 96120362` | `PASS` exception case; `p2` required manual processing while `p5` was auto-pushed |
| 13 | Validate `T1`, C&R, reject, C&R to `T3`, then validate | `96120351-107761892`; `T2: 96120358`; `T3: 96120363` | `PASS` exception case; `p2` required manual processing while final `p5(T3)` was auto-pushed |
| 14 | Auto-suppressed cashflows, including `SUPPDONOT` and specified product contexts | `96120375`; reference `96264326` | `PASS`; payment became available in the Cashflow Blotter and was auto-suppressed |
| 15 | Fixing cashflow after `COMP` | `96120366-107761929` | `PASS`; fixing payment was available in the Cashflow Blotter |
| 16 | Validation, C&R for typology update, then validation of `T2` | `96120371-107761938`; `96120373` | `PASS`; original `p1` was cancelled and replacement `p3` was present |
| 17 | Adhoc SSI, C&R for typology update, then validation | `96120370-107761937`; `96120374` | `PASS`; `p2` and `p3` were marked as Non Eco amendment in the Group Blotter |
| 18 | STELLA cashflows; check SCF | — | No procedure, evidence, or result recorded |
| 19 | EG/NP/SA cashflows; check FX and SCF | — | No procedure, evidence, or result recorded |

## Integration Defect Evidence

Scenarios 4 and 6 document an initial failure in the TDS3-to-RATAN status path:

- TDS3 showed `VALD` in Elastic.
- RATAN did not show the corresponding message on the inspected topic through AKHQ.
- The source records “VALD status not flown from TDS3 to RATAN.”
- Scenario 6 notes that RATAN did not receive the `VALD` message from TDS3 and that assistance from TDS3 was pending.

Both scenarios were later marked `Retest PASS`, but the source does not state whether the issue was fixed, replayed, bypassed, or simply not reproduced. The retest therefore supports observed recovery, not a fully documented permanent resolution.

## Exception Handling

Scenarios 11–13 demonstrate that complex or non-economic amendment sequences do not automatically release every predecessor or reversal cashflow. Operations manually proceeds selected payments that remain in `Pending Validation`, while the latest applicable replacement cashflow may be auto-pushed after validation.

The source records this as expected UAT behavior but does not define the production policy, ownership, approval controls, or canonical rule for selecting payments for manual release.

## Scope Limitations

The source does not establish:

- the identifier or business rule distinguishing v1 and v2 cashflows;
- whether a v1 STP attempt must be blocked when a v2 cashflow remains in the Group Blotter;
- the authoritative TDS3 message, topic, consumer, or correlation key for `VALD`;
- the permanent corrective action for the scenarios 4 and 6 propagation issue;
- a complete result for scenario 3;
- executable evidence for scenarios 18 and 19.

The test trade and payment identifiers provide traceability but should not be treated as general configuration rules.

## Related Wiki Pages

This evidence informs [[concepts/trade-validation-cashflow-gating]], [[concepts/fmrp-cashflow-status-synchronization]], [[concepts/non-economic-cashflow-amendment-handling]], and [[concepts/fmrp-payment-eligibility-and-suppression]]. The unresolved requirements are tracked in [[queries/why-did-tds3-vald-messages-not-reach-ratan]] and [[queries/what-is-the-v1-v2-cashflow-stp-blocking-rule]].