---
type: source
title: "Cash Settlement Home Page — Functional Requirement — Netting — CCIL Netting"
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, CCIL, netting, Ratan, FMRP, India, IRS]
related: [ccil, ratan, murex-2-11, stella, scbml, ccil-guaranteed-and-non-guaranteed-netting, ccil-settlement-method-stamping, ccil-non-guaranteed-client-static-data, cashflow-logical-model, swift-versus-cashflow-suppression, cashflow-suppression-rules, maker-checker-settlement-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CCIL Netting.md"]
---
# Cash Settlement Home Page — Functional Requirement — CCIL Netting

## Scope

This functional requirement defines India cash-settlement handling for CCIL-related IRS cashflows in [[ratan]]. It covers guaranteed and non-guaranteed CCIL cashflows, NSTP holding, GUI and backend filtering, bilateral netting, a new CCIL Netting action, pre-netting review, settlement-method stamping, and resultant cashflow generation.

India was identified as an H1 2024 [[fmrp]] cashflow-migration market, and CCIL netting was mandatory. The strategic design was not expected to be ready for the release timeline, so the document specifies a tactical implementation based on Murex 2.11 static data and the MxML adaptor service.

## Business Context

Trades booked with CCIL counterparties are netted to a single cashflow facing the CCIL central counterparty. SWIFT generation is bypassed for the netting resultant, while accounting remains required.

- Guaranteed CCIL trades are cleared and novated to the CCIL central counterparty.
- Non-guaranteed CCIL trades are not cleared and retain their original counterparties, but their multi-component cashflows are operationally netted to a resultant facing CCIL.
- Ratan must hold both categories as NSTP, provide quick filters, support different netting actions, and provide a pre-netting review for discrepancies between SCB and CCIL netting results.

## Strategic and Tactical Approaches

The strategic approach requires a golden source for the non-guaranteed CCIL client list. stella identifies guaranteed and non-guaranteed CCIL cashflows and stamps `Settlement Method = CCIL`. Business rules stop STP, and Ratan provides filtering and netting capabilities.

The tactical approach copies Murex 2.11 CCIL client static data into Ratan logical static data. Ratan uses this local copy to identify non-guaranteed flows and stamp them with `Settlement Method = CCIL`. The copied data and classification logic are explicitly temporary and should be removed after Murex 2.11 decommissioning.

## Eligibility Matrix

### Bilateral Netting

| **Bilateral Netting Criteria** | **Conditions** | **Validation in GUI** | **Validation from backend** |
| --- | --- | --- | --- |
| Generic | Settlement Method != CCIL and Cashflow Status in (WAITING, READY) | Yes | Yes |
| CCIL Guaranteed | Settlement Method == CCIL and Cashflow Status in (WAITING) and sub status type =='Pending Netting' and Counterparty FMID ==400021949 | Yes | Yes |

### CCIL Netting

| **CCIL Netting Criteria** | **Conditions** | **Validation in GUI** | **Validation from backend** |
| --- | --- | --- | --- |
| Non Guaranteed | Settlement Method == CCIL and Cashflow Status in (WAITING) and sub status type =='Pending Netting' and Counterparty FMID !=400021949 | Yes | Yes |

## Tactical Settlement-Method Stamping Rule

The Murex 2.11-to-Ratan interface implements Rule 4.1 in the MxML adaptor service. The stated rule is:

```text
Entity.Booking_Entity_SCI_FMID == '4'
Instrument_Common.Murex_Product_Family=='IRD' and Instrument_Common.Murex_Product_Group=='IRS'
Entity.Counterparty_SCI_FMID is 400021949 or the FMID from the above non guaranteed CCIL client static data list
Cashflow.Payment_Currency is INO
```

The source uses `INO` as the payment-currency value; it does not define whether this is the authoritative internal representation or a mapping that requires confirmation.

## CCIL Netting Resultant

The new `CCIL Netting(Non Guaranteed)` action is restricted to eligible non-guaranteed cashflows. It creates a resultant facing CCIL central counterparty `400021949` with display shortcode `CCIL/MMB`.

| Logical model field | Generation Logic | Comment |
| --- | --- | --- |
| Data_Flow.Unique_Identifier_Message_Id | UUID | |
| Execution_Date_Time | latest time stmap | |
| Cashflow.Cashflow_Id | fix length 12: 'N' + 11 numeric | |
| Cashflow.Cashflow_Event_Type | pre-config: New | |
| Cashflow.Cashflow_State | pre-config: QUEUED | |
| Cashflow.Cashflow_Affirmation_Status | pre-config: Unaffirmed | |
| Cashflow.Cashflow_Sub_State | pre-config: Blank | |
| Cashflow.Cashflow_Sub_State_Updater | pre-config: Blank | |
| Cashflow.Cashflow_Sub_State_Type | pre-config: Blank | |
| Cashflow.Payment_Type | pre-config: Blank | |
| Cashflow.Netting_Id | UUID | |
| Entity.Counterparty_SCI_FMID | pre-config: 400021949 | |
| Entity.Counterparty_Murex_Display_Shortcode | pre-config: CCIL/MMB | |
| Settlement_Method | pre-config: CASH | |
| Delivery_Method | pre-config: CASH | |
| Trade_Id | Pre-config: Blank | |
| Pre-config: Blank | Pre-config: Blank | |
| Parent_Trade_Id | NA | |
| Trade_State | pre-config: TOBESENT | |
| Cashflow.Cashflow_Version | Pre-Config: 0 | |
| Cashflow.Cashflow_Business_Version | Pre-Config: 0 | |
| Cashflow.FMO_Comment | Pre-config: Blank | |
| Cashflow.FMO_Comment_Updater | Pre-config: Blank | |
| Cashflow.FMO_Comment_Timestamp | Pre-config: Blank | |
| Data_Flow.Data_Publication_Date_Time | Latest timestamp | |
| Other Attributes | Copy from first cashflow | |

## Operational Cases

Fully novated guaranteed cashflows use the existing bilateral netting action. Non-guaranteed cashflows use the new CCIL Netting action. A trade expected to be novated but still booked against its original counterparty intraday appears in the non-guaranteed population; pre-netting review is used to identify the discrepancy and request novation by MO.

Cash and Bond flows booked with FMID `400021949` are not required to net with guaranteed IRS cashflows. The formal eligibility matrix does not fully specify the product-level predicate behind this exclusion.

Operations may remove an eligible non-guaranteed cashflow from netting by using the existing `Settle as Gross` action. This requires an additional exception and four-eye validation.

For a newly onboarding CCIL client whose FMID is not yet in the static-data list, the temporary process is to add an NSTP rule, manually verify the Nostro account number, manually suppress SWIFT, request a permanent Ratan static-data update, and then remove the temporary NSTP rule.

## FMRP 8.0 Flow Updates

The source records two later flow requirements:

- Story `14473106` requires IRS-netting resultants `N1` and `N2` to enter `Pending Auto Netting`, hit the `CCIL Guarantee` rule, and produce a final `N3`.
- Story `15765034` requires Ratan Settlement to enrich some flows from `GROSS` to `CCIL`, allowing non-guaranteed flows to hit `CCIL Netting` and guaranteed flows to hit `CCIL Guarantee`.

In both examples, `N1` and `N2` become `DEAD` after the auto-netting job. The final `N3` is shown as `Gross`, `WAITING + Pending Exception`, and associated with exception code `Auto Netting - INO IRS`. The document does not define the complete resolution, accounting, or SWIFT-suppression lifecycle for this final state.

## Static Data Sample

The following is explicitly a sample and must not be treated as the complete authoritative client population.

| No | CCIL Member Id | Member Name | FMID | Shortname |
| --- | --- | --- | --- | --- |
| 1 | CCBNCNRB0011 | CANARA BANK | 155001698 | CANARA/MMB |
| 2 | CCBPHDFC0005 | HDFC BANK LIMITED | 130000556 | HDFC/MMB |
| 3 | CCBPICIC0049 | ICICI BANK LIMITED | 400006168 | ICICIBK/MMB |
| 4 | CCPDISEC0033 | ICICI SECURITIES PRIMARY DEALERSHIP LIMITED | 300036942 | ZICICI/MMB |
| 5 | CCBPIDBL0218 | IDBI BANK LTD | 400002527 | IDBIBK/MMB |
| 6 | CCBNSBIN0031 | STATE BANK OF INDIA | 400007691 | SBI/MMB |
| 7 | CCBPFDRL0020 | THE FEDERAL BANK LIMITED | 155001365 | FEDBK/CCN |
| 8 | CCBPRABL0129 | THE RATNAKAR BANK LTD. | 400199971 | RATBANK/KOH |
| 9 | CCBNUBIN0007 | UNION BANK OF INDIA | 155001352 | UBIN/MMB |
| 10 | CCBPUTIB0028 | AXIS BANK LTD | 155001402 | UTIB/MMB |

## Caveats

The source distinguishes input classification from resultant configuration: eligible inputs use `Settlement Method = CCIL`, while the manually generated non-guaranteed resultant uses `Settlement_Method = CASH`. Later FMRP auto-netting examples reclassify intermediate resultants as `CCIL` and show final resultants as `Gross`. A canonical lifecycle is not defined.

The source also leaves open ownership of tactical Ratan static data, the exact predicate excluding non-CCIL products booked with FMID `400021949`, the meaning of `INO`, and the resolution process for final `N3` exceptions.

## Related Wiki Topics

See [[ccil-guaranteed-and-non-guaranteed-netting]], [[ccil-settlement-method-stamping]], [[ccil-non-guaranteed-client-static-data]], and what is the canonical ccil resultant cashflow lifecycle.