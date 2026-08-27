---
type: source
title: RATAN KTLO Tracker
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_queries/query/dcbb9fba-5da6-40e8-bfff-9b6645a7e4c4/"
venue: Azure DevOps
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, ktlo, production-support, operational-resilience, azure-devops]
related: [ratan-transient-failure-recovery, ratan-operational-observability, ratan-disaster-recovery-automation, ratan-workflow-auditability, ratan-interface-inventory, ratan-interface-architecture, razor, stella]
sources: ["RATAN/RATAN -KTLO Tracker/RATAN -KTLO Tracker.md"]
---
# RATAN KTLO Tracker

## Summary

This operational tracker records production issues, support pain points, resilience work, observability gaps, disaster-recovery concerns, database performance risks, and operator usability issues for [[entities/ratan]]. It is a planning and issue-tracking artifact rather than a formal design specification or completed-delivery report.

The tracker identifies six priority areas:

1. Razor-response ordering and early-arrival failures, with associated manual cashflow replay.
2. Resilience to intermittent connectivity and technical-call timeouts.
3. Monitoring and interface-inventory gaps.
4. Disaster-recovery automation and Redis-outage handling.
5. Strategic-Flow custom-search database performance.
6. Operator-facing auditability for `RevertToQueued` events.

Most proposed solutions, owners, ETAs, target states, and acceptance criteria remain pending confirmation. Comments such as `29OCt` and `12Nov` do not identify a year.

## Operational Findings

### Razor-response failures and manual replay

The tracker reports that RATAN processing can fail when a Razor response arrives out of order or too quickly. STORY 8502031 concerns BCS cashflow `006226593174`, which was caught by a RATAN auto-fail job. The tracker reports approximately two BCS-related exception-replay tickets per week, with PSS informing and instructing Ops on manual replay.

Proposed remedies are automatic retry or replay, or an improved exception blotter that allows Ops to monitor and replay exceptions through self-service. GENERIC TASK 8565961 separately concerns a BCS/Strategic Flow failure to process an early Razor response. STORY 8881385 records a Strategic-Flow cashflow, `006522099847`, that could not be updated to `SETTELED` because of acknowledgement-related processing.

The tracker mentions discussion of a possible BCS Flow migration to Strategic Flow with a target of 2026. This is not presented as an approved migration plan and does not resolve the current BCS operational risk.

### Technical timeout resilience

STORY 6930146 attributes a technical-call timeout to network jitter and calls for more robust exception handling to avoid manual replay or reinstatement. Possible contributing areas include upstream systems, infrastructure, networks, and databases. The tracker states that the non-functional requirements for exception handling remain to be finalized.

GENERIC TASK 9095247 records continuing RATAN–STELLA API timeout exceptions, with PSS still required to inform users about manual replay.

### Monitoring and interface visibility

GENERIC TASK 10913098 states that current ITRS monitoring is missing or incomplete for:

1. Business-volume monitoring.
2. Interface-connectivity monitoring.
3. RATAN API-availability monitoring.
4. Throughput and processing-latency monitoring.
5. SLA and OLA commitment monitoring.

The stated objective is earlier detection of abnormalities. RATAN 2.0 is expected to be in scope, and knowledge-transfer sessions for Ratan Foundation 2.0 are reported as in progress.

GENERIC TASK 10829458 records PSS collection of RATAN upstream and downstream interface information. The intended outcome is a clear picture of RATAN-related interfaces and flows to improve support visibility and enable earlier issue detection. The tracker does not itself establish an authoritative inventory, ownership model, maintenance cadence, or criticality classification.

### Disaster recovery and Redis

GENERIC TASK 7991917 states that PSS must manually start a VIP on the required node during DR. The requested enhancement is intended to streamline the process and support a one-click DR test while meeting RATAN RTO and RPO objectives. The tracker provides no RTO/RPO values or validated test results.

STORY 6832041 requests automatic handling of Redis outages to avoid processing impact. The issue is linked to a DR incident and is expected to be addressed before the next DR exercise. Health-check information collection and further investigation involving Irisa, Nick, Dennis, and the network team are planned.

### Database performance

STORY 10841570 concerns a Strategic-Flow custom search that is slow or unable to return results. The tracker records one reported case but treats the issue as a potential broader database-performance risk requiring prioritised fine-tuning. No response-time measurements, query plan, load profile, or systemic-impact evidence is supplied.

### `RevertToQueued` auditability

GENERIC TASK 10062646 requests an audit comment when a cashflow is returned to the Maker queue through `RevertToQueued`. The listed triggers include Nostro refresh, Vostro refresh, and netting-rule updates. The tracker reports three to four requests since August and states that Ops cannot easily retrieve the required information from the UI.

The source does not establish whether `RevertToQueued` is a formal accounting status transition or a workflow action recorded in audit history.

## Work-Item Register

