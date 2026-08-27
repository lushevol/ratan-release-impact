---
type: concept
title: Redis and VIP Failover
created: 2026-08-25
updated: 2026-08-25
tags: [redis, vip, high-availability, ratan, disaster-recovery, failover]
related: [ratan, rundeck, ratan-disaster-recovery-failover, authoritative-ratan-wat-ark-node-topology]
sources: ["RATAN/RATAN -Service Restart Guide/RATAN DR Plan.md"]
---
# Redis and VIP Failover

## Definition

Redis and VIP failover is the coordinated movement and verification of the Redis master role and the virtual IP before RATAN application recovery. In the RATAN DR plan, these are operational gates for selecting the intended active environment.

## WAT to ARK

Before WAT→ARK application failover, operators are instructed to:

- Confirm that the VIP is running on ARK and roll it with `zk_vip_controller` if necessary.
- Stop the WAT-side application services with `cluster_controller`.
- Confirm through Eureka that service placement is as expected.
- Verify that Redis has failed over to ARK.

The source names `Redis_slave_tkeover` as a Rundeck job used in this preparation sequence.

## ARK to WAT

Before ARK→WAT failover, operators are instructed to check or roll the VIP and ensure that Redis is running on WAT. If the Redis master does not move after the stop procedure, the runbook directs operators to use the approved Rundeck recovery procedure.

The source describes RATAN DB as active-active in this direction, but Redis location remains an explicit dependency.

## Security boundary

The source includes a Redis CLI example containing a plaintext password. Credentials must not be copied into general wiki content. Any manual Redis verification or recovery should use an approved secret manager, privileged access path, and current production operating procedure.

## Unresolved topology

The runbook uses `P`, `S`, `A`, and `B` node labels without defining their relationship to WAT, ARK, or the named hosts. The expected Redis and VIP target state should therefore be confirmed against the authoritative topology before execution. See [[authoritative-ratan-wat-ark-node-topology]].