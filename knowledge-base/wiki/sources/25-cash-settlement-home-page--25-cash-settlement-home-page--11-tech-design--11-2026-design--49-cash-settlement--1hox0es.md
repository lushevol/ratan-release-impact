---
type: source
title: "Cash Settlement Platform Architecture — Indonesia: Active-Active to Active-Passive"
authors: []
year: 2026
url: ""
venue: "Internal technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, indonesia, architecture, active-passive, active-active, disaster-recovery]
related: [cash-settlement-platform, cash-settlement-dc-failover-strategy, message-racing-prevention-in-dual-dc-deployments, deployment-profile, virtual-ip, cluster]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# Cash Settlement Platform Architecture — Indonesia: Active-Active to Active-Passive

## Summary

This internal technical-design note compares two deployment strategies for the Indonesia [[cash-settlement-platform]] across two data centres:

- **Option-1:** Maintain one deployment profile and use Virtual IP (VIP) switching.
- **Option-2:** Maintain two deployment profiles for two clusters with isolated data centres.

The note does not record an approved decision, implementation status, recovery objectives, or test evidence.

## Option-1: One Profile with VIP

Option-1 is described as a real Active-Passive model. Its stated benefits are:

1. Infrastructure switching is transparent to domain applications.
2. Only one deployment profile must be maintained.
3. The operating model is explicitly Active-Passive.

The stated constraints are:

1. Six servers in each cluster require six VIPs.
2. Application-to-infrastructure connectivity is available to only one data centre at a time.
3. Failover requires an ordered operational procedure:

   1. Stop primary data-centre applications.
   2. Check that all primary data-centre services are down.
   3. Switch the VIPs.
   4. Start backup data-centre applications.
   5. Check that all backup data-centre services are up.

This procedure makes verified shutdown of the primary data centre a prerequisite for starting the backup data centre.

## Option-2: Two Profiles for Two Clusters

Option-2 removes the need for additional VIPs and keeps the two data centres totally isolated. Its trade-offs are:

1. Two deployment profiles must be maintained separately.
2. The CD script must be revised so one CD deployment can support two profiles.
3. The design could operate as Active-Active, so startup of MB must be manually restricted to avoid message racing.

The note does not define MB, explain the message-processing topology, or specify a technical fencing mechanism.

## Comparison

| | Pros | Cons |
| --- | --- | --- |
| Option-1 | 1. Infra switch is transparent for domain applications 2. Only maintain 1 profile 3. Real Active-Passive model | 1. 6 servers for each cluster need 6 VIPs 2. Apps to infra connectivity is available to only 1 DC at same time, so switch step should be 1. Stop primary DC apps. 2. Check all primary DC services are down. 3. Switch VIPs. 4. Start backup DC apps. 5. Check all backup DC services are up. |
| Option-2 | 1. No additional VIPs required 2. Two DCs are totally isolated | 1. Need to maintain 2 profiles separately. 2. CD script needs to be revised to support 1 CD deploy 2 profiles. 3. Could be Active-Active, need to manual avoid message racing(MB startup should be restricted). |

## Limitations and Open Architecture Questions

The note does not specify:

- Recovery time objective (RTO) or recovery point objective (RPO).
- VIP ownership, routing, or failover implementation.
- Database, message broker, cache, file, or distributed-lock state replication.
- Message ordering, deduplication, retry, or in-flight transaction handling.
- Automated fencing or leader-election controls.
- Release consistency, rollback, or profile-drift controls for Option-2.
- The meaning of MB or the messages it processes.
- Approval, ownership, implementation date, or test evidence.

The distinction between network endpoint failover and safe stateful processing failover remains unresolved. See [[queries/which-indonesia-cash-settlement-deployment-strategy-is-approved]] and [[queries/what-is-mb-and-how-is-dual-dc-message-processing-fenced]].

## Relationship to Existing Cashflow Architecture

The deployment choices may affect cashflow event ordering, batch completeness, acknowledgements, and duplicate handling. However, this note does not name Murex, RATAN, FMRP, Solace, or any other specific settlement component. No platform-specific dependency should be inferred without additional evidence.
