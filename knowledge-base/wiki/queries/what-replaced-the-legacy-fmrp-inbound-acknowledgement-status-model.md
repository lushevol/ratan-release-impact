---
type: query
title: What Replaced the Legacy FMRP Inbound Acknowledgement Status Model?
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, ratan, acknowledgement, cashflow-lifecycle, open-question]
related: [fmrp, scb-fmrp-dbf, fmrp-murex-cashflow-status-synchronization, ratan-murex-211-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md"]
---
# What Replaced the Legacy FMRP Inbound Acknowledgement Status Model?

RATAN-10822 explicitly deletes legacy acknowledgement components that validated `razorID`, checked record existence, and updated `SCB_FMRP_DBF` to `MATH`.

It creates the following replacement components:

- `client.scb.fmrp.inbound.inboundRouter`
- `client.scb.fmrp.inbound.payFlowID`
- `client.scb.fmrp.inbound.syncRelease`
- `client.scb.fmrp.inbound.processAck`
- `client.scb.fmrp.inbound.syncAck`
- `FmrpInboundRouter`
- `SNTR2RLSR`
- `FmrpAckProcessor`
- `FmrpReleaseProcessor`

The source does not provide their definitions, routing graph, validation rules, status transitions, or retry/error behavior.

Required evidence includes the RATAN-10822 implementation specification, formula exports, workflow configuration, and test evidence showing acknowledgement and release outcomes.