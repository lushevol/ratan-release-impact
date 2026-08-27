---
type: source
title: PT-Ratan Expose the Cashflow Data to SSDR
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, SSDR, query-service, performance-testing, PostgreSQL, JSONB, indexing]
related: [ssdr, query-service, cash-settlement-query-cn-cashflow-data, wide-cashflow-read-projection-performance, jsonb-expression-indexed-query-performance, which-indexes-were-used-in-the-ssdr-cashflow-data-benchmarks, are-ssdr-and-query-service-date-status-and-counterparty-filters-semantically-equivalent, does-ssdr-cashflow-exposure-meet-its-required-latency-and-pagination-sla]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/PT-Ratan expose the cashflow data to SSDR.md"]
---
# PT-Ratan Expose the Cashflow Data to SSDR

This source provides DEV and load-test performance evidence for exposing `cashflow_data` to [[ssdr]] through [[query-service]]. It compares idle and high-load filtered queries, and broad cashflow projections retrieved through JSONB-based and physical-column APIs.

The results are evidence for the exact tested queries and environment, not a complete API contract, production SLA assessment, or index-design specification.

## SSDR and Query Service SQL

The SSDR-requested SQL is:

```sql
Select id , trade_id, trade_state, cashflow_index, cashflow_status, cashflow__cashflow_event_type
from cashflow_data
where VALUE_DATE >= ‘YYYY/MM/DD’
  and VALUE_DATE <= ‘YYYY/MM/DD’
  and STATUS <> ‘xxx’
  and counterparty in (XXXXX)
```

The SQL run in Query Service is:

```sql
Select id , trade_id, trade_state, cashflow_index, cashflow_status, cashflow__cashflow_event_type
from local_cash_settlement_query_cn.cashflow_data
where cashflow__payment_cutoff_time >= '2023-04-10'
  and cashflow__payment_cutoff_time <= '2023-04-10'
  and cashflow_status <> 'DEAD'
  and entity__counterparty_sci_fmid in ('400640613','400058400')
```

The document does not establish that `VALUE_DATE` and `cashflow__payment_cutoff_time`, `STATUS` and `cashflow_status`, or `counterparty` and `entity__counterparty_sci_fmid` are semantically equivalent. It also does not state whether `cashflow__payment_cutoff_time` is a date or timestamp, nor its timezone and inclusive-boundary semantics.

## Filtered-query measurements

The stated base contains 100,000 records. The source labels conditions as “query 10%” through “query 50%” but does not formally define whether these represent returned-record percentages, selectivity, or another test variable.

| Base records | Condition | Idle DB | High-load DB | High-load increase |
|---:|---:|---:|---:|---:|
| 100,000 | query 10% | 1,966 ms | 2,531 ms | 28.7% |
| 100,000 | query 20% | 2,345 ms | 4,068 ms | 73.5% |
| 100,000 | query 30% | 2,534 ms | 5,408 ms | 113.4% |
| 100,000 | query 40% | 3,028 ms | 8,731 ms | 188.3% |
| 100,000 | query 50% | 3,790 ms | 8,790 ms | 131.9% |

The source states that a busy database takes “60% more time.” The individual measurements do show slower high-load performance, but the observed increases range from 28.7% to 188.3%; therefore, 60% should not be used as a general rule.

## Wide-projection benchmark

The following query shape is a broad `LIMIT ... OFFSET 0` projection from `cash_settlement_query_cn.cashflow_data`, spanning Data Flow, Cashflow, Trade, Entity, Portfolio, Instrument Common, and Settlement Instruction fields. It has no `ORDER BY`, so it does not establish stable pagination or performance for non-zero offsets.

