---
type: source
title: Netting Service - GUI & API Integration
authors: []
year: 0
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, RATAN, GUI, API, functional-requirement]
related: [ratan, razor, stella, cashflow-netting, netting-api-contract, settle-as-gross-maker-checker-workflow, netting-resultant-settlement-method-selection, what-is-the-authoritative-manual-netting-and-un-netting-eligibility-matrix, what-happens-when-netting-calculates-to-zero, what-is-the-authoritative-settlement-method-precedence-for-netting-resultants, what-is-the-authoritative-razor-release-validation-for-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Service - GUI & API intergration.md"]
---
# Netting Service - GUI & API Integration

This functional requirement describes RATAN GUI and API processing for manual netting, manual un-netting, Stella-triggered automatic un-netting, and the maker/checker **Settle as Gross** workflow.

The document is an implementation-oriented requirement rather than a fully resolved contract. It contains explicit TBC items, inconsistent GUI and backend eligibility rules, and sample-data inconsistencies. Its examples should not be used as canonical test fixtures without reconciliation.

## Manual netting

The GUI guide permits netting for selected cashflows that are neither `Settled` nor `Released`, have a blank Netting Id, and are in one of:

`Projected`, `Queued`, `Pending`, `Validated`, `Ready`, `Waiting`, or `Hold`.

The backend API re-queries each selected cashflow and validates a narrower state set:

`Projected`, `Queued`, `Pending`, or `Validated`.

All components must have blank Netting Ids and identical payment currency, payment date, booking entity FMID, and counterparty FMID. The requirement that neither current nor prior cashflow versions have been sent to [[razor]] is marked TBC.

## Netting GUI request

```js
{ cashflowId: item.Cashflow.Cashflow_Id, -- cashflowVersion: item.Cashflow.Cashflow_Version, businessVersion: item.Cashflow.Cashflow_Business_Version, fmid: item.Entity?.Counterparty_SCI_FMID, currency: item.Cashflow.Payment_Currency, entity: item.Entity?.Booking_Entity_SCI_FMID, valueDate: item.Cashflow.Payment_Date, settlementMethod: item.Trade.Settlement_Method, payRec: item.Cashflow.Pay_Receive_Indicator, cashflowAmount: item.Cashflow.Payment_Amount, netId: item.Cashflow.Netting_Id || '', }
```

| GUI Field | Cashflow Bean field | Comment |
| --- | --- | --- |
| cashflowId | ${CashFLowInfo.Cashflow__Cashflow_Id} | |
| cashflowVersion | ${CashFLowInfo.Cashflow__Cashflow_Version} | |
| businessVersion | ${CashFLowInfo.Cashflow__Business_Version} | |
| fmid | ${CashFLowInfo.Entity__Counterparty_SCI_FMID} | |
| currency | ${CashFLowInfo.Cashflow__Payment_Currency} | |
| entity | ${CashFLowInfo.Entity__Booking_Entity_SCI_FMID} | |
| valueDate | ${CashFLowInfo.Cashflow__Payment_Date} | |
| settlementMethod | ${CashFLowInfo.Cashflow__Settlement_Method} | |
| payRec | ${CashFLowInfo.Cashflow__Pay_Receive_Indicator} | |
| cashflowAmount | ${CashFLowInfo.Cashflow__Payment_Amount} | |
| netId | ${CashFLowInfo.Cashflow__Netting_Id} | value would be blank |

## Netting calculation

The stated convention is SCB `Pay` as positive and SCB `Receive` as negative. The signed sum determines the resultant direction: a positive total is `Pay`; a negative total is `Receive`.

The source does not define zero-balance treatment, rounding, precision, or currency-decimal rules. See what happens when netting calculates to zero.

## Resultant construction

A netting resultant is generated using the SCBML `New` template. It receives new identifiers and is initialized as `Queued`, `Unaffirmed`, `New`, version `0`, with payment type `netAmount`.

| Bean field name | Description |
| --- | --- |
| ${CashFLowInfo.Data_Flow__Data_Publication_Date_Time} | Current timestamp |
| ${CashFLowInfo.Data_Flow__Data_Publication_Id} | New UUID |
| ${CashFLowInfo.Data_Flow__Unique_Identifier_Message_Id} | New UUID |
| ${Cashflow__Event_Date} | Current System Date |
| ${CashFLowInfo.Cashflow__Netting_Id} | New UUID with length as 36 |
| ${CashFLowInfo.Cashflow__Cashflow_Id} | New cashflow id with length as 12 |
| ${CashFLowInfo.Cashflow__Payment_Payer_Party_Reference} | If ${CashFLowInfo.Cashflow__Pay_Receive_Indicator} is Pay then `Party1` else `Party2` |
| ${CashFLowInfo.Cashflow__Payment_Receiver_Party_Reference} | If ${CashFLowInfo.Cashflow__Pay_Receive_Indicator} is Pay then `Party2` else `Party1` |
| ${CashFLowInfo.Cashflow__Payment_Currency} | Copy from the first component cashflow |
| ${CashFLowInfo.Cashflow__Payment_Amount} | Calculated from last step |
| ${CashFLowInfo.Cashflow__Payment_Date} | Copy from the first component cashflow |
| ${CashFLowInfo.Instrument_Common__CFI_Code} | Copy from the first component cashflow |
| ${CashFLowInfo.Instrument_Common__Source_System_Instrument_Sub_Type} | Copy from the first component cashflow |
| ${CashFLowInfo.Instrument_Common__ISDA_Taxonomy} | Copy from the first component cashflow |
| ${CashFLowInfo.Portfolio__Booking_Entity_Trade_Portfolio_Name} | Copy from the first component cashflow |
| ${CashFLowInfo.Portfolio__Booking_Entity_Trade_Portfolio_Unique_Name} | Copy from the first component cashflow |
| ${CashFLowInfo.Entity__Booking_Entity_SCI_FMID} | Copy from the first component cashflow |
| ${CashFLowInfo.Entity__General_Ledger_Business_Unit_Name} | Copy from the first component cashflow |
| ${CashFLowInfo.Booking_Entity_General_Ledger_Business_Unit_Id} | Copy from the first component cashflow |
| ${CashFLowInfo.Entity__Counterparty_SCI_FMID} | Copy from the first component cashflow |
| ${CashFlowInfo.Data_Flow__Data_Source_System} | Hardcode as `Ratan` |
| $CashFlowInfo.Data_Flow__Data_Sender} | Hardcode as `Ratan` |
| ${CashFlowInfo.Cashflow__Cashflow_Event_Type} | Hardcode as `New` |
| ${CashFlowInfo.Cashflow__Cashflow_State} | Hardcode as `Queued` |
| {CashFlowInfo.Cashflow__Cashflow_Affirmation_Status} | Hardcode as `Unaffirmed` |
| ${CashFlowInfo.Cashflow__Cashflow_Business_Version} | Hardcode as 0 |
| ${CashFlowInfo.Cashflow__Cashflow_Version} | Hardcode as 0 |
| ${CashFlowInfo.Cashflow__Payment_Type} | Hardcode as `netAmount` |
| ${CashFlowInfo.Trade__Settlement_Method} | Hardecode as `Gross` - DVP: would be DVP if DVP exists in any component cashflow - CCIL: CCIL if IRS Netting |
| ${CashFlowInfo.Trade__Delivery_Method} | Hardcode as `Cash` |
| Family | Inherit if values are same; empty if different |
| Group | Inherit if values are same; empty if different |
| Type | Inherit if values are same; empty if different |
| Typology | Inherit if values are same; empty if different |
| Strategy | Inherit if values are same; empty if different |
| Trade_Id | Inherit if values are same; empty if different |

