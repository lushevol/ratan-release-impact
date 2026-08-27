---
type: comparison
title: Cash Settlement Cluster Topology Options
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cluster-topology, availability, infrastructure, operations]
related: [cash-settlement-shared-platform-architecture, foundation-service-mesh-platform, razor, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Platform - Co-development Guideline.md"]
---
# Cash Settlement Cluster Topology Options

The co-development guideline records two possible implementations of the shared FSM-aligned platform. It does not record a final topology decision.

| Option | Description | Benefits | Risks and open questions |
|---|---|---|---|
| Single shared cluster | Shared infrastructure, foundation services, and domain services run on one cluster | Simpler service placement and potentially simpler operational coordination | PSS ownership, failure-domain isolation, capacity management, and maintenance impact remain undefined |
| Split hosting | The Ratan VM cluster provides infrastructure services while Razor physical servers host domain services | Separates infrastructure hosting from domain-service hosting | VM patching downtime, physical-server hard reboots, cross-environment availability synchronization, and operational coordination |

## Assessment

The source establishes the options and their concerns but does not provide the evidence needed to choose between them. A decision should compare availability targets, patching procedures, disaster recovery, network dependencies, capacity, ownership, monitoring, and failure isolation.