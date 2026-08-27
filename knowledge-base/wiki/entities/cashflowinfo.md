---
type: entity
title: CashFlowInfo
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, java, bean, dto, scbml, data-contract]
related: [scbml, ratan, ratan-scbml-template-rendering, cashflow-detail-field-projection, cashflow-lifecycle-supersession-and-audit-history]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/SCBML Template.md"]
---
# CashFlowInfo

## Role

`CashFlowInfo` is the Java bean or data-transfer object proposed as the canonical in-memory representation for generating Ratan cashflow SCBML messages.

Domain services are expected to calculate and populate its values. Common utility tooling then projects those values into SCBML template placeholders. The source presents the object as broader than any single event template: it includes cashflow, data-flow, entity, instrument, portfolio, settlement-instruction, and trade attributes.

The mapping below preserves the source terminology and property names. It is a source-specific contract, not evidence that every property is populated for every event.

## Cashflow and data-flow mappings

| Indexed term | Bean attribute |
| --- | --- |
| `Cashflow.Bypass_Workflow_Indicator` | `CashFlowInfo.Cashflow__Bypass_Workflow_Indicator` |
| `Cashflow.Cashflow_Affirmation_Status` | `CashFlowInfo.Cashflow__Cashflow_Affirmation_Status` |
| `Cashflow.Cashflow_Audit_Version` | `CashFlowInfo.Cashflow__Cashflow_Audit_Version` |
| `Cashflow.Cashflow_Business_Version` | `CashFlowInfo.Cashflow__Cashflow_Business_Version` |
| `Cashflow.Cashflow_Event_Type` | `CashFlowInfo.Cashflow__Cashflow_Event_Type` |
| `Cashflow.Cashflow_Id` | `CashFlowInfo.Cashflow__Cashflow_Id` |
| `Cashflow.Cashflow_Minor_Version` | `CashFlowInfo.Cashflow__Cashflow_Minor_Version` |
| `Cashflow.Cashflow_State` | `CashFlowInfo.Cashflow__Cashflow_State` |
| `Cashflow.Cashflow_Sub_State` | `CashFlowInfo.Cashflow__Cashflow_Sub_State` |
| `Cashflow.Cashflow_Sub_State_Type` | `CashFlowInfo.Cashflow__Cashflow_Sub_State_Type` |
| `Cashflow.Cashflow_Sub_State_Updater` | `CashFlowInfo.Cashflow__Cashflow_Sub_State_Updater` |
| `Cashflow.Cashflow_Version` | `CashFlowInfo.Cashflow__Cashflow_Version` |
| `Cashflow.Event_Date` | `CashFlowInfo.Cashflow__Event_Date` |
| `Cashflow.Exception_Reason` | `CashFlowInfo.Cashflow__Exception_Reason` |
| `Cashflow.Execution_Date_Time` | `CashFlowInfo.Cashflow__Execution_Date_Time` |
| `Cashflow.FMO_Comment` | `CashFlowInfo.Cashflow__FMO_Comment` |
| `Cashflow.FMO_Comment_Timestamp` | `CashFlowInfo.Cashflow__FMO_Comment_Timestamp` |
| `Cashflow.FMO_Comment_Updater` | `CashFlowInfo.Cashflow__FMO_Comment_Updater` |
| `Cashflow.Is_Amended_Post_Settlement` | `CashFlowInfo.Cashflow__Is_Amended_Post_Settlement` |
| `Cashflow.Is_Cashflow_Unnet` | `CashFlowInfo.Cashflow__Is_Cashflow_Unnet` |
| `Cashflow.Is_Payment_Intent_To_Settle` | `CashFlowInfo.Cashflow__Is_Payment_Intent_To_Settle` |
| `Cashflow.Is_Private_Banking_Cashflow` | `CashFlowInfo.Cashflow__Is_Private_Banking_Cashflow` |
| `Cashflow.Is_STP` | `CashFlowInfo.Cashflow__Is_STP` |
| `Cashflow.Is_STP` | `CashFlowInfo.Cashflow__Is_STP` |
| `Cashflow.Minor_Version_Description` | `CashFlowInfo.Cashflow__Minor_Version_Description` |
| `Cashflow.Netting_Cuttoff_Date` | `CashFlowInfo.Cashflow__Netting_Cuttoff_Date` |
| `Cashflow.Netting_Id` | `CashFlowInfo.Cashflow__Netting_Id` |
| `Cashflow.Next_Cashflow_Id` | `CashFlowInfo.Cashflow__Next_Cashflow_Id` |
| `Cashflow.NSTP_Reason` | `CashFlowInfo.Cashflow__NSTP_Reason` |
| `Cashflow.Pay_Receive_Indicator` | `CashFlowInfo.Cashflow__Pay_Receive_Indicator` |
| `Cashflow.Payer_Name` | `CashFlowInfo.Cashflow__Payer_Name` |
| `Cashflow.Payment_Amount` | `CashFlowInfo.Cashflow__Payment_Amount` |
| `Cashflow.Payment_Currency` | `CashFlowInfo.Cashflow__Payment_Currency` |
| `Cashflow.Payment_Cutoff_Time` | `CashFlowInfo.Cashflow__Payment_Cutoff_Time` |
| `Cashflow.Payment_Date` | `CashFlowInfo.Cashflow__Payment_Date` |
| `Cashflow.Payment_Date_Business_Day_Convention` | `CashFlowInfo.Cashflow__Payment_Date_Business_Day_Convention` |
| `Cashflow.Payment_Payer_Party_Reference` | `CashFlowInfo.Cashflow__Payment_Payer_Party_Reference` |
| `Cashflow.Payment_Receiver_Party_Reference` | `CashFlowInfo.Cashflow__Payment_Receiver_Party_Reference` |
| `Cashflow.Payment_Type` | `CashFlowInfo.Cashflow__Payment_Type` |
| `Cashflow.Prev_Cashflow_Id` | `CashFlowInfo.Cashflow__Prev_Cashflow_Id` |
| `Cashflow.Status_Event_Type` | `CashFlowInfo.Cashflow__Status_Event_Type` |
| `Cashflow.STP_Cutoff_Date_Time` | `CashFlowInfo.Cashflow__STP_Cutoff_Date_Time` |
| `Cashflow.Transaction_Details` | `CashFlowInfo.Cashflow__Transaction_Details` |
| `Cashflow.Validation_Status` | `CashFlowInfo.Cashflow__Validation_Status` |
| `Data_Flow.Data_Publication_Date_Time` | `CashFlowInfo.Data_Flow__Data_Publication_Date_Time` |
| `Data_Flow.Data_Publication_Id` | `CashFlowInfo.Data_Flow__Data_Publication_Id` |
| `Data_Flow.Data_Sender` | `CashFlowInfo.Data_Flow__Data_Sender` |
| `Data_Flow.Data_Source_System` | `CashFlowInfo.Data_Flow__Data_Source_System` |
| `Data_Flow.Data_Source_System_Country_Code` | `CashFlowInfo.Data_Flow__Data_Source_System_Country_Code` |
| `Data_Flow.Data_Source_System_Domain_Name` | `CashFlowInfo.Data_Flow__Data_Source_System_Domain_Name` |
| `Data_Flow.Data_Type` | `CashFlowInfo.Data_Flow__Data_Type` |
| `Data_Flow.Unique_Identifier_Message_Id` | `CashFlowInfo.Data_Flow__Unique_Identifier_Message_Id` |

