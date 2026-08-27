---
type: source
title: Beneficiary BIC Netting
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, beneficiary-bic, Ratan, Murex]
related: [beneficiary-bic-netting, bic-net-eligibility-flag, paystp-net, netting-resultant-cashflow, bic-netting-un-netting, beneficiary-bic-netting-versus-bilateral-manual-netting, ratan, murex, sci, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting.md"]
---
# Beneficiary BIC Netting

## Purpose

This functional requirement defines a controlled manual Beneficiary BIC netting workflow in [[entities/ratan]]. The workflow is based on the existing [[entities/murex]] BAU process and is intended to let settlement operations filter, review, select, and net eligible cashflows directly from the [[entities/cashflow-blotter]].

The requirement emphasizes user control, segregation from bilateral manual netting, configurable eligibility data, resultant-cashflow lineage, client affirmation, maker-checker verification, and pre-release automatic un-netting.

## Functional requirements

1. Ratan should provide filter logic for Beneficiary BIC netting similar to Murex, including entity, value date, counterparty, and fields represented in `PAYSTP_NET`.
2. Ratan should validate that cashflows have the same BIC-net flag, Beneficiary BIC, value date, currency, and entity before allowing BIC netting.
3. The operations user decides which cashflows are netted together and assumes the associated operational risk.
4. Manual netting categories must be segregated. BIC netting has higher priority than bilateral manual netting.
5. `PAYSTP_NET` must be configurable by users.
6. Eligible cashflows should be updated to `Pending Netting`.
7. The Cashflow Blotter should provide a new `Ben BIC Netting` action.
8. The resultant cashflow ID should be displayed after execution.
9. The resultant cashflow requires client affirmation and maker-checker verification.
10. Ratan should automatically un-net the resultant cashflow when a withdrawal or amendment occurs before release.
11. The strategic solution requires SWIFT 192/292 messaging.

## Eligibility and source mapping

The Beneficiary BIC is the BIC code obtained from [[entities/sci]] where `mediumUsage='MXR'`.

```text
BIC_NET flag Logical Model: Entity.Counterparty_SCI_BIC_Net_Flag
BIC_NET flag Physical Model: /scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party2']/conf:bicNetFlag
```

The stated eligibility condition is:

```text
Entity = LONDON
BIC_Net = 'Y'
Cashflow.Cashflow_Sub_State_Type = 'Pending Netting'
```

The source shows `Payment Date >= Today` struck through. Its final applicability is therefore unresolved.

## Selection and netting key

The prototype requires selected cashflows to share:

- The same BIC-net flag
- The same Beneficiary BIC
- The same value date
- The same currency
- The same entity

The meeting minutes define the following expanded key:

```text
Entity/Currency/Value Date/Ben BIC/Family/Group/Type/Typology/Strategy
```

The source does not explicitly resolve whether the expanded fields replace the five-field prototype rule or additionally constrain the selection.

## Resultant cashflow generation

The source-prescribed generation contract is retained below.

| Logical model field | Generation logic | Comment |
|---|---|---|
| `Data_Flow.Unique_Identifier_Message_Id` | UUID | |
| `Execution_Date_Time` | latest time stmap | Source spelling preserved |
| `Cashflow.Cashflow_Id` | fix length 12: `'N' + 11 numeric` | |
| `Cashflow.Cashflow_Event_Type` | pre-config: `New` | |
| `Cashflow.Cashflow_State` | pre-config: `QUEUED` | |
| `Cashflow.Cashflow_Affirmation_Status` | pre-config: `Unaffirmed` | |
| `Cashflow.Cashflow_Sub_State` | pre-config: Blank | |
| `Cashflow.Cashflow_Sub_State_Updater` | pre-config: Blank | |
| `Cashflow.Cashflow_Sub_State_Type` | pre-config: Blank | |
| `Cashflow.Payment_Type` | pre-config: Blank | |
| `Cashflow.Netting_Id` | UUID | |
| **Counterparty FMID** | Randomly pick up | |
| **Counterparty Murex shortcode** | Consistent with cpty FMID | |
| **Family** | Inherit from component cashflow if the values are same; empty if values are different | |
| **Group** | Inherit from component cashflow if the values are same; empty if values are different | |
| **Type** | Inherit from component cashflow if the values are same; empty if values are different | |
| **Typology** | Inherit from component cashflow if the values are same; empty if values are different | |
| **Strategy** | Inherit from component cashflow if the values are same; empty if values are different | |
| **Trade_Id** | Inherit from component cashflow if the values are same; empty if values are different | |
| **Taxonomy** | Restamp according to current family/group/type/typology/strategy | |
| **CFI Code** | Restamp according to current family/group/type/typology/strategy | |
| **Settlement Method** | Pre-config: `GROSS` | |
| **Delivery Method** | Pre-config: `CASH` | |
| **Unspecified fields** | Pre-config: Blank | The source contains two unnamed “Pre-config: Blank” rows |
| `Parent_Trade_Id` | `NA` | |
| `Trade_State` | pre-config: `TOBESENT` | |
| `Cashflow.Cashflow_Version` | Pre-Config: `0` | |
| `Cashflow.Cashflow_Business_Version` | Pre-Config: `0` | |
| `Cashflow.FMO_Comment` | Pre-config: Blank | |
| `Cashflow.FMO_Comment_Updater` | Pre-config: Blank | |
| `Cashflow.FMO_Comment_Timestamp` | Pre-config: Blank | |
| `Data_Flow.Data_Publication_Date_Time` | Latest timestamp | |
| **Other Attributes** | Copy from first cashflow | |

## BAU process

1. On VD-1, the operations user enters the `LDN: CR CPTY NET` payment queue, where eligible Beneficiary BIC netting payments are loaded.
2. The operations user selects the BIC cashflows and saves. The system nets them using entity, currency, value date, and Beneficiary BIC.
3. Operations takes the resultant payment and obtains client affirmation.
4. The payment moves through maker-checker queues: maker `INIT` to `CHCK`, then checker `CHCK` to `SNET`.
5. If the client disputes the resultant payment, settlement operations manually un-nets it and returns to the BIC netting queue if another netting operation is required.
6. A post-settlement trade amendment by Middle Office may require different handling; the source does not define the authoritative rule.

## BAU problems

The source identifies several operational problems:

- Newly onboarded give-up counterparties may not be added to `PAYSTP_NET` in time.
- Missing counterparties can produce settlement amount mismatches.
- Users may manually net cashflows across bilateral and BIC-based queues.
- Cashflows may need suppression and manual payment through OSCAR.
- Missing Swift BIC data in Murex can require payment outside Murex.
- Delayed UDF updates can create Gross/Net issues.

## Open specification issues

- The five-field prototype key conflicts with the nine-field meeting-minutes key.
- The meeting minutes describe the resultant as `NSTP/Pending Affirmation`, while the generation table specifies `QUEUED`, `Unaffirmed`, and blank sub-state fields.
- The source does not define how `PAYSTP_NET` is reconciled with SCI when their data disagrees.
- “Randomly pick up” is not a deterministic or auditable Counterparty FMID assignment rule.
- The source does not define technical locking or reservation to enforce BIC-netting priority.
- Post-release amendment and settlement-finality behavior remains unspecified.