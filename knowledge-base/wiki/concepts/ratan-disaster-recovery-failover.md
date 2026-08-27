---
type: concept
title: RATAN Disaster Recovery Failover
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, disaster-recovery, failover, business-continuity, wat, ark]
related: [ratan, rundeck, redis-and-vip-failover, service-restart-runbook, application-health-check, dr-evidence-and-closure]
sources: ["RATAN/RATAN -Service Restart Guide/RATAN DR Plan.md"]
---
# RATAN Disaster Recovery Failover

## Definition

RATAN disaster recovery failover is the controlled transition of RATAN operations between the WAT and ARK environments. The [[ratan]] DR plan treats WAT→ARK and ARK→WAT as distinct procedures rather than interchangeable directions.

## Common control flow

Both directions include:

1. Pre-DR health validation.
2. Preparation of application infrastructure, including [[redis-and-vip-failover]].
3. Coordination with infrastructure teams through Group Chat.
4. Failover validation through Eureka, the FMO MFE GUI, ITRS, service monitoring, and transaction-failure indicators.
5. Network-isolation and network-reinstatement verification.
6. Application restart or recovery after DR, where required.
7. Evidence submission, Child CR closure, Confluence updates, and DR rebalance tracking.

The times in the source are rough SGT coordination points, not explicit service-level objectives.

## Directional differences

### WAT to ARK

The runbook requires Redis and the VIP to be placed on ARK, WAT-side application services to be stopped, and RATAN service placement to be checked through Eureka. After UVT, the whole application is restarted using Rundeck or Control-M.

This direction has a documented OpenSearch exception: if OpenSearch is started by a one-touch restart job and causes an issue, operators are instructed to stop it. Individual service restart jobs are the fallback when the whole-service restart fails.

### ARK to WAT

The runbook requires Redis to be running on WAT and includes ARK-side service preparation. It states that the RATAN database is active-active, so no service stop is needed for database reasons. However, the same procedure contains ARK cluster-stop instructions. This ambiguity is tracked in [[ratan-ark-to-wat-application-service-stop]].

ARK→WAT also depends on ETL squad confirmation of RATAN EOD before application status is reported. Sunday MLZ jobs must be held if the P node is not available because those jobs run only on that node.

## Health-validation layers

A failover is not complete merely because infrastructure has moved. The runbook calls for:

- Service placement checks in Eureka.
- GUI accessibility checks through FMO MFE.
- Green ITRS status for Solace, Kafka, service monitoring, and transaction failures.
- Node-specific health checks, although the meanings of A, B, P, and S are not defined.
- Communication of readiness and completion times in Group Chat.
- ETL/EOD confirmation for ARK→WAT.

The source does not define measurable pass/fail thresholds, required transaction tests, approvers, or rollback criteria.

## Governance closure

The operational sequence ends with TVT upload and Child CR closure in the GDC West DR Drill Portal, followed by DR rebalance status update at 21:00 Sunday. WAT→ARK additionally calls for a DR Confluence page update during post-network-reinstatement verification; ARK→WAT contains the same update requirement.

## Open implementation concerns

The authoritative mapping among WAT, ARK, `P`, `S`, `A`, and `B` remains unresolved. The source also does not identify owners for ETL/EOD confirmation, MLZ job hold and release, OpenSearch recovery, evidence upload, or Child CR closure. See [[authoritative-ratan-wat-ark-node-topology]].