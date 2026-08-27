---
type: source
title: RATAN DR Plan
authors: ["1514844", "Yunzhe Ta"]
year: 2026
url: ""
venue: "RATAN -Service Restart Guide"
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, disaster-recovery, failover, wat, ark, runbook]
related: [ratan, rundeck, ratan-disaster-recovery-failover, redis-and-vip-failover, service-restart-runbook, authoritative-ratan-wat-ark-node-topology, ratan-ark-to-wat-application-service-stop]
sources: ["RATAN/RATAN -Service Restart Guide/RATAN DR Plan.md"]
---

# RATAN DR Plan

## Summary

This document is an operational disaster-recovery runbook for moving RATAN between the WAT and ARK environments. It defines separate WAT→ARK and ARK→WAT sequences covering pre-DR health checks, Redis and VIP preparation, application service handling, infrastructure coordination, network-isolation and reinstatement validation, post-DR restart, evidence submission, and rebalance status.

The timings are explicitly described as rough SGT times and depend on confirmation in Group Chat that database, NAS, network, VM, and network-isolation activities have reached the required stage.

## Document control

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| 1514844 | 2026-03-02 | @Yunzhe Ta | 2026-04-09 | |

The source text states that the article status was updated to Published after review, but the displayed Status cell is blank.

## WAT to ARK

The documented sequence is:

1. Perform a pre-DR health check at approximately 22:30 on Saturday.
2. Before application DR, ensure that Redis and the VIP are running on ARK. Use `zk_vip_controller` to roll the VIP if required, stop the WAT-side application clusters with `cluster_controller`, and verify service placement through Eureka.
3. Confirm that Redis has failed over to ARK and report that the application is ready in Chat.
4. At approximately 04:00, after infrastructure completion is confirmed in Group Chat, validate that RATAN is running on ARK and report the failover completion time.
5. During post-network-isolation verification at approximately 07:45, check the FMO MFE GUI and confirm green ITRS status for Solace, Kafka, service monitoring, and transaction failures.
6. During post-network-reinstatement verification at approximately 10:05, perform another health check, report completion, and update the DR Confluence page.
7. After RATAN UVT completes, restart the whole application at approximately 10:30 using the Rundeck `cluster_controller` all-restart method or the Control-M `RAT_RESTART_ALL_SERVICES` job.
8. If OpenSearch is started by a one-touch restart job and causes an issue, stop it using the controlled `shell_command_windows` procedure. If the one-touch restart fails, contact the development team and use `service_restart_jobs` to restart services individually.
9. At approximately 11:30, upload TVT and close Child CRs in the GDC West DR Drill Portal.
10. At 21:00 on Sunday, update the DR rebalance status.

## ARK to WAT

The documented sequence is:

1. Perform a pre-DR health check at approximately 20:30 on Saturday.
2. Before application DR, check and, if necessary, roll the VIP using `zk_vip_controller`. Stop or otherwise prepare the ARK-side application clusters with `cluster_controller`, and verify service placement through Eureka.
3. Ensure that Redis is running on WAT. If the Redis master does not roll after the stop procedure, use the approved Rundeck recovery procedure.
4. The runbook states that the RATAN database is active-active and therefore does not need to be stopped for database reasons. It also contains instructions to stop ARK-side services, creating an ambiguity that requires architectural clarification.
5. Confirm RATAN EOD with the ETL squads before reporting that the application is ready or that failover is complete.
6. At approximately 04:00, after infrastructure completion is confirmed in Group Chat, verify RATAN on the active-active configuration and report the failover completion time.
7. During post-network-isolation verification at approximately 07:45, check the FMO MFE GUI and confirm green ITRS status for Solace, Kafka, service monitoring, and transaction failures.
8. During post-network-reinstatement verification at approximately 10:05, start the A node and perform a health check. Hold Sunday MLZ jobs if the P node is not available because those jobs run only on that node. Confirm RATAN EOD with the ETL squads, report completion, and update the DR Confluence page.
9. At approximately 11:30, upload TVT and close Child CRs in the GDC West DR Drill Portal.
10. After DR completion, run the Control-M `RAT_RESTART_ALL_SERVICES` job and repeat GUI and ITRS validation. No rough completion time is provided.
11. At 21:00 on Sunday, update the DR rebalance status.

## Operational job references

