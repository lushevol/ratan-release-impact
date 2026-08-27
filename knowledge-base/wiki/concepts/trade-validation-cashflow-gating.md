---
type: concept
title: Trade Validation Cashflow Gating
created: 2026-08-24
updated: 2026-08-23
tags: [trade-validation, cashflow-ingestion, RATAN, settlement-control, STP, NSTP, cashflow-gating, group-blotter, cashflow-blotter]
related: [ratan, stella, murex-211, mo, cashflow-lifecycle-state-model, cashflow-event-control, manual-cashflow-blotter-push-exception, does-manual-ratan-blotter-push-bypass-trade-validation, tds3, fmrp-cashflow-status-synchronization, fmrp-murex-cashflow-status-synchronization, non-economic-cashflow-amendment-handling, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--34-trade-validation-cashf--g0i06l]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/RATAN Settlement Control on Trade Validation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/UAT test cases - Murex 2.11 booking.md"]
---
# Trade Validation Cashflow Gating

Trade validation cashflow gating controls the relationship between a trade's validation state and its cashflow's progression into RATAN.

The RATAN Settlement Control source describes the control as permitting a cashflow to enter the RATAN cashflow blotter only after its related trade reaches an accepted validated state. Separately, the Murex 2.11 UAT source describes a non-validated trade's cashflow as remaining in RATAN's Group Blotter with status `Pending Validation` until the relevant trade status has been validated. These descriptions should be read as source-specific statements about the gate's intended and tested behaviour.

## Operating Models

The RATAN Settlement Control source describes three operating models:

- Current CN flows from [[stella]] and [[murex-211]] push cashflows without a validation check. Unmatched payments do not STP, and the Settlements team performs counterparty affirmation before release.
- From 10 August, SG, MY, and IN use validation-gated ingestion. CN remains on the current BAU process.
- A September 2024 Stella/CDU auto-validation enhancement for SCF and LoanDepo is proposed but marked TBC.

Under the validation-gated model, the control operates at ingestion time rather than relying only on a downstream settlement match.

## Murex 2.11 UAT Behaviour

For ordinary Murex 2.11 lifecycles, the UAT evidence indicates that receipt of `VALD` causes the applicable current cashflow to move automatically to RATAN's Cashflow Blotter.

The following paths generally passed this check:

- Direct `VALD`
- `PEND/CHCK/VALD`
- Modification
- Rejection and rework
- C&R
- Market-event removal
- Cancellation removal
- Typology update
- Fixing

### End-to-End Dependency

The UAT source states that the gate depends on successful status propagation from Murex through [[tds3]] to [[ratan]].

Scenarios 4 and 6 initially showed that `VALD` could be visible in TDS3/Elastic while the corresponding message was absent from RATAN's inspected Kafka topic. A later retest was marked `PASS`, but the UAT source does not document the corrective action or demonstrate durable resolution.

## Exceptions and Non-Standard Outcomes

If validation is unavailable on value date, the RATAN Settlement Control source states that operators monitor the cashflow and may manually push it to the RATAN blotter. That source does not establish whether this action is a controlled override of the validation gate or a separate exception-queue operation. The distinction is tracked in [[does-manual-ratan-blotter-push-bypass-trade-validation]].

The Murex 2.11 UAT source further shows that the gate is not equivalent to universal automatic release:

- In scenarios 11–13, non-economic and complex C&R sequences can leave predecessor or reversal payments pending after successor-trade validation.
- [[operations]] manually proceeds selected payments in those cases.
- In scenario 14, an eligible `SUPPDONOT` payment became available in the Cashflow Blotter and was then auto-suppressed rather than remaining pending.

## Control Boundaries

Trade validation, payment matching, group completeness, and auto-suppression are separate dimensions:

- **Validation** determines whether the related trade is eligible for normal cashflow ingestion or movement from the Group Blotter.
- **Matching** determines whether a payment can proceed through STP.
- **Group completeness** determines whether all cashflows for a market event have arrived.
- **Auto-suppression** is a separate outcome that can occur after an eligible payment becomes available in the Cashflow Blotter.

A cashflow can satisfy one dimension while remaining blocked, pending, or otherwise processed under another. The relationship to the RATAN group blotter is described in [[ratan-group-blotter-event-completeness]].

## Unresolved v1/v2 Control

The Murex 2.11 UAT source proposes preventing STP of a v1 cashflow when v2 cashflows remain in the Group Blotter. It does not define version identification, blocking scope, or release conditions.

This proposed requirement must not be treated as validated by the payment generations shown in the UAT scenarios. It is tracked in [[what-is-the-v1-v2-cashflow-stp-blocking-rule]].