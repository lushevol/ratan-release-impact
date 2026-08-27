---
type: entity
title: RATAN Accounting Service
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, accounting, service, database, cashflow-splitting]
related: [ratan, ebbs, cashflow-splitting, cashflow-splitting-accounting-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT/Cashflow Splitting UAT For EBBS.md"]
---
# RATAN Accounting Service

The RATAN Accounting Service is the accounting-service and persistence context referenced by the EBBS cashflow-splitting UAT. Its database schema is identified as `ratan_cash_accounting_service`.

## Validation table

The source identifies the following table as the store queried for accounting request validation:

```text
ratan_cash_accounting_service.ratan_accounting_request_task
```

The query selects:

```text
cashflow_id
business_version
minor_version
payment_date
trade_id
country
booking_entity_fmid
booking_entity_fmcode
counterparty_fmid
counterparty_fmcode
external_system_key
currency
request_info
```

The tested cashflow IDs were:

```text
S00000050000
S00000049998
S00000049999
S00000050001
S00000050019
S00000050020
S00000050022
S00000050023
```

## Role in the UAT

The table provides the persistence-level validation artifact for determining whether accounting request information exists after a child-cashflow action. The UAT expected records for partial release, `swift_suppress`, child failure, and eligible automatic release scenarios, while the `cashflow_suppress` scenario expected no accounting information.

The source does not provide query output, record counts, or `request_info` contents. The exact cardinality and completeness requirements for accounting requests therefore remain unspecified.