---
type: query
title: Which DEV and Production MQ Topology Is Authoritative for Murex-RATAN?
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, mq, topology, environment]
related: [murex-ratan-bidirectional-cashflow-integration, cn-settlement-murex-211-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# Which DEV and Production MQ Topology Is Authoritative for Murex-RATAN?

The technical design contains two DEV MQ descriptions:

- An earlier MLS/FEDS-oriented configuration using `GM.MXG.MLS.FEDS.UAT`, `GM.MXG.MLS.FEDSIN.UAT`, and `GMPCI.MLS.MXG.RQSTIN`, including a shared-FXDC testing dependency.
- A later configuration explicitly naming RATAN routes: `CF.MXG.RATAN.RQST` and `CF.RATAN.MXG.RESPIN`.

The source does not state whether the earlier configuration was retired, was an adaptor route, or represented a separate delivery phase. It also says that production would require new inbound and outbound MQs without identifying them.

## Evidence needed

- Approved DEV, UAT, and production MQ topology.
- Relationship between MLS/FEDS and `CF.*.RATAN.*` queues.
- Confirmation of whether the FXDC shared-MQ dependency remains applicable.
- Named operational owner and certificate/access-management model.