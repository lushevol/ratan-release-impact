---
type: entity
title: RAT_PCT2_REFRESH
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, rdm, pct2, scheduled-job, konggateway, api]
related: [rdm, konggateway, ratan-rdm-reference-data-integration]
sources: ["RATAN/RATAN -Interfaces/Ratan and RDM 38430.md"]
---
# RAT_PCT2_REFRESH

## Role

`RAT_PCT2_REFRESH` is the named job associated with PCT2 portfolio-data delivery in the RDM interface inventory. The source states that PCT2 portfolio data is delivered globally through an API via [[entities/konggateway]].

## Unknown contract details

The source does not define the job schedule, initiator, API endpoint, authentication, request parameters, response schema, refresh semantics, retry policy, failure handling, or reconciliation controls. The relationship between PCT2, RDM, and the receiving RATAN component also remains unspecified.