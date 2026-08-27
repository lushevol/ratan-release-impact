---
type: source
title: Korea Accounting - OLTP
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [korea, accounting, oltp, ebbs, cash-settlement, kafka]
related: [korea-cashflow-migration, ebbs-vs-oltp-accounting-flow, oltp-accounting, ebbs, cash-settlement-accounting-service, currency-dependent-bridge-account-selection, oltp-scbml-accounting-message, accounting-task-retry-exclusion, oltp-ack-nack-processing, accounting-task-sod-recovery]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# Korea Accounting - OLTP

This technical design extends the existing EBBS settlement-accounting workflow for Korea cashflows routed to [[oltp-accounting]]. The broad task lifecycle remains common—initialization, validation, message generation, publication, response handling, and SOD recovery—but the downstream payload, storage field, topics, validation, bridge-account selection, and retry policy differ.

## Processing differences

| Task Type | Downstream | Diff |
| --- | --- | --- |
| Normal | EBBS | set task.System_Date as Payment_Date, 1 entity only have 1 bridge_account |
| OLTP | set task.System_Date as Payment_Date, but bridge_account depends on currency |
| Reversal | EBBS | same as Normal type |
| OLTP | same as Normal type |
| Netted/Split | EBBS | same as Normal type |
| OLTP | same as Normal type |

| Task Type | Downstream | Diff |
| --- | --- | --- |
| Normal | EBBS | check nostro and bridge account are stamped, then check EBBS json fileds are filled |
| OLTP | check nostro and bridge account are stamped, if settlementMeans = 'NOX' and settlementAccount contains 'UUID'/'UISUS' then disable the task |

| Task Type | Downstream | Diff |
| --- | --- | --- |
| Normal | EBBS | set task.Request_info = EBBS format json |
| OLTP | set task.ExtColumn2 = OLTP format json, 53 BIC/Receiver BIC need add new logic |
| Reversal | EBBS | update task.Request_info json, flip account and direction |
| OLTP | update task.ExtColumn2 json, also flip account and direction in TransData part |
| Netted/Split | EBBS | same as Normal type |
| OLTP | same as Normal type |

| Task Type | Downstream | Diff |
| --- | --- | ---|
| Normal | EBBS | existed function for publish message to ebbs |
| OLTP | create a new kafka topic for OLTP message and create a new method for this |
| Reversal | EBBS | same as Normal type |
| OLTP | same as Normal type |
| Netted/Split | EBBS | same as Normal type |
| OLTP | same as Normal type |

## Recovery and responses

| Downstream | Diff |
| --- | --- |
| EBBS | 1. Sent but no response will retry 3 times interval 4 min 2. if response is TXN99999 or TEC0004 will retry 3 times interval 4min |
| OLTP | no retry mechanism, but need to exclude KR tasks from retry job |

| Downstream | Diff |
| --- | --- |
| EBBS | 1. start at 06:00 every day interval 1 hour util 18:00. It will collect all Hold and payment_date <= current_date tasks. 2. check if request_info is empty will generate json message first |
| OLTP | 1. start at 06:00 every day interval 1 hour util 18:00. It will collect all Hold and payment_date <= current_date tasks. 2. check **extColumn2 **is empty? yes, then generate json first |

| Downstream | Diff |
| --- | --- |
| EBBS | 1. receive response msg from topic 2. save message 3. update task status |
| OLTP | it follows EBBS process, only receive response from different topic |

OLTP normal responses use `YOACK`, `YOEERR`, and `YOEMSG` in `TRANDATA`. The EOD NACK example instead contains an `ns:exceptions` envelope and timeout exception text; it must not be treated as the same response shape without an explicit mapping.

## Messaging configuration

```text
To OLTP:   Cash_Settlement_OLTP_Accounting_KR
From OLTP: Cash_Settlement_OLTP_Response
```

The design refers to Kafka topics and provides further Solace details in `attachments/KR_OLTP_ProjectEngagement_Template.xlsx`.

## Static-data and properties configuration

```yml
        - bookingEntitySciFmid: 10036645
          branchCode: 70
```

| M_ENTITY | FMID | ISO Currency | Bridge Account |
| --- | --- | --- | --- |
| SCFB_SEOUL | 10036645 | KRW | 000287 |
| SCFB_SEOUL | 10036645 | FCY | 040446 |

The design requires `com.scb.ratan.sd.entity.EbbsAccount` to add a `currency` attribute.

| Entity Name | FMID | Country Code |
| --- | --- | --- |
| SCFB_SEOUL | 10036645 | KR |

Additional properties-service changes:

```text
add Korea FMID in STRATEGIC_FM_LIST
CPT cashflow release condition to be updated to VD<= 14-Aug
currency - USD = 1 & KRW = 1
```

## Database changes

### `ratan_cash_accounting_service.ratan_accounting_request_task`

| column name | type | default value |
| --- | --- | --- |
| settlement_means | varchar | null |
| settlement_account | varchar | null |
| booking_entity_BIC_code | varchar | null |

### `ratan_cash_accounting_service.ratan_accounting_request_task_history`

| column name | type | default value |
| --- | --- | --- |
| settlement_means | varchar | null |
| settlement_account | varchar | null |
| booking_entity_BIC_code | varchar | null |

```sql
CREATE INDEX IF NOT EXISTS ratan_accounting_request_task_history_task_status_idx ON ratan_cash_accounting_service.ratan_accounting_request_task_history USING btree (task_status, booking_entity_fmid, created_at);
```

### `ratan_cash_accounting_service.ratan_accounting_response_info`

| column name | type | default value |
| --- | --- | --- |
| original_response | text | null |

## Implementation boundaries

The OLTP request is a nested SCBML envelope with `SYSTEMHEADER`, `TRANCOMMONHEADER`, and `TRANDATA`, rather than the EBBS JSON:API-style message. Several mappings remain unresolved, including BIC and Receiver BIC derivation, `TMSG_CRE_SYS_NM`, `TRAN_CD`, `TRXCD`, `BIZDISTCD`, `INPUTDISTCD`, `INPUTDISTCD_CANCEL`, correlation identifiers, timestamp formatting, and the ownership of hardcoded values.

See [[what-is-the-authoritative-oltp-accounting-message-schema]], [[what-is-the-korea-oltp-retry-and-recovery-policy]], and [[how-is-fcy-defined-for-korea-bridge-account-selection]].