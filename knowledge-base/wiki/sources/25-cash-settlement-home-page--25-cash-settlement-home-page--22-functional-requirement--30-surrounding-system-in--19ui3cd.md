---
type: source
title: CN Settlement - Murex 2.11 Delivery Plan
authors: []
year: 2023
url: ""
venue: Internal delivery plan
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, china-settlement, delivery-plan, cashflow-integration]
related: [cn-settlement-murex-211-integration, murex-ratan-bidirectional-cashflow-integration, china-cashflow-payment-stp-exclusion, murex-ratan-cashflow-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 Delivery Plan.md"]
---
# CN Settlement - Murex 2.11 Delivery Plan

## Scope and evidentiary status

This internal plan sets out intended Q4 and Q1 2023 delivery work for China settlement integration between [[murex-211]] and [[ratan]]. It is evidence of planned scope, sequencing, dependencies, and estimated capacity. It does not demonstrate that any work item was implemented, successfully tested, approved for go-live, or deployed to production.

The intended integration includes Murex cashflow publication to RATAN, status synchronization through a staging table, and Murex consumption of RATAN ACK and Release messages. See [[murex-ratan-bidirectional-cashflow-integration]].

## Delivery-plan task register

| # | Task Type | Task Desc | Completion | Capacity | In Backlog | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Analysis | Murex Integration Strategy | Q4 - Sprint13 | 8 | Y | |
| 2 | Control-m | Cashflow auto publish into RATAN - Control-m Schedulers | Q4 - Sprint13 | 5 | Y | Depends on user input on job frequency. |
| 3 | Functional | Cashflow auto publish into RATAN - New Payment Queues + Processing Script | Q4 - Sprint14 | 5 | Y | |
| 4 | Analysis | Accounting Impact Analysis for cashflow remaining/returned in Murex | Q4 - Sprint14 | 2 | Y | |
| 5 | Script | Cashflow auto publish into RATAN - Store Procedure Capture cashflow into staging table + MSRB | Q4 - Sprint15 + Sprint16 | 8 | Y | |
| 6 | Analysis | Murex Integration Strategy Aligning to New Scope | Q4 - Sprint15 | 5 | Y | |
| 7 | Script | Exclude China Cashflow from Murex2.11 Payment STP | Q4 - Sprint15 | 3 | Y | |
| 8 | SIT | SIT - Murex outbound workflow to RATAN. (with Ratan?) | Q4 - Sprint16-17 (Till 10-Jan) | 5 | [RATAN-10651](https://jira.global.standardchartered.com/browse/RATAN-10651) | |
| 9 | Functional | Murex Send Cashflow to RATAN with Revised Technical Design | Q4 - Sprint16-17 | 10 | [RATAN-10649](https://jira.global.standardchartered.com/browse/RATAN-10649) | |
| 10 | Workflow | Dev MQ connectivity for inbound & outbound | Q4 - Sprint14 | 5 | Y | Require 2 set of MQ for Dev but only one is applicable |
| 11 | Workflow | Workflow enhancement - distribute message to RATAN + sync flow status in staging table | Q4 - Sprint14 + Sprint15 | 10 | Y | |
| 12 | Workflow | Enrich Extra Tag into cashflow for RATAN consume | Q4 - Sprint16 | 5 | [RATAN-10656](https://jira.global.standardchartered.com/browse/RATAN-10656) | |
| 13 | Analysis | RATAN to process amendment flow sourcing from Murex | by Q4 | 8 | [RATAN-10821](https://jira.global.standardchartered.com/browse/RATAN-10821) | by Q4 we have completed design for common case. SN7 would need further testing to reproduce each of trade amendment steps, RATAN side would start with the common case first. |
| 14 |  |  |  |  |  |  |
| 15 | Workflow | Murex consume ACK from RATAN. | Q1 2023-Sprint 1 | 5 | [RATAN-10822](https://jira.global.standardchartered.com/browse/RATAN-10822) | |
| 16 | Workflow | Murex consume Release message from RATAN. | Q1 2023-Sprint 2 | 5 | [RATAN-11254](https://jira.global.standardchartered.com/browse/RATAN-11254) | |
| 17 | Script | Exclude China Cashflow from Murex2.11 Payment STP | Q1 2023-Sprint 1 | 3 | [RATAN-10678](https://jira.global.standardchartered.com/browse/RATAN-10678) | |
| 18 | Functional | Disable/Exclude China Cashflow from BAU payment queue. | Q1 2023 | 5 | RATAN-10367 | |
| 19 | Analysis | MX2.11 / RATAN feeds to LMS | Q1 2023-Sprint 1,2,3,4 | 5 | RATAN-10785 | |
| 20 | Functional | Monitor screen/Report for settlement user | Q1 2023-Sprint 1 | 6 | [RATAN-11047](https://jira.global.standardchartered.com/browse/RATAN-11047) | |
| 21 | Functional | Murex Cashflow Realtime Recon with RATAN | Q1 2023-Sprint 2 | 5 | [RATAN-11055](https://jira.global.standardchartered.com/browse/RATAN-11055) | |
| 22 | Solutioning | Murex MSRB presentation | Q1 2023-Sprint 3 | 3 | [RATAN-11059](https://jira.global.standardchartered.com/browse/RATAN-11059) | |
| 23 | Analysis | Murex STP exception analysis | Q1 2023-Sprint 3 | 7 | [RATAN-10666](https://jira.global.standardchartered.com/browse/RATAN-10666) | |
| 24 | Solutioning | Technical Exception handling Analysis |  | 6 | RATAN-11275 | |
| 25 | Testing | Murex inbound + outbound integration test - reverse ACK functional test 6 - reverse RELEASE functional test 6 - E2E SIT with RATAN 20 | Q1 2023-Sprint 2,3,4 | 25 | RATAN-11281 [RATAN-11569](https://jira.global.standardchartered.com/browse/RATAN-11569) | |
| 26 | Testing | SIT test pack design. |  |  | [RATAN-11571](https://jira.global.standardchartered.com/browse/RATAN-11571) | |
| 27 | Functional | Enable FMO Hard Block for CPN RLSD | Q1 2023-Sprint 3 | 8 | [RATAN-11414](https://jira.global.standardchartered.com/browse/RATAN-11414) | |
| 28 | Analysis | Analyze Murex market operation impacting cashflow to RATAN | Q1 2023-Sprint 3 | 8 | [RATAN-11415](https://jira.global.standardchartered.com/browse/RATAN-11415) | |
| 29 | Solutioning | DPS Approval for Murex Integration Go live go live | Q1 2023-Sprint 4,5,6,7 | 20 | [RATAN-11570](https://jira.global.standardchartered.com/browse/RATAN-11570) | |
| 30 | Testing | Murex UAT test pack design | Q1 2023-Sprint 4 | 3 |  | |
| 31 | Solutioning | Murex Cashflow Migration | Q1 2023 |  |  | To be agreed when closed to go live |
| 32 | Reporting | Exclude accounting population from murex to Aspire & EBBS | Q1 2023 |  |  | Depends on Razor accounting design |
| 33 | Reporting | Accounting entries posting to CPN suspense for TLM recon | Q1 2023 |  |  | Depends on Razor accounting design |
| 34 | Workflow | Workflow Optimization Analysis | Q1 2023 |  |  | Depends on MSRB condition |
| 35 | Workflow | Workflow Optimization Dev | Q1 2023 |  |  | Depends on MSRB condition |

## Planning observations

- The plan allocates scheduled publication, queues, scripts, stored procedures, staging, and workflow distribution to the Murex-to-RATAN outbound path.
- Inbound work is planned for Murex consumption of RATAN ACK and Release messages; payload schemas, correlation rules, and state effects are not specified.
- China cashflows are planned to be excluded from both `Murex2.11 Payment STP` and the BAU payment queue. The plan repeats the Payment STP exclusion in Tasks 7 and 17 without explaining the distinction.
- RATAN amendment processing was planned to begin with a common case. `SN7` required further testing to reproduce each trade-amendment step.
- Reporting and accounting work involving [[razor]] and [[ebbs]] is contingent on Razor accounting design. Workflow optimization is contingent on an unspecified MSRB condition.
- Several planned activities have no stated completion period or capacity, including technical exception analysis, SIT test-pack design, cashflow migration, accounting reporting work, and workflow optimization development.
- The `In Backlog` column mixes `Y`, Jira references, blank values, and an unlinked Jira key. It should not be interpreted as a consistent Boolean status.

## Related investigation

- [[what-is-the-final-china-cashflow-exclusion-rule-for-murex-211-payment-stp]]
- [[what-are-the-murex-ratan-ack-and-release-message-contracts]]
- [[what-does-sn7-mean-and-which-murex-amendment-scenarios-remain-unsupported]]
- [[what-is-the-development-mq-topology-for-murex-ratan-inbound-and-outbound-connectivity]]