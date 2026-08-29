---
type: source
title: IRS Fixed Leg & Floating Leg Payment Handling
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, IRS, Murex, Stella, RATAN, pending-fixing]
related: [irs-fixed-floating-leg-netting, pending-another-leg-status, murex-pending-fixing-flag-processing, irs-refixing-unnetting-and-renetting, murex, tdsx]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---
# IRS Fixed Leg & Floating Leg Payment Handling

This functional requirement defines how [[ratan]] handles Interest Rate Swap (IRS) fixed- and floating-leg coupon cashflows from [[murex]] and stella. Its stated objective is to settle the net amount for a payment schedule rather than settling a known fixed leg independently before its corresponding floating-leg amount is known.

The requirement contains distinct source-system pathways. Murex processing is driven by the upstream pending-fixing flag and market-specific delivery timing. Stella processing uses IRS taxonomy, coupon type, and schedule information retrieved through [[tdsx]]. These pathways must not be treated as interchangeable.

## Murex 2.11 Processing

For CN, SG, IN, and MY real-time flows, Murex sends a fixed-leg cashflow with pending-fixing flag `Y`. RATAN holds it as `WAITING` with `Pending Another Leg`. After floating-rate fixing, Murex sends a reversal of the fixed leg and a net resultant; RATAN cancels the original fixed leg and processes the resultant through normal cashflow checks.

For UK and DE, the treatment depends on batch versus real-time delivery:

- In batch, a fixed leg with `Y` is held as `Pending Another Leg`.
- A real-time reversal or resultant carrying provisional `X` is blocked with the `Fixing Unknown` NSTP rule until a later `FMRP_MUREX_FIX_FLAG` record provides the actual flag.
- A batch resultant with `N` continues through standard STP checks.
- In real time, a fixed leg initially carrying `X` is blocked by `Fixing Unknown`; the later file update changes the treatment to either `Pending Another Leg` for `Y` or normal STP checks for `N`.

### Pending-Fixing Field Mappings

```text
MXML Path: /MxPayML/scbExtraInfoBlock/isWaitingFixing

Physical Model:
 /scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:pendingFixingFlag

Logical Model:
 Cashflow.Pending_Fixing_flag
```

### `FMRP_MUREX_FIX_FLAG` Example

```text
FLOW_ID;WAIT_FIX
110777819;N
110777820;N
110777821;N
110777823;N
110777824;N
110777826;N
110777985;N
110777986;N
110777987;N
110777988;N
110777995;N
110777997;N
110778423;N
110778426;N
110778442;N
110778443;N
110778444;N
110778446;N
110810074;N
110810075;N
```

The file is applicable only when the target cashflow meets all stated conditions:

```text
Cashflow Status == WAITING
& Sub Status type == Pending Exception
& Sub Status in (Pending Operator, Pending Verification)
& Exception code == 'Fixing Unknown'
```

The requirement states that RATAN must not reprocess a fixed-leg reversal when the underlying fixed leg is already cancelled. It should instead continue processing the net resultant through remaining STP checks.

## Stella IRS Coupon Processing

For Stella cashflows, IRS eligibility is based on data source, ISDA taxonomy, payment type, and non-withdrawal event type. The source specifies the following rule:

```text
if (CashFlowInfo.Data_Flow__Data_Source_System=='Stella'
    and Instrument_Common.ISDA_Taxonomy in(
        ' InterestRate:IRSwap:FixedFloat',
        'InterestRate:IRSwap:OIS',
        'InterestRate:IRSwap:FloatFloat',
        'InterestRate:IRSwap:FixedFixed'
    )
    and Cashflow.Payment_Type in('Coupon/Fixed','Coupon/Float')
)
and Cashflow.Cashflow_Event_Type != Withdrawal

Then compare cashflow number with TDX for same cashflow ID and value date,

If RATAN cashflow number < TDX cashflow number,
then update status to "WAITING + Pending another leg"

else go to next check
```

For FMRP booking lineage `Blade->Stella->TDS3→Ratan`, RATAN must query [[tdsx]] using the trade ID. It compares the cashflow payment date from SCBML with the payment-date schedules of both IRS legs. The source identifies these paths:

```text
First leg:
tradeData.tradeRecord.swapInstrument.iRLeg.firstLeg.periodicCashFlow.periodicAdjustedInterestPaymentDate

Second leg:
tradeData.tradeRecord.swapInstrument.iRLeg.secondLeg.periodicCashFlow.periodicAdjustedInterestPaymentDate
```

Where the expected counterpart cashflow does not exist for a payment schedule, RATAN should bypass `Pending Another Leg` and continue settlement processing. The wording of the schedule-match condition is ambiguous and requires confirmation in what is the authoritative stella tdx tdsx schedule lookup contract.

## Netting and Amendment Behaviour

For two coupons of the same IRS trade, auto-netting changes both component cashflows to `NETTED` and creates an intra-trade net resultant in `WAITING`. Resultants from separate IRS trades can subsequently be netted across trades; the prior intra-trade resultants become `DEAD` and a new cross-trade resultant is created.

A floating-leg re-fixing before payment release is intended to trigger automatic un-netting and re-netting. The withdrawn floating leg is cancelled, the prior resultant becomes `DEAD`, the fixed leg remains available for re-netting, and a revised resultant is created.

After the prior net resultant has been released or settled, a floating-leg withdrawal and replacement are assigned the `Cancel / Amend after payment release` exception and are NSTP. Operations must manually net the withdrawal and replacement to create the delta cashflow.

The source also permits manual cross-product netting of an IRS fixed leg in `WAITING` / `Pending Another Leg` with CDS cashflows. It does not define the treatment when the expected floating leg arrives later; this is tracked in what happens when a floating irs leg arrives after the fixed leg is manually netted with other products.

## Scope Boundary

The document explicitly marks user-driven “Unnet of a Net Cashflow” as not required for Day 1. This must remain separate from the described automated re-fixing un-netting behaviour.