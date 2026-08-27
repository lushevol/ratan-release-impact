---
type: concept
title: Currency-Level Cashflow Rounding Configuration
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, rounding, currency, configuration, static-data]
related: [ratan-cashflow-rounding-config, why-is-ratan-cashflow-rounding-config-indexed-twice-by-currency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Standardization Service.md"]
---
# Currency-Level Cashflow Rounding Configuration

Currency-level cashflow rounding configuration is a data-driven pattern in which rounding behavior is selected by currency rather than embedded solely in application logic.

In the documented schema, [[ratan-cashflow-rounding-config]] maps `k_currency` to optional `v_precision` and `v_type` fields. This establishes the storage shape only. It does not establish rounding algorithms, mode names, null-handling rules, default behavior, or governance for changes.

The table's explicit index duplicates the indexed key of its primary key in the supplied DDL; the intent requires confirmation in [[why-is-ratan-cashflow-rounding-config-indexed-twice-by-currency]].