---
type: source
title: Payment Accounting Functional Requirement
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page functional requirements"
tags: [cash-settlement, payment-accounting, Aspire, eBBS, Keystone, Nostro]
related: [aspire, ebbs, keystone, payment-accounting-flow, nostro-account-scope]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting.md"]
---
# Payment Accounting Functional Requirement

## Summary

This functional requirement defines payment-accounting ownership across Aspire and eBBS before and after the Keystone transition. The post-Keystone model introduces an account-level split for HK: eBBS owns HK Main Nostro, while Aspire owns HK Suspense. eBBS retains its existing scope for CN, SG, IN, MY, AG, and UK, and Aspire retains all Nostro accounts for TW and TH.

The source does not define the meaning of Keystone, effective cutover rules, transaction routing, accounting entries, reconciliation controls, or migration and rollback procedures.

## Accounting ownership

### Before Keystone

```text
Payment Accounting Flow | Entities       | Nostro Account
eBBS                   | CN/SG/IN/MY/AG/UK | All
Aspire                 | HK/TW/TH         | All
```

### Post Keystone

```text
Payment Accounting Flow | Entities       | Nostro Account
eBBS                   | CN/SG/IN/MY/AG/UK | All
eBBS                   | HK              | Main Nostro
Aspire                 | Hk              | Suspense
Aspire                 | TW/TH           | All
```

`Hk` is normalized to `HK` in the interpretation of this source.

## Referenced materials

- [Cash Settlement - Aspire Accounting](https://confluence.global.standardchartered.com/display/DSP/Cash+Settlement+-+Aspire+Accounting)
- [Cash Settlement - EBBS Accounting](https://confluence.global.standardchartered.com/display/DSP/Cash+Settlement+-+EBBS+Accounting)
- [Cash Settlement - Korea Accounting Recon - RATAN->TLM](https://confluence.global.standardchartered.com/display/DSP/Cash+Settlement+-+Korea+Accounting+Recon+-+RATAN-%3ETLM)
- [Korea Cashflow Migration -Ratan to OLTP Accounting](https://confluence.global.standardchartered.com/display/DSP/Korea+Cashflow+Migration+-+Ratan+to+OLTP+Accounting)

## Scope interpretation

The source uses `Entities` as a scope column, but does not clarify whether the values represent markets, legal entities, or booking locations. The abbreviation `AG` is also undefined. `All` is not explicitly defined and should not be assumed to include every account subtype or accounting flow.

The linked Korea references mention RATAN, TLM, and OLTP, but this document does not establish their detailed participation in the Aspire/eBBS ownership model.

## Open questions

- What system event, date, or configuration establishes the Keystone cutover?
- Does the post-Keystone HK split apply to new transactions only, or also to migrated and in-flight cashflows?
- Is HK Main Nostro always routed to eBBS and HK Suspense always routed to Aspire after cutover?
- What account categories are included in `All`?
- What do `Entities` and `AG` mean in this matrix?
- How do RATAN, TLM, and OLTP participate in Korea accounting reconciliation and migration?