---
type: concept
title: Settlement Message Routing
created: 2026-08-22
updated: 2026-08-22
tags: [routing, filtering, cash-settlement, messaging]
related: [ratan, fmrp-uber, swift-mt-mx-integration, 51358-ratan-cash-settlement-group-management-service, 51358-ratanone-db-repository]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# Settlement Message Routing

Settlement message routing directs cashflow, confirmation, and integration events to topics, systems, or consumers according to configured flows and filters.

## RATAN Routing Evidence

[[chg1016055]] changes routing across:

- UBER flows and filters.
- SCBML flows and filters.
- LOANIQ-specific handling.
- Murex Korea ACK processing.
- ENISIS MT/MX ingress and egress.
- Group-management consumer selection.

## FMRP UBER Intent

The database scope records an intent to make UBER available to consumers except LOANIQ and retain SCBML for LOANIQ. Group-management wording also references LOANIQ and Murex consumer handling.

These statements should be validated against actual `ratan_bridge_flow` and `ratan_bridge_filter` records because the source does not transcribe the complete production query results.