---
type: concept
title: Korea TIS Payment-Type Classification
created: 2026-08-23
updated: 2026-08-23
tags: [korea, tis, uino, payment-routing, direct-debit, bok-wire]
related: [ratan, tis, oltp, enisis, korea-settlement-account-routing, ratan-tis-payment-query-integration, what-is-the-authoritative-payacct-glno-mapping-for-korea-tis-payments, what-is-the-authoritative-korea-tis-product-field-schema]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md"]
---
# Korea TIS Payment-Type Classification

Korea TIS Payment-Type Classification derives the TIS `UINO` from cashflow direction, currency, beneficiary account, beneficiary BIC, and SCB Nostro account marker.

## Pay-side UINOs

| UINO | Condition | Payment classification |
| --- | --- | --- |
| `5338` | `BR%` beneficiary account and `KRW`/`KRO` | Internal Movement |
| `5339` | `BR%` beneficiary account and FCY | Internal Movement |
| `5318` | `UISUS`, non-`BR%` account, Korea currency, `SCBLKR%` BIC | KRW book transfer |
| `5319` | `UISUS`, non-`BR%` account, FCY, `SCBLKR%` BIC | FCY internal account |
| `5323` | `UISUS`, non-`BR%` account, Korea currency, non-`SCBLKR%` BIC | Interbank Remittance Network |
| `5324` | `UIBOK`, Korea currency, beneficiary account absent or `dummy` | Bank of Korea settlement |
| `5325` | `UIBOK`, Korea currency, non-`BR%` beneficiary account | End-client account through BOK-Wire |

The `dummy` beneficiary-account value is case-insensitive. A value of `DUMMY`, `dummy`, or another case variation has the same routing effect.

## Receipt/direct-debit UINOs

For `UIDD` receipt cashflows:

```text
KRW or KRO → 0201
all other currencies → 3013
```

Both direct-debit types are in scope.

## Excluded route

Foreign-currency external-client payments with an external receiver BIC and no `UISUS` or `UIBOK` account marker are not classified for TIS. They continue through [[enisis]] using MX + MT210.

## Important payload controls

The source defines status `STAT` as `0` initial, `1` TIS received data, and `3` UI received data; however, the API mapping hard-codes `STAT = '0'`. It also defines hard-coded Korean routing values including `PAYACCT_BR = '017'`, `DEP_REQ_NM = 'SCBK'`, `DEP_INF_IND = '01'`, and `DEP_IDENTITY = '1028121843'` for relevant UINOs.

The FCY `PAYACCT_GLNO` specification is inconsistent between `040446` and `040434`; see [[what-is-the-authoritative-payacct-glno-mapping-for-korea-tis-payments]].