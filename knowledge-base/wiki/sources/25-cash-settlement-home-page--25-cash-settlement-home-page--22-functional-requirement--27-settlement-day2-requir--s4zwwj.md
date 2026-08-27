---
type: source
title: "Cashflow Auto Netting — Refactor Netting and Status Move Process"
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page — Functional Requirement"
tags: [cashflow-auto-netting, service-refactoring, lifecycle-management, netting]
related: [cashflow-auto-netting, netting-and-lifecycle-service-separation, event-driven-component-cashflow-status-management, lifecycle-service, netting-service, stella, netting-resultant-cashflow, netting-un-net-lifecycle, pending-auto-netting-state, ratan-cashflow-lifecycle-state-machine]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting & Status Move Process.md"]
---
# Cashflow Auto Netting — Refactor Netting and Status Move Process

## Summary

This functional requirement proposes refactoring the Cashflow Auto Netting and cashflow-status-update process. The stated drivers are high API-performance requirements, a complex update-status API containing business logic unrelated to status changes, production issues associated with long execution times, and the resulting maintenance and regression burden.

The proposal separates individual cashflow lifecycle management from netting orchestration:

- [[lifecycle-service]] owns cashflow initialization and individual cashflow status transitions.
- [[netting-service]] owns netting, unnetting, resultant-cashflow generation, component-cashflow status management, netting-rule checks, and re-netting.
- Component-cashflow status updates may be handled through the `cash_settlement_cashflow_domain_events` domain-event flow.

The source is an architectural proposal. It does not include the referenced current and target service-invocation diagrams, netting sequence diagrams, current status-update process, proposed net sequence, or detailed new API definitions. Therefore, transaction boundaries, state-transition semantics, event choreography, idempotency, retry behavior, and performance improvements remain unverified.

## Cashflow Netting Model

A user combines two or more cashflows to generate a new cashflow called a resultant cashflow. The combined cashflows are component cashflows.

The resultant cashflow continues through the lifecycle until settlement. The component cashflows stop flowing independently after successful netting; their status is updated to `netted` and does not change further according to the source description.

This relationship is central to [[concepts/netting-resultant-cashflow]] and [[concepts/netting-un-net-lifecycle]].

## Problems Identified in the Existing API

The source describes the existing update cashflow status API as having:

1. Multiple business-logic steps beyond status maintenance.
2. A potentially large transaction containing operations that may not require a single transaction.
3. Logic that requires developers to inspect the complete implementation to understand a single X → Y status transition.
4. Broad regression-testing requirements when changing or adding logic.
5. Resultant-cashflow generation embedded in cashflow status updates.

The source questions whether generating a resultant cashflow during a generic status update is an appropriate responsibility. It uses software design principles including SRP, OCP, KISS, DIP, and the Least Knowledge Principle to motivate separation of concerns.

No latency baseline, throughput target, transaction-duration measurement, error rate, or post-refactoring benchmark is provided.

## Proposed Service Responsibilities

### Lifecycle Service

1. Initialize the cashflow Stella message event when consuming a `Cash_Settlement_Orchestration_Process_In` message.
2. Maintain the cashflow status by changing it from X to Y.

The source describes the Stella message event as the cashflow's main data and states that it is used in every state change. This proposed ownership boundary relates to [[concepts/ratan-cashflow-lifecycle-state-machine]] and [[entities/stella]].

### Netting Service

The source assigns the following responsibilities to the Netting Service:

1. Net cashflows and generate a resultant cashflow.
2. Update component-cashflow status.
3. Unnet a resultant cashflow and update component-cashflow status.
4. Consume domain events to manage component-cashflow status.
5. Check whether a cashflow matches netting rules.
6. Find incomplete cashflow net requests and regenerate resultant cashflows.

The Netting Service is described as the entry point for cashflow netting because it manages the relationship between resultant and component cashflows.

## Proposed APIs

| Service | Function | Responsibility | Comment |
| --- | --- | --- | --- |
| Lifecycle Service | `updateStatus` | Change the cashflow's status from X to Y |  |
| Lifecycle Service | `initializeCashflow` | Generate a new cashflow Stella message event |  |
| Netting Service | `net` | 1. Net cashflow to generate a resultant cashflow<br>2. Update component cashflow's status | Manual and auto netting |
| Netting Service | `unnet` | 1. Unnet a resultant cashflow<br>2. Update component cashflow's status | Manual unnet |
| Netting Service | `manageComponentCashflowStatus` | Consume a domain event to update component cashflow's status if needed | Resultant status `released`/`settled`; topic: `cash_settlement_cashflow_domain_events` |
| Netting Service | `netRuleCheck` | Check whether one cashflow matches netting rules |  |
| Netting Service | `renet` | Find uncompleted cashflow net requests and regenerate resultant cashflow |  |

The final status-update API is proposed to use action-specific behavior in a template mode, because different actions have different behavior. The source does not provide the templates or their detailed contracts.

## Domain-Event-Driven Component Status Management

The proposed `manageComponentCashflowStatus` function consumes the `cash_settlement_cashflow_domain_events` topic and updates component-cashflow status when the resultant cashflow status changes to `released` or `settled`.

This may reduce synchronous work in the primary status-update API, but the source does not define:

- Event payloads or schemas.
- Delivery guarantees.
- Ordering requirements.
- Retry and dead-letter behavior.
- Deduplication or idempotency rules.
- Replay procedures.
- The required consistency relationship between resultant and component cashflows.

See [[concepts/event-driven-component-cashflow-status-management]].

## Roadmap

```text
2025.5: analysis+redefine+implement Net/NetNew/RevertToQueue action
2025.6: implement most of action except new/withdrawal action
2025.7: implement new/withdrawal action and support uber
2025.8: migrate some actions to the new api and uber function completed
2025.9: migrate other actions to new api
```

The source describes the 2025.9 milestone as migration completion, with all actions using the new implementation. This document alone does not verify whether any milestone was delivered.

## Evidence Gaps and Open Risks

The following evidence is absent from the source:

- Current and target service-invocation relationships.
- Current and proposed netting sequence diagrams.
- Detailed current status-update process.
- New API contracts and error semantics.
- Authoritative status-transition matrix.
- Transaction boundaries and consistency guarantees.
- Failure compensation when resultant creation and component updates diverge.
- Idempotency and duplicate-prevention rules for `net` and `renet`.
- Event retry, replay, ordering, and deduplication behavior.
- Production rollout status and quantitative performance results.

The proposed Netting Service also remains broad, combining orchestration, reversal, rule evaluation, recovery, and event-driven status synchronization. Further decomposition may be needed if these responsibilities evolve independently.

## Related Wiki Pages

- [[concepts/cashflow-auto-netting]]
- [[concepts/netting-and-lifecycle-service-separation]]
- [[concepts/event-driven-component-cashflow-status-management]]
- [[concepts/netting-resultant-cashflow]]
- [[concepts/netting-un-net-lifecycle]]
- [[concepts/pending-auto-netting-state]]
- [[concepts/ratan-cashflow-lifecycle-state-machine]]
- [[entities/lifecycle-service]]
- [[entities/netting-service]]
- [[entities/stella]]