- [`Redis_slave_tkeover`](https://rundeckselfservice.global.standardchartered.com/selfservice/project/RATANRT/job/show/8088b502-df97-42d5-a432-ed999352cc6f): Redis role transition used in WAT→ARK preparation.
- [`zk_vip_controller`](https://rundeckselfservice.global.standardchartered.com/selfservice/project/RATANRT/job/show/1805c800-e9e7-46f0-81b7-6750b4afe899): VIP movement or rolling.
- [`cluster_controller`](https://rundeckselfservice.global.standardchartered.com/selfservice/project/RATANRT/job/show/71eacd2e-3163-46bc-8a2b-96fe2231cfee): Cluster stop and whole-service restart.
- [`service_restart_jobs`](https://rundeckselfservice.global.standardchartered.com/selfservice/project/RATANRT/job/show/7df689b6-a670-4a25-bbd3-df887390a374): Individual service restart fallback.
- [`shell_command_windows`](https://rundeckselfservice.global.standardchartered.com/selfservice/project/RATANRT/job/show/11911b9c-57fb-471d-acb4-9898b739818b): Controlled OpenSearch stop procedure.
- [Eureka](https://uklvapapp590.gdc.standardchartered.com:8763/): Service-placement validation.
- [FMO MFE](https://fmo-mfe.gdc.standardchartered.com:8453/login): GUI availability validation.
- [GDC West DR Drill Portal](https://teamsites.zone1.scb.net/sites/ITSCM-TestManagement-GDCWDR/Lists/2026%20H1H2%20GDCW%20PSS%20Nomination/AllItems.aspx): TVT upload and Child CR closure.
- [GDC West DR Rebalancing Portal](https://teamsites.zone1.scb.net/sites/ITSCM-TestManagement-GDCWDR/Lists/2026%20H1H2%20Rebalancing/AllItems.aspx): Rebalance status.

The source also contains a Redis CLI example with a plaintext credential. That credential and the production command are intentionally not reproduced here; operators should use the approved secret-management and access-control procedure.

## Limitations and unresolved risks

- The source does not define the mapping between WAT, ARK, and the labels `P`, `S`, `A`, and `B`.
- The relationship between named hosts such as `uklvapapp590` and `uklvasapp590` is not made explicit.
- “Healthy check,” green ITRS status, GUI accessibility, and transaction validation have no quantitative acceptance criteria.
- The ARK→WAT instructions appear to conflict on whether application services must be stopped.
- ETL/EOD confirmation, MLZ job hold and release, OpenSearch recovery, evidence upload, and Child CR closure have no named operational owner.
- Screenshots support the runbook but are not authoritative evidence of current state.
- The source documents operational intent and does not prove that each step was successfully executed.

## Verbatim runbook tables

### WAT to ARK

| DR Type | DR Step | Duty Shift | Rough Time SGT | Action (URL) | Screenshot | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| WAT -> ARK | Pre DR action | Sat Shift | 22:30 | | Screenshot in source | 1, healthy check |
| WAT -> ARK | Pre DR action for Application | Sat Shift | 1:00 | Rundeck `Redis_slave_tkeover`; Rundeck `zk_vip_controller` | Attachments in source | Check Redis and VIP placement; roll VIP if required; stop WAT services with `cluster_controller`; verify Eureka; fail over Redis to ARK; report readiness in Chat |
| WAT -> ARK | DR failover to ARK | Sat Shift | 4:00 | | | Confirm DB, NAS, Network, and VM failover in Group Chat; validate RATAN on ARK; report completion |
| WAT -> ARK | Post Network Isolation | Sat Shift | 7:45 | FMO MFE login | Attachment in source | Check GUI and green ITRS status for Solace, Kafka, service monitoring, and transaction failures |
| WAT -> ARK | Post Network Reinstatement | Sun | 10:05 | | | Validate RATAN on ARK, report completion, and update the DR Confluence page |
| WAT -> ARK | Once DR Completed | Sun | 10:30 | `cluster_controller` with `all_restart`, or Control-M `RAT_RESTART_ALL_SERVICES` | Attachment in source | Complete RATAN UVT first; stop OpenSearch if started by one-touch jobs; use individual restart jobs if required |
| WAT -> ARK | After DR action | Sun | 11:30 | GDC West DR Drill Portal | Attachments in source | Upload TVT and close Child CR |
| WAT -> ARK | DR Rebalance | Sun | 21:00 | GDC West DR Rebalancing Portal | Attachment in source | Update rebalance status |

### ARK to WAT

| DR Type | DR Step | Duty Shift | Rough Time SGT | Action (URL) | Screenshot | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| ARK-> WAT | Pre DR action | Sat | 20:30 | | Screenshot in source | 1, healthy check |
| ARK-> WAT | Pre DR action for Application | Sun | 1:00 | `zk_vip_controller`; `cluster_controller` | Attachments in source | Roll VIP if required; prepare ARK services; verify Eureka and Redis; ensure Redis is on WAT; confirm RATAN EOD with ETL squads |
| ARK-> WAT | DR failover to WAT | Sun | 4:00 | | | Confirm DB, NAS, Network, and VM failover in Group Chat; validate active-active RATAN; confirm EOD and report completion |
| ARK-> WAT | Post Network Isolation | Sun | 7:45 | FMO MFE login | Attachment in source | Check GUI and green ITRS status for Solace, Kafka, service monitoring, and transaction failures |
| ARK-> WAT | Post Network Reinstatement | Sun | 10:05 | Hold Sunday MLZ jobs if P node is unavailable | | Start A node; validate health; confirm EOD; report completion and update the DR Confluence page |
| ARK-> WAT | After DR action | Sun | 11:30 | GDC West DR Drill Portal | Attachments in source | Upload TVT and close Child CR |
| ARK → WAT | Once DR Completed | Sun | Not specified | Control-M `RAT_RESTART_ALL_SERVICES` | Attachment in source | Restart whole RATAN and repeat GUI and ITRS validation |
| ARK → WAT | DR Rebalance | Sun | 21:00 | GDC West DR Rebalancing Portal | Attachment in source | Update rebalance status |