“First component cashflow” is not deterministically defined. The `Gross`/`DVP`/`CCIL` settlement-method rule has no stated precedence.

## Lifecycle and exceptions

After successful manual netting, component cashflows become `Netted`, and the generated resultant becomes `Queued`. RATAN creates a `Net Cashflow` exception on the resultant. If a component previously carried a `Previously Netted` exception, that exception is closed when the component is netted again.

For manual un-netting, the backend validates that the resultant has a Netting Id and is `Queued`, `Pending`, or `Validated`. Components identified by the Netting Id return to `Queued`; the resultant becomes `Dead`; the resultant's `Net Cashflow` exception closes; and components receive a `Previously Netted` exception.

## Un-net GUI request

```js
{ cashflowId: details.Cashflow.Cashflow_Id, cashflowVersion: details.Cashflow.Cashflow_Version, businessVersion: details.Cashflow.Cashflow_Business_Version, entity: details.Entity?.Booking_Entity_SCI_FMID, currency: details.Cashflow.Payment_Currency, netId: details.Cashflow.Netting_Id, valueDate: details.Cashflow.Payment_Date, }
```

## Automatic un-netting

stella Withdrawal events from Middle Office trade amendments, cancellations, or terminations can trigger automatic un-netting for a netted component. If the resultant remains in RATAN in `Waiting` or `Ready`, it becomes `Dead`; remaining components return from `Netted` to `Queued`.

Where the resultant was released or settled downstream, RATAN instead creates a new `Withdrawal` event for the resultant, which follows `Projected → Queued → Waiting`. This system-driven path must be distinguished from prohibited user-initiated netting or un-netting of released or settled cashflows.

## Settle as Gross

Settlement Ops makers can select **Settle as Gross** for a `WAITING` cashflow with `Pending Netting` or `Pending Another Leg` status. The action creates a checker-only `Settle As Gross` exception and moves the cashflow to `WAITING / Pending Exception / Pending Verification/Operator`.

A checker approves the exception through multiple-exception approval, moving the cashflow to `READY`. The document does not define the rejection lifecycle or exception disposition when the checker does not agree.

## Scope note

`Fixing Rate` and `Amortized notional` are requested preview fields but are unavailable from Stella. The enhancement is deferred to RATAN-14236.