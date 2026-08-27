---
type: concept
title: RATAN TIS Payment Query
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, tis, payment, receipt, api, korea]
related: [ratan, tis, oltp, korea-kro-non-kro-payment-routing, how-does-korea-tis-processing-interact-with-oltp-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md"]
---
# RATAN TIS Payment Query

RATAN exposes Korea TIS APIs for payment and receipt information retrieval, intended to reduce daily manual payment entry in [[oltp]].

```text
GET https://fmo-mfe.gdc.standardchartered.com:8453/api/ratan/v1/tis/query/payment/{payment date}

GET https://fmo-mfe.gdc.standardchartered.com:8453/api/ratan/v1/tis/query/receipt/{payment date}
```

## Eligibility scope

The documented TIS scope requires all of the following:

- Cashflow status is `Released` or `Settled`.
- `STTL_MEANS = NOX`.
- No reversal event exists.
- Entity FMID is `10036645`.

The source specifies HTTP-style response codes `200`, `400`, `401`, `404`, and `500`, but does not define retry, token renewal, or replay behavior.

TIS eligibility should not be assumed to be identical to OLTP accounting eligibility. The OLTP wording appears to identify a `NOX` and `UIDD`/`UISUS` exception, whose meaning remains unresolved in [[how-does-korea-tis-processing-interact-with-oltp-accounting]].