---
type: entity
title: VIP
created: 2026-08-25
updated: 2026-08-25
tags: [vip, virtual-ip, high-availability, ratan, disaster-recovery]
related: [ratan, wat, ark, redis-and-vip-failover, ratan-disaster-recovery-failover]
sources: ["RATAN/RATAN -Service Restart Guide/RATAN DR Plan.md"]
---
# VIP

VIP is the virtual IP used as a high-availability endpoint in the RATAN DR procedure. Operators must check its current running node and use the Rundeck `zk_vip_controller` job to roll it to the intended environment when required.

The WAT→ARK procedure expects the VIP on ARK before WAT-side application services are stopped. The ARK→WAT procedure similarly requires VIP preparation before recovery, but the source's node labels and final-state terminology are not sufficiently defined to establish a complete topology.