```sql
Select Data_Flow.Data_Source_System,Data_Flow.Data_Source_System_Country_Code,Data_Flow.Data_Source_System_Domain_Name,Data_Flow.Data_Type,Cashflow.Cashflow_Id,Cashflow.Cashflow_Version,Cashflow.Cashflow_Business_Version,Cashflow.Cashflow_State,Cashflow.Event_Physical_Status,Cashflow.Cashflow_Event_Type,Cashflow.Status_Event_Type,Cashflow.Event_Date,Cashflow.Payment_Payer_Party_Reference,Cashflow.Payment_Receiver_Party_Reference,Cashflow.Payment_Currency,Cashflow.Payment_Amount,Cashflow.Payment_Date,Cashflow.Payment_Date_Business_Day_Convention,Cashflow.Netting_Id,Instrument_Common.CFI_Code,Instrument_Common.ISDA_Taxonomy,Trade_State,Trade_Id,Cashflow.Position_Id,Parent_Trade_Id,Entity.Booking_Entity_SCI_FMID,Entity.Counterparty_SCI_FMID,Settlement_Method,Delivery_Method,Entity.Counterparty_SCI_FMCODE,Entity.Counterparty_CIF_Code,Entity.Counterparty_Source_System_Entity_Id,Cashflow.Pay_Receive_Indicator,Cashflow.Payer_Name,Cashflow.Is_Private_Banking_Cashflow,Cashflow.Is_Amended_Post_Settlement,Cashflow.Payment_Type,Cashflow.Is_Cashflow_Unnet,Cashflow.Transaction_Details,Data_Flow.Unique_Identifier_Message_Id,Execution_Date_Time,Entity.General_Ledger_Business_Unit_Name,Entity.Booking_Entity_General_Ledger_Business_Unit_Id,Trade_Lake_Valid_From_Date_Time,Trade_Lake_Valid_To_Date_Time,Trade_Lake_Latest_Event_Date_Time,Trade_Lake_Raw_Event_Date_Time,Trade_Lake_Transaction_From_Date_Time,Trade_Lake_Transaction_To_Date_Time,BCS_Parent_Trade_Id,BCS_Trade_Id,Trade_Version,Portfolio.Booking_Entity_Trade_Portfolio_Name,Cashflow.Cashflow_Affirmation_Status,Cashflow.Is_STP_RATAN,Cashflow.Is_STP,Cashflow.NSTP_Reason,Settlement_Instruction.Account.EBBS_Bridge_Account_Number,Settlement_Instruction.Account.EBBS_Account_Number,Settlement_Instruction.Account.Booking_Entity_Correspondent_BIC_code,Settlement_Instruction.Account.Booking_Entity_Correspondent_Account_Name,Settlement_Instruction.Account.Booking_Entity_Correspondent_Street_Address,Settlement_Instruction.Account.Booking_Entity_Correspondent_City,Settlement_Instruction.Account.Booking_Entity_Correspondent_Account_Number,Cashflow.Cashflow_Sub_State,Cashflow.Cashflow_Sub_State_Updater,Cashflow.Cashflow_Sub_State_Type,Cashflow.Prev_Cashflow_Id,Cashflow.Next_Cashflow_Id,Cashflow.Validation_Status,Cashflow.Exception_Reason,Cashflow.FMO_Comment,Cashflow.FMO_Comment_Updater,Cashflow.FMO_Comment_Timestamp,Cashflow.STP_Cutoff_Date_Time,Cashflow.Netting_Cuttoff_Date,Entity.Booking_Entity_SCI_FMCODE,Cashflow.Cashflow_Audit_Version,Cashflow.Payment_Cutoff_Time,Settlement_Instruction.Nostro_Swift_Message_Type,Cashflow.Minor_Version_Description,Cashflow.Bypass_Workflow_Indicator,Cashflow.Cashflow_Minor_Version,Settlement_Instruction.SSI_Unique_Id,Settlement_Instruction.SSI_Source,Settlement_Instruction.SSI_Priority,Settlement_Instruction.Swift_Message_Type,Settlement_Instruction.Account.SCB_Nostro_Account_Number,Settlement_Instruction.Account.SCB_Nostro_Account_Type,Settlement_Instruction.Account.Beneficiary_BIC_code,Settlement_Instruction.Account.Beneficiary_Account_Name,Settlement_Instruction.Account.Beneficiary_Account_Name_2,Settlement_Instruction.Account.Beneficiary_Street_Address,Settlement_Instruction.Account.Beneficiary_City,Settlement_Instruction.Account.Beneficiary_Account_Number,Settlement_Instruction.Account.Intermediary_BIC_code,Settlement_Instruction.Account.Intermediary_Account_Name,Settlement_Instruction.Account.Intermediary_Street_Address,Settlement_Instruction.Account.Intermediary_City,Settlement_Instruction.Account.Intermediary_Account_Number,Settlement_Instruction.Account.Beneficiary_Bank_BIC_code,Settlement_Instruction.Account.Beneficiary_Bank_Account_Name,Settlement_Instruction.Account.Beneficiary_Bank_Street_Address,Settlement_Instruction.Account.Beneficiary_Bank_City,Settlement_Instruction.Account.Beneficiary_Bank_Account_Number,Settlement_Instruction.Account.Beneficiary_Correspondent_BIC_code,Settlement_Instruction.Account.Beneficiary_Correspondent_Account_Name,Settlement_Instruction.Account.Beneficiary_Correspondent_Street_Address,Settlement_Instruction.Account.Beneficiary_Correspondent_City,Settlement_Instruction.Account.Beneficiary_Correspondent_Account_Number,Settlement_Instruction.Account.Ordering_Customer_BIC_Code,Settlement_Instruction.Account.Ordering_Customer_Account_Name,Settlement_Instruction.Account.Ordering_Customer_Street_Address,Settlement_Instruction.Account.Ordering_Customer_City,Settlement_Instruction.Account.Ordering_Customer_Account_Number,Settlement_Instruction.Remittance_Information_1,Settlement_Instruction.Remittance_Information_2,Settlement_Instruction.Remittance_Information_3,Settlement_Instruction.Remittance_Information_4,Settlement_Instruction.Sender_To_Receiver_Information_1,Settlement_Instruction.Sender_To_Receiver_Information_2,Settlement_Instruction.Sender_To_Receiver_Information_3,Settlement_Instruction.Sender_To_Receiver_Information_4,Settlement_Instruction.Sender_To_Receiver_Information_5,Settlement_Instruction.Sender_To_Receiver_Information_6,Settlement_Instruction.Account.Counterparty_CMS_Account_Number,Settlement_Instruction.Is_Third_Party_Payment,Settlement_Instruction.Swift_Payment_Method,Settlement_Instruction.Charge_Bearer,Instrument_Common.Source_System_Instrument_Sub_Type,Portfolio.Booking_Entity_Trade_Portfolio_Unique_Name,Entity.Person.Coverage_Marketer_PSID,Entity.Person.Event_Coverage_Marketer_PSID,Entity.Person.Execution_Marketer_PSID,Entity.Person.Event_Execution_Marketer_PSID,Entity.Person.Booking_Marketer_PSID,Entity.Person.Event_Booking_Marketer_PSID,Entity.Person.Trader_PSID,Entity.Person.Event_Trader_PSID,Trade.Event_Physical_Status,Resultant_Position_Id,Trade_Original_Source_System_Name,Cashflow.Is_Payment_Intent_To_Settle,Cashflow.Action_Type,Cashflow.Cashflow_Event_Reason,Settlement_Instruction.Value_Date,Settlement_Instruction.Value_Date_Business_Day_Convention,Instrument_Common.Financial_Instrument_Code,Cashflow.Cashflow_Major_Version,Cashflow.Cashflow_SubEvent_Type,Cashflow_Sequence,Effective_Date_Time,Entity.Booking_Entity_Country_ISO_Code,TP_System_Name,Trade_Purpose from cash_settlement_query_cn.cashflow_data  LIMIT  xxx OFFSET  0
```

