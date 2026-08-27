---
type: source
title: "Korea Cash Settlement Migration — 2026 Static Data Summary"
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, Korea, RATAN, EBBS, auto-netting, NSTP, static-data]
related: [seoul, korea, ebbs, ratan-settlement, 51358-ratanone-db-repository, korea-static-settlement-configuration, nds-auto-netting, cashflow-suppression, korea-ssi-onboarding, korea-settlement-accounting, korea-swift-mx-message-generation, is-kro-the-intended-cpt-currency-code]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/Static date summary.md"]
---
# Korea Cash Settlement Migration — 2026 Static Data Summary

## Scope

This functional-requirement summary describes static data and rule configuration for the Korea cash settlement migration. The implementation target is Seoul, identified by FMID `10036645`, with settlement processing involving [[entities/ebbs]] and [[entities/ratan-settlement]].

The source documents requirements and configuration examples. It does not provide deployment confirmation, completion dates, ownership, or sign-off evidence.

## Nostro Static

### EBBS bridge accounts

| Entity | FMID | Legal Entity | Closing Entity | EBBS bridge account | Branch code |
| --- | --- | --- | --- | --- | --- |
| SEOUL | 10036645 | SCB SEOUL*SEL | | 000287(KRW) | 70 |
| SEOUL | 10036645 | SCB SEOUL*SEL | | 040446(ALL) | 70 |

The branch code is stated to be held in a `static-data-service` file.

The source provides the following query joining the bridge-account and transaction-code tables:

```sql
select * from ratanone.ratan_static__cashflow_ebbs_bridge_account a , ratanone.ratan_static__cashflow_ebbs_txn_code b  where a.fmid =b.fmid and a.fmid ='10036645'
```

The Nostro Static section contains an empty `Sign off:` field.

## Netting configuration

The source provides this exact configuration insert:

```sql
INSERT INTO cash_netting_service.ratan_auto_netting_type_config (id, net_type,net_group_key_config,resultant_mapping_config,is_swift_suppress_when_single_cashflow,priority,description,"version",created_at,updated_at) VALUES

('8','NDS Auto Netting','[{"field":"Cashflow.ND_Parent_Trade_Id","path":"CASHFLOW__ND_PARENT_TRADE_ID"},{"field":"Entity.Booking_Entity_SCI_FMID","path":"ENTITY__BOOKING_ENTITY_SCI_FMID"},{"field":"Entity.Counterparty_SCI_FMID","path":"ENTITY__COUNTERPARTY_SCI_FMID"},{"field":"Cashflow.Payment_Currency","path":"CASHFLOW__PAYMENT_CURRENCY"},{"field":"Cashflow.Payment_Date","path":"CASHFLOW__PAYMENT_DATE"}]','{"Cashflow__Payment_Type":"NDS Auto Netting"}',false,54,'NDS Auto netting',1,'2026-02-09 10:45:15.00171','2026-02-09 10:45:15.00171');
```

The grouping key contains:

1. `Cashflow.ND_Parent_Trade_Id`
2. `Entity.Booking_Entity_SCI_FMID`
3. `Entity.Counterparty_SCI_FMID`
4. `Cashflow.Payment_Currency`
5. `Cashflow.Payment_Date`

The resultant payment type is `NDS Auto Netting`. The configuration has `is_swift_suppress_when_single_cashflow = false`, so the insert does not configure automatic SWIFT suppression for a single cashflow.

## Cutoff time

For all currencies, the cutoff is `1:30:00 AM GMT` on value date, stated as `10:30 AM KST` on value date.

## SWIFT static

| Entity | FMID | Legal Entity | Sender BIC | Field 53 BIC | Field 53 CCY to be used | Field 58 BIC |
| --- | --- | --- | --- | --- | --- | --- |
| SEOUL | 10036645 | SCB SEOUL*SEL | SCBLKRSEXXX | | | |

The sender BIC is `SCBLKRSEXXX`. Field 53 BIC, Field 53 currency, and Field 58 BIC are blank. The source separately states:

```text
No BIC_netting rule needed in RATAN for Korea.
```

Blank fields are not classified by the source as either intentionally unused or incomplete.

## NSTP rules

The source gives five Korea-related NSTP predicates. The source tables leave date, owner, department, NSTP code, completion, and comments fields blank.

### Korea typology check

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Instrument_Common__Murex_Product_Typology in ("Structured Swap", "Red Trades-StrucSwap", "SLT-Cust")
```

### Korea financial-institution client check

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Entity__Counterparty_Client_Type == "FININST"
```

### Korea loan-branch check

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Instrument_Common__Murex_Product_Group == "LN_BR"
```

The rule comment states: `KR LN_BR -> LNBR to be NSTP and suppress manually by ops`.

### Pending NDS Netting

```text
Instrument_Common__Murex_Product_Typology in ("NDS", "NDCF", "NDFRA", "ND CDS Fixing", "ND CDS", "ND-Convert", "NDS Fixing") && Cashflow__ND_Parent_Typology != "NDIRS" && Cashflow__Cashflow_Event_Reason not in ("Reversal", "Rebook") && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && ((Cashflow__Duplicate_NDS_FXD == null || Cashflow__Duplicate_NDS_FXD == "")) && (Cashflow__Splitting_Id == null || Cashflow__Splitting_Id == "") && (Cashflow__Payment_Currency != "USD" || Entity__Counterparty_Client_Type not in ("\"INTECOM\"", "\"INTEBCH\"", "\"INTLACC\"") || Entity__Counterparty_SCI_FMID == "10036645") && Entity__Booking_Entity_SCI_FMID != "10036645"
```

This rule explicitly excludes Seoul as the booking entity.

### Korea 500 Mio Payment

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Cashflow__Cashflow_Amount_USD_Transfered >= 500000000
```

