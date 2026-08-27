---
type: query
title: What Is the Korea OLTP Accounting Exclusion Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [korea, oltp, accounting, nox, settlement-account]
related: [oltp, tis, ratan-tis-payment-query, korea-accounting-and-swift-exception-monitoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md"]
---
# What Is the Korea OLTP Accounting Exclusion Rule?

The Korea guide states that accounting should be sent to OLTP except for:

```text
Sett Means = 'NOX' and Sett Account in ('%UIDD%', '%UISUS%')
```

It is unclear whether this is an exclusion rule, an inclusion rule, or a Korea routing condition. The source also does not define whether `Sett Means` and `STTL_MEANS` are the same field, or whether `%UIDD%` and `%UISUS%` are literal SQL-like matching expressions.

This question affects the relationship between [[oltp]] accounting and [[tis]] processing.