| Priority | ADO ticket | Description | Issue | Justification | comment on 29OCt | comment on 12Nov |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | STORY 8502031 | [<u>Story 8502031: [BCS Flow] 006226593174 was being caught by RATAN auto-fail job and keep sending it …</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8502031) | Ratan process fail as razor response return disorder or too quick ,need to check the impact for BCS flow as no migration plan, and fix if required | Around weekly 2 tickets for BCS related exception replay, PSS need to inform and instruct Ops on the replay. Either automate the replay or enhance the blotter for Ops to easily monitor and replay by self service would improve the efficiency and reduce turnaround time. | Nick to work with PO finalize the auto retry machanism, and provide timeline next week, auto replay. Liam: double check the business impact and whether the status write back can be skipped or not Nick to confirm the plan and ETA and update next week. | Nick mentioned there's discussion for BCS flow migrate to strategic flow, target 2026. |
| GENERIC TASK 8565961 | [<u>Generic Task 8565961: [BCS/Strategic Flow] Ratan can't process Razor response due to it comes befor…</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8565961) |
| STORY 8881385 | [<u>Story 8881385: [Strategic Flow] cashflow 006522099847 cannot be updated to “SETTELED” due to ack an…</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8881385) |
| GENERIC TASK 9095247 | [<u>Generic Task 9095247: [BCS/Strategic/Trade Control] RATAN STELLA api call timeout case summary</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9095247) | Still many exception and pending PSS to inform user manual replay |
| GENERIC TASK 7582056 | [<u>Generic Task 7582056: [PSS REQ] BCS cashflow settlement exception handling enhancement</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7582056) | Enhance exception blotter for user better usage, it's not user friendly and user is not monitoring nor know how to handle those exceptions |
| 2 | STORY 6930146 | [<u>Story 6930146: [Strategic Flow] Network jitter which caused a technical call timeout - enhance exce…</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6930146) | Exception handling machanism to be enhanced to avoid unhandled exception need manual replay/reinstate. | Improve RATAN exception handling machanism and make it more robust for intermittent connectivity issue with upstream or infra(network, DB etc) | NFR definition for exception handling to be finalized. | |
| 3 | [GENERIC TASK 10913098](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10913098) | [<u>Generic Task 10913098: ITRS Monitor enhancement request</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10913098) | Currently ITRS monitoring can't cover all aspects of monitoring requirements, below monitoring are still missing/incomplete: 1 business volume monitor 2 interface connectivity monitor 3 Ratan API availability monitor 4 throughput processing latency monitor 5 Monitor for SLA OLA commitment | ITRS monitoring to be enhanced to enable early detection of abnormality | RATAN 2.0 scope to be introduced, Nick to schedule a call next week | A series of KT session for Ratan foundation 2.0 in progress. |
| GENERIC TASK 10829458 | [<u>Generic Task 10829458: [TRADE] Check the interface information between Ratan and up/downstreams</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10829458) | PSS is collecting the interface information for Ratan | To give clear picture of all RATAN related interface and improve visibility of all the flows for support and enable issue early detection. |
| 4 | GENERIC TASK 7991917 | [<u>Generic Task 7991917: [Infra] one click DR</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7991917) | During DR, PSS needs to manually manage to start VIP on the required node which is not easy to manage. please help on the enhancement | To streamline the DR process and achieve one-click DR test ensure RATAN can do DR successfully without issue and meet the RTO, RPO. | prepare DR plan for: health check information collection Irisa to schedule another call with Nick, Dennis and network team to further explore on the issue | |
| [STORY 6832041](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6832041) | [<u>Story 6832041: [Infra] Exception handling - handle redis outage automatically avoid any processing …</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6832041) | Linked to issue faced during DR, and need to be addressed and avoided before next DR. |
| 5 | STORY 10841570 | [<u>Story 10841570: [Strategic Flow] DB Performance issue- custom search not able to return result from…</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10841570) | Slowness reported by user, fix need to be prioritized | 1 case reported, however this would be a risk for DB performance, to be fine tuned with priority. | Nick to check Geoffrey for ETA and confirm next week | |
| 6 | GENERIC TASK 10062646 | [<u>Generic Task 10062646: [PSS support]: Ratan Cashflow Push Back to Pending Operator-RevertToQueued</u>](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10062646) | Add comment for user easy reference and reduce user query: Cashflow was pushed back to Maker queue caused by Nostro refresh, similarly Vostro refresh, netting rule update would also trigger Action "RevertToQueued". As there's no comment in the audit history, user can't know the reason. | 3-4 request since Aug, while this shows the UI is not self-service for Ops and Ops can't easily get the required information from UI, which need to be enhanced. | Nick to confirm with PO ETA for enhancement and confirm next week | |

## Evidence Limitations

The tracker supports the existence of recurring operational problems, but it does not establish universal root causes, final designs, approved ownership, committed delivery dates, measurable acceptance criteria, RTO/RPO values, or completed implementation. The BCS and Strategic-Flow Razor examples should therefore be treated as related incidents, not automatically as one defect. Similarly, the STELLA, Redis, network, and database references identify possible failure domains rather than confirmed causes for every issue.

## Related Wiki Topics

- [[concepts/ratan-transient-failure-recovery]]
- [[concepts/ratan-operational-observability]]
- [[concepts/ratan-disaster-recovery-automation]]
- [[concepts/ratan-workflow-auditability]]
- [[concepts/ratan-interface-inventory]]
- [[concepts/ratan-interface-architecture]]
- [[entities/razor]]
- [[entities/stella]]
- [[sources/5-ratan--17-ratan-infra-copy--12-ratan-infra--li3x71]]