---
type: source
title: Investigate SCI Response Data - eueNotice
authors: []
year: 2025
url: ""
venue: ""
tags: [ratan, sci, counterparty-data, trade-validation, schema-change, eue-notice]
related: [ratan, sci, ratanone-data-ambassador, ratanone-trade-service, ratanone-rule-service, sci-regulatory-field-schema-deprecation, eue-notice-trade-validation-rule-dependency, what-is-the-rule-engine-behavior-when-lds-eue-notice-is-absent, which-ratan-consumers-use-smallbankexem-or-cftcclearingexemption, does-cashflow-blotter-or-any-other-frontend-consume-euenotice, what-is-the-impact-status-of-ratan-cash-settlement-query-service]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md"]
---
# Investigate SCI Response Data - eueNotice

## Summary

This investigation assesses the effect on RATAN of SCI changes to legal-entity Dodd-Frank data. The demonstrated material dependency is on `eueNotice`: the `ratanone-trade-service` invokes `ratanone-rule-service` for `TRADE_VALIDATION`, and two `FO_SUPERVISION` rules explicitly evaluate the propagated `Lds_Eue_Notice` fact.

The source establishes that `Lds_Eue_Notice` can currently be present with a `null` value. It does not establish whether a field omitted after SCI schema removal has equivalent rule-engine semantics. The supplied Cashflow Blotter GraphQL queries do not request any changed field and are assessed as having no direct impact. Other no-impact assessments are preliminary where no code or field-level evidence is provided.

## SCI schema changes

| Field Name | Level 1 | Level 2 | Attribute Name | Impact Description |
| --- | --- | --- | --- | --- |
| EUE notice | legalEntity | doddFrankDetails | eueNotice | To be removed from the Schema |
| Small Bank Exemption | legalEntity | doddFrankDetails | smallBankExem | To be removed from the Schema |
| CFTC Clearing Exemption | legalEntity | doddFrankDetails | cftcClearingExemption | Additional LOVs to be added to this attribute. |

## Service impact assessment

| Impact | Service | API or component | Recorded assessment |
| --- | --- | --- | --- |
| Y | [[ratanone-data-ambassador]] | `/v1/counterparty` | Counterparty data path used by [[ratanone-trade-service]] trade validation. |
| No | `ratan-cashflow-lifecycle-service` | `counterPartyService.getValueMapByDQSL` | Marked as unaffected. |
| No | `ratan-cash-settlement-ssi-stamping-service` | `DataAmbassdorClient.fetchCounterParties`; `TradeStampingService.findFMCodes` | Marked as unaffected. |
| No | `ratanone-swift-service` | Service | Marked as unaffected. |
| No ?? | `ratan-cash-settlement-query-service` | Service | Assessment remains unresolved. |
| No | `ratanone-foundation` | Service/library | Marked as unaffected. |
| Y | [[ratanone-rule-service]] | `ratanone_rule_service.ratan_scbml_field_rest_config` | Used when the rule engine considers a counterparty field absent; source notes “v3 validate/ no impact”. |
| No | [[ratanone-data-ambassador]] | Cashflow Blotter GraphQL trades, trade headers, and cashflows query | Marked as unaffected. |
| No | [[ratanone-data-ambassador]] | Cashflow Blotter Counterparty Detail `fmEntity` GraphQL query | Marked as unaffected. |
| Pending | Frontend | Confirmation from Judy | Source records that confirmation is awaited. |

## Demonstrated validation path

`ratanone-trade-service` invokes rule validation as follows:

```java
List<ResponseOfValidationMultiRuleType> ruleSvcResponse =
    ruleService.validate(
        context.getTradeDto(),
        TRADE_VALIDATION_BUSINESS_FLOW,
        SUB_BUSINESS_FLOWS);
```

The supplied `TRADE_VALIDATION` payload includes the EUE notice fact:

```json
{
  "businessFlow": "TRADE_VALIDATION",
  "message": {
    "additionalFacts": {
      "Custom__CounterParty": {
        "Legal_Entity_Main_Profile": {
          "LMP_Dodd_Stat": {
            "Lds_Us_Party_Ind": "N",
            "Lds_Eue_Notice": null
          }
        }
      }
    },
    "ruleTypeList": [
      "DETECTIVE",
      "FO_SUPERVISION",
      "CONTROL_MONITORING"
    ]
  }
}
```

