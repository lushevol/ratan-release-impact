---
type: source
title: RATAN to TIS — Korea Migration
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [korea-migration, cash-settlement, ratan, tis, oltp, api-integration]
related: [korea-cash-settlement-migration, korea-migration, ratan, tis, oltp, scfb-seoul, ratan-tis-payment-query-integration, korea-settlement-account-routing, korea-tis-payment-type-classification]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md"]
---
# RATAN to TIS — Korea Migration

## Summary

This functional requirement specifies a read-only Korean cash-settlement integration in which [[ratan]] exposes date-parameterized payment and receipt data for [[tis]], which supplies payment information to [[oltp]]. The target flow is:

```text
RATAN → TIS → OLTP(UI)
```

The interface is limited to the active booking entity [[scfb-seoul]] (`FMID 10036645`). It is intended to remove daily manual payment entry in OLTP(UI), but the document does not provide production deployment, testing, or go-live evidence.

The design uses two distinct query populations:

- Pay-side cashflows routed through `UISUS` or `UIBOK`.
- Receipt/direct-debit cashflows routed through `UIDD`.

Both API filters include `Released` and `Settled` cashflows, exclude `Reversal` event reasons, and apply a user-selected settlement date. The document also states that no acknowledgement, callback, refresh, or RATAN state transition occurs after a TIS query.

## Scope and operational boundaries

- In scope: pay-side UINOs `5338`, `5339`, `5318`, `5319`, `5323`, `5324`, `5325`; receipt/direct-debit UINOs `0201` and `3013`.
- Excluded: reversal and withdrawal cashflows. These may retain the original cashflow ID but are not supplied to TIS.
- Excluded from TIS: foreign-currency external-client payments, which continue through [[enisis]] using MX + MT210.
- Static-data prerequisites include accurate settlement-account markers and the in-progress Vostro migration to [[ssi-plus]].

## Eligibility filters

| | To TIS with 2 API |
| --- | --- |
| Filter A | STTL_MEANS = NOX and STTL_Account like ('%UISUS%' or '%UIBOK%' ) & Cashflow.Pay_Receive_Indicator ='Pay'& Cashflow.Cashflow_State in ('Released','Settled') & Cashflow.Cashflow_Event_Reason <> 'Reversal' & Cashflow.Payment_Date=Param 'settDate' & Entity.Booking_Entity_SCI_FMID='10036645' |
| Filter B | STTL_MEANS = NOX and STTL_Account like ('%UIDD%' ) & Cashflow.Pay_Receive_Indicator ='Receive' & Cashflow.Cashflow_State in ('Released','Settled') & Cashflow.Cashflow_Event_Reason <> 'Reversal' & Cashflow.Payment_Date=Param 'settDate' & Entity.Booking_Entity_SCI_FMID='10036645' |

## API contract