## Cashflow suppression rules

### Korean bonds

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Instrument_Common__Murex_Product_Family == "IRD" && Instrument_Common__Murex_Product_Group == "BOND" && Instrument_Common__Murex_Product_Typology != "SLT-Cust"
```

### Netted KRX/SEL cashflows

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Entity__Counterparty_SCI_FMID == "400649418" && (Cashflow__Netting_Id != null && Cashflow__Netting_Id != "")
```

### Non-FMRP entities

```text
Entity__Booking_Entity_SCI_FMID not in ("400001378", "10020899", "235003861", "10078716", "10036642", "10062461", "10032025", "400054708", "400054737", "400054741", "400057714", "400075752", "400085753", "400090093", "400095464", "400130180", "400130178", "400185419", "400193370", "400209000", "400218197", "400220273", "400229749", "400516443", "400516442", "400667486", "400677737", "400683682", "400798477", "400899993", "300036368", "3", "400452428", "400451508", "4", "400960089", "9", "400093619", "401036553", "400991880", "400007847", "10075222", "400041070", "400906330", "401053411", "300075472", "6", "300011345", "2", "10038345", "400018439", "5", "8", "10036428", "7", "10036382", "400032489", "400045551", "300089409", "400910415", "10036430", "300010782", "300011525", "10041903", "10041902", "10040387", "10037477", "300084297", "10036647", "10022098", "10041530", "10036655", "300011470", "10036645") && Trade_Original_Source_System_Name not matches "(?i)^LOANIQ$"
```

This broad rule excludes Seoul FMID `10036645` and excludes trades whose original source system is `LOANIQ`.

### Korean precious metals

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Cashflow__Payment_Currency in ("XAF", "XAG", "XAU", "XPD", "XPT", "XRH")
```

## Auto-netting rules

### KRX/SEL IRS

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Entity__Counterparty_SCI_FMID == "400649418" && Instrument_Common__Murex_Product_Group == "IRS" && Cashflow__Payment_Currency == "KRO" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
```

The source labels this `KR KRX/SEL auto netting`.

### SCB/London NDF

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Entity__Counterparty_SCI_FMID == "10075222" && Cashflow__Payment_Currency in ("USD", "EUR") && Instrument_Common__Murex_Product_Type == "FXD" && Instrument_Common__Murex_Product_Typology == "NDF" && Portfolio__Booking_Entity_Trade_Portfolio_Name != "COM_KRO_BTB" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
```

The source labels this `KR SCB/LDN NDF auto netting` and notes that it is duplicated in `uat-4`.

### SCB/London commodity NDF

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Entity__Counterparty_SCI_FMID == "10075222" && Cashflow__Payment_Currency == "USD" && Instrument_Common__Murex_Product_Type == "FXD" && Instrument_Common__Murex_Product_Typology == "NDF" && Portfolio__Booking_Entity_Trade_Portfolio_Name == "COM_KRO_BTB" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
```

The source labels this `KR SCB/LDN Commodity NDF auto netting`.

### Seoul NDS Auto Netting

```text
Instrument_Common__Murex_Product_Typology in ("NDS", "NDCF", "NDFRA", "ND CDS Fixing", "ND CDS", "ND-Convert", "NDS Fixing") && Cashflow__ND_Parent_Typology != "NDIRS" && Cashflow__Cashflow_Event_Reason not in ("Reversal", "Rebook") && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && ((Cashflow__Duplicate_NDS_FXD == null || Cashflow__Duplicate_NDS_FXD == "")) && (Cashflow__Splitting_Id == null || Cashflow__Splitting_Id == "") && Entity__Booking_Entity_SCI_FMID == "10036645"
```

### Cross-entity UK/Korea rule

The source crosses out this rule and its description, so it is treated as inactive or superseded rather than current configuration:

```text
~~Cashflow__Payment_Currency == "USD" && Cashflow__Cashflow_Event_Type == "New" && ((Entity__Booking_Entity_SCI_FMCODE in ("SCB LONDON*LDN") && Entity__Counterparty_SCI_FMCODE in ("SCB SEOUL*SEL")) || (Entity__Booking_Entity_SCI_FMCODE == "SCB SEOUL*SEL" && Entity__Counterparty_SCI_FMCODE in ("SCB LONDON*LDN"))) && Trade_Original_Source_System_Name != "LOANIQ" && Cashflow__Cashflow_Event_Reason not in ("Rebook", "Reversal", "Reversal_Rebook") && Instrument_Common__Murex_Product_Typology != "NDF"~~
```

The crossed-out description is:

```text
~~Ratan Inter Entity Netting UK vs KR~~
```

## Findings and unresolved items

- Auto-netting, NSTP, and cashflow suppression use separate predicates and should not be treated as interchangeable controls.
- The KRX/SEL IRS auto-netting rule uses `KRO`, while the EBBS bridge account is labelled `KRW`. This requires authoritative currency-code confirmation; see [[queries/is-kro-the-intended-cpt-currency-code]].
- The source does not establish whether the bridge accounts, branch code `70`, or rules were deployed or signed off.
- The blank SWIFT Field 53 and Field 58 values require confirmation.
- The duplicated SCB/London NDF rule in `uat-4` requires investigation.
- The crossed-out UK/Korea inter-entity rule should not be considered active without separate confirmation.