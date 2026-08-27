---
type: source
title: Murex 2.11 Cashflow Integration — Ratan MxML-SCBML Adaptor
authors: []
year: 2024
url: ""
venue: Internal functional requirement
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, cashflow, mxml, scbml, integration, settlement]
related: [murex, ratan, ratan-one, murex-to-ratan-cashflow-interface, mxml-to-scbml-conversion, murex-flow-group-batch-handling, post-settlement-amendment-and-cancellation-handling, what-is-the-authoritative-murex-cashflow-publication-window, what-is-the-canonical-mxml-cashflow-id-format, should-mxml-amount-mapping-use-flowamount-or-flowamountrounded]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Ratan MxML- SCBML Adaptor ( Entity CN, SG, IN, MY).md"]
---
# Murex 2.11 Cashflow Integration — Ratan MxML-SCBML Adaptor

This functional requirement defines the Murex 2.11 to Ratan cashflow interface for CN, SG, IN, and MY entities. Murex publishes individual `MxPayML` payment messages through MQ; the Ratan MxML-SCBML Adaptor converts them into SCBML cashflow data for settlement processing.

The document is a design requirement, not evidence that the described configuration or behavior was deployed or tested in production.

## Interface lifecycle

The intended lifecycle is:

1. Murex publishes eligible cashflows in `INIT` status.
2. After sending the message, Murex changes the payment status from `INIT` to `SNTR`.
3. Ratan returns an acknowledgment to Murex.
4. Settlement Operations releases or settles the cashflow in Ratan.
5. Ratan sends `RELEASED` back to Murex.
6. Murex changes the payment status from `SNTR` to `RSLR`.
7. Ratan `SETTLED` status is not synchronized back to Murex.

This establishes an asymmetric lifecycle boundary: release is fed back to Murex, while final settlement remains a Ratan-side state. See [[murex-to-ratan-cashflow-interface]] and [[event-driven-component-cashflow-status-management]].

## Publication eligibility

The source contains conflicting publication-window requirements:

- the feeding agreement states the next **9 calendar days**, without holiday or weekend adjustment;
- the interface section states the next **7 business days**;
- the `Flows` processing rule selects payments within `mxSystemDate + 9Day`.

New bookings within the eligible window are intended to be published in real time. Existing cashflows are sent by a Monday-to-Friday scheduled job. The conflict is tracked in [[what-is-the-authoritative-murex-cashflow-publication-window]].

## Murex-side product netting

For swap products, including IRS and COM Swap, the source attributes two-leg payment netting to Murex 2.11:

- Murex generates a fixed-leg payment in advance, reportedly at VD-9.
- At fixing, normally around VD-2, Murex generates a reversal of that fixed-leg payment and a payment for the netted fixed- and floating-leg amount.
- Murex sends these payments to Ratan.

This is Murex-specific product processing and is not evidence for Ratan-side auto-netting behavior.

## Market events and SSI refresh

The document identifies these payment-generation patterns:

- `RPL_M`, `RPL`, and `MOD` events generate reversal and new payments.
- `RPL_D` generates a reversal payment.
- Non-economic Murex UDF changes do not generate reversal and new payments.
- Portfolio changes within the same entity do not generate reversal and new payments.
- A daily global SSI refresh job scans trades and generates reversal and new payments when SSI changes.

## MxML source fields

| Field | MxML path | Meaning |
|---|---|---|
| Original Transaction Id | `/MxPayML/scbExtraInfoBlock/TrnOrginalID` | Original trade identifier |
| Parent transaction Id | `/MxPayML/scbExtraInfoBlock/TrnParentID` | Creating trade identifier; `0` if absent |
| Latest Trade Id | `/MxPayML/transactionID` | Latest trade identifier |
| Payment Comment | `/MxPayML/comment` | Identifies reversals, for example `Reverse of flow 50082813` |
| Trade amendment flag | `/MxPayML/scbExtraInfoBlock/amendmentFlag` | `Y` for amendment-generated payments; otherwise `N` |
| Payment ID | `/MxPayML/flowID` | Murex payment flow identifier |
| Payment amount | `/MxPayML/flowAmountRounded` | Earlier mapping specification |
| Payment currency | `/MxPayML/currency` | Payment currency |
| Payment value date | `/MxPayML/valueDate` | Payment date |
| Credit flag | `/MxPayML/isCredit` | Drives payer and receiver assignment |
| Entity name | `/MxPayML/entity` | Murex entity display name |
| Entity FMID | `/MxPayML/scbExtraInfoBlock/entityFMID` | Booking entity FMID |
| Counterparty FMID | `/MxPayML/scbExtraInfoBlock/counterpartyFMID` | Counterparty FMID |
| Flows | `/MxPayML/scbExtraInfoBlock/Flows` | Snapshot of related flow IDs, statuses, and value dates |
| Murex system date | `/MxPayML/scbExtraInfoBlock/mxSystemDate` | Date used in flow-window selection |
| Murex Structure Id | `/MxPayML/flowUserDefinedFields/userDefinedField[fieldLabel='SID']/fieldValue` | Ignore when the value is `0` |