### Average latency without index in DEV ENV

| Query Records Num | Average Query by Jsonb type (second) | Average Query by Column type (second) | Jsonb cost more time |
|---:|---:|---:|---:|
| 100 | 1.976 | 1.578 | 25% |
| 1000 | 9.888 | 3.686 | 168% |
| 2000 | 16.888 | 7.812 | 116% |
| 5000 | 85.012 | 16.29 | 422% |

### Individual runs without index in DEV ENV

| Query Records Num | Query by JsonB type (second) | Query by Column type (second) |
|---:|---:|---:|
| 100 | 2.09 | 1.677 |
| 100 | 1.963 | 1.2 |
| 100 | 1.937 | 1.679 |
| 100 | 1.943 | 1.667 |
| 100 | 1.947 | 1.669 |
| 1000 | 6.99 | 3.85 |
| 1000 | 6.85 | 3.43 |
| 1000 | 15.23 | 3.48 |
| 1000 | 9.46 | 3.34 |
| 1000 | 10.91 | 4.33 |
| 2000 | 13.51 | 8.97 |
| 2000 | 18.57 | 7.12 |
| 2000 | 16.75 | 7.3 |
| 2000 | 16.89 | 8.29 |
| 2000 | 18.72 | 7.38 |
| 5000 | 85 | 18.57 |
| 5000 | 80.5 | 16.55 |
| 5000 | 82.14 | 15.72 |
| 5000 | 85.62 | 14.08 |
| 5000 | 91.8 | 16.53 |

