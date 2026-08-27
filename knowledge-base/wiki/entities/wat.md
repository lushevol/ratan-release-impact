---
type: entity
title: WAT
created: 2026-08-25
updated: 2026-08-25
tags: [wat, ratan, environment, disaster-recovery]
related: [ratan, ark, ratan-disaster-recovery-failover, redis-and-vip-failover]
sources: ["RATAN/RATAN -Service Restart Guide/RATAN DR Plan.md"]
---
# WAT

WAT is one of the two environments in the RATAN bidirectional disaster-recovery topology. It is the source environment for WAT→ARK failover and the target environment for ARK→WAT recovery.

The DR plan requires WAT-side application services to be stopped during WAT→ARK preparation and requires Redis to be running on WAT before ARK→WAT failover. The document also refers to WAT targets and hosts, but does not define the complete mapping between WAT and the `P`, `S`, `A`, and `B` node labels.