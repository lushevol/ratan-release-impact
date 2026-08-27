---
type: concept
title: Korea KRO and Non-KRO Payment Routing
created: 2026-08-23
updated: 2026-08-23
tags: [korea, kro, swift, tis, payment-routing]
related: [ratan, tis, enisis, ratan-tis-payment-query, korea-accounting-and-swift-exception-monitoring, what-is-the-authoritative-korea-kro-payment-routing-matrix]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md"]
---
# Korea KRO and Non-KRO Payment Routing

The Korea processing guide states that [[ratan]] generates SWIFT messages only for non-KRO payments and that all KRO payments are manually handled through [[tis]].

This routing rule is specific to the Korea migration flow. It is not evidence of a general RATAN SWIFT-generation rule.

The detailed TIS cases refer to settlement-account values including `KRO UISUS`, `FCY UISUS`, `KRO UIBOK`, `KRO UIDD`, and `FCY UIDD`. The source does not define whether “KRO payments” means a specific account family, Korea-local payments generally, or another business classification. This ambiguity is tracked in [[what-is-the-authoritative-korea-kro-payment-routing-matrix]].