---
type: entity
title: SCSTAR
created: 2026-08-23
updated: 2026-08-23
tags: [payment-processing, swift, settlement, integration]
related: [fmsre, swift-status-lifecycle-and-reconciliation, scpay]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# SCSTAR

SCSTAR is a downstream status label used in the MX/FMSRE event mapping of the FMRP SWIFT-generation requirement.

An AMH NACK is represented as `SCSTAR Error`, while an AMH ACK is represented as `Released by SCSTAR`. The source does not define SCSTAR’s relationship to [[scpay]], [[amh]], or FMSRE, and it should not be assumed to be equivalent to FMSGW-route status labels.