---
type: entity
title: Lifecycle Service
created: 2026-08-22
updated: 2026-08-23
tags: [application-service, cashflow-lifecycle, status-management, cashflow, lifecycle, service, settlement, cash-settlement, lifecycle-management, fixing-flag, reprocessing]
related: [netting-and-lifecycle-service-separation, ratan-cashflow-lifecycle-state-machine, stella, cash-settlement-home-page, netting-service, lifecycle-netting-responsibility-separation, scbml, batch-service, fixing-flag-notification-processing, fixing-notification-event-ordering, cashflow-reinstatement-and-replay]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting & Status Move Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting Process.md"]
---
# Lifecycle Service

## Role

The Cashflow Auto Netting refactor sources describe Lifecycle Service as the proposed application-service owner for generic cashflow lifecycle responsibilities. It owns the lifecycle of an individual cashflow from generation through completion.

Those refactor sources present Lifecycle Service as a responsibility boundary rather than confirmed evidence of a separately deployed component.

The fixing-flag notification technical design describes Lifecycle Service as the proposed component responsible for applying fixing-flag notifications to cashflows and coordinating subsequent lifecycle processing.

## Core Cashflow Lifecycle Responsibilities

According to the Cashflow Auto Netting refactor sources, Lifecycle Service is responsible for:

- `initializeCashflow`: generate a new cashflow Stella message event.
- Consume `Cash_Settlement_Orchestration_Process_In` and initialize the cashflow Stella message event.
- `updateStatus`: change a cashflow status from X to Y.

The Stella message event is described as the cashflow's main data and is used in every lifecycle state change.

## Fixing-Flag Notification Processing

According to the fixing-flag notification technical design, Lifecycle Service is responsible for:

1. Consuming fixing notifications published by batch service.
2. Persisting the original notification for batch and real-time processing.
3. Applying the notification's fixing flag to the cashflow.
4. Reverting eligible cashflows to `queued` for reprocessing.
5. Avoiding reprocessing of a cancelled cashflow.

### Cancellation Behavior

The fixing-flag notification design contains a tension between:

- An instruction to do nothing when a cashflow is cancelled.
- A withdrawal scenario requiring the latest fixing flag to remain visible in the GUI while the cashflow remains cancelled.

A safe but non-authoritative interpretation is that Lifecycle Service suppresses re-queueing and lifecycle transition for cancelled cashflows while still persisting the notification and updating fixing-flag or read-model data.

### Failure Recovery

The fixing-flag notification design states that a later fixing notification can trigger reinstatement of cashflows in `failed` or `techfailed` states. The eligibility criteria and whether both failure states follow the same path remain unspecified.

## Boundary with Netting Service

Lifecycle Service should maintain the individual cashflow lifecycle status. It should not own:

- Resultant-cashflow generation.
- Component/resultant relationship management.
- Netting-rule checks.
- Unnetting.
- Re-netting.
- Component-cashflow status management.

Under the proposed [[lifecycle-netting-responsibility-separation]], the newly generated Cashflow Auto Netting source assigns resultant-cashflow generation, component/resultant relationship management, netting-rule checks, and unnetting to [[netting-service]]. The existing Cashflow Auto Netting source additionally assigns re-netting and component-cashflow status management to [[netting-service]].

Lifecycle transitions can still trigger netting-related reactions through domain events. Consequently, direct implementation coupling may be reduced, but a semantic dependency remains through event contracts and status meanings.

## Open Contract Details

The Cashflow Auto Netting refactor sources do not provide the authoritative:

- Lifecycle transition matrix.
- API contract.
- Transaction boundary.
- Invalid-transition behavior.

The fixing-flag notification design does not define:

- Whether notification persistence and cashflow updates are transactional.
- Idempotency behavior.
- Retry behavior.
- Locking behavior.
- Duplicate-notification behavior.

## Related Pages

- ratan cashflow lifecycle state machine
- [[netting-and-lifecycle-service-separation]]
- [[lifecycle-netting-responsibility-separation]]
- stella
- [[netting-service]]
- batch service
- fixing flag notification processing
- fixing notification event ordering
- cashflow reinstatement and replay