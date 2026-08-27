---
type: query
title: Are SCPAY, SCSTAR, and AMH Statuses Equivalent Across SWIFT Integration Routes?
created: 2026-08-23
updated: 2026-08-23
tags: [swift, status-mapping, scpay, scstar, amh]
related: [swift-status-lifecycle-and-reconciliation, scpay, scstar, amh, fmswiftgateway, fmsre, enisis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# Are SCPAY, SCSTAR, and AMH Statuses Equivalent Across SWIFT Integration Routes?

## Question

What is the canonical relationship among FMSGW/AMH/SCPAY, MX/FMSRE/SCSTAR, and ENISIS/SAA/AMH status labels?

## Evidence

The FMSGW route maps AMH ACK/NACK to `Released by AMH` and `AMH Error`; a high-level table also uses `SCPAY Processed` and `SCPAY Error`. The MX/FMSRE table uses `Released by SCSTAR` and `SCSTAR Error`, while ENISIS describes business outcomes from SAA/AMH.

## Required resolution

The integration contract should establish system ownership, business-event equivalence, status precedence, and whether these labels are route-specific aliases or distinct downstream outcomes.