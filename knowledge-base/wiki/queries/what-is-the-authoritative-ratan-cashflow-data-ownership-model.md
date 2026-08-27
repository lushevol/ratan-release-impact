---
type: query
title: What Is the Authoritative RATAN Cashflow Data Ownership Model?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, data-ownership, golden-source, cashflow, governance]
related: [ratan, ratan-cashflow-lifecycle-service, ratan-cash-settlement-query-service, ratan-cqrs-cashflow-read-model, strategic-settlements-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md"]
---
# What Is the Authoritative RATAN Cashflow Data Ownership Model?

The technical design calls RATAN PostgreSQL the Strategic Cash Settlement cashflow golden source, while also describing an event-driven Query Service read database and integrations with Murex, FMRP STELLA, and Razor.

## Open questions

- Which store is authoritative for processing state, reporting state, trade data, SSI data, and downstream settlement status?
- What reconciliation and precedence rules apply when data differs across systems?
- How are read-model lag, replay, and correction handled?

The source establishes intended service boundaries but does not answer these governance questions.