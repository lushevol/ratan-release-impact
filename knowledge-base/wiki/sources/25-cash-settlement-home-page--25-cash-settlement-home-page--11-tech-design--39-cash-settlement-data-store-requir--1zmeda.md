---
type: source
title: Cash Settlement Data Store Requirements
authors: []
year: 2026
url: ""
venue: Internal technical requirements document
tags: [cash-settlement, postgresql, data-store, requirements, cashflow, high-availability]
related: [postgresql, cash-settlement-platform, camunda, cashflow-lifecycle-service, domain-owned-postgresql-schemas, cash-settlement-cashflow-read-model, postgresql-global-replication-and-continuous-consistency, what-is-the-approved-postgresql-replication-and-failover-topology, what-is-the-canonical-cashflow-storage-and-history-model]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Data Store Requirements.md"]
---
# Cash Settlement Data Store Requirements

This early-stage requirements document proposes PostgreSQL as the primary datastore for the [[cash-settlement-platform]]. It defines domain-owned storage categories, illustrates a broad cashflow read model, and states must-have requirements for replication, availability, and real-time consistency. It does not select a replication topology, define measurable availability objectives, or resolve retention and canonical-data-model questions.

## Storage Requirements

| # | Title | User Story | Owner | Type | Retention | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cashflow | Users need to view all payments and go into details on demand, as well as history query 1. Economics 2. Payment status 3. SSI information 4. Downstream processing message, like FMSRE | Cashflow Lifecycle Service | Storage | | |
| 2 | Camunda native data | Camunda will be the workflow to orchestration settlement processing, native storage required, tables start with "act_" | Settlement Orchestration | Storage | | |
| 3 | Suppression rules | Users need a self defined rules on cashflow suppression | Suppression Service | Storage | Forever | |
| 4 | Processed raw messages | Keep the messages on concerned events received from STELLA | Payment Lake Service | Storage | | |
| 5 | Audit | Users need to view the audit history on the manual review process as well as automated events | Audit Service | Storage | | |
| 6 | User login/logout audit | Group level requirement | Audit Service | Storage | | |
| 7 | Exception | Exceptions occurred during the processing | Exception Service | Storage | | |
| 8 | Customized filters/views | User need to create self-defined filters and views for blotter querying and searching | BFF | Storage | Forever | |
| 9 | SWIFT messages | SWIFT messages need to be displayed | SWIFT processing Service | Storage | | |
| 10 | | | | | | |

The proposed ownership model is described by [[domain-owned-postgresql-schemas]]. The document does not establish whether these owners use schemas in one cluster, separate databases, or separate PostgreSQL instances.

## PostgreSQL Requirements

| # | Title | User Story | Importance | Notes |
| --- | --- | --- | --- | --- |
| 1 | Global Replication | Writes to one instance should be automatically propagated to other instances. | Must Have | |
| 2 | High Availability | DB instance DR will be transparent to us, failure on DB operation is not accepted. | Must Have | |
| 3 | Continuous Consistency | Data should be in sync in real time | Must Have | |

These are requirements rather than an approved architecture. The source does not define RPO, RTO, replication lag, number or location of instances, quorum, failover authority, read/write routing, network-partition behavior, or whether consistency means synchronous commit, read-after-write consistency, or another guarantee. See [[postgresql-global-replication-and-continuous-consistency]] and [[what-is-the-approved-postgresql-replication-and-failover-topology]].

## Cashflow Sample Data

The source includes `attachments/SampleJsonForCashflow.json`, illustrating the read-model breadth expected for a cashflow: trade identity and versions, data-flow metadata, settlement instructions and account-routing details, instrument and entity data, portfolio data, cashflow status, dates, payment economics, and netting fields.

