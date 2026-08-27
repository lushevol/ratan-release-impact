---
type: query
title: Are SSDR and Query Service Date, Status, and Counterparty Filters Semantically Equivalent?
created: 2026-08-24
updated: 2026-08-24
tags: [SSDR, query-service, cashflow-data, date-filtering, semantic-mapping]
related: [ssdr, query-service, cash-settlement-query-cn-cashflow-data, value-date-bounded-cashflow-queries]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/PT-Ratan expose the cashflow data to SSDR.md"]
---
# Are SSDR and Query Service Date, Status, and Counterparty Filters Semantically Equivalent?

The source presents an SSDR SQL requirement and a Query Service SQL implementation using different field names and relation qualifiers:

- `VALUE_DATE` versus `cashflow__payment_cutoff_time`
- `STATUS` versus `cashflow_status`
- `counterparty` versus `entity__counterparty_sci_fmid`
- `cashflow_data` versus `local_cash_settlement_query_cn.cashflow_data`

The document does not define these mappings. In particular, using the same inclusive lower and upper date value on `cashflow__payment_cutoff_time` may exclude same-day records if the field is timestamp-valued.

## Resolution needed

Confirm the canonical field mappings, the relation identity, data types, timezone, date-boundary convention, null semantics, and status/counterparty value mappings. Validate results with representative records and a date range that crosses timezone and day boundaries.