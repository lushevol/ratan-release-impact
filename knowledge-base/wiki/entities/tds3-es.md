---
type: entity
title: TDS3 ES
created: 2026-08-23
updated: 2026-08-23
tags: [tds3, elasticsearch, trade-query, lien, integration]
related: [tds3, ratan, lien-driven-cashflow-nstp, can-tds3-es-support-per-cashflow-lien-lookups-at-ratan-volume]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration/RATAN Cashflow Process with Lien - Function Specs.md"]
---
# TDS3 ES

TDS3 ES is the Elasticsearch-backed trade-query interface that [[ratan]] is expected to call to retrieve the latest parent-trade lien information from [[tds3]].

The stated design performs one TDS3 ES query for each Murex cashflow, using the correlated original trade ID. The source projects about 50,000 daily cashflows but supplies no capacity evidence, service-level objective, batching design, caching policy, retry policy, or fallback behavior.

The source refers to latest-record querying but does not define a deterministic event-ordering or version-selection rule. See [[can-tds3-es-support-per-cashflow-lien-lookups-at-ratan-volume]].