```json
{
  "Delivery_Method":"",
  "Trade_State":"TOBESENT",
  "Cashflow_Sub_Status_Type":null,
  "Parent_Trade_Id":"3294505081",
  "Trade_Lake_Transaction_From_Date_Time":"2022-10-12T02:24:03.692Z",
  "Trade_Id":"3294505081",
  "Cashflow_Sub_Status":null,
  "Trade_Lake_Valid_To_Date_Time":"9999-12-31T00:00:00Z",
  "Cashflow_Sub_Status_Updater":null,
  "Trade_Lake_Latest_Event_Date_Time":null,
  "Data_Flow":{
    "Data_Publication_Date_Time":"2022-10-12T02:23:17Z",
    "Data_Type":"CashflowData",
    "Data_Source_System_Domain_Name":"FM",
    "Unique_Identifier_Message_Id":null,
    "Data_Source_System_Country_Code":"ALL",
    "Data_Source_System":"Stella",
    "Data_Publication_Id":"71f2132e-04da-4539-8015-7f474b6c4be8-2_1001",
    "Data_Sender":"STELLA"
  },
  "Trade_Version":"4",
  "Settlement_Instruction":{
    "Sender_To_Receiver_Information_1":"",
    "Remittance_Information_1":"",
    "Swift_Payment_Method":"",
    "Swift_Message_Type":"",
    "Nostro_Swift_Message_Type":"",
    "SSI_Unique_Id":"",
    "Is_Third_Party_Payment":"",
    "SSI_Priority":"",
    "SSI_Source":"",
    "Charge_Bearer":"",
    "Account":{
      "Intermediary_Account_Number":"",
      "Beneficiary_Account_Number":"",
      "Beneficiary_Bank_BIC_code":"",
      "Beneficiary_Correspondent_Account_Number":"",
      "Counterparty_CMS_Account_Number":"",
      "EBBS_Account_Number":"",
      "Intermediary_BIC_code":"",
      "Booking_Entity_Correspondent_Account_Number":"",
      "SCB_Nostro_Account_Number":"",
      "EBBS_Bridge_Account_Number":"",
      "Beneficiary_BIC_code":"",
      "Ordering_Customer_Account_Number":"",
      "Ordering_Customer_BIC_Code":"",
      "SCB_Nostro_Account_Type":""
    }
  },
  "Instrument_Common":{
    "Parent_Trade_Instrument":null,
    "Source_System_Instrument_Sub_Type":"",
    "Equity_Instrument_Reference":null,
    "ISDA_Taxonomy":"ForeignExchange:Spot",
    "CFI_Code":"ForeignExchange:Spot"
  },
  "Entity":{
    "Counterparty_SCI_FMCODE":"UNILEVER NEPAL*KTM",
    "Counterparty_CIF_Code":"",
    "Counterparty_SCI_FMID":"400594382",
    "Booking_Entity_General_Ledger_Business_Unit_Id":"236",
    "General_Ledger_Business_Unit_Name":null,
    "Booking_Entity_SCI_FMCODE":"NEPAL GRINDLAYS*KTM",
    "Counterparty_Source_System_Entity_Id":"",
    "Booking_Entity_SCI_FMID":"400007847"
  },
  "Trade_Lake_Transaction_To_Date_Time":"9999-12-31T00:00:00Z",
  "Position_Id":"3294505082",
  "Settlement_Method":"",
  "Trade_Lake_Raw_Event_Date_Time":null,
  "Cashflow":{
    "Cashflow_Affirmation_Status":null,
    "Payer_Name":null,
    "Bypass_Workflow_Indicator":null,
    "Payment_Type":"Cashflow",
    "Is_STP":"false",
    "NSTP_Reason":null,
    "Payment_Date":"2020-07-20T00:00:00Z",
    "Payment_Receiver_Party_Reference":"party2",
    "Cashflow_Ratan_Internal_Version":null,
    "Cashflow_Business_Version":"N/A",
    "Netting_Cutoff_Date":null,
    "Status_Event_Type":"",
    "Payment_Date_Business_Day_Convention":"NONE",
    "Pay_Receive_Indicator":"Pay",
    "STP_Cutoff_Date_Time":null,
    "Next_Cashflow_Id":null,
    "Netting_Id":"",
    "Is_Private_Banking_Cashflow":"false",
    "Payment_Amount":"1111100.0",
    "Payment_Cutoff_Time":null,
    "Cashflow_Version":"1",
    "Validation_Status":null,
    "Cashflow_Id":"003294505082",
    "Cashflow_Event_Type":"Withdrawal",
    "Cashflow_Minor_Version":null,
    "Cashflow_State":"SUPPRESSED",
    "Prev_Cashflow_Id":null,
    "Is_Cashflow_Unnet":"false",
    "Is_STP_Ratan":null,
    "Payment_Payer_Party_Reference":"party1",
    "Minor_Version_Description":null,
    "Payment_Currency":"USD",
    "Event_Date":"2022-10-12T00:00:00Z",
    "Is_Amended_Post_Settlement":"false",
    "Adjusted_Payment_Date":"2022-10-12T00:00:00Z",
    "Payment_Version":"1"
  },
  "BCS_Parent_Trade_Id":"",
  "Trade_Lake_Valid_From_Date_Time":"2022-10-12T02:23:17Z",
  "BCS_Trade_Id":"",
  "Portfolio":{
    "Booking_Entity_Trade_Portfolio_Unique_Name":"SABRE||STL-FXFW-NP-NPR",
    "Booking_Entity_Trade_Portfolio_Name":"STL-FXFW-NP-NPR"
  }
}
```

The sample is illustrative, not a finalized persistence or API schema. In particular, it represents values such as `Is_STP`, `Is_Cashflow_Unnet`, and `Payment_Amount` as strings, leaving canonical data types and nullability unresolved.

## GraphQL Attachment

The attached GraphiQL endpoint demonstrates a paginated cashflow query:

```graphql
cashflows(
  filter: [
    {
      field: "Cashflow.Cashflow_Id"
      operator: IN
      values: ["003294505060", "003294505082", "003294505083"]
    }
  ]
  page: 0
  size: 50
) {
  pageInfo {
    totalHits
    pageNo
    pageSize
    lastPage
  }
  results {
    ...
  }
}
```

The attachment demonstrates nested-field filtering, `IN` filtering, page-number pagination, and a nested result structure. It does not establish an approved production API contract, authorization model, sort semantics, maximum page size, or performance target.

## Gaps Requiring Resolution

- Retention is specified only as “Forever” for suppression rules and customized filters/views.
- The authoritative cashflow ownership, versioning, and history model is unspecified.
- No data-access, cross-schema foreign-key, migration, backup, or restore policy is defined.
- The Questions and Not Doing sections are placeholders and record no decisions or scope exclusions.
- The source’s availability requirement is absolute, but no measurable acceptance criteria are provided.

See [[what-is-the-canonical-cashflow-storage-and-history-model]] for the cashflow-model decision and [[what-is-the-approved-postgresql-replication-and-failover-topology]] for the availability design decision.