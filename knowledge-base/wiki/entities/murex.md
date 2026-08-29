---
type: entity
title: Murex
created: 2026-08-22
updated: 2026-08-24
tags: ["financial-platform", "cash-settlement", "CPT", "murex", "upstream-system", "korea", "trading-platform", "cashflows", "settlement", "product-strategy", "migration", "settlements", "trading-system", "source-system", "cashflow-events", "IRS", "pending-fixing", "netting", "cashflow", "dvp", "ccs", "auto-dvp", "test-dependency", "integration", "trade-validation"]
related: ["2025-cash-settlement-tranche-1", "cashflow-monitoring", "cashflow-reconciliation", "ratan-settlement", "korea", "murex-to-ratan-rule-replication", "korea-settlement-localization", "swap-agent", "sal-swap-agent-hard-blocker", "fmo-post-trade-portal", "nstp", "fmrp", "ratan", "projects/murex-cashflow-migration-to-ratan", "murex-to-ratan-cashflow-integration", "murex-ratan-migration-reconciliation", "murex-2-11", "murex-korea", "trade-event-id-lineage", "cashflow-event-versioning", "what-is-the-authoritative-murex-cancellation-removal-cashflow-sequencing-and-correlation-model", "murex-pending-fixing-flag-processing", "pending-another-leg-status", "auto-dvp", "receive-to-pay-cashflow-linkage", "dvp-nstp-exception-handling", "auto-dvp-ebbs", "cashflow-lineage-and-amendment-correlation", "stella", "25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--obojum", "what-is-the-approved-tanzania-dfcc-uat-scenario-and-murex-dependency", "tanzania-scb-dar", "cash-settlement-exception-handling", "cash-settlement-ola-break-monitoring", "cashflow-reinstatement-and-replay", "itrs", "tds3", "scbml", "ratanone", "trade-validation-gating", "what-is-the-authoritative-murex-trade-to-cashflow-linkage", "what-is-the-canonical-trade-validation-key-by-source-system"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---

# Murex

Murex is an upstream trading, cashflow-event, and cashflow source system in the cited cash-settlement and FMRP materials. The Tech Design exception-handling source describes it more specifically as an integrated system in the Cash Settlement operational flow: it supplies cashflows to [[ratan]] and receives status write-backs from the Ratan Murex adaptor.

The RatanOne trade-confirmation and validation design separately describes Murex as a source system for trades and cashflows considered by that design.

Murex responsibilities and observed behaviors differ by source, product version, and processing scope. The claims below retain those boundaries.

## Operational interactions and exception handling

According to the Tech Design exception-handling source:

- Missing Murex-to-Ratan cashflows are primarily detected through Murex real-time ITRS OLA monitoring and may require manual replay by OPS.
- Ratan-to-Murex status write-back failures can occur while a cashflow is `RELEASED SETTLED`.
- Ratan supports replaying the status update.
- No manual Murex action is supported for updating that status.
- Murex PSS participates in investigating both inbound missing cashflows and failed status write-backs.

These operational interaction claims come from the exception-handling design and should not be generalized to every Murex interface or processing flow.

## Trade validation and trade-to-cashflow linkage

According to the RatanOne Trade Validation Confirmation Process Tech Design, the proposed Murex validation rule uses:

- Trade ID
- Trade status

Accepted statuses are `VALD` and `COMP`. Unlike FMRP, this trade-validation source does not specify backward applicability across major versions for Murex.

The same design proposes that trade-confirmation and validation status come from [[tds3]]. It states that internal counterparty and SCF deals may be automatically confirmed, while confirmation is unavailable in CDU and payments may remain pending for affirmation in BAU.

For cashflow linkage, the design extracts both `originalTradeId(murex)` and `tradeId(murex)` from scbml. It does not establish which identifier is authoritative for joining a Murex cashflow to the TDS3 trade-status record. This unresolved linkage is tracked in what is the authoritative murex trade to cashflow linkage.

These claims are limited to the proposed RatanOne trade-confirmation and validation design. They do not establish a general Murex trade-validation rule, confirmation process, or authoritative trade-to-cashflow key for other interfaces or processing scopes.

## FMRP Cashflow Migration Tranche 1

According to the FMRP requirement, Murex is the source trading and processing platform for the Cashflow Migration Tranche 1 scope. The candidate entities are:

- HONGKONG
- SCS HK
- BANGKOK
- TAIPEI
- OBU TAIPEI
- NEWYORK

The FMRP requirement states that Murex trade, event, and cashflow changes are expected to affect RATAN through published states, attributes, event semantics, settlement currency, and migration controls.

Migration-related requirements identified by that source include:

- Allocation events and allocation flags.
- Clearing and Remaining Party events.
- Refresh and UNDO events.
- Step In events and novation workflows.
- Deliverable-currency and non-USD settlement.
- Trade-migration validation and duplicate-payment prevention.
- New attributes such as `Structure id` and `TRAN_CLEAR`.

In the FMRP requirement, Murex remains the subject of the source-side business changes. RATAN impact and ownership are frequently unresolved or marked as UAT support only.

The document does not provide authoritative entity FMIDs, mandatory indicators, or target release dates.

## IRS fixed- and floating-leg payment handling

According to the IRS Fix Leg & Floating leg payment handling requirement, Murex 2.11 is an upstream source of IRS cashflows for [[ratan]]. It provides fixed-leg cashflows, withdrawal or reversal events, and net resultants after floating-rate fixing.

For IRS processing, this source states that Murex supplies `Cashflow.Pending_Fixing_flag`, represented in messages through `pendingFixingFlag` / `isWaitingFixing`. RATAN uses `Y` to hold an eligible non-withdrawal cashflow as `WAITING` with `Pending Another Leg`.

In UK and DE real-time flows, the same requirement states that Murex can send provisional `X`, causing RATAN to apply the `Fixing Unknown` NSTP rule. Murex subsequently supplies the `FMRP_MUREX_FIX_FLAG` file to update the pending-fixing outcome.

This Murex flag-driven handling is distinct from stella IRS identification, which, according to the IRS payment-handling requirement, depends on taxonomy, coupon type, and schedule lookup logic.

## Auto DVP CCS eligibility, linkage, and UAT specification

According to the Auto DVP (eBBS) requirement, [[murex]] is a source system for cashflows processed by RATAN.

In the initial auto dvp scope, a Murex cashflow is eligible as CCS when:

```text
Instrument_Common__ISDA_Taxonomy == "IRD|CS"
```

The stated receive-to-pay linkage uses trade ID and payment date.

The Auto DVP UAT specification separately describes Murex as a source trading platform whose covered cashflows are consumed by [[ratan]] for settlement and DVP-exception processing. Its tested CCS eligibility condition is also:

```text
Instrument_Common__ISDA_Taxonomy == "IRD|CS"
```

For the UAT specification, Murex Receive and Pay cashflows are linked when they have the same `tradeid` and payment date:

```text
Murex: same tradeid + payment date
```

The Auto DVP requirement documents an amendment example in which a replacement Murex pay cashflow has a changed trade ID while retaining an original trade relationship. The authoritative linkage contract for that case is unresolved in what is the authoritative murex receive to pay linkage key for amended cashflows.

The UAT source does not confirm the Murex product version. It is distinct from murex 2 11, which represents the existing version-specific wiki entry. The UAT specification is unexecuted: it defines expected Murex-related inputs and outcomes but does not provide completed test results.

## Role in cashflow rules and self-testing evidence

According to the self-testing evidence, Murex is the source platform or data domain supplying cashflow attributes used by the tested NSTP hard-blocker and netting rules.

The evidence specifically references:

- `Instrument_Common__Murex_Product_Strategy`
- `Cashflow__Payment_Type`
- `Cashflow__Netting_Id`

The tested rule matches `SWAP_AGENT` cashflows with payment type `Coupon` or `Interim MTM` when the cashflow has no existing netting identifier. The source also uses `RECALC` in one cross-strategy netting scenario.

The evidence does not establish a broader Murex product-strategy compatibility matrix.

## Role in the 2025 cash settlement runbook

According to the 2025 cash settlement runbook, `Murex` is the platform explicitly assigned to:

- Push tranche 1 CPT cashflows using the stated test amount of `1 USD/0.01 XAU`.
- Cancel the CPT cashflow after monitoring.

These activities are part of the controlled testing sequence for 2025 Cash Settlement Tranche 1. The runbook also calls for repeating the testing behavior on Apr 29 and Apr 30, subject to clarification of the repeated schedule.

The runbook does not evaluate Murex generally or provide evidence that these actions were completed successfully. Its statements describe intended operational responsibilities only.

## Role in Korea migration analysis

The Korea migration functional analysis identifies Murex as an upstream system whose message format, additional fields, and integration transport must be assessed for the Korea cashflow migration into RATAN.

The checklist asks whether the integration uses MQ, batch processing, or both. It does not define the interface contract, required fields, message schemas, ownership, or implementation status.

These Murex questions are part of the broader migration readiness assessment described in 26 auto netting page md files  135 cash settlement home page cash settlement home page functional requirement 2  1ah4lj. They should not be treated as confirmation that a Murex interface change is required or delivered.

## Trade and cashflow events in deprecated material

The deprecated Murex Trade & Cashflow Events note discusses Murex-originated lifecycle activity, including:

- Trade booking.
- Cancellation.
- Cancellation removal.
- Undefined `C&R` events.

That source identifies a downstream risk for [[ratan]] when related Murex cashflow events arrive out of order or cannot be reliably correlated. It reports reversal linkage for selected cancellation-related cashflows, but reports no equivalent linkage for cancellation-removal outputs.

The deprecated note does not establish which Murex fields carry source-event identity, predecessor lineage, cashflow identity, or version ordering. That contract remains open in what is the authoritative murex cancellation removal cashflow sequencing and correlation model.

These observations are limited to the cited deprecated material. They are not generalized here to all Murex products, versions, or interfaces. For version-specific material, see murex 2 11 and murex korea.

## Tanzania DFCC UAT dependency

According to the UAT testing check for Tranche 1, Murex is an external dependency in the recorded Tanzania DFCC UAT scenario. As of 2026-08-13, the tracker states that trade booking in Murex was pending. An earlier entry also states that user-provided information needed for booking was pending.

The source does not describe Murex interfaces, ownership, booking workflow, or general settlement behavior. Its documented role is limited to the blocker for the Tanzania DFCC test case.

This scenario is therefore separate from the FMRP, IRS, Auto DVP, Korea migration, deprecated-event, exception-handling, trade-validation, and 2025 runbook descriptions above. It does not establish a general Murex booking status or dependency for other entities, products, or UAT scenarios.