---
type: entity
title: ARK
created: 2026-08-25
updated: 2026-08-25
tags: [ark, ratan, environment, disaster-recovery]
related: [ratan, wat, ratan-disaster-recovery-failover, redis-and-vip-failover]
sources: ["RATAN/RATAN -Service Restart Guide/RATAN DR Plan.md"]
---
# ARK

ARK is one of the two environments in the RATAN bidirectional disaster-recovery topology. It is the target environment for WAT→ARK failover and the source environment for ARK→WAT recovery.

The DR plan requires Redis and the VIP to be placed on ARK before WAT→ARK application failover. It also contains ARK-side service-preparation steps before ARK→WAT. The source does not define the authoritative relationship between ARK and the `P`, `S`, `A`, and `B` node labels.