---
type: concept
title: Group-Ready CCY Pair Enrichment
created: 2026-08-23
updated: 2026-08-23
tags: [group-management, CCY-Pair, cashflow-grouping, enrichment]
related: [group-management-service, ccy-pair-based-nostro-selection, multi-entity-cash-settlement-compatibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md"]
---
# Group-Ready CCY Pair Enrichment

Group-ready `CCY Pair` enrichment is the proposed Option 1 mechanism in which the Group Management Service derives and adds a currency pair after a cashflow group is ready.

Enrichment requires an eligible booking entity, an eligible foreign-exchange product taxonomy, and exactly two payment currencies in the grouped cashflows. An incomplete group delivered manually may not contain enough information to derive the pair.

The source does not define the derivation algorithm, final message path, exception type, or replay behavior.