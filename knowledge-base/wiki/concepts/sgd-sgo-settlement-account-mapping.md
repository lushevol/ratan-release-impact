---
type: concept
title: SGD-SGO Settlement-Account Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [SGD, SGO, settlement-account, SSI, static-data, cashflow, nostro]
related: [dedicated-nostro-static-data-model, nostro-records, sgo-ssi-replication, nostro-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/FMRP SGO Testing.md"]
---
# SGD-SGO Settlement-Account Mapping

## Definition

SGD-SGO settlement-account mapping is the distinction between settlement-account labels used by SGD cashflows and those used by SGO cashflows after SSI replication.

The expected namespace mapping is:

```text
SGD cashflows: SGD MAIN, SGD NO 2
SGO cashflows: SGO MAIN, SGO NO 2
```

## Test evidence

Case 24 records the expected distinction and includes the following example:

```text
Settlement Account: SGD NO 2
Cashflow ID: 10028828
SSI ID: 74703489
Currency: SGD - SINGAPORE DOLLAR
Entity: SG SUB DBU/18
Account classification: Over-Account
```

The source also refers to SGO `MAIN` and `NO 2` accounts in cases 4 and 24. The formal pass/fail value for the complete account-mapping case is not clearly populated.

## Interpretation boundary

The testing record does not establish whether `SGO MAIN` and `SGO NO 2` are:

- Separate static-data records;
- Transformed display values; or
- Aliases of corresponding SGD accounts.

That distinction should be resolved against the authoritative static-data model and [[dedicated-nostro-static-data-model]].
