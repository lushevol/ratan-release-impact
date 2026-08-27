---
type: source
title: "Ratan One Processing Guide (DOI) — Korea"
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, korea, migration, tis, oltp, swift, operational-guide]
related: [ratan, tds3, tis, oltp, enisis, korea-kr-comp-csv-upload, ratan-tis-payment-query, korea-kro-non-kro-payment-routing, korea-accounting-and-swift-exception-monitoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md"]
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/FMRP/Settlement+-+KR+Murex+2.11+DOI+Document"
venue: "Operational processing guide"
---
# Ratan One Processing Guide (DOI) — Korea

This operational guide describes a Korea migration flow in [[ratan]]: manual `COMP` trade-status upload, [[tis]] payment and receipt retrieval, [[oltp]] accounting submission and monitoring, and SWIFT exception monitoring.

The guide is Korea-specific. It should not be treated as a general RATAN processing contract without corroborating evidence.

## Korea `COMP` upload

Korea is described as not onboarded to [[tds3]], so trade status cannot be synchronized through TDS3. RATAN provides a `KR COMP` GUI function to upload trade information, affirm cashflows automatically, and record trades with status `COMP`.

| Number | Step |
| --- | --- |
| 1 | Prepare a CSV file containing SCBML trade information. File size limitation: `20M`; number limitation: `2000`. |
| 2 | Log in with an authorized account. |
| 3 | Click `KR COMP`. |
| 4 | Select the prepared CSV file. |
| 5 | Click `Open`; a success prompt confirms a successful upload. |
| 6 | For file-format or data errors, use the failure prompt's specific reason to correct the CSV. |

The source identifies these authorized accounts:

- `1372116-Yang, Ji Hoon`
- `1371935-Cho, Hye Won`
- `1372224-Choo, Ji Won`

The source does not provide the CSV schema, header rules, encoding, duplicate treatment, or partial-success behavior. See [[what-is-the-scbml-kr-comp-csv-schema]].

## TIS payment processing

The guide presents TIS retrieval as an alternative to daily manual payment keying through the OLTP UI.

```text
Payment:
https://fmo-mfe.gdc.standardchartered.com:8453/api/ratan/v1/tis/query/payment/{payment date}

Receipt:
https://fmo-mfe.gdc.standardchartered.com:8453/api/ratan/v1/tis/query/receipt/{payment date}
```

TIS scope is limited to cashflows meeting all of these conditions:

1. Status is `Released` or `Settled`.
2. `STTL_MEANS = NOX`.
3. No reversal event exists.
4. Entity FMID is `10036645`.

| Case | Pay/Receive | Conditions |
| --- | --- | --- |
| `5338` | Pay | `57BIC: SCBLKR`; Settlement Account: `KRO UISUS`; Beneficiary Customer Account: mandatory, starts with `BR%` |
| `5339` | Pay | `57BIC: SCBLKR`; Settlement Account: `FCY UISUS`; Beneficiary Customer Account: mandatory, starts with `BR%` |
| `5318` | Pay | `57BIC: SCBLKR`; Settlement Account: `KRO UISUS`; Beneficiary Customer Account: mandatory, does not start with `BR%` |
| `5319` | Pay | `57BIC: SCBLKR`; Settlement Account: `FCY UISUS`; Beneficiary Customer Account: mandatory, does not start with `BR%` |
| `5323` | Pay | `57BIC: No-SCBLKR`; Settlement Account: `KRO UISUS`; Beneficiary Customer Account: mandatory, does not start with `BR%` |
| `5324` | Pay | `57BIC: No-SCBLKR`; Settlement Account: `KRO UIBOK`; Beneficiary Customer Account: `NULL` or `dummy` |
| `5325` | Pay | `57BIC: No-SCBLKR`; Settlement Account: `KRO UIBOK`; Beneficiary Customer Account: mandatory, does not start with `BR%` |
| `0201` | Receive | Settlement Account: `KRO UIDD` |
| `3013` | Receive | Settlement Account: `FCY UIDD` |

The document does not identify whether these case numbers are production codes, message types, or business-rule references.

### TIS response codes

| Name | Code | Meaning |
| --- | --- | --- |
| Success | `200` | The request succeeded and requested information is in the response. |
| NotFound | `404` | The requested resource does not exist on the server. |
| BadRequest | `400` | Parameter format does not meet requirements. |
| Unauthorized | `401` | The token is invalid. |
| InternalServerError | `500` | An error occurred in the service. |

The source says downstream consumers should adjust parameters when an error code is returned, but it does not define retry, alerting, authentication renewal, or idempotency behavior.

## OLTP accounting and monitoring

The stated cashflow-status scope for accounting is:

```text
Failed / Swift_suppressed / Released / Settled
```

The guide gives the following wording:

```text
Except below condition, accounting will need send to OLTP.

Sett Means = 'NOX' and Sett Account in ('%UIDD%', '%UISUS%')
```

Its intended inclusion or exclusion semantics are not explicit. This is potentially significant because TIS scope explicitly includes `STTL_MEANS = NOX`. See [[what-is-the-korea-oltp-accounting-exclusion-rule]] and [[how-does-korea-tis-processing-interact-with-oltp-accounting]].

Users monitor accounting errors in the Cashflow Dashboard through `Accounting Error`, filtering yesterday, today, and tomorrow by accounting status:

- `SENT`
- `REJECTED`
- `MISSING_INFO`

[[ops]] processes these items in OLTP. Users can inspect the `Accounting Detail` tab for accounting information, status, and reason.

## SWIFT exception handling

For the Korea flow, RATAN generates SWIFT messages only for non-KRO payments. The guide states that all KRO payments are manually handled through TIS.

Users monitor errors through the Cashflow Dashboard's `Swift Error` function for yesterday, today, and tomorrow. `FinalCancelled` is identified as a NACK status from [[enisis]]. The prescribed action is to process the item in the exception blotter or replay it in ENISIS.

The guide does not define the full KRO routing matrix, the meaning of KRO relative to account families in the TIS cases, or ENISIS replay controls. See [[what-is-the-authoritative-korea-kro-payment-routing-matrix]].