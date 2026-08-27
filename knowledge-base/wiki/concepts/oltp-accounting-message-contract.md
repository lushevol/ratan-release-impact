---
type: concept
title: OLTP Accounting Message Contract
created: 2026-08-23
updated: 2026-08-23
tags: [oltp, ratan, message-contract, trandata, solace, accounting]
related: [korea-ratan-oltp-accounting-integration, bridge-and-nostro-accounting-legs, nostro-correspondent-bic-normalization, enisis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# OLTP Accounting Message Contract

The RATAN-to-OLTP message uses an SCBML envelope with `TRANDATA` holding posting and reconciliation data.

The account contract requires `AIGJJRSU = "02"` and two `AIGJ` elements. The reconciliation contract requires `AIRCJRSU = "01"` and one `AIRC` element. `AIREFNO` is a 16-character cashflow reference comprising cashflow ID, business version, and minor version.

Amounts in `AIAMT` and `AIRCAMT` must have two decimal places. OLTP validates content, array counts, account and currency combinations, BIC conversion, business dates, cross-leg amount/currency equality, and decimal placement through `TXN00001`–`TXN00063`.

Request/response correlation relies on returned Solace headers including `X-Outbound-Property-mxDocID`, `X-Outbound-Property-trackingId`, `imsCorrelationId`, `imsTraceId`, and `imsPreviousCorrelationId`. Several response-side mandatory headers remain unresolved.

The source templates are not valid executable JSON because they include comments, malformed quotations, and missing commas.