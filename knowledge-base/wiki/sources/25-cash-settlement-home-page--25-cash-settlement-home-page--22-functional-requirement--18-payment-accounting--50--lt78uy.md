---
type: source
title: Korea Cashflow Migration - RATAN to OLTP Accounting
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [korea, payment-accounting, ratan, oltp, cashflow-migration, integration]
related: [korea-ratan-oltp-accounting-integration, oltp, ratan-accounting-status-lifecycle, oltp-accounting-message-contract, oltp-eod-accounting-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# Korea Cashflow Migration - RATAN to OLTP Accounting

This functional requirement moves Korea real-time cashflow accounting delivery from the Murex-KR route to direct [[ratan]]-to-[[oltp]] messaging. The cashflow population remains the same as the population currently received by RATAN from Murex-KR.

RATAN generates the accounting entry, sends it to OLTP through Solace, and records `SUCCESS` only after an OLTP ACK. The requirement defines Korean posting rules, payload fields, status outcomes, validation errors, and manual handling during the OLTP EOD interruption.

## Scope and routing

Accounting applies to cashflows in `Failed`, `Swift_suppressed`, `Released`, or `Settled` status.

The stated routing conditions are:

1. `Sett Means = 'NOS'`.
2. `Sett Means = 'NOX' and Sett Account in ('KRO UIBOK', 'KRO BOKSEO')`.

However, the implementation is described as a blacklist: only NOX accounts `CCY UISUS` and `CCY UIDD` are blocked; all other NOX accounts can be sent to OLTP. Adding another excluded account requires a RATAN code change. See [[oltp-accounting-eligibility-blacklist]].

## Posting behavior

For a new cashflow:

- SCB pay: increase the Bridge account and decrease the Nostro account.
- SCB receive: increase the Nostro account and decrease the Bridge account.

For a withdrawal, the directions reverse:

- SCB pay: decrease the Bridge account and increase the Nostro account.
- SCB receive: increase the Bridge account and decrease the Nostro account.

Each message contains two account legs and one reconciliation record. See [[bridge-and-nostro-accounting-legs]].

## RATAN accounting statuses

| Status | Meaning |
| --- | --- |
| `HOLD` | Entry is generated but is being held before delivery. |
| `DISABLED` | Entry was generated for NOX with `CCY UISUS` or `CCY UIDD` but is not sent to OLTP. |
| `SENT` | Entry was sent to OLTP and RATAN has not received a response. |
| `SUCCESS` | OLTP consumed the entry and returned ACK. |
| `REJECTED` | OLTP could not consume the entry and returned an error. |
| `MISSING_INFO` | Mandatory data is absent, including an unavailable Nostro for a `SWIFT_SUPPRESSED` case; RATAN does not generate the entry. |

The requirement states that pre-value-date `HOLD` entries are sent at 06:00 local time; if the amount of accounting is large, sending continues hourly.

## TRANDATA mapping

| Field | Format | Rule or source |
| --- | --- | --- |
| `AIGRILJA` | `NUMBER(8)` | Value date: `Cashflow.Payment_Date`. |
| `AIREFNO` | `CHAR(16)` | Cashflow ID (12) + business version (2) + minor version (2). |
| `AIGJJRSU` | `NUMBER(2)` | Hardcoded `02`. |
| `AIBRNO(1)`, `AIBRNO(2)` | `NUMBER(3)` | Hardcoded `017`. |
| `AICODE(1)` | `NUMBER(6)` | Bridge account: KRW `000287`; non-KRW `040446`. |
| `AICODE(2)` | `NUMBER(6)` | Nostro account from `settlement_Instruction.account.EBBS_Account_Number`. |
| `AISECD(1)`, `AISECD(2)` | `NUMBER(2)` | Hardcoded `00`. |
| `AITONG(1)`, `AITONG(2)` | `CHAR(3)` | ISO payment currency. |
| `AIIPJI(1)` | `CHAR(2)` | Bridge direction: `10` debit/pay; `30` credit/receive. |
| `AIIPJI(2)` | `CHAR(2)` | Opposite direction of `AIIPJI(1)`. |
| `AIAMT(1)`, `AIAMT(2)` | `NUMBER(15,2)` | Payment amount formatted to two decimal places. |
| `AIGUBN(1)`, `AIGUBN(2)` | `CHAR(1)` | Hardcoded `N`. |
| `AIRCJRSU` | `NUMBER(2)` | Hardcoded `01`. |
| `AIRCTYPE` | `CHAR(1)` | Hardcoded `1`. |
| `AIRCBIC` | `CHAR(11)` | Normalized Nostro correspondent BIC. |
| `AIRCTONG` | `CHAR(3)` | ISO payment currency. |
| `AIRCIPJI` | `CHAR(1)` | `1` for credit/receive and `2` for debit/pay; same business direction as the Bridge leg. |
| `AIRCDATE` | `NUMBER(8)` | Value date. |
| `AIRCAMT` | `NUMBER(15,2)` | Payment amount formatted to two decimal places. |
| `AIRCREF` | `CHAR(16)` | `"DV70"+Cashflow_ID`. |
| `AIRCGBN` | `CHAR(1)` | Documented as hardcoded `NULL`; see unresolved issue below. |

### Amount formatting

| Amount in RATAN | Send to OLTP | Rule |
| --- | --- | --- |
| `1.236` | `1.24` | Round to two decimal places. |
| `1.23` | `1.23` | Preserve. |
| `1.2` | `1.20` | Pad one decimal place. |
| `12345` | `12345.00` | Add `.00`. |
| `12345678901234.56` | `12345678901234.56` | OLTP returns `TXN00060`. |

### BIC normalization

| Scenario | Original BIC | Target BIC |
| --- | --- | --- |
| Ten-character BIC | `SCBLGB2LTSY` | `SCBLGB2L` followed by three spaces |
| Eight-character BIC | `SCBLIDJX` | `SCBLIDJX` followed by three spaces |
| Eleven-character BIC ending `XXX` | `SCBLEGCAXXX` | `SCBLEGCA` followed by three spaces |
| Eleven-character BIC with another suffix | `SCBLCNSXSHA` | `SCBLCNSXSHA` |

The `xxx` notation in the requirement means literal spaces, not the characters `x`. See [[nostro-correspondent-bic-normalization]].

## Solace/JMS transport requirements

The request and response must retain `X-Outbound-Property-mxDocID`, `X-Outbound-Property-trackingId`, `imsCorrelationId`, `imsTraceId`, and `imsPreviousCorrelationId`. `imsEvent` is `SENT` for the RATAN request and `RECEIVED` for the OLTP response. ENISIS updates `imsTimestamp` to system time.

Response values for mandatory Solace fields `trackingId`, `sender`, `domainName`, `initiatedTimestamp`, and `countryCode` remain pending alignment among OLTP, KR EDMi, and FM Solace.

## OLTP validation error catalogue

```text
TXN00000  Transaction posting (Multi_Leg - Posting type)
TXN00001  Transaction date must be in numeric format
TXN00002  Transaction date must be today & the previous business day
TXN00003  Must be a valid Reference no.
TXN00004  Number of iterations must be in numeric format
TXN00005  Number of iterations must be the hardcoded value "2"
TXN00006  Number fields(digit) in the first array of AIGJ must be numeric format
TXN00007  Numeric data error in the second account information
TXN00008  AIBRNO(1) field value error in the first array of AIGJ
TXN00009  AICODE(1) field value error of the first array of AIGJ
TXN00010  AITONG(1) field value error of the first array of AIGJ
TXN00011  AIIPJI(1) field value error of the first array of AIGJ
TXN00012  AIAMT(1) field value error of the first array of AIGJ
TXN00013  AIGUBN(1) field value error of the first array of AIGJ
TXN00014  AIBRNO(2) field value error in the first array of AIGJ
TXN00015  AICODE(2) field value error of the first array of AIGJ
TXN00016  AITONG(2) field value error of the first array of AIGJ
TXN00017  AIIPJI(2) field value error of the first array of AIGJ
TXN00018  AIAMT(2) field value error of the first array of AIGJ
TXN00019  AIGUBN(2) field value error of the first array of AIGJ
TXN00020  Number of iterations must be in numeric format
TXN00021  Error if the array count exceeds two
TXN00022  Number fields(digit) in the first array of AIRC must be numeric format
TXN00023  AIRCTYPE(1) field value error of the first array of AIRC
TXN00024  AIRCBIC(1) field value error of the first array of AIRC
TXN00025  AIRCIPJI(1) field value error of the first array of AIRC
TXN00026  AIRCDATE(1) field value error of the first array of AIRC
TXN00027  AIRCAMT(1) field value error of the first array of AIRC
TXN00028  AIRCREF(1) field value error of the first array of AIRC
TXN00029  AIRCGBN(1) field value is "null"
TXN00030  CCY code unmatch betwwen AITONG(1) and AIRCTONG(1)
TXN00031  Error if this condition is not met
TXN00032  Number fields(digit) in the second array of AIRC must be numeric format
TXN00033  AIRCTYPE(2) field value error of the second array of AIRC
TXN00034  AIRCBIC(2) field value error of the second array of AIRC
TXN00035  AIRCIPJI(2) field value error of the second array of AIRC
TXN00036  AIRCDATE(2) field value error of the second array of AIRC
TXN00037  AIRCAMT(2) field value error of the second array of AIRC
TXN00038  AIRCREF(2) field value error of the second array of AIRC
TXN00039  AIRCGBN(2) field value is "null"
TXN00040  CCY code unmatch betwwen AITONG(2) and AIRCTONG(2)
TXN00041  AIBRNO field value error
TXN00042  OLTP Mapping error of AITON field value
TXN00043  AICODE field value error
TXN00044  SECD value provided but not maintained in OLTP account code table
TXN00045  SECD value mismatch between OLTP account code table and message
TXN00046  AITONG field is KRW, AICODE is a foreign ccy account
TXN00047  AITONG field is the foreign CCY, AICODE is a KRW account
TXN00048  Exchange rate not registered in OLTP
TXN00049  Error during OLTP internal program(GTQUOTE) processing
TXN00050  BIC code conversion error in OLTP
TXN00051  Error during OLTP account processing program(GFGSEDT)
TXN00052  DB setting error during OLTP account processing
TXN00053  Transaction date must be a business day (Based on Korean business days)
TXN00054  CCY code unmatch betwwen AITONG(1) and AITONG(2)
TXN00055  Amount unmatch betwwen AIAMT(1) and AIRCAMT(1)
TXN00056  Amount unmatch betwwen AIAMT(2) and AIRCAMT(2)
TXN00057  Amount unmatch betwwen AIAMT(1) and AIAMT(2)
TXN00058  CCY code must be in character format
TXN00059  CCY code mapping error
TXN00060  AIAMT(1) must include a decimal point before the last two digits
TXN00061  AIAMT(2) must include a decimal point before the last two digits
TXN00062  AIRCAMT(1) must include a decimal point before the last two digits
TXN00063  AIRCAMT(2) must include a decimal point before the last two digits
```

The requirement identifies `TXN00042` through `TXN00052` and `TXN00059` as OLTP errors.

## EOD exception process

During OLTP EOD from 23:30 to 00:30 KST, failed real-time accounting is handled manually. KREDMI returns an exception/NACK response; RATAN displays the error on its Dashboard and marks the accounting record:

```text
OLTP_EOD_ERROR("EOD001", "Can not reach to OLTP")
```

An exception containing `"*body" : "Error"` is mapped to `REJECTED` with reason `Can not reach to OLTP`. KR OPS then handles the record in [[oscar]] and OLTP. See [[oltp-eod-accounting-exception-handling]].

## Static data

| Entity Name | FMID | Country Code | Branch code |
| --- | --- | --- | --- |
| `SCFB_SEOUL` | `10036645` | `KR` | `70` |

| M_ENTITY | FMID | ISO Currency | Bridge Account |
| --- | --- | --- | --- |
| `SCFB_SEOUL` | `10036645` | `KRW` | `000287` |
| `SCFB_SEOUL` | `10036645` | FCY | `040446` |

## Unresolved points

- `AIRCGBN` is mapped as `NULL`, but `TXN00029` and `TXN00039` reject `"null"`.
- `KRO BOKSEO` is described both as eligible for OLTP accounting and as manually uploaded through SSDR.
- The requirement does not define complete posting behavior for `FAILED` and all `SWIFT_SUPPRESSED` cases.
- A timeout does not define an inquiry or reconciliation process to prevent duplicate posting.
- The distinct use of branch values `017`, `70`, `45`, and `0998` is not explained.
- The supplied JSON templates contain comments and syntax defects, so they are illustrative rather than executable payloads.