## Entity, instrument, and portfolio mappings

| Indexed term | Bean attribute |
| --- | --- |
| `Entity.Booking_Entity_Name` | `CashFlowInfo.Entity__Booking_Entity_Name` |
| `Entity.Booking_Entity_General_Ledger_Business_Unit_Id` | `CashFlowInfo.Entity__Booking_Entity_General_Ledger_Business_Unit_Id` |
| `Entity.Booking_Entity_SCI_FMCODE` | `CashFlowInfo.Cashflow__Booking_Entity_SCI_FMCODE` |
| `Entity.Booking_Entity_SCI_FMID` | `CashFlowInfo.Entity__Booking_Entity_SCI_FMID` |
| `Entity.Booking_Entity_SCI_LEID` | `CashFlowInfo.Entity__Booking_Entity_SCI_LEID` |
| `Entity.Counterparty_CIF_Code` | `CashFlowInfo.Entity__Counterparty_CIF_Code` |
| `Entity.Counterparty_Name` | `CashFlowInfo.Entity__Counterparty_Name` |
| `Entity.Counterparty_SCI_FMCODE` | `CashFlowInfo.Entity__Counterparty_SCI_FMCODE` |
| `Entity.Counterparty_SCI_FMID` | `CashFlowInfo.Entity__Counterparty_SCI_FMID` |
| `Entity.Counterparty_Source_System_Entity_Id` | `CashFlowInfo.Entity__Counterparty_Source_System_Entity_Id` |
| `Entity.General_Ledger_Business_Unit_Name` | `CashFlowInfo.Entity__General_Ledger_Business_Unit_Name` |
| `Entity.Person.Booking_Marketer_PSID` | `CashFlowInfo.Entity__Person__Booking_Marketer_PSID` |
| `Entity.Person.Coverage_Marketer_PSID` | `CashFlowInfo.Entity__Person__Coverage_Marketer_PSID` |
| `Entity.Person.Event_Booking_Marketer_PSID` | `CashFlowInfo.Entity__Person__Event_Booking_Marketer_PSID` |
| `Entity.Person.Event_Coverage_Marketer_PSID` | `CashFlowInfo.Entity__Person__Event_Coverage_Marketer_PSID` |
| `Entity.Person.Event_Execution_Marketer_PSID` | `CashFlowInfo.Entity__Person__Event_Execution_Marketer_PSID` |
| `Entity.Person.Event_Trader_PSID` | `CashFlowInfo.Entity__Person__Event_Trader_PSID` |
| `Entity.Person.Execution_Marketer_PSID` | `CashFlowInfo.Entity__Person__Execution_Marketer_PSID` |
| `Entity.Person.Trader_PSID` | `CashFlowInfo.Entity__Person__Trader_PSID` |
| `Instrument_Common.CFI_Code` | `CashFlowInfo.Instrument_Common__CFI_Code` |
| `Instrument_Common.ISDA_Taxonomy` | `CashFlowInfo.Instrument_Common__ISDA_Taxonomy` |
| `Instrument_Common.Source_System_Instrument_Sub_Type` | `CashFlowInfo.Instrument_Common__Source_System_Instrument_Sub_Type` |
| `Portfolio.Booking_Entity_Trade_Portfolio_Name` | `CashFlowInfo.Portfolio__Booking_Entity_Trade_Portfolio_Name` |
| `Portfolio.Booking_Entity_Trade_Portfolio_Unique_Name` | `CashFlowInfo.Portfolio__Booking_Entity_Trade_Portfolio_Unique_Name` |