This provides evidence for the propagation chain:

`SCI legalEntity.doddFrankDetails.eueNotice` → [[ratanone-data-ambassador]] counterparty data → validation facts → [[ratanone-rule-service]] rule evaluation.

## Rule-engine evidence

The source identifies two `TRADE_VALIDATION` / `FO_SUPERVISION` records:

```text
7322836024697135104  TRADE_VALIDATION  FO_SUPERVISION
7322837366211096576  TRADE_VALIDATION  FO_SUPERVISION
```

The searches used to locate them were:

```sql
select * from ratanone_rule_service.ratan_rule_engine a
where lower(a.user_rule) like '%notice%';

select * from ratanone_rule_service.ratan_rule_engine a
where lower(a.running_rule) like '%notice%';
```

The recorded rule expressions are:

```text
Data_Flow__Data_Source_System in ("Murex", "Blade") && Instrument_Common__ISDA_Taxonomy in ("InterestRate:FRA", "InterestRate:IRSwap:Basis", "InterestRate:IRSwap:OIS", "InterestRate:IRSwap:FixedFixed", "InterestRate:IRSwap:FixedFloat") && Physical_Status == "Live" && Trade_Date >= "2016-01-01" && Clearing_Status != "Registered" && Entity__Booking_Entity_Id != "SYDNEY" && Trade_Strategy not in ("IR_FWD_BOND_CS", "CR_TRS_FND_B", "CR_TRS_PFND_LCY", "CR_LOANINS", "IR_DEPO_MC_LOAN", "CR_TRS_UNFND_B", "IR_ZCINFSWAP", "CR_TRS_PFND_B", "CR_TRS_PFND_BS", "IR_IRS_MC", "IR_INFYOYSWAP", "IR_ZCINFOPT", "IR_INFYOYOPT", "IR_IRS_CALL", "IR_DEPO_STRUCT", "CR_TRCLI", "COM_OUTRGHT_DVP", "CR_RTM_CCS", "CR_REPO_TOPUP", "IR_CF_KOCAP", "IR_TRS_UNFND_B", "IR_XSW_COMMIT") && Instrument_Common__Source_System_Instrument_Id != "USD SOFR TERM" && (Swap_Instrument__IR_Leg__First_Leg__Notional_Amount_Currency == "MXN" || Forward_Future_Instrument__Notional_Amount_Currency == "MXN" || Swap_Instrument__IR_Leg__Second_Leg__Notional_Amount_Currency == "MXN") && Entity__Counterparty_Name not in ("ICECLEARASC/ATL", "LCH/LDN", "CMECCP/WMN", "SCBOTCCCP/HKG", "JSCC/TYO", "EUREXCAGCCP/FRA", "CCPLCHEDIPH/LDN", "LCHCLE/LDN") && Custom__CounterParty__Legal_Entity_Main_Profile__LMP_Inc_Cntry_Iso_Code == "MX" && Custom__CounterParty__Legal_Entity_Main_Profile__LMP_Dodd_Stat__Lds_Eue_Notice != "Y" && (Instrument_Common__Source_System_Instrument_Type not matches ".*Early_Term" && Instrument_Common__Source_System_Instrument_Type not matches ".*Structured Swap" && Instrument_Common__Source_System_Instrument_Type not matches ".*LNBR_ASIA" && Instrument_Common__Source_System_Instrument_Type not matches ".*Structured Deposit") && (Source_System_System_Date equals $CURRENT_DATE || Source_System_System_Date isAfter $CURRENT_DATE)
```

