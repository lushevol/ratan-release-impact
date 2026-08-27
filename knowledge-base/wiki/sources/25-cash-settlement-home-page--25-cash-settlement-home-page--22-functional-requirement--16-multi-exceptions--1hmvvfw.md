---
type: source
title: Multi Exception Generation
authors: []
year: 2023
url: ""
venue: Internal functional requirement
tags: [cash-settlement, ratan, exceptions, maker-checker, ssi]
related: [ratan, cashflow-multi-exception-generation, pending-confirmation-affirmation, ssi-dual-blind-remediation, back-value-exception-management, high-value-payment-exception, rdm, fx-conversion-service, settlement-ops]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md"]
---
# Multi Exception Generation

This functional requirement specifies intended multi-exception generation, presentation, and maker/checker remediation behavior when a new cashflow enters the [[ratan]] settlement workflow. It describes actionable maker/checker exceptions, checker-only classifications, SSI validation and dual-blind controls, rejection loops, and dependencies on [[sci]], [[rdm]], and the [[fx-conversion-service]].

The document is evidence of required behavior, not confirmation of implementation, testing, or production approval.

## Exception categories

### Maker/checker exceptions

- Pending Confirmation/Affirmation
- Missing Vostro
- Multi Vostro
- Nostro vs Vostro Mismatch
- Adhoc SSI
- Missing Nostro
- Validate Ben Info
- GSAM Client
- Back Value
- Bad Business Day
- Adhoc_Netting
- Corporate Client

### Checker-only exceptions

- Secondary Vostro
- Reversal
- Rebook
- NetOverAmend
- Net Cashflow
- Settled as gross
- Previously Netted
- Bad Business Day
- Replayed from Failed Status
- NSTP Client, NSTP Product, and `NSPP Currency`
- High Value Payment

## Confirmation-status mapping

| # | Message | Xpatch/Logic Model | Confirmation Status |
| --- | --- | --- | --- |
| 1 | Stella Trade | `Trade_State` | `NONCONFIRMED\|AFFIRMED\|CONFIRMED` |
| 2 | Murex Trade | `Source_System_Validation_Status` | `COMP` |
| 3 | Stella Cashflow | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:state[@stateScheme='http://www.sc.com/coding-scheme/state/tradeWorkflowStatus']` - TBD | `NONCONFIRMED\|AFFIRMED\|CONFIRMED` |
| 4 | Murex Cashflow | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:state[@stateScheme='http://www.sc.com/coding-scheme/state/tradeWorkflowStatus']` | `COMP` |

Pending Confirmation/Affirmation is generated only where both parent-trade and cashflow confirmation are missing. Ratan first evaluates the cashflow message and, if it is not confirmed, queries the parent trade by trade ID. A later trade confirmation should scan related Murex and Stella cashflows with the same trade ID and remove the exception where the trade is confirmed.

The exception must not be generated where:

- `Cashflow.Cashflow_Event_Reason==Reversal`
- `Entity.Counterparty_Is_Internal==Y`
- A component cashflow with the same trade ID is confirmed

The Stella cashflow XPath is explicitly marked TBD.

## Lifecycle and netting field mappings

| New Logical model | New Physical model | Sample Values |
| --- | --- | --- |
| `Cashflow.Cashflow_Event_Reason` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:eventReason[@eventReasonScheme='http://www.sc.com/coding-scheme/eventReason']` | `Reversal`: withdrawal of a settled cashflow; `Rebook`: new cashflow from post-settlement amendment; `Reversal_Rebook`: component cashflow contains either event |
| `Cashflow.Booking_System_Event` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:event[@eventScheme='http://www.sc.com/coding-scheme/event/Booking-System-Event']` | `New`: new trade booking; `Amendment`: trade amendment or similar event; `Withdrawal`: trade cancellation |
| `Cashflow.Is_Adhoc_Net` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:isCashflowAdhocNet` | `true`: manual netting where not all component cashflows are Pending Netting; `false`: otherwise |

## Rule highlights

- Generate `Validate Ben Info` where payment type is `MT202` and beneficiary BIC is blank.
- Generate GSAM Client where SCI `legalEntity.operationStatus1Value` is `REFER`.
- Generate Corporate Client where SCI `fmAccount.fmType` is `CORP`.
- Run Back Value after SSI stamping or SSI checker approval. It is generated for a past `Cashflow.Payment_Date`, or for same-day payment after the GMT release cutoff, unless Vostro settlement means is `Over Account`.
- Generate NetOverAmend where `Cashflow.Cashflow_Event_Reason==Reversal_Rebook` and `Cashflow.Netting_Id is not null`.
- Generate Previously Netted only after Pending Netting and Auto Netting checks are inapplicable, where `Cashflow.Status_Event_Type == 'Un-Net'` and `Trade.Settlement_Method == 'Gross'`.
- Generate Replayed from Failed Status when Settlement Ops Re-Instate changes a cashflow from `FAILED` to `QUEUED` and Ratan returns it to workflow.
- Generate High Value Payment above USD 100 million after conversion through the FX Conversion API.

## Resolution controls

SSI remediation requires GUI and backend validation. Vostro and Nostro settlement means and settlement account must match; the checker-side backend validation is a hard blocker.

For standard SSI and Back Value remediation, maker and checker enter values independently. Ratan compares their inputs before closure. A mismatch leaves the relevant SSI or Back Value exception open while other completed exceptions may close.

For Adhoc SSI, a checker rejection returns the item to the maker. Previous maker input may be preloaded only when the same maker user reopens the item; one maker's prior entry must not become another maker's default.

## User-interface requirements

- Vostro information is always visible on the left.
- Nostro information is always visible at the top left.
- Cashflow Affirmation is always visible to makers, but mandatory only when Pending Affirmation exists.
- Back Value is visible only when generated.
- NSTP is visible only when one or more NSTP exceptions exist.
- Other Exceptions is visible only when relevant exception classifications exist.
- Comments are always available as free text.
- Maker/checker actions appear at the bottom of the exception page.

Prototype: https://www.figma.com/file/crlFDt3cKfWzIXWdUhrtQ7/Exceptions-in-Cashflow-CN?node-id=396%3A5862&t=9BRAKYhpMA7akI7t-0

## Open implementation gaps

The source does not define exception precedence, external-service failure handling, SSI/date comparison normalization, the release cutoff time, or the FX-rate methodology. It also uses inconsistent labels for Pending Confirmation/Affirmation versus Pending Affirmation and NSTP versus `NSPP Currency`.