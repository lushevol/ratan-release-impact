---
type: source
title: Korea Accounting - TLM Recon
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/DSP/Cash+Settlement+-+Korea+TLM+Accounting"
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [korea, accounting, reconciliation, tlm, ebbs, ratanone, api]
related: [tlm, fmaa, query-recon-records, ratan-accounting-request-task-history, korea-tlm-accounting-reconciliation, latest-sent-accounting-task-history-selection, fmaa-authenticated-accounting-retrieval, ebbs, accounting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# Korea Accounting - TLM Recon

This technical design specifies the RATAN API used by [[tlm]] to retrieve Korea accounting-feed records in [[ebbs]] message format for reconciliation. Retrieval is bounded by accounting-task history `created_at`, filtered to `SENT` tasks and booking-entity FMIDs, and returns the latest eligible history row for each `task_id`.

## API contract

UAT4 request:

```bash
curl --location --request GET 'https://uklvadapp1344.uk.dev.net:8453/api/ratan/v1/accounting/queryReconRecords?fmidList=10036645&startReleaseTime=2026-05-28T09:00:00&endReleaseTime=2026-05-29T09:00:00' --header 'Accept-Encoding: gzip' --compressed
```

Required headers:

```text
Accept-Encoding: gzip
FMAA-Token: ${token from FMAA}
FMAA-userId: ${userId from FMAA}
FMAA-appId: ${appId from FMAA}
```

Clients must register with [[fmaa]] before obtaining the FMAA-generated header values. Gzip is required because API responses can exceed 10 MB.

The source shows this PROD URL, including its apparent extra `[` character:

```text
https://fmo-mfe.gdc.standardchartered.com:8453/api/ratan/[v1/accounting/queryReconRecords?fmidList=10036645&startReleaseTime=2026-03-30T00:00:00&endReleaseTime=2026-04-01T00:00:00
```

## Parameters and errors

| name | type | M/O | sample | comment |
| --- | --- | --- | --- | --- |
| startReleaseTime | DateTime(yyyy-mm-dd'T'HH24:MM:SS) need covert to GMT | M | 2026-04-30T00:00:00 | ratan_accounting_request_task_history. created_at >= startReleaseTime |
| endReleaseTime | DateTime(yyyy-mm-dd'T'HH24:MM:SS) need covert to GMT | M | 2026-05-01T00:00:00 | ratan_accounting_request_task_history. created_at < endReleaseTime |
| fmidList | String | M | 10036645,10075222 | ratan_accounting_request_task_history. booking_entity_fmid in fmidList; only support 10036645 currently |

| Exception scenario | ErrorMessage |
| --- | --- |
| When fill in start time after end time | startReleaseTime can not after endReleaseTime |
| When the period between start time and end time is over 72 hours | can not fetch records over 72 hours |
| When parameter is empty | Parameters are mandatory |

The intended query interval is inclusive at `startReleaseTime` and exclusive at `endReleaseTime`. A request must not exceed 72 hours.

## History-record selection

The design identifies [[ratan-accounting-request-task-history]] as the retrieval source. It selects `SENT` records in the specified `created_at` range, scoped to `booking_entity_fmid`, then keeps the greatest `id` within each `task_id`.

```sql
select distinct on (task_id) id , task_id, rarth.created_at , rarth.request_info from ratan_accounting_request_task_history rarth
where rarth.created_at >= '2026-04-04 01:50:00' and rarth.created_at < '2026-04-04 01:55:00' and booking_entity_fmid in ('10036645')
and task_status in ('SENT') order by task_id, id desc;
```

`created_at` is returned as the publication timestamp, while `request_info` supplies the EBBS message. The source requests an index on “`booking_entity_id /created_at/country/task_status` column at least”; this conflicts with the query's use of `booking_entity_fmid`.

## Response and payload

The formal response description is:

| field name | type | comment |
| --- | --- | --- |
| totalRecords | int | |
| accountingFeeds | JsonArray | message: EBBS json, publishTimestamp |

However, UAT and Korea examples use `totoalNumberOfRecords`, `accountingRecords`, and `publishTimeStamp`. This schema inconsistency is tracked in [[what-is-the-canonical-korea-tlm-recon-api-response-schema]].

Each EBBS message has two `transaction entry` records: a Nostro leg and an EBBS bridge-account leg. Their transaction natures are opposite. For a New cashflow where payer reference equals `party1`, the Nostro leg is `C` and the bridge leg is `D`; otherwise, they are `D` and `C`, respectively.

| Path | Field | Type | Length | RATAN Length | Mandatory | Ratan Logic | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| data/attributes/request/transaction entry/narratives | narration1**(Mandatory)** | VARCHAR | 35 | 32 | M | "DV" + Branch code +cashflow ID | SWIFT tag 20 |
| narration2 | VARCHAR | 50 |  | M | Party2.SCI.Entity.FM_CODE | Counterparty FM CODE |
| narration3 | VARCHAR | 50 | text | M | Payment.Instrument_Common.ISDA_Taxonomy | Product Taxonomy |
| narration4 | VARCHAR | 35 | text | M | Trade_Id +" "+Source_System_Trade_Internal_Id | Trade_Id (Mandatory)+ " " +S2BX Trade Id |
| narration5 | VARCHAR | 35 | text | M | Transaction_Banking_Comments | TB Comments Field (from Trade) Contains Source system Payment Reference (From Trade) + Underlying client ID Blank for non utilization |
| narration6 | VARCHAR | 35 | text | M | Cashflow.Cashflow_State +" " +Data_Flow.Data_Source_System | Cashflow Status + “ ” + Data_Source_System |
| data/attributes/request/transaction entry/extended-narratives | EXTENDEDNARRATIVE1 | VARCHAR | 65 | text | M | Instrument_Common.Murex_Product_Strategy#Cashflow.Payment_Type#Cashflow.Netting_Id | Netting ID replacement under Swap Agent change ADO 5967599 |
| EXTENDEDNARRATIVE2 | VARCHAR | 65 | text | M | Cashflow.splitParentId#Party1.Entity.Booking_Entity_SCI_FMID+" "+Party1.SCI.Entity.FM_CODE | booking entity FMID+ Entity FM CODE |
| EXTENDEDNARRATIVE3 | VARCHAR | 65 | text | M | FXU.Payment Reference +“ ” +FXU.Area code +" " + FXU.Maker ID +" " FXU.Checker ID+ FXU.utilization status | Blank for non utilization & auto util & pastdue |
| EXTENDEDNARRATIVE4 | VARCHAR | 65 | text | M | Party2.Entity.Counterparty_SCI_FMID | CounterParty FMID Blank for non split |
| EXTENDEDNARRATIVE5 | VARCHAR | 65 |  | M | Party2.SCI.Entity.Counterparty_Long_Name | Counterparty long name |
| EXTENDEDNARRATIVE6 | VARCHAR | 65 | text | M | Portfolio.Booking_Entity_Trade_Portfolio_Name | Biz Portfolio |

## Korea-specific enrichment

- `posting-branch` is empty for Korea.
- `transaction-code` is specified as `NULL` for Korea, but examples also use `""`.
- The external system key is `Cashflow.Cashflow_Id + "." + Cashflow.Cashflow_Business_Version + "." + Cashflow.Cashflow_Minor_Version`.
- Cashflow `C1` as New uses `C1.1.1`; its withdrawal uses reversal key `C1.2.1`.
- Currency is derived from `Cashflow.Payment_Currency` and ISO static data, with special SG CNH logic.
- Value date is `Cashflow.Payment_Date` in `YYYY-MM-DD`.
- The bridge account is resolved from entity FMID through static data.

See [[korea-tlm-accounting-reconciliation]], [[latest-sent-accounting-task-history-selection]], and [[fmaa-authenticated-accounting-retrieval]].

## Performance evidence

A reported 72-hour performance-test extraction contained:

```text
releaseTimeScope: 2026-07-22T00:00:00 → 2026-07-25T00:00:00
response total accounting feeds: 20286
```

The source links an Apache JMeter Dashboard but provides no readable latency, concurrency, error-rate, payload-size, or acceptance-threshold results. This volume is evidence of a test run, not a production performance guarantee.