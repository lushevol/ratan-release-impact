---
type: query
title: Is client.scb.fmrp.inbound.razorID a Stale or Missing Formula?
created: 2026-08-24
updated: 2026-08-24
tags: [FMRP, inbound, RATAN, Murex-formula, configuration]
related: [fmrp, murex-ratan-cashflow-message-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change.md"]
---
# Is `client.scb.fmrp.inbound.razorID` a Stale or Missing Formula?

The `FmrpInboundMQ` metadata maps `STPDOC_DATA_TYPE2` to `client.scb.fmrp.inbound.razorID`, but the supplied formula definitions include `client.scb.fmrp.inbound.ratanID`, `murexID`, and `payFlowID`, not `razorID`.

The mapping may be a stale name, a typographical error, or a dependency omitted from the source. The deployed MQ task and the intended per-flow correlation field should be checked.