## Core MxML-to-SCBML mapping

| Bean attribute | MxML path | Target format or rule |
|---|---|---|
| `CashFlowInfo.Cashflow__Cashflow_Id` | `/MxPayML/flowID` | Murex payment flow ID |
| `CashFlowInfo.Cashflow__Event_Date` | `/MxPayML/computerDate` | `YYYY-MM-DD` |
| `CashFlowInfo.Cashflow__Payment_Amount` | `/MxPayML/flowAmount` | Revised source; replaces `flowAmountRounded` |
| `CashFlowInfo.Cashflow__Payment_Currency` | `/MxPayML/currency` | Payment currency |
| `CashFlowInfo.Cashflow__Payment_Date` | `/MxPayML/valueDate` | `YYYY-MM-DD` |
| `CashFlowInfo.Data_Flow__Data_Publication_Date_Time` | `/MxPayML/scbExtraInfoBlock/publicationDateTime` | `yyyy-mm-dd'T'hh:mm:Ss'Z'` |
| `CashFlowInfo.Entity__Booking_Entity_Name` | `/MxPayML/entity` | Booking entity name |
| `CashFlowInfo.Entity__Booking_Entity_SCI_FMID` | `/MxPayML/scbExtraInfoBlock/entityFMID` | Booking entity FMID |
| `CashFlowInfo.Entity__Booking_Entity_SCI_LEID` | `/MxPayML/scbExtraInfoBlock/entityLEID` | Booking entity LEID |
| `CashFlowInfo.Entity__Counterparty_Name` | `/MxPayML/counterparty` | Counterparty name |
| `CashFlowInfo.Entity__Counterparty_SCI_FMID` | `/MxPayML/scbExtraInfoBlock/counterpartyFMID` | Counterparty FMID |
| `CashFlowInfo.Entity__General_Ledger_Business_Unit_Name` | `/MxPayML/scbExtraInfoBlock/portBizUnit` | Portfolio business unit |
| `CashFlowInfo.Entity__Person__Trader_PSID` | `/MxPayML/scbExtraInfoBlock/traderID` | Trader ID |
| `CashFlowInfo.Portfolio__Booking_Entity_Trade_Portfolio_Name` | `/MxPayML/portfolio` | Portfolio |
| `CashFlowInfo.Trade__Settlement_Method` | `/MxPayML/type` | Settlement method input |
| `CashFlowInfo.Trade__Trade_Id` | `/MxPayML/transactionID` | Latest trade ID |
| `Trade.Parent_Trade_Id` | `/MxPayML/scbExtraInfoBlock/TrnOrginalID` | Original trade ID |
| `CashFlowInfo.Trade__Trade_State` | `/MxPayML/scbExtraInfoBlock/validationLevel` | Trade validation status |
| `Cashflow.Murex_Structure_Id` | `/MxPayML/flowUserDefinedFields/userDefinedField[fieldLabel='SID']/fieldValue` | Ignore when `0` |
| `Instrument_Common.Murex_Product_Family` | `/MxPayML/transactionFamily` | Product family |
| `Instrument_Common.Murex_Product_Group` | `/MxPayML/transactionGroup` | Product group |
| `Instrument_Common.Murex_Product_Type` | `/MxPayML/transactionType` | Product type |
| `Instrument_Common.Murex_Product_Strategy` | `/MxPayML/strategy` | Product strategy |
| `Instrument_Common.Murex_Product_Typology` | `/MxPayML/transactionTypology` | Trade typology |
| `Trade_Date` | `/MxPayML/tradeDate` | Added in March 2024 |

The source is inconsistent on the amount field: an earlier table and mandatory-field list require `flowAmountRounded`, while Rule 1 changes the target mapping to `flowAmount`. See [[should-mxml-amount-mapping-use-flowamount-or-flowamountrounded]].

## Default SCBML attributes

| Bean attribute | Default value |
|---|---|
| `CashFlowInfo.Cashflow__Bypass_Workflow_Indicator` | Blank |
| `CashFlowInfo.Cashflow__Cashflow_Affirmation_Status` | `Unaffirmed` |
| `CashFlowInfo.Cashflow__Cashflow_Business_Version` | `0` |
| `CashFlowInfo.Cashflow__Cashflow_State` | `Projected` |
| `CashFlowInfo.Cashflow__Cashflow_Version` | `0` |
| `CashFlowInfo.Trade__Delivery_Method` | Blank |
| `CashFlowInfo.Cashflow__Is_Amended_Post_Settlement` | `false` |
| `CashFlowInfo.Cashflow__Is_Payment_Intent_To_Settle` | `true` |
| `CashFlowInfo.Cashflow__Minor_Version_Description` | Blank |
| `CashFlowInfo.Data_Flow__Data_Source_System` | `Murex` |
| `CashFlowInfo.Data_Flow__Data_Sender` | `Murex` |

## Transformation rules

### Trade validation status

