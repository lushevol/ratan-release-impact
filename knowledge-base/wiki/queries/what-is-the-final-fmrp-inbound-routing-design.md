---
type: query
title: What Is the Final FMRP Inbound Routing Design?
created: 2026-08-24
updated: 2026-08-24
tags: [query, fmrp, ratan, inbound-integration, workflow]
related: [fmrp-murex-211-settlement-workflow, ratan-cashflow-acknowledgement-and-release-processing, fmrp-inbound-mq]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md"]
---

# What Is the Final FMRP Inbound Routing Design?

## Question

Which inbound routing and processing task graph is authoritative: the initial `FmrpInboundMQ → FmrpAckRouter` design, or the later design using `FmrpInboundRouter`, `SNTR2RLSR`, `FmrpAckProcessor`, and `FmrpReleaseProcessor`?

## Evidence

The 2023-01-17 update explicitly deletes `FmrpAckRouter` and creates the later task set. The later design should be treated as the current candidate, but the deployed workflow definition and task links are not included in the source.

## Verification needed

Confirm the deployed Murex workflow configuration, the output labels from `FmrpInboundRouter`, and the role of `SNTR2RLSR` in acknowledgement and release processing.