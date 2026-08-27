---
type: entity
title: CDU Lake
created: 2026-08-22
updated: 2026-08-23
tags: ["CDU-Lake", "trade-confirmation", "Murex", "Solace", "confirmation", "data-platform", "integration", "deprecated-evidence", "cdu", "stella", "ratan"]
related: ["solace", "cashflow-migration-readiness", "cdu", "cdu-exceptor", "cdu-ps", "ratan", "murex-2-11", "stella", "confirmation-status-normalization", "confirmation-source-routing", "what-is-the-current-authoritative-confirmation-status-to-stp-mapping-for-ratan", "what-is-the-authoritative-stella-cdu-cashflow-version-correlation-rule"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/01- Function Flow/Cashflow Migration Readiness.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Copy of Trade Confirmation & Cashflow STP - Deprecated.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Deprecated - Stella Market events & cashflow generation.md"]
---
# CDU Lake

CDU Lake is identified by the Cashflow Migration Readiness tracker as the location where Murex 2.11 trade-confirmation status is available.

Deprecated requirements describe CDU Lake as a consolidation and distribution layer for trade-confirmation statuses consumed by [[ratan]]. A separate deprecated Stella cashflow-generation requirement names CDU Lake as the component that sends trade-confirmation status to [[ratan]] after a [[cdu]] confirmation event.

## Migration-Relevant Role

According to the Cashflow Migration Readiness tracker, CDU Lake would assess the effort required to publish Murex 2.11 confirmation status to [[solace]].

The tracker states that paper confirmation is handled by [[cdu-ps]], while Swift confirmation is handled by CityNet.

The tracker does not confirm that publication to Solace was implemented or that the confirmation-status flow passed UAT.

## Historically Documented Inputs and Routing

The deprecated trade-confirmation requirement documents the following historical CDU Lake inputs:

- [[cdu-exceptor]] for Murex 2.11 paper confirmations.
- CitiNet, spelled `Citynet` in a preserved payload, for Murex 2.11 SWIFT confirmations.
- [[cdu-ps]] for Stella paper/SWIFT confirmations associated with [[fmrp]].

These deprecated-source input assignments are retained separately from the migration tracker’s statement that CDU PS handled paper confirmation and CityNet handled Swift confirmation.

The deprecated trade-confirmation requirement states that CDU Lake segregated Solace publication topics by:

- Source system
- Asset class
- Confirmation method
- `status-match` versus `status-oth` category

It describes Murex correlation as `Trade_ID` only and Stella correlation as `Trade_Id + Trade Major Version`.

## Stella Cashflow Tracking Versions

According to the separate deprecated Stella cashflow-generation requirement, confirmation messages sent through CDU Lake have tracking versions that differ from the tracking versions of the cashflows promoted to STP.

That document does not define whether CDU Lake is a system, message-distribution layer, datastore, or merely an informal name for a CDU integration path. Do not assume a direct tracking-version equality rule. See [[what-is-the-authoritative-stella-cdu-cashflow-version-correlation-rule]].

## Evidence Status

The consolidation, routing, correlation, topic-segregation, and Stella tracking-version details above are deprecated evidence. They do not establish the current CDU Lake schema, routing topology, status-to-STP contract, component classification, or an authoritative Stella CDU cashflow-version correlation rule.