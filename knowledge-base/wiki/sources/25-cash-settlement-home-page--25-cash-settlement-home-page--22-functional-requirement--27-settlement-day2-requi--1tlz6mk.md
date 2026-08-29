---
type: source
title: Cashflow Auto Netting — Refactor Netting Process
authors: []
year: 2025
url: ""
venue: Internal functional requirement
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-auto-netting, netting-service, lifecycle-service, refactoring, settlement-day-2]
related: [lifecycle-service, lifecycle-netting-responsibility-separation, event-driven-component-cashflow-status-management, cashflow-netting-renetting, resultant-cashflow-status-consistency, canonical-unnet-lifecycle, netting-service, cashflow-auto-netting, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting Process.md"]
---
# Cashflow Auto Netting — Refactor Netting Process

This functional requirement proposes separating generic cashflow lifecycle processing from cashflow-netting behavior. It identifies the current update-status API as a large transaction that embeds unrelated business logic, including resultant-cashflow generation, and reports production issues caused by long execution time.

The proposal assigns lifecycle transitions and Stella event initialization to [[lifecycle-service]], while [[netting-service]] owns netting relationships, resultant-cashflow generation, component status management, rule checks, unnetting, and recovery re-netting.

## Current Netting Flow

The source describes the current logical sequence as:

1. Prepare a cashflow net request.
2. Update cashflow statuses.
3. Save the cashflow net request.

It states that resultant cashflows are generated inside the update cashflow status API. To make a resultant cashflow flow, SCBML is published to the `Cash_Settlement_Orchestration_Process_In` topic to activate the workflow.

A resultant cashflow is formed by combining two or more component cashflows. As the resultant progresses to settlement, its component cashflows stop flowing: their status becomes `netted` and does not subsequently change under the described normal flow.

## Proposed Service Responsibilities

| Service | Responsibility | Comment |
| --- | --- | --- |
| lifecycle service | 1. initialize cashflow stella message event ( when consuming the topic Cash_Settlement_Orchestration_Process_In message） 2. maintain cashflow status (change the cashflow's status from X to Y) | 1. lifecycle means one cashflow from generation to completion (0→1, 1→ 100) 2. the stella message event is the cashflow main data. in other words, it is used in every state change. |
| netting service | All cashflow net logic. 1. net 2. unnet 3. manage the component cashflow status (if need) 4. net rule check 5. renet 6. ..... | It's the entry point of the cashflow netting because it manages the relationship between resultant and component cashflow, |

## Proposed APIs

| Service | Function | Responsibility | Comment |
| --- | --- | --- | --- |
| Lifecycle Service | updateStatus | change the cashflow's status from X to Y | |
| initializeCashflow | generate a new cashflow stella message event. | |
| Netting Service | net | 1. net cashflow to generate a resultant cashflow 2. update component cashflow's status | manual and auto netting. |
| unnet | 1. unnet a resultant cashflow 2. update component cashflow's status | manual unnet. |
| manageComponentCashflowStatus | consume domain event to update component cashflow's status if need | when the resultant cashflow's status is changed released/settled. topic: cash_settlement_cashflow_domain_events |
| netRuleCheck | check one cashflow is matched netting rules or not. | |
| renet | find uncompleted cashflow net requests to re-generate resultant cashflow | |

## Design Direction

The proposed update-status API uses the principle that different actions have different behavior (“template mode”). The intent is to make action paths clear, understandable, and easier to maintain, rather than requiring developers to understand the complete status-update flow for every transition.

The source cites SRP, OCP, KISS, DIP, and LKP as principles not adequately followed by the current API. The central operational recommendation is captured in [[lifecycle-netting-responsibility-separation]].

## Event-Driven Component Status Updates

`manageComponentCashflowStatus` is proposed as a Netting Service operation that consumes `cash_settlement_cashflow_domain_events`. It updates component cashflow status where necessary when the resultant cashflow changes to `released` or `settled`.

The source does not define the event schema, delivery semantics, idempotency, ordering, retries, dead-letter handling, or recovery process for failed component updates. These are material implementation concerns documented in [[event-driven-component-cashflow-status-management]] and resultant cashflow status consistency.

## Roadmap

| date | content | comment |
| --- | --- | --- |
| 2025.5 | analysis+redefine+implement Net/NetNew/RevertToQueue action | |
| 2025.6 | implement most of action except new/withdrawal action | |
| 2025.7 | implement new/withdrawal action think how to support uber? | |
| 2025.8 | migrate some action to new api | |
| 2025.9 | migrate other actions to new api | migrate done. all actions use new implemention. |
| 2025.10 | adaptor cash settlement | |
| | | |

This is a planned roadmap, not evidence that implementation or migration was completed.

## Open Questions Recorded by the Source

1. Why is generating a resultant cashflow after updating cashflow status?
2. Can generating a resultant cashflow is before updating cashflow status?
3. How to unet resultant cashflow?

These questions are tracked in resultant cashflow status consistency and canonical unnet lifecycle.