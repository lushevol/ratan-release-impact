---
type: source
title: Cash Flow Query Model
authors: []
year: 0
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, query-service, graphql, cashflow, api-contract]
related: [cashflowsnew, cash-settlement-query-service-graphql-read-model, cashflow-query-response-null-semantics, why-does-cashflowsnew-response-not-match-the-cashflow-id-filter, what-authorization-and-masking-controls-govern-cashflowsnew-ssi-fields, query-service, stella, cash-settlement-cashflow-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/Cash flow query model.md"]
---
# Cash Flow Query Model

This source documents an example GraphQL request to `cashflowsNew` and a representative paginated response. It is evidence of a consumer-facing composite read model, not a complete service, authorization, filtering, ordering, or performance specification.

## Preserved GraphQL Request

```graphql
{
  cashflowsNew(
    filter: [
        # {field: "Cashflow.Is_STP_Ratan", operator: NE, values: "false"}, 
        {field: "Cashflow.Cashflow_Id", operator: EQ, values: "12070687922588"}]
    page: 0
    size: 5
  ) {
        pageInfo{
        totalHits
        pageNo
        pageSize
        lastPage
        }
        results{
            Trade_Id
            Delivery_Method
                                    Instrument_Common{
                 Source_System_Instrument_Sub_Type
                                                CFI_Code
                                                ISDA_Taxonomy
                                                Equity_Instrument_Reference
                                                Parent_Trade_Instrument
                                    }
                                    Data_Flow{
                                                Data_Publication_Date_Time

                                                Data_Publication_Id

                                                Data_Sender

                                                Data_Source_System

                                                Data_Source_System_Country_Code

                                                Data_Source_System_Domain_Name

                                                Data_Type

                                                Unique_Identifier_Message_Id
                                    }
                                    Entity{
                                                Person{
                                                Coverage_Marketer_PSID

                                                Event_Coverage_Marketer_PSID

                                                Execution_Marketer_PSID

                                                Event_Execution_Marketer_PSID

                                                Booking_Marketer_PSID

                                                Event_Booking_Marketer_PSID

                                                Trader_PSID

                                                Event_Trader_PSID
                                                }
                 
                                                Booking_Entity_SCI_FMCODE
                                                Booking_Entity_SCI_FMID
                                                Counterparty_SCI_FMID
                                                Counterparty_SCI_FMCODE
                                                Counterparty_CIF_Code
                                                Counterparty_Source_System_Entity_Id
                                                General_Ledger_Business_Unit_Name
                                                Booking_Entity_General_Ledger_Business_Unit_Id          
                                                
                                    }
            
                                    Cashflow{
                Cashflow_Id
                                                Cashflow_Version
                                                Cashflow_Business_Version
                                                Cashflow_State
                                                Cashflow_Event_Type
                                                Status_Event_Type
                                                Event_Date
                                                Payment_Payer_Party_Reference
                                                Payment_Receiver_Party_Reference
                                                Payment_Currency
                                                Payment_Amount
                                                Payment_Date
                                                Payment_Date_Business_Day_Convention
                                                Netting_Id
                                                Pay_Receive_Indicator
                                                Payer_Name
                                                Is_Private_Banking_Cashflow
                                                Is_Amended_Post_Settlement
                                                Payment_Type
                                                Is_Cashflow_Unnet
                                                Transaction_Details
                                                Cashflow_Affirmation_Status
                                                Is_STP
                                                Is_STP_RATAN
                                                NSTP_Reason
                                                Execution_Date_Time
                                                Cashflow_Sub_State
                                                Cashflow_Sub_State_Updater
                                                Cashflow_Sub_State_Type
                                                Prev_Cashflow_Id
                                                Next_Cashflow_Id
                                                Validation_Status
                                                Exception_Reason
                                                FMO_Comment
                                                FMO_Comment_Updater
                                                FMO_Comment_Timestamp
                                                STP_Cutoff_Date_Time
                                                Netting_Cuttoff_Date
                                                Booking_Entity_SCI_FMCODE
                                                Cashflow_Audit_Version
                                                Payment_Cutoff_Time
                                                Minor_Version_Description
                                                Bypass_Workflow_Indicator
                                                Cashflow_Minor_Version
                                                Is_Payment_Intent_To_Settle
              }
          
                                    Trade{
             Event_Physical_Status

                                    Resultant_Position_Id

                                    Trade_Original_Source_System_Name

                                    Action_Type

                                    Trade_Lake_Valid_From_Date_Time

                                    Trade_Lake_Valid_To_Date_Time

                                    Trade_Lake_Latest_Event_Date_Time

                                    Trade_Lake_Raw_Event_Date_Time

                                    Trade_Lake_Transaction_From_Date_Time

                                    Trade_Lake_Transaction_To_Date_Time

                                    BCS_Parent_Trade_Id

                                    BCS_Trade_Id

                                    Trade_Version

                                    Trade_State

                                    Position_Id

                                    Parent_Trade_Id

                                    Settlement_Method
          }
         
                                    Settlement_Instruction{
                                                Account{
                                                            SCB_Nostro_Account_Number
                                                            SCB_Nostro_Account_Type
                                                            Beneficiary_BIC_code
                                                            Beneficiary_Account_Name
                                                            Beneficiary_Account_Name_2
                                                            #  Beneficiary_Street_Address
                                                            Beneficiary_City
                                                            Beneficiary_Account_Number
                                                            Intermediary_BIC_code
                                                            Intermediary_Account_Name
                                                            Intermediary_Street_Address
                                                            Intermediary_City
                                                            Intermediary_Account_Number
                                                            Beneficiary_Bank_BIC_code
                                                            Beneficiary_Bank_Account_Name
                                                            Beneficiary_Bank_Street_Address
                                                            Beneficiary_Bank_City
                                                            Beneficiary_Bank_Account_Number
                                                            Beneficiary_Correspondent_BIC_code
                                                            Beneficiary_Correspondent_Account_Name
                                                            Beneficiary_Correspondent_Street_Address
                                                            Beneficiary_Correspondent_City
                                                            Beneficiary_Correspondent_Account_Number
                                                            Ordering_Customer_BIC_Code
                                                            Ordering_Customer_Account_Name
                                                            Ordering_Customer_Street_Address
                                                            Ordering_Customer_City
                                                            Ordering_Customer_Account_Number
                                                            Counterparty_CMS_Account_Number
                                                            EBBS_Bridge_Account_Number
                                                            EBBS_Account_Number
                                                            Booking_Entity_Correspondent_BIC_code
                                                            Booking_Entity_Correspondent_Account_Name
                                                            Booking_Entity_Correspondent_Street_Address
                                                            Booking_Entity_Correspondent_City
                                                            Booking_Entity_Correspondent_Account_Number
                                                                                                }
                                                            SSI_Unique_Id

                                                            SSI_Source

                                                            SSI_Priority

                                                            Swift_Message_Type

                                                            Remittance_Information_1

                                                            Remittance_Information_2

                                                            Remittance_Information_3

                                                            Remittance_Information_4

                                                            Sender_To_Receiver_Information_1

                                                            Sender_To_Receiver_Information_2

                                                            Sender_To_Receiver_Information_3

                                                            Sender_To_Receiver_Information_4

                                                            Sender_To_Receiver_Information_5

                                                            Sender_To_Receiver_Information_6

                                                            Is_Third_Party_Payment

                                                            Swift_Payment_Method

                                                            Charge_Bearer

                                                            Nostro_Swift_Message_Type
                                                }
              Portfolio{
                Booking_Entity_Trade_Portfolio_Name
                Booking_Entity_Trade_Portfolio_Unique_Name
              }
              FMO_Comments{
                FMO_Comment
                FMO_Comment_Updater
                FMO_Comment_Timestamp
              }
        }
  }}
```

## Observed Contract

The operation accepts a `filter` array and zero-based `page` and `size` inputs. The example response reports `totalHits: 42`, `pageNo: 0`, `pageSize: 5`, and `lastPage: false`.

Each requested result combines cashflow, trade, instrument, entity, portfolio, settlement-instruction, operational-comment, and `DataFlow` provenance information. The five shown records identify [[stella]] as `data_source_system`, with `data_type: "CashflowData"`.

The sample includes `PROJECTED`, `QUEUED`, and `DEAD` cashflow states, and `New` and `Amendment` cashflow event types. These observed values are not a complete lifecycle enumeration or transition definition.

## Contract Caveats

- The request filters for `Cashflow.Cashflow_Id = "12070687922588"`, but the response contains five different cashflow IDs and reports 42 hits. This example cannot establish equality-filter semantics.
- Requested GraphQL names such as `Data_Flow`, `Cashflow_Id`, and `Trade_Id` differ from response keys such as `DataFlow`, `cashflow_id`, and `trade_id`.
- Missing values appear as JSON `null`, empty strings, and literal `"null"` strings.
- `Settlement_Instruction` is `null` in every shown result, despite the broad requested account and payment-routing projection.
- The exposed API field is spelled `Netting_Cuttoff_Date`; consumers should retain this spelling pending an authoritative schema contract.
- `FMO_Comment` fields are requested both within `Cashflow` and in `FMO_Comments`, but the source does not state which location is canonical.

See [[cash-settlement-query-service-graphql-read-model]] for the consumer-facing model and [[cashflow-query-response-null-semantics]] for missing-value handling. Open issues are tracked in [[why-does-cashflowsnew-response-not-match-the-cashflow-id-filter]] and [[what-authorization-and-masking-controls-govern-cashflowsnew-ssi-fields]].