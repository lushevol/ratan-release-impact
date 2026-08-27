---
type: query
title: Which Ratan Data Source Populates Remaining Amount?
tags: [ratan, cashflow, remaining-amount, data-provenance]
related: [ratan, cashflow-remaining-amount, cashflow-blotter, cash-settlement-query-service-graphql-read-model]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Remaining Amount via OpenFin.md"]
---
# Which Ratan Data Source Populates Remaining Amount?

The Ratan cashflow blotter displays a remaining amount, but the source does not identify the data source or read path that supplies it.

## Questions to resolve

- Which service, API, table, or read model provides the displayed amount?
- Is the amount returned directly by the blotter query or calculated in the Ratan client?
- Does the value originate from current cashflow data, history, settlement records, or an external system?
- What freshness and version-selection rules apply to the displayed amount?

## Current evidence

[[fxu-remaining-amount-via-openfin]] does not establish that [[cash-settlement-query-service-graphql-read-model]] or any other known query implementation supports this workflow.