### Average latency with index in DEV ENV

| Query Records Num | Query by JsonB type (second) | Query by Column type (second) | Jsonb cost more time |
|---:|---:|---:|---:|
| 100 | 1.91 | 1.7 | 12% |
| 1000 | 4.39 | 3.1 | 42% |
| 2000 | 7.53 | 4.35 | 73% |
| 5000 | 15.23 | 7.34 | 107% |

### Individual runs with index in DEV ENV

| Query Records Num | Query by JsonB type (second) | Query by Column type (second) |
|---:|---:|---:|
| 100 | 2.00 | 1.81 |
| 100 | 1.87 | 1.79 |
| 100 | 1.88 | 1.679 |
| 100 | 2.04 | 1.78 |
| 100 | 1.76 | 1.83 |
| 1000 | 4.33 | 3.15 |
| 1000 | 4.15 | 3.35 |
| 1000 | 5.04 | 3.18 |
| 1000 | 4.26 | 3.05 |
| 1000 | 4.17 | 2.80 |
| 2000 | 6.98 | 4.38 |
| 2000 | 7.76 | 3.80 |
| 2000 | 7.27 | 4.71 |
| 2000 | 7.63 | 4.36 |
| 2000 | 8.02 | 4.5 |
| 5000 | 14.9 | 8.15 |
| 5000 | 14.75 | 6.97 |
| 5000 | 15.05 | 7.63 |
| 5000 | 15.03 | 6.86 |
| 5000 | 16.43 | 7.09 |

## Findings and limits

For this DEV benchmark's wide projection, the column API was consistently faster than the JSONB API. Indexing substantially reduced latency for 1,000–5,000 records, especially for JSONB, but did not remove the JSONB penalty: at 5,000 records, indexed JSONB averaged 15.23 seconds compared with 7.34 seconds for columns.

The source does not provide API implementation details, index DDL, query plans, cache state, hardware, data distribution, payload equivalence, concurrent workload, or production targets. It therefore cannot validate a particular PostgreSQL index, prove JSONB is unsuitable for all workloads, or establish SSDR SLA compliance.

See [[wide-cashflow-read-projection-performance]] and the open questions [[which-indexes-were-used-in-the-ssdr-cashflow-data-benchmarks]], [[are-ssdr-and-query-service-date-status-and-counterparty-filters-semantically-equivalent]], and [[does-ssdr-cashflow-exposure-meet-its-required-latency-and-pagination-sla]].