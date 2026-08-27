---
type: source
title: Trade Validation and Cashflow Process
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, trade-validation, cashflow, FMRP, RATAN, Stella, Murex-2-11, TDS3, SCBML]
related: [trade-validation-gated-cashflow-visibility, non-economic-amendment-cashflow-replacement, trade-major-version-cashflow-correlation, what-are-the-authoritative-trade-validation-status-mappings, what-is-the-authoritative-mo-validation-bypass-configuration, cashflow-lifecycle-state-model, fmrp-cashflow-publication-lifecycle, fmrp-cashflow-status-synchronization, fmrp-murex-cashflow-status-synchronization, cashflow-version-concurrency-control, released-settled-amendment-control, scbml-cashflow-payload]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process.md"]
---
# Trade Validation and Cashflow Process

## Source summary

This functional requirement defines a control in which [[entities/stella]] and [[entities/murex-211]] may generate cashflows before trade validation, while [[entities/ratan]] keeps those cashflows held and invisible to settlement operations until the parent trade is considered validated. Trade validation is performed by MO and synchronized to [[entities/tds3]], after which RATAN looks up impacted cashflows and resumes settlement processing.

The document is design evidence rather than production-confirmed implementation evidence.

## Target process

1. Stella or Murex 2.11 generates a cashflow and sends cashflow SCBML to RATAN.
2. RATAN checks the parent trade validation status.
3. If the trade is not validated, RATAN places the cashflow in `HOLD` and excludes it from the settlement GUI.
4. TDS3 receives the trade validation status.
5. RATAN consumes the validated trade status, identifies impacted cashflows, marks them `VALIDATED`, removes them from `HOLD`, and continues the settlement workflow.

Cashflow generation is therefore decoupled from settlement visibility.

## Initial validation from cashflow SCBML

RATAN reads the trade state from:

```text
/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:state[@stateScheme="http://www.sc.com/coding-scheme/state/tradeWorkflowStatus"]
```

The source specifies the following states as validated:

| Data_Flow.Data_Source_System | Trade_State |
|---|---|
| Murex | `VALD` |
| Murex | `CONFIRMED` |
| Other | `SENT` |
| Other | `ECONAFFIRMED` |
| Other | `AFFIRMED` |
| Other | `ECONCONFIRMED` |
| Other | `CONFIRMED` |
| Other | `NONCONFIRMED` |

If the cashflow state is not accepted, RATAN performs a parent-trade lookup, subject to the bypass predicate.

## Stella parent-trade validation

Stella trades are queried by `Trade_ID` and `Trade_Lake_Trade_Major_version`. The source defines the following validation combinations:

| Trade_State | Action_Type |
|---|---|
| `TOBESENT` | `Validate` |
| `SENT` | |
| `ECONAFFIRMED` | |
| `AFFIRMED` | |
| `ECONCONFIRMED` | |
| `CONFIRMED` | |
| `NONCONFIRMED` | |

The intended interpretation is that `TOBESENT` requires the `Validate` action, while the other listed states are sufficient without a specified action.

The Stella SCBML fields are:

| Logical model name | SCBML path |
|---|---|
| `Trade_ID` | `/scb:SCBML/scb:payload/scb:FPMLPayload/scbextn:rateFixing/scbextn:tradeIdentifier/conf:tradeId[@tradeIdScheme="http://www.sc.com/coding-scheme/tradeId"]` |
| `Trade_Lake_Trade_Major_version` | `(/scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade\|/scb:SCBML/scb:payload/scb:FPMLPayload/((*/(*:originalTrade\|*:trade))\|((*:novation\|*:cancelReissue)/*:newTrade)))/conf:tradeHeader/conf:partyTradeIdentifier[conf:partyReference/@href="party1"]/conf:versionedTradeId[conf:tradeId/@tradeIdScheme="http://www.sc.com/coding-scheme/tradeId/tradeLake"]/conf:version` |
| `Trade_State` | `/scb:SCBML/scb:payload/scb:FPMLPayload/scb:header/scb:process/scb:subState[@stateScheme="http://www.sc.com/coding-scheme/state/tradeWorkflowStatus"]` |
| `Action_Type` | `/scb:SCBML/scb:payload/scb:FPMLPayload/scb:header/scb:process/scb:transactionType[@transactionTypeScheme="http://www.sc.com/coding-scheme/action"]` |

For a validated TDS3 trade message, RATAN uses `Trade_ID` and `Trade_Lake_Trade_Major_version` to locate cashflows, marks matching records `VALIDATED`, removes `HOLD`, and resumes processing.

## Murex 2.11 parent-trade validation

Murex trades use `Source_System_Trade_Internal_Id` to locate the parent trade. The parent trade is considered validated when `Source_System_Validation_Status` is `VALD` or `COMP`.

