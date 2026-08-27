---
type: entity
title: FMRP UBER
created: 2026-08-22
updated: 2026-08-22
tags: [fmrp, uber, routing, rules, trade-attributes]
related: [ratan, chg1016055, ratan-settlement-korea, rule-engine-trade-attributes, settlement-message-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# FMRP UBER

FMRP UBER is an integration and processing stream included in [[chg1016055]]. Its changes cross several architectural layers of [[ratan]].

## Release Scope

### Query and data exposure

[[51358-ratan-cash-settlement-query-service]] adds new FMRP fields and TIS query support.

### Netting and rule evaluation

[[ratan-cash-settlement-netting]] and [[ratan-rule-service]] add ten trade fields for rule checks. The source does not enumerate the names of all ten fields in text.

### Group management

[[51358-ratan-cash-settlement-group-management-service]] applies new fields according to Eco/Non eco amendment behavior and changes downstream routing.

### Database routing

[[51358-ratanone-db-repository]] configures UBER and SCBML flows and filters. The recorded intent is to enable UBER for consumers except LOANIQ while retaining the SCBML flow for LOANIQ.

### Frontend rules

`51358-mfe-rules` adjusts the hierarchy of FMRP UBER trade fields. PIT also checks that new trade attributes are available in filter, view, and rule builders.

## Validation

Production checks query `uber-flow` records and associated filters. The source includes expected-result screenshots but does not transcribe all returned route and filter values.

## Evidence Limits

The package-level evidence strongly supports implementation across services. It does not include a complete end-to-end business scenario demonstrating that query, rules, netting, grouping, routing, and frontend behavior interoperate successfully in production.