```java
mxValidStatus = getMxML('/MxPayML/scbExtraInfoBlock/validationLevel')

if mxValidStatus == 'COMP'
    CashFlowInfo.Trade__Trade_State = 'CONFIRMED'
else if mxValidStatus == 'VALD'
    CashFlowInfo.Trade__Trade_State = 'VALD'  // To be done
else
    CashFlowInfo.Trade__Trade_State = 'TOBESENT'
```

### Cashflow ID

```java
Set prefix = ' M0'
murexFlowId = getMxML('/MxPayML/flowID')

if length(murexFlowId) < 10
    murexFlowId = '0' + murexFlowId

murexFlowId = prefix + murexFlowId
```

The document’s worked example says flow ID `87755146` becomes `M00087755146`. This does not unambiguously follow from the displayed pseudocode, so the required format is tracked in [[what-is-the-canonical-mxml-cashflow-id-format]].

### Product allotment

```java
if family, group, and type are populated:
    family|group|type
else if family and group are populated:
    family|group
else if only family is populated:
    family
```

### Payment direction

```java
isCredit = getMxML('/MxPayML/isCredit')

if isCredit == 'Y'
    payer = 'party2'
    receiver = 'party1'
else
    payer = 'party1'
    receiver = 'party2'
```

### Reversal processing

```java
comment = getMxML('/MxPayML/comment')

if comment is like 'Reverse%'
    reversal = true
    CashFlowInfo.Cashflow__Cashflow_Event_Type = 'Withdrawal'
    swap(
        CashFlowInfo.Cashflow__Payment_Payer_Party_Reference,
        CashFlowInfo.Cashflow__Payment_Receiver_Party_Reference
    )
else
    reversal = false
    CashFlowInfo.Cashflow__Cashflow_Event_Type = 'New'
```

For a comment such as `Reverse of flow 72225832`, the adaptor extracts the final token as the original cashflow ID and applies the standard Murex ID-padding convention. Withdrawal events set both business and cashflow versions to `1`.

### Amendment NSTP rule

```java
amendmentFlag = getMxML(
    '/MxPayML/scbExtraInfoBlock/amendmentFlag'
)
comment = getMxML('/MxPayML/comment')

if amendmentFlag == 'Y' && comment not like 'Reverse%'
    CashFlowInfo.Cashflow__Is_STP = false
    CashFlowInfo.Cashflow__NSTP_Reason = 'Pending on Reversal'
```

## Flow-group completeness

A single market event can create multiple MxML payment messages. The `Flows` block is intended to let Ratan infer the group of payments expected from that event and raise an exception if one or more expected messages are missing.

The documented selection logic is:

```java
if mxSystemDate <= Payment VD <= mxSystemDate + 9Day
    Murex would send the MxML in the current trade event
else
    the payment would be sent in future
```

The source does not define an authoritative grouping key, completeness timeout, retry process, or treatment of stale `Flows` snapshots. See [[murex-flow-group-batch-handling]].

## Post-settlement event treatment

For a post-released or settled trade amendment, such as Cancel & Reissue, Restructure, or Modify:

- the reversal is NSTP;
- Murex does not provide an indicator to identify the rebook payment directly;
- under the documented CN Day 1 heuristic, new payments with value dates within 30 days after the reversal are NSTP;
- new payments outside that 30-day window are STP.

For trade cancellation or similar events such as early termination:

- Murex creates a reversal;
- the reversal is treated as a withdrawal;
- the reversal is STP, not NSTP.

This distinction is documented in [[post-settlement-amendment-and-cancellation-handling]] and should not be generalized into a single reversal policy.

## Settlement-method override

The source specifies a `CCIL` override:

```java
entityFMID = getMxML('/MxPayML/scbExtraInfoBlock/entityFMID')
counterpartFMID = getMxML('/MxPayML/scbExtraInfoBlock/counterpartyFMID')
mxFamily = getMxML('/MxPayML/transactionFamily')
mxGroup = getMxML('/MxPayML/transactionGroup')
currency = getMxML('/MxPayML/currency')

if entityFMID == '4'
   and mxFamily == 'IRD'
   and mxGroup == 'IRS'
   and currency == 'INO'
   and (
       counterpartFMID == '400202766'
       or counterpartFMID in the CCIL client FMID list
   )
    set CashFlowInfo.Trade__Settlement_Method = 'CCIL'
```

The source refers to an external CCIL client FMID list; its current ownership and validity are not established here.

## Outstanding implementation questions

- Which Murex publication window is authoritative?
- Which amount source is authoritative: `flowAmount` or `flowAmountRounded`?
- What is the exact cashflow ID prefix and zero-padding algorithm?
- What complete mapping is required for `validationLevel`, especially `VALD`?
- How should MQ duplicates, retries, late messages, and missing-message exceptions be managed?
- How should unrelated new payments be excluded from the 30-day rebook heuristic?
- What payment-type mapping is required for SWAP_AGENT, RFR, notional, coupon, and MTM flows?
- How should Murex and Ratan reconcile final settlement when `SETTLED` is not returned to Murex?