```text
Data_Flow__Data_Source_System in ("Murex", "Blade") && Instrument_Common__ISDA_Taxonomy in ("InterestRate:FRA", "InterestRate:IRSwap:Basis", "InterestRate:IRSwap:OIS", "InterestRate:IRSwap:FixedFixed", "InterestRate:IRSwap:FixedFloat") && Physical_Status == "Live" && Trade_Date >= "2016-01-01" && Clearing_Status != "Registered" && Entity__Booking_Entity_Id != "SYDNEY" && Trade_Strategy not in ("IR_FWD_BOND_CS", "CR_TRS_FND_B", "CR_TRS_PFND_LCY", "CR_LOANINS", "IR_DEPO_MC_LOAN", "CR_TRS_UNFND_B", "IR_ZCINFSWAP", "CR_TRS_PFND_B", "CR_TRS_PFND_BS", "IR_IRS_MC", "IR_INFYOYSWAP", "IR_ZCINFOPT", "IR_INFYOYOPT", "IR_IRS_CALL", "IR_DEPO_STRUCT", "CR_TRCLI", "COM_OUTRGHT_DVP", "CR_RTM_CCS", "CR_REPO_TOPUP", "IR_CF_KOCAP", "IR_TRS_UNFND_B", "IR_XSW_COMMIT") && Instrument_Common__Source_System_Instrument_Id != "USD SOFR TERM" && ((Swap_Instrument__IR_Leg__First_Leg__Notional_Amount_Currency in ("USD", "EUR", "GBP", "JPY", "AUD", "MXN", "NOK", "PLN", "SEK", "CAD", "HKD") || Forward_Future_Instrument__Notional_Amount_Currency in ("USD", "EUR", "GBP", "JPY", "AUD", "MXN", "NOK", "PLN", "SEK", "CAD", "HKD") || Swap_Instrument__IR_Leg__Second_Leg__Notional_Amount_Currency in ("USD", "EUR", "GBP", "JPY", "AUD", "MXN", "NOK", "PLN", "SEK", "CAD", "HKD")) || (Instrument_Common__ISDA_Taxonomy in ("InterestRate:IRSwap:Basis", "InterestRate:IRSwap:OIS", "InterestRate:IRSwap:FixedFixed", "InterestRate:IRSwap:FixedFloat") && Trade_Date >= "2018-10-14" && ((Swap_Instrument__IR_Leg__First_Leg__Leg_Type matches "Fixed.*" && Swap_Instrument__IR_Leg__Second_Leg__Leg_Type not matches "Fixed.*") || (Swap_Instrument__IR_Leg__First_Leg__Leg_Type not matches "Fixed.*" && Swap_Instrument__IR_Leg__Second_Leg__Leg_Type matches "Fixed.*")) && (Swap_Instrument__IR_Leg__First_Leg__Notional_Amount_Currency in ("SGD", "CHF") || Swap_Instrument__IR_Leg__Second_Leg__Notional_Amount_Currency in ("SGD", "CHF")))) && Entity__Counterparty_Name not in ("ICECLEARASC/ATL", "LCH/LDN", "CMECCP/WMN", "SCBOTCCCP/HKG", "JSCC/TYO", "EUREXCAGCCP/FRA", "CCPLCHEDIPH/LDN", "LCHCLE/LDN") && Custom__CounterParty__Legal_Entity_Main_Profile__LMP_Dodd_Stat__Lds_Us_Party_Ind in ("Y", "Q") && Custom__CounterParty__Legal_Entity_Main_Profile__LMP_Dodd_Stat__Lds_Eue_Notice != "Y" && (Instrument_Common__Source_System_Instrument_Type not matches ".*Early_Term" && Instrument_Common__Source_System_Instrument_Type not matches ".*Structured Swap" && Instrument_Common__Source_System_Instrument_Type not matches ".*LNBR_ASIA" && Instrument_Common__Source_System_Instrument_Type not matches ".*Structured Deposit") && (Source_System_System_Date equals $CURRENT_DATE || Source_System_System_Date isAfter $CURRENT_DATE)
```

Both rules apply to eligible trades sourced from [[murex]] or [[blade]] and contain:

```text
Custom__CounterParty__Legal_Entity_Main_Profile__LMP_Dodd_Stat__Lds_Eue_Notice != "Y"
```

## Cashflow Blotter GraphQL evidence

The supplied Counterparty Detail query requests the following Dodd-Frank fields:

```graphql
doddFrankDetails {
  dfComplaint
  doddFrankEntityTypeValue
  usPerson
  tradestatusvalue
  intialMarginMethod
}
```

It does not request `eueNotice`, `smallBankExem`, or `cftcClearingExemption`. This supports a no-direct-impact conclusion only for the documented GraphQL queries, not for all frontend clients or cached schemas.

## Implications

Before SCI removes `eueNotice`, the owning teams should establish whether the compatibility mapping remains available, replace or retire the two identified rules, and test absent-field evaluation separately from the observed `null` state. The source supplies no direct consumption evidence for `smallBankExem` or `cftcClearingExemption`; this is an incomplete investigation rather than evidence of no impact.