| URL | POST header |
| --- | --- |
| [https://fmo-mfe-preprod.pi.dev.net:8453/api/ratan/v1/tis/query/payment/{paymentDate}](https://fmo-mfe-preprod.pi.dev.net:8453/api/ratan/v1/tis/query/payment/%7BpaymentDate%7D) | FMAA-token {your fmaa toke} FMAA-userId {your fmaa user id} FMAA-appId {your fmaa appId} |
| [https://fmo-mfe-preprod.pi.dev.net:8453/api/ratan/v1/tis/query/receipt/{paymentDate}](https://fmo-mfe-preprod.pi.dev.net:8453/api/ratan/v1/tis/query/receipt/%7BpaymentDate%7D) | FMAA-token {your fmaa toke} FMAA-userId {your fmaa user id} FMAA-appId {your fmaa appId} |

| Field Name | Optional/Mandatory | Description | Format | Sample |
| --- | --- | --- | --- | --- |
| settDate | M | User manually select from TIS | YYYY-MM-DD | 2026-04-25 |

| Status | Code | Description |
| --- | --- | --- |
| Success | 200 | Indicates that the request succeeded and that the requested information is in the response. |
| NotFound | 404 | Indicates that the requested resource does not exist on the server. |
| BadRequest | 400 | Indicates that the mandatory parameter of request doesn't exist. Or the parameter format doesn't meet the requirement. |
| Unauthorized | 401 | Indicates that the token is invalid |
| InternalServerError | 500 | Indicates that an error has occurred in the service. |

The source additionally defines `msg = "success"` for a successful query and `msg = "failed"` when data or value date is absent or a service error occurs. The relationship between `msg`, HTTP status codes, and an empty response body is not specified; see [[what-is-the-authoritative-ratan-tis-api-error-contract]].

## Pay-side response schema

```text
AUDITTIMESTAMP
CASHFLOWNO
PRODUCT
TYPE
SETTDATE
UINO
CCY
AMOUNT
CNO
SN
AMT_IND
PAYACCT_BR
PAYACCT_IND
PAYACCT_GLNO
BIC
BANKCD
BOKCD
BR_NM
DEPACCT
DEP_REQ_NM
DEP_REQ_IND
DEP_REQ_AR
DEP_REQ_CMS
COMMENTS
COMMENT_ENG
PAY_TM
DEP_INF_IND
DEP_IDENTITY
FEE_IND
FEE_REASON
PRINT_IND
STAT
ACCOUNTTYPE
BENE_FULL_NAME
```

The pay-side UINO derivation is:

```text
case when Settlement_Instruction.Account.Beneficiary_Account_Number not like 'BR%' then
(
  case when ((Settlement_Instruction.Account.Beneficiary_Account_Number not null)
    and (Settlement_Instruction.Account.Beneficiary_Account_Number not equal 'dummy')) then
    (
      case when Settlement_Instruction.Account.SCB_Nostro_Account_Number like '%UISUS%' then
        (
          case when Cashflow.Payment_Currency in('KRW','KRO') then
            (
              case when Settlement_Instruction.Account.Beneficiary_Bank_BIC_code like 'SCBLKR%' then '5318' else '5323' end
            )
          else '5319' end
        )
      else '5325' end
    )
  else '5324' end
)
else
(
  case when Cashflow.Payment_Currency in ('KRO', 'KRW') then '5338' else '5339' end
)
end as UINO
```

`DUMMY` in `Settlement_Instruction.Account.Beneficiary_Account_Number` is case-insensitive.

## Receipt response schema

```text
AUDITTIMESTAMP
CASHFLOWNO
UINO
SN
CCY
AMOUNT
ACCOUNTNUM
ACCOUNTTYPE
VALUEDATE
PRODUCT
PRODTYPE
CNO
NOPD_REASON
```

Receipt UINO derivation:

```text
case when (Cashflow.Payment_Currency in ('KRO', 'KRW')) then '0201' else '3013' end
```

The supplied sample response uses `TYPE` where the defined schema uses `PRODTYPE`. This must be resolved before implementation; see [[what-is-the-authoritative-korea-tis-product-field-schema]].

## Pay-side payment classification

| UI NO | Explanation | 57BIC | Settlement_Instruction.Account.SCB_Nostro_Account_Number | Currency | if M_BEN_ACC exists | Current through | Target through | in Payment method | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5338 | Internal Movement | SCBLKR | %UISUS% | KRW | Y start with 'BR%' | UI(OLTP) | TIS->UI(OLTP) | 1 | Manual |
| 5339 | Internal Movement | SCBLKR | %UISUS% | FCY | Y start with 'BR%' | UI(OLTP) | TIS->UI(OLTP) | 1 | Manual |
| 5319 | USD internal account. | SCBLKR | %UISUS% | FCY | Y not start with 'BR%' | UI(OLTP) | TIS->UI(OLTP) | 4 | Manual |
| 5318 | KRW settlement case. Book transfer | SCBLKR | %UISUS% | KRW | Y not start with 'BR%' | UI(OLTP) | TIS->UI(OLTP) | 4 | Manual |
| 5323 | another bank(IRN) | No-SCBLKR | %UISUS% | KRW | Y not start with 'BR%' | UI(OLTP) | TIS->UI(OLTP) | 3 | Manual |
| 5324 | bank of korea settlement | No-SCBLKR | %UIBOK% | KRW | N('dummy' or NULL) | UI(OLTP) | TIS->UI(OLTP) | 2 | Manual |
| 5325 | end client account. | No-SCBLKR | %UIBOK% | KRW | Y not start with 'BR%' | UI(OLTP) | TIS->UI(OLTP) | 2 | Manual |
| Not in TIS scope | Foreign currency External Client(Receiver BIC is external) | No-SCBLKR | not like %UIBOK% and not like %UISUS% | FCY | | ENISIS(MX+MT210) | ENISIS(MX+MT210) | 5 | Auto |

| Payment Method | |
| --- | --- |
| 1 | Internal Movement: Transfer funds to another branch, through UI(OLTP), krw&fcy, not in RAZOR-TIS |
| 2 | BOK-Wire: External transfer funds, KRW only, RAZOR, through UI(OLTP) |
| 3 | Interbank Remittance Network: External transfer funds via Interbank remittance network, RAZOR, KRW only |
| 4 | Credit to the account held in SCBK: KRW&FCY, RAZOR |
| 5 | SCBLKR to no SCB KR bank with foreign currency: to RATAN -- ENISIS |

## Static data

| Entity Name | FMID | Country Code | Branch code |
| --- | --- | --- | --- |
| SCFB_SEOUL | 10036645 | KR | 70 |

| | Sett Means | Sett Account | Cashflow Status Post Cutoff | Payment Type | Currency | Payment Process | Accounting |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | NOS | CCY MAIN | Released/Settled | External Client | FCY | SWIFT into ENISIS | Accounting entry into OLTP |
| 2 | NOS | CCY KEBSEO | Released/Settled | External Client | FCY | SWIFT into ENISIS | Accounting entry into OLTP |
| 3 | NOS | CCY WRBSEO | Released/Settled | External Client | FCY | SWIFT into ENISIS | Accounting entry into OLTP |
| 4 | NOX | CCY UISUS | Released | Internal Movement, 1. credit funds to another branch account hold in SCBK 2. credit funds to client account hold in SCBK 3. Interbank Remittance Network | KRW & FCY | Ratan->TIS->UI(OLTP) | Accounting entry will not flow into OLTP |
| 5 | NOX | CCY UIBOK | Released | BOK-Wire | KRW | Ratan->TIS->UI(OLTP) | Accounting entry into OLTP |
| 6 | NOX | CCY UIDD | Released | Internal Movement, 1. debit funds to another branch account hold in SCBK 2. debit funds to client account hold in SCBK | KRW & FCY | Ratan->TIS->UI(OLTP) | Accounting entry will not flow into OLTP |
| 7 | NOX | KRO BOKSEO | Released | Client is Bank, through BOK wire | KRW | User will manually query in SSDR, then manually upload into OLTP | Accounting entry into OLTP |

## Key unresolved points

- The API filters include `Settled`, while the static-data matrix lists the TIS paths as `Released` only.
- The document's statement that payments will not generate accounting or SWIFT messages in RATAN is ambiguous when compared with the matrix's OLTP accounting and ENISIS routing entries.
- `PAYACCT_GLNO` specifies FCY value `040446` while a sample shows `040434`.
- The field mapping specifies pay-side `PRODUCT` and `TYPE` as `CHAR(200)`, but an open question proposes lengths of `20` and `50`.
- TIS does not refresh duplicate items keyed by trade ID/cashflow ID. A later reversal is excluded from the interface, creating a reconciliation risk for an item already retrieved by TIS.

See [[ratan-tis-payment-query-integration]], [[korea-settlement-account-routing]], and [[korea-tis-payment-type-classification]].