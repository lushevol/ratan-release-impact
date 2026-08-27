---
type: source
title: FMRP - SSI Stamping Flow
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, ssi, settlement-instructions, cashflow-stamping, functional-requirement]
related: [ratan, ssi-plus, dqsl, scbml, ratan-ssi-stamping, vostro-nostro-ssi-selection, ssi-maker-checker-remediation, adhoc-ssi-exception-workflow, ssi-effective-date-selection, cover-payment-and-mt103-serial-routing, scbml-ssi-field-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md"]
---
# FMRP - SSI Stamping Flow

This functional requirement specifies how [[ratan]] selects Vostro and Nostro settlement instructions from SSI data, stamps cashflows, handles SSI exceptions, enriches confirmation documents and SCBML, and re-stamps impacted cashflows after effective-dated SSI updates.

## Core processing requirement

For SCB Pay cashflows, RATAN must query Vostro SSI first. It then uses the selected Vostro settlement means and settlement account to query Nostro SSI. If that Nostro query is blank, RATAN uses a default Nostro. If no Vostro is stamped, RATAN queries default Nostro using Legal Entity and Currency.

| Vostro query result | Nostro query result | API response | Confirmation document result |
| --- | --- | --- | --- |
| Missing Vostro | Missing Nostro | `"vostroResult": "MISSING_VOSTRO_ERROR", "nostroResult": "MISSING_NOSTRO_ERROR"` | Party A and Party B account information is `Please advise`. |
| Multi Vostro | Missing Nostro | `"vostroResult": "MULTI_VOSTRO_ERROR", "nostroResult": "MISSING_NOSTRO_ERROR"` | Party A and Party B account information is `Please advise`. |
| Good Vostro | Missing Nostro | `"vostroResult": "SUCCESS", "nostroResult": "MISSING_NOSTRO_ERROR"` | Enrich Party A; Party B account information is `Please advise`. |
| Good Vostro | Good Nostro | `"vostroResult": "SUCCESS", "nostroResult": "SUCCESS"` | Enrich Party A and Party B account information. |

## SSI query configuration

The following example is source-specific and must not be treated as a universal RATAN query configuration.

```javascript
{field: "Settlement_Instruction.BranchId_Murex3Id", operator: IN, values: ["NEPAL GRINDLAYS*KTM","Global"] }, //booking entity fmcode
 {field: "Settlement_Instruction.Payment_Currency", operator: IN, values: ["NPR"] }, //payment currency
 {field: "Settlement_Instruction.CFI_Code", operator: IN, values: ["JF****","*F****","******"] }, //CFI code, **Xpath changed**, 2026-06-26 : TDS3Data.cashFlowData[*].cashFlowRecord.Instrument_Common.**CFI_Code** → TDS3Data.cashFlowData[*].cashFlowRecord.Instrument_Common.**Financial_Instrument_Code**
 {field: "Settlement_Instruction.Counterparty_SCI_FMID", operator: IN, values: ["400419550"] },//counterparty FMID
 {field: "Settlement_Instruction.Debit_Credit", operator: IN, values: ["Both","Credit"] }, //or [ Both, Debit]
 {field: "Settlement_Instruction.Settlement_Type", operator: IN, values: ["CASH”] },
{field: "Settlement_Instruction.Settlement_Method", operator: IN, values: ["CASH”,"FEDWIRE"] }, //if cashflow settlement method is Cash, Gross, "", query with ["CASH”,"FEDWIRE"], else CASH will be replaced by the settlement method value:  [{*settlement method*},"FEDWIRE"]
 {field: "Settlement_Instruction.SSI_Status", operator: IN, values: ["Active","New","Update"] },
```

The stated [[tds3]] CFI source-path change is dated `2026-06-26` and requires release-date confirmation.

## Selection and exception requirements

- Non-UK matching prioritizes CFI specificity, followed by primary/secondary and branch scope; the detailed priority table instead orders country/global scope before primary/secondary.
- London (FMID `10075222`) and SSTL (FMID `400041070`) use a separate branch-first hierarchy.
- Vostro-related exceptions use maker/checker handling. SCB Pay validates both Vostro and Nostro and compares settlement account and settlement means; SCB Receive validates Nostro only.
- Manual entry of field 54 disables field 56, and manual entry of field 56 disables field 54.
- Cover-payment conditions require `<scb:swiftPaymentMethod>Cover</scb:swiftPaymentMethod>`.

See [[ratan-ssi-stamping]], [[vostro-nostro-ssi-selection]], [[ssi-maker-checker-remediation]], and [[cover-payment-and-mt103-serial-routing]].

## Effective-date rule

```text
If End_EffectiveDate is not blank:
    If VD <= End_EffectiveDate: take this SSI
    Else: drop the SSI

Else if Start_EffectiveDate is not blank:
    If VD >= Start_EffectiveDate: take this SSI
    Else: drop the SSI

Else if both Start_EffectiveDate Start_EffectiveDate are blank:
    take this SSI

Else take the SSI
```

SSI+ publishes an end-dated old record and a start-dated new record with an `_ED` suffix to [[dqsl]] and Elastic Search. RATAN must apply the rule to automatic stamping and Vostro exception candidate queries, then re-trigger stamping for impacted cashflows after an SSI update.

## Implementation caveats

The source contains unresolved terminology and technical defects. In particular, it conflicts between `Multi Nostro` and `Multi Vostro`, provides inconsistent Missing Nostro UI behavior, uses several undefined stamping-event labels, and contains potentially malformed logical-model field names and SCBML paths. The mapping tables must be schema-validated before implementation. See the linked queries for required resolution.