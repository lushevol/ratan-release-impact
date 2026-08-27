---
type: entity
title: FmrpOutboundMQ
created: 2026-08-24
updated: 2026-08-24
tags: [workflow-task, mq, fmrp, murex-211, outbound-integration]
related: [fmrp, fmrp-murex-211-settlement-workflow, fmrp-inbound-mq]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md"]
---

# FmrpOutboundMQ

`FmrpOutboundMQ` is the outbound MQ workflow task that publishes enriched FMRP payment messages after status synchronization and payment-context filtering.

## Configuration

| Field | Value |
|---|---|
| Host | `10.198.198.93` |
| Port | `8212` |
| Channel | `UKMXGCLNTS2` |
| Queue manager | `UKFM02S1` |
| Queue | `GM.MXG.MLS.FEDS.UAT` |
| User | `ukmxgmq` |

The queue name contains `MLS`, but the source does not establish whether this is legacy naming, shared infrastructure, or evidence of MLS ownership. Queue naming alone must not be used to merge FMRP and MLS system responsibilities.