## Settlement-instruction mappings

| Indexed term | Bean attribute |
| --- | --- |
| `Settlement_Instruction.Account.Beneficiary_Account_Name` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Account_Name` |
| `Settlement_Instruction.Account.Beneficiary_Account_Name_2` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Account_Name_2` |
| `Settlement_Instruction.Account.Beneficiary_Account_Number` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Account_Number` |
| `Settlement_Instruction.Account.Beneficiary_Bank_Account_Name` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Bank_Account_Name` |
| `Settlement_Instruction.Account.Beneficiary_Bank_Account_Number` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Bank_Account_Number` |
| `Settlement_Instruction.Account.Beneficiary_Bank_BIC_code` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Bank_BIC_code` |
| `Settlement_Instruction.Account.Beneficiary_Bank_City` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Bank_City` |
| `Settlement_Instruction.Account.Beneficiary_Bank_Street_Address` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Bank_Street_Address` |
| `Settlement_Instruction.Account.Beneficiary_BIC_code` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_BIC_code` |
| `Settlement_Instruction.Account.Beneficiary_City` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_City` |
| `Settlement_Instruction.Account.Beneficiary_Correspondent_Account_Name` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Correspondent_Account_Name` |
| `Settlement_Instruction.Account.Beneficiary_Correspondent_Account_Number` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Correspondent_Account_Number` |
| `Settlement_Instruction.Account.Beneficiary_Correspondent_BIC_code` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Correspondent_BIC_code` |
| `Settlement_Instruction.Account.Beneficiary_Correspondent_City` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Correspondent_City` |
| `Settlement_Instruction.Account.Beneficiary_Correspondent_Street_Address` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Correspondent_Street_Address` |
| `Settlement_Instruction.Account.Beneficiary_Street_Address` | `CashFlowInfo.Settlement_Instruction__Account__Beneficiary_Street_Address` |
| `Settlement_Instruction.Account.Booking_Entity_Correspondent_Account_Name` | `CashFlowInfo.Settlement_Instruction__Account__Booking_Entity_Correspondent_Account_Name` |
| `Settlement_Instruction.Account.Booking_Entity_Correspondent_Account_Number` | `CashFlowInfo.Settlement_Instruction__Account__Booking_Entity_Correspondent_Account_Number` |
| `Settlement_Instruction.Account.Booking_Entity_Correspondent_BIC_code` | `CashFlowInfo.Settlement_Instruction__Account__Booking_Entity_Correspondent_BIC_code` |
| `Settlement_Instruction.Account.Booking_Entity_Correspondent_City` | `CashFlowInfo.Settlement_Instruction__Account__Booking_Entity_Correspondent_City` |
| `Settlement_Instruction.Account.Booking_Entity_Correspondent_Street_Address` | `CashFlowInfo.Settlement_Instruction__Account__Booking_Entity_Correspondent_Street_Address` |
| `Settlement_Instruction.Account.Counterparty_CMS_Account_Number` | `CashFlowInfo.Settlement_Instruction__Account__Counterparty_CMS_Account_Number` |
| `Settlement_Instruction.Account.EBBS_Account_Number` | `CashFlowInfo.Settlement_Instruction__Account__EBBS_Account_Number` |
| `Settlement_Instruction.Account.EBBS_Bridge_Account_Number` | `CashFlowInfo.Settlement_Instruction__Account__EBBS_Bridge_Account_Number` |
| `Settlement_Instruction.Account.Intermediary_Account_Name` | `CashFlowInfo.Settlement_Instruction__Account__Intermediary_Account_Name` |
| `Settlement_Instruction.Account.Intermediary_Account_Number` | `CashFlowInfo.Settlement_Instruction__Account__Intermediary_Account_Number` |
| `Settlement_Instruction.Account.Intermediary_BIC_code` | `CashFlowInfo.Settlement_Instruction__Account__Intermediary_BIC_code` |
| `Settlement_Instruction.Account.Intermediary_City` | `CashFlowInfo.Settlement_Instruction__Account__Intermediary_City` |
| `Settlement_Instruction.Account.Intermediary_Street_Address` | `CashFlowInfo.Settlement_Instruction__Account__Intermediary_Street_Address` |
| `Settlement_Instruction.Account.Ordering_Customer_Account_Name` | `CashFlowInfo.Settlement_Instruction__Account__Ordering_Customer_Account_Name` |
| `Settlement_Instruction.Account.Ordering_Customer_Account_Number` | `CashFlowInfo.Settlement_Instruction__Account__Ordering_Customer_Account_Number` |
| `Settlement_Instruction.Account.Ordering_Customer_BIC_Code` | `CashFlowInfo.Settlement_Instruction__Account__Ordering_Customer_BIC_Code` |
| `Settlement_Instruction.Account.Ordering_Customer_City` | `CashFlowInfo.Settlement_Instruction__Account__Ordering_Customer_City` |
| `Settlement_Instruction.Account.Ordering_Customer_Street_Address` | `CashFlowInfo.Settlement_Instruction__Account__Ordering_Customer_Street_Address` |
| `Settlement_Instruction.Account.SCB_Nostro_Account_Number` | `CashFlowInfo.Settlement_Instruction__Account__SCB_Nostro_Account_Number` |
| `Settlement_Instruction.Account.SCB_Nostro_Account_Type` | `CashFlowInfo.Settlement_Instruction__Account__SCB_Nostro_Account_Type` |
| `Settlement_Instruction.Charge_Bearer` | `CashFlowInfo.Settlement_Instruction__Charge_Bearer` |
| `Settlement_Instruction.Is_Third_Party_Payment` | `CashFlowInfo.Settlement_Instruction__Is_Third_Party_Payment` |
| `Settlement_Instruction.Nostro_Swift_Message_Type` | `CashFlowInfo.Settlement_Instruction__Nostro_Swift_Message_Type` |
| `Settlement_Instruction.Remittance_Information_1` | `CashFlowInfo.Settlement_Instruction__Remittance_Information_1` |
| `Settlement_Instruction.Remittance_Information_2` | `CashFlowInfo.Settlement_Instruction__Remittance_Information_2` |
| `Settlement_Instruction.Remittance_Information_3` | `CashFlowInfo.Settlement_Instruction__Remittance_Information_3` |
| `Settlement_Instruction.Remittance_Information_4` | `CashFlowInfo.Settlement_Instruction__Remittance_Information_4` |
| `Settlement_Instruction.Sender_To_Receiver_Information_1` | `CashFlowInfo.Settlement_Instruction__Sender_To_Receiver_Information_1` |
| `Settlement_Instruction.Sender_To_Receiver_Information_2` | `CashFlowInfo.Settlement_Instruction__Sender_To_Receiver_Information_2` |
| `Settlement_Instruction.Sender_To_Receiver_Information_3` | `CashFlowInfo.Settlement_Instruction__Sender_To_Receiver_Information_3` |
| `Settlement_Instruction.Sender_To_Receiver_Information_4` | `CashFlowInfo.Settlement_Instruction__Sender_To_Receiver_Information_4` |
| `Settlement_Instruction.Sender_To_Receiver_Information_5` | `CashFlowInfo.Settlement_Instruction__Sender_To_Receiver_Information_5` |
| `Settlement_Instruction.Sender_To_Receiver_Information_6` | `CashFlowInfo.Settlement_Instruction__Sender_To_Receiver_Information_6` |
| `Settlement_Instruction.SSI_Priority` | `CashFlowInfo.Settlement_Instruction__SSI_Priority` |
| `Settlement_Instruction.SSI_Source` | `CashFlowInfo.Settlement_Instruction__SSI_Source` |
| `Settlement_Instruction.SSI_Unique_Id` | `CashFlowInfo.Settlement_Instruction__SSI_Unique_Id` |
| `Settlement_Instruction.Swift_Message_Type` | `CashFlowInfo.Settlement_Instruction__Swift_Message_Type` |
| `Settlement_Instruction.Swift_Payment_Method` | `CashFlowInfo.Settlement_Instruction__Swift_Payment_Method` |

## Trade mappings

| Indexed term | Bean attribute |
| --- | --- |
| `Trade.Action_Type` | `CashFlowInfo.Trade__Action_Type` |
| `Trade.BCS_Parent_Trade_Id` | `CashFlowInfo.Trade__BCS_Parent_Trade_Id` |
| `Trade.BCS_Trade_Id` | `CashFlowInfo.Trade__BCS_Trade_Id` |
| `Trade.Delivery_Method` | `CashFlowInfo.Trade__Delivery_Method` |
| `Trade.Event_Physical_Status` | `CashFlowInfo.Trade__Event_Physical_Status` |
| `Trade.Parent_Trade_Id` | `CashFlowInfo.Trade__Parent_Trade_Id` |
| `Trade.Position_Id` | `CashFlowInfo.Trade__Position_Id` |
| `Trade.Resultant_Position_Id` | `CashFlowInfo.Trade__Resultant_Position_Id` |
| `Trade.Settlement_Method` | `CashFlowInfo.Trade__Settlement_Method` |
| `Trade.Trade_Id` | `CashFlowInfo.Trade__Trade_Id` |
| `Trade.Trade_Lake_Latest_Event_Date_Time` | `CashFlowInfo.Trade__Trade_Lake_Latest_Event_Date_Time` |
| `Trade.Trade_Lake_Raw_Event_Date_Time` | `CashFlowInfo.Trade__Trade_Lake_Raw_Event_Date_Time` |
| `Trade.Trade_Lake_Transaction_From_Date_Time` | `CashFlowInfo.Trade__Trade_Lake_Transaction_From_Date_Time` |
| `Trade.Trade_Lake_Transaction_To_Date_Time` | `CashFlowInfo.Trade__Trade_Lake_Transaction_To_Date_Time` |
| `Trade.Trade_Lake_Valid_From_Date_Time` | `CashFlowInfo.Trade__Trade_Lake_Valid_From_Date_Time` |
| `Trade.Trade_Lake_Valid_To_Date_Time` | `CashFlowInfo.Trade__Trade_Lake_Valid_To_Date_Time` |
| `Trade.Trade_Original_Source_System_Name` | `CashFlowInfo.Trade__Trade_Original_Source_System_Name` |
| `Trade.Trade_State` | `CashFlowInfo.Trade__Trade_State` |
| `Trade.Trade_Version` | `CashFlowInfo.Trade__Trade_Version` |

## Template usage

A representative placeholder is:

```xml
<scb:cashflowId
    cashflowIdScheme="http://www.sc.com/coding-scheme/cashflowId"
    th:text="${CashFLowInfo.Cashflow__Cashflow_Id}">
</scb:cashflowId>
```

The source uses both `CashFlowInfo` and `CashFLowInfo`. The capitalization difference, and the sender expression `th:text="$CashFlowInfo.Data_Flow__Data_Sender"`, require validation against the configured template engine.