| Field name | Logical model name | SCBML path |
|---|---|---|
| Trade ID | `Source_System_Trade_Internal_Id` | `(/scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade\|/scb:SCBML/scb:payload/scb:FPMLPayload/((*/(*:originalTrade\|*:trade))\|((*:novation\|*:cancelReissue)/*:newTrade)))/conf:tradeHeader/conf:partyTradeIdentifier[conf:partyReference/@href="party1"]/conf:tradeId[@tradeIdScheme="http://www.sc.com/coding-scheme/tradeId/Murex/tradeInternalId"]` |
| Trade status | `Source_System_Validation_Status` | `/scb:SCBML/scb:payload/scb:FPMLPayload/scb:header/scb:process/scb:subState[@stateScheme="http://www.sc.com/coding-scheme/state/Murex"]` |

| Source_System_Validation_Status | Interpretation |
|---|---|
| `VALD` | Validated |
| `COMP` | Validated |

The source contains an inconsistent table heading that labels these values as `Source_System_Trade_Internal_Id`; the status interpretation above follows the surrounding validation rules.

## Validation bypass predicate

The following Stella trades bypass the MO validation check:

```java
Data_Flow.Data_Source_System==Stella and (
  Entity Egypt, Nepal, Saudi
    (FMID "401036553", "400991880", "400007847")
  or (
    Product: SCF
    (Instrument_Common.CFI_Code =="MMMXXX")
  or
    LoanDepo
    (Instrument_Common.ISDA_Taxonomy =="InterestRate:LoanDeposit")
  )
  or (
    CN entities FMID in (
      "400001378","10020899","235003861","10078716","10036642",
      "10062461","10032025","400054708","400054737","400054741",
      "400057714","400075752","400085753","400090093","400095464",
      "400130180","400130178","400185419","400193370","400209000",
      "400218197","400229749","400516443","400516442","400667486",
      "400677737","400683682","400798477","400899993"
    )
    and Instrument_Common.ISDA_Taxonomy in (
      ForeignExchange:Forward,
      ForeignExchange:Spot,
      ForeignExchange:NDF,
      ForeignExchange:Swap
    )
  )
)
```

The bypass categories are:

- Egypt, Nepal, and Saudi entities with FMIDs `401036553`, `400991880`, and `400007847`.
- `SCF` where `Instrument_Common.CFI_Code == "MMMXXX"`.
- [[entities/loandepo]] where `Instrument_Common.ISDA_Taxonomy == "InterestRate:LoanDeposit"`.
- Listed CN entities when the taxonomy is `ForeignExchange:Forward`, `ForeignExchange:Spot`, `ForeignExchange:NDF`, or `ForeignExchange:Swap`.

The source does not identify an authoritative configuration owner, effective date, or reference-data source for this list.

## Amendment behavior

Trade major version is part of the cashflow correlation key for Stella. When a later version is validated, earlier rejected or obsolete versions remain unavailable, closed, or withdrawn as specified by the event sequence.

Economic amendments generate withdrawal and replacement events. Non-economic amendments require an additional check of the original cashflow history:

- If the original cashflow has no relevant manual action and has not been released or settled, RATAN may replace it with the latest cashflow event sequence.
- If the original cashflow has been touched, released, or settled, RATAN must not silently replace it. The source uses `HOLD-NONECO` for the non-economic amendment path.
- New economic-amendment withdrawal and replacement events use normal `HOLD` behavior until validation.

The in-scope manual-action list is:

1. Exception Fix/Reject, including affirmation, SSI key-in, SWIFT value-date key-in, approve, and reject.
2. Settle as Gross.
3. Netting or un-netting.
4. Hold or unhold.
5. Manual fail.
6. Re-instate.
7. FM Comment.
8. Manual Cashflow Suppression.
9. Manual Swift Suppression.
10. Early materialization.

## Business-case outcomes

| Business case | Intended outcome |
|---|---|
| New trade, not validated, then cancelled | No trade events are validated; cashflows remain unavailable to settlement operations. |
| New trade validated, then cancelled | The original cashflow may be visible and processed before the cancellation version is validated; the cancellation withdrawal remains held until then. |
| New trade rejected, then FO-amended | Only cashflows from the validated major version 2 are visible. |
| Validated trade, economic amendment | Earlier cashflows are withdrawn or closed; only cashflows from the validated amendment become visible. |
| Validated trade, non-economic amendment with no user action | The original cashflow may be replaced by the latest validated cashflow events. |
| Validated trade, non-economic amendment with manual action or settlement | The original cashflow is protected and must not be silently substituted. |

Scenario examples use illustrative identifiers such as `T1`, `C1`, `C2`, and `C3`, and contain apparent status spellings such as `SETTELD` and `CANCELLD`. These should not be treated as canonical status contracts without confirmation.

## Evidence limitations and open questions

The requirement does not establish production implementation, test evidence, or a definitive status taxonomy. The following require confirmation through [[queries/what-are-the-authoritative-trade-validation-status-mappings]] and [[queries/what-is-the-authoritative-mo-validation-bypass-configuration]]:

- Whether `NONCONFIRMED` is intentionally a validated Stella state.
- Whether `COMP` is a Murex validation status or a completion status.
- Whether `TOBEVALIDATED` is a formal intermediate state.
- Which audit data determines historical manual action.
- Whether `HOLD`, `HOLD-NONECO`, `ACTIVE`, `CLOSED`, and `CANCELLED` are canonical RATAN states.
- How cancellation races, out-of-order TDS3 messages, retries, and replay are controlled.