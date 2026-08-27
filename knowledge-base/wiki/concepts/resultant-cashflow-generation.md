---
type: concept
title: Resultant Cashflow Generation
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, resultant-cashflow, aggregation]
related: [cashflow-netting, netting-service, cashflow-unnetting, cashflow-splitting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md"]
---

# Resultant Cashflow Generation

Resultant cashflow generation creates an aggregate cashflow from a set of component cashflows selected for a netting operation.

The source requires the component amounts to be summed and the resultant to be created with status `Queued`. Its examples show resultant records with payment type `IRS`, including:

- `N01` with amount `300` from components of `100` and `200`
- `N02` with amount `700` from components of `100`, `200`, and `400`

The design does not specify how the resultant derives currency, payment direction, entity, counterparty, settlement date, settlement method, version fields, or other cashflow attributes. It also does not define whether resultant creation and component status updates are atomic.

The source contains a separate split scenario in which a resultant of `300` is marked `SPLIT` and produces two `WAITING` cashflows of `150`. This indicates that resultant generation is connected to, but distinct from, [[cashflow-splitting]].