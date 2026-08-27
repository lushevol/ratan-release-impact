---
type: source
title: Cash Settlement Home Page Static Data Functional Requirement
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, static-data, functional-requirement, ratan, settlement]
related: [cashflow-suppression-rules, nstp-rule-routing, netting-eligibility-static-data, cashflow-cutoff-static-data, vostro-data-sourcing-from-ssi-plus, rdm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data.md"]
---
# Cash Settlement Home Page Static Data Functional Requirement

## Scope

This functional requirement defines static-data-controlled behavior for the Cash Settlement Home Page, including cashflow suppression, NSTP exception routing, netting eligibility, Vostro sourcing, cutoff calculation, profile limits, and Currency Calendar dependencies.

The principal systems and platforms are [[entities/ratan]], [[entities/ssi-plus]], [[entities/murex-2-11]], [[entities/stella]], and [[entities/cash-settlement-home-page]]. Currency Calendar data is sourced from [[rdm]].

## Cashflow Suppression Rule

The rule owner profiles are `FMO_BR_MKR` and `FMO_BR_APR`. Creation, update, and deletion use a Maker/Checker process. Rules may be defined using any cashflow-level attributes.

The 2024 Drop 2 suppression inventory includes entity/counterparty combinations, portfolios, Murex 2.11 labels, trade purposes, port-to-port cashflows, non-FMRP entities, non-economic amendments, and products without settlement.

Representative source rules are preserved below:

```text
Entity.Booking_Entity_SCI_FMID==#Entity.Counterparty_SCI_FMID
```

```text
Trade_Purpose==XVA-Premium
```

```text
Trade_Purpose==Yearly-PL-Sweep
```

```text
Entity.Booking_Entity_SCI_FMID!=400001378&&Entity.Booking_Entity_SCI_FMID!=10020899&&Entity.Booking_Entity_SCI_FMID!=235003861&&Entity.Booking_Entity_SCI_FMID!=10078716&&Entity.Booking_Entity_SCI_FMID!=10036642&&Entity.Booking_Entity_SCI_FMID!=10062461&&Entity.Booking_Entity_SCI_FMID!=10032025&&Entity.Booking_Entity_SCI_FMID!=400054708&&Entity.Booking_Entity_SCI_FMID!=400054737&&Entity.Booking_Entity_SCI_FMID!=400054741&&Entity.Booking_Entity_SCI_FMID!=400057714&&Entity.Booking_Entity_SCI_FMID!=400075752&&Entity.Booking_Entity_SCI_FMID!=400085753&&Entity.Booking_Entity_SCI_FMID!=400090093&&Entity.Booking_Entity_SCI_FMID!=400095464&&Entity.Booking_Entity_SCI_FMID!=400130180&&Entity.Booking_Entity_SCI_FMID!=400130178&&Entity.Booking_Entity_SCI_FMID!=400185419&&Entity.Booking_Entity_SCI_FMID!=400193370&&Entity.Booking_Entity_SCI_FMID!=400209000&&Entity.Booking_Entity_SCI_FMID!=400218197&&Entity.Booking_Entity_SCI_FMID!=400220273&&Entity.Booking_Entity_SCI_FMID!=400229749&&Entity.Booking_Entity_SCI_FMID!=400516443&&Entity.Booking_Entity_SCI_FMID!=400516442&&Entity.Booking_Entity_SCI_FMID!=400667486&&Entity.Booking_Entity_SCI_FMID!=400677737&&Entity.Booking_Entity_SCI_FMID!=400683682&&Entity.Booking_Entity_SCI_FMID!=400798477&&Entity.Booking_Entity_SCI_FMID!=400899993&&Entity.Booking_Entity_SCI_FMID!=300036368&&Entity.Booking_Entity_SCI_FMID!=3&&Entity.Booking_Entity_SCI_FMID!=400452428&&Entity.Booking_Entity_SCI_FMID!=400451508&&Entity.Booking_Entity_SCI_FMID!=4&&Entity.Booking_Entity_SCI_FMID!=400960089&&Entity.Booking_Entity_SCI_FMID!=9&&Entity.Booking_Entity_SCI_FMID!=400093619&&Trade_Original_Source_System_Name!=LOANIQ
```

```text
Cashflow.Booking_System_Event==NonEcoAmend&&Cashflow.Cashflow_Event_Reason==Reversal
```

```text
Cashflow.Booking_System_Event==NonEcoAmend&&Cashflow.Cashflow_Event_Reason==Rebook&&Cashflow.Parent_Cashflow_State in ('READY-Pending Ack','CASHFLOW_SUPPRESSED-NA','RELEASED-NA','SETTLED-NA','NETTED-Released','NETTED-Settled')
```

The source states that no Swift Suppression Rule is required for cashflow migration Day 1. This is a migration-specific scope statement and does not remove the need to process cashflows that are otherwise Swift-suppressed.

## NSTP Rule

NSTP rules use arbitrary cashflow-level attributes and are maintained through Maker/Checker creation, update, and deletion. The output model is:

| Content | Exception Code | Operation Level | Exception Category |
|---|---|---|---|
| `Settlement_Method==DVP` | `DVP` | `MAKER_CHECKER` | `NSTP` |
| `Cashflow.Booking_System_Event==ManualDeliver` | `Manual Deliver` | `MAKER_CHECKER` | `NSTP` |
| `Cashflow.Booking_System_Event==AmendmentError` | `AmendmentError` | `MAKER_CHECKER` | `NSTP` |
| `Cashflow.Is_Cashflow_Reinstate==true` | `ReInstate` | `MAKER_CHECKER` | `NSTP` |
| `Cashflow.Netting_Id!=empty` | `Net Cashflow` | `CHECKER_ONLY` | `OTHER` |
| `Cashflow.Is_Cashflow_Unnet==true` | `Previously Netted` | `CHECKER_ONLY` | `NSTP` |
| `Cashflow.Is_Cashflow_SettleAsGross==true` | `Settled as gross` | `CHECKER_ONLY` | `NSTP` |
| `Cashflow.Is_Adhoc_Net==true` | `Adhoc_Netting` | `CHECKER_ONLY` | `HIGH_RISK_NSTP` |
| `Cashflow.Netting_Id!=empty&&Cashflow.Cashflow_Event_Reason==Reversal_Rebook` | `NetOverAmend` | `CHECKER_ONLY` | `HIGH_RISK_NSTP` |
| `Cashflow.Is_Withdrawal_On_Component==true` | `Withdrawal on component` | `CHECKER_ONLY` | `HIGH_RISK_NSTP` |
| `Cashflow.Cashflow_Event_Reason==Reversal` | `Reversal` | `CHECKER_ONLY` | `HIGH_RISK_NSTP` |
| `Cashflow.Cashflow_Event_Reason==Rebook` | `Rebook` | `CHECKER_ONLY` | `HIGH_RISK_NSTP` |
| `Cashflow.Cashflow_Event_Reason==Reversal` | `reversal` | `MAKER_ONLY` | `NSTP` |
| `Cashflow.Cashflow_Event_Reason==Rebook` | `Rebook` | `MAKER_ONLY` | `NSTP` |
| blank condition | `High Value Payment` | `CHECKER_ONLY` | `NSTP` |
| blank condition | `Pending Affirmation` | `MAKER_ONLY` | `AFFIRMATION` |
| blank condition | `Back Value Date` | `MAKER_CHECKER` | `BACK_VALUE` |

The inventory also covers Stella Corporate CCS, portfolio reassignment/close-out, China FDL clients, Murex 2.11 CRD/IRS/commodity products, WHT clients, Corporate clients, and ad hoc-netting clients.

## Netting Eligibility Rule

Netting eligibility is maintained with Maker/Checker controls. Its configured data structure is:

| Attribute | Operator | Logical Model Field | Can Be Blank? | Sample |
|---|---|---|---|---|
| Booking Entity FMID/FM Code | IS | `Entity.Booking_Entity_SCI_FMID Entity.Booking_Entity_SCI_FMCODE` |  | `1007522 SCB LONDON*LDN` |
| Portfolio | IS |  | Y |  |
| Client FMID/FM Code | IS | `Entity.Counterparty_SCI_FMID Entity.Counterparty_SCI_FMCODE` |  | `10036739 BARCLAYS FX*LDN` |
| Product Type? | IS/IN | `Instrument_Common.CFI_Code Instrument_Common.ISDA_Taxonomy` | Y | `SRACCP InterestRate:CrossCurrency:Basis` |
| Currency | IS/IN | `Cashflow.Payment_Currency` | Y | `USD/Blank` |

The supplied CN Day1 rule is:

```text
Entity.Counterparty_SCI_FMID==400202766&&Cashflow.Netting_Id==null
```

Its stated reason is `Shanghai Clearing Hourse`. The requirement does not define whether a match means eligible, ineligible, or exception-routed.

## Vostro

Vostro data is sourced by [[entities/ratan]] through an API from [[entities/ssi-plus]] and is not stored locally in RATAN. For derivative products, relevant CFI codes are tagged against existing Security IDs in SSI+, allowing existing SSI records to feed both Murex 2.11 and RATAN.

## Cutoff

Cutoff static data is keyed by Legal Entity and Currency. The cutoff shifter and unit provide a backward shift for calculating the cutoff date, with examples such as `0` and `-1`. Cutoff time is a GMT time picked up directly for the cashflow. Queue shifter derives the Ratan-to-Razor release cutoff time from the calculated cutoff date and time.

The supplied text references a calculation result sample and cashflow migration Day 1 data, but does not include those records.

## Profile Limit

Profile limits use Maker/Checker maintenance. The structure is:

| Filed Name | Field Type | Comment |
|---|---|---|
| Limit | Numeric | Type in by user |
| Profile Name | Text | Type in by user |

The source references a profile-limit configuration image for cashflow migration Day 1.

## Currency Calendar

Currency Calendar data is sourced from [[rdm]]. The supplied document includes an image reference but does not specify the API, synchronization schedule, calendar semantics, or fallback behavior.

## Limitations and Open Issues

- Reversal and rebook NSTP rules appear with conflicting operation levels and categories.
- Several NSTP rows have blank conditions.
- Both `Data_Flow.Data_Source_System` and `Cashflow.Data_Flow__Data_Source_System` appear as field names.
- Scientific-notation rule identifiers may be spreadsheet display artifacts.
- Large FMID and shortcode lists require authoritative ownership, effective dating, and audit controls.
- Referenced images and `Cashflow Migration Business Rules.xlsx` are not available in the supplied text.