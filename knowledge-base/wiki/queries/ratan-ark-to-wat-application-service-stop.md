---
type: query
title: Does RATAN ARK-to-WAT DR Require Application Service Stop?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, ark-to-wat, disaster-recovery, application-services, active-active, open-question]
related: [ratan, ratan-disaster-recovery-failover, redis-and-vip-failover, service-restart-runbook]
sources: ["RATAN/RATAN -Service Restart Guide/RATAN DR Plan.md"]
---
# Does RATAN ARK-to-WAT DR Require Application Service Stop?

## Question

During ARK→WAT DR, should RATAN application services be stopped on ARK, or does the active-active database architecture remove the need for an application service stop?

## Conflicting instructions

The runbook describes steps to stop services from ARK servers using `cluster_controller`. Elsewhere in the same ARK→WAT preparation step, it states that the RATAN database is active-active and therefore “no need to stop service,” while requiring Redis to run on WAT.

These statements may refer to different layers: database services versus RATAN application services. The source does not make that distinction explicit.

## Required evidence

Resolution should be based on the RATAN architecture record and a validated DR exercise. It should specify:

- Whether “service” means database services, RATAN application services, or both.
- Whether ARK application instances remain active during the transition.
- The required Redis and VIP states before any stop or start action.
- The rollback procedure if both sites advertise service ownership.
- The approval authority for deviating from the cluster-stop sequence.