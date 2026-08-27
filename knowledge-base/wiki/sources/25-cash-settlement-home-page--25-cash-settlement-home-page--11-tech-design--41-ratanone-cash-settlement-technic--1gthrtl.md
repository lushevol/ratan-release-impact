---
type: source
title: Trade Validation Confirmation Process Technical Design
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, trade-validation, trade-confirmation, RatanOne, technical-design]
related: [trade-validation-gating, group-level-trade-validation-hold, fmrp-major-version-backward-validation, ratanone, tds3, scbml, ratan-cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Trade Validation Confirmation Process Tech Design.md"]
---
# Trade Validation Confirmation Process Technical Design

## Purpose

This technical design proposes preventing settlement workflow processing until the underlying trade has reached an acceptable confirmation or validation status. Settlement Operations requested that payments be processed only after trade validation, even though the trade-status information becomes available after cashflows enter RatanOne.

The document marks Option 1 as preferred on 2024-05-29. The preference is not a final architectural decision because ownership, identifier linkage, state transitions, and operational behavior remain unresolved.

## Design principles

- Source trade confirmation and validation status from [[tds3]] for FMRP and Murex.
- Maintain the trade keys needed for cashflow linkage within RatanOne.
- Retain [[cdups]] only as a dependency for FX SWAP near-leg confirmation; this dependency is TBD.
- Maintain trade status within `ratan-cashflow-standarlization-service`, described as the Group service.
- Support trade-status queries within the settlement domain.
- Keep a cashflow group pending until all expected cashflows have arrived.
- Prevent workflow publication when an associated trade is not validated.

## Source-specific validation rules

FMRP validation uses trade ID, major version, and status. The accepted statuses are:

- `SENT`
- `AFFIRMED`
- `CONFIRMED`
- `TOBESENT+Validate[action]`

A validated FMRP major version applies backward to earlier major versions. For example, validation of major version 4 is treated as validating major versions 1, 2, and 3.

Murex validation uses trade ID and status. The accepted statuses are:

- `VALD`
- `COMP`

The Murex rule is trade-ID-only and does not inherit the FMRP major-version rule.

## Group behavior

The proposed group-level behavior is:

1. The group remains `PENDING` until all cashflows have arrived.
2. After all cashflows arrive, the group proceeds only when all associated trades are validated.
3. If all cashflows have arrived but any associated trade is not validated, the group becomes `PENDING_TRADE_VALIDATION`.
4. A cashflow becomes `OFFSET` when both new and withdrawal events arrive while it is pending.

The source does not provide a complete state machine, transition table, persistence contract, retry behavior, or late-validation recovery procedure. The headings “Cashflow Group state machine” and “manual deliver cashflow for trade validated” contain no substantive implementation detail.

## Alternatives

### Option 1 — Group-service gate

Option 1 is marked preferred as of 2024-05-29. It proposes that the Group service:

- Add a control to hold messages when the associated trade is not validated.
- Publish to workflow only after the group is complete and the trade is validated.
- Disable the `Manual STP` function for items associated with an unvalidated trade.

The main advantage is avoiding changes to the current cashflow lifecycle workflow. The principal concern is that the standardization or Group service would participate in cashflow progression control rather than only group management. Users may also need to consult both the cashflow and group blotters to identify blockers.

### Option 2 — Lifecycle-service status

Option 2 would:

- Add `TOBEVALIDATED` before `PROJECTED`.
- Have the Lifecycle service query the Group service for trade validation.
- Make the Lifecycle service responsible for cashflow status movement and STP workflow control.

This option provides clearer status visibility and a more explicit lifecycle ownership boundary, but changes the main workflow and increases regression effort. It is crossed out in the source and is not the preferred option.

## Amendment scenario

The design records a risk involving different trade versions:

1. Cashflow `C1` for trade `T1` major version 1 is waiting.
2. `T1` major version 1 becomes validated.
3. New cashflow `C2` arrives for `T1` major version 2, but version 2 is not validated.
4. `C1` may settle.
5. Validation for version 2 arrives later.
6. The withdrawal for `C1` and the new cashflow `C2` may then settle.

The source states that this control may not be required for current Murex behavior and suggests that a hold control may be preferable. This is an unresolved policy consideration rather than a finalized solution.

## SCBML extraction mappings

The source specifies the following extraction paths for the Cashflow Group service:

| field | xpath |
|---|---|
| originalTradeId(murex) | /scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeIdentifier/conf:originatingTradeId/conf:tradeId[@tradeIdScheme='[http://www.sc.com/coding-scheme/tradeId/originatingTradeId](http://www.sc.com/coding-scheme/tradeId/originatingTradeId)'] |
| tradeId(murex) | /scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeIdentifier/conf:tradeId[@tradeIdScheme='[http://www.sc.com/coding-scheme/tradeId](http://www.sc.com/coding-scheme/tradeId)'] |
| tradeId(stella) | /scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeIdentifier/conf:tradeId[@tradeIdScheme='[http://www.sc.com/coding-scheme/tradeId](http://www.sc.com/coding-scheme/tradeId)'] |
| tradeStatus(both) | /scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:state[@stateScheme='[http://www.sc.com/coding-scheme/state/tradeWorkflowStatus](http://www.sc.com/coding-scheme/state/tradeWorkflowStatus)'] |

The Murex and Stella `tradeId` fields use the same XPath in the design, although their logic-model names differ. This mapping requires confirmation.

## SCBML logic-model mapping

| **Field** | **Logic Model Name(Murex)** | **Logic Model Name(Stella)** |
| --- | --- | --- |
| tradeId | Source_System_Trade_Internal_Id | Trade_Id |
| majorVersion | | Trade_Lake_Trade_Major_Version |
| trackingVersion | | Tracking_Version |
| tradeStatus | Source_System_Validation_Status | Trade_State |
| productType | Instrument_Common.ISDA_Taxonomy | Instrument_Common.ISDA_Taxonomy |
| action | Source_System_Action_Type | Action_Type |
| sourceSystem | Data_Flow.Data_Sender | Data_Flow.Data_Sender |

The mapping specifies major and tracking versions for Stella but not for Murex. It does not define the canonical key used to join TDS3 trade status to RatanOne cashflows.

## Open questions and limitations

- Which Murex identifier is authoritative for TDS3-to-cashflow linkage: `originalTradeId`, `tradeId`, or another key?
- Is `PENDING_TRADE_VALIDATION` a group-only state, a cashflow state, or both?
- Which service releases a group after late validation?
- How are validation reversals, corrections, and status regressions handled?
- How is the TBD CDUPS dependency resolved for FX SWAP near-leg confirmation?
- What operational procedure is intended by “manual deliver cashflow for trade validated”?
- What is the impact on LIEN STP processing?
- What audit evidence proves that a group was released only after all required trades were validated?

## Evidence assessment

The source provides moderate evidence for the stated business requirement, proposed statuses, source-specific validation rules, and SCBML mappings. It provides weak evidence for implementation feasibility because it omits detailed APIs, message contracts, persistence schemas, complete